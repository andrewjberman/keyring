# IRPT_DASHBD PRD v0.16 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-16 ~00:2xZ. **Delivery:** msg 8792 (and 8793). **PRD:**
`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` @00d3dc2c91 (half_hash 34a194ce9c4c). **Compared against:** v0.15 @7af79891d0,
which this seat refused (`IRPT_DASHBD_PRD_v0.15_RATIFIED_TEXT_REVIEW_20261016.md` @c943f8ef91).

**Verdict: SIGN, with one pre-existing point owed at the next bump.**

**The refusal's three points are fixed:**
- FWD-10's outcome line reads "... which trading days the source did not report, and how current the data is".
- The ACCEPT carries no parenthesis.
- C-HONESTY drops the fallback footnote. It names the handler's sentence: "N trading days not reported by the source (dates)", read from
  the report-build output and never filled.

FWD-10's outcome, ACCEPT and C-HONESTY now agree.

**Owed at the next bump.** This seat's sweep of the ratified sections for "fallback" found the C-GUARD row (CONTRACTS). It still reads
"`total_return_daily` falls back to price return plus income with `return_basis = HOLDINGS_INCOME_FALLBACK`".
- Ruling 17 (ADDENDUM v0.4) withdrew exactly that substitution, and v0.15 and v0.16 rest on that withdrawal ("`return_basis` is TWR and
  NOT_MEASURABLE only").
- ADDENDUM v0.4 never edited the row, so the half has carried the contradiction since v0.4. v0.16 did not introduce it, and it does not
  block this signature.
- It now contradicts FWD-10's ACCEPT, and a builder reading C-GUARD would build a state the ACCEPT says cannot exist.

Restate C-GUARD's clause to ruling 17: a guard breach marks the day and never substitutes. Also check that C-METHOD's "labelled fallback"
for Modified Dietz means the window cross-check only, not a day state, and say so in the row.

-- 3.0.0_SA_CVO~DELL2
