# GitHub Projects v2 — Board Configuration Blueprint

**Status:** Configuration specification only. Epics and Stories are already GitHub Issues. **A native GitHub Projects v2 board, fields, iterations and automation have NOT been provisioned via this connection**; they require an authorized Projects administrator / GitHub UI access. Do not mistake planning files for an active board.

## Create one program-level GitHub Project
Suggested project title: `AMLO Cybercrime — Program Scrum`

### Fields
| Field | Type | Suggested values |
|---|---|---|
| Status | Single select | Product Backlog, Ready, In Progress, Code Review, Testing, PO Review, Done |
| Type | Single select | Epic, Story, Task, Bug, Enabler, Gate |
| Squad | Single select | A Platform, B Analytics, C Case, D Claim/Refund, E Citizen/BI, Shared, Cross-team |
| Priority | Single select | P0 Critical, P1 High, P2 Normal, P3 Later (confirm with PO) |
| Sprint | Iteration | 2-week planning cycle, adjusted from signed start date |
| Target Gate | Single select | D30, D120, D210, D240, Not Applicable |
| Story Points | Number | Blank until Developers estimate |
| Blocked | Single select | No, Yes |
| Blocked Since | Date | Only if blocked |
| Owner | Person | Assign after staffing confirmed |
| Due / forecast | Date | Optional: only for real deadlines or tracked forecast |
| Dependency Reference | Text | GitHub Issue key/link or safe dependency ID |
| Evidence/RTM Reference | Text | Public-safe ID or approved restricted reference |

Use the Project's built-in `Assignees` field when appropriate. Do not pre-assign fake staff or dates.

### Saved views
1. **Program Master Board** — Board grouped by Status; show Squad, Priority, Sprint, Blocked and Gate; filters exclude closed duplicates.
2. **Product Backlog** — Table ordered by Priority, Epic/Product Value, dependencies and PO order; all Stories not assigned to current Sprint.
3. **Squad A–E** — Board view filtered by Squad with common workflow.
4. **Current Sprint** — Board/table filter Sprint = current iteration, show Sprint Goal reference.
5. **Dependency Watch** — Table filter Blocked = Yes, columns owner/blocked-since/dependency.
6. **Release & TOR Gate** — Table/group by Target Gate; link milestone acceptance issues.
7. **Quality & Security** — View by Shared QA/Security issues and open release-blocking bugs (no restricted details).
8. **Executive Overview** — Summary by status, gate, team, due risks and accepted work (never fabricate % completion).

### Workflow and automation guidance
- Newly added Story → Product Backlog by default; add item to Program Project.
- Pull request checks/reviews may inform Code Review or Testing, but must not automatically mark Done without meeting DoD.
- Done only after quality review; contractual acceptance recorded separately.
- Flag Blocked on current stage, enter owner/reason/next action in safe form; clear only after verification.
- At Sprint Planning select a realistic set, agree Sprint Goal and assign current Sprint field.
- Once items pass the Done policy, close Issues. Do not use closing as a shortcut for formal acceptance.
- Use Project charts for item throughput/aging; evidence completeness and actual release risks require separate inspection.

## Procedure for admin
1. Open repository owner GitHub Projects and create a new Project (board/table template).
2. Add this repository's Issues to the Project; ensure repo connection or manual bulk-add.
3. Create custom fields above and views with appropriate filters.
4. Establish write permissions; Product Owner sets ordering, Developers maintain estimates/status.
5. Configure initial iterations aligned to signed start date; **do not lock Oct 1 2026 as actual without confirmation**.
6. Review field mapping with team and update Issue templates if Project configuration changes.

## Public disclosure
This repository is public. Never put live identities/case records, contract-confidential material, private network details or security vulnerabilities into Projects custom text fields.
