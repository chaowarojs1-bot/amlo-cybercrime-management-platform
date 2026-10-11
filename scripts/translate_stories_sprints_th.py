#!/usr/bin/env python3
"""แปล GitHub Issues: User Stories 75 และ Sprint Trackers 17 รายการเป็นภาษาไทย

อ่านข้อมูลฉบับสำรองที่ตรวจสอบแล้วและพจนานุกรมคำแปลที่ทบทวนเป็นรายงาน
โหมด validate ไม่แก้ไขข้อมูล; โหมด apply แก้เฉพาะ title/body ของ Issues ที่ยังไม่มีคำแปล
ไม่แก้ state, labels, assignees, milestone, Project custom fields หรือเลข Issue
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
REPO="chaowarojs1-bot/amlo-cybercrime-management-platform"
BASE="https://github.com/"+REPO
SNAPSHOT=ROOT/"project-management/migration/planner_issue_snapshot_2026-10-11.jsonl"
TRANS=ROOT/"project-management/translation"
COMMON_DOD="ผ่านเกณฑ์งานเสร็จร่วมของทีม พร้อมหลักฐานการทดสอบและการทบทวนที่เหมาะสม โดยไม่เปิดเผยข้อมูลอ่อนไหวในคลังสาธารณะ"
GOV_DOD="มีการอ้างอิงหลักฐานข้อตกลงจากพื้นที่ที่ได้รับอนุญาตและควบคุมสิทธิ์อย่างเหมาะสม"
TAGS={"A":"ระบบพื้นฐานและเชื่อมโยงข้อมูล","B":"การวิเคราะห์ธุรกรรมและกราฟ","C":"ระบบบริหารจัดการคดี","D":"การยื่นคำร้องและการคืนทรัพย์สิน","E":"ระบบบริการข้อมูลและรายงาน","Shared":"งานสนับสนุนร่วม","Cross-team":"งานข้ามสายงาน","Governance":"การกำกับการดำเนินงาน"}
REPO_LINK=BASE+"/blob/main/project-management/"

def call(path,method="GET",data=None):
    token=os.getenv("GITHUB_TOKEN")
    if not token:raise RuntimeError("ไม่พบ GITHUB_TOKEN")
    body=json.dumps(data,ensure_ascii=False).encode("utf-8") if data is not None else None
    headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
             "X-GitHub-Api-Version":"2022-11-28","User-Agent":"AMLO-Thai-Translation"}
    if body is not None:headers["Content-Type"]="application/json"
    req=Request("https://api.github.com"+path,headers=headers,data=body,method=method)
    for attempt in range(4):
        try:
            with urlopen(req,timeout=50) as response:return json.load(response)
        except HTTPError as error:
            if error.code in (403,429,500,502,503,504) and attempt<3:
                time.sleep(2**attempt+1)
                continue
            raise RuntimeError("GitHub HTTP "+str(error.code)+" สำหรับ "+path+" "+error.read(350).decode("utf-8","replace"))
    raise RuntimeError("GitHub API ไม่ตอบสนอง")

def data():
    issues=[json.loads(row) for row in SNAPSHOT.read_text(encoding="utf-8").splitlines() if row.strip()]
    issue_map={i["number"]:i for i in issues}
    stories={}
    for path in ["user_story_th_part1.json","user_story_th_part2.json"]:
        translations=json.loads((TRANS/path).read_text(encoding="utf-8"))
        for no,doc in translations.items():
            if int(no) in stories:raise RuntimeError("หมายเลข Story ซ้ำ "+no)
            stories[int(no)]=doc
    sprints={int(no):v for no,v in json.loads((TRANS/"sprint_plan_th.json").read_text(encoding="utf-8")).items()}
    expected=[i["number"] for i in issues if i["issue_type"] in ("Story","Sprint")]
    if len(expected)!=92 or len(stories)!=75 or len(sprints)!=17 or set(expected)!=(set(stories)|set(sprints)):
        raise RuntimeError("รายการคำแปลไม่ครบ 75 Stories + 17 Sprints")
    for number,doc in stories.items():
        if len(doc.get("criteria",[]))!=3 or not doc.get("title"):
            raise RuntimeError("เกณฑ์ยอมรับไม่ครบสำหรับ Issue #"+str(number))
    return issue_map,stories,sprints

def metadata(body,key):
    patterns={
     "epic":r"(?i)\bEpic\s*:\*\*\s*#(\d+)",
     "forecast":r"(?i)(?:Forecast(?: iteration)?|Forecast sprint)\s*:\*\*\s*(S\d{2})",
     "priority":r"(?i)\b(P[0-3])\b",
     "dependencies":r"(?im)^\s*(?:-\s*)?\*\*(?:Predecessors / dependencies|Dependencies|Dependency):\*\*\s*([^\n]+)"
    }
    match=re.search(patterns[key],body)
    return match.group(1).strip() if match else ""

def get_meta(source):
    body=source["body"]
    epic=metadata(body,"epic")
    forecast=metadata(body,"forecast")
    priority=metadata(body,"priority")
    dependencies=metadata(body,"dependencies")
    if dependencies:
        dependencies=dependencies.split(";")[0].replace("**","").strip().rstrip(".")
    # Some source issues have inline "**Forecast:**" or proposed sprint texts;
    # the regular expression above is deliberately based on source metadata.
    if not epic:
        epmatch=re.search(r"(?i)\bEpic\s*:\s*#(\d+)",body)
        if epmatch:epic=epmatch.group(1)
    if not forecast:
        fmatch=re.search(r"(?i)(?:Forecast(?: iteration)?|Forecast sprint)\s*:\s*(S\d{2})",body)
        if fmatch:forecast=fmatch.group(1)
    return epic,forecast,priority,dependencies

def render_story(source,doc):
    number=source["number"]
    ident=re.match(r"^(\[STORY\]\[([^\]]+)\]\[([^\]]+)\])",source["title"])
    if not ident:raise RuntimeError("รหัส Story ไม่ถูกต้อง #"+str(number))
    prefix,squad,code=ident.groups()
    epic,forecast,priority,dependencies=get_meta(source)
    if not epic or not forecast or not priority:
        raise RuntimeError(f"ข้อมูล Epic/Sprint/Priority ไม่ครบในต้นฉบับ #{number}: {epic}/{forecast}/{priority}")
    if not dependencies:
        raise RuntimeError("ไม่พบรายการพึ่งพาตามต้นฉบับ #"+str(number))
    fourth="เจ้าของผลิตภัณฑ์ทบทวนแนวทางการตรวจรับ" if number==98 else GOV_DOD if 92<=number<=97 else COMMON_DOD
    title=prefix+" "+doc["title"]
    capability=TAGS.get(squad,"โครงการ")
    body=[
        "## เรื่องราวผู้ใช้",
        "",
        "ในฐานะผู้ใช้งานหรือผู้เกี่ยวข้องที่ได้รับอนุญาต ต้องการดำเนินงาน **"+doc["title"]+
        "** เพื่อให้ขีดความสามารถด้าน"+capability+"มีความน่าเชื่อถือ ควบคุมสิทธิ์ได้ และตรวจสอบย้อนหลังได้ตามขอบเขตงาน",
        "",
        "## เกณฑ์การยอมรับ",
        "",
    ]
    for criterion in doc["criteria"]+[fourth]:
        body.append("- [ ] "+criterion)
    body+=["",
        "## ข้อมูลการวางแผนและการอ้างอิง",
        "",
        "- **ประเภทงาน:** เรื่องราวผู้ใช้ (รายการงานผลิตภัณฑ์)",
        "- **รหัสงาน:** "+code,
        "- **งานระดับ Epic:** #"+epic,
        "- **สายงานที่เสนอ:** "+squad+" — "+capability,
        "- **สปรินต์ที่คาดการณ์:** "+forecast+" (ยังไม่ใช่ข้อผูกพันของแผนสปรินต์)",
        "- **ลำดับความสำคัญที่เสนอ:** "+priority+" (รอเจ้าของผลิตภัณฑ์ยืนยัน)",
        "- **งานหรือเงื่อนไขที่ต้องพึ่งพา:** "+dependencies,
        "- **ขนาดงาน:** รอทีมพัฒนาประเมินระหว่างการปรับปรุงรายการงาน",
        "- **ผู้พิจารณาเกณฑ์ยอมรับ:** เจ้าของผลิตภัณฑ์หรือผู้แทนที่ได้รับมอบหมาย",
        "- **การเชื่อมโยง TOR:** อ้างอิงขอบเขตงานฉบับเปิดเผยได้; การเชื่อมโยง TOR รายข้อและหลักฐานฉบับควบคุมต้องตรวจสอบภายใน",
        "- **สถานะการวางแผน:** เป็นรายการงานที่เสนอ ไม่ถือว่าได้รับอนุมัติหรือดำเนินการเสร็จแล้ว",
        "",
        "> เอกสารนี้อยู่ในคลังสาธารณะ ให้ใช้ข้อมูลทดสอบสังเคราะห์เท่านั้น ห้ามเผยแพร่ข้อมูลคดีจริง ข้อมูลส่วนบุคคล รหัสผ่าน ที่อยู่ระบบภายใน หรือผลตรวจสอบความปลอดภัยที่จำกัดการเข้าถึง",
        "",
        "**แหล่งอ้างอิง:** [ทะเบียนรายการงานผลิตภัณฑ์]("+REPO_LINK+"PRODUCT_BACKLOG_REGISTER_PUBLIC.md) · [เกณฑ์งานพร้อมและงานเสร็จ]("+REPO_LINK+"DEFINITION_OF_READY_DONE_PUBLIC.md)",
    ]
    return title,"\n".join(body)+"\n"

def render_sprint(source,thai_title):
    number=source["number"]
    match=re.match(r"^(\[SPRINT\]\[(S\d{2})\])",source["title"])
    if not match:raise RuntimeError("รหัส Sprint ไม่ถูกต้อง #"+str(number))
    prefix,code=match.groups()
    original=source["body"]
    day=re.search(r"\bD(\d+)–D(\d+)\b",original)
    dates=re.search(r"\b(20\d{2}-\d{2}-\d{2})\s*[–-]\s*(20\d{2}-\d{2}-\d{2})\b",original)
    if not day or not dates:raise RuntimeError("ช่วงเวลาไม่ครบ #"+str(number))
    c=re.search(r"(?:Candidate related backlog / gate|Candidate backlog items)\s*:\*\*\s*([^\n]+)",original)
    if not c:raise RuntimeError("รายการงานเสนอไม่ครบ #"+str(number))
    candidates=c.group(1).strip().replace("[Gate M1 #99]","งวด M1 (#99)").replace("[Gate M2 #100]","งวด M2 (#100)").replace("[Gate M3 #101]","งวด M3 (#101)").replace("[Gate M4 #102]","งวด M4 (#102)").replace("controlled closeout","การปิดโครงการภายใต้การควบคุม")
    title=prefix+" "+thai_title+" — แผนเสนอ"
    body=[
        "## แผนสปรินต์ "+code+" (ยังไม่ใช่สปรินต์ที่เริ่มดำเนินการ)",
        "",
        "- **ช่วงวันตามสัญญาที่เสนอ:** D"+day.group(1)+"–D"+day.group(2)+" (รอบละ 14 วันปฏิทิน)",
        "- **ช่วงวันที่ตัวอย่าง:** "+dates.group(1)+" ถึง "+dates.group(2)+" โดยใช้วันที่ 1 ตุลาคม 2569 เป็นวันเริ่มสัญญา **สมมติ** เท่านั้น",
        "- **หัวข้อสำหรับพิจารณาและสาธิต:** "+thai_title,
        "- **รายการงานหรือจุดส่งมอบที่เสนอ:** "+candidates,
        "- **เป้าหมายสปรินต์ที่มีผลจริง:** รอทีมสกรัมตกลงร่วมกันในการประชุมวางแผนสปรินต์",
        "- **กำลังทีม ขนาดงาน และงานที่จะรับเข้าในสปรินต์:** รอเจ้าของผลิตภัณฑ์และทีมพัฒนาพิจารณาตามความพร้อม",
        "",
        "## รายการตรวจสอบวงจรสกรัม",
        "",
        "- [ ] เจ้าของผลิตภัณฑ์และทีมพัฒนาร่วมกำหนดเป้าหมายสปรินต์ที่มีคุณค่าในการประชุมวางแผน",
        "- [ ] ทีมพัฒนาเลือกงานตามกำลังและวางแผนการพัฒนา การเชื่อมระบบ การทดสอบ และคุณภาพ",
        "- [ ] การประชุมสกรัมรายวันใช้ทบทวนความคืบหน้า ปัญหา และปรับแผนตามเป้าหมาย",
        "- [ ] ผลงานที่รวมเข้าระบบผ่านเกณฑ์งานเสร็จร่วมของทีม; งานที่ยังไม่เสร็จกลับเข้าสู่รายการงานผลิตภัณฑ์",
        "- [ ] การทบทวนสปรินต์สาธิตผลงานกับผู้มีส่วนได้ส่วนเสียและปรับลำดับงานตามข้อเสนอแนะ",
        "- [ ] การสะท้อนบทเรียนหลังกิจกรรมสปรินต์กำหนดผู้รับผิดชอบและการปรับปรุงครั้งถัดไป",
        "",
        "## ความเสี่ยงและการตรวจรับตาม TOR",
        "",
        "ทบทวนงานที่ต้องพึ่งพาระหว่างทีม ความปลอดภัย การคุ้มครองข้อมูลส่วนบุคคล และความพร้อมส่งมอบตาม TOR โดยไม่เผยแพร่รายละเอียดที่จำกัดการเข้าถึง",
        "",
        "ช่วง D239–D240 จัดไว้สำหรับการทบทวนและส่งมอบตามสัญญาขั้นสุดท้ายหลัง S17 **ไม่ใช่สปรินต์เพิ่มเติม**",
        "",
        "**เอกสารอ้างอิง:** [แผนสปรินต์ทั้ง 17 รอบ]("+REPO_LINK+"SPRINT_ROADMAP_PUBLIC.md) · [เกณฑ์งานเสร็จ]("+REPO_LINK+"DEFINITION_OF_READY_DONE_PUBLIC.md)",
        "",
        "> รายการนี้เป็นเพียงแผนเสนอ ยังไม่ยืนยันว่าได้เริ่มหรือเสร็จงาน ผ่านการทดสอบ ได้รับการตรวจรับตามสัญญา หรือเปิดใช้งานระบบจริงแล้ว",
    ]
    return title,"\n".join(body)+"\n"

def get_issue(number):return call("/repos/"+REPO+"/issues/"+str(number))

def verify_previous(current,original):
    if current["title"]!=original["title"]:
        return "ชื่อไม่ตรงกับต้นฉบับ หรือมีการแก้ไขร่วมกัน"
    if (current.get("body") or "").strip()!=(original.get("body") or "").strip():
        return "รายละเอียดไม่ตรงกับต้นฉบับ หรือมีการแก้ไขร่วมกัน"
    return ""

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=["validate","apply"],default="validate")
    parser.add_argument("--confirm",default="")
    opts=parser.parse_args()
    if opts.mode=="apply" and opts.confirm!="TRANSLATE_75_STORIES_17_SPRINTS_TH":
        raise RuntimeError("ต้องระบุรหัสยืนยันของขั้นตอนปรับข้อมูล")
    originals,story_map,sprint_map=data()
    plan=[]
    for no in sorted(set(story_map)|set(sprint_map)):
        source=originals[no]
        proposed=render_story(source,story_map[no]) if no in story_map else render_sprint(source,sprint_map[no])
        current=get_issue(no)
        if current["title"]==proposed[0] and (current.get("body") or "").strip()==proposed[1].strip():
            plan.append((no,proposed,"already"))
        else:
            mismatch=verify_previous(current,source)
            if mismatch:raise RuntimeError(f"Issue #{no} มีข้อมูลเปลี่ยนจาก snapshot: {mismatch} (หยุดก่อนเขียนทับ)")
            plan.append((no,proposed,"pending"))
    pending=[p for p in plan if p[2]=="pending"]
    print(f"ตรวจครบ 92: เรื่องงานผู้ใช้ {len(story_map)} รายการ / สปรินต์ {len(sprint_map)} รอบ")
    print(f"ต้องปรับอีก {len(pending)} รายการ / แปลแล้ว {92-len(pending)} รายการ")
    if opts.mode=="validate":
        print("ผ่านการตรวจสอบต้นฉบับและคำแปล ไม่เปลี่ยน GitHub Issues")
        return
    for index,(no,(title,body),_) in enumerate(pending,1):
        call("/repos/"+REPO+"/issues/"+str(no),"PATCH",{"title":title,"body":body})
        if index%10==0:print("อัปเดตสำเร็จ",index,"/",len(pending))
    print("แปลข้อมูล GitHub Issues สำเร็จครบ 92 รายการ")
    path=os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path,"a",encoding="utf-8") as file:
            file.write("### AMLO Cybercrime — คำแปลภาษาไทย\n\n")
            file.write("✅ User Stories 75 รายการ · แผนสปรินต์ 17 รอบ · คงหมายเลข Issue/Epic/ลำดับงานเดิม\n")
            file.write("✅ [เปิดกระดานหลัก Public Project #1](https://github.com/users/chaowarojs1-bot/projects/1)\n")

if __name__=="__main__":
    try:main()
    except Exception as exc:
        print("TRANSLATION ERROR:",str(exc),file=sys.stderr)
        sys.exit(1)
