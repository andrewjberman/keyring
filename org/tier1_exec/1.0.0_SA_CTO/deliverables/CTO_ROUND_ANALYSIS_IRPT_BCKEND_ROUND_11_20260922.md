# CTO ROUND ANALYSIS -- IRPT_BCKEND round 11 -- 2026-09-22 ~04:5xZ

**Input:** `3.0.0_SA_CVO~B`'s L10 slug `surprise-channel/remediations/REMEDIATION_v5.md` @`d20200b92c`.
- L9 is `ADJUDICATION_v8.md` (C-S169..C-S177) at the same commit.
- The diagnostic is `IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs`, also at the same commit.

This is the second of the three L10 acts. Round 12 is cut by `2.0.0_SA_COO~B` in ONE issuance.

## Coverage read -- round 11 closes; no PRD addendum

- Round state: 0 of 95 open orders; 0 of 338 worker items undispositioned.
- **R107-AC3 FAIL (C-S169).** The two R10 residuals now refuse. Two new lifecycle defects remain:
  - **C-S170, ARMED.** The last `refuseIfLatched()` runs BEFORE `await context.storageState()`. A foreign navigation during that await latches and still writes. This gap pre-dates this round.
  - **C-S171, ARMED.** The response listener has no navigation filter. A foreign NON-navigation resource response wrongly refuses a valid capture. This over-refusal is NEW this round.
- FWD-2 and FWD-11 are NOT_REALIZED.
- There is no PRD addendum. The gap is a cell under an existing outcome.

## The pattern, and what changes because of it

This is the fourth capture repair, and each round's diagnostic has found the next hole. The repairs are correct as far as they reach. The recurring cause is that each fix guards a POINT in the lifecycle rather than the INVARIANT.

**Round 12's design direction therefore states the invariant and puts the check at the ONE place the file is written.**

## Round 12 -- ONE issuance

### 1. Capture helper, fourth repair (C-S170, C-S171; C-S153 and C-S127 stay armed until this passes)

**(a) INVARIANT: no bytes reach disk unless the latch is clear AFTER the state was captured.**
- Capture state to MEMORY: `storageState()` with no `path`.
- Then check the latch.
- Only then write the file, atomically: write to a temp file, then rename.
- Check the latch again immediately after the rename. If it has set, delete the file and exit non-zero.
- This makes the timing of any navigation irrelevant, because the check follows the last await that could admit one.

**(b) The observer's scope is MAIN-FRAME NAVIGATIONS ONLY.**
- Use `request.isNavigationRequest()` and `frame === page.mainFrame()`, on both the request and the response paths.
- Foreign subresources (fonts, analytics, CDNs) never latch. This closes C-S171.
- Stated precisely: the property is WHERE THE PAGE IS, not what it loads.

**(c) Retry taxonomy (W13-S1): behaviour and documentation must agree.**
- The code retries exactly the set the README lists. Choose ONE: timeout, 5xx, and marker-absent-after-load.
- Any other outcome is a terminal refusal with its cause printed.
- A foreign origin is never retryable.

**(d) Acceptance.** The following run unmodified and must hold:
- `3.0.0_SA_CVO~B`'s diagnostics R11, R10, R9 and R8. R11 must refuse the final-await case AND must succeed on both same-origin twins (the navigation twin and the resource twin).
- A single-difference pair for each of (a) and (b), each with a positive control.

**(e) Publication.**
- New packet and both halves. The README hash is updated in the publish act.
- No host start. No MFA automation.

**(f) Grading.** The JUDGMENT grade (the R107 successor) is `3.0.0_SA_CVO~B`'s.

### 2. C-S174 metadata

- Reconcile the rti-1 and rtk-1 proof and result files: the post-publish state, the hash grain, and the W13-S2 final evidence. No publish replay.
- `2.0.0_SA_COO~B` owns reconciling the retained recovery worktree `C:/tmp/wk-irpt-11-13b`: its uncommitted proof edit and its `.scratch/`.
  - Commit what is evidence.
  - Remove the worktree ONLY after reading what it holds. It is not to be consumed as delivered proof.

### 3. W13-S2 ruling

- This seat concurs with `3.0.0_SA_CVO~B`: refusing a grant on a terminal order is documented law, not a gate defect.
- No finished order's grant is widened.

## Carried

- The capture ask stays HELD at `0.0.0_AB_MSTR`.
- rti-6 stays PARKED.
- W10-S2 is parked.
- External items are unchanged.
- 166 older stale rows, disclosed; no bulk close.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
