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


---

# ROUND 2 -- the ENRICHMENT (issuer 2.0.0_SA_COO~Q1, dell1; cut 2026-10-09 ~01:2xZ)

**Status: ISSUED** in one issuance. Round 1 above is FROZEN (ROUND_CLOSE @9317792251; thread n; real run @246e601ef2).

**Cut on:** PRD v0.3 @fe3d0659ad (L4-R ADMITTED: ratified-text half re-SIGNED by `3.0.0_SA_CVO` @0afa06a7c6 at the current ENDPOINT hash; brief
half admitted, CRO-written). The rectangle is the CTO's round-1 analysis (`1.0.0_SA_CTO~DELL1` msg 1337; record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_MDPF_DEMQUE_20261009T0108Z.md`): FWD-1's consumer is (a), the client's
backfilled holding values built by ADVI_COTBKF from these prices. Four items: (1) hop 5, the CUSIP absent from the lander's
transactions object; (2) the hop-6 seam, a file contract with dell2's ADVI_COTBKF (path, key namespace, one AMLP trace end to end);
(3) S_00 scheduled (dell1 applies it); (4) the enrichment list @5a392db104.

## Measured at the base, 2026-10-09 ~00:4xZ-01:2xZ

- `opal-data-cot` `silver/transactions/`: 118 objects (2026-03-09 .. 2026-10-08), 993,962 rows, 1,515 distinct CUSIPs; AMLP
  `00162Q866` in 0 of 118; 945 of the price-need file's 4,545 CUSIPs appear anywhere. Under consumer (a) hop 5 does not go through
  Cottonwood's Black Diamond transactions at all: it lands in the queue's own price store, keyed by Commonwealth's CUSIP, which ADVI_COTBKF
  reads (item 1 and item 2 are one store).
- Builder output (`lib/opal_naming.address`, run 2026-10-09 ~01:1xZ): store `s3://opal-data-assets/yahoo/global/silver/price_history/cusip=<CUSIP>`,
  index `.../price_history/index`; ledger `s3://opal-data-assets/yahoo/global/bronze/demand_ledger/dt=<date>`.
- `infra/aws/terraform/cot-pipeline/ssm.tf` `opal-cot-gold-run`: `run_gold <id> <script> <flags> [optional]`, 18 steps A_00..D_04; an
  `optional` step logs WARN and the chain continues. `build_canonical_prices_v2.py:283,298` `get_object` with no missing-key branch.
- The queue (`demand_queue.py`) accepts `close` only and its `draw` keeps no prices (ex-date service @5a392db104; real run @246e601ef2).

## Rule 24

Domain: the four items. Items 1 and 2 are one write set and one intent (the store a consumer reads, and the contract describing it):
`DQ-t-6`. Item 4's queue changes share `demand_queue.py` and one intent (the queue serves more than closes and hands what it drew
onward): `DQ-t-7`. Item 3 is Cottonwood's gold chain: `DQ-t-8`. The schedule of the daily draw and the AMLP trace with dell2 are drain
acts. No remainder. State coherence: t-6 never pulls or ranks; t-7 never stores prices; t-8 never touches the queue or the store, and
does not change what any page reads (row D1-W4-S2 stands: nothing reads `canonical_prices` yet).

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `DQ-t-6` | `price_store.py`: per CUSIP, only the LOCKED range, served close and as-traded close kept apart with splits and dividends, the lock row beside them; an index row per CUSIP (symbol, range, claim, rows, as of); an unchanged second write is a no-op; local root or the builder S3 root. Plus `PRICE_STORE_CONTRACT.md`, the hop-6 file contract for ADVI_COTBKF | FWD-1 (hops 5-6), FWD-8 | dell1 code + contract doc; the S3 write is the issuer's drain act | LOCAL | E, `0.9.0_WK_MDPF_DEMQUE~5` |
| `DQ-t-7` | `demand_queue.py`: fields `dividends` and `splits` accepted and counted in cells; `draw(..., on_result=cb)` hands each OK result to a callback (the store hookup); `upload_ledger(path, date, dry_run=True)` to the builder ledger address | FWD-2, FWD-4 | dell1 code | LOCAL | F, `0.9.0_WK_MDPF_DEMQUE~6` |
| `DQ-t-8` | `build_canonical_prices_v2.py` survives absent Tier-2 objects (WARN, Tier 2 empty, writes); `ssm.tf` gains `run_gold S_00 build_canonical_prices_v2.py "$UPLOAD_FLAG" optional` ahead of A_00 | FWD-1 (row D1-W4-S1) | dell1 code + Terraform; the code upload and `safe-apply` are the issuer's drain acts | WORLD | G, `0.9.0_WK_MDPF_DEMQUE~7` |

## Write sets (disjoint)

- **DQ-t-6:** `data/mdpf/scripts/demque/price_store.py`, `.../test_demque_store.py`,
  `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md`, the channel.
- **DQ-t-7:** `data/mdpf/scripts/demque/demand_queue.py`, `.../test_demque_queue.py`, the channel.
- **DQ-t-8:** `data/cot/scripts/gold/build_canonical_prices_v2.py`, `data/cot/scripts/gold/test_s00_missing_tier2.py`,
  `infra/aws/terraform/cot-pipeline/ssm.tf`, the channel.
- The `draw(on_result=...)` -> `price_store.write` hookup belongs to no cell (C10): the issuer adds it at the merge.
- Checks (issuer's, dry-run at the base 2026-10-09 ~01:2xZ, all 5 FAIL as expected; `dq_t7_tests.py`'s five round-1 names PASS at the
  base (regression arm) and `dq_t8_schedule.py`'s 18-step control PASSES): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R2_CHECKS/`.

## Edges and fan-out

No data edge: t-6 and t-7 meet only at the merge hookup; t-8 is another pipeline. `fanout: 3 of 3 chains, cap 8`.

## Battery

- `comp-schedule`: t-8 changes the content of an existing schedule's run (one optional step), not a schedule; read at the drain apply.
- `comp-iam`: DECLARED-NOT-APPLICABLE for the cells (no role change). Drain: the dell1 user's PutObject on `opal-data-assets/yahoo/` and
  `opal-data-cot/code/gold/` is read before each write; dell1 applies its own IAM now (msgs 1242, 1252) and reports after the fact.
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- enrichment of LOCAL code; the WORLD cell's apply is a never-widen act at the drain.
- C-NAMES: every new address is builder output (above). `S_00` mints no resource name.

## The issuer's acts at the drain (not cells)

1. Merge per chain; the `on_result -> price_store.write` hookup; hygiene (`py_compile`, ruff py39, the four test files) once.
2. AMLP end to end: queue request -> draw (one Yahoo request) -> lock -> store write at the builder address (the store's first object)
   -> the contract and the index to dell2 through `0.0.0_AB_MSTR~DELL1` (CTO act 2) -> ADVI_COTBKF's read of AMLP valued on the client's
   backfilled dates, checked against trade prices (FWD-1 ACCEPT v0.3).
3. t-8: DS-lane upload of `build_canonical_prices_v2.py` to `s3://opal-data-cot/code/gold/` (`.tools/safe-deploy.sh`) and `safe-apply` of
   `cot-pipeline` for the SSM document, under a change-management entry; the next 07:30 ET chain's log reads `=== S_00` and no halt.
4. The daily draw on dell1 armed after the AMLP trace (FWD-1 "no person ran a pull").


---

# ROUND 3 -- CANDIDATES, NOT CUT (issuer 2.0.0_SA_COO~Q1; noted 2026-10-09 ~02:0xZ on an empty tick, /next-calls --drive)

Round 2 is EXECUTING (frozen). Round 3 is cut only from the CTO's round-2 analysis; these are the issuer's candidates for it.

| candidate | why | input |
|---|---|---|
| Bloomberg requests on the queue | the queue meters and quotes Yahoo only; site Z files two AMGT_RESAPP research-page requests (tier 4, run at site Z, C-SITES) and Rival Funds history is tier 3 on Bloomberg | msg 1380; Andrew ~23:0xZ record @86d85ab4a5; C-METER (BQL vs reference/history channels) |
| the reserve | FWD-3: the ledger has no Bloomberg channel figures yet, so no CEILING / RESERVE / allowance | C-RESERVE; `bbg_budget.py` rows -> cells conversion (C-CELL) |
| the pilot readout | R2-PILOT-50's lock outcomes by asset type, push-backs, actual vs quoted cells -> tolerance bands confirmed or retuned | FWD1_REAL_RUN_R2.md |
| priority ranking | FWD-9: requests carry a tier, but within-tier score (held days x accounts x largest purchase) and the "gone client" exclusion are not computed | dell2 research s.6; crosswalk (MATCHED 471 of 1,533) |
| unresolved list | FWD-5: REJECTED / no-symbol / partial-range securities are not yet listed with reason and open date ranges | dell2 research s.2, s.5 |

## ROUND 3 -- CUT (issuer 2.0.0_SA_COO~Q1, dell1; 2026-10-09 ~03:2xZ)

**Status: ISSUED** in one issuance. Round 2 is CLOSED (@590c35ee97). Rectangle: `1.0.0_SA_CTO~DELL1` msg 1511 -- "Cut round 3 in ONE
issuance with the C-METER Bloomberg quote cell first (quote in BQL/reference cells, record actuals; site Z draws per C-SITES)". Since
law edit 4d77a9c3ea (msg 1502) every Bloomberg draw files to this queue, and under msg 1466 none but the two RESAPP calls draws unquoted,
so every new Bloomberg request blocks on this cell. The candidates above (reserve measurement, pilot readout incl. row D1-S1, ranking,
unresolved list) are not in this round: they go to the CTO in the round-2 drain-end message.

**Measured at the base:** the two filed requests (`requests/AMGT_RESAPP-493c-ICT-IDENTITY.json`: channel `reference`, 1 security x 4 static
fields, null window; `requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json`: channel `model_block`, the field set
`integrations/bloomberg/research/model_block_pull.py` declares: `HEADER_FIELDS` :103, `HIST_FIELDS` :220, `FORECAST_FIELDS` :330, "calls per
name stay 8" :340). Allowance inputs: BQL CEILING = the measured floor 2,920,000 cells (2026-10-05, PRD C-RESERVE); the RESERVE (tier-1
production's measured draw + margin) is not on the ledger yet (msg 1511 (2): production is ledgered as RESERVE draws, from now); the
reference/history and model-block channels have no measured ceiling.

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `DQ-t-9` | `bbg_quote.py`: a Bloomberg request (`vendor` bloomberg; `channel` bql / reference / history / model_block) quoted in cells per channel before it draws -- reference = securities x fields; history/bql = weekdays x fields x securities; model_block = the producer's declared per-name groups (read by `ast`, never imported) with a per-group breakdown; finish date only when the channel's allowance (CEILING - RESERVE - drawn today, `bbg_allowance.json`, each figure with its claim) is known, else `finish_date: null` + `allowance_gap` naming what is missing; `record_actual()` appends the drawer's MEASURED cells beside the quote to the ledger, labelling a draw with no quote "drawn before C-METER Bloomberg; no quote" | FWD-3, FWD-4 | dell1 code | LOCAL | H, `0.9.0_WK_MDPF_DEMQUE~8` |

Write set: `data/mdpf/scripts/demque/bbg_quote.py`, `.../bbg_allowance.json`, `.../test_demque_bbg.py`, the channel. Checks (dry-run at the
base ~03:2xZ, both FAIL as expected): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R3_CHECKS/`. `fanout: 1 of 1 chains, cap 8`.
Battery: comp-schedule / comp-iam / comp-adversary DECLARED-NOT-APPLICABLE (no schedule, no AWS, no vendor call; LOCAL code).


---

# ROUND 4 -- the ENRICHMENT (issuer 2.0.0_SA_COO~Q1, dell1; cut 2026-10-09 ~03:2xZ)

**Status: ISSUED** in one issuance. Round 3 CLOSED @a9fb093353 (L8 packet READ by `3.0.0_SA_CVO`, no BLOCKING/ARMED row). Rectangle: the
CTO's round-2 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_DEMQUE_ROUND_2_20261009.md` (msg 1519) items 1-4,
confirmed by the CTO's round-3 analysis (msg 1536, `CTO_ROUND_ANALYSIS_MDPF_DEMQUE_ROUND_3_20261009.md`), with three rulings folded in: **item 2 corrected (msg 1522, "bands")** -- a match locks when at least 90 pct of the client's trade dates
agree within THAT security type's band (0.5 pct mutual funds at NAV, 2 pct listed; dell2 research s.1), not "within 2 pct" for all;
**item 1 (msg 1524, "held+ask")** -- `bql.reserve` starts as a HELD estimate from the producers' code plus a stated margin, every Bloomberg
finish date carries "held" until it reads measured; **site Z ruling 32309 (msg 1532)** -- ONE order from this issuer to
`0.7.0_AE_CloudOps~Z` for a site-Z uploader that turns the draws site Z already records into cell rows on the builder ledger home.

**Measured at the base:** `data/etfs/scripts/rivalfunds/bbg_budget.py` `record()` (:73-76) writes `%LOCALAPPDATA%\opal_bbg_budget\bbg_budget_<UTC
day>.jsonl`, lines `{at, mode, rows, batch_id}` (:9, :50); site Z's reconstruction
(`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md` :82-89) gives cells per row by
producer (rivalfunds BQL holdings 16; G4 market refdata = its MARKET_FIELDS count; others not counted). Builder:
`address("bloomberg","global","bronze","demand_ledger","dt=<day>")` -> `s3://opal-data-assets/bloomberg/global/bronze/demand_ledger/dt=<day>`.
The scheduled 07:00 ET daily pull's steps are in `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`.

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `DQ-t-10` | `reserve_estimate.py`: per channel, the cells one run of each tier-1 producer draws (names x fields x rows, read from the producers' code as text, the producer set = the steps of `scheduled_daily_pull.cmd`), plus a stated margin; writes `bbg_allowance.json` `<channel>.reserve` with claim `held` and its basis; the quote's finish date carries "held" when the reserve is held | FWD-3 | dell1 code | LOCAL | I, `0.9.0_WK_MDPF_DEMQUE~9` |
| `DQ-t-11` | `lock.py`: the 90 pct agreement floor on top of each type's band; below it `REJECTED:LOW_TRADE_AGREEMENT` | FWD-5, FWD-1 | dell1 code | LOCAL | J, `0.9.0_WK_MDPF_DEMQUE~10` |
| `DQ-t-12` | `unresolved.py`: the FWD-5 list, one row per (CUSIP, open period) with reason, state, next act, attempts; fed by failed pulls and rejected locks; seeded with the 5 no-data CUSIPs | FWD-5 | dell1 code | LOCAL | K, `0.9.0_WK_MDPF_DEMQUE~11` |
| `DQ-t-13` | `rank.py` + the draw's sort key in `demand_queue.py`: within a tier, P1 living client > P2 match open > P3 gone (crosswalk), then held days x accounts x largest purchase (dell2 research s.6); a gone client's unmatchable fund is not pursued; each item carries its rank and reason | FWD-9 | dell1 code | LOCAL | L, `0.9.0_WK_MDPF_DEMQUE~12` |
| `DQ-t-14` | site-Z uploader: reads the `bbg_budget_<day>.jsonl` files `record()` writes and writes cell rows (rows x the stated per-mode cells-per-row, each with its claim) to the builder ledger home; scheduled at site Z; no producer edited; OPAL_BBGTML named as a gap if it does not call `record()` | FWD-2, FWD-3 | site Z, `0.7.0_AE_CloudOps~Z` (a seat, not a worker) | WORLD | M |

Write sets (disjoint): t-10 `reserve_estimate.py`, `test_demque_reserve.py`, `bbg_allowance.json`; t-11 `lock.py`, `test_demque_lock.py`; t-12
`unresolved.py`, `test_demque_unresolved.py`; t-13 `rank.py`, `test_demque_rank.py`, `demand_queue.py`; t-14 `bbg_ledger_upload.py`,
`test_demque_bbg_ledger_upload.py` (all under `data/mdpf/scripts/demque/`), plus the channel. The `daily_draw.py` hookups (unresolved rows
from the draw, the rank before the draw) belong to no cell: the issuer adds them at the merge. Checks (dry-run at the base ~03:2xZ, all FAIL
as expected; `dq_t11_tests.py`'s five round-1 lock names PASS at the base, the regression arm): `.../MDPF_DEMQUE_Q1/R4_CHECKS/`.
`fanout: 5 of 5 chains, cap 8` (four dell1 workers; one site-Z seat order).
Battery: comp-schedule -- t-14 adds a site-Z scheduled job, read at its apply by the site-Z seat; comp-iam -- t-14's S3 PutObject on the
bloomberg ledger prefix is read at site Z before its first write; comp-adversary DECLARED-NOT-APPLICABLE (LOCAL cells; t-14 is a pair act).

**The issuer's acts at the drain (not cells):** (a) the `daily_draw.py` hookups (unresolved rows, rank order); (b) **item 7, the RESAPP
quoted-vs-drawn pair (msg 1536):** both RESAPP requests are quoted (round-3 real run @62d605f7ed: ICT 4 reference cells, ABNB 989
model-block cells); when site Z reports each draw's measured cells, record it with `bbg_quote.py --record ... ` WITH the quote (label
`quoted`), the first quoted-vs-drawn pair for FWD-4; (c) AMLP and PONPX re-tested under the floor; (d) the one real run of each outcome;
(e) close only with every BLOCKING row dispositioned and the L8 packet READ by the CVO.

**Round-5 candidates noted during round 4 (issuer, not cut):** (1) retire `price_store`'s write path at the SECHIST port (CTO msg 1716,
`CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md` ADDENDUM 1; row D1-S2) -- SECHIST's writer writes the same keys, one
window switches the writer, dell2 re-points, same-window rollback; (2) quote a STANDING request (`bbg_quote.py` raises "request has no
securities" on ETFS_RIVALS-HISTORY-OWED-DAILY; its file carries the run cap as a held quote); (3) the per-request state
active/paused/stopped at a builder address (CTO msg 1640, XA condition 3).


---

# ROUND 5 -- DRAFT, NOT CUT (issuer 2.0.0_SA_COO~Q1; drafted 2026-10-09 ~06:5xZ on an empty tick)

Round 4 is EXECUTING (DQ-t-14 open at site Z). Round 5 is cut from the CTO's round-4 analysis; this is the issuer's draft against
what is already ruled: PRD ADDENDUM v0.4 (standing request + readable state, @02df620d05), ADDENDUM v0.5 (prices are total return,
@6c538a0bfd, Andrew-direct ~05:4xZ record @cb023aa95f), CTO msgs 1716 (keep+port) and 1846 C (comparison first).

| candidate | what | ruled by | depends on |
|---|---|---|---|
| TR comparison (FIRST) | Bloomberg vs Yahoo total return on clear dividend payers: stored ~1y Bloomberg TR (ED, BX, CSCO, BBY, DG; `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`) now, 6 classic payers after the queued draw (`requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json`, 15,720 cells); Yahoo TR built from the as-traded close + dividends on ex-dates; per-event report (splits, dividends, interest, special distributions) | 1846 C; Andrew ~05:4xZ | none for the 1y names; the site-Z draw for the 6 |
| TR columns | `yahoo_pull.py` / `price_store.py`: per ticker per day the as-traded price, the dividend/interest cash on its ex-date, and the total-return value, by the method the comparison fixes | ADDENDUM v0.5 | the comparison |
| standing request + state | `bbg_quote.py` prices a STANDING request (its run cap) and the queue writes `request_state` (active/paused/stopped) at the builder address the addendum names | ADDENDUM v0.4; msg 1752 | none |
| one intake | the Yahoo draw reads `requests/` like Bloomberg (today a box-local dir on dell1) | issuer (gap list) | none |
| price_store retirement | retire the write path at the SECHIST port, same keys, same-window switch | msg 1716 | SECHIST's writer cell |
| reserve enforcement | a Bloomberg backfill stops at CEILING - RESERVE - drawn; where it is enforced (site Z producer vs a queue gate) is the CTO's call | C-RESERVE | DQ-t-14 (measured draws) |


---

# ROUND 5 -- CUT (issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~09:2xZ; supersedes the ROUND 5 DRAFT above)

**Rectangle:** the CTO's round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` @91f3ee9da6 section 3 (msg 2158), items 1-4, with rulings
R1 (price_store keeps the write path until SECHIST's writer exists; its retirement is cut the round after) and R2 (meter OPAL_BBGTML;
until it lands the ledger carries one named "unmetered" line). Round 4 CLOSED @a32c0cb89f. The draft's "one intake" and "reserve
enforcement" rows are NOT in this rectangle and stay candidates.

| cell | serves | what | write set | assignee | risk |
|---|---|---|---|---|---|
| DQ-t-15 | FWD-4 | per-kind ceilings: reference / history ceilings seeded from the served demand ledger (largest day per channel, held, never lowered; C-RESERVE "re-measured from the ledger"); a held history reserve from producer code; model_block priced on its component channels (finish = the later of its reference and history finish days) | `bbg_quote.py`, `bbg_allowance.json`, `reserve_estimate.py`, NEW `ceiling_from_ledger.py`, NEW `test_demque_ceiling.py` | `0.9.0_WK_MDPF_DEMQUE~13` | LOCAL |
| DQ-t-16 | FWD-4 (ADDENDUM v0.4) | the standing shape and its state writer: `standing.py` quotes a standing request PER RUN (its cap) and is the ONE writer of `request_state/.../state.json` at the builder address; the request file gains `"shape": "standing"` | NEW `standing.py`, NEW `test_demque_standing.py`, `requests/ETFS_RIVALS-HISTORY-OWED-DAILY.json` | `0.9.0_WK_MDPF_DEMQUE~14` | LOCAL (the real state write is the issuer's run at close: a one-object write the actor names) |
| DQ-t-17 | C-PRICES (ADDENDUM v0.5) | the total-return comparison, BEFORE any TR column: Bloomberg's stored DAY_TO_DAY_TOT_RETURN_GROSS_DVDS (opal-data-etfs `bbg/<date>/history_topup.parquet`, ~1 year for ED, BX, CSCO, BBY, DG) against Yahoo's as-traded close + ex-date cash; per-event table; a written finding on how Yahoo handles splits, dividends, special distributions and interest | NEW `tr_compare.py`, NEW `test_demque_tr_compare.py`, its deliverables folder | `0.9.0_WK_MDPF_DEMQUE~15` | LOCAL (Yahoo read, S3 read-only; nothing served) |
| DQ-t-18 | FWD-2 (R2) | the OPAL_BBGTML meter at site Z: each notebook run of the 07:00 ET runner writes one `bbg_budget.record()` line (no notebook rewritten); the uploader turns it into a ledger row, and a day with no meter line carries one `bbgtml-unmetered` row | NEW `bbgtml_meter.py`, NEW `test_demque_bbgtml_meter.py`, `bbg_ledger_upload.py`, `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` | `0.7.0_AE_CloudOps~ZQ` (site Z) | WORLD (the 07:00 production runner, under `1.0.0_SA_CTO~Z`'s half) |

**Chains:** four, disjoint write sets, no data edge between them. DQ-t-17's 6-name extension (KO, JNJ, T, VZ, MO, XOM) re-runs the same
script when the queued Bloomberg draw `requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json` lands; that draw is a queue item, not a cell.
**Next round (named, not cut):** the TR column (price, cash, TR per ticker per day) by the method DQ-t-17 fixes; one quote front door that
routes the standing shape to `standing.py`; price_store write-path retirement after SECHIST's writer (R1).


---

# ROUND 6 -- CUT (issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~12:4xZ)

**Rectangle:** the CTO's round-5 analysis `ledger/ROUND_ANALYSIS.round5.md` @7732d73c04 section 3 (msg 2426), items 1-3, with rulings R1
(history reserve from the measurement) and R2 (both total-return guards inside the build). Round 5 CLOSED @1e39ebdfb0. Carried, not cut:
the lock floor (graded on the 2026-10-10 02:30Z draw) and the `price_store` write-path retirement (waits for SECHIST's writer). The three
round-5 quotes are frozen beside their requests @70379bb41d.

| cell | serves | what | write set | assignee | risk |
|---|---|---|---|---|---|
| DQ-t-19 | FWD-4 | read a quoted request against its frozen finish day: ON_TIME / LATE / OPEN from `requests/<id>.quote.json` and `ledger/BBG_ACTUALS.jsonl`; today's reference request is read this round (the 2026-10-13 quotes are the second arm, read on their day) | NEW `quote_vs_actual.py`, NEW `test_demque_quote_vs_actual.py` | `0.9.0_WK_MDPF_DEMQUE~16` (worker-light) | LOCAL |
| DQ-t-20 | FWD-3 (R1) | the history reserve = the served ledger's measured largest-day history draw x (1 + margin), held, from the ledger, never typed; a quote whose allowance is not positive says so | `ceiling_from_ledger.py`, `reserve_estimate.py`, `bbg_allowance.json`, NEW `test_demque_reserve_ledger.py` | `0.9.0_WK_MDPF_DEMQUE~17` (worker-light) | LOCAL |
| DQ-t-21 | C-PRICES (ADDENDUM v0.5, R2) | the total-return column in the price store: `cash` and `total_return` (+ `tr_source`, `flags`) beside the unchanged `close_served` / `as_traded_close`; guard (a) a non-ex-date gap against Bloomberg's stored TR is flagged `missing_cash`; guard (b) a money-market fund's TR comes from Bloomberg or an accrual, never Yahoo's 0 | NEW `tr_column.py`, NEW `test_demque_tr_column.py`, NEW `money_market.csv`, `price_store.py`, `PRICE_STORE_CONTRACT.md` | `0.9.0_WK_MDPF_DEMQUE~18` | SERVED (prices.parquet gains columns at the next scheduled draw; existing columns byte-identical) |

**Chains:** three, disjoint write sets, no data edge.
