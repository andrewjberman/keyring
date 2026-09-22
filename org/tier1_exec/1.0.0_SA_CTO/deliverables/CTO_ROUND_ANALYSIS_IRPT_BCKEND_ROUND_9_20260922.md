# CTO ROUND ANALYSIS -- IRPT_BCKEND round 9 -- 2026-09-22 ~00:2xZ

**Inputs:**
- `3.0.0_SA_CVO~B`'s L10 slug: `surprise-channel/remediations/REMEDIATION_v3.md` @`a62b69f6d3` (9 rows).
- L9: `ADJUDICATION_v5.md`, same pin.

Second of the three L10 acts (Rule 27). Round 10 is cut by `2.0.0_SA_COO~B` in ONE issuance.

## FIRST: a correction to this seat's own ruling -- the capture is NOT ready, and the ask to Andrew is RE-HELD

My rti-6 park ruling @`4a773b6ae3` said un-park condition (1) was MET because the fixed tool was published, and it called the ask to Andrew UNBLOCKED. **Both statements were wrong.** The tool was published, but it was not FIXED. CVO~B's round-9 grade shows two things:

- **R91-AC7 FAIL / C-S153.** The helper discards the response to its first `page.goto`. A session that goes portal -> foreign origin -> portal, then authenticates validly, is written once and reported as success. So S127's origin guarantee does not hold across the whole navigation lifecycle. The six-arm diagnostic is at `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R9_CAPTURE_REDIRECT_DIAGNOSTIC.cjs`.
- **C-S156.** The README starts the host and invokes the local wrapper without first delivering the fixed bytes or checking their hashes. The only sync that is documented sits inside the render command document, not in host start. **A human following the runbook today would run the OLD, defective tool.** My sign-off said "no on-host verification is claimed". CVO~B is right that the runbook then asks for a credential on bytes nobody has verified.

**Amended un-park condition (1).** All three parts are required:
- (a) the capture helper passes CVO~B's redirect diagnostic;
- (b) it passes its own single-difference initial-foreign-return regression plus a positive control;
- (c) the human runbook delivers the fixed bytes to the host and verifies both hashes BEFORE any capture or credential entry.

Conditions (2)-(4) are unchanged. **The ask to Andrew is HELD again until the amended (1) is met.**

My CTO sign-off half @`93dda7a939` stands for what it covered: the S3 publish, its blast radius and its rollback. That act was correct and reversible. It did not claim, and never covered, readiness to capture.

## Coverage read -- round 9 closes; no PRD addendum

**Round state:**
- 0 of 91 orders open; 0 of 336 investigation items undispositioned.
- R92-AC3 PASS: true-source provenance only.
- R93-AC3 NOT_EVALUATED: 0 of 2 discriminated.
- R91-AC7 FAIL.

**Outcomes:**
- FWD-2 is SPLIT and NOT_REALIZED.
- FWD-11: backend ADVANCED; overall NOT_REALIZED.
- Nothing claims REALIZED.

**Why no PRD addendum:**
- Every gap is a cell under an existing outcome.
- The capture defect is a tooling defect, not an endpoint mis-statement.

## Round 10 -- ONE issuance; wave 1 in parallel

**1. Capture helper second repair (C-S153, C-S127).**
- Guard the complete navigation lifecycle: the initial response, every hop, and the interactive interval.
- Acceptance:
  - CVO~B's redirect diagnostic, unmodified, refuses every counterexample arm.
  - The round-8 diagnostic still passes.
  - A single-difference initial-foreign-return regression.
  - An authenticated-positive control.
- Constraints:
  - No allowlist widening, and no MFA automation.
  - Fold in W9-S1: derive the allowlist from `IRPT_PORTAL_ORIGIN` (`ssm.tf:84`), or fail on drift.
- A new publish needs a new packet and both halves.

**2. Host delivery runbook (C-S156).** This may be the same cell as item 1 if the write paths overlap; COO~B decides from the decomposition.
- The README establishes the fixed bytes on the host and prints both hashes, which must equal the packet table, BEFORE the helper runs.
- No render is used to side-load tools.
- The mechanism must be an explicit, printed step, e.g. a documented `aws s3 cp` of exactly the two keys plus a `sha256sum` check.

**3. L4 bounded test principal (W11-S1).**
- As ruled in 99312: an AE/CloudOps lane, CTO + CRO halves, ListBucket on 2 targets + 1 control, then deletion verified by NoSuchEntity.

**4. Metadata repair (C-S154).**
- Reconcile the final rti-1 proof pins, the result/exclusions and the compiler summary.
- Do NOT replay the publish.

**5. Source-map note (W10-S3).**
- Through a lane holding the source-map grant.
- Correct the note only; no deploy scope.

**Carried, not cut:**
- W10-S2: the ycharts redeploy stays PARKED on its un-park condition.
- rti-6 stays PARKED under the amended condition (1).
- S116 and W1-S47 are external, in this seat's naming lane.
- Break-glass role deletion is at Andrew (open-calls card 3).
- The 159 older stale rows: no bulk close.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
