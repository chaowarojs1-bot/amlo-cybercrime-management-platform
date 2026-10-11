#!/usr/bin/env python3
"""เปลี่ยนชื่อแสดงผลของมุมมอง User Story/Sprint Plan ใน GitHub Project #1 เป็นไทย
คง Project #1 Public, URL, การ์ด, ตัวเลือกงาน และฟิลด์ตัวเลข S01–S17 ไม่เปลี่ยน
"""
import json,os,sys
from urllib.request import Request,urlopen

PROJECT=1
OWNER="chaowarojs1-bot"
VIEW_NAMES={
 "Scrum | Kanban":"เรื่องงานผู้ใช้ | กระดานสกรัม",
 "Sprints | แผน":"แผนสปรินต์ | 17 รอบ",
}
FIELD_NAMES={"SprintPlan":"แผนสปรินต์"}

def api(query,variables=None):
    token=os.environ.get("AMLO_PROJECT_TOKEN")
    if not token:raise RuntimeError("ต้องตั้งค่า AMLO_PROJECT_TOKEN")
    request=Request("https://api.github.com/graphql",method="POST",
        data=json.dumps({"query":query,"variables":variables or {}},ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type":"application/json","Authorization":"Bearer "+token,
                 "Accept":"application/vnd.github+json","User-Agent":"AMLO-Thai-Views"})
    with urlopen(request,timeout=60) as response:payload=json.load(response)
    if payload.get("errors"):raise RuntimeError("; ".join(x.get("message","GraphQL error") for x in payload["errors"]))
    return payload["data"]

QUERY='''query($login:String!){user(login:$login){projectV2(number:1){
id number public url
views(first:100){nodes{id name layout}}
fields(first:100){nodes{
... on ProjectV2Field{id name}
... on ProjectV2SingleSelectField{id name}
... on ProjectV2IterationField{id name}
}}
}}}'''
VIEW='''mutation($input:UpdateProjectV2ViewInput!){updateProjectV2View(input:$input){projectV2View{id name}}}'''
FIELD='''mutation($input:UpdateProjectV2FieldInput!){updateProjectV2Field(input:$input){projectV2Field{
... on ProjectV2SingleSelectField{id name}}}}'''

def project():
    p=api(QUERY,{"login":OWNER})["user"]["projectV2"]
    if not p:raise RuntimeError("ไม่พบ Project #1")
    if p["number"]!=PROJECT or not p["public"]:raise RuntimeError("Project #1 ไม่ได้อยู่ในสถานะ Public ตามที่ตกลง")
    return p

def main():
    before=project()
    views={x["name"]:x for x in before["views"]["nodes"]}
    fields={x["name"]:x for x in before["fields"]["nodes"]}
    for old,new in VIEW_NAMES.items():
        if new in views:continue
        if old not in views:raise RuntimeError("ไม่พบมุมมองต้นทาง "+old)
    for old,new in FIELD_NAMES.items():
        if new not in fields and old not in fields:raise RuntimeError("ไม่พบฟิลด์ต้นทาง "+old)
    for old,new in VIEW_NAMES.items():
        if new in views:continue
        api(VIEW,{"input":{"viewId":views[old]["id"],"name":new}})
        print("เปลี่ยนชื่อมุมมอง:",new)
    for old,new in FIELD_NAMES.items():
        if new in fields:continue
        api(FIELD,{"input":{"fieldId":fields[old]["id"],"name":new}})
        print("เปลี่ยนชื่อฟิลด์:",new)
    updated=project()
    names={v["name"] for v in updated["views"]["nodes"]}
    fieldnames={f["name"] for f in updated["fields"]["nodes"]}
    if not set(VIEW_NAMES.values()).issubset(names) or not set(FIELD_NAMES.values()).issubset(fieldnames):
        raise RuntimeError("การตรวจชื่อหลังแปลไม่ผ่าน")
    print("สำเร็จ: Project #1 Public, ลิงก์เดิม:",updated["url"])
if __name__=="__main__":
    try:main()
    except Exception as error:
        print("VIEW TRANSLATION ERROR:",error,file=sys.stderr)
        sys.exit(1)
