# MDPF_SECCLASS round 15 -- drain-end packet (2.0.0_SA_COO~M1, dell1, 2026-10-09 ~08:4xZ)

For: 3.0.0_SA_CVO (L8 compile, L9 on judgment criteria) and 1.0.0_SA_CTO~DELL1 (round-15 analysis). Issuance @f9e0c2ca74.
origin CLOUD = 393790d6ad (ls-remote read at packet time). `round-close-check.py --project MDPF_SECCLASS --round 15`:
**verdict=MAY-CLOSE**. 3 orders, 3 complete, proofs 3/3 structural OK, judgment 0, ungraded 0, reviewer present on dell1.

## Orders (3 of 3 dispositioned)

| order | risk | disposition | carrier |
|---|---|---|---|
| TO-SC-e76 BD NAME:: lookup | WORLD | complete, merged; act LANDED (push deploy 19:41:58Z 10-08); ledger CLOSED | drain 1e603ee75c; halves ff248f0bc7 / bc3afa80b8; close 8b1706a3c4 |
| TO-SC-e77 D1-S11 rows + liquid-alt REMAP | WORLD | complete, merged; act LANDED (103 new, 34 remap); ledger CLOSED | drain 9df203a45d; halves 105ea27edc / d223a117ef; close 8b1706a3c4 |
| TO-SC-e78 prompt states Andrew's alternatives rule | WORLD | complete, merged; e49's AI leg resumed on it and closed (956 = 771 landed + 178 refused-final + 1 transport + 6 taken by e77) | drain dd6fa463d5; e49 ledger CLOSED 6c3675723a |

## The real run of each outcome at close (2026-10-09 04:00Z BD fire; log gold_incremental_2026-10-09_20261009_061917.log, COMPLETE exit 0, 29/29 rc=0)

- **e76:** the served `platinum/firm/mix_summary.json` (VersionId lp8kKqX7, D_04 05:49:12Z, data_as_of 10-07) reads unclassified
  **6.94 -> 0.05 pct**, against the candidate 0.38 and the limit 5.0. The PROD-tree walk (tmp/ui-walk/20261009T073722Z) shows the 49F firm
  Mix tiles equal to that file (structured $88.2M, alternatives $5.21M).
- **e77:** the REMAP funds hold **$209,064.46** across 8 distinct holdings over the 10-07 partition (116,919 positions), all served as
  alternatives: from structured $63,279.75, from equity $60,374.45, from fixed_income $85,410.26. Record
  `E77_REMAP_HELD_DOLLARS_20261007.json`.
- **e78:** carried by e49's close (CloudOps ~SD, 10-08 21:5xZ).

## Acts closed in the same window (outside the round's cells; issuer acts and releases)

e65b (`_shared` two keys, ~SC1); e67 (COT C_06, shipped 02:14:55Z, G at the 10:30Z COT run); e71 (one re-seed, ~SC1; `E71-RESEED ok=True`);
e75 (BD C_06 retained reclass, CLOSED with one-relationship widening KEEP, CTO ADDENDUM 1 + XA-2797); e60 (BD D_04 Unclassified line,
shipped 07:07:36Z, G at the next BD run); thread-r3 (CLOSED, B4 on ruling I + XA-96fb); e63 RETIRED SUPERSEDED.

## Rows filed in the window

D1-S17 (~SC1), D1-S18 (seed --dry-run prints "Items written"), D1-S19 (a BD gold test pins the retired ship-everything rule),
D1-S20 (~SC1, proof-schema kind), D1-S21 (e75 single-class census miss), D1-S22 (~SC1).

## Still open after the round (for the round-15 analysis)

1. **e67 G, remap-b COT half, cot-repoint S, cot-cusip-rows R:** all read the 2026-10-09 10:30Z COT run (log ~11:3xZ).
2. **e60 G:** the next BD run's D_04 (`R13_CHECKS/e60_mix_verify.py`).
3. **bd-securities-cot-new-p1:** 925/941 placed; 16 absent = 5 e49 FINAL refusals + 11 never in FWD-15's plan (named in its hold). The
   11 need a ruling: not held (CLOSED_UNREMEDIATED NOT_A_DEFECT), or a placement cell.
4. **e57e61 FWD-10 apply (~S):** held on the first scheduled new-security run that plans US stocks.
5. Forward rule from the e75 ruling: later pairs over C_06's retained reclass census every class outside the six.

FWD-1: **live for Investor Reporting and for the Black Diamond firm Mix page** (thread-r3 closed). Cottonwood reads after e67 G.
