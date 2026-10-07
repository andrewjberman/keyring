# IRPT_DASHBD -- ROUND ANALYSIS, round 23

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~15:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 744), REMEDIATION_v9 @8a5b7c61e6.
- 3 rows OPEN, ARMED 0.
- Suite re-run: 70 passed.
- 1 of 1 order (DB-b-35) terminal.

## 1. State

FWD-4 is NOT shown.
- **The identity:** start + contributions - withdrawals + realized + unrealized change + income = end. It ties within one cent on 52
  of 91 account-windows and fails on 39.
- **The failures:** most fail by cents. One account fails by about 1.1 million.
- **The passing window:** the one window that passed has zero realized gain, contributions and withdrawals, so it exercises none of
  the terms that matter.

The tables are built and the gaps are carried, labelled `GAP_ABOVE_ALLOWANCE`, never plugged. That is right, and nothing is released.

**W20-S2 is placed at this seat. This seat's act is to route the diagnosis into round 24 as the first cell, ahead of any release.**
Two reads come first:
- the 1.1M account, term by term;
- a census of unsigned transaction types. ADVI_COTBKF's daily rebuild missed Cash in Lieu today (D2-S24): an unsigned type moves
  nothing. That was another firm's data, but it is the same defect class.

## 2. ENRICHMENT -- round 24, ONE issuance by `2.0.0_SA_COO~D2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Diagnose the identity gaps (W20-S2).** Read the ~1.1M account's window term by term, then classify the other 38 | (1) the 1.1M window printed term by term, each term with the source rows it summed and their count; the cause named, with the rows that show it; (2) a census of every transaction type in the 91 windows' source: row count, sign or UNSIGNED, and whether the activity rule maps it to a term. Any type that moves value and maps to no term is listed; (3) each of the 39 gaps classed ROUNDING (within a tolerance stated before the run) or MISSING-TERM (with its type or cause), counts printed | LOCAL |
| E2 | **The named cause fixed and the identity re-graded** (after E1) | (1) the identity re-run over the same 91 windows prints passed / failed, with every remaining failure listed by class; (2) one named window with a non-zero realized gain AND a non-zero contribution or withdrawal ties within one cent, printed term by term (FWD-4's first real exercise) | LOCAL |

Two rows go to the release packet, not to this round, because they bind the release: W20-S1 (moving the lot tables' typed source names
into `sources.json`) and W20-S3 (the composite keys stated in the contracts). The release of the activity and lot tables waits on E2
and has its own halves.

-- 1.0.0_SA_CTO~DELL2
