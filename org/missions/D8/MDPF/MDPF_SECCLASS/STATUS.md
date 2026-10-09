# MDPF_SECCLASS -- one canonical security classification -- status

Seat `2.0.0_SA_COO~M1` (dell1), successor to `2.0.0_SA_COO~M`. Contract `org/standards/MDPF_SECCLASS_CONTRACT.json`. Lease **FULL**
(`drive-mode.py read`); `/canonical-drive` armed at 10m on Andrew-direct ~03:1xZ (MSTR msg 1542). As of **2026-10-09 ~08:0xZ**.
This file replaces the 2026-10-01 FAST-mode status. History is in git and the drive logs
(`org/tier1_exec/2.0.0_SA_COO~M1/drive_log_20261009T0*Z_*.md`).

Claim words: `measured` = read this session against the served artifact; `held` = cited from a record.

## Live thread (FWD-1)

| Surface | State | Claim |
|---|---|---|
| Investor Reporting Holdings | live since 2026-09-30 | held |
| Black Diamond firm Mix (Advisor Intelligence, PROD bf780f94 tree) | **LIVE.** The 49F firm Mix tiles equal the served `platinum/firm/mix_summary.json` (structured $88.2M, alternatives $5.21M); firm unclassified 6.94 -> **0.05 pct** on the 2026-10-09 04:00Z fire | measured 07:3xZ |
| BD relationship z08327149 | served composition reads VXX structured/Hedge from `etf-classifications`; 0 `bd-securities` class sources in the run | measured |

## Deploy ledgers

| Ledger | State |
|---|---|
| e65b `_shared` cash-token (two keys 40ffa3fa) | CLOSED (0.7.0_AE_CloudOps~SC1) |
| e71 seed names (one re-seed, 15 rows) | CLOSED (~SC1; issuer-verified `E71-RESEED ok=True`) |
| e75 BD C_06 retained reclass | CLOSED. One-relationship widening (z08296368, PDBC) kept: CTO ADDENDUM 1 + XA-2797; row D1-S21 |
| e76 BD NAME:: lookup | CLOSED (unclassified 0.05 pct vs 0.38 / 5.0) |
| e77 S11 rows + liquid-alt remap | CLOSED (REMAP funds $209,064.46 now alternatives) |
| thread-r3 (BD thread, 10-01) | CLOSED, B4 on ruling I + XA-96fb (served bytes + firm walk) |
| e60 BD D_04 Unclassified line | SHIPPED 07:07:36Z (D_04 23d2f2ae); HELD on leg G = the next BD run (`R13_CHECKS/e60_mix_verify.py`) |
| e67 COT C_06 retired class | SHIPPED 02:14:55Z; HELD on leg G = the 2026-10-09 10:30Z COT run |
| remap-b (33 multi_asset rows) | HELD; its COT half reads with e67 G |
| cot-repoint (10-02) | HELD; leg S closes after the 10:30Z COT run (ruling I, XA-96fb) |
| cot-cusip-rows (10-02) | HELD; its leg R reads with cot-repoint S |
| bd-securities-cot-new-p1 (09-26) | HELD; 925/941 placed, 16 absent (5 e49 FINAL, 11 outside FWD-15's plan); waits on a ruling for the 11 |
| e57e61 FWD-10 apply (~S) | HELD on the first scheduled new-security run that plans US stocks |

## Held build lines

e63 RETIRED SUPERSEDED (by e65b; branch kept, since deletion of unmerged commits waits on a human word). e60 released (above).

## Next, in order

1. **~11:3xZ COT log** (poll armed): e67 G, remap-b's COT half, cot-repoint S, then cot-cusip-rows R.
2. **Next BD run:** e60 G (`E60-MIX ok=True`).
3. **Round-15 analysis** (1.0.0_SA_CTO~DELL1): the p1 residue (11 keys); later pairs over C_06's retained reclass census every class
   outside the six (CTO ADDENDUM 1).

Rows filed this session: D1-S18 (seed `--dry-run` prints "Items written"), D1-S19 (a BD gold test pins the retired ship-everything
rule), D1-S21 (e75 single-class census miss).
