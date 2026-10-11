#!/usr/bin/env python3
"""สร้างบอร์ด Markdown จาก GitHub Issues; ไม่ถือว่า Issue ที่ปิดคือการตรวจรับ TOR"""
import json, os, re
from pathlib import Path
from collections import defaultdict
from urllib.request import Request, urlopen
from urllib.error import HTTPError

REPO=os.getenv("GITHUB_REPOSITORY","chaowarojs1-bot/amlo-cybercrime-management-platform")
TOKEN=os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
URL="https://api.github.com/repos/"+REPO
OUT=Path(__file__).resolve().parents[1]/"project-management"
STAGES=["Product Backlog","Ready","In Progress","Code Review","Testing","PO Review","Done"]
LABELS={"status:backlog":STAGES[0],"status:ready":STAGES[1],"status:in-progress":STAGES[2],"status:code-review":STAGES[3],"status:testing":STAGES[4],"status:po-review":STAGES[5],"status:done":STAGES[6]}
GATES={"gate:preparing":"เตรียมส่งมอบ","gate:evidence-review":"ตรวจหลักฐาน","gate:sit-uat":"SIT/UAT","gate:submitted":"ส่งตรวจรับ","gate:accepted":"ตรวจรับแล้ว (ต้องตรวจหลักฐาน)","gate:returned":"ส่งกลับแก้ไข"}
COLORS={"status:blocked":"b60205",**{k:"bfdadc" for k in LABELS},**{k:"fef2c0" for k in GATES}}
COLORS["status:done"]="0e8a16"
COLORS["gate:accepted"]="0e8a16"

def request(path,method="GET",data=None):
    body=None if data is None else json.dumps(data).encode()
    headers={"Authorization":"Bearer "+TOKEN,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"amlo-board"}
    if body: headers["Content-Type"]="application/json"
    with urlopen(Request("https://api.github.com"+path,data=body,headers=headers,method=method),timeout=45) as r:
        return json.load(r)

def paged(path):
    acc=[]
    for page in range(1,20):
        items=request(path+("&" if "?" in path else "?")+"per_page=100&page="+str(page))
        acc.extend(items)
        if len(items)<100: break
    return acc

def get_labels(issue):
    return {x["name"].lower() for x in issue.get("labels",[])}

def stage(issue):
    labels=get_labels(issue)
    found=[v for k,v in LABELS.items() if k in labels]
    if issue["state"]=="closed" and not found: return "Closed (ไม่ยืนยัน Done)"
    return found[0] if found else STAGES[0]

def link(issue):
    title=re.sub(r"[\r\n\t]+"," ",issue["title"])
    for x,y in [("|","¦"),("[","［"),("]","］"),("<","‹"),(">","›")]:
        title=title.replace(x,y)
    return "[#"+str(issue["number"])+" "+title[:160]+"]("+issue["html_url"]+")"

def head(title):
    return ["# "+title,"","> กระดานจาก GitHub Issues ไม่ใช่ GitHub Projects v2 | ไม่แสดงข้อมูลคดีจริงหรือหลักฐานลับ","> ปิด Issue ไม่เท่ากับผ่าน Definition of Done / UAT / การตรวจรับ TOR","",
       "[Scrum](./SCRUM_BOARD.md) · [Program](./PROGRAM_BOARD.md) · [Delivery](./DELIVERY_BOARD.md) · [คู่มือ](./BOARD_USER_GUIDE_TH.md)",""]

def scrum(issues):
    stories=[x for x in issues if x["title"].startswith("[STORY]")]
    open_stories=[x for x in stories if x["state"]=="open"]
    by=defaultdict(list)
    for x in open_stories: by[stage(x)].append(x)
    lines=head("Scrum Board — AMLO Cybercrime")
    lines+=["## กระดานสถานะงาน","",
      "| "+" | ".join(STAGES)+" |",
      "| "+" | ".join("---" for _ in STAGES)+" |",
      "| "+" | ".join(str(len(by[s])) for s in STAGES)+" |","",
      "User Stories เปิดอยู่: "+str(len(open_stories))+" | รายการที่ปิดแล้ว: "+str(len(stories)-len(open_stories)),
      "งานที่ยังไม่มี status label เริ่มต้นที่ Product Backlog; สถานะอื่นต้องมีผู้รับผิดชอบปรับ Label",""]
    for s in STAGES:
        lines+=["## "+s+" ("+str(len(by[s]))+")",""]
        groups=defaultdict(list)
        for x in sorted(by[s],key=lambda a:a["number"]):
            m=re.search(r"^\[STORY\]\[([^\]]+)\]",x["title"])
            groups[m.group(1) if m else "อื่น ๆ"].append(x)
        if not groups: lines+=["_ไม่มีรายการ_",""]
        for group in sorted(groups):
            lines+=["### Squad "+group,""]
            for x in groups[group]:
                block=" — BLOCKED" if "status:blocked" in get_labels(x) else ""
                lines+=["- "+link(x)+block]
            lines.append("")
    closed=[x for x in stories if x["state"]=="closed"]
    lines+=["## Issues ที่ปิดแล้ว — ไม่เท่ากับผ่าน TOR",""]
    lines+=["- "+link(x) for x in sorted(closed,key=lambda a:a["number"])]
    lines.append("")
    return "\n".join(lines)

def program(issues):
    epics=sorted([x for x in issues if re.match(r"^\[EP-\d+\]",x["title"])],key=lambda x:x["number"])
    lines=head("Program Board — Epic และภาพรวมโครงการ")
    lines+=["| Epic | สถานะติดตาม |","|---|---|"]
    for e in epics: lines+=["| "+link(e)+" | "+stage(e)+" |"]
    lines+=["","[แผน Sprint 17 รอบ](./SPRINT_ISSUE_REGISTER_PUBLIC.md) · [TOR Gates](./DELIVERY_BOARD.md)","",""]
    return "\n".join(lines)

def delivery(issues):
    gates=sorted([x for x in issues if x["title"].startswith("[GATE]")],key=lambda x:x["number"])
    sprints=sorted([x for x in issues if x["title"].startswith("[SPRINT]")],key=lambda x:x["number"])
    lines=head("Delivery Board — ตรวจรับตาม TOR")
    lines+=["## จุดตรวจรับ (D30 / D120 / D210 / D240)","","| วัน | Gate | สถานะ |","|---|---|---|"]
    for day,g in zip([30,120,210,240],gates):
        v=[val for key,val in GATES.items() if key in get_labels(g)]
        status="Label ซ้ำ ต้องตรวจสอบ" if len(v)>1 else v[0] if v else "ยังไม่ยืนยัน"
        lines+=["| D"+str(day)+" | "+link(g)+" | "+status+" |"]
    lines+=["","สถานะ gate:accepted จะใช้ได้ต่อเมื่อมีหลักฐานตรวจรับอย่างเป็นทางการ ไม่ใช่ผลจากการปิด Issue","","## Sprint Trackers (ยังเป็นแผน)",""]
    for s in sprints: lines+=["- "+link(s)]
    lines+=["","วันที่เริ่มสัญญา 1 ตุลาคม 2569 ใน Roadmap เป็นตัวอย่าง ต้องยืนยันวันเริ่มจริง","",""]
    return "\n".join(lines)

def main():
    if not TOKEN: raise SystemExit("ไม่พบ GH_TOKEN หรือ GITHUB_TOKEN")
    existing={x["name"].lower() for x in paged("/repos/"+REPO+"/labels?")}
    for name,color in COLORS.items():
        if name in existing: continue
        try: request("/repos/"+REPO+"/labels","POST",{"name":name,"color":color,"description":"AMLO board tracking; not a TOR acceptance"})
        except HTTPError as e: print("ไม่สามารถสร้าง label",name,e.code)
    issues=[x for x in paged("/repos/"+REPO+"/issues?state=all&") if "pull_request" not in x]
    OUT.mkdir(parents=True,exist_ok=True)
    for fname,content in [("SCRUM_BOARD.md",scrum(issues)),("PROGRAM_BOARD.md",program(issues)),("DELIVERY_BOARD.md",delivery(issues))]:
        (OUT/fname).write_text(content,encoding="utf-8")
        print("Updated",fname)
    print("Issues:",len(issues))

if __name__=="__main__": main()

# ป้ายชื่องานที่แสดงใช้ชื่อ Issue ภาษาไทยล่าสุด โดยไม่เปลี่ยนสถานะงาน
