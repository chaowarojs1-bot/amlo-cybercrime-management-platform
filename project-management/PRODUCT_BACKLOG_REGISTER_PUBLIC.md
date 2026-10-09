# Product Backlog Register — Public/Sanitized

**Source of truth for work state:** GitHub Issues. This register indexes planning coverage; open individual Issues for Acceptance Criteria, dependencies and forecasts. No items below are implied to be developed, committed or accepted.

**Product Goal:** See [Scrum Operating Model](./SCRUM_OPERATING_MODEL_PUBLIC.md).

## Capability-to-Epic / Story coverage

| Epic | Stream | Area | Stories | Issue range | Initial ordering band |
|---|---|---|---|---|---|
| [#5](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/5) | A / IAM | SSO, MFA, RBAC | IAM-01…04 | #21–#24 | P0 |
| [#6](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/6) | A / CFG | System Configuration | CFG-01…04 | #25–#28 | P1 |
| [#7](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/7) | A / NOT | Notification | NOT-01…04 | #29–#32 | P1 |
| [#8](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/8) | A / INT | Data Integration + OCR | INT-01…05 | #33–#37 | P0 |
| [#9](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/9) | B / TXN | Transaction + Graph | TXN-01…05 | #38–#40, #44–#45 | P0 |
| [#10](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/10) | C / CASE | Case Management | CASE-01…05 | #46–#50 | P0 |
| [#11](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/11) | D / CLM | Claim Request | CLM-01…05 | #51–#55 | P0 |
| [#12](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/12) | D / REF | Asset Return/Distribution | REF-01…05 | #56–#60 | P0 |
| [#13](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/13) | E / BOT | Chatbot | BOT-01…04 | #61–#64 | P1 |
| [#14](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/14) | E / RPT | Reporting | RPT-01…04 | #65–#68 | P1 |
| [#15](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/15) | E / DASH | Dashboard | DASH-01…04 | #69–#72 | P1 |
| [#16](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/16) | Shared / OPS | Cloud + DevOps | OPS-01…05 | #73–#77 | P0 |
| [#17](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/17) | Shared / SEC | Security, Privacy, Audit | SEC-01…05 | #78–#82 | P0 |
| [#18](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/18) | Shared / QA | SIT, UAT, Release | QA-01…06 | #83–#87, #98 | P0 |
| [#19](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/19) | Cross-team / UX | UX / Prototype | UX-01…04 | #88–#91 | P1 |
| [#20](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/20) | Cross-team / GOV | Scrum + TOR governance | GOV-01…06 | #92–#97 | P0 |

## TOR capabilities (11 required groups)
1. SSO → EP-01
2. Configuration → EP-02
3. Notification → EP-03
4. Data Integration (incl. document/OCR processing) → EP-04
5. Transaction Analysis & Graph → EP-05
6. Case Management → EP-06
7. Claim Request → EP-07
8. Asset Return Distribution → EP-08
9. Chatbot → EP-09
10. Reporting → EP-10
11. Dashboard / Data Visualization → EP-11

Enabling delivery and acceptance: EP-12 Cloud/DevOps, EP-13 Security/Privacy/Audit, EP-14 Quality/Release, EP-15 UX, EP-16 Scrum Governance. Existing Issues [#1](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/1) – [#4](https://github.com/chaowarojs1-bot/amlo-cybercrime-management-platform/issues/4) are retained as the initial management/discovery baseline; avoid duplicate work.

## Prioritization and refinement protocol
- `P0 / P1 / P2` values are **suggestions**, not Product Owner decisions. Prioritize value, risk, external lead time and integrated usefulness.
- Developers own sizing: **no invented Story Points**. Estimate during refinement; split any item too large for a Sprint.
- Forecast `Sxx` in issue bodies is a tentative target, **not Sprint Backlog membership** or a fixed date commitment.
- Business/legal policy and validation of allocation calculations must be signed off by authorized AMLO reviewers.
- Use links such as `Depends on: #issue` and `Blocked by` for real dependencies; cited keys in user stories are initial planning signals.
- Clause-level TOR RTM, private architecture and actual data remains in approved controlled workspace; put only a safe reference/status here.
- All stories include Acceptance Criteria. Record test evidence and business review before Done per shared DoD.

## Status clarity
- **Product Backlog / Ready / In Progress / Code Review / Testing / PO Review / Done** are workflow stages for Scrum work.
- **Accepted at Contract Gate** is a separate stage tracked at D30/D120/D210/D240, not synonymous with Done.
- Issues #41–#43 are closed duplicates of canonical TXN stories #38–#40 and should not be counted as open backlog.

## Missing decisions for baseline
Product Owner, teams and capacity, estimates, actual contract start, integration access, and acceptance approvers remain unspecified. Until approved, all sprint forecasts and priorities are proposals.
