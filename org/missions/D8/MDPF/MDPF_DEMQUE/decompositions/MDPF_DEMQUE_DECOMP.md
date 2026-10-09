# MDPF_DEMQUE decomposition -- ROUND 1, the THREAD (issuer 2.0.0_SA_COO~Q1, dell1; cut 2026-10-08 ~23:xxZ)

**Status: ISSUED** in one issuance. Seat: `2.0.0_SA_COO~Q1`, seated by the dell1 operator for MDPF_DEMQUE ("Seated for MDPF_DEMQUE ...
L5 starts once the CVO signs").

**Cut on:** PRD v0.2 @94d21953b7 (L4-R ADMITTED: ratified-text half SIGNED by `3.0.0_SA_CVO` at the current ENDPOINT hash, @52286c2722;
brief half admitted because the CROs wrote the briefs). Briefs: `docs/briefs/bbg-backfill-demand-queue-brief-20261008.md` @91f5c90ec2;
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md` @e112184d3b.

**Input carried, not yet readable here:** `0.0.0_AB_MSTR~DELL1` msgs 1232/1235 relay Andrew ~23:0xZ (record
`ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_CALLS_ANSWERED.md` @86d85ab4a5): site Z's daily Bloomberg price asks for Rival Funds
history are MDPF_DEMQUE tier 3. Measured at the cut: neither the record nor @86d85ab4a5 is on `origin/CLOUD` @0573ceb0c3. Tier 3 is not
round-1 scope (round 1 is FWD-1 only); it is read before the round-2 cut.

## The thread (FWD-1) and its hops, measured at the base 2026-10-08 ~23:3xZ

FWD-1: a named security a living Cottonwood client holds, with no history before, shows its daily prices on that client's pages; the
prices agree with the prices the client traded at; no person ran a pull by hand.

| hop | what | today | cell |
|---|---|---|---|
| 1 arrive | a new Cottonwood security is seen | `data/cot/scripts/gold/E_18.detect_new_securities.py` detects securities not in the canonical table (MDPF_SECCLASS SC-e-4). The need list is ADVI_COTBKF's `PRICE_NEED_FOR_SECHIST.csv` @50a35d3ada (3,226 YAHOO-sourced CUSIPs, columns `security_id,asset_class,source,first_date_needed,last_date_needed,days_needed`) | none: relied on (C-PRODUCERS) |
| 2 identify | the CUSIP is locked to one Yahoo symbol, per date range, against the client's own trade prices | NOTHING locks. Candidates exist: Commonwealth silver transactions (`opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23/`, 14 parquet) carry Cusip+Symbol; 3,101 of 3,226 have a Symbol; 481,060 trade observations (dell2 research M1, M2) | `DQ-t-1` |
| 3 pull | the locked symbol's whole daily history, one gentle request, stored as traded | Yahoo callers pace per caller (PRD STARTING STATE); `data/black_diamond/scripts/silver/backfill_yahoo_prices_safe.py` has the checkpoint + stop-on-429 pattern (20 per batch, 5 s) for 49F. No shared pacer; no as-traded derivation. yfinance 1.7.0 installed on dell1 | `DQ-t-2` |
| 4 queue | the request is priced in cells and drawn on a day without a person | NOTHING. `bbg_budget.py` is Bloomberg rows for rival funds only. `lib.opal_naming.address("yahoo",...)` REFUSES ("source 'yahoo' is not a systems.json key", run 2026-10-08 ~23:3xZ) | `DQ-t-3` |
| 5 land | the as-traded series reaches the input Cottonwood's price build reads | `data/cot/scripts/gold/build_canonical_prices_v2.py:281-288` reads `opal-data-cot:silver/historical_prices.parquet` (`ticker,date,close`) as Tier 2 and `:290-298` maps `asset_name -> ticker` from `opal-data-cot:config/ticker_lookup.json`. **Both objects are ABSENT live** (`list-objects-v2`, 2026-10-08 ~23:2xZ; positive control: `silver/prices/` lists 90 objects in the same bucket) | `DQ-t-4` |
| 6 page | the price build runs on schedule and the client's page shows the series | `silver/prices/canonical_prices.parquet` LastModified **2026-06-09T20:42:16Z** while `gold/positions_cube/2026-10-07.parquet` was written 2026-10-08T11:34:14Z. `gold_dispatch.sh:1069-1071` rebuilds canonical prices only on `--chain full`; which chain the schedule fires, whether the build currently fails on the absent Tier-2 objects, and which page shows a client's per-security daily prices are UNREAD | `DQ-t-5` (read) |

## Rule 24

Domain: the FWD-1 thread, hops 1-6. Hop 1 works and is relied on. The remainder is five write sets with one intent each: the lock (t-1),
the pull and pacer (t-2), the queue and its ledger home (t-3), the lander (t-4), and the hop-6 read (t-5). No remainder. Same grain: each
cell is one hop adapter. State coherence: t-1 never pulls; t-2 never decides identity; t-3 never lands; t-4 writes nothing unless the
issuer runs `--apply` at the drain; t-5 writes only its document. No cell moves the Bloomberg budget (`bbg_budget.py`), a producer's code
(C-PRODUCERS) or any page.

## Shared shapes (fixed here so the chains build in parallel)

- **Pull result** (t-2 writes, t-1/t-3/t-4 read): `yahoo_pull.pull(symbol, fetch=None) -> PullResult` with `symbol`, `status` in
  {`OK`, `FAILED_EMPTY`, `FAILED_REFUSED`, `STOPPED_PUSHBACK`}, `http_status` (int or None), `prices` (DataFrame `date, close_served,
  as_traded_close`), `splits` (DataFrame `date, ratio`), `dividends` (DataFrame `date, amount`), `cells` (rows x fields drawn; 0 on
  failure). `as_traded_close(d) = close_served(d) x product of split ratios dated after d`.
- **Lock row** (t-1 writes, t-4 reads), dell2 research s.1: `cusip, yahoo_symbol, valid_from, valid_to, method, observations_checked,
  observations_passed, median_abs_error, state` (`LOCKED` / `REJECTED:PRICE_MISMATCH`), `claim` (`measured` / `held`), `locked_at,
  run_id, supersedes`.
- **Request** (t-3): JSON `request_id, tier (1-5, C-PRIORITY), reason, page, securities [{cusip, symbol}], fields ["close"], start, end`.
- **Ledger row** (t-3): `date, vendor, channel, job (request_id), page, cells_quoted, cells_drawn, outcome`.

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `DQ-t-1` | `lock.py`: trade prices `|Amount/Quantity|` from Commonwealth's trade rows; the lock rule (within tolerance on >= min(3, available) trade dates, >= 1 in the earliest third; 0.5% mutual funds, 2% listed); no trade prices -> LOCKED with claim `held`; `--probe N` reads the real transactions | FWD-1 (hop 2) | dell1 code | LOCAL | A, `0.9.0_WK_MDPF_DEMQUE~1` |
| `DQ-t-2` | `yahoo_pull.py`: one security per request, `auto_adjust=False, actions=True`, as-traded close; the shared pacer (8-12 s jitter, daily cap 400, stop the day on 401/403/429, gap doubles next day, checkpoint per request, resume); empty or refused = failure, never prices; `--probe SYMBOL` | FWD-1 (hop 3) | dell1 code; one live Yahoo request (Andrew @489e1cd24c) | LOCAL | B, `0.9.0_WK_MDPF_DEMQUE~2` |
| `DQ-t-3` | `demand_queue.py`: request -> quote (cells = rows x fields per channel; finish date from the daily cap and the queue ahead) -> draw in tier order through t-2 -> one ledger row per request, quote beside actual; plus the `yahoo` VENDOR row in `infra/logic/registry/systems.json` so the builder names the ledger home | FWD-1 (hop 4) | dell1 code + registry row | WORLD (floored by the L6 gate: the registry is an infrastructure path) | B (after t-2), `~2` |
| `DQ-t-4` | `land_cot.py`: LOCKED rows only, inside their range, appended as `ticker,date,close` (as-traded) to `opal-data-cot:silver/historical_prices.parquet` and `asset_name -> ticker` to `config/ticker_lookup.json`; never rewrites an existing ticker; unmatched listed; dry-run by default, `--apply` is the issuer's; `--probe` reads the live transactions | FWD-1 (hop 5) | dell1 code; the apply is the issuer's drain act | LOCAL (the apply: SERVED, at the drain) | C, `0.9.0_WK_MDPF_DEMQUE~3` |
| `DQ-t-5` | READ-ONLY trace of hop 6: Q1 which chain the schedule fires; Q2 whether S_00 runs in it; Q3 whether S_00 succeeds today with the Tier-2 objects absent; Q4 which page shows a Cottonwood client's per-security daily prices; Q5 the artifact chain from canonical prices to that page; `VERDICT: BUILD-NEEDED|NO-BUILD-NEEDED` | FWD-1 (hop 6) | dell1, document only | LOCAL | D, `0.9.0_WK_MDPF_DEMQUE~4` |

## Write sets (disjoint)

- **DQ-t-1:** `data/mdpf/scripts/demque/lock.py`, `data/mdpf/scripts/demque/test_demque_lock.py`, the channel.
- **DQ-t-2 then DQ-t-3:** `data/mdpf/scripts/demque/yahoo_pull.py`, `.../test_demque_yahoo.py`, `.../demand_queue.py`,
  `.../test_demque_queue.py`, `infra/logic/registry/systems.json`, the channel.
- **DQ-t-4:** `data/mdpf/scripts/demque/land_cot.py`, `.../test_demque_land.py`, the channel.
- **DQ-t-5:** `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/FWD1_HOP6_PRICES_TO_PAGE_TRACE.md`, the channel.
- `data/mdpf/scripts/demque/__init__.py` belongs to no cell (hookup at the merge, C10).
- Checks (issuer's, dry-run at the base 2026-10-08 ~23:4xZ, all 9 FAIL as expected; `dq_t3_home.py`'s bloomberg control arm PASSES at the
  base): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/`.

## Edges and fan-out

One edge: `DQ-t-3` draws through `DQ-t-2`'s `pull()` and pacer (chain B, one worker). t-1 and t-4 read the shared shapes above, not another
cell's output, so they build in parallel. `fanout: 4 of 4 chains, cap 8`.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE for the cells -- no cell changes a schedule. The drain's daily draw on dell1 is a schedule act and
  is read with `comp-schedule` at the drain.
- `comp-iam`: DECLARED-NOT-APPLICABLE for the cells -- no Lambda, no role change; the probes are reads by the dell1 agent user. The drain's
  `--apply` puts to `opal-data-cot` (`silver/historical_prices.parquet`, `config/ticker_lookup.json`); the dell1 user's PutObject there is
  UNREAD and is read before the apply.
- `comp-blast load_historical_prices` (2026-10-08 ~23:4xZ): AMBIGUOUS-SUBJECT -- the graph holds the `bd` and `inf` copies only
  (`pipeline:bd:gold:build_canonical_prices_v2:load_historical_prices`, `pipeline:inf:gold:INF_build_canonical_prices:load_historical_prices`);
  **the Cottonwood copy is not in the graph**, so the graph is blind on hop 5-6 and t-5 reads the code directly. Vintage 2026-10-08T12:54Z,
  29,586 nodes.
- `comp-routes` / `comp-cache`: DECLARED-NOT-APPLICABLE at the cut -- the page is unknown until t-5 answers Q4; t-5 uses `comp-routes trace`.
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round.
- C-NAMES: the round mints no resource name. The one new address (the Yahoo ledger home) is builder output after t-3's registry row; the
  two lander keys are EXISTING keys an existing consumer reads (rule 30 non-application: existing pipeline).

## The issuer's acts at the drain (not cells)

1. Merge chains; `__init__.py` hookup; repo hygiene (`py_compile`, ruff py39) once.
2. Pick the FWD-1 security: one P1 (living-client) CUSIP from the need file with trade prices and no row in `canonical_prices`; record it.
3. The one real run: enqueue a tier-2 request for it -> one draw (one Yahoo request) -> lock -> `land_cot.py` dry-run manifest -> read the
   dell1 user's PutObject on the two keys -> `--apply` (SERVED: a never-widen half names the blast radius -- two keys in `opal-data-cot`,
   new objects, rollback = delete the two new objects) -> the price build per t-5's answer -> the page, looked at.
4. FWD-1's "no person ran a pull" needs the draw scheduled on dell1: armed only after the real run, read with `comp-schedule`.
