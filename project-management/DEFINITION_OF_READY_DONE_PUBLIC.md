# Definition of Ready / Definition of Done / Acceptance

## Definition of Ready (DoR): optional refinement aid, not a Scrum Guide commitment
A Product Backlog Item is generally suitable for Sprint Planning when:
- User/actor, value/outcome and boundaries are understandable.
- Epic and high-level TOR functional mapping exist.
- At least 2–3 verifiable acceptance conditions are written.
- External inputs, dependencies and compliance questions are identified.
- Development/test evidence route is possible using safe data.
- Developers can assess its size and split as necessary.
- Product Owner has ordered it with the Product Goal in mind.

**DoR must not become a bureaucratic gate** preventing teams from delivering valuable work or clarifying details inside the Sprint.

## Shared Definition of Done (DoD): mandatory quality standard
For an applicable working product Increment:
- [ ] Meets approved acceptance criteria and intended business process.
- [ ] Peer-reviewed changes incorporated; documented technical changes appropriate.
- [ ] Automated tests and relevant integration/regression checks pass.
- [ ] Role authorization, access denial, privacy handling and logging meet agreed controls.
- [ ] API/data schema compatibility and provenance/reconciliation are verified where applicable.
- [ ] Error handling, usability/accessibility and nonfunctional expectations are checked.
- [ ] No unresolved critical blocker or prohibited data disclosure exists for this item.
- [ ] Evidence and source/revision links are accessible to authorized reviewers.
- [ ] Product Owner can inspect demonstrable usable work at Sprint Review.
- [ ] Integrated with other Increment components and deployable in the agreed environment.

A documentation or planning item has a tailored verifiable output (peer-approved artifact) rather than pretending to be deployed code. The **common quality bar is not optional**.

## Acceptance separation
- **Story acceptance:** PO or delegate inspects the item and checks acceptance criteria.
- **Increment Done:** Developers confirm shared DoD. Items that do not meet DoD are not Done.
- **SIT/UAT:** separate structured verification and business acceptance evidence.
- **Contract/TOR gate:** formal package reviewed per contract; never automatically implied by closing GitHub Issues.

## Minimum issue evidence (PUBLIC view)
- PBI / Epic reference; Product Goal connection
- Acceptance checklist, reviewer, result status
- Link to PR/build/test summary that is approved for public sharing (otherwise safe reference only)
- Known follow-ups, verified dependencies, disposition of defects
- No real cases, claimant identities, bank statements, credentials, vulnerability descriptions or private system configurations.

## Working principle
Never use Story Points or ticket completion alone as evidence of contract acceptance; require delivered usable capability, verification and documented sign-off.
