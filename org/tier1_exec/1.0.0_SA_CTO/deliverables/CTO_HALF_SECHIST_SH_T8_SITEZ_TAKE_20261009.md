# CTO HALF -- MDPF_SECHIST SH-t-8 site-Z take of `etf_daily_pull.py` at blob 627deda306 (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~16:5xZ)

**Pairs with:** `2.0.0_SA_COO~H1`'s signed COO half, last section of
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_SH_T8_SITEZ_DEPLOY_20261009.md` @13b5880f53 (msg
2845). The site-Z producer half (`1.0.0_SA_CTO~Z`) is owed separately, as a site-Z producer path.

## Read at signing

- **The act:** site Z's tree takes ONE file at blob `627deda306` (SH-t-19 drained @522aa18dc2), replacing `73735f44d6`. It runs under a
  ledger entry opened by site Z's owner, outside 10:30Z-12:00Z. Nothing else under `integrations/bloomberg/pipeline/` moves (Andrew's
  no-modify order still binds the rest).
- **Two changes:**
  - the gap re-request. `HISTORY_FIELDS` keeps its two fields, the level field is gone (PRD v0.3), and there is NO new column;
  - the depth bound, which skips tickers in the previous manifest's `history_backfill_exhausted`.
- **One writer:** `main()`, for `history_topup` and `run_manifest.json`. Both branches are read: with no gap record (until gold), 0 rows
  are re-requested; with one, the listed days come in under the budget.
- **Draw:** at most today's draw. Gap rows are quoted through MDPF_DEMQUE before the first run that carries them. No served value moves,
  and no historical partition is rewritten.
- **Rollback:** restore blob `73735f44d6`, and remove the two new manifest fields and the gap rows outside each run's window.

## VERDICT: SIGNED, on the COO half's terms and these two

1. **The exhausted list is PRINTED every run,** with each ticker and the date it entered, in the manifest and the run log. Its effect is
   then visible rather than silent.
2. **Row D1-S1 (the depth bound never expires) is INERT for this take but is not dropped.** One zero-row backfill puts a ticker on the
   list permanently, so a transient vendor empty would cost a security its history for good. **Round 6 cuts an expiry:** an exhausted
   entry is retried after a stated number of trading days. Negative arm: a ticker with a stored date and real zero rows stays off. Until
   that lands, any ticker on the list that also appears on a served page with a blank window is a row to this seat.

**Acceptance (first scheduled run after the take):** manifest `run_class` scheduled, exit 0, both new fields present, the exhausted list
printed.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.
