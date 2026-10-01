# MDPF_SECCLASS -- one canonical security classification -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Contract `org/standards/MDPF_SECCLASS_CONTRACT.json`. Reviewer `3.0.0_SA_CVO` (not
seated; its seating is asked of `0.0.0_AB_MSTR` by the CTO). As of 2026-10-01T05:5xZ.

Mode: FAST. Lease `MDPF_SECCLASS`, `org/mcp/drive-mode.log` line 36, until 2026-10-01T13:39Z, on 1.0.0_SA_CTO
DECISION 103498 (a) under Andrew-direct 2026-10-01 ~04:2xZ (record @c48af273cc). No round-6 analysis is written; the
round-7 list is built directly. FULL -> FAST boundary: no worker was running; nothing was cut; one order stays
`parked` (TO-SC-e12); round 6's drain-end packet is
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/2.0.0_SA_COO~M/DRAIN_END_R6_20260930.md` @2744a9fc57.

Claim words: `measured` = read this session; `held` = cited from a record, not re-read.

## Pins

| What | Value | Claim |
|---|---|---|
| Working branch / worktree | `coo-m-r30` at `../coo_m_r30` (shared with IRPT_BCKEND~M; disjoint files) | measured |
| Live table `etf-classifications` | 2,309 ticker rows + 348 `CUSIP:` rows | held (session log @9f8fd81494) |
| BD thread code live on `s3://opal-data-bd/code/` | the rolled-back, pre-window versions; C_06, D_03, D_04 read STALE against CLOUD (`comp-pipescript deployed --firm bd`, 05:2xZ) | measured |
| BD_THREAD_R3 half | COO + CTO SIGNED @8769ffe8d5; the nine candidate files' md5 at HEAD equal the signed values; the act's inputs are unchanged since the CTO's signing HEAD 53f971d7a6 | measured 05:4xZ |
| Silver document `opal-bd-asset-dim-download` | the bytes to publish: sha256 d3a38c7b...d3f407, 10,840 bytes (`git show HEAD:`) | measured |
| W12-S1 fix | this file's commit: `seed-etf-classifications.py` `merge_item` | measured |

## Live thread

FWD-1 (one security reads one class from the canonical table, to the page): LIVE for Investor Reporting Holdings since
2026-09-30 (narrowed release); NOT LIVE for the Black Diamond pages (the thread code is rolled back). First failing
hop: the BD gold scripts on the runner, which the BD_THREAD_R3 window redeploys.

## Write claims

- `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py::merge_item` (landed with this file).

## Next proof

BD_THREAD_R3: C_06, D_03 and D_04 import and run on the real runner from `code/gold/lib/_shared/`, then the first
scheduled gold fire and the first 22:10Z silver fire accept it, then the page read for relationship `z08327149`.

## Next-list, in order

1. **BD_THREAD_R3 window** (thread-breaking; both halves signed). Opens when no BD gold run is in progress and the
   runner is stopped; it must leave the 22:10Z silver fire more than 30 minutes away and finish before the 23:00Z
   gold fire. One ledger entry, opened first. Order: the ONE `safe-deploy` call, then the document publish.
2. **W12-S2**: `ETFClassifier.classify_holdings` raises KeyError on alternatives / commodities / structured (the
   client and its two copies). AFTER item 1: the client's bytes are part of item 1's signed candidate.
3. **A fresh reader census** printing TOLERATED, then the MODEL_ROWS half. Today:
   `MODEL-READER-CENSUS readers=34 tolerates=23 read_only=8 crashes=3 refuses=0 fails_contract=0` (the three
   crashes are item 2). The census also printed `UNCENSUSED infra/aws/lambda/investor-reporting/reports/generate_installed.py`.
4. **E_18's trigger** (row W10-S2): `gold_dispatch.sh` carries no E_* id, so E_18 never runs on a schedule. A
   production pipeline is scheduled; the change is a deploy and takes both halves.
5. **A canonical row for `CEMIX`**: Cottonwood serves it fixed_income / International on 67 positions
   (2,039,120.10 USD, measured on a real build 2026-10-01) through a bd-securities name alias; it is an
   emerging-markets equity fund. A served class moves, so it takes both halves.
6. The exact contract-version pin (round-6 deviation 1).

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| The BD gold runner stopped | the 04:00Z scheduled run | EC2 state of `i-01003b035d2988dfb` | AWAITED: a watch is armed; running at 05:37Z |
| Andrew's call: may a per-firm value FILL an absent `instrument_kind` on an existing row | Andrew (CTO 103218 routed it) | -- | AWAITED; no item above depends on it |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| "FAST from 2026-10-01T05:39Z; pins graded after the fact" (the boundary's one line to the CVO); round 6's three issuer-amendment deviations are in the drain-end packet | `3.0.0_SA_CVO` | a CVO is seated; it reads this row |
| TO-SC-e12, the shared-infra bd-securities grant narrowing | `0.7.0_AE_CloudOps` | that seat is live (CTO 103327) |
| `.tools/test_safe_deploy.py` fails 7 of 14 before and after round 6 (row W10-S3) | owner of `.tools/safe_deploy_core.py` | its next change |
| `test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged` fails on CLOUD's unmodified script (row W11-S2) | owner of `seed-etf-constituents.py` | its next change |
| The live bytes of the `bd-asset-dim-trigger` Lambda are unread (the half is sound under either reading) | `2.0.0_SA_COO~M` | item 1's ledger reads them |

## Limits

Item 1 is a served move and is not run. The W12-S1 fix is a local script change: no table row is written by it, and
no live row carries the defect (0 model rows in the table, held). No product ID is PASS until the CVO grades a
pinned candidate. No S3 delete runs under the BD_THREAD_R3 half (CTO condition 3).
