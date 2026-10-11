#!/usr/bin/env python3
"""Read-only audit of personal Projects #1 and #2, without leaking item titles to public logs."""
import json,os,sys
from urllib.request import Request,urlopen
LOGIN="chaowarojs1-bot"
QUERY='''query($login:String!,$number:Int!,$after:String){
 user(login:$login){projectV2(number:$number){
 id number title url public closed
 fields(first:100){nodes{
 __typename
 ... on ProjectV2Field{id name dataType}
 ... on ProjectV2SingleSelectField{id name dataType options{id name color description}}
 ... on ProjectV2IterationField{id name dataType configuration{duration iterations{id title startDate duration}}}
 ... on ProjectV2MultiSelectField{id name dataType multiSelectOptions{id name color description}}
 }}
 views(first:100){nodes{id name layout filter}}
 items(first:100,after:$after){totalCount pageInfo{hasNextPage endCursor}nodes{
 id type isArchived
 content{__typename
 ... on Issue{id repository{nameWithOwner isPrivate}}
 ... on PullRequest{id repository{nameWithOwner isPrivate}}
 ... on DraftIssue{id title}
 }
 }}
 }}}
'''
def graphql(q,variables):
 token=os.environ.get("AMLO_PROJECT_TOKEN")
 if not token:raise RuntimeError("AMLO_PROJECT_TOKEN missing")
 request=Request("https://api.github.com/graphql",data=json.dumps({"query":q,"variables":variables}).encode(),headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json","Content-Type":"application/json","User-Agent":"AMLO-Projects-Audit"})
 with urlopen(request,timeout=60) as r:res=json.load(r)
 if res.get("errors"):raise RuntimeError(str(res["errors"])[:900])
 return res["data"]
def load(number):
 after=None;items=[];p=None
 while True:
  p=graphql(QUERY,{"login":LOGIN,"number":number,"after":after})["user"]["projectV2"]
  if not p:raise RuntimeError("Project #"+str(number)+" not found or unauthorized")
  batch=p["items"];items.extend(batch["nodes"])
  if not batch["pageInfo"]["hasNextPage"]:break
  after=batch["pageInfo"]["endCursor"]
 p["items_sanitized"]=items
 return p
def main():
 a=load(1);b=load(2)
 def ids(p):return {x["content"]["id"] for x in p["items_sanitized"] if x.get("content") and x["content"].get("id")}
 for p in [a,b]:
  its=p["items_sanitized"];private=sum(1 for i in its if i.get("content") and (i["content"].get("repository") or {}).get("isPrivate"))
  drafts=sum(1 for i in its if i["type"]=="DRAFT_ISSUE")
  fields=[f["name"]+" ("+f["dataType"]+")" for f in p["fields"]["nodes"]]
  views=[v["name"]+" ("+v["layout"]+")" for v in p["views"]["nodes"]]
  print("Project #",p["number"],"| public=",p["public"],"| items=",len(its),"| private-linked=",private,"| draft=",drafts, "| fields=",json.dumps(fields,ensure_ascii=False),"| views=",json.dumps(views,ensure_ascii=False))
 print("Shared items=",len(ids(a)&ids(b)),"| #1-only=",len(ids(a)-ids(b)),"| #2-only=",len(ids(b)-ids(a)))
 if len(b["items_sanitized"])<50:raise RuntimeError("Source #2 unexpectedly small: refuse to copy")
 print("Audit complete: NO WRITES. QR URL /projects/1 preserved.")
if __name__=="__main__":
 try:main()
 except Exception as e:print("AUDIT ERROR:",str(e),file=sys.stderr);sys.exit(1)
