# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 37 (EXECUTING), 2026-10-16 02:20Z to 04:05Z (site Z)

Resumed from the wind-down log (`session_log_20261016T01Z_wind_down_opal_bloomberg.md`) on Andrew's word ("time to get back on the mission", 02:0xZ; loops 60m then 30m at ~02:45Z, msg 34668). Finish-by Fri 2026-10-16 ~22:00Z (PRD v3.12). All commits LOCAL on `box/sitez` unless box-sync has pushed them.

## Measured and done

| act | result |
|---|---|
| Gateway suite, trunk `474b9770d5` vs the hookup worktree | 982 passed / 61 failed on both, identical failing ids (0 new) |
| Hookup merged | `5aeafbda15` |
| `OG-ap-24` Phase B GO (three halves signed at .tf `21a54e8f197eeea2`) | six vendor read roles LIVE, order complete `dcc3ac9174`; AC2 script fixed `d55475e545` (row Z-S158; filer `~ZS` filed Z-S159) |
| `OG-cl-7` merged | `517f78548d`: AC1 PASS (50 tests), firm literals 0, AC2 FAIL on 8 non-firm bd49f strings |
| `OG-sv-1` cut `7c8c1ee4db`, merged `40051277fc` | six tools BUILT (correlations, etf_returns, factor_tilts, model_portfolio_timeseries, peer_performance, trending); `model_portfolios_views` ruled out at 95 trading days |
| `OG-sv-2` cut `0bd61ef886`, merged `a765e13af8` | `portal_get_cma_assumptions` (2026 edition, 27 rows) |
| `OG-cl-8` cut `deb7ff9952`, merged `2ed472c4b9` | four none_owed rows in `name_rulings.json`, `orion/4698` alias gone; AC3 PASS, AC2 FAIL (gate never reads the rows) |
| `OG-cl-9` cut `53a14c2153`, merged `80e59dd45e` | the `etfs` row |
| Hookup of the seven sv tools | `7200f493d2` (registry 114 to 121, non-data 105 to 112; pin and sv tests 27 passed) |
| `OG-ap-23` STAGED `18b05a842d` | `OG-ap-22` superseded; checks ap23.AC1/AC2; GO waits on the gate fix |
| `OG-ng-2` cut `9104dc611a`, worker ~114 | the commit-time naming gate reads `name_rulings.json` (XA-20261016T034740Z-28da ruled (a)) |

## Rulings and answers this stretch

- **Catalog LAYER name is not an S3 prefix:** PRD v3.13 item 2 ("served/* needs IAM") withdrawn @7656f484ab after I measured every prefix is under `json/*`, granted by `queryv0-iam.tf:34` (CTO msg 34690). No never-widen ask.
- **MCPINDEX 34654 / 34695:** 3 rows ratified out (empty table, 183 and 160 days stale); 7 served rows in `OG-ap-23`; `cma_assumptions` in; the DynamoDB etf-classifications table is the NAMED NEXT INCREMENT (grant plus census), owner `2.0.0_SA_COO~O`, outside the 22:00Z line (CTO ruling @d97ea3ae82 section 2). `opal-harvest-security-metrics` goes to dell1 AMGT_HARVST.
- **Gateway queue order:** `OG-ap-23` first, then `MX-r-15` (msg to `~MI`); the live commit goes to `~MI` and `~MP` at the `OG-ap-23` ledger close.
- **Naming gate:** CTO msgs 34699 and 34713: no new class, no R20, no override; rows in `name_rulings.json` plus a fix to `naming-gate.py` so it reads them.
- Calls queued: `sitez-20261016T023921Z-035e` (eight rows, now ruled ADD minus the withdrawn IAM).

## Open

`OG-ng-2` running (worker ~114). When it merges: re-grade the ten lines, run the planted negatives, then the Phase A GO to `0.7.0_AE_CloudOps~Z` naming `trunk_sha`. `OG-cl-7`/`cl-8` AC2 close then (the same check as `OG-ng-2` AC2). Row Z-S158 to disposition (fixed `d55475e545`).

## Traps met (each cost a retry)

- Writing a new check named `ng1.AC1.sh` overwrote an existing OG-ng-1 check: tracked files restored from HEAD, mine renamed `ng2.*`. List the checks dir before naming a new check.
- The COO cannot commit `infra/logic/registry/` (lane PLATFORM_LOGIC_DOCS) or the gateway app files (lane CLOUD_OPS_OR_ETL) without the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the hookup commit; the registry rows go through a worker order that names the path.
- A resumed worker (SendMessage) needs its worktree fast-forwarded to trunk first.

## Compiler Tools

`comp-find --name ... --limit N` for the ap-24 files (a piped census is denied: use `--limit`); `python .tools/open-calls.py add/list`; `python .tools/unblock.py tick` each tick. The rail denied three raw-grep forms; each ran after the printed RUN NEXT form. Gap: no tool reads a catalog row's freshness; I parsed `DATA_CATALOG.yaml` with python.
