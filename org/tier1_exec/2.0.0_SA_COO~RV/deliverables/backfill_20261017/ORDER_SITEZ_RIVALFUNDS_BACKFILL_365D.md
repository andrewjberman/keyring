# ORDER (Andrew-direct): rivalfunds 365-day close backfill on the site-Z Terminal, now, under his 2M-cell override

**From:** `2.0.0_SA_COO~RV` (ETFS_RIVALS issuer, dell1). **To:** `0.0.3_BG_BBGTerminal` (site Z, the seat at the Terminal).
**Authority:** `org/tier1_exec/2.0.0_SA_COO~RV/deliverables/ANDREW_DIRECT_20261017_031xZ_RIVALFUNDS_BACKFILL_365D_NOW.md`
-- Andrew, verbatim: "backfill all securities in there back 365 days right now" and "override like 2m cells right now".
Budget envelope: Andrew-direct 2026-10-16 ~15:5xZ (surface C 400,000 a day; you may download), now overridden to ~2,000,000.

## The work (measured on live S3 by the issuer, 2026-10-17 03:1xZ)

- 746 Bloomberg securities: `org/tier1_exec/2.0.0_SA_COO~RV/deliverables/backfill_20261017/securities_owed_20261016.txt`
- 180,991 owed (security, trading day) closes, 250 trading days, 2025-10-20 .. 2026-10-16 (`history_owed.owed`, page day 2026-10-19).
- Field PX_LAST only. Rows land as backfill-marked G4 objects; the deployed readers (rounds 20, 26, 27) use them for the price
  curves only and never move the served rankings.

## The act (on the Terminal machine, site-Z working tree at or after this commit)

1. `data/etfs/scripts/rivalfunds/bbg_budget.json`: set `daily_ceiling_rows` to `2030000` (reserve 30,000 stays, so the backfill
   allowance is 2,000,000 -- Andrew's override). This guard has no env override; the file is the only lever.
2. Dry run (requests nothing; prints the plan and points):
   `python -m data.etfs.scripts.rivalfunds.enrichment_bloomberg --mode market-range --start 2025-10-17 --end 2026-10-16 --max-points 200000 --securities org/tier1_exec/2.0.0_SA_COO~RV/deliverables/backfill_20261017/securities_owed_20261016.txt --sink s3 --batch-id rv-bf365-20261017`
   MEASURED by the issuer on dell1 at 03:2xZ (same command, dell1's empty ledger): `REFUSED ... plan 178294 points (746 securities
   x 239 un-held trading days of 251 in 2025-10-17..2026-10-16) + 177 currency lookups > 120000 points left ... (ceiling 150000 -
   reserve 30000; spent 0 on 2026-10-17)`. The 120,000 guard is the ONLY refusal; step 1 lifts it. 12 dates (2026-09-29 ..
   2026-10-15) already hold a daily market object and are skipped; their ~2.7k owed units stay with the daily history-owed leg.
3. The same command with `--live`. It never overwrites a date already holding a market object; nothing lands unless every batch answered.
4. Reply with: the dry-run and live result lines (points planned, requested, landed, carried, failed, currency lookups), the
   bbg_budget ledger total for the day, and any vendor warning. The issuer re-reads `history_owed` on S3 after and closes it.

## If it refuses

Do not narrow the set. A refusal line, a vendor limit warning, or a DAPI-down session goes back as the reply verbatim; the
issuer routes it. Do not split into days on your own judgement -- Andrew asked for now.
