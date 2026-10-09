# Release & TOR Acceptance Governance — Public/Sanitized

This is a proposed evidence-management plan. Formal contract, TOR originals and authorized decisions remain controlling. Sprint Reviews do not themselves constitute TOR contractual acceptance.

## Four mandatory contractual delivery checkpoints
| Gate | Due (day from contract) | Public evidence summary | Working readiness checks | Acceptance / outcome |
|---|---|---|---|---|
| M1 | D30 | Project Management Plan, Kick-off Report, Risk Management Plan | Organization, roles, governance, risk baseline, workshop plan | Formal submission and client review |
| M2 | D120 | Preliminary, SRS, validation, functional/software design, prototype, UX/UI, test planning/artifacts, architecture | Signed-off requirements/design baseline; validated prototype and traceability | Formal submission and client review |
| M3 | D210 | Developed system, ERD, Data Dictionary, SIT/UAT, Security Test, Performance Test | Integrated release, test summaries, remediation/evidence, acceptance review | Formal submission and client review |
| M4 | D240 | Training, manuals, go-live/cloud deployment, source handover, documents, Final Report | Cutover/runbook, support, knowledge transfer, evidence index, formal closeout | Formal submission and client review |

The publicly documented payment shares are 10% / 30% / 40% / 20%; those do not establish actual payment status.

## Evidence checklist by phase
### M1 — Plan and governance
- [ ] PM plan, stakeholder and role governance, schedule baseline and change control.
- [ ] Kick-off agenda/minutes, communications and escalation plan.
- [ ] Initial risk plan and secure document control.
### M2 — Requirement and design package
- [ ] Requirement validation workshop evidence and approved SRS.
- [ ] Functional, UX, architecture, data/interface and security design views.
- [ ] Prototype demonstration, usability notes and relevant test approach.
- [ ] TOR-to-requirement-to-story cross-reference (detailed matrix stored privately).
### M3 — Build and verification
- [ ] Build/version inventory and deployment evidence (restricted where sensitive).
- [ ] ERD/Data Dictionary and reconciled interfaces.
- [ ] SIT/UAT evidence, results/defects, performance test and security-test acceptance **without publishing findings**.
- [ ] PO/business review and outstanding exception/risk disposition.
### M4 — Production and transfer
- [ ] Production readiness and approved cutover/rollback results.
- [ ] User/admin training records and manuals.
- [ ] Source code/configuration transfer and operational handover under controlled channels.
- [ ] Closeout report, open-item transfer and client delivery record.

## Explicit distinction
1. GitHub Issue `Done` = shared Scrum Definition of Done satisfied.
2. Integrated Increment demonstrated = Sprint Review visibility.
3. SIT/UAT accepted = verification and business acceptance recorded.
4. TOR milestone accepted = authorized contractual review/signature per contract.

## Cross-cutting exit rules
- No work is accepted purely because a card changed to Done.
- Critical security issues are managed only in private authorized trackers.
- Decisions about legal entitlement or asset allocation stay with authorized human reviewers.
- Public issues/README store safe summary and reference IDs, not confidential approval documents.
- Contract start and exact dates are tentative until formal baseline confirmed.

## Links
See [public TOR summary](../docs/TOR_SUMMARY_PUBLIC.md), [Product Backlog](./PRODUCT_BACKLOG_REGISTER_PUBLIC.md), and [Sprint Roadmap](./SPRINT_ROADMAP_PUBLIC.md).
