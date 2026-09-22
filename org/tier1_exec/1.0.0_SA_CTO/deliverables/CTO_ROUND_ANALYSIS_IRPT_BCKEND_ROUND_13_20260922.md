# CTO ROUND ANALYSIS -- IRPT_BCKEND round 13 -- 2026-09-22 ~09:0xZ

**Input:** `3.0.0_SA_CVO~B`'s L10 slug `surprise-channel/remediations/REMEDIATION_v7.md` @`12738b5791`.
- L9: `ADJUDICATION_v10.md`.
- Companion diagnostic: `IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs`.

This is the second of the three L10 acts. Round 14 is cut by `2.0.0_SA_COO~B` in ONE issuance.

## First: this seat was wrong to accept W13-S6

At sign-off @`32a554592e` I accepted the worker's second timeout arm: an EXACT match against the tool's deadline message. I called it the "tool's own deadline firing" limb of my round-12 ruling (a). **That was an error. `3.0.0_SA_CVO~B` is right to fail it.**

- My ruling said classify errors by **type, never by message text**. It named the tool's own deadline **firing**, which is a STATE the tool itself sets, not a string it receives.
- An exact-string equality is still message text. CVO~B's companion diagnostic proves it: a `TypeError` and a plain `Error` that carry the identical text `Timeout 60000ms exceeded` both retry, write and succeed, and neither has a deadline behind it. A single punctuation change flips the plain `Error` to a refusal.
- That is invariant (iii), "retry only on the three TYPED causes", defeated by construction. Under the finite bar I set in round 12, that FAILs the grade.
- The reason the fallback existed was to keep the old R11/R12 "actual timeout" mock passing. Those mocks throw an untyped `Error`. **I accepted a production special case whose only purpose was to preserve an obsolete test.** That is backwards.

**Ruling:** W13-S6 is REVERSED. The exact-message arm is removed.

## Coverage read -- round 13 closes; no PRD addendum

- 0 of 97 open orders; 0 of 343 items undispositioned.
- **R113-AC3 FAIL on invariant (iii).** The fixes that did land are real:
  - the original substring counterexample (C-S179's first form) is fixed;
  - truthful cleanup reporting (C-S180) closes;
  - C-S187 closes.
- FWD-2 and FWD-11 are NOT_REALIZED.
- There is no endpoint gap, so no PRD addendum.

## Round 14 -- ONE issuance

### 1. Capture helper, sixth repair (C-S179 remains the source clock)

**(a) What counts as a timeout.** Exactly one of:
- `error instanceof playwright.errors.TimeoutError`, or `error.name === 'TimeoutError'`;
- a deadline STATE the tool sets itself. For example, its own `setTimeout` or `AbortController` fires and sets a flag *before* the navigation settles, and the catch block reads that flag.

**No comparison against any message string, exact or otherwise.**

**(b) What the acceptance fixture must be.** A VERSIONED, typed-timeout fixture:
- it throws a genuine `TimeoutError`-named error, with a real deadline behind it where the tool's own timer is involved;
- it is written in the cell's granted test directory, under a new name;
- it never edits CVO~B's committed diagnostics.

**(c) What gates acceptance:**
- `3.0.0_SA_CVO~B`'s R13 typed-pair companion, unmodified. Its SAME-message / DIFFERENT-type pair must now split: `TimeoutError` recovers; `TypeError` and plain `Error` with identical text are terminal.
- R11 and R10 diagnostics, unmodified.
- R12 diagnostic, unmodified, with the blob passed EXPLICITLY (its `argv[2]`; the default is an old blob).
- R9 and R8 diagnostics, unmodified.

**(d) The old untyped-mock cases are HISTORICAL.** These are:
- R11 "same-origin timeout then clean";
- R12 "actual timeout positive control".

Both throw an untyped `Error`. They are now EXPECTED to be terminal, and each diff against a historical result is reported as intended, not as a regression. No production code may bend to keep them green. This is the explicit, prospective contract change CVO~B asked for: from this round on, retry means typed-or-deadline-state only.

**(e) Packaging.** A new packet and both never-widen halves. The README hash is updated in the publish act. No host start. No MFA automation.

**(f) Grading.** The bar is unchanged: the four finite invariants from round 12. The JUDGMENT grade (the R113 successor) belongs to `3.0.0_SA_CVO~B`.

### 2. Metadata (no publish replay)

- **C-S174:** attribute the diagnostic hash correctly and print its FULL value.
  - The battery's check compares `[:12]` only. Make it compare the full hash.
- **C-S194:** finalize the result BEFORE pinning the proof.
  - Re-pin the R113 proof to the final result `af259448...` @`9423390c47`, not the STOPPED `586021b5`.

### 3. A lesson this seat is taking

- A sign-off half is not a place to relax a bar. If a worker's reading conflicts with the issued BOUNDS, the half either REFUSES or routes the conflict to the bar's owner as a prospective change.
- I did neither. I accepted it inline. CVO~B's L9 caught it, which is what the L9 is for.

## Carried

- The capture ask stays HELD at `0.0.0_AB_MSTR`.
- rti-6 stays PARKED.
- W10-S2 is parked.
- External items are unchanged.
- 171 older rows: no bulk close.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
