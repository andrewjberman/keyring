# IRPT_BCKEND PRD v0.36 -- ratified-text review (ADDENDUM v0.36, two claim values renamed)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @dd8ba1ff0b.
**Asked by:** `1.0.0_SA_CTO~DELL2` msg 5022. **Prior review:** `IRPT_BCKEND_PRD_v0.35_RATIFIED_TEXT_REVIEW_20261011.md` @a78b3232a3 (SIGNED).
**Verdict: SIGNED.**

## What changed

Two values of `date_basis_claim` are renamed: `OWN_DATE` to `ACCT_OWN_DATE`, `PRIOR_DATE` to `ACCT_PRIOR_DATE`. The addendum says
nothing else of v0.35 moves, and its text changes nothing else: the order of decision, the five kinds, the serving rule and the
re-count stand, read with the new names.

## What this seat checked

- **The reason is true.** `holdings_performance.py:145-148` prints the source-grain set as the addendum cites it: `OWN_DATE`,
  `PRIOR_TRADING_DAY`, `NO_SINGLE_CLOSE`. The account-day claim no longer shares a value with it.
- **The census reproduces.** Word-boundary, tracked files, this seat's own run over `infra/aws/lambda/investor-reporting`,
  `data/assets/scripts` (wider than the addendum's `gold/`) and portal DEV `src`: 0 files for each of the eleven tokens and for
  `PER_ACCOUNT_DAY`.
- **This answers the one point of the v0.35 review**, and more durably than the field-name note that review asked for.

## The gate

`prd-signoff.py status` read this half SIGNED and current at v0.36 before this review, on the v0.35 signature. Same gap as row
IRPT_BCKEND-D2-S83; the delivery came by message.

## What this seat read

The addendum's 18 lines (`git show dd8ba1ff0b`); the four cited lines; the census above. Nothing is built under either name.
