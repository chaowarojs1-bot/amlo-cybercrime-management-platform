# TOR Capability Traceability — Public Index

**Important:** This is a capability-level index based on the existing public TOR summary. It is **not** a clause-by-clause contractual RTM. Exact clause IDs, private design/evidence and approved sign-off must be maintained in restricted project records and checked against original TOR.

| TOR capability | Epic | Representative story keys | Verification route | Gate |
|---|---|---|---|---|
| SSO / MFA | #5 | IAM-01…04 | Access role and authentication tests | M2 design → M3 test |
| System Configuration | #6 | CFG-01…04 | Parameter change and audit tests | M3 |
| Notification | #7 | NOT-01…04 | Event and delivery scenarios | M3 |
| Data Integration/OCR | #8 | INT-01…05 | Extraction/schema/validation/SIT | M2 interfaces → M3 |
| Transaction / Graph | #9 | TXN-01…05 | Search/graph/trace UAT | M3 |
| Case Management | #10 | CASE-01…05 | Case flow and audit UAT | M2 prototype → M3 |
| Claim Request | #11 | CLM-01…05 | Identity/claim/status UAT | M2 prototype → M3 |
| Asset Return | #12 | REF-01…05 | Approved rules and review workflow | M3 |
| Chatbot | #13 | BOT-01…04 | Language and authorized query testing | M3 |
| Reporting | #14 | RPT-01…04 | Reconciliation/export UAT | M3 |
| Dashboard | #15 | DASH-01…04 | KPI accuracy and user access tests | M3 |
| Cloud/Operations | #16 | OPS-01…05 | Platform readiness, rollout/restore | M2–M4 |
| Security & Privacy | #17 | SEC-01…05 | Controlled security assurance | M2–M4 |
| Quality & Acceptance | #18 | QA-01…06 | SIT/UAT/performance/acceptance | M2–M4 |
| UX | #19 | UX-01…04 | Prototype + usability evidence | M2/M3 |
| Governance | #20 | GOV-01…06 | Governance, risk, change, acceptance trace | M1–M4 |

## Internal controlled RTM required columns
TOR clause ID; source requirement text/version; affected capability; Product Backlog Item key; user/approver; acceptance criteria; design reference; test case/results; release package; issue/defect reference; final approval and date.

## Quality rules
- Never infer legal rules from a generated story. Authorized business/legal subject-matter experts approve decisions.
- Cross-team enablers and nonfunctional needs are first-class Product Backlog Items.
- Every formal deliverable must have an owner and evidence reference before submission.
- Keep actual confidential requirement excerpts and case/data examples out of this public repository.

See [Product Backlog register](./PRODUCT_BACKLOG_REGISTER_PUBLIC.md) and [TOR acceptance gates](./RELEASE_ACCEPTANCE_PUBLIC.md).
