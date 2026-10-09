# Sprint Roadmap — proposed 14-day synchronized cadence

> This is a forecast for refinement. **Only Sprint Planning creates a Sprint Backlog and Sprint Goal**. The Scrum Team must account for staffing, real capacity and current Product Backlog. No start date has been contractually confirmed.

## Timeline
- Existing public project schedule uses **1 Oct 2026 as planning baseline only**, not asserted actual contract commencement.
- D1–D238: 17 sequential 14-calendar-day Sprint planning windows.
- D239–D240: contractual closeout/acceptance buffer, not a substitute for an extra unofficial Sprint.
- Do not pre-assign teams or Story Points until Scrum roles and staffing confirmed.

| Sprint | Contract days | Indicative dates* | Proposed review theme (subject to Sprint Goal) |
|---|---|---|---|
| S01 | D1–D14 | 2026-10-01 – 2026-10-14 | Product goal, ownership, kickoff, initial requirement intake |
| S02 | D15–D28 | 2026-10-15 – 2026-10-28 | Source contracts, security baseline, environment decisions |
| S03 | D29–D42 | 2026-10-29 – 2026-11-11 | D30/M1 package; user journeys and validation plan |
| S04 | D43–D56 | 2026-11-12 – 2026-11-25 | SRS/architecture working slices, OCR, case states |
| S05 | D57–D70 | 2026-11-26 – 2026-12-09 | Data/entity models and prototype walkthrough |
| S06 | D71–D84 | 2026-12-10 – 2026-12-23 | Claim prototype, shared configuration and notification events |
| S07 | D85–D98 | 2026-12-24 – 2027-01-06 | Integrated ingestion and case record slice |
| S08 | D99–D112 | 2027-01-07 – 2027-01-20 | Case history, access controls and early notification slice |
| S09 | D113–D126 | 2027-01-21 – 2027-02-03 | D120/M2 baseline; usable demo and approved design package |
| S10 | D127–D140 | 2027-02-04 – 2027-02-17 | Graph exploration and calculation preview |
| S11 | D141–D154 | 2027-02-18 – 2027-03-03 | Integrated data reconciliation, first reports/analytics |
| S12 | D155–D168 | 2027-03-04 – 2027-03-17 | Claim review and return approval vertical slice |
| S13 | D169–D182 | 2027-03-18 – 2027-03-31 | Feature-complete target D175; report/dashboard/SIT breadth |
| S14 | D183–D196 | 2027-04-01 – 2027-04-14 | End-to-end functional verification, fixes and UAT rehearsal |
| S15 | D197–D210 | 2027-04-15 – 2027-04-28 | D210/M3 package; SIT, UAT and security/performance evidence |
| S16 | D211–D224 | 2027-04-29 – 2027-05-12 | Hardening, production readiness, training and cutover rehearsal |
| S17 | D225–D238 | 2027-05-13 – 2027-05-26 | Go-live support, handover, final UAT/residual fixes |

*Illustrative only. Recalculate calendar dates from signed contract start; contractual schedule prevails.*

## TOR stage-gates (independent from Sprints)
| Gate | Due | Evidence group |
|---|---|---|
| M1 | D30 (forecast 2026-10-30) | Project Management Plan, Kick-off, Risk Management Plan |
| M2 | D120 (forecast 2027-01-28) | Requirement/SRS/design/prototype/architecture and test planning |
| M3 | D210 (forecast 2027-04-28) | Implemented system, ERD/DD, SIT/UAT, security and performance testing |
| M4 | D240 (forecast 2027-05-28) | Training, manuals, go-live, handover/source code, final report |

## Sprint planning/review operating checklist
1. **Before Planning:** PO has ordered, clarified Product Backlog and agrees Product Goal; Developers know capacity, risks, necessary skills and technical debt.
2. **Planning:** choose Sprint Goal and realistic set of stories; Developers identify subtasks, test strategy, pairings and interfaces.
3. **Daily Scrum:** inspect Sprint Goal and adjust; blocked dependencies escalate to shared integration sync.
4. **Continuous integration:** vertical slices test across API/data, case, claim/return and reporting; never defer all system integration until M3.
5. **Review:** present usable Increment with acceptance observations and update Product Backlog.
6. **Retrospective:** record one or two improvement actions and verify next Sprint.
7. **Gate review:** separate PM/PO, QA and business approval process validates TOR delivery artifacts before submission.

## Planning guardrails
- Intermediate D60 / D90 / D175 / D195 / D205 / D225 points in the existing public roadmap are **internal forecasts** only.
- Feature complete means planned functionality implemented, not final acceptance.
- Sprint Review and UAT/contract acceptance are distinct.
- Reserve capacity each Sprint for quality, security, integration, review and defects. No fabricated team velocities.
