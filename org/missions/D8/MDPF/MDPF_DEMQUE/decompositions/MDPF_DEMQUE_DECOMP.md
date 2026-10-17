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


---

# ROUND 7 -- CUT (issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~13:3xZ)

**Rectangle:** the CTO's round-6 analysis `ledger/ROUND_ANALYSIS.round6.md` @4f7ded8845 section 3 (msg 2479): R1 (a history backfill draws
on non-trading days at the measured 5,858 a day; 0 on a trading day; a vendor limit warning stops it) and R2 (`--all` over every quote
shape). Round 6 CLOSED @0c72210d2b. Carried, not cut: the total-return column's first served write and the lock floor, both at the
2026-10-10 02:30Z draw (the issuer's real run).

| cell | serves | what | write set | assignee | risk | depends |
|---|---|---|---|---|---|---|
| DQ-t-22 | FWD-4, FWD-3 (R1) | `bbg_quote.py`: a history request is quoted over NON-trading days (`lib/trading_calendar.py`) at the measured ceiling (5,858, claim `measured`, from the ledger's largest day); `allowance_today` is 0 on a trading day; `--today` on the CLI | `bbg_quote.py`, `ceiling_from_ledger.py`, `bbg_allowance.json`, NEW `test_demque_nontrading.py` | `0.9.0_WK_MDPF_DEMQUE~19` | LOCAL | none |
| DQ-t-23 | FWD-4 (R2) | `quote_vs_actual.py --all` reads every quote file; an older shape with no finish_date reads `UNQUOTED` | `quote_vs_actual.py`, NEW `test_demque_qva_all.py` | `0.9.0_WK_MDPF_DEMQUE~20` (worker-light) | LOCAL | none |
| DQ-t-24 | FWD-3, FWD-4 (R1) | the first non-trading-day backfill at site Z: the 15,720-cell TR-comparison request drawn on Saturday 2026-10-10 up to that day's quoted allowance (5,858), stopping on any vendor limit warning or refusal; actuals recorded (`bbg_budget`, `ledger/BBG_ACTUALS.jsonl`) and read against the quote | NEW `bbg_backfill.py`, NEW `test_demque_bbg_backfill.py`, `bbg_ledger_upload.py`, `ledger/BBG_ACTUALS.jsonl`, its deliverables | `0.7.0_AE_CloudOps~ZQ` (site Z) | WORLD (a Bloomberg draw under `1.0.0_SA_CTO~Z`'s half) | DQ-t-22 |

**Chains:** two independent (t-22 -> t-24; t-23). Fan-out 2 of 2 chains.


---

# ROUND 8 -- CUT (issuer 2.0.0_SA_COO~Q1, 2026-10-11 ~05:xxZ)

**Rectangle:** the CTO's round-7 analysis `ledger/ROUND_ANALYSIS.round7.md` @f5553ca3d5 section 3 (msg 3487), items 1-5, with rulings R1
(the non-trading walk keys on TIER, with D1-S5) and R2 (re-freeze under the rule in force, keep the old quote; a STANDING site-Z drawer on
every non-trading day). Round 7 CLOSED at the CVO's slug (msg 3478, MAY-CLOSE 3 of 3, `round-close-check` MAY-CLOSE). Carried, a read only: FWD-3's
Monday 2026-10-12 morning production read grades FWD-3; no cell serves it.

| cell | serves | what | write set | assignee | risk | depends |
|---|---|---|---|---|---|---|
| DQ-t-25 | FWD-3, FWD-4 (R1; rows D1-W19-S1, D1-S5) | ONE change to `quote()`'s history branch by the request's tier: tier 1 draws against the reserve on any day (a Monday SHT8 quote reads a positive `allowance_today` and finishes that day); tier 2+ walks non-trading days at the measured ceiling whatever the reserve's claim; a ceiling not `measured` reads `finish_date null` with its reason, never the weekday rule | `bbg_quote.py`, `test_demque_bbg.py`, NEW `test_demque_tier_quote.py` | `0.9.0_WK_MDPF_DEMQUE~21` | LOCAL | none |
| DQ-t-26 | FWD-4 (R2 quote half; row D1-C-S17) | the walk counts a non-trading day only when a drawer fires on it (`drawer_schedule.py`); `refreeze.py` writes a re-frozen quote beside the superseded one (kept, with its reason); `quote_vs_actual` grades the re-frozen quote and prints both | NEW `drawer_schedule.py`, NEW `refreeze.py`, `bbg_quote.py`, `quote_vs_actual.py`, NEW `test_demque_refreeze.py` | `0.9.0_WK_MDPF_DEMQUE~21` (queue, second) | LOCAL | DQ-t-25 (same file) |
| DQ-t-27 | FWD-3 (R2 drawer half; row D1-C-S17) | the STANDING non-trading-day drawer at site Z: one scheduled fire per non-trading day, drawing open tier-2+ history backfills in rank order up to the measured ceiling, resuming where the last day stopped, stopping on a vendor warning or refusal; receipt and actuals line per run | NEW `standing_drawer.py`, NEW `test_demque_standing_drawer.py`, `bbg_backfill.py`, `test_demque_bbg_backfill.py`, `ledger/BBG_ACTUALS.jsonl`, change-management | `0.7.0_AE_CloudOps~ZQ` (site Z) | WORLD (a standing Bloomberg draw under `1.0.0_SA_CTO~Z`'s half) | DQ-t-26 |
| DQ-t-28 | C-PRICES (row D1-S8) | `redraw_stale.py`: list the served price files still carrying the original 3 columns, reset exactly those symbols in the Yahoo pacer and enqueue ONE paced re-draw request; the second run with nothing stale enqueues nothing | NEW `redraw_stale.py`, NEW `test_demque_redraw_stale.py` | `0.9.0_WK_MDPF_DEMQUE~22` | LOCAL (the issuer's `--apply` and the next scheduled draw are SERVED, under a never-widen half) | none |
| DQ-t-29 | repairs (rows D1-S6, D1-S7) | `bbg_ledger_upload.py` resolves a Name-to-literal assignment before `literal_eval`; `land_cot.py` reads its consumer's keys through `lib/opal_naming.legacy_address` so `pytest data/mdpf/scripts/demque` collects with no INTERNALERROR | `bbg_ledger_upload.py`, `test_demque_bbg_ledger_upload.py`, `land_cot.py`, `test_demque_land.py` | `0.9.0_WK_MDPF_DEMQUE~23` (worker-light, the batch repair cell) | LOCAL | none |

**Chains:** three (t-25 -> t-26 -> t-27 share `bbg_quote.py` and then the schedule; t-28; t-29). Fan-out 3 of 3 chains, cap 8: t-27 is a seat order
at site Z, not a worker slot. Write sets are disjoint apart from `bbg_quote.py`, which one worker's queue holds in order.

**The issuer's acts at the drain (not cells):**
1. After DQ-t-26 merges: `refreeze.py --request-id DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS --as-of 2026-10-09 --reason "rule changed, round 6 R1"` on the
   real requests folder, committed (the superseded quote is kept beside the new one). `quote_vs_actual.py` then reads ONE ruled quote.
2. After DQ-t-28 merges: `redraw_stale.py --apply` on this box's daily-draw home (resets 32 pacer entries, enqueues one request), then the
   scheduled 22:30 local daily draw writes the seven columns; the served read of 141 of 141 files is this round's SERVED real run. NEVER-WIDEN pair:
   CTO half = the round-7 analysis item 3 (@f5553ca3d5); COO half = this section. Blast radius: the 32 listed CUSIP prefixes' `prices.parquet`
   (existing three columns byte-identical, t21's contract); rollback per key = the object's prior S3 version.
3. The ONE real run of each outcome at close, under `deliverables/2.0.0_SA_COO~Q1/`.

**Essential wait (qualified):** DQ-t-27 AC3, the first scheduled non-trading-day fire, cannot precede the next non-trading day the drawer
exists on (2026-10-17 at the latest): a history draw is barred on trading days by round-6 R1 (production would be crowded), so the
positive arm has no on-demand act; the negative arm (a trading day draws 0) is driven on demand in AC2. Reported to the CTO in the round's message.

**Round 8 outcome (record):** t-25 .. t-29 terminal; t-27's first fire drew 5,858 of 5,858 on 2026-10-11 (earlier than the 10-17 bound above). D1-S8
127 of 141 (D1-S9). `ROUND8_REAL_RUN.md`. Closed at the CVO's L10 slug (@50398613b5).


---

# ROUND 9 -- CUT (issuer 2.0.0_SA_COO~Q1, 2026-10-11 ~16:xxZ)

**Rectangle:** the CTO's round-8 analysis `ledger/ROUND_ANALYSIS.round8.md` @92a9b27704 section 3 (msg 3951): R1 (the price store reaches the T-1 frontier
daily: a standing tier-1 extension, the lock reading the latest transactions partition, the one-time gap through the queue), R2 (the 14 rejected
names: no wider band; a per-name cause instrument; the existing files serve with claim `held`; the two near-40 pct names read for client-page use),
Z-S2 and Z-S3 (this seat's cells). Carried, a read only: FWD-3's Monday 2026-10-12 morning production read.

**A PREMISE THE ANALYSIS DID NOT HAVE (measured by the issuer 2026-10-11 ~16:2xZ, row D1-S11):** the transactions store
`s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/` holds ONE partition, `date=2026-06-23`, and its largest Trade_Date is
2026-06-22. No later partition exists, so "the lock reads the LATEST partition" resolves to the same June snapshot today, and the client's
trades since 2026-06-22 are not in this store to be checked. Cut as ruled: t-30 resolves the partition dynamically (it advances by itself when a
later partition lands) and reports `trades_through`; where a served window runs past `trades_through` the lock's claim is `held`, never `measured`
(the existing vocabulary, no new key). The extension's SERVED apply (t-31) is HELD for the CTO's word on this premise: its half "covers both
branches or it is not signed".

| cell | serves | what | write set | assignee | risk | depends |
|---|---|---|---|---|---|---|
| DQ-t-30 | C-PRICES, FWD-1 (R1 b) | `lock.py` resolves the latest `date=` partition holding parquet (no pinned date), exposes `trades_through`, `--partition`; `check()` claims `held` when the window runs past the trades | `lock.py`, NEW `test_demque_lock_partition.py` | `0.9.0_WK_MDPF_DEMQUE~24` | LOCAL | none |
| DQ-t-31 | C-PRICES, FWD-1, FWD-8 (R1 a, c) | `extend_frontier.py`: the standing tier-1 request ending at the T-1 frontier (`expected_last_trading_day`) over every locked symbol, the pacer reset for exactly those symbols, hooked ahead of the draw in `run_daily_draw.sh`; its first run IS the one-time 76-trading-day gap, quoted by the draw's own ledger | NEW `extend_frontier.py`, NEW `test_demque_extend_frontier.py`, `run_daily_draw.sh`, `daily_draw.py` | `0.9.0_WK_MDPF_DEMQUE~24` (queue, second) | LOCAL (the apply and the draw after it are SERVED, under its own never-widen pair, HELD for the CTO) | DQ-t-30 (`trades_through`) |
| DQ-t-32 | C-PRICES, FWD-5 (R2) | `lock_cause.py`: per rejected name the agreement against the old file and the new draw, the disagreeing dates with trade type and ex-dividend/split proximity, whether the first lock pre-dates the floor, a classed cause; `hold_lock_records.py`: the claim `held` with its reason on those lock records (dry-run here; the apply is the issuer's) | NEW `lock_cause.py`, NEW `hold_lock_records.py`, NEW `test_demque_lock_cause.py` | `0.9.0_WK_MDPF_DEMQUE~25` | LOCAL (the apply writes 14 served `lock.json`, SERVED, CTO half = R2) | none |
| DQ-t-33 | FWD-4 (Z-S2, Z-S3; round 7 R2) | a re-quote of a partly drawn request prices the REMAINING cells and says so; a history request is priced on TRADING days; an outcome `COMPLETE` closes a request and sets its drawn date; a re-freeze chains a second superseded quote | `bbg_quote.py`, `quote_vs_actual.py`, `refreeze.py`, NEW `test_demque_quote_remaining.py`, `test_demque_bbg.py` | `0.9.0_WK_MDPF_DEMQUE~26` | LOCAL | none |
| DQ-t-34 | FWD-3, FWD-4 (Z-S3) | the standing drawer closes a request whose every security reached its end date: the completing fire records `COMPLETE`, later fires skip it, no 0-cell `DRAWN` line | `standing_drawer.py`, NEW `test_demque_standing_drawer_close.py`, `ledger/BBG_ACTUALS.jsonl`, change-management | `0.7.0_AE_CloudOps~ZQ` (site Z) | WORLD (the standing drawer under CTO~Z's half; no new draw capacity) | DQ-t-33 (`COMPLETE`) |

**Chains:** three (t-30 -> t-31; t-32; t-33 -> t-34). Fan-out 3 of 3 chains, cap 8: t-34 is a seat order at site Z, not a worker slot.

**The issuer's acts at the drain (not cells):**
1. After DQ-t-33 merges: re-freeze the real TR request again (`refreeze.py`, reason "cells priced on trading days, round 9 Z-S3"); the
   superseded chain keeps all three quotes.
2. After DQ-t-32 merges: `lock_cause.py` over the 14 (the real run, table recorded), then `hold_lock_records.py --apply` (14 served lock.json
   writes; CTO half = round-8 R2; rollback per key = the object's prior S3 version). The two names near 40 pct are read for client-page use.
3. DQ-t-31's `--apply` and the first extended draw: HELD (the premise above). The pair's blast radius when released: the 141 CUSIP prefixes'
   `prices.parquet`, `lock.json`, `splits.parquet`, `dividends.parquet`; rollback per key = the object's prior S3 version; the overlap rows'
   delta is measured against a pre-run snapshot and printed (`close_served` can legitimately restate on a split inside the new tail).
4. The ONE real run of each outcome at close, `deliverables/2.0.0_SA_COO~Q1/ROUND9_REAL_RUN.md`.

**Round 9 amendment 1 (issuer, 2026-10-11 ~16:2xZ; two cells added under the CTO's ADDENDUM 3 and the issuer's own defect; the spec is the CTO's
ruling, so this is an amendment and not a surprise row):**

| cell | serves | what | write set | assignee | risk | depends |
|---|---|---|---|---|---|---|
| DQ-t-35 | C-PRICES, C-IDENTITY (R2; row D1-S12, BLOCKING) | the read-only valuation trace for FTHSX (4 accounts) and PFORX (11): price file -> carrying artifact -> value artifact -> portal route and firm, denominator 15; the three wrong-symbol CUSIPs re-resolved through the EXISTING resolvers with each candidate's agreement printed (no page or served change) | `deliverables/0.9.0_WK_MDPF_DEMQUE~27/` only | `0.9.0_WK_MDPF_DEMQUE~27` | LOCAL (records) | none |
| DQ-t-36 | C-PRICES (issuer defect in DQ-t-31) | `extend_frontier.py` refuses a frontier before the store's latest `valid_to`, so a manual `--today` can never shorten a served file; `apply` then writes and resets nothing | `extend_frontier.py`, NEW `test_demque_extend_guard.py` | `0.9.0_WK_MDPF_DEMQUE~28` (worker-light) | LOCAL | DQ-t-31 (merged @1961d4ee7a) |

Chains now five: t-30 -> t-31 (merged), t-32 (merged), t-33 -> t-34, t-35, t-36. Fan-out for the amendment: 2 of 2 chains, cap 8. The
COO half of the t-31 never-widen pair is written on the bytes AFTER t-36 merges (the override is then covered by the guard, not by a promise).

**Round 9 amendment 2 (issuer, 2026-10-11 ~17:0xZ):** DQ-t-36 merged @df9aaa34cc. Reading the merged bytes for the half found the other
direction of the same override: a `--today` AFTER the local date plans, applies and writes a lock `valid_to` that has not happened, after which
DQ-t-36's own guard refuses every normal run until the calendar catches up. One more cell, `DQ-t-37` (`extend_frontier.py` refuses a `today` after
`date.today()`; `0.9.0_WK_MDPF_DEMQUE~29`, worker-light, LOCAL, workstream EXTGUARD2, depends on DQ-t-36). The half is written after it merges.
DQ-t-36 merged @df9aaa34cc, DQ-t-37 @8e63ec0a23, DQ-t-35 @9ae2f2d054 (the trace: no client page reads the Yahoo file for FTHSX/PFORX; the page
value is B_00's BD market value / units; no re-resolve candidate reaches 90; D1-S12 with the CTO).

**Round 9 amendment 3 (issuer, 2026-10-11 ~17:1xZ):** reading the CTO's ADDENDUM 1 against the merged bytes for the half: "the lock record states
`trades_through`". The row carries only the claim. One more cell, `DQ-t-38` (`ROW_KEYS` gains `trades_through`; `0.9.0_WK_MDPF_DEMQUE~30`,
worker-light, LOCAL, workstream LOCKTHRU, depends on DQ-t-30). The COO half of the t-31 pair is written on the bytes after it merges.
DQ-t-38 merged @1bb7035580; COO half @b3baaeb04c; CTO half SIGNED (msg 4028) with one condition.

**Round 9 amendment 4 (issuer, 2026-10-11 ~17:2xZ):** the CTO half's condition: `commonwealth_daily_valuation.py:469` reads `splits.parquet` in
production, so a name that gains a split row in the extension keeps its prior file and is listed. The issuer reads it as the WHOLE name (the
prices are split-adjusted from the same pull; restated prices beside an old `splits.parquet` would be inconsistent). One more cell, `DQ-t-39`
(`price_store.write` holds a name whose pull adds a split row; `0.9.0_WK_MDPF_DEMQUE~31`, worker-light, LOCAL, workstream SPLITHOLD). The
apply runs after it merges. Names held are listed with split date, ratio and the account count of holders (a positions read); those rows get their
own pair and wait on Andrew if the valuation reaches a client page.

**Round 9 amendment 5 (issuer, 2026-10-12 ~03:2xZ):** CTO ADDENDUM 6 (msg 4243): dell2's IRPT_BCKEND enrolment adds about 938 symbols a day to
the standing extension against the pacer cap of 400, which stays; the daily pull becomes INCREMENTAL and BATCHED, proved cell-for-cell on 50+
symbols, else tiered. One cell, `DQ-t-40` (`batch_pull.py`, the HTTP-request measurement, the equality report; `0.9.0_WK_MDPF_DEMQUE~32`, worker,
LOCAL, workstream BATCHPULL). The cell MEASURES the HTTP requests of the library's multi-ticker call first: the pacer's unit is "vendor requests",
and a library call that issues one HTTP request per symbol underneath would leave Yahoo's load unchanged. Wiring into `demand_queue.draw` /
`daily_draw` (the pacer counting HTTP requests) is the next order, written on its report and run under its own never-widen pair; the IRPT enrolment
waits on it.
DQ-t-40 merged @34040149bb: batch equals per-symbol (50 of 50) but the library issues one HTTP request per symbol (verdict BATCH_DOES_NOT_REDUCE).

**Round 9 amendment 6 (issuer, 2026-10-12 ~03:5xZ):** CTO ADDENDUM 7 (msg 4252) rules branch (c): the standing extension is TIERED. One cell,
`DQ-t-41` (`extend_frontier.py` tiers from `requests/ENROLMENT_TIERS.json`: DAILY 141 stored plus ADVI's 15, ROLLING IRPT's 782 in FWD-9 rank
blocks on a 5-trading-day cycle, a refusal above the cap less a reserve of 20, `--plan-week`, the per-tier lag in the freshness entry;
`0.9.0_WK_MDPF_DEMQUE~33`, worker, LOCAL, workstream ROLLTIER, depends on DQ-t-31/36/37). The apply is the issuer's under its own pair, written
on the merged bytes. dell2 was told the lag in words (crossbox CALL XB-20261012T033435Z-54b6, `DELL2_IRPT_ENROLMENT_LAG_20261012.md`).

**Round 9 close of DQ-t-41 (issuer, 2026-10-12 ~04:2xZ):** merged @dbf7bacc77 (AC1 TIER-OK, AC2 TIER-REAL-OK: 7 trading days, max 306 requests a day,
782 rolling names each within 5 trading days; folder 145 passed). Rulings on its rows, all inside this decomposition: **W33-S2** the enrolment key
`rolling[].stored_at_enrolment` (the 96 CUSIPs in the index when IRPT was enrolled; they stay daily) is RATIFIED, it is the snapshot the cell's rule needs.
**W33-S4** an ADVI fund that is also an IRPT name is DAILY (8 of the 10 overlap are not yet stored; the rolling set is 774 once they land). **W33-S3** the
freshness entry is NOT landed: the served config holds one JSON object per entry and the store is thousands of cusip-partitioned parquet files with an
index.parquet/csv, so no existing mode fits and a new mode is a build the moratorium bars; asked of the CTO. Read-only `--plan` against the real
store after the merge: daily 141, rolling 0, rolling_not_landed 782, so the Monday 22:30 run asks for the same 141 names as before (DELTA=0); the
first rolling day is after IRPT's history lands, and the SERVED pair is written then, covering the in-block and out-of-block branches.

**Round 9 amendment 7 (issuer, 2026-10-12 ~04:3xZ):** CTO ADDENDUM 8 (msg 4260) withdraws the freshness-entry clause: the lag is DECLARED in
`ENROLMENT_TIERS.json` (`freshness_basis: trading-day-frontier`, `cycle_trading_days` per tier) and the week close prints the declared cycle against
every name's measured lag with the denominator; no checker, alarm or mode. One cell, `DQ-t-42` (the declaration with one-source validation, and a
read-only `--lag-report`; `0.9.0_WK_MDPF_DEMQUE~34`, worker, LOCAL, workstream LAGDECL, depends on DQ-t-41).

**Round 9 close of DQ-t-42 (issuer, 2026-10-12 ~04:2xZ):** merged @e148463ae6 (AC1 LAG-OK, AC2 LAG-REAL-OK: 141 indexed, daily 127 within and 14 over at lag 77 from
2026-06-23, rolling 0 landed and 782 not landed; folder 148 passed). The declaration is in `ENROLMENT_TIERS.json`; the report is
`extend_frontier.py --lag-report`; no checker or mode exists. **W34-S1 ruled:** the cell measured the lag from `valid_to` (the lock window end the
extension writes); `as_of` is the max date of the price rows and is the stored max date proper. They agree on all 141 today. The week close
recomputes each name's lag from `as_of`, prints the count of names where the two differ, and where it is non-zero `as_of` governs. **W34-S2:** the
rolling cycle of 5 is unmeasured on real data until IRPT's history lands (2026-10-14); the week close is the first reading.

**Round 9 amendment 8 (issuer, 2026-10-13 ~14:2xZ):** CTO msg 4875 rules the Bloomberg client-history need (CARD-A, 1,319 names): cut the per-security
window cell, the P1 living-client slice first and former clients last, no new allowance, the P1 count, cells and days-to-finish printed before the first
draw, and a number brought to the CTO if P1 alone runs past 30 days. One cell, `DQ-t-43` (`bbg_quote.quote` prices a window per security;
`card_a_slice.py --priority P1 --out --quote`; `0.9.0_WK_MDPF_DEMQUE~35`, worker, LOCAL, workstream CARDASLICE, depends on DQ-t-25). The need's per-security
CSV was moved out of the repo under the CTO containment ruling @0e8209c33c (client account ids), so windows are derived from the silver transactions'
first trade date per CUSIP to the need's end 2026-06-23. Also: `rank.py` NEED_FILE and `lock.py` still name the moved CSV path (row D1-S15). The 50-cell
scanner first slice from COO~R1 (msg 4877) is quoted and frozen @fc431ae325, the full scanner request stays filed and undrawn.

**Round 9 close of DQ-t-43 and amendment 9 (issuer, 2026-10-13 ~14:5xZ):** DQ-t-43 merged @b956c6307e (AC1 SLICE-OK, AC2 SLICE-REAL-OK: P1 609 names, 607 priced and 2
FDIC placeholders unresolved, 882,024 cells, 330 trading days at an implied 2,673 cells a day; folder 151 passed). The number went to the CTO (msg to
1.0.0_SA_CTO~DELL1, ask: rank-ordered ~2-week blocks or a higher allowance). Andrew-direct 2026-10-13 (CTO msgs 4881, 4884, 4889, 4892) adds the 2012 floor, the
need-class declaration with refusal, the 365-day non-client window, the surface order A/B/E/C/D with 10 percent held for ad-hoc, and a hold on new Bloomberg
draws until his form is complete. One cell, `DQ-t-44` (the Bloomberg-side refusal and `--check-declared`, request declarations, the TR remainder by identity,
the P1 window to the frontier intersected with held; `0.9.0_WK_MDPF_DEMQUE~36`, worker, LOCAL, workstream NEEDCLASS, depends on DQ-t-43). The Yahoo side
(`demand_queue.validate`, `extend_frontier._request`, the device queue copies of the in-flight IRPT and ADVI requests) is a separate cell `DQ-t-45`, cut after
`DQ-t-44` merges, so that no nightly draw is refused mid-flight. The qualification table is `deliverables/2.0.0_SA_COO~Q1/QUEUE_QUALIFICATION_20261013.md`
@ac96e00cbd; the form is `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`.

**Round 9 amendment 10 (issuer, 2026-10-13 ~15:2xZ):** CTO msg 4904: hold CARD-A P1 entirely, the 16-name block included, until three counts are read and printed:
how many P1 names Yahoo can price, how many have Black Diamond units and market value on their held dates (an exact price, no vendor draw), and the residual
Bloomberg-only set with its cells. One cell, `DQ-t-46` (`p1_coverage.py`, read only, no vendor call; `0.9.0_WK_MDPF_DEMQUE~37`, worker, LOCAL, workstream
P1COVER, depends on DQ-t-43). Inputs located by the issuer: Cottonwood bucket `s3://opal-data-cot/` `gold/canonical/holdings/YYYY-MM-DD.parquet` (daily from
2026-04-22) and `silver/cot_holdings.parquet` (units, market_value, cusip; snapshot 2026-06-09); earlier history is for the worker to find and name.

**Round 9 close of DQ-t-44 and amendment 11 (issuer, 2026-10-13 ~16:3xZ):** DQ-t-44 merged @900406e221 (AC1 CLASS-OK, AC2 CLASS-REAL-OK: 7 of 8 Bloomberg request files accepted,
the ABNB model block refused by the 365-day rule and held undrawn per CTO msg 4912; the TR comparison plans 1,004 cells on MO and XOM; the P1 slice re-windowed to the
frontier on the Commonwealth sign table: 609 names, 607 priced, 471,522 cells, 175 trading days; folder 156 passed). Worker rows S1-S12 ruled in the order's AMENDED
section; S2 disarmed (`DISARM_EVIDENCE_D1_W36_S2_20261013.md`). The TR quote was re-frozen @eeb36aba99 with its finish corrected to 2026-10-17 (the refreeze tool counted cells, not
identity). The six Yahoo requests in the repo and the device queue were declared by the issuer (client, window start) @this commit. One cell, `DQ-t-45`: the same
refusal in `demand_queue.validate` and `--check-declared`, and the standing extension declares itself (`0.9.0_WK_MDPF_DEMQUE~38`, worker, LOCAL, workstream YCLASS, depends on
DQ-t-44). Row D1-W36-S8 (ADVI request carries no vendor or channel) is read by the Yahoo-side check, which keys on `securities` without a Bloomberg vendor.

**Round 9 close of DQ-t-46 and DQ-t-45, and amendment 12 (issuer, 2026-10-13 ~17:xxZ):** DQ-t-46 merged @1d7ad82723 (P1 coverage on the merged window: Yahoo in store 0, rejected 5, no
symbol 601; Black Diamond units and value 11 names and 126 held days; residual 606 names, 467,992 of 468,118 cells; cash-identifier rule for CFNCASH and FDIC). DQ-t-45 merged
@6f6a61123b (the Yahoo side refuses an undeclared or over-window request; the standing extension and `redraw_stale` declare client; device queue 7 of 7 and requests 2 of 2
accepted). Rows W37-S1/S3 and W38-S2 disarmed (evidence files). Andrew-direct via CTO msg 4931 (form @e961fee72f): (1) incremental mode is the last 5 trading days on every
surface once a need's backfill is covered, with a targeted refill for a wider gap; (2) research-app model data keeps `HIST_START` 2016-01-01 as a NAMED exception, ABNB (989
cells) may draw; (3) ACWI and IWM leave rival funds. One cell, `DQ-t-47` (the named exception in `bbg_quote._validate`, `0.9.0_WK_MDPF_DEMQUE~39`, worker, LOCAL, workstream
MODELEXC, depends on DQ-t-44). Item (1) on the Yahoo standing extension is a SERVED change with its own question to the CTO (no Yahoo request is saved by a 5-day window; a split
restates the history), so it is NOT cut here; item (3) and the Z-changes are site Z and ETFS_RIVALS's.

**Round 9 amendment 13 (issuer, 2026-10-13 ~17:xxZ):** CTO msg 4936 answers the incremental-rule question: Yahoo takes the last 5 trading days normally and a full re-pull of a
name only when a split (or another restatement the store keys on) lands, with a targeted refill for a gap wider than 5 trading days; the same request count; a SERVED change under its
own never-widen pair, to be proved 50 of 50 cell-equal on a no-split day and on one split arm. One cell, `DQ-t-48` (`incremental_append.py`, `incremental_plan.py`,
`incremental_equal.py` and a test file; LOCAL, builds and proves, wires nothing; `0.9.0_WK_MDPF_DEMQUE~40`, workstream INCREMENTAL, depends on DQ-t-37/40/45). The wiring into
`daily_draw.py` and `extend_frontier.py` is a later SERVED cell (`DQ-t-49`) cut on this cell's report, with its pair written first.

**Round 9 close of DQ-t-47 and DQ-t-48, and amendment 14 (issuer, 2026-10-13 ~18:xxZ):** DQ-t-47 merged @2989e78de8 (ABNB admitted under the named 2016 exception, 989 cells, 8 of 8
Bloomberg requests accepted); DQ-t-48 merged @9de742d8f9 (the Yahoo incremental path proved 50 of 50 cell-equal on a no-split day, one split arm refilled and equal; plan 326 names, 326
requests, writes 2,959 cells instead of 427,433; lock record differs on LCEYX and FTHSX, row W40-S1). Andrew-direct "Go with your rec" and Surface B (CTO msgs 4946, 4964): the porting
test is confirmed (returns, 10 bps, 5 intervals, at most 10 cells a security) and Yahoo-sourced client prices read UNVERIFIED until they pass; B1 is option C on the client-income
basis with the total-return field for the 11 long-held bonds, $1.00 money market funds skipped by fund type (UNREAD pulled), the 8 rejected funds joined. Cells: `DQ-t-49` (the porting-test
request and comparator, `0.9.0_WK_MDPF_DEMQUE~41`, workstream PORTING) and `DQ-t-50` (the B1 request: `dates` and per-entry `fields` in `bbg_quote`, `b1_request.py`;
`0.9.0_WK_MDPF_DEMQUE~42`, workstream B1REQUEST). Not cut here: the UNVERIFIED labelling (SERVED, its own pair), Z8 and Z9 (the models pull's incremental change and meter; the
notebooks are production code on the Bloomberg device and their change is a site-Z act). The draw of B1 waits on Andrew's form.

**Round 9 close of DQ-t-49 and amendment 15 (issuer, 2026-10-13 ~18:xxZ):** DQ-t-49 merged @567a058ddb (the porting-test request: 326 securities, 2,497 cells; comparator: every interval within
10 bps; 174 passed). Its worker found 182 of 326 held windows fit fewer than 5 intervals and could never pass. CTO ruling msg 4976: always 5 intervals, a length that does not fit is
replaced by a sha256-drawn length that does, minimum 5 trading days, overlap allowed, a window under 10 trading days is UNTESTABLE (a reason, not a FAIL). One cell, `DQ-t-51`
(`porting_test.py` and its tests; `0.9.0_WK_MDPF_DEMQUE~43`, worker, LOCAL, workstream PORTINTERVALS, depends on DQ-t-49).

**Round 9 close of DQ-t-50 and DQ-t-51, and amendment 16 (issuer, 2026-10-13 ~18:xxZ):** DQ-t-50 merged @911d2806c8 (the B1 Cottonwood request at option C depth: 614 securities, 37,514
cells, finish 2026-11-07 on non-trading-day fires, filed and priced @ee5ad75db7, NOT drawn; the $1.00 skip matched none of 227 cash equivalents, 194 UNREAD pulled). DQ-t-51 merged
@adbdc57967 (the porting test always draws 5 intervals: 326 testable, 0 UNTESTABLE, 1,630 intervals, 3,195 cells). The dell1 pivot packet (CTO pivot order XB-c5bf, MSTR msg 5009):
DEMQUE is DRIVE for the standard card, the P3 exclusion and the SECCLASS sync cell (O6, O7); former clients (P3) are never drawn, a match-open name (P2) draws only after its match
resolves; do not start a new Bloomberg draw until Andrew's form is complete. Measured at 14:2xZ: the price index P1 246, P2 72, P3 8; the IRPT request P1 630, P2 229, P3 19. The
device queue copy of the IRPT request was cut to P1 (630) by the issuer (original kept in the scratchpad; the repo copy stays as filed). One cell, `DQ-t-52` (`priority_gate.py`, `rank.py`
refusal, the extension tiers and the daily draw skip P2 and P3, fail closed; `0.9.0_WK_MDPF_DEMQUE~44`, worker, LOCAL, workstream PRIGATE). The SECCLASS sync cell and the P1 windows to each
account's held dates (the active-account set dell2 publishes) are later cells; this cell does not add them.

**Round 9 amendment 17 (issuer, 2026-10-13 ~18:xxZ):** CTO msg 5025 (cluster packet O6/O7): B1's CUSIPs classified: 613 P1, 1 P2 (ABNFX, held back), 0 P3 (@13722430d4); the `rank.py` P3
refusal is DQ-t-52 (in flight). The DEMQUE half of the SECCLASS sync (`C-DEMQUE-SECCLASS-SYNC`, PRD addendum): one cell, `DQ-t-53` (`secclass_sync.py --prove`, read only: one real
security's key printed equal on the request row, the unresolved entry and the `etf-classifications` row, plus the negative arm; `--coverage` of landed fund names; `0.9.0_WK_MDPF_DEMQUE~45`,
worker, LOCAL, workstream SECCLASSSYNC). Measured by the issuer: the table's one hash key is `ticker`, so the key a human reads across the three places is the symbol string.

**Round 9 close of DQ-t-52 and DQ-t-53, and amendment 18 (issuer, 2026-10-13 ~20:2xZ):** DQ-t-52 merged @0294f140f0 (the priority gate: P3 never drawn, P2 waits, P1 only, on CLIENT requests; non-client requests are not gated;
fail closed; index P1 246, P2 72, P3 8; folder 187 passed). DQ-t-53 merged @2498d1dabc (key AES equal across the request row, the unresolved list and the `etf-classifications` row; 108 of 131 landed fund names
classified). The B1 fund-type request (227 cells, FUND_TYP) is filed and priced @6a54a440d6. Andrew-direct ~20:0xZ and ~20:1xZ (CTO msgs 5130, 5134, 5139): the $1.00 check is YES; NO quota limit was hit on
10-13 (Bloomberg was not logged in and there was no BBGTerminal fallback), so non-trading-day history pulls expand cell for cell with the unused trading-day allowance, the site Z drawer reading the `bbg_budget`
ledger at run time and the dell1 quote staying at zero carried over; surface E has a turnaround CAP (10 percent of the day's history allowance, refused at intake naming the cap, never split); D1 to D5 approved
(TR remainder 1,004 cells, ABNB 989, ICT 1, scanner slice 1 50, the full scanner list 1,038 only if slice 1 reads non-USD). Two cells: `DQ-t-54` (the carry-over, `standing_drawer.py --carry-over`;
`0.9.0_WK_MDPF_DEMQUE~46`, workstream CARRYOVER) and `DQ-t-55` (the surface E cap, `surface_e_intake.py`; `0.9.0_WK_MDPF_DEMQUE~47`, workstream SURFACEECAP). CORRECTION to my own message 5133: I priced the cap off
the 2,673-a-day averaged rate (about 267); the cap is 10 percent of the measured history ceiling, 5,858, so 585 cells, and a one-security one-year two-field request (504 cells) is accepted under it.

**Round 9 close of DQ-t-55 and amendment 19 (issuer, 2026-10-13 ~21:xxZ):** DQ-t-55 merged @450bf78800 (the surface E cap: 10 percent of the measured 5,858 history ceiling = 585 cells, refused at intake naming the
cap; a one-security one-year two-field request, 504 cells, accepted). The CTO lifted the draw hold (msg 5165): the form is complete. The issuer measured that the standing drawer returns ONE open request (the TR comparison):
B1 (CUSIP entries with `dates` and per-entry `fields`), the porting test (CUSIP single-day entries) and the fund-type check (a `reference` request) are not drawable by it. CTO msg 5174: one drawer, one queue; teach it
all three. One cell, `DQ-t-56` (`standing_drawer.py`: `bloomberg_id` with a `/cusip/` form probed with one row first, `dates` entries drawn by identity, per-entry `fields`, the `reference` channel, the priority gate on client
requests, `--open` and `--plan` for requests without a request-level window; `0.9.0_WK_MDPF_DEMQUE~48`, worker, LOCAL, workstream DRAWERENTRIES, depends on DQ-t-54 which edits the same file, so it is spawned after that merge).
The porting test request is filed and frozen (326 CUSIPs, 3,195 cells, `MDPF_SECHIST-CARD-A-PORTING-TEST`). The two-week total is `TWO_WEEK_TOTAL_BY_SURFACE_20261013.md`: about 62,700 cells wanted against 23,432 at the
day rate; the fit with the expansion is UNMEASURED until the 2026-10-17 receipt prints production's unused cells (CTO msg 5174).

**Round 9 amendment 20 (issuer, 2026-10-13 ~21:5xZ):** dell2 published the active Cottonwood set (CTO msg 5216; commit `ec617572b8` on box/dell2; both sha256 values verified by the issuer against the commit: 42,319 rows,
769 active accounts, 3,357 securities, windows from each account's earliest record floored at 2012-01-01, `held_to` a date or `open`). Measured by the issuer (counts only): 609 of B1's 613 CUSIPs are in the set; clipping B1 to
its windows takes 37,439 cells to about 34,341 (saves about 3,100, 99 CUSIPs shrunk, 1 emptied; 4 CUSIPs not in the set keep their window). The ABNFX hold-back was a hand edit of the filed request; the builder now holds back
P2 and P3 itself. One cell, `DQ-t-57` (`active_set.py`, `b1_request.py` clip and hold-back; `0.9.0_WK_MDPF_DEMQUE~49`, worker, LOCAL, workstream ACTIVEWINDOWS, depends on DQ-t-50 and DQ-t-52). The issuer re-files and re-quotes B1 on the
merged bytes. Also filed: `VALUATION_TRACE_DEIDENTIFIED_DQ_t35.md` (the chain, counts only) for the CVO's grade of `DQ9-t35-AC2`, whose original trace was moved out under the containment ruling. DQ-t-54 merged @8b7c76ad35 (carry-over).
DQ-t-56 (drawer) is in its second pass, held at merge until the full scanner request's `draw_hold` is honoured (row W48-S1, ARMED).

**Round 9 amendment 21 (issuer, 2026-10-13 ~22:3xZ):** both never-widen pairs for the two SERVED cells are signed (call `dell1-20261013T214300Z-eb2a`, CTO msgs 5245, 5249, 5251; `ledger/NEVER_WIDEN_R9_YAHOO_{A,B}_{COO,CTO}_HALF.md`).
Pair A (wire the Yahoo incremental path): Branch 1 and the gap branch SIGNED on two binding conditions (appended rows carry the TR columns and the 50-name proof is re-run including them; the receipt lists names appended without a re-lock and a
failed `lock.check` makes the name held); Branch 2 (gained split, restated bar) stays HELD, listed `HELD_RESTATEMENT`, files unchanged. The issuer found while writing the half that `incremental_append.py` carries no TR columns, so DQ-t-48's 50-of-50 covered
price cells only; named in the pair. One cell, `DQ-t-58` (`daily_draw.py`, `price_store.py` `write_incremental`, `incremental_equal.py --tr`; `0.9.0_WK_MDPF_DEMQUE~50`, worker, **SERVED**, workstream WIREINCREMENTAL, depends on DQ-t-48/21/31). Pair B (the `porting_verdict`
column on the index, 2 keys): cell `DQ-t-59` is cut AFTER `DQ-t-58` merges (same file, `price_store.py`). The downstream label in `commonwealth_price_need.py` / `land_cot.py` is routed by the CTO to dell2's ADVI_COTBKF.

**Round 9 amendment 22 (issuer, 2026-10-13 ~23:2xZ):** the pair B cell, `DQ-t-59` (the `porting_verdict` column on the store index, 2 keys; `price_store.py` `INDEX_COLS` / `index` / `write_index` / `--index-preview`; `0.9.0_WK_MDPF_DEMQUE~51`, worker, SERVED, workstream PORTINGVERDICT, depends on
DQ-t-49/51/58). It is cut now and provisioned AFTER `DQ-t-58` merges (same file; `DQ-t-58` is in its third pass: the issuer found at the drain read that a held name would raise in `unresolved.update` and crash the nightly run, and ruled the fix, order amendments of ~23:0xZ and ~23:3xZ). The
verdicts file path is the device state home (`~/.opal/demque/porting_verdicts.json`); it is written by a later cell after the Bloomberg porting draw, never by this one.

**Round 9 amendment 23 (issuer, 2026-10-14 ~00:3xZ):** the CTO's msg 5292: dell2's Active Cottonwood set V2 (commit `4d427d3bbb`, `ACTIVE_COTTONWOOD_SET_V2.csv` sha256 `5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae`, 41,826 rows, 860 accounts, 3,368 securities, 834 blank-CUSIP rows) SUPERSEDES V1 for P1 windows; the two hashes (V2 and `REVERSE_MATCH_V3.csv`
`0783f088aecb...`) were verified by the issuer against the commit, and the four bond and T-bill CUSIPs V1 did not hold (`DQ-t-57`) now have one row each. One cell, `DQ-t-60` (the pinned file, commit and sha256 in `active_set.py`; `0.9.0_WK_MDPF_DEMQUE~52`, worker, LOCAL, workstream ACTIVEV2, depends on `DQ-t-57`). The issuer re-files and re-quotes B1
on the merged bytes. Note: `dq_t57_real.py` pins V1's counts and reads as a history record after this merge.

**Round 9 amendment 24 (issuer, 2026-10-14 ~04:3xZ):** the 2026-10-13 22:30 ET scheduled run (the first with the priority gate, the need-class refusal and the tiers; rc 0, 81 minutes) is read: extension DRAWN 535,407 of 581,955 cells, IRPT P1 PARTIAL 29,124 of 81,270, the other three jobs 0 (pacer cap); 398 names processed, 308 LOCKED
and written, 90 REJECTED and not written; the store grew from 326 to 483 names; 225 unresolved rows; the gate skipped 1; the lag report reads daily tier 130 of 144 within cycle and rolling tier 258 of 259. The 14 over in the daily tier (LCEYX, FTHSX, HLMEX, IWS, IWP, IWN, IWO, VSEIX, PFORX, RPIFX, VSS, VWO, MISIX, PIMSX) are stuck at 2026-06-23 on a failed
identity lock (all `LOW_TRADE_AGREEMENT`, passing 39% to 88% of observations; FTHSX, PFORX and RPIFX near 40%). CTO msg 5411 RULES: no looser identity rule; they leave Yahoo and are priced by Bloomberg under surface B (depth c, active-Cottonwood windows), priced and quoted first; BRKB is a symbol-form fix. Cell `DQ-t-61` (the B1 builder takes a named
CUSIP list; `0.9.0_WK_MDPF_DEMQUE~53`, worker, LOCAL, workstream YAHOOFAILED14, depends on DQ-t-50/57/60). The BRKB symbol cell (`DQ-t-62`) and `DQ-t-59` are cut after `DQ-t-58` merges (shared files). The version baseline of the store after the run is `STORE_BASELINE_AFTER_2026-10-13_RUN_VERSIONS.csv`.

**Round 9 amendment 25 (issuer, 2026-10-14 ~05:1xZ):** `DQ-t-58` merged @ea0dd99e4e (the Yahoo incremental path wired under pair A; the merge needed the investigation file resolved by id because the row gate refused the auto-union's duplicates; recorded here so the next drain uses `SAFE_MERGE_IN_TREE=1`). `DQ-t-61` merged @0288b4fb5c; the 14-name Bloomberg request
`MDPF_SECHIST-CARD-A-B1-YAHOO-FAILED-14` is filed @2de831ee1b, priced and quoted (14 CUSIPs, 7,685 cells at depth c on the V2 windows, finish 2026-10-18 at zero carried over) with a `draw_hold` until the CTO or Andrew approves the quote (CTO msg 5411: priced and quoted first). `DQ-t-59` (worker `~51`) is in flight on a base
that carries `DQ-t-58`. One more cell, `DQ-t-62` (the share-class symbol form: `BRKB` goes to Yahoo as `BRK-B`, keyed as given; `0.9.0_WK_MDPF_DEMQUE~54`, worker, LOCAL, workstream SYMBOLFORMS, depends on `DQ-t-58`; one live probe request allowed). The first nightly run on the wired path is 2026-10-14 22:30 ET; the version baseline for comparison is `STORE_BASELINE_AFTER_2026-10-13_RUN_VERSIONS.csv`.

**Round 9 amendment 26 (issuer, 2026-10-14 ~19:3xZ):** Andrew-direct ~18:5xZ, relayed by the CTO (msg 5713): "ETFS_RIVALS is done now, all it needs is its backfill sorted out in DEMQUE." `2.0.0_SA_COO~V1` cited three measured gaps (msg 5716, `BACKFILL_GAPS_FOR_DEMQUE.md` @c9e98081a6): total return on held days (123,933 units), the close on dialog-curve days (89,717 units on 10-14, 89,216 on 10-13) and `DVD_HIST_ALL` for the securities with no corporate-actions row. Cell `DQ-t-63` (`etfs_rivals_intake.py`: seven requests, TR and close in three disjoint newest-first stages 30/90/365 on Andrew's "C1 yes, approved in that order", plus the dividend request; `0.9.0_WK_MDPF_DEMQUE~55`, worker, LOCAL, workstream ETFSINTAKE, depends on DQ-t-43/44/50). The cell builds and reports; the issuer files and quotes the requests on the merged bytes, behind the approved B1 cells and the 14-name request. Issuer finding: V1's Row 3 list holds 71 keys and the last is `nan` (a null key), so the dividend request is 70 securities.

**Round 9 amendment 27 (issuer, 2026-10-15 ~17:5xZ):** Andrew-direct 2026-10-15, relayed by the CTO (msg 6105; ruling `org/missions/D8/ADVI/ADVI_COTBKF/ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` @f984c02191, items 2 to 5): "Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance." Measured at HEAD before the cut: (1) NO `draw_hold` stands on B1 or on the 14-name request (`MDPF_SECHIST-CARD-A-B1-YAHOO-FAILED-14`'s was lifted @d11d20734b, 10-14 00:34Z, after CTO msg 5419; B1 never carried one); `standing_drawer.py --open` lists both, plus the porting test after them in file order. Both draw through the queue on non-trading days; lifting that rule is Andrew's call (CTO call `dell1-20261015T174959Z-99be`, REC (a) yes for B1 and failed-14), so until he answers the first fire for them is 2026-10-17. (2) The porting test (3,195 cells) already sorts after B1 and failed-14 (tier 2, no rank, file order). (3) and (4) are new work and they are cut in this order: `DQ-t-64` NOW (`0.9.0_WK_MDPF_DEMQUE~56`, worker, LOCAL, workstream INACTIVESET, depends on DQ-t-57/60): `inactive_set.py`, a read-only census of the securities no V2 active account holds, how many have a symbol, how many are stored, and the nights one Yahoo pass takes at the 380-request cap. The two SERVED cells are cut AFTER `DQ-t-64` merges and its census is read, and the first of them behind a signed never-widen pair (it moves a served file): `DQ-t-65` re-points the standing Yahoo extension to the inactive-only set (the DQ-t-52 gate stops excluding P2 and P3 for Yahoo, since Andrew's new word admits inactive names there; V2-held names stop being extended) and adds the daytime batches the quote needs; `DQ-t-66` labels every stored Yahoo price of a V2-held name not-for-active. The label is a SEPARATE index column, not a value of `porting_verdict`: the porting test grades a price's parity, "not for active" grades who may use it, and one column carries one intent (TAXONOMY LAW iii); the enum and its census arrive with the cell. The existing active-name Yahoo prices stay stored (ruling item 4).

**Round 9 amendment 28 (issuer, 2026-10-15 ~18:1xZ):** `DQ-t-64` merged @0a1fa594f8 (225 tests pass on the merged tree); its real census: 4,634 CUSIPs held, 2,929 in V2, 1,705 outside it (P1 32, P2 1,448, P3 225), 10 of them stored, 477 V2-held names stored, and only 14 of the 1,705 with a symbol (one Yahoo pass 14 requests, one night at the 380 cap). CTO msg 6114 (ruling amendment 1 @bed1cdb778) RULES that the 1,448 P2 names count as inactive for Yahoo under the not-for-active label in its own column, that a P2 holder that later matches into V2 moves its names to ADVI_COTBKF's Bloomberg need, and that the non-Bloomberg CUSIP-to-symbol resolver is the next cell. No external resolver is needed: Cottonwood's own silver transactions carry a `Symbol` column (`rank.load_transactions` reads six columns and drops it), and a pre-measure by the issuer counts 1,071 of the 1,705 inactive-only CUSIPs with a non-blank one (counts only; asset types of the 1,705: Equity 609, Mutual Fund 388, Fixed Income 303, Cash Equivalent 234, ETF 58, UIT 41, closed-end 31, Annuity 29, so many will still fail the identity lock or return no Yahoo data, which the lock and the unresolved list already handle). Cell `DQ-t-65` (`0.9.0_WK_MDPF_DEMQUE~57`, worker, LOCAL, workstream INACTIVESYMBOLS, depends on DQ-t-64): `inactive_set.py` takes its symbols from the transactions after the index and the request files, and the census reports `tx_symbol_only`. Amendment 27's two later cells are renumbered: the SERVED cells stay behind this one, `DQ-t-66` re-points the standing Yahoo extension to the inactive-only set and `DQ-t-67` adds the not-for-active column to the index (one signed never-widen pair covers the extension's target set and the index, both served).

**Round 9 amendment 29 (issuer, 2026-10-15 ~18:3xZ):** `DQ-t-65` merged @b3b9b93e2b (228 tests pass on the merged tree): of the 1,705 securities outside V2, 1,071 now carry a symbol (1,057 from Cottonwood's own transactions), 634 do not, one Yahoo pass is 1,071 requests (three nights at the 380 cap alone). Three cells are cut, with disjoint write sets (three chains): `DQ-t-66` (`0.9.0_WK_MDPF_DEMQUE~58`, worker, SERVED, workstream YAHOOGATE): the Yahoo leg's gate becomes the V2 active set instead of P2/P3 (the Bloomberg-side gate is untouched), and a landed name enrolled in no tier rolls (the old rule would put ~1,000 landed inactive names in the daily tier and `_day` refuses over 380, which stops the nightly run); `DQ-t-67` (`~59`, worker, LOCAL, workstream INACTIVEREQ): `inactive_request.py`, the Yahoo history requests for the symbolled inactive-only names in files of at most 300, start 2012-01-01, end the closed frontier, client need class, built into a scratch directory; `DQ-t-68` (`~60`, worker, SERVED, workstream USECLASS): the `use_class` index column (`NOT_FOR_ACTIVE` | `INACTIVE_USE`, fail closed), its own column beside `porting_verdict`. `DQ-t-66` and `DQ-t-68` change what the nightly run writes, so they are BUILT now and MERGED only after the never-widen pair `ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_{COO,CTO}_HALF.md` is signed (the COO half is filed with this amendment; the CTO half is asked). The backfill files are PLACED in the queue by the issuer after the merge, under the same pair. Item 3's "added daytime batches" is NOT cut: the pacer's 400 a day is a rate guard the nightly run already respects, the nightly run used 319 of 400 on 10-14, and the whole backfill fits in about four nights at the cap; a daytime run would raise the cap, which is a vendor-risk change nobody has asked for. Renumbering: amendments 27 and 28 named the served cells `DQ-t-65` and `DQ-t-66`/`67`; the cells are as numbered here.

**Round 9 amendment 30 (issuer, 2026-10-16 ~01:2xZ):** the first run under the active-set gate (started by hand 2026-10-15 23:54Z on Andrew's "do yahoo runs now") read clean against the store's S3 versions: 400 of 400 requests, no pushback, 158 new names, 9 keys on baseline names all in the run's appended list, 0 V2-held names touched, no key outside the never-widen table (`deliverables/2.0.0_SA_COO~Q1/ROUND9_MANUAL_RUN_RECEIPT_20261015.md` @4416f20cec). The volume limit is the pacer's 400-request day, not the clock. CTO msg 6379 RULES one step, 400 to 600, then read the receipt's 429s, timeouts and empty bodies before any next step, holding at the last clean step on the first sign of pushback. Cell `DQ-t-71` (`0.9.0_WK_MDPF_DEMQUE~61`, worker, LOCAL, DIRECT-ACT, workstream PACERCAP, depends on DQ-t-66/67): `yahoo_pull.Pacer`'s default cap and the two quote constants that must agree with it (`extend_frontier.DAILY_CAP`, so the standing request cap reads 580; `inactive_request.DAILY_CAP`) become 600, with the tests that pin the old cap. The step is recorded in `LIMIT_STEP_DAYS.md` beside the Bloomberg steps, so each change is attributable on its own night.

**Round 9 amendment 31 (issuer, 2026-10-16 ~02:5xZ):** the second manual Yahoo run (the first on the 600 cap, 200 added requests) read clean on pushback (0 429s, 0 timeouts, factor 1.0) and on the store (72 keys on names in its own appended list, 15 new names, 0 active-set names touched), but spent 138 of its 200 requests on symbols the pacer already holds as `FAILED_EMPTY` (158 in all; real tickers of delisted or acquired securities). `Pacer.done` skips only an `OK` symbol, so the vendor is asked again on every run, and the extra cap bought 15 new names, not 200 requests of progress. Cell `DQ-t-72` (`0.9.0_WK_MDPF_DEMQUE~62`, worker, LOCAL, DIRECT-ACT, workstream EMPTYCOOL, depends on DQ-t-71): a symbol whose last outcome is `FAILED_EMPTY` within the last 7 days is skipped before the budget check, so it costs no request. A transient failure is `FAILED_REFUSED`, not `FAILED_EMPTY`, so it is not hidden by the cooldown. Issuer ruling inside this decomposition (no endpoint change, no key moves that run 2 did not, no identity rule touched).

**Round 9 amendment 32 (issuer, 2026-10-16 ~16:0xZ):** Andrew-direct ~15:5xZ (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261016_155xZ_BBG_DAILY_BUDGET_2_5M_AND_TERMINAL_AGENT_MAY_DOWNLOAD.md` @f50271705e): "yes this is much better policy ... definitely let it download it has to be able to download", and the CTO ruled the implementation (`ledger/CTO_RULING_BBG_DAILY_BUDGET_2_5M_IMPLEMENTATION_20261016.md`, msg 6824): dell1's half is ONE cell. Cell `DQ-t-73` (`0.9.0_WK_MDPF_DEMQUE~63`, worker, LOCAL, DIRECT-ACT, workstream BUDGET): the five surface budgets (A 350,000, B 1,500,000, C 400,000, D 100,000, E 150,000 = 2,500,000), the E per-request cap of 5,000, the release rule (what A, C, D and E leave unused flows to B the same day; A is first claim), the unit-weight assumption (inferred) and the seven ramp steps become a `budgets` block in `bbg_allowance.json`, each figure with its claim; and every queued Bloomberg request carries a `surface` tag (A to E) by a new `surface_tag.py`, inserted as text so no other byte of a request moves. NOTHING SERVED MOVES in this cell: `history.ceiling` stays 5,858 and `bql.ceiling` 2,920,000 (the ceiling climbs only by the ramp's measured steps, one clean drawing day each, a round-10 act), no quote changes, no code the drawer reads changes. The drawer, the intake's E cap and the room per fire are site Z's half (`1.0.0_SA_CTO~Z`). Production-leg meter owners, carried in the block with claim `held`: A1 `2.0.0_SA_COO~D1` and A5 `2.0.0_SA_COO~H1` (ruled by the CTO, msg 6849: A5 is A2's sibling Positioning pull under the 2026-09-30 hold, A1 feeds the model data MDPF_CANON holds), A2 `2.0.0_SA_COO~H1`, A3 `2.0.0_SA_COO~RV`, A4 `2.0.0_SA_COO~R1` (the record); each meter is a daily count in the ledger, additive, never a change to a pull and never an alert. Issuer ruling inside this decomposition (no endpoint change, no served key, no identity rule).

**Round 9 amendment 33 (issuer, 2026-10-17 ~04:4xZ):** Andrew-direct 2026-10-16 ~15:5xZ named "round-10 cells DQ-t-69 and DQ-t-70" for the drawer's room per fire, and 2026-10-17 ~03:1xZ and ~03:4xZ ordered the rival funds 365-day backfill "done completely" through DEMQUE with no limit change. The CTO ruled (`ledger/CTO_RULING_DRAWER_HONOURS_SURFACE_BUDGETS_20261017.md` @d4ad590946, `1.0.0_SA_CTO~DELL1`): the quote and the drawer read the surface budgets `DQ-t-73` wrote (a surface-tagged request draws against its surface's line, surface C 400,000 a day; an untagged request keeps the 5,858 history ceiling; the sum never exceeds the 2,500,000 daily total; the trading-day gate is untouched, so a trading-day fire still draws nothing), and the cells are cut now. The ids are the ruling's; they are cut inside the open round 9 because round 9's L10 waits on the 2026-10-17 fire of `TO-DQ-t34`. Cell `DQ-t-69` (`0.9.0_WK_MDPF_DEMQUE~64`, worker, LOCAL, DIRECT-ACT, workstream SURFROOM, depends on DQ-t-73): `bbg_quote.py` and `standing_drawer.py` read `budgets`, new actuals rows carry the surface, and `standing_drawer.py --room` prints the day's rooms. Cell `DQ-t-70` (`0.7.0_AE_CloudOps~ZQ`, CloudOps, WORLD, STAGED until `DQ-t-69` is on `CLOUD`, depends on DQ-t-69): site Z runs the merged code and the 2026-10-17 14:00Z fire is read (surface C past 5,858, at most 400,000). The superseded design `deliverables/2.0.0_SA_COO~Q1/TRADING_DAY_DRAW_DESIGN_20261015.md` (trading-day draws) is not what these ids now mean: the CTO's ruling keeps the trading-day gate. After the fire the issuer re-quotes the open surface-C requests. Issuer ruling inside this decomposition, on the CTO's ruling; no endpoint change, no limit value changes.

**Round 9 amendment 34 (issuer, 2026-10-17 ~04:3xZ):** Andrew-direct ~04:2xZ (`org/tier1_exec/2.0.0_SA_COO~Q1/deliverables/ANDREW_DIRECT_20261017_042xZ_RIVALFUNDS_ALL_COMPLETELY_FILLED.md` @1438d1fb76): "Yeah I want all those completely filled", then "Now". The CTO ruled (msg 7279): tonight's fill goes by `2.0.0_SA_COO~RV`'s producer route through site Z (it lands on the page store; DEMQUE output in ZQ_STANDING does not), covering the 12,480 closes, `ETFS_RIVALS-C1-TR-HELD-D30/D90/D365` and `ETFS_RIVALS-C1-DIVIDENDS`. All of those requests carry a `draw_hold` so DEMQUE does not draw them a second time. CARRIED TO ROUND 10 (no cell cut now): an ETFS_RIVALS landing cell, so a DEMQUE draw of a rival funds request reaches the page store. `DQ-t-69` and `DQ-t-70` proceed unchanged: surface-tagged draws of every other surface honour the budgets. Issuer ruling inside this decomposition, on the CTO's ruling.
