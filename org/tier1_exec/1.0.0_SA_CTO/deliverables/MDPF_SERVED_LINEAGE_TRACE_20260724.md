# MDPF Served-State Lineage Trace -- 2026-07-24 (Andrew-direct, during fabric pause)

**Author:** 1.0.0_SA_CTO. **Method:** comp-tools first (pipescript, comp-routes, comp-grep, comp-surface-check routing), every load-bearing hop then verified on the LIVE primitive (CF get-distribution-config, S3 list-object-versions, EventBridge full-pagination + EventBridge SCHEDULER, Lambda config/policy/logs, DDB query). Every claim below is MEASURED unless marked INFERRED.

## The five questions, answered

### 1. What artifact is the portal serving for Model Portfolios?

The ModelPortfolios page (`portal/src/pages/ModelPortfolios.tsx`, PROD == DEV on these paths, verified `origin/PROD`) reads ONLY static JSON. Path: CF behavior `/api/general/*` -> Lambda@Edge `public-data-router` rewrite `/api/general/*` -> `/json/*` -> **s3://opal-data-portal-v2**. LIVE distribution `EVTSA9VEHNZVH` verified: **no opal-data-assets origin exists; the monolith cutover has NOT happened.** Per-firm and global ARE separate artifacts:

| Element | Served key (opal-data-portal-v2) | Current bytes' vintage |
|---|---|---|
| Global AUA+count timeseries | `json/mdpf/global/aggregate-aua-timeseries.json` | 07-23T21:18:53Z (hand-staged) |
| Per-firm timeseries (x3) | `json/mdpf/{49financial,inflection,cottonwood}/aggregate-aua-timeseries.json` | 07-23T21:47Z (hand-staged) |
| Global bell curve | `json/portfolios/account-distribution.json` (NOT the mdpf/global sibling -- W-6 trap) | 07-23T20:57:18Z (hand-staged) |
| Per-firm bell (49F, INF) | `json/mdpf/{firmId}/account-distribution.json` | **07-24T11:30:39Z (live daily writer)** |
| Per-firm bell + metrics (COT) | `json/mdpf/cottonwood/{account-distribution,aum-metrics}.json` | 07-23T04:04Z -- **NO writer exists; 2 one-off versions ever** |
| Global AUM cards | `json/portfolios/aum-{metrics,timeseries}.json` | daily 11:30Z |

`platinum/mdpf/*` on the same bucket is the build tier (chain-written), not directly FE-consumed. COO's 07-23 byte-verified consumption map (`MDPF_SERVING_ARCHITECTURE_synthesis.md`) agrees with today's live inventory 1:1.

### 2. What writes it?

FOUR distinct writer signatures, from S3 version history + code + logs:

- **A. The MDPF daily chain** (event-driven): EC2 `mdpf-daily-runner` executing `s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh` -- Stages: S0 orion bronze pull; S1 feeders WS-B/WS-C/WS-D; S2 WS-E; S2.5 custody gate; S3 `mdpf_aggregate_aua.py` -> `platinum/mdpf/aggregate_aua/{date}.json`; S4 `build_aggregate_aua_timeseries.py` -> platinum rollup + **`json/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries.json`**; S5 OWNTS; S6 "revamp_stage" runs the DEPLOYED `dim_mdpf_*` scripts (vintage 07-21, **23 commits behind HEAD** -- CVO-corrected E3) and stages `gold/mdpf_revamp/*` on **opal-data-assets**. Last full run 07-18T15:01Z; write pattern 07-08/07-10/07-16x2/07-17/07-18 -- irregular, trigger-shaped.
- **B. Legacy smartx Lambda** (scheduled, LIVE): `opal-smartx-ingestion-pipeline` on EventBridge rule `smartx-account-distribution-daily` cron(30 11) ENABLED. Writes per-firm 49F+INF bells (today 11:30:39Z), global `aum-metrics`/`aum-timeseries`; its global-bell write is code-disabled (W-6 producer-conflict ruling 07-23; behaviorally exercised -- global key untouched today while per-firm wrote). Reads `opal-data-mdpf/mdpf/feeds/model_aua_positions/*` + DDB `opal-data-smartx`.
- **C. Manual stagings + the publisher**: the currently-served timeseries bytes are 07-23 hand-stages (`aws s3 cp`). `opal-assets-mdpf-portal-publisher` (LastModified 07-23T19:28Z) copies `gold/mdpf_revamp/*` -> `opal-data-assets/json/*` (the build-alongside serve): **it has NO resource policy -- no service can invoke it; manual-only by construction.** Its output is not served by CF (see #1).
- **D. Cottonwood per-firm bell/metrics: NO writer.** Two versions ever (07-23T01:33, 04:04). Frozen the moment nobody hand-runs `build_cottonwood_mdpf_pair.py`.

### 3. Schedules on the serving writer?

**The chain has NONE.** Sole trigger: S3 EventBridge `Object Created` on `opal-data-inf/gold/meta/pipeline-complete.json` -> rule `mdpf-daily-refresh-trigger` (EVENT-PATTERN, ENABLED) -> Lambda `mdpf-daily-trigger` -> freshness gate -> SSM -> runner EC2. Verified in BOTH classic EventBridge (141 rules, full pagination) AND EventBridge **Scheduler** (10 schedules -- a surface the earlier E1 sweeps missed entirely; no mdpf entry there either, so E1 holds on a wider denominator). The documented `mdpf-freshness-checker` + cron + alarm do NOT exist live (E2, CVO-confirmed).

**Today's live exhibit of the defect (all measured):** monolith `fact_rps_s2 date=2026-07-23` landed **10:16:05Z** (producer input fresh). INF marker fired **15:01:40Z**; the gate DEFERRED at 15:01:43Z because it reads a DIFFERENT object -- legacy `opal-data-bd/schwab/silver/rps/date=YYYYMMDD` -- which only rolled at **15:44:02Z**, 42 minutes late. One-shot trigger, no re-fire, no schedule => 5th consecutive missed day with every input fresh by 15:44Z. The gate's verdict is about an object the producers do not consume (the roster's `m1_the_legacy_gate_path`, live today).

### 4. Where does the writer get its data?

Deployed chain script reads (deployed bytes, not repo):
- WS-B: **SmartX vendor API directly** (api.smartxadvisory.com, Secrets Manager creds) -> writes `opal-data-mdpf/mdpf/feeds/model_aua_positions/49financial/`
- WS-C: `opal-data-inf` (INF gold) -> feeds `.../inflection/` (frozen 07-18, chain-only)
- WS-D.1: `opal-data-etfs`; WS-E: **`opal-data-bd` (legacy schwab tree)**
- WS-A/rollup: `opal-data-mdpf` feeds + `opal-data-portal-v2` platinum (self-referential carry)
- S6 revamp (dim_*): monolith `opal-data-assets` silver (fact_rps_s2 etc.) + SERVED-bucket reads (the two BLOCKING self-reads comp-dataflow found)
- Writer B additionally: `wsb-49f-model-aua-pull-daily` (Scheduler cron(30 3) TUE-SAT -> Lambda `wsb-49f-model-aua-daily`) independently refreshes the 49F feed (03:31Z writes 07-21/22/24; **07-23 partition missing -- unexplained anomaly**). Inflection feed has NO independent pull -> B republishes stale-input artifacts daily with fresh timestamps.

### 5. Ingestion lineage + every trigger on it

**INF chain (produces the marker that is MDPF's only trigger):** `opal-inf-jwt-fetch` cron(0 13); API pulls `inf-api-reps/accounts/assets-v2/unified-account-dim/positions/tax/txn` cron 13:17/13:22/13:27/13:32/13:37/13:42/13:47; `inf-billing` 14:22, `inf-performance` 14:27; EC2 bronze runner `opal-inf-bronze-runner-cron` cron(30 13); then event-chained: `inf-silver-chain-bronze-complete` (event) -> silver -> `inf-silver-aggregator` (S3 notif `silver/_silver_complete/`) -> gold (kill-switch `INF_GOLD_DISPATCH_RELEASE`, `inf-gold-dispatch-release-changed` event rule) -> writes `gold/meta/pipeline-complete.json` -> S3 notif -> `inf-portal-publisher` AND EventBridge -> mdpf. (`inf-gold-incremental-daily` cron + `inf-gold-full-on-bronze-complete` are DISABLED.)

**Monolith ingest (opal-data-assets -- the target architecture; ALREADY RUNNING):**
- Vendor pulls: smartx jwt/rest/assets (Scheduler crons 09:00/09:15/09:30); `opal-assets-bd49f-daily-pull` cron(30 2) + reattempt cron(30 4) + `opal-assets-bd49f-dim-convert` (Scheduler cron(5 3)); `opal-assets-ingest-mirror-inf-daily` cron(15 14); `opal-assets-ingest-mirror-cot-daily` cron(30 3); `etfs-netassets-daily` cron(0 22); canonical-schwab si2 pulls cron(15 10,22) + cron(45 9,21).
- **C1 bronze->silver: 8 LIVE S3-event configs** on opal-data-assets (blackdiamond/cottonwood .xlsx, eclipse/inflection .json, trueshares DIVZ+IDVZ .html, pathfinder .csv, orion .jsonl.gz, schwab 08242234+08335338 .zip) -> `opal-assets-silver-*` Lambdas, plus per-vendor daily sweep crons (05:00/12:15/16:00x3/23:30).
- Schwab head: OneDrive delivery -> **MANUAL** sync (AE-owned 49-schwab-conv) -> bronze .zip -> event-driven silver. The 10:16Z monolith RPS landing today was this path.
- **Gold DDB exists**: `opal-assets-daily-aua` (cohort-grain, value_class/vintage_state discipline), written by `opal-assets-daily-emitter` cron(15 17) ENABLED. **But today's run log shows it consumes the CHAIN's platinum partition** (`partition_key: platinum/mdpf/aggregate_aua/2026-07-18.json`, run_date 2026-07-18) -- the gold DDB is currently a PASSENGER of the frozen chain, not independently derived from monolith silver. Table also holds run_date 07-22 rows (14) from the 07-22 backfill wave; provenance of that stamp not established today.
- The per-channel as-of manifest instrument (CI-R9, 0.7.0~A) is built + exercised in-repo; NOT wired to any scheduled producer.

**Legacy bd tree (still read by the gate + WS-E):** nightly crons 21:38-23:00 (`bd-unrealized/transaction/realized/fees/allocation/asset-dim` pipeline triggers, `bd-silver-merge` on `_BRONZE_COMPLETE`, `bd-gold-nightly-fallback` cron(0 23)); today's legacy RPS roll landed 15:44:02Z.

## The architecture verdict (what confounds the goal)

1. **Two parallel serving stacks**: legacy portal-v2 (SERVED, written by a schedule-less chain + an 11:30Z legacy Lambda + hand-stages) and monolith opal-data-assets (populated, disciplined, NOT served -- publisher manual-only, CF cutover not landed).
2. **The only automated path to the served timeseries has no schedule and a mis-pointed gate** (reads legacy bd while producers read monolith): 5 missed days with fresh inputs.
3. **The freshest-looking served artifacts are the least-fresh data**: 11:30Z writer restamps 07-18-frozen inflection feed daily; cottonwood per-firm files have no writer at all.
4. **The deployed revamp producers are 23 commits behind HEAD** (51,999B vs 124,241B; CVO-corrected, my re-measure agrees), and at HEAD they write LOCAL-only (staging is the dispatch's job) -- nothing that runs on a trigger today builds what HEAD describes.
5. Monolith ingest (pulls + C1 events + silver sweeps + gold DDB emitter) is scheduled and live end-to-end -- the missing legs are: producer-input-aligned gate, a real schedule, the publisher trigger, DDB emitter independence from the chain, and the CF cutover.

## CVO validation fold (the pause exercise)

- E1/E2 CONFIRMED (CVO two-route; my Scheduler sweep adds the missing 10-schedule surface -- E1 unchanged). E3 CONFIRMED with CVO's corrections verified by me against the repo: HEAD 124,241B (not 119,499), 23 commits (not 20). E3 == the stale Cottonwood valuation Andrew asked about (one root cause, per CVO).
- I2 split per CVO: the 8 roster-declared MDPF feeds are grounded (all at adjusted lag 0 in my 196-feed re-sweep, denominator printed); non-roster feeds remain inference-classified. My original "83 feeds" sweep list was not persisted (scratchpad reaped); the re-sweep supersedes it with a broader denominator.
- Six instrument gaps (CVO list) share one property: none reports its own visibility boundary. Today's trace worked around all six by pairing each comp-tool with a live primitive.
- My retraction today: the emitter "4-minute race" hypothesis I briefly held -- WRONG on measurement (monolith RPS landed 10:16Z, emitter 17:15Z; the emitter's actual constraint is the chain's platinum frontier, from its own log).
