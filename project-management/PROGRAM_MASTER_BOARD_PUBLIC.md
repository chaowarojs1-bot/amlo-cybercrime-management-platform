# Program Master Scrum Board — Public / Read-Only Launch View

> **This is a static navigation view, not a live GitHub Projects board.** GitHub Issues are created; native Project Status, Squad, Iteration, Priority and blocked automation remain unconfigured. Do not infer development progress from issue creation.

## Product Goal
Build one connected, safe and auditable platform for case/intake, transaction insights, claims and controlled return-of-assets journeys, with authorized public service and management information.

## Workstream navigation
| Workstream | Epic items | User Story coverage | Scrum working view |
|---|---|---|---|
| Squad A: Platform & Integration | [Identity #5](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/5), [Config #6](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/6), [Notification #7](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/7), [Data/OCR #8](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/8) | IAM / CFG / NOT / INT | Integration & access baseline |
| Squad B: Transaction & Graph | [#9](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/9) | TXN | Analyst trace and graph |
| Squad C: Case | [#10](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/10) | CASE | Case lifecycle and audit |
| Squad D: Claim & Asset Return | [Claim #11](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/11), [Return #12](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/12) | CLM / REF | Claim-to-approved-return |
| Squad E: Citizen & Analytics | [Bot #13](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/13), [Reports #14](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/14), [Dashboard #15](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/15) | BOT / RPT / DASH | Authorized services and KPIs |
| Shared: Platform, Security, QA | [Ops #16](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/16), [Security #17](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/17), [Test/Release #18](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/18) | OPS / SEC / QA | Continuous quality |
| Cross-team | [UX #19](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/19), [Governance #20](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/20) | UX / GOV | Usability and contract trace |

## Proposed workflow (to implement on native Project)
`Product Backlog → Ready → In Progress → Code Review → Testing → PO Review → Done`

Track **Blocked = Yes/No** with owner/since/next step separately from the status column. Stages are **not currently assigned** through GitHub Projects; all story issue creation should be understood as *uncommitted Product Backlog proposals*.

## Views to build
- Program Board by Status and Sprint;
- one board per Squad (filter Squad);
- Product Backlog ordering (PO-managed);
- Current Sprint Goal / Sprint Backlog;
- Dependencies and blockers;
- Release acceptance gates and evidence readiness;
- Security/QA outcomes at public-safe summary level.

## Integrated delivery chains (illustrative)
- Data/OCR (#8) → Case (#10) → Claim (#11) → Return (#12) → Reporting (#14)
- Data/OCR (#8) → Transaction/Graph (#9) → Case (#10) → Dashboard (#15)
- Identity (#5) and Security (#17) are cross-cutting to all restricted services.
- Cloud/DevOps (#16) and QA (#18) support every Sprint Increment.

## Release tracker
| Phase | Contract checkpoint | Tracker |
|---|---|---|
| M1 | D30 management and risk | [#99](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/99) |
| M2 | D120 SRS/design/prototype | [#100](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/100) |
| M3 | D210 integrated system/tests | [#101](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/101) |
| M4 | D240 go-live/training/handover | [#102](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/102) |

## Review rhythm and live links
- [Open product work in GitHub Issues](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues?q=is%3Aissue+is%3Aopen)
- [Sprint planning placeholders](./SPRINT_ISSUE_REGISTER_PUBLIC.md)
- [Product Backlog Register](./PRODUCT_BACKLOG_REGISTER_PUBLIC.md)
- [Scrum Operations](./SCRUM_OPERATING_MODEL_PUBLIC.md)
- [Native GitHub Projects configuration blueprint](./GITHUB_PROJECT_BOARD_SETUP_PUBLIC.md)

**DoD != UAT != contractual acceptance.** No status, acceptance, team allocations or work completion is asserted by this launch view.
