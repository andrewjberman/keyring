# CTO ROUND ANALYSIS -- MDPF_DEMQUE round 2 (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~03:1xZ)

**Inputs:** `2.0.0_SA_COO~Q1` drain-end msg 1518; `deliverables/2.0.0_SA_COO~Q1/FWD1_REAL_RUN_R2.md`; round 2 CLOSED @590c35ee97; the
decomposition's ROUND 3 candidates table @8907a701e6; dell2 `2.0.0_SA_COO~C2`'s AMLP consumer read @14d4fc7049 (msg 1372). Round 3 is
already issued @06cb4fc38c with ONE cell (DQ-t-9, the C-METER Bloomberg quote), on this seat's ruling in msg 1508.

## FWD state

| FWD | state | evidence |
|---|---|---|
| FWD-1 | NOT REALIZED. Hops 1-6 EXERCISED; hop 7 open | Queue store live (AMLP). No hand pull EXERCISED 02:30Z. dell2 valued 1,058 days, 0 unpriced, 3 of 4 trades within 2% (L9 judgment owed). Hop 7, the served page of client 0QF880237, carries forward. |
| FWD-3 | NOT REALIZED | `bql.reserve` is absent, so no Bloomberg allowance or finish date can be computed (candidate 1) |
| FWD-4 | IN BUILD | the round-3 quote cell (DQ-t-9) |
| FWD-5 | NOT BUILT | 5 no-data CUSIPs already seen (candidate 4) |
| FWD-9 | PARTIAL | tiers set by Andrew; the within-tier ranking is not built (candidate 3) |

## Rulings on the five candidates

1. **The reserve. CUT, round 4, cell 1.** Measure the BQL draw of tier-1 production (the 07:00 ET etf_daily_pull and ETF Positioning)
   from the ledger over the trading days available, and write `bql.reserve` = that draw plus a stated margin (C-RESERVE v0.2). Without
   it, the quote cell cannot give a finish date. It would have belonged in round 3, but round 3 is issued and frozen.
2. **The lock-rule agreement floor (row D1-S1, PONPX locked at 51 of 83). RULED: a match locks only when at least 90 pct of the client's
   trade dates agree within 2 pct.** Below that floor the security goes to the unresolved list with reason "low trade agreement" and its
   open dates. 51 of 83 (61 pct) does not lock. Re-test the AMLP lock under the floor (3 of 4 = 75 pct would not lock either). The L9
   judgment on whether the crash-day miss counts is the CVO's. If the floor holds AMLP back, that is a finding for my next analysis, not a
   reason to lower the floor.
3. **The within-tier ranking. CUT, round 4,** per dell2 research s.6 (living client first; dollars held; days missing) and Andrew's
   example (a former client's unmatchable fund is not pursued).
4. **The unresolved list. CUT, round 4:** the FWD-5 list with reason and open date ranges, seeded with the 5 no-data CUSIPs and fed by
   item 2's floor.
5. **The per-security lock range.** Already fixed in the hookup @7cbb1f8c7f; no cell.

## ENRICHMENT LIST, round 4 (ONE issuance by `2.0.0_SA_COO~Q1`, after round 3 closes)

1. The reserve measured and written (item 1).
2. The lock agreement floor of 90 pct, with AMLP and PONPX re-tested (item 2).
3. The within-tier ranking (item 3).
4. The unresolved list (item 4).
5. FWD-1 hop 7: dell2's served page for client 0QF880237 showing the backfilled values, read once ADVI_COTBKF serves it (a cross-box
   read, not a dell1 build).
