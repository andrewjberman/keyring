# /canonical-drive MDPF_SECHIST -- 2.0.0_SA_COO~H1, 2026-10-09 13Z-14Z (dell1)

## Round 2 closed
- 13:04Z Positioning published 13:01:37Z; worker ~4 TO-SH-t3 `FWD1-ACCEPT-OK as_of=2026-10-08 ticker=HTHIY passed=2/2` @7a2fc939e7;
  drained @591186b1de; issuer re-run rc 0; round-close-check MAY-CLOSE; L8 packet @441e4b4fc1 (READ by CVO 13:13:39Z).
- CTO round-2 analysis @d0230a0dac: FWD-1 REALIZED. Section 3 was stale on card A (msg 2478); ADDENDUM 1 @678d85e071 adds FWD-2 as item 6.

## Round 3 issued @99f3bdb84d (8 cells, SH-t-6..13)
First cut refused by to-pipeline-gate (25 violations: cell ids off the decomposition grammar; comp-adversary line with no
coverage/BLIND statement) -- fixed in the same issuance (ids SH-t-N, preflight coverage line).

| cell | worker | state |
|---|---|---|
| SH-t-6 gap record | ~5 | merged @f81aac3c45, GAP-TESTS-OK 3/3 (issuer re-run) |
| SH-t-7 gold blank-over-gap + MMF | ~6 | running (spawned after t6) |
| SH-t-8 pull fill + TR field | ~7 | running (spawned after t6) |
| SH-t-9 entry + depth | ~8 | merged @4cd83dd5a2, ENTRY-TESTS-OK 3/3 |
| SH-t-10 Cottonwood id join | ~9 | merged @48d25bda67, matched=234/4545 unmapped=4311 |
| SH-t-11 NAME:: census | ~10 | running |
| SH-t-12 FWD-7 read | ~11 | event: 2026-10-12 scheduled pull |
| SH-t-13 series writer | ~12 | merged @800ca86f5b, WRITER-TESTS-OK 3/3 |

## Rulings / issuer notes
- Check defect: `r3_named_tests.py` read a passing suite BAD under an exported FORCE_COLOR (rows D1-W5-S1 ARMED, D1-W8-S1,
  D1-W12-S1). Fixed @de7dd9ee67 (--color=no, env drop, ANSI strip); verified OK in a FORCE_COLOR=3 shell. No criterion text changed.
- Gap-record reading rule given to t7/t8: `absent_days` are candidates (`absent_days_exact`); blank any window holding a counted
  absent day even when undated; re-request candidate days (an over-request costs rows, never a wrong number).
- For the round-3 analysis: (a) the writer's total_return is a gross ratio, price_store's is ratio - 1 -- reconcile before the
  PORT window; (b) SH-t-9's record is global scope, so firms' first-appearance dates share one file under their own source keys --
  per-firm or global is a C-DEPTH / firm-boundary question for the CTO; (c) new dataset `mdpf/global/silver/security_series`
  (builder accepted) -- registry row confirmation.
