# T2-stale grounding + NFRA_PPLINF topology pre-read (COO GO 231420Z)

**archetype:** TRACE
**author:** 0.6.1_AE_PartnerETL
**date:** 2026-07-02
**status:** grounded; RAVC'd COO. Both LOW-urgency depth-drives while L7 nightly-gated.

## PART 1 -- T2-STALE grounding (Rule-22 mechanism)

**Question (COO):** is the historical-prices producer DEAD/stalled or intentionally-static?
Is T2 ever LIVE-READ? -> fix (producer-dead AND T2-reachable) vs document/decommission (vestigial).

### Producer = STALLED (not clean-disabled, not static)
- Producer: `historical-prices-fetcher` EC2 (EC2_MANIFEST:279), managed by
  `historical-prices-scheduler` Lambda; EventBridge `historical-prices-daily` cron(0 14)
  **State=ENABLED** (LIVE). Writes ONE consolidated key `silver/historical_prices.parquet`
  (backfill_yahoo_prices.py:47,238; resumable, NOT dated-partitioned).
- ARTIFACT FROZEN 05-05: `aws s3 ls silver/` = only `historical_prices.parquet` @ 2026-05-05
  09:58:55 (29.8MB). No fresh/dated key.
- YET THE FETCHER KEPT LAUNCHING: last visible launches 2026-06-01 / 05-26 / 05-25 (all
  14:00:47Z = the cron firing). => the fetcher LAUNCHES but FAILS TO WRITE since 05-05 -- a
  STALLED producer (ENABLED + firing + burning EC2, producing nothing since 05-05), not a clean
  decommission and not intentionally-static. (No launch visible after 06-01 -- records aged out
  or launches stopped; artifact ground-truth = frozen 05-05.)

### T2 IS live-read, but current-impact = NIL
- INF_S_00 (INF_build_canonical_prices.py) READS T2 every run: `load_historical_prices()` L368
  -> merged into the price spine L394 -> `t2_price` fills gaps. So T2 is live-reachable code-wise.
- BUT a 05-05-frozen file has NO rows for post-05-05 dates -> the spine merge finds no t2_price
  for June/July -> **T2 contributes NOTHING to CURRENT-date canonical prices**. Current pricing
  (the served AUA surfaces) rides T1 (transaction_observed, primary) + T4 (carry_forward).
  Historical-date canonical (through 05-05) still uses T2 correctly.

### VERDICT: real freshness GAP, LOW severity
producer-STALLED AND T2 live-read -> per COO's framework a freshness gap to fix. BUT current
AUA/served pricing UNAFFECTED (T1+T4 cover); only recent-date (post-05-05) T1-sparse tickers lose
the T2 backstop -> fall to T4 carry-forward (bounded quality degrade). Plus a minor cost /
false-liveness issue (ENABLED scheduler launches a failing fetch ~daily). Root-cause of the
write-stall is NOT yet source-confirmed (needs the fetcher TELEMETRY_KEY + CloudWatch logs --
fix-phase; Rule 22a: I assert the symptom [frozen 05-05 despite launches], not the mechanism).

**RECOMMENDATION (COO/CTO prioritize, low-urgency, NFRA_PPLINF/comp-debt class):** FIX (root-cause
the fetch/upload stall -> restore T2 as a live backstop; my lean -- a stalled-ENABLED producer is
worse than fixed-or-cleanly-decommissioned) OR DECOMMISSION (if T1+T4 deemed sufficient, disable
the scheduler + document T2 vestigial). Either beats the current ENABLED-but-dead state.

### ROOT-CAUSE (COO steer 000045Z; Rule 22a metric+telemetry confirmed)
The stall LOCUS is the EC2 fetch, and it is SILENT:
- SCHEDULER HEALTHY: historical-prices-scheduler Lambda Invocations=44/45d, Errors=0; EventBridge
  historical-prices-daily Invocations=44, FailedInvocations=0. Schedule + Lambda + EC2-start all fine.
- THE BREAK IS DOWNSTREAM IN THE EC2 FETCH: backfill_telemetry.json start_time frozen 2026-05-05
  (last run CLEAN: 3024 tickers / 27202 rows / 0 errors / no rate-limit). Post-05-05 the EC2
  (backfill_yahoo_prices.py) fails to write telemetry OR the artifact -> the failure is in the
  fetch, DOWNSTREAM of the healthy scheduler.
- SILENT: the scheduler is FIRE-AND-FORGET (start_instances, no completion check) -> the EC2 fetch
  failure surfaces NO error -> the ENABLED-but-dead false-liveness, burning EC2 daily. This is the
  SAME class as the L7 DLQ-graveyard: a fire-and-forget producer with no completion alarm.
- historical-prices-yfinance Lambda = 0 invocations (vestigial alternate path).
- EXACT EC2-fetch error NOT yet source-confirmed (Rule 22a: locus + silent-class grounded, precise
  library error needs the EC2 run-log -- not in the CW Lambda groups, both empty; probable cause =
  yfinance library/Yahoo-API breakage, a fragile external dep that broke clean-05-05 -> silent-fail).

DISPOSITION REC (mechanism-grounded): whatever the fix/decommise call, the REAL debt is the
silent-failure (no completion alarm on a fire-and-forget producer). If FIX (restore T2 backstop):
repair the yfinance fetch + ADD a freshness/completion alarm (mirror the L7 DLQ-alarm -- a stale
historical_prices.parquet must BLARE). If DECOMMISSION (T1+T4 sufficient): disable the scheduler,
stop the daily EC2 burn, document T2 vestigial. Either kills the ENABLED-but-dead + the
silent-freeze class. My lean: the current-impact is NIL so this is not urgent, but the
silent-fire-and-forget pattern is worth an alarm regardless of fix-vs-decommise.

## PART 2 -- NFRA_PPLINF topology pre-read (manifest pre-stage)

`pipescript advi-inf` (census 2026-06-15): 14 threads / 24 resources (lambdas+EC2). Full
inventory captured. L7 Stage-3 retire-set maps cleanly to threads:
- RETIRE (Stage-3, human-gated): `inf-bronze-api-pull` (9 REST-pull crons) + `inf-silver-aggregator-quorum`
  (the aggregator) + `inf-canonical-prices-daily` (a trigger in `inf-gold-dispatch-ec2`).
- STAYS: `inf-bronze-runner-ec2` (produces _BRONZE_COMPLETE my new trigger keys on), `inf-jwt-exporter`,
  `inf-silver-chain` (bronze/orion-api CSV -> silver dims), `inf-gold-dispatch-ec2` (my new trigger added here).

### CENSUS-STALENESS FINDINGS (Rule-22 reconciliation -- manifest MUST use LIVE source, not the 2026-06-15 census)
1. **Cron-time drift:** census shows 12:xx UTC (bronze-runner "43 12", reps "30 12", jwt "13 12");
   live TF (this session) shows 13:xx UTC (bronze-runner cron(30 13), reps cron(17 13), jwt cron(0 13)).
   Census predates a retiming -> stale by ~1h.
2. **inf-silver-chain sentinel claim FALSE:** census says inf-silver-chain "writes
   silver/_silver_complete/*.json sentinels." SOURCE-CONFIRMED FALSE: its only put_object writes
   `silver/api_dims/_chain_summary/{date}.json` (observability summary, lambda_function.py:219-225)
   -- a DIFFERENT prefix that does NOT trigger the aggregator (which listens on silver/_silver_complete/).
   => **VALIDATES my L7 Q-B PASS**: the silver/_silver_complete/ writers are EXACTLY the 9 crons +
   the aggregator's own _AGGREGATOR_FIRED marker; removing the 9 crons DOES make the aggregator
   writer-less (Stage-3 aggregator-decommission remains safe).
3. DEBT flag: `inf-client-detail` UNREVIEWED / needs-consumer-trace / deployed STUB (no API GW) --
   candidate manifest debt item.

**Manifest pre-stage:** 24-resource inventory + per-thread producer->served->frontend->reachability
captured. When NFRA_PPLINF un-stages (post-L7-Stage-2-GREEN, I lead), build the resource-SSOT from
LIVE source (TF+aws), and flag the advi-inf census for a refresh (2 stale claims found).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| pipescript advi-inf | topology pre-read (14 threads/24 resources) | PASS -- captured; surfaced 2 stale census claims |
| aws events/ec2/s3 (live) | producer liveness + artifact freshness (Rule 22a applied-layer) | PASS -- scheduler ENABLED, artifact frozen 05-05, fetcher launched thru 06-01 |
| grep/Read (source) | INF_S_00 T2 read + inf-silver-chain sentinel reconciliation | PASS -- census claim falsified vs source |

## Next
RAVC COO both. T2: await fix-vs-decommission steer (low-urgency). NFRA_PPLINF: manifest pre-staged,
finalize on un-stage (post-Stage-2-GREEN) from live source. Neither blocks the 07-03 L7 exercise.
