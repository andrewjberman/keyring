# MDPF legacy-route blast census — comp-blast(kuzu) exercised against the Addendum-C canon

**Author:** 3.0.0_SA_CVO · **Date:** 2026-08-04 ~01:1xZ · **Trigger:** Andrew-direct at the CVO
terminal ("try running comp-blast around mdpf aws resources and see if you see any bullshit legacy
routes that are non-opal-data-assets"). **Canon reference:** Andrew voice memo
`docs/references/MDPF_ARCH_CLEANUP_ANDREW_MEMO_20260803.md` (CTO-transcribed; PRD Addendum C):
vendors -> bronze/silver/gold inside `opal-data-assets` -> publisher Lambda ->
`opal-data-portal-v2/platinum/mdpf/` — *"the only structure feeding the Opal Portal Model
Portfolios page."* All findings OBSERVED (live primitive or live-fired evidence) unless flagged.
Instruments: comp-blast (kuzu universe, post-72753ea4f2), comp-kuzu, comp-trigger, live aws
(rail-checked APPLIED-plane reads). This census FEEDS MDPF_GLOBAL T1.A/T5 — register/evidence
only, no builds, no kills (T5 is gated on T1-T3 proven, memo-verbatim ordering).

## CANONICAL ROUTE — live and firing

- `opal-assets-mdpf-portal-publisher-daily` ENABLED cron(15 16 UTC) -> Lambda
  `opal-assets-mdpf-portal-publisher` -> `opal-data-portal-v2` (platinum). FIRED 6x in window,
  last datapoint 2026-08-02. ⚠ the expected 2026-08-03 16:15Z fire is not in the datapoints —
  consistent with the T2.A truncation/INF-failure diagnosis in flight; noted, not diagnosed here.

## LIVE NON-CANONICAL ROUTES (fired this week — the memo's "mayhem", still running)

1. **SmartX ingest outside the monolith:** `smartx-account-distribution-daily` ENABLED
   cron(30 11 UTC) -> Lambda `opal-smartx-ingestion-pipeline` (Active, modified 07-24) — FIRED
   7x, last 2026-08-02. Its live env carries THREE disable flags
   (`DISABLE_PORTAL_AUM_TIMESERIES_WRITE=1`, `DISABLE_PORTAL_AUM_METRICS_WRITE=1`,
   `DISABLE_PORTAL_BELL_WRITE=1`) — **a half-decommission: portal writes turned off by flag while
   the schedule, compute, and remaining writes persist.** Graph ties its remaining write targets
   to `opal-data-mdpf`. (Flags OBSERVED; exact current write set INFERRED from graph edges —
   T1.A-owner to confirm from deployed code.)
2. **49F feeder pair into the legacy bucket:** Lambdas `wsb-49f-model-aua-daily` +
   `wsd-49f-partner-held-etf-daily` (both Active, 07-16) -> `opal-data-mdpf/mdpf/feeds/*` — live
   write evidence: `model_aua_positions/49financial/2026-08-01.parquet` landed 07-31 ~23:31 ET.
   CW alarm `wsb-49f-model-aua-daily-errors` rides the legacy leg.
3. **The INF-contingency chain (the memo's named anti-pattern, still wired):**
   `mdpf-daily-refresh-trigger` ENABLED, event-pattern on INF completion, NO schedule -> Lambda
   `mdpf-daily-trigger` (Active) -> EC2 `mdpf-daily-runner` (= i-02448edb624a7a7cf, currently
   stopped; start-run-stop; last chain run 07-31 with a LEGACY-EMIT step in its own telemetry) ->
   legacy emits + `gold/mdpf_revamp/*`. Chain did not run 08-03 (INF-gated + weekend).
4. **Accrual twin-plane:** SCHEDULE `mdpf-accrual-bridge-daily` -> Lambda `mdpf-accrual-trigger`
   — the hyphen-plane producer of the T2 twin-planes divergence.

## DEAD RESIDUE (exists but refers to nothing, or should not exist)

5. **Dead grants for the phantom freshness family:** Lambda + rule + alarm ABSENT live (T1.A,
   positive-controlled) — but `mdpf-freshness-checker-lambda-role` EXISTS live (created
   2026-06-02) with `mdpf-freshness-checker-scoped` policy in the graph. Role-without-function.
6. **Shadow-monolith write-target residue inside the legacy bucket:** graph S3Keys
   `opal-data-mdpf/platinum/mdpf/aggregate_aua_timeseries.json`, `gold/eclipse/{*}/...parquet`,
   `silver/eclipse/{*}/...parquet`, `silver/netassets_daily.parquet` — **objects DO NOT exist
   live** (bucket top-level: bmkaud-evidence/ cache/ code/ mdpf/ telemetry/ only). A
   silver/gold/platinum layering declared INSIDE the bucket that "should not even exist" —
   route-confusion residue with live writer code behind it.
7. Legacy-chain accessories: SSM document `mdpf-legacy-emit-on-demand`; CW alarms
   `mdpf-daily-stage5-ownts-failed` + `mdpf-daily-trigger-dlq-not-empty`; SQS
   `mdpf-daily-trigger-dlq`; runner SG/instance-profile/roles. All kuzu-live nodes.

## Instrument note (dial-session evidence)

The pre-rebase comp-blast could not have produced this census — `opal-data-mdpf` was NOT-FOUND in
its universe. Post-rebase, one blast call surfaced the full caller chain (29 callers incl. the
three live Lambdas + rule + alarm at depth 2). `--compare opal-data-mdpf opal-data-assets`
answered honestly: NO-OVERLAP-POSSIBLE (bucket-grain has no extracted downstream consumers) — a
correct refusal, not a similarity fabrication; key-grain comparison is the follow-on shape.

— 3.0.0_SA_CVO
