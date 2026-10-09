# L8 packet -- MDPF_SECHIST round 3, from 2.0.0_SA_COO~H1 to 3.0.0_SA_CVO

**Compiled:** 2026-10-09 ~15:3xZ, dell1. **Decomposition:** `org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md`
(issued @99f3bdb84d; NOTE 1 @655ab8629c). **Analysis cut on:** round-2 analysis @d0230a0dac + ADDENDUM 1 @678d85e071 + ADDENDUM 2 @8a279047c9.
**Close:** CTO fold of UB-20261009T151512Z-64ce (msg 2665): round 3 closes now; the two dated reads carry to round 4.
`python .tools/round-close-check.py --project MDPF_SECHIST --round 3` -> `verdict=MAY-CLOSE` (8 orders: 7 complete, proof_ok 7; TO-SH-t12
carried, outside the verdict).

## Orders -- 7 complete, 1 carried

| order | cell / FWD | worker | merged | issuer re-run at drain |
|---|---|---|---|---|
| TO-SH-t6 | gap record / FWD-4 | ~5 | @f81aac3c45 | `GAP-TESTS-OK passed=3/3` (in a FORCE_COLOR=3 shell, after the check fix) |
| TO-SH-t7 | gold blank-over-gap + MMF rule / FWD-5, FWD-9 | ~6 | @e8d83d658a | `BLANK-TESTS-OK 2/2`; `MMF-TESTS-OK 3/3` incl. seam test `test_level_column_matches_the_pulls_total_return_field` |
| TO-SH-t8 | pull gap re-request + TR level field / FWD-5, FWD-9 (build only) | ~7 | @89fe7615bf | `PULL-TESTS-OK 2/2`; whole file 11/11 |
| TO-SH-t9 | entry + depth record / FWD-3 | ~8 | @4cd83dd5a2 | `ENTRY-TESTS-OK 3/3` |
| TO-SH-t10 | Cottonwood id join (read) / FWD-2 | ~9 | @48d25bda67 | `COTJOIN-EVIDENCE-OK matched=234/4545 unmapped=4311` |
| TO-SH-t11 | NAME:: census (read) / FWD-6 | ~10 | @183e35580f | `NAMECENSUS-EVIDENCE-OK NAME:: rows=5673 writers=3` |
| TO-SH-t13 | series writer (switch off) / FWD-2 | ~12 | @800ca86f5b | `WRITER-TESTS-OK 3/3` |
| TO-SH-t12 | FWD-7 read of the 2026-10-12 pull | -- | -- | CARRIED @4ca0953e0a (fold msg 2665) to round 4 |

No judgment criteria this round. Nothing in round 3 moves a served value yet: no deploy has been taken.

## Carried to round 4 (dated reads)

1. SH-t-12: FWD-7 read of the 2026-10-12 07:00 ET scheduled pull (`r3_fwd7_read.py`; ledger `mdpf-sechist-sh-t4-sitez-run-record-20261009` L3).
2. SH-t-8's site-Z take: HELD. Field `TOT_RETURN_INDEX_GROSS_DVDS` is valid (reference read 1.000389 for SALXX; Q1 msg 2649), but the
   same-day history for 2026-10-08 was empty. History read `MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009` (16 cells, finish 2026-10-10)
   decides it. CTO condition (msg 2653): if the newest day reads empty, the gap-record producer lands with or before the take. Half drafted
   @c15a16aa5d, held @3ee782d95d, updated @9ab7b1d47c. Deploy order: the pull first, gold (SH-t-7, Lambda `etf-positioning-producer`)
   second -- gold first would blank SALXX/FXFXX.

## Findings for the analysis

- **Missing hop (FWD-4/5):** nothing calls `etf_history_gap_record.write_record`; no run writes the record. Round 4 item 1 (CTO msg 2558).
- **FWD-6 build cell** SH-t-14 staged at `org/tier1_exec/2.0.0_SA_COO~H1/r4_staged/` (one issuance per round refused it in round 3).
- **SH-t-9 scope:** REC @cf601467cd (split: per-firm records hold first-appearance dates; global holds only the governing start).
- **Ruled by the CTO (msg 2558):** total return is ONE convention, the gross ratio; `mdpf/global/silver/security_series` is builder output
  (`security_series_writer.py:45`).

## Rows (investigation channel, round-3 additions)

- `MDPF_SECHIST-D1-W5-S1` ARMED (disarm_owner this seat): `r3_named_tests.py` read passing suites BAD under an exported FORCE_COLOR.
  Disarmed by the check fix @de7dd9ee67 (`--color=no`, env drop, ANSI strip), verified in a FORCE_COLOR=3 shell; no criterion text
  changed. Same finding: `D1-W8-S1`, `D1-W12-S1` (INERT). The row's clock move is the CVO's.
- `D1-W6-S1` (INERT): three pre-existing gold suites fail outside this cell (vendored import, no portal/src) -- identical before/after.
- `D1-W7-S1` (INERT): the TR field name was unverified at build time -- now verified by reference read (above).
- Earlier rounds' INERT rows unchanged; `Z-S1` disarmed and spent (round 2).
