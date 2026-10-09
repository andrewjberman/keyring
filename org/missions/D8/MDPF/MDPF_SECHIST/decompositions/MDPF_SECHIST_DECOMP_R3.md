# MDPF_SECHIST decomposition -- ROUND 3, enrichment (issuer 2.0.0_SA_COO~H1, dell1; cut 2026-10-09 ~13:3xZ)

**Status: ISSUED** in one issuance. **Cut on:** the CTO's round-2 analysis `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round2.md`
@d0230a0dac (msg 2477) with ADDENDUM 1 @678d85e071 (msg 2480, item 6), PRD v0.2 + ADDENDUM v0.3 (prices are total return). Pre-draft
`org/tier1_exec/2.0.0_SA_COO~H1/MDPF_SECHIST_DECOMP_R3_PREDRAFT.md`. The analysis's section 2 (items 1-5) plus addendum item 6 is the
rectangle. FWD-8 is not in round 3 (it goes with MDPF_SECCLASS FWD-5).

## The rectangle

| item | FWD | cell | order | worker | depends on | risk |
|---|---|---|---|---|---|---|
| 1 | FWD-4 | `SH-t-6` gap record: per tracked security the stored range, the required range, the missing and held-null days, from the vendor's own per-run count (`vendor_observations`), never a trading calendar | `TO-SH-t6` | `0.9.0_WK_MDPF_SECHIST~5` | none | SERVED |
| 1, 4 | FWD-5, FWD-9 | `SH-t-7` gold: a window over a listed gap serves blank; a money-market fund's daily return comes from its total-return level ((P + D) / P_prev, analysis item 4), and a day with neither is blank | `TO-SH-t7` | `~6` | `SH-t-6` (reads the gap record) | SERVED |
| 1, 4 | FWD-5, FWD-9 | `SH-t-8` pull: the next run requests the record's listed days; the history request gains the total-return level field (route 2a). BUILD ONLY; its site-Z take is a separate WORLD act under `1.0.0_SA_CTO~Z`'s half and an MDPF_DEMQUE quote | `TO-SH-t8` | `~7` | `SH-t-6` | LOCAL (code) |
| 2 | FWD-3 | `SH-t-9` entry + depth: per security, each source (Opal ETF, client account by firm, rival fund) and its required depth, the deepest governing (C-DEPTH) | `TO-SH-t9` | `~8` | none | SERVED |
| 2 | FWD-2 (join) | `SH-t-10` Cottonwood id join, READ ONLY: the 4,545 price-need ids against table keys, with the unmapped listed | `TO-SH-t10` | `~9` | none | LOCAL |
| 3 | FWD-6 | `SH-t-11` `NAME::` census, READ ONLY: which writer mints `NAME::` keys, rows per writer, whether any hop carries one to the pull label or the join | `TO-SH-t11` | `~10` | none | LOCAL |
| 5 | FWD-7 | `SH-t-12` the 2026-10-12 scheduled run prints the draw beside the ledger remainder (ledger `mdpf-sechist-sh-t4-sitez-run-record-20261009` L3) | `TO-SH-t12` | `~11` | EVENT: the 2026-10-12 07:00 ET scheduled pull | SERVED |
| 6 | FWD-2 | `SH-t-13` SECHIST series writer: per security per day the as-traded price, the dividend/interest cash and the total-return value (ADDENDUM v0.3), keyed by Commonwealth CUSIP as `price_store` is; writes nothing without an explicit switch (KEEP, then PORT: never two writers) | `TO-SH-t13` | `~12` | none | LOCAL (code) |

## Rule 24

Domain: analysis items 1-5 plus addendum item 6 (six items). Subtraction: 1 -> a, b (blank), f (fill); 2 -> c, d; 3 -> e (census; the
build waits on the CTO's key ruling); 4 -> b (MMF rule), f (field); 5 -> g; 6 -> w. Remainder: none. Same grain: each cell is one
surface (a silver record, the gold returns, the pull, a silver record, an evidence file, an evidence file, a served manifest read, a
writer). State coherence: no cell moves the served page's existing windows for a security with no gap; `w` moves no live writer.

Cell letters used below: a = SH-t-6, b = SH-t-7, f = SH-t-8, c = SH-t-9, d = SH-t-10, e = SH-t-11, g = SH-t-12, w = SH-t-13.

## Write sets (disjoint)

- a: `data/etfs/scripts/silver/etf_history_gap_record.py`, `data/etfs/scripts/silver/test_etf_history_gap_record.py`.
- b: `data/etfs/scripts/gold/etf_positioning_gold.py`, `data/etfs/scripts/gold/test_etf_positioning_blank_over_gap.py`,
  `data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py`.
- f: `integrations/bloomberg/pipeline/etf_daily_pull.py`, `integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py`
  (Andrew lifted no-modify for this file, record `ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_CALLS_ANSWERED.md`; the rest of
  `integrations/bloomberg/pipeline/` stays under the order).
- c: `data/mdpf/scripts/silver/security_entry_depth.py`, `data/mdpf/scripts/silver/test_security_entry_depth.py`.
- d, e, g: their evidence files under `deliverables/0.9.0_WK_MDPF_SECHIST~<n>/` only.
- w: `data/mdpf/scripts/silver/security_series_writer.py`, `data/mdpf/scripts/silver/test_security_series_writer.py`.

Addresses (builder output, read 2026-10-09): gap record `address("bloomberg","etfs","silver","history_gaps","as_of=<d>","gap_record.json")`
-> `s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=<d>/gap_record.json`; entry record
`address("mdpf","global","silver","security_entry","as_of=<d>","entry_depth.json")` -> `s3://opal-data-assets/mdpf/global/silver/security_entry/as_of=<d>/entry_depth.json`.

## Edges and fan-out

a -> b and a -> f are data edges (the gap record). g is event-gated on 2026-10-12. c, d, e, w are independent.
`fanout: 8 of 8 cells cut; 5 chains ({a,b,f}, c, d, e, w) plus g event-gated; spawned now: a, c, d, e, w; cap 8`.

## Battery (every criterion dry-run at the base 2026-10-09 ~13:3xZ, each FAILS as expected)

Checks in `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`: `GAP-TESTS-BAD missing-file`, `BLANK-TESTS-BAD
missing-file`, `MMF-TESTS-BAD missing-file`, `PULL-TESTS-BAD not-passed=test_next_run_requests_listed_gap_days,
test_history_request_carries_total_return_level`, `ENTRY-TESTS-BAD missing-file`, `COTJOIN-EVIDENCE-BAD missing-file`,
`NAMECENSUS-EVIDENCE-BAD missing-file`, `FWD7-READ-BAD no-scheduled-manifest-since 2026-10-09`, `WRITER-TESTS-BAD missing-file`.
