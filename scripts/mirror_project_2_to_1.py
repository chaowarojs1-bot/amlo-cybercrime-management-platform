#!/usr/bin/env python3
"""Safely mirror GitHub Project #2 into existing public Project #1 (preserve QR URL).
- Preview by default.
- On apply, first create PRIVATE backup of Project #1 including its 12 draft issues.
- Copy fields/views/linked items and project-level field values from #2.
- Archive (not delete) old #1-only items, remove old #1-only views after verification.
- Project #2 remains unchanged. GitHub Issue records remain unchanged.
"""
import argparse
import json
import os
import sys
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

OWNER = "chaowarojs1-bot"
SOURCE = 2
TARGET = 1
BACKUP_TITLE = "AMLO Project 1 - Private Safety Backup Before Copying Project 2"
CONFIRM = "COPY_PROJECT_2_INTO_PROJECT_1_PUBLIC"
BASE = "https://api.github.com/graphql"

class MirrorError(Exception):
    pass

def query_api(query, vars=None):
    token = os.environ.get("AMLO_PROJECT_TOKEN")
    if not token:
        raise MirrorError("Secret AMLO_PROJECT_TOKEN ไม่พบ")
    req = Request(BASE, data=json.dumps({"query":query,"variables":vars or {}}).encode(),
                  headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
                           "Content-Type":"application/json","User-Agent":"AMLO-QR-Project-Mirror"}, method="POST")
    for attempt in range(5):
        try:
            with urlopen(req,timeout=90) as resp:
                result=json.load(resp)
            if result.get("errors"):
                raise MirrorError("; ".join(e.get("message","GraphQL failure") for e in result["errors"])[:850])
            return result["data"]
        except HTTPError as err:
            if err.code in (429,502,503,504) and attempt<4:
                time.sleep(2**attempt)
                continue
            raise MirrorError("GitHub API HTTP "+str(err.code)+" "+err.read(500).decode(errors="replace")[:300])
        except URLError:
            if attempt<4:
                time.sleep(2**attempt)
                continue
            raise MirrorError("GitHub API ไม่ตอบสนอง")
    raise MirrorError("GitHub API ล้มเหลว")

def mutation(name,type_name,response,input):
    query="mutation($input:"+type_name+"!){"+name+"(input:$input){"+response+"}}"
    return query_api(query,{"input":input})[name]

QUERY = '''
query($login:String!,$number:Int!,$after:String){
 user(login:$login){projectV2(number:$number){
 id number title url public closed readme shortDescription
 fields(first:100){nodes{
 __typename
 ... on ProjectV2Field{id name dataType}
 ... on ProjectV2SingleSelectField{id name dataType options{id name color description}}
 ... on ProjectV2IterationField{id name dataType configuration{duration iterations{id title startDate duration}}}
 ... on ProjectV2MultiSelectField{id name dataType multiSelectOptions{id name color description}}
 }}
 views(first:100){nodes{
 id name layout filter
 fields(first:100){nodes{
 ... on ProjectV2Field{id name}
 ... on ProjectV2SingleSelectField{id name}
 ... on ProjectV2IterationField{id name}
 ... on ProjectV2MultiSelectField{id name}
 }}
 }}
 items(first:60,after:$after){
 totalCount pageInfo{hasNextPage endCursor}
 nodes{id type isArchived content{__typename
 ... on Issue{id number repository{nameWithOwner isPrivate}}
 ... on PullRequest{id repository{nameWithOwner isPrivate}}
 ... on DraftIssue{id title}
 }
 fieldValues(first:50){nodes{
 __typename
 ... on ProjectV2ItemFieldSingleSelectValue{field{... on ProjectV2SingleSelectField{name}} name}
 ... on ProjectV2ItemFieldNumberValue{field{... on ProjectV2Field{name}} number}
 ... on ProjectV2ItemFieldTextValue{field{... on ProjectV2Field{name}} text}
 ... on ProjectV2ItemFieldDateValue{field{... on ProjectV2Field{name}} date}
 ... on ProjectV2ItemFieldIterationValue{field{... on ProjectV2IterationField{name}} iterationId}
 ... on ProjectV2ItemFieldMultiSelectValue{field{... on ProjectV2MultiSelectField{name}} options{id name}}
 }}
 }
 }}
}}
'''

def read_project(number):
    cursor=None
    items=[]
    proj=None
    while True:
        data=query_api(QUERY,{"login":OWNER,"number":number,"after":cursor})
        user=data.get("user") or {}
        proj=user.get("projectV2")
        if not proj:
            raise MirrorError("ไม่พบหรือไม่มีสิทธิ์เข้าถึง Project #"+str(number))
        page=proj["items"]
        items.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor=page["pageInfo"]["endCursor"]
    proj["all_items"]=items
    return proj

def project_list():
    query='''query($login:String!,$cursor:String){user(login:$login){id projectsV2(first:100,after:$cursor){nodes{id number title url public}pageInfo{hasNextPage endCursor}}}}'''
    cursor=None
    allprojects=[]
    ownerid=None
    while True:
        u=query_api(query,{"login":OWNER,"cursor":cursor})["user"]
        if not u:
            raise MirrorError("ไม่พบ GitHub Owner")
        ownerid=u["id"]
        p=u["projectsV2"]
        allprojects.extend(p["nodes"])
        if not p["pageInfo"]["hasNextPage"]:break
        cursor=p["pageInfo"]["endCursor"]
    return ownerid,allprojects

def active_items(project):
    return [x for x in project["all_items"] if not x["isArchived"]]

def linked_id(item):
    content=item.get("content") or {}
    return content.get("id") if item.get("type") in ("ISSUE","PULL_REQUEST") else None

def preflight(src,dst):
    si=active_items(src)
    if len(si)!=116:
        raise MirrorError("Project #2 ต้องมี 116 รายการที่มองเห็นได้ แต่พบ "+str(len(si)))
    if len({linked_id(x) for x in si})!=len(si):
        raise MirrorError("Project #2 มี Draft Issue, เนื้อหาที่อ่านไม่ได้ หรือข้อมูลรายการซ้ำ")
    if any((x["content"].get("repository") or {}).get("isPrivate") for x in si):
        raise MirrorError("Project #2 มี Issue จาก Repository ส่วนตัว จึงไม่สามารถเผยแพร่ #1 ได้อย่างปลอดภัย")
    sf={x["name"]:x for x in src["fields"]["nodes"]}
    tf={x["name"]:x for x in dst["fields"]["nodes"]}
    for name in ["Status","WorkType","Squad","SprintPlan","Priority","TORGate","DeliveryStage","Blocked","StoryPoints","EvidenceRef"]:
        if name not in sf:raise MirrorError("Project #2 ขาดฟิลด์ "+name)
        if name in tf and sf[name]["dataType"]!=tf[name]["dataType"]:
            raise MirrorError("ชนิดฟิลด์ไม่ตรงกัน: "+name)
    extras=[x for x in active_items(dst) if linked_id(x) not in {linked_id(s) for s in si}]
    stats={
        "source_active":len(si),"target_active_before":len(active_items(dst)),
        "target_extra_items":len(extras),
        "target_extra_drafts":sum(1 for x in extras if x["type"]=="DRAFT_ISSUE"),
        "source_fields":len(src["fields"]["nodes"]),
        "source_views":len(src["views"]["nodes"]),
        "target_public":dst["public"],
        "new_linked_items":len([x for x in si if linked_id(x) not in {linked_id(t) for t in active_items(dst)}])
    }
    print("CHECKS:",json.dumps(stats,ensure_ascii=False))
    return stats

def ensure_backup(original):
    ownerid,projects=project_list()
    match=[p for p in projects if p["title"]==BACKUP_TITLE]
    if match:
        if match[0]["public"]:
            raise MirrorError("Backup project มีสถานะ Public อย่างไม่คาดคิด")
        backup=read_project(match[0]["number"])
        saved_drafts=sum(x["type"]=="DRAFT_ISSUE" for x in active_items(backup))
        original_drafts=sum(x["type"]=="DRAFT_ISSUE" for x in active_items(original))
        if saved_drafts < original_drafts:
            raise MirrorError("Backup project มี Draft Issues ไม่ครบ")
        if {v["name"] for v in backup["views"]["nodes"]}!={v["name"] for v in original["views"]["nodes"]}:
            raise MirrorError("Backup project มี Views ไม่ครบ")
        print("ใช้สำเนาสำรองส่วนตัวที่มีอยู่แล้ว:",backup["url"])
        return backup
    result=mutation("copyProjectV2","CopyProjectV2Input","projectV2{id number url public}",
        {"projectId":original["id"],"ownerId":ownerid,"title":BACKUP_TITLE,"includeDraftIssues":True})["projectV2"]
    mutation("updateProjectV2","UpdateProjectV2Input","projectV2{id public}",
        {"projectId":result["id"],"public":False})
    print("สร้างสำเนาสำรอง Private:",result["url"])
    for attempt in range(12):
        backup=read_project(result["number"])
        if sum(x["type"]=="DRAFT_ISSUE" for x in active_items(backup)) >= sum(x["type"]=="DRAFT_ISSUE" for x in active_items(original)):
            break
        time.sleep(3)
    if sum(x["type"]=="DRAFT_ISSUE" for x in active_items(backup)) < sum(x["type"]=="DRAFT_ISSUE" for x in active_items(original)):
        raise MirrorError("สำเนาสำรอง Draft Issues ไม่ครบ ยุติก่อนแก้ไข Project #1")
    if not all(x["type"]!="DRAFT_ISSUE" for x in active_items(original)):
        if sum(x["type"]=="DRAFT_ISSUE" for x in active_items(backup)) < sum(x["type"]=="DRAFT_ISSUE" for x in active_items(original)):
            raise MirrorError("สำเนาสำรองไม่มี Draft Issues ครบ ยุติ")
    return backup

def opts(field):
    return field.get("options",field.get("multiSelectOptions",[]))

def option_input(x,id=None):
    d={"name":x["name"],"color":x.get("color") or "GRAY","description":x.get("description") or ""}
    if id:d["id"]=id
    return d

def ensure_fields(src,dst):
    sf={x["name"]:x for x in src["fields"]["nodes"]}
    tf={x["name"]:x for x in dst["fields"]["nodes"]}
    custom={"SINGLE_SELECT","MULTI_SELECT","NUMBER","TEXT","DATE","ITERATION"}
    for name,s in sf.items():
        if s["dataType"] not in custom:
            continue
        if name in tf:
            if s["dataType"]!=tf[name]["dataType"]:
                raise MirrorError("Field type mismatch for "+name)
            if s["dataType"]=="SINGLE_SELECT":
                t=tf[name]
                old={x["name"]:x for x in opts(t)}
                merged=[option_input(x,old.get(x["name"],{}).get("id")) for x in opts(s)]
                source_names={x["name"] for x in opts(s)}
                merged += [option_input(x,x["id"]) for x in opts(t) if x["name"] not in source_names]
                if [x["name"] for x in opts(t)]!=[x["name"] for x in merged] or len(opts(t))!=len(merged):
                    mutation("updateProjectV2Field","UpdateProjectV2FieldInput","projectV2Field{... on ProjectV2SingleSelectField{id}}",
                      {"fieldId":t["id"],"singleSelectOptions":merged})
                    print("ปรับตัวเลือกฟิลด์:",name)
            continue
        datatype=s["dataType"]
        arg={"projectId":dst["id"],"name":name,"dataType":datatype}
        if datatype=="SINGLE_SELECT":
            arg["singleSelectOptions"]=[option_input(x) for x in opts(s)]
        elif datatype=="MULTI_SELECT":
            arg["multiSelectOptions"]=[option_input(x) for x in opts(s)]
        elif datatype=="ITERATION":
            conf=s["configuration"];iterations=conf["iterations"]
            if not iterations:raise MirrorError("Iteration config is empty: "+name)
            arg["iterationConfiguration"]={"startDate":iterations[0]["startDate"],
                "duration":conf["duration"],"iterations":[{"title":z["title"],"startDate":z["startDate"],"duration":z["duration"]} for z in iterations]}
        mutation("createProjectV2Field","CreateProjectV2FieldInput",
           "projectV2Field{... on ProjectV2Field{id} ... on ProjectV2SingleSelectField{id} ... on ProjectV2IterationField{id} ... on ProjectV2MultiSelectField{id}}",
           arg)
        print("สร้างฟิลด์:",name)

def ensure_views(src,dst):
    existing={x["name"]:x for x in dst["views"]["nodes"]}
    for v in src["views"]["nodes"]:
        args={"name":v["name"],"layout":v["layout"]}
        if v["name"] in existing:
            args["viewId"]=existing[v["name"]]["id"]
            if v.get("filter") is not None:args["filter"]=v["filter"]
            mutation("updateProjectV2View","UpdateProjectV2ViewInput","projectV2View{id}",args)
        else:
            args={"projectId":dst["id"],"name":v["name"],"layout":v["layout"]}
            created=mutation("createProjectV2View","CreateProjectV2ViewInput","projectV2View{id}",args)["projectV2View"]
            if v.get("filter"):
                mutation("updateProjectV2View","UpdateProjectV2ViewInput","projectV2View{id}",
                    {"viewId":created["id"],"filter":v["filter"]})
            print("สร้าง View:",v["name"])

def source_values(item):
    values=[]
    for x in item["fieldValues"]["nodes"]:
        if not x:continue
        fld=x.get("field")
        if not fld or not fld.get("name"):continue
        typ=x["__typename"]
        if typ=="ProjectV2ItemFieldSingleSelectValue" and x.get("name") is not None:
            values.append((fld["name"],"SINGLE_SELECT",x["name"]))
        elif typ=="ProjectV2ItemFieldNumberValue" and x.get("number") is not None:
            values.append((fld["name"],"NUMBER",x["number"]))
        elif typ=="ProjectV2ItemFieldTextValue" and x.get("text") is not None:
            values.append((fld["name"],"TEXT",x["text"]))
        elif typ=="ProjectV2ItemFieldDateValue" and x.get("date") is not None:
            values.append((fld["name"],"DATE",x["date"]))
        elif typ=="ProjectV2ItemFieldMultiSelectValue" and x.get("options"):
            values.append((fld["name"],"MULTI_SELECT",[z["name"] for z in x["options"]]))
        elif typ=="ProjectV2ItemFieldIterationValue" and x.get("iterationId"):
            values.append((fld["name"],"ITERATION",x["iterationId"]))
    return values

def copy_items(src,dst):
    target=read_project(TARGET)
    dstid=target["id"]
    by_content={linked_id(x):x for x in active_items(target) if linked_id(x)}
    fields={x["name"]:x for x in target["fields"]["nodes"]}
    source_fields={x["name"]:x for x in src["fields"]["nodes"]}
    count_new=0
    for n,record in enumerate(active_items(src),1):
        source_id=linked_id(record)
        if not source_id:raise MirrorError("Unexpected draft source")
        if source_id in by_content:
            item_id=by_content[source_id]["id"]
        else:
            item=mutation("addProjectV2ItemById","AddProjectV2ItemByIdInput","item{id}",
                {"projectId":dstid,"contentId":source_id})["item"]
            item_id=item["id"]
            count_new+=1
        for name,datatype,value in source_values(record):
            if name not in fields or name not in source_fields:continue
            f=fields[name]
            if f["dataType"] not in ("SINGLE_SELECT","MULTI_SELECT","NUMBER","TEXT","DATE","ITERATION"):
                continue  # GitHub built-ins like Title/Assignees are shared via linked Issue, not written
            if datatype!=f["dataType"]:raise MirrorError("ประเภทข้อมูลฟิลด์ไม่ตรงกัน: "+name)
            if datatype=="SINGLE_SELECT":
                matching=[x for x in opts(f) if x["name"]==value]
                if not matching:raise MirrorError("ไม่มีตัวเลือก "+name+"="+str(value))
                payload={"singleSelectOptionId":matching[0]["id"]}
            elif datatype=="NUMBER":payload={"number":value}
            elif datatype=="TEXT":payload={"text":value}
            elif datatype=="DATE":payload={"date":value}
            elif datatype=="MULTI_SELECT":
                selection=[x["id"] for x in opts(f) if x["name"] in value]
                if len(selection)!=len(value):raise MirrorError("Multiselect missing option: "+name)
                payload={"multiSelectOptionIds":selection}
            elif datatype=="ITERATION":
                targetconf=f.get("configuration",{})
                sourceconf=source_fields[name].get("configuration",{})
                corresponding=next((x for x in sourceconf.get("iterations",[]) if x["id"]==value),None)
                targetiteration=next((x for x in targetconf.get("iterations",[]) if corresponding and x["title"]==corresponding["title"]),None)
                if not targetiteration:raise MirrorError("Iteration not found: "+name)
                payload={"iterationId":targetiteration["id"]}
            else:continue
            mutation("updateProjectV2ItemFieldValue","UpdateProjectV2ItemFieldValueInput",
                "projectV2Item{id}",{"projectId":dstid,"itemId":item_id,"fieldId":f["id"],"value":payload})
        if n%20==0:print("คัดลอกข้อมูลแล้ว",n,"/116")
    print("เพิ่มการ์ดที่เชื่อมกับ GitHub Issues:",count_new)

def finish(src,dst):
    target=read_project(TARGET)
    sid={linked_id(x) for x in active_items(src)}
    allcontent={linked_id(x) for x in active_items(target)}
    missing=sid-allcontent
    if missing:raise MirrorError("Project #1 ยังขาดการ์ด "+str(len(missing)))
    extra=[x for x in active_items(target) if linked_id(x) not in sid]
    for x in extra:
        mutation("archiveProjectV2Item","ArchiveProjectV2ItemInput","item{id}",
            {"projectId":target["id"],"itemId":x["id"]})
    print("เก็บรายการเก่าของ #1 ไว้ใน Archive:",len(extra))
    # Remove target-only views only after backup and full successful card migration.
    current=read_project(TARGET)
    sourceview={v["name"] for v in src["views"]["nodes"]}
    for v in current["views"]["nodes"]:
        if v["name"] not in sourceview:
            mutation("deleteProjectV2View","DeleteProjectV2ViewInput","projectV2View{id}",{"viewId":v["id"]})
            print("ลบมุมมองเดิมที่ไม่อยู่ใน Project #2:",v["name"])
    new_readme=src.get("readme") or ""
    new_desc=src.get("shortDescription") or "Scrum / TOR Delivery board"
    mutation("updateProjectV2","UpdateProjectV2Input","projectV2{id public url}",
        {"projectId":target["id"],"title":src["title"],"shortDescription":new_desc,
         "readme":new_readme,"public":True,"closed":False})
    verified=read_project(TARGET)
    valid_active={linked_id(x) for x in active_items(verified)}
    if valid_active!=sid or len(active_items(verified))!=116 or not verified["public"]:
        raise MirrorError("ตรวจสอบหลังย้ายไม่ผ่าน: Project #1 ไม่ตรงกับ Project #2")
    if {x["name"] for x in verified["views"]["nodes"]}!={x["name"] for x in src["views"]["nodes"]}:
        raise MirrorError("ตรวจสอบ View หลังย้ายไม่ผ่าน")
    print("สำเร็จ: Project #1 เป็น Public และมีการ์ด 116 รายการตรงกับ #2")
    print("เปิด QR เดิม:",verified["url"])
    path=os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path,"a",encoding="utf-8") as f:
            f.write("## AMLO Project #1 — คัดลอก #2 สำเร็จ\n\n")
            f.write("- ✅ [เปิด Project #1 ลิงก์ QR เดิม]("+verified["url"]+")\n")
            f.write("- ✅ Public · 116 การ์ด · 6 มุมมอง · สำรองรายการเดิมแล้ว\n")
            f.write("- Project #2 ไม่เปลี่ยนแปลง; GitHub Issues ไม่เปลี่ยนแปลง\n")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=["preview","apply"],default="preview")
    parser.add_argument("--confirmation",default="")
    args=parser.parse_args()
    src=read_project(SOURCE)
    dst=read_project(TARGET)
    if src["id"]==dst["id"]:raise MirrorError("Source and target are same project")
    preflight(src,dst)
    if args.mode=="preview":
        print("PREVIEW ONLY: ไม่มีการเปลี่ยนข้อมูลใด ๆ")
        return
    if args.confirmation!=CONFIRM:
        raise MirrorError("Confirmation code ไม่ถูกต้อง")
    backup=ensure_backup(dst)
    if backup["public"]:raise MirrorError("Backup ไม่เป็น Private")
    print("สำรอง Project #1 ไว้ที่:",backup["url"])
    ensure_fields(src,dst)
    # Reload target fields before copy.
    current=read_project(TARGET)
    ensure_views(src,current)
    copy_items(src,current)
    finish(src,current)

if __name__=="__main__":
    try:main()
    except Exception as e:
        print("MIRROR ERROR:",str(e),file=sys.stderr)
        sys.exit(1)
