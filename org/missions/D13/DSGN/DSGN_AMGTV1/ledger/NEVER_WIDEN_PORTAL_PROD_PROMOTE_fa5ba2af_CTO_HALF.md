# NEVER-WIDEN CO-SIGN -- CTO HALF. Portal PROD promote `bf780f94 -> fa5ba2af` (DSGN rounds 58-60 ONLY), and the round-60 DEV review

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~08:2xZ, on `2.0.0_SA_COO~D1` msg 2105. **Ruling:** `ledger/ROUND_ANALYSIS.round59.md` ADDENDUM 1
@f01d69edd3 (DSGN only; dell2's 11 commits excluded on dell2's answer XB-d88b @66207bce7d).

## Measured at signing (portal, fetched ~08:2xZ)

- `git log bf780f94..fa5ba2af`: 9 commits, each with ONE parent, in a linear line. The one "merge" is only a word in `6e278b7b`'s subject.
- `git diff --name-only bf780f94 fa5ba2af`: **0** files outside `src/pages/SecurityAnalysis/`.
- `git diff fa5ba2af e6fb269c -- src/pages/SecurityAnalysis/`: **empty**. PROD's page is byte-equal to the DEV candidate's.
- **Round 60's four polarity-changed checks (row W130-S1), read:**
  - `posture.harness` `noObjectHeader` and `refusedOk` now assert the header carries no posture line, AND that the Posture tab carries the
    served reason (`data-posture-reason`), plus "No call on this name yet" for the refused arm. The fact is still asserted where it now
    lives. Sound.
  - `tabs.harness` `generation_captions_present`, security-mode arm: it asserts 0 captions in the identity header, because round 59
    removed the readings sentence (SAW-14, Andrew's "plumbing out of the face"). The list arms are unchanged. Sound, but the check's NAME
    now reads opposite to its security arm. Round 61 renames that arm, with no behaviour change.

## VERDICT

- **DEV candidate `e6fb269c` (DEV `d06ae384` + round 60): APPROVED.** The box manager lands the fast-forward, re-cut on DEV's head if
  DEV has moved.
- **PROD promote to `fa5ba2af`: SIGNED, on one condition:** the signed-in walk of `fa5ba2af` against the live backends (port 5174, when
  it frees) reads every tab for AMD, and the round-59 register items read as on DEV. A failed walk is a STOP.
  - Blast radius: portal PROD's ref and its build, nothing else.
  - Rollback: PROD back to `bf780f94`.
  - No word from Andrew is owed: `/security-analysis` is requireInternal (law d92d08c448).
  - The COO half is `2.0.0_SA_COO~D1`'s. `0.0.0_AB_MSTR~DELL1` runs `/prod-deploy`, bound to `fa5ba2af`.

**SIGNED** (the walk condition) -- `1.0.0_SA_CTO~DELL1`.
