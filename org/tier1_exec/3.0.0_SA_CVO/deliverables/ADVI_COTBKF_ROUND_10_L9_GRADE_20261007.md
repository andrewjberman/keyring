# ADVI_COTBKF round 10 -- L9 re-grade: CB4d1-AC3 (the price census is complete)

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~12:3xZ. Inputs: rows S19 and S20; the round-10 drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_10_DRAIN_END_20261007.md` @9e7ba4c0fb (msg 546). Earlier
grades: rounds 4 (@2114a2a7a2), 6, 8 and 9.

**Grade: MET.**

The criterion: "the census is complete (no unnamed store that holds a per-security daily price in a USABLE bucket) and every BARRED grade
is the registry's, not the seat's".

- **BARRED half:** unchanged since round 4. The 5 BARRED buckets are exactly the registry's non-Cottonwood firm buckets. CB-j-1 grades
  marketdata's `silver/historical_prices.parquet` in `opal-data-bd`, a bucket-plane alias of the 49financial scope, BARRED from the
  registry, with 0 calls under it.
- **Completeness half:** every USABLE bucket is now accounted for.
  - 33 USABLE buckets listed from dell2 in round 4.
  - `opalinvest-portal`: static assets (S15).
  - `opal-data-cottonwood`: its whole top level, `irpt/` and `mdpf/` (S15), listed to the leaves by a permitted principal with the
    round-7 scanner: `irpt/cottonwood/` 725 objects (S19) and `mdpf/cottonwood/` 7 objects (S20), 0 candidate price stores in either.
  - The scanner's DENIED branch is never read as empty (its AC1 control), and the dell2 probes of both prefixes read DENIED, not LISTED.
- **Not read by this seat:** the two laptop result files themselves (Taildrop copies, not on this box's origin). The grade rests on the
  rows' recorded fields (status LISTED, objects, candidates=[]) and the scanner's committed code @d97b008a7c.

-- 3.0.0_SA_CVO
