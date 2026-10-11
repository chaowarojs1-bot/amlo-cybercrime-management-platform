#!/usr/bin/env python3
"""ติดตั้ง GitHub Projects v2 แบบ Kanban จริงจาก Issues เดิม
ไม่แก้ไข Issues / ไม่สร้างซ้ำ / Project เป็น Private / ห้ามถือว่าการปิด Issue คือการตรวจรับ TOR
"""
import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

REPO = "chaowarojs1-bot/amlo-cybercrime-management-platform"
OWNER = REPO.split("/")[0]
TITLE = "AMLO Cybercrime — Scrum & TOR Kanban"
MARKER = "AMLO_GITHUB_PROJECT_INSTALLER_V1"
STAGES = ["Product Backlog","Ready","In Progress","Code Review","Testing","PO Review","Done"]
LABEL_STATUS = {"status:backlog":"Product Backlog","status:ready":"Ready","status:in-progress":"In Progress",
 "status:code-review":"Code Review","status:testing":"Testing","status:po-review":"PO Review","status:done":"Done"}
FIELDS = {
 "WorkType":("SINGLE_SELECT",["Epic","User Story","Sprint Tracker","TOR Gate","Governance"]),
 "Squad":("SINGLE_SELECT",["A","B","C","D","E","Shared","Cross-team"]),
 "SprintPlan":("SINGLE_SELECT",[f"S{n:02d}" for n in range(1,18)]),
 "Priority":("SINGLE_SELECT",["P0","P1","P2","P3"]),
 "TORGate":("SINGLE_SELECT",["D30","D120","D210","D240"]),
 "DeliveryStage":("SINGLE_SELECT",["Planning","Preparing","Evidence Review","SIT/UAT","Submitted","Accepted","Returned"]),
 "Blocked":("SINGLE_SELECT",["Yes","No"]),
 "StoryPoints":("NUMBER",[]),
 "EvidenceRef":("TEXT",[])
}
VIEWS = [("Scrum | Kanban","BOARD_LAYOUT",'worktype:"User Story"'),
         ("Program | Epics","BOARD_LAYOUT","worktype:Epic"),
         ("Delivery | TOR","BOARD_LAYOUT",'worktype:"TOR Gate"'),
         ("Sprints | แผน","TABLE_LAYOUT",'worktype:"Sprint Tracker"'),
         ("All Work | Master","TABLE_LAYOUT","")]
class Error(Exception): pass

class API:
 def __init__(self, token):
  if not token: raise Error("ไม่พบ GitHub token สำหรับขั้นตอนนี้")
  self.token = token
 def req(self, endpoint, query=None, variables=None):
  data=json.dumps({"query":query,"variables":variables or {}}).encode() if query else None
  headers={"Authorization":"Bearer "+self.token,"Accept":"application/vnd.github+json",
           "X-GitHub-Api-Version":"2022-11-28","User-Agent":"AMLO-Project-Installer"}
  if data: headers["Content-Type"]="application/json"
  req=Request("https://api.github.com"+endpoint,data=data,headers=headers,method="POST" if data else "GET")
  for attempt in range(3):
   try:
    with urlopen(req, timeout=60) as resp: output=json.load(resp)
    if query and output.get("errors"):
     raise Error("; ".join(x.get("message","GraphQL error") for x in output["errors"]))
    return output["data"] if query else output
   except HTTPError as exc:
    if exc.code in (429,502,503,504) and attempt<2:
     time.sleep(2**attempt);continue
    raise Error("GitHub API HTTP "+str(exc.code)+": "+exc.read(1000).decode(errors="replace")[:350])
   except URLError:
    if attempt<2:time.sleep(2**attempt);continue
    raise Error("ไม่สามารถเชื่อมต่อ GitHub API")
  raise Error("GitHub API ไม่ตอบสนอง")
 def gql(self,query,**variables):return self.req("/graphql",query,variables)
 def issues(self):
  out=[]
  for page in range(1,25):
   batch=self.req(f"/repos/{REPO}/issues?state=all&per_page=100&page={page}")
   out.extend(x for x in batch if "pull_request" not in x)
   if len(batch)<100:break
  return out

def kind(x):
 n,t=x["number"],x["title"]
 if 5<=n<=20 and re.match(r"^\[EP-\d+\]",t):return "Epic"
 if (21<=n<=40 or 44<=n<=98) and t.startswith("[STORY]"):return "User Story"
 if 99<=n<=102 and t.startswith("[GATE]"):return "TOR Gate"
 if 103<=n<=119 and t.startswith("[SPRINT]"):return "Sprint Tracker"
 if 1<=n<=4:return "Governance"
 return None

def selected(issues):
 result=[x for x in issues if kind(x)]
 counts=Counter(kind(x) for x in result)
 expected={"Epic":16,"User Story":75,"TOR Gate":4,"Sprint Tracker":17,"Governance":4}
 if dict(counts)!=expected or len({x["number"] for x in result})!=len(result):
  raise Error(f"จำนวนรายการไม่ตรงตามแผน ({dict(counts)}) คาดว่า ({expected}); ยุติเพื่อให้ตรวจสอบ")
 return sorted(result,key=lambda x:x["number"]),counts

def metadata(x):
 typ=kind(x);title=x["title"];body=x.get("body") or ""
 labels={v["name"].lower() for v in x.get("labels",[])}
 statuses=[v for k,v in LABEL_STATUS.items() if k in labels]
 if len(statuses)>1:raise Error(f"Issue #{x['number']} มี Status Labels มากกว่าหนึ่งค่า")
 data={"WorkType":typ,"Status":statuses[0] if statuses else "Product Backlog"}
 if "status:blocked" in labels:data["Blocked"]="Yes"
 if typ=="User Story":
  m=re.match(r"^\[STORY\]\[([^\]]+)\]",title)
  if m and m.group(1) in FIELDS["Squad"][1]:data["Squad"]=m.group(1)
  m=re.search(r"(?:Forecast iteration|Iteration forecast|Forecast sprint)[^\n]{0,80}?\b(S\d{2})\b",body,re.I)
  if m and m.group(1) in FIELDS["SprintPlan"][1]:data["SprintPlan"]=m.group(1)
  m=re.search(r"(?:Proposed priority|Priority)[^\n]{0,60}?\b(P[0-3])\b",body,re.I)
  if m:data["Priority"]=m.group(1)
 elif typ=="Epic":
  n=x["number"]
  data["Squad"]="A" if n<=8 else "B" if n==9 else "C" if n==10 else "D" if n<=12 else "E" if n<=15 else "Shared" if n<=18 else "Cross-team"
 elif typ=="Sprint Tracker":
  m=re.search(r"\[S(\d{2})\]",title)
  if m:data["SprintPlan"]="S"+m.group(1)
 elif typ=="TOR Gate":
  data["TORGate"]={99:"D30",100:"D120",101:"D210",102:"D240"}[x["number"]]
  data["DeliveryStage"]="Planning"
 return data

Q_REPO='query{repository(owner:"chaowarojs1-bot",name:"amlo-cybercrime-management-platform"){id owner{__typename id login}}}'
Q_PROJECT='query($owner:String!,$after:String){user(login:$owner){id projectsV2(first:100,after:$after){nodes{id number title url readme}pageInfo{hasNextPage endCursor}}}}'
Q_ORG=Q_PROJECT.replace("user(login:","organization(login:")
Q_FIELDS='''query($id:ID!){node(id:$id){... on ProjectV2{
fields(first:100){nodes{... on ProjectV2Field{id name}
... on ProjectV2SingleSelectField{id name options{id name color description}}
... on ProjectV2IterationField{id name}}}
views(first:100){nodes{id name layout filter}}
}}}'''
Q_ITEMS='''query($id:ID!,$after:String){node(id:$id){... on ProjectV2{
items(first:100,after:$after){nodes{id content{... on Issue{id number}}
fieldValues(first:30){nodes{... on ProjectV2ItemFieldSingleSelectValue{field{... on ProjectV2SingleSelectField{name}} name}}}
}pageInfo{hasNextPage endCursor}}
}}}'''
def mutation(api,op,input_type,selection,data):
 q=f"mutation($input:{input_type}! ){{{op}(input:$input){{{selection}}}}}"
 return api.gql(q,input=data)[op]

def find_project(api,owner_type):
 query=Q_ORG if owner_type=="Organization" else Q_PROJECT
 key="organization" if owner_type=="Organization" else "user";after=None
 while True:
  root=api.gql(query,owner=OWNER,after=after)[key]
  if not root:raise Error("ไม่มีสิทธิ์อ่าน Projects ของเจ้าของ Repository")
  projects=root["projectsV2"]
  same=[x for x in projects["nodes"] if x["title"]==TITLE]
  if same:return same[0]
  if not projects["pageInfo"]["hasNextPage"]:return None
  after=projects["pageInfo"]["endCursor"]

def ensure_project(api):
 repo=api.gql(Q_REPO)["repository"]
 if not repo or repo["owner"]["login"]!=OWNER:raise Error("อ่าน Repository ต้นทางไม่ได้")
 obj=find_project(api,repo["owner"]["__typename"])
 if obj:
  if MARKER not in (obj.get("readme") or ""):raise Error("มี Project ชื่อเดียวกันแต่ไม่ได้สร้างด้วยตัวติดตั้งนี้ หยุดเพื่อไม่แก้ไขของผู้อื่น")
  print("ใช้ Project เดิม:",obj["url"]);return obj
 print("สร้าง GitHub Projects v2 ใหม่:",TITLE)
 obj=mutation(api,"createProjectV2","CreateProjectV2Input","projectV2{id number title url}",
             {"ownerId":repo["owner"]["id"],"repositoryId":repo["id"],"title":TITLE})["projectV2"]
 description="# AMLO Cybercrime — Scrum & TOR\n\n"+MARKER+"\n\nPrivate project; 17 sprint forecasts are not commitments. Done is not TOR acceptance."
 mutation(api,"updateProjectV2","UpdateProjectV2Input","projectV2{id}",
          {"projectId":obj["id"],"public":False,"shortDescription":"Scrum / Kanban / TOR Delivery","readme":description})
 return obj

def fields_views(api,pid):
 root=api.gql(Q_FIELDS,id=pid)["node"]
 if not root:raise Error("ไม่พบ Project")
 return ({x["name"]:x for x in root["fields"]["nodes"]},{x["name"]:x for x in root["views"]["nodes"]})

def options(names,existing=()):
 prior={x["name"]:x for x in existing}
 colors={"Product Backlog":"GRAY","Ready":"BLUE","In Progress":"YELLOW","Code Review":"PURPLE",
         "Testing":"ORANGE","PO Review":"PINK","Done":"GREEN",
         "P0":"RED","P1":"ORANGE","P2":"YELLOW","P3":"GREEN","Accepted":"GREEN","Returned":"RED"}
 result=[]
 for name in names:
  opt={"name":name,"color":colors.get(name,"BLUE"),"description":"For AMLO project planning; not TOR acceptance"}
  if name in prior:opt["id"]=prior[name]["id"]
  result.append(opt)
 return result

def existing_items(api,pid):
 out={};after=None
 while True:
  page=api.gql(Q_ITEMS,id=pid,after=after)["node"]["items"]
  for item in page["nodes"]:
   content=item.get("content") or {}
   if content.get("id"):
    filled={v["field"]["name"] for v in item.get("fieldValues",{}).get("nodes",[]) if v.get("field") and v.get("name")}
    out[content["id"]]={"id":item["id"],"filled":filled}
  if not page["pageInfo"]["hasNextPage"]:break
  after=page["pageInfo"]["endCursor"]
 return out

def ensure_fields(api,pid):
 fields,_=fields_views(api,pid)
 if "Status" in fields:
  status=fields["Status"]
  if "options" not in status:raise Error("Status ไม่ใช่ SINGLE_SELECT")
  if not set(STAGES).issubset(x["name"] for x in status["options"]):
   if existing_items(api,pid):raise Error("Project มีงานแล้วและตัวเลือก Status ไม่ครบ จะไม่เปลี่ยนฟิลด์โดยพลการ")
   mutation(api,"updateProjectV2Field","UpdateProjectV2FieldInput","projectV2Field{... on ProjectV2SingleSelectField{id}}",
            {"fieldId":status["id"],"singleSelectOptions":options(STAGES,status["options"])})
 else:
  mutation(api,"createProjectV2Field","CreateProjectV2FieldInput","projectV2Field{... on ProjectV2SingleSelectField{id}}",
           {"projectId":pid,"name":"Status","dataType":"SINGLE_SELECT","singleSelectOptions":options(STAGES)})
 fields,_=fields_views(api,pid)
 for name,(datatype,choices) in FIELDS.items():
  if name in fields:continue
  args={"projectId":pid,"name":name,"dataType":datatype}
  if datatype=="SINGLE_SELECT":args["singleSelectOptions"]=options(choices)
  mutation(api,"createProjectV2Field","CreateProjectV2FieldInput",
           "projectV2Field{... on ProjectV2Field{id} ... on ProjectV2SingleSelectField{id}}",args)
  print("สร้าง field:",name)
 fields,_=fields_views(api,pid)
 missing=set(["Status"]+list(FIELDS))-set(fields)
 if missing:raise Error("ฟิลด์ไม่ครบ: "+str(missing))
 return fields

def ensure_views(api,pid):
 _,views=fields_views(api,pid)
 for name,layout,filt in VIEWS:
  view=views.get(name)
  if not view:
   view=mutation(api,"createProjectV2View","CreateProjectV2ViewInput","projectV2View{id name layout}",
                 {"projectId":pid,"name":name,"layout":layout})["projectV2View"]
   print("สร้างมุมมอง:",name)
  if filt and view.get("filter")!=filt:
   mutation(api,"updateProjectV2View","UpdateProjectV2ViewInput","projectV2View{id}",
            {"viewId":view["id"],"filter":filt})

def add_items(api,pid,fields,issues):
 existing=existing_items(api,pid)
 optmap={key:{x["name"]:x["id"] for x in value.get("options",[])} for key,value in fields.items()}
 count=0
 for issue in issues:
  if issue["node_id"] in existing:
   itemid=existing[issue["node_id"]]["id"];set_fields=existing[issue["node_id"]]["filled"]
  else:
   itemid=mutation(api,"addProjectV2ItemById","AddProjectV2ItemByIdInput","item{id}",
                   {"projectId":pid,"contentId":issue["node_id"]})["item"]["id"]
   set_fields=set();count+=1
  for name,val in metadata(issue).items():
   if name in set_fields:continue
   option=optmap.get(name,{}).get(val)
   if not option:raise Error(f"ไม่พบตัวเลือก {name}={val} สำหรับ #{issue['number']}")
   mutation(api,"updateProjectV2ItemFieldValue","UpdateProjectV2ItemFieldValueInput","projectV2Item{id}",
            {"projectId":pid,"itemId":itemid,"fieldId":fields[name]["id"],"value":{"singleSelectOptionId":option}})
  if count and count%20==0 and issue["node_id"] not in existing:print("เพิ่มการ์ด:",count)
 print("เพิ่มการ์ดใหม่:",count,"| มีอยู่เดิม:",len(issues)-count)

def summary(message):
 print(message)
 path=os.environ.get("GITHUB_STEP_SUMMARY")
 if path:
  with open(path,"a",encoding="utf-8") as f:f.write(message+"\n")

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--mode",choices=["validate","install"],default="validate")
 mode=p.parse_args().mode
 token=os.getenv("AMLO_PROJECT_TOKEN") if mode=="install" else os.getenv("GITHUB_TOKEN")
 if mode=="install" and not token:raise Error("ต้องตั้ง Repository Secret ชื่อ AMLO_PROJECT_TOKEN ก่อน")
 api=API(token)
 issues,counts=selected(api.issues())
 for x in issues:metadata(x)
 summary(f"### AMLO Issues ตรวจสอบแล้ว\n\n16 Epics · 75 Stories · 17 Sprints (proposed) · 4 TOR Gates · 4 Governance · **{len(issues)} Issues**")
 if mode=="validate":return
 project=ensure_project(api)
 fields=ensure_fields(api,project["id"])
 ensure_views(api,project["id"])
 add_items(api,project["id"],fields,issues)
 summary("### GitHub Projects v2 ติดตั้งแล้ว\n\n**"+project["url"]+"**\n\nPrivate Kanban • Scrum / Program / Delivery • ไม่สร้าง Issues ซ้ำ")
if __name__=="__main__":
 try:main()
 except Error as error:
  print("ติดตั้งไม่สำเร็จ:",error,file=sys.stderr)
  sys.exit(1)
