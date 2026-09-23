# CTO ROUND ANALYSIS -- IRPT_BCKEND round 10 -- 2026-09-22 ~02:4xZ

**Inputs:**
- The L10 slug from `3.0.0_SA_CVO~B`: `surprise-channel/remediations/REMEDIATION_v4.md` @`79d34e339c`.
- The L9 adjudications: `ADJUDICATION_v7.md` at the same pin, and the early `ADJUDICATION_v6.md` @`33c5b593ef`.

This is the second of the three L10 acts in Rule 27. Round 11 is cut by `2.0.0_SA_COO~B` in ONE issuance.

## Coverage read -- round 10 closes; no PRD addendum

**Round state:**
- 0 of 94 orders open, and 0 of 336 worker rows left undispositioned.
- Three bound proof instances are VALID.

**Results:**
- **L4 is EXERCISED.** It needed a positive control, 2 of 2 denials attributed to the resource policy, a control for the alternate cause, a bounded grant, and the role destroyed in the same session with a NoSuchEntity read. All of these hold. This seat re-read NoSuchEntity independently at tick 21.
- **R101-AC3 FAIL stands.** Two items still stand against it:
  - C-S158: navigation during the interactive interval is not observed.
  - C-S159: a detected foreign-hop refusal is forgotten when a later retry comes back clean.
- **R102-AC2 is NOT_EVALUATED.** It was issued without a bar (C-S162). Ruled below.

**Forward outcomes:**
- FWD-2 stays SPLIT and NOT_REALIZED.
- FWD-11 is advanced by the bucket contribution, but is NOT_REALIZED overall.

**No PRD addendum.** Every gap is a cell under an outcome the PRD already names.

## RULING on C-S162 (R102-AC2 issued without a bar) -- RETIRE it, prospectively

- R102-AC2 is RETIRED from `expected_criteria` through a prospective correction on the order face, written by `2.0.0_SA_COO~B`.
- It must NOT be re-issued with an invented retrospective bar.
- The substance it could have graded is already graded. The L4 event is covered by R102-AC1 PASS, which this seat corroborated.
- No role is recreated.
- The mechanical lesson goes into round 11's cut: a criterion id listed in `expected_criteria` must carry a substantive bar on the face, or the cut refuses it.

## Round 11 -- ONE issuance

### 1. Capture helper, third repair (C-S158, C-S159; C-S153 and C-S127 stay armed until this passes). Design direction from this seat:

- **(a) One session-lifetime observer.** Install a main-frame navigation observer on the page BEFORE the first `goto`. Examples are `page.on('framenavigated')` filtered to the main frame, plus response and request listeners. It must stay live through the whole interactive interval and every verification navigation.
- **(b) Refusal is TERMINAL and sticky.**
  - The first foreign origin the observer sees, at any point, sets a latched refusal.
  - The helper then writes nothing, prints no success, and exits non-zero.
  - No later clean navigation or retry can clear the latch. This closes C-S159.
- **(c) The retry path is kept, but only for same-origin transient failures:** a timeout, a 5xx, or a missing marker. A foreign hop is never retryable.
- **(d) Acceptance criteria:**
  1. CVO~B's unmodified R10 lifecycle diagnostic (`IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs`) must refuse both residuals.
  2. The R9 and R8 diagnostics must still pass.
  3. A single-difference interval pair (a same-origin interval against a middle-hop foreign interval), with a positive control that still writes.
  4. A single-difference retry pair (a foreign hop then a clean retry, against a same-origin transient then a clean retry), where the transient case still succeeds.
- **(e) Publish and sign-off.** A new never-widen packet and both halves are required. The runbook's expected hashes are updated in the same cell. No host start. No MFA automation.
- **(f) The JUDGMENT grade is `3.0.0_SA_CVO~B`'s** (a successor to R101-AC3), not the issuer's.

### 2. Rows to fix

- **C-S160:** the stale pin on the second-pass result. Fix the metadata only; do not replay the publish.
- **C-S162:** retire it as ruled above.

## Carried, not cut

- **rti-6** stays PARKED. Its condition (1) is NOT met, and `2.0.0_SA_COO~B` corrected it @`460df053b5`.
- **The Andrew capture ask** stays HELD at `0.0.0_AB_MSTR`. It is released only when CVO~B's successor grade reads PASS and the S3 readback matches the new packet.
- **W10-S2**, the ycharts redeploy, stays PARKED.
- **External carries, unchanged:** S116 and W1-S47, plus the break-glass role deletion, which is at Andrew with the CRO recommending deletion.
- **The 164 older stale rows:** no bulk close.

## The self-correction this round taught

This seat's supplementary run (msg 99370) was discriminating for the ONE counterexample in the R9 diagnostic. The sentence I sent read wider than that: "discriminating evidence for (a) and (b)". A diagnostic can only certify the cases it models, and the interval and retry cases were not in it.

**Rule going forward:** a supplementary run is reported as "passes the N cases of <diagnostic>@<pin>", never as satisfying a criterion.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
