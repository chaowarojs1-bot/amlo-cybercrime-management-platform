# Scrum Operating Model — AMLO Cybercrime (Public/Sanitized)

> **Status:** Proposed working model for Product Owner and Scrum Teams to approve. Repository is PUBLIC. Never publish case/victim/banking records, private legal annexes, real environment configs, access credentials, internal endpoints or vulnerability findings.

## Product Goal
Deliver a secure, connected platform that enables authorized staff to intake and correlate information, manage cases, support victim/claim journeys and execute controlled, auditable asset-return processes; provide understandable status and management information. Business/legal decisions remain with authorized humans.

## Product scope and accountabilities
- **One Product / one accountable Product Owner** for the cross-system Product Backlog: orders items, explains value and accepts business outcomes. Appoint by client/project governance; not assumed named.
- **Scrum Masters:** establish Scrum effectiveness and remove impediments. One person may coach more than one team, if capacity allows; role to be confirmed.
- **Developers:** cross-functional accountable professionals who plan, estimate, build, test, integrate and verify a usable Increment every Sprint; include BA/SA/QA/security/DevOps expertise as needed.
- **Project Manager / Contract Governance (complementary, not substitute for Scrum):** maintain TOR milestones, submission packages, RAID/risks, communications and approval evidence.
- **Stakeholders:** program sponsor, business owners, legal/compliance, authorized operations, external source coordinators, UAT representatives.

## Proposed cross-functional team boundaries
| Workstream | Capability ownership | Epic reference |
|---|---|---|
| Squad A — Platform & Integration | SSO, configuration, notification, API/document processing | #5–#8 |
| Squad B — Transaction & Analytics | Transaction/graph | #9 |
| Squad C — Case Operations | Case management | #10 |
| Squad D — Claim & Return | Claim, asset distribution | #11–#12 |
| Squad E — Citizen Service & BI | Chatbot, reports, dashboards | #13–#15 |
| Shared service enablers | Cloud/DevOps, security, test/release | #16–#18 |
| Cross-team | UX and Scrum governance | #19–#20 |

These are planning streams, **not** automatically separate Scrum Teams. Confirm staffing and assign real Scrum Teams; minimize handoffs and integrate continuously. Avoid independent “Done” claims for code that does not meet common DoD.

## Scrum accountabilities, events, artifacts, commitments
| Element | AMLO adoption |
|---|---|
| Product Backlog → **Product Goal** | One ordered, emergent backlog, with 11 capabilities plus common controls and TOR evidence. Product Owner accountable; Developers size items. |
| Sprint Backlog → **Sprint Goal** | Each participating Scrum Team selects Product Backlog Items and its plan at Sprint Planning; forecast in Issues is **not** a commitment. |
| Increment → **Definition of Done** | Integrated, usable, verifiable capability with evidence; can produce several Increments within one Sprint. |
| Sprint | Proposed synchronized **14-calendar-day planning windows**, S01–S17, subject to team agreement. |
| Sprint Planning | Begin each Sprint: why this Sprint is valuable, what can be Done, and how. Start with available capacity, known risk and Sprint Goal. |
| Daily Scrum | Developers meet 15 minutes each working day; inspect progress toward Sprint Goal and adapt. |
| Sprint Review | End of Sprint: demonstrate real integrated work to PO and stakeholders, inspect Product Goal progress, adapt Product Backlog. Not a contractual acceptance ceremony. |
| Sprint Retrospective | End of Sprint: improve quality, effectiveness and collaboration; track actions in team. |
| Product Backlog refinement | Ongoing PO + Developers activity: split/order/clarify/test dependencies and estimate. |
| Cross-team Integration/Dependency Sync | Proposed 2–3 sessions weekly when needed; resolves cross-team blockers without replacing Scrum events. |

## Issue/board policies
- **Issue hierarchy:** Epic → User Story / Product Backlog Item → optional tasks/checklists. Defects reference impacted story.
- **Workflow:** Product Backlog → Ready → In Progress → Code Review → Testing → PO Review → Done. `Blocked` is a flag/reason/owner, not an alternative substitute for stage.
- **Mandatory on a story:** testable acceptance, Epic, Squad, dependencies, PO priority decision, estimate from Developers, evidence, TOR capability mapping.
- **WIP:** each Scrum Team sets realistic in-progress and review limits; favor finish-over-start.
- **Done:** only when shared DoD holds. Contractual deliverable acceptance is separately tracked in Release/Acceptance view.
- **Security:** use synthetic sample data; confidential implementation evidence and defect specifics only in approved restricted systems.
- **No velocity-as-performance ranking:** use flow, predictability, outcomes and quality for inspection, never individual productivity scoring.

## Governance overlay: Hybrid Scrum + contractual checkpoints
- Keep TOR submission D30, D120, D210, D240 (4 contractual packages) separate from Sprint reviews.
- A checkpoint is not a Sprint boundary by default; readiness is tracked in Release & Acceptance view.
- Planned intermediate gates D60, D90, D175, D195, D205, D225 are management targets only, not TOR deadlines.
- Roles, sprint capacity, external access, final start date, acceptance reviewers and security approvals are **TBD** and must be formally confirmed.

## Sources
Derived from public/sanitized repository summaries: [TOR summary](../docs/TOR_SUMMARY_PUBLIC.md), [Project Master Plan](./PROJECT_MASTER_PLAN_PUBLIC.md), [Roadmap](../roadmap/ROADMAP.md). Scrum adaptation is a proposed management design; the TOR does not itself specify Scrum roles, team counts, Story Points or Sprint schedule.
