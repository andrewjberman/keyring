# /draw — MDPF ingestion, vendor → platinum, every scope, every trigger (Andrew-direct ~0357Z)
**Grounding:** T1.A trigger census @389c528ddb · clock v2 @5a20433a5c · OVP WS-1 registry @01ab614102 ·
T2.B ruling @440d16e018 · route censuses @b48634789a/@ea47d52931 · voice memo @7a585074e ·
cot LAG fix @bf4c0aabbe. Trigger vintages as of 2026-08-04 ~04:00Z; the T2.C apply (executing) adds
the FLOOR and migrates the publisher to ET.
**Andrew verbatim carried:** "track ingestion all the way from data vendor -> bronze all the way
through portal publisher to opal-data-portal-v2/platinum/mdpf, for every scope" + "we should be able
to categorically delete all unused routes. there is nothing that opal-data-mdpf and associated
resources should be doing that matters."

## PLANE 1 — THE BUILD: vendor → bronze → silver → gold → publisher → platinum

```
 VENDORS (per scope)                         TRIGGER NATURE (all times as cited)
 ══════════════════                          ══════════════════════════════════
 49FINANCIAL
  SmartX API (models/AUM/roster) ──────────  [CRON 09:30 ET  smartx-assets-daily-pull]
  Black Diamond xlsx (hold/alloc/fees) ────  [DAILY bd 49f monolith feeds, LAG=1 configured]
  Schwab RPS/SDD (custody) ────────────────  [CRON 12:15Z (08:15 ET) opal-assets-silver-schwab-sweep]
 INFLECTION
  Orion API x11 endpoints ─────────────────  [CRONs 09:32 / 09:37 ET  (post-07-01 shift, measured)]
  Eclipse API x4 (portfolios/models) ──────  [DAILY AM ET  (current-state class: run-date labels)]
 COTTONWOOD
  Black Diamond xlsx via cot_bronze_ingest   [NIGHTLY 02:00Z period tables; snapshot LAG=1 @bf4c0aabbe]
 ETF OVERLAY (feeds global rows)
  etfs netassets ──────────────────────────  [CRON 22:00Z  etfs-netassets-daily]  → netassets_daily.parquet
        │
        ▼  (raw, byte-for-byte; parquet FORBIDDEN at this layer — Rule 17a)
 ┌──────────────────────────────────────────────────────────────────────────────┐
 │ BRONZE   s3://opal-data-assets/…/bronze/          (as-of stamps per OVP law) │
 └──────────────────────────────────────────────────────────────────────────────┘
        │  silver converters (dedup + dtype ONLY — Rule 17)
        ▼
 ┌──────────────────────────────────────────────────────────────────────────────┐
 │ SILVER   fact_* COMPLETE tables  (fact_model_aum_daily · fact_holdings ·     │
 │          fact_allocations · fact_rps · …)   keys EXERCISED per T4.A          │
 └──────────────────────────────────────────────────────────────────────────────┘
        │  gold = THE ONE parse-down point
        ▼
 ┌──────────────────────────────────────────────────────────────────────────────┐
 │ GOLD     revamp dim_* projections (dim_mdpf_aggregate_aua_timeseries + the   │
 │          Stage-6 family incl. 6d cottonwood slice — 6c repaired @0f0f…-era)  │
 │   TRIGGERS:  ★ FLOOR [NEW, T2.C applying]: Scheduler CRON 11:00 ET DAILY     │
 │              incl. weekends → revamp rebuild  (NEVER#4 satisfied)            │
 │              INF event edge → ACCELERATOR-ONLY (demoted; never the floor)    │
 └──────────────────────────────────────────────────────────────────────────────┘
        │  accrual bridge
        ▼
 ┌──────────────────────────────────────────────────────────────────────────────┐
 │ ACCRUAL  mdpf-accrual-trigger  [Scheduler CRON 15:45Z → migrating to the ET  │
 │          clock: window 11:00–12:15 ET]  → portal/gold vintage                │
 └──────────────────────────────────────────────────────────────────────────────┘
        │  the Lambda publish (fired 3/3 daily incl. weekend, START-event proven)
        ▼
 ┌──────────────────────────────────────────────────────────────────────────────┐
 │ PUBLISH  opal-assets-mdpf-portal-publisher  [16:15Z → ET Scheduler per v2]   │
 │   →  s3://opal-data-portal-v2/platinum/mdpf/{scope}/     ◄ THE CANONICAL     │
 │       aggregate-aua-timeseries.json  · account-distribution.json ·           │
 │       aum-metrics.json (cottonwood LIVE; global/49f/inflection = the         │
 │       ELEVATED EMITTER build)             LOCATION — read ONLY from here     │
 └──────────────────────────────────────────────────────────────────────────────┘

 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  THE DYING BRANCH (categorical-delete target) ─ ─ ─ ─ ─ ─ ─
  INF spine sentinel (opal-data-inf gold/meta/pipeline-complete.json)
    └─[EVENT] mdpf-daily-refresh-trigger → mdpf-daily-trigger (+ freshness gate:
      ANDREW WORD PENDING terminate-vs-rebuild) → SSM → mdpf-daily-runner EC2
      → pulls opal-data-mdpf/code/ → feeders → opal-data-mdpf/mdpf/feeds/*.parquet
      → mdpf_aggregate_aua.py → underscore plane (displayed NEVER — F6; one-miss-measured)
  KILL GATES: ① feed-head repoint onto the opal-data-assets pattern (C1 family /
  memo production law) ② C2 ✓ landed ③ then opal-data-mdpf + routes delete whole
 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
```

## PLANE 2 — THE SERVE: platinum → browser (the voice-memo component map)

```
 Browser ──► CloudFront /api/general/mdpf/{scope}/{artifact}
                │ viewer-request:  auth-validator-edge v18
                │ origin-request:  public-data-router v6   [rewrite → /platinum/mdpf/ …
                │                  exercised on live traffic 08-01 + 08-03]
                │ origin-response: cache-control-injector v2
                ▼
        s3://opal-data-portal-v2/platinum/mdpf/{scope}/
                │
   ┌────────────┼──────────────────────────────┐
   ▼            ▼                              ▼
 aum-metrics  account-distribution  aggregate-aua-timeseries
   │            │                              │
   ▼            ▼                              ▼
 RADIAL +     BELL CURVE +           AUA TAB: monthly/quarterly
 metrics      juxtaposed container   stacked bars + daily area
 container    beneath it             charts
 (the whole   ("these two are        (per respective scope)
  group)       symmetrical")
```

## Analogy — farm to table

| Layer | Analogy | Trigger nature |
|---|---|---|
| Vendors | The farms | Their own harvest clocks |
| Bronze | Receiving dock — crates unopened, exactly as delivered | Delivery trucks on CRON schedules |
| Silver | Washed & sorted pantry (nothing thrown away, nothing seasoned) | Follows the truck |
| Gold | Mise en place — the ONE place prep decisions happen | ★ The 11:00 ET FLOOR (a shift that starts daily, whether or not the doorbell rang) |
| Accrual + Publisher | The kitchen pass — plated at 16:15Z sharp, every day incl. weekends | CRON, migrating to the ET clock |
| platinum/mdpf | The plated dish under the heat lamp — the only place waiters pick up | — |
| CloudFront/router | The waiter (rewrites your order to the right dish, checks your reservation) | Per request |
| The dying runner chain | An old side-kitchen that only cooked when the OTHER kitchen's bell rang | [EVENT] — the defect NEVER#4 names |

## Concrete end-to-end: cottonwood account-distribution.json (real stamps, this week)

BD xlsx lands (02:00Z nightly + snapshot at LAG=1) → bronze opal-data-assets → silver
fact_holdings/fact_allocations (dedup keys exercised, dup 0.0) → gold Stage-6d cottonwood slice
(starved 07-29→08-03 by the 6c defect, repaired 21:24Z) → accrual 15:45Z → publisher 16:15:31Z →
`platinum/mdpf/cottonwood/account-distribution.json` (_provenance.written_by = the publisher) →
router rewrite → the BELL CURVE + its container; footer stamp reads the artifact's own as-of —
which is why Andrew's screenshot said 07-29 while three sibling scopes said 07-31.

## The story

One spine lives: every vendor lands on its own cron into opal-data-assets bronze, flows
dedup-only through silver, parses down ONCE at gold, and is plated daily by the publisher into
platinum/mdpf — the canonical location the voice memo names, the only place the portal reads.
Everything event-coupled through opal-data-mdpf is the dying branch: displayed never (measured),
upstream-load-bearing only at the feeds-head, and categorically deletable the moment that head
repoints onto the same spine. The one build standing between today and the memo's end-state is
the aum-metrics emitter for three scopes — after which every component on the page reads exactly
one designed-for artifact, and every artifact rides exactly one clock.
