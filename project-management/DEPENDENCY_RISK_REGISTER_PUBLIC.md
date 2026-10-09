# Cross-Team Dependency & Risk Register — Public/Sanitized

This is an illustrative dependency map for Scrum coordination. It does **not** assert external agreements, live access, actual blockers or confidential risks.

## Dependency register
| ID | Upstream | Downstream | Condition for handoff | Coordinator | Target |
|---|---|---|---|---|---|
| DEP-01 | EP-13 Security + EP-12 Cloud | EP-01/04/06 | Approved security and development baseline | Shared lead | Before integrated tests |
| DEP-02 | INT-03/04 data contract/intake | CASE-02, TXN-01 | Validated, versioned synthetic payload and error contract | A+B+C leads | Early integration |
| DEP-03 | IAM-02/03 identity | CASE, CLM, BOT, reports | User/role access contract and negative tests | A + dependent teams | Before user-specific UAT |
| DEP-04 | CASE-01/03 statuses | NOT-01/03, CLM-04 | Event, state machine and audit definitions | C+D+A | Before notification SIT |
| DEP-05 | CASE/CLM data | REF-01/02 | Rules and data semantics approved by business | C+D + PO | Prior to allocation verification |
| DEP-06 | REF approvals/results | RPT-03, DASH-03 | Authorized outcome/reconciliation definitions | D+E | Before dashboard/reports UAT |
| DEP-07 | CLM identity/status service | BOT-03 | Authenticated lookup contract and controlled error behavior | D+E | Before bot acceptance |
| DEP-08 | UX prototyping | CASE/CLM/REF implementations | Reviewed and accessible journey patterns | UX+teams | Before build refinement |
| DEP-09 | OPS CI/CD | QA tests and all services | Repeatable build/test, evidence capture | Shared leads | Continuously |
| DEP-10 | SIT/UAT and security | Go-live/handover | Exit criteria and residual risk authorization | QA/PO/PM | M3→M4 |

## Generic RAID categories for weekly inspection
- External source interface/access readiness (do not state real partner details on public Issues).
- Requirements/business rule decisions, especially allocation/approval semantics.
- Cross-team data contracts and version compatibility.
- Specialist capacity and staffing uncertainty.
- Accumulating quality, security and performance test debt.
- Contract deliverable evidence completeness.
- Production readiness and support continuity.

## Blocker protocol
1. Flag impacted issue `Blocked` in GitHub Project with plain, non-sensitive reason.
2. Record owner, when blocked, impact on Sprint Goal, next action and check-back date.
3. Coordinate cross-team issue at dependency sync; escalate only if local resolution fails.
4. At each Sprint Review/weekly PM checkpoint, revise forecasts and risks transparently.
5. Sensitive details remain in approved restricted tracker, referenced only by sanitized tracking ID.

## Public status
All dependencies are **planned/potential** and not marked currently blocked without confirmation. No resource assignment or external service availability is assumed.
