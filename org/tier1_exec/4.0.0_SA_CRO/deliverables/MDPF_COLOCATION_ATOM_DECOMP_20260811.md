# MDPF COLOCATION -- the atom_decomp ground-truth run (opal-data-mdpf -> opal-data-assets)

**Author:** 4.0.0_SA_CRO · **2026-08-11, 0440-0520Z** · **archetype:** TRACE + VALIDATE
**Commission:** Andrew-direct via CTO, three framings folded (043735Z task · 044439Z ground-truth
sharpening · 043954Z pattern extraction) + the 045521Z canonical-form invariant.
**Run record (machine-readable, schema-validated):**
`workflows/atom_decomposition/runs/opal-data-mdpf-colocation/20260811T0440Z/` -- rectangle.c0 +
rectangle.final (16 entities x 8 fields; census: 118 MEASURED / 2 INFERRED / 1 UNMEASURED /
7 NOT_MEASURABLE) + run.json, all VALID against `ssot_establishment.schema.json`. Method vintage
@d5eda6112f. **Read-only run: nothing mutated, nothing dispatched, no serving surface touched.**

<a name="domain-bar"></a>**Domain bar (Rule 14b, declared before population):** expected variance =
key-level drift between records and live state (the estate is mid-MDPF_REMED; waves land nightly).
FINDING class = a dependency edge whose EXISTENCE or DIRECTION differs from the recorded belief, a
runtime path absent from the record, or a live serve whose chain is dark. Cosmetic re-spellings and
only-on-change mtime gaps are expected-variance, not findings.

---

## PART A1 -- THE LOAD-BEARING ANSWER (what actually depends on opal-data-mdpf, proven live)

**Removing the bucket today breaks, with consumer-side proof for each:**

1. **A client-facing serve chain, exercised 2026-08-10:** the cron feeder lambdas wrote
   `mdpf/feeds/model_aua_positions` + `model_composition` + `partner_held_etf` **tonight 03:30-03:31Z**
   (TUE-SAT cron); the smartx producers read those feeds (hardcoded bucket,
   `compute_account_distribution.py:66-67,117,165` + the deployed lambda copy) and wrote the
   **per-firm served bells** `opal-data-portal-v2/json/mdpf/{49financial,inflection}/account-distribution.json`
   at **2026-08-10T11:30:39Z**. Feed -> read -> serve, all three legs alive the same day.
2. **Both EC2 runtime legs' BOOT path:** `mdpf-daily-trigger` pulls `mdpf-daily-dispatch.sh` from
   `code/` (`lambda_function.py:49`) and the runner syncs `code/scripts/ --delete` before executing
   (dispatch.sh:131-159). No bucket, no chain -- main leg AND accrual leg.
3. **The accrual bridge's DATA dependency:** `build_portal_gold_accrual.py:110,136` reads
   `partner_roster.json` **from inside the code prefix** (config-in-code-store; runs daily 13:40Z,
   last 2026-08-10T13:41Z, 21 telemetry logs).
4. **The aggregate's feed reads:** `mdpf_aggregate_aua.py:65` FEEDER_BUCKET hardcode (writes the
   `gold/mdpf_revamp/_aggregate_aua` staging the floor consolidator then consumes -- see A3).
5. **The producers themselves:** wsb/wsd lambdas + three chain feeders PUT into the bucket
   (hardcoded literal + IAM-pinned; they fail, not degrade, on delete).
6. **The deploy plane:** `safe_deploy_core.py:103` maps mdpf -> this bucket; `pipeline_cli.py:228,2054`
   hardcodes its special `code/scripts/<layer>` layout; DS deploys land here (code/ written
   **tonight 03:00:57Z** by the remediation window).
7. **`generate_smartx_timeseries_and_metrics.py:86-88`** reads `model_aua_positions` + `non_model_aua`.

**NOT broken by removal (measured, so the cutover doesn't over-scope):** the FLAT global bell
`json/portfolios/account-distribution.json` (frozen at 2026-07-23T20:57Z; its write leg was
DISABLED by the CTO producer-conflict ruling that same day -- source `:411-427`); the platinum
publisher leg (reads assets-side gold, 08-10T13:50Z); the floor consolidator's own reads (assets
silver/gold + staging -- **it never reads opal-data-mdpf**).

## PART A2 -- BELIEVED vs ACTUAL (the delta table; full evidence per cell in rectangle.final.json)

| # | Believed (source of belief) | Actual (grounding) |
|---|---|---|
| 1 | "Good-as-retired / decommission" (kill-list RETIRE-WHOLE-CANDIDATE; Andrew's recorded remark) | **LOAD-BEARING LIVE**: 3 feeds written tonight; per-firm bells exercised 08-10; both EC2 legs boot from it; DS deploys into it (A1 above) |
| 2 | "TWO runtime paths produce mdpf gold" (task map) | **FOUR-plus schedules, and the two named are SERIES-COUPLED, not parallel**: consolidator's STAGING_PREFIX = `gold/mdpf_revamp` -- the thing the chain's aggregate writes (:83-87 vs :79-80). Third leg = accrual bridge (daily 13:40Z, 21 logs, absent from the map); fourth = platinum publisher (13:50Z); fifth = smartx bells (11:30Z) |
| 3 | "Runner last ran 2026-08-10T13:40Z" (map + comp-estate) | **CONFLATION**: 08-10T13:40Z was the ACCRUAL leg. The MAIN chain last ran **2026-08-06T13:01Z and FAILED** (Stage 3.5 explicit-deny AccessDenied + Stage 5 no-allow AccessDenied, from the runner's own traceback); logs/history/status.json all end 08-06 |
| 4 | "mdpf-daily-refresh-trigger ENABLED, event-driven" (map); "something writes pipeline-complete.json daily" (E2 census 07-31) | Rule ENABLED but its event source is **DEAD**: the INF sentinel last wrote **2026-07-31T14:56:49Z** (head-object). The designed trigger has been dark 11 days -- the E2 "daily" claim went false the day it was recorded. What fired the 08-06 run is UNTRACED (recorded, not asserted). **The chain has NO schedule floor -- the exact only-trigger-is-another-pipeline's-success defect CLAUDE.md names, measured live again** |
| 5 | "account-distribution.json = THE live portal bell" (memory + map, flat key) | **SPLIT**: per-firm 49financial + inflection LIVE (08-10T11:30Z); cottonwood + global FROZEN 07-23; the flat global key frozen 07-23 with its writer deliberately disabled the same day |
| 6 | "aggregate writes portal-v2 `platinum/mdpf/aggregate_aua_timeseries.json`" (comp-estate census) | **That key 404s live.** Aggregate writes assets-side `gold/mdpf_revamp/_aggregate_aua/{date}.json` (source :79-80 + staging listing, newest 08-10T13:00:59Z); real serving = portal-v2 `platinum/mdpf/{firm}/aggregate-aua-timeseries.json`, HYPHENATED, publisher-written 08-10T13:50Z (the per-layer spelling law) |
| 7 | "Pointers already moved into _code" | `portal/gold/mdpf/_code` holds **exactly 1 object** (the floor zip, 08-11T03:24Z). Deploy map, feeders, smartx readers, dispatch, and the whole data plane still point at opal-data-mdpf |
| 8 | "code/ is ~20 commits behind HEAD" (iam.tf:166 comment) | Divergence is real but BIDIRECTIONAL: assets_gold layer measures 2 MATCH / **1 STALE** (`build_dim_model_portfolio` -- upstream of the very `dim_model_portfolio` parquets the floor consolidator reads) / **4 not-in-tree** (deployed with NO repo source -- the reverse class). And code/ was written TONIGHT (03:00Z) by the remediation window. "Behind" points both ways per file |
| 9 | Chain = "feeder -> aggregate -> rollup" (map) | **7+ stages with failure semantics**: S0 token-gate, S0 bronze, WS-B/C/D.1/D.2 parallel, WS-E, LEG2-CUSTODY-GATE, 3.5 LEGACY-EMIT (IAM-severed), 4 aggregate, 5 OWNTS (IAM-severed), 6 REVAMP spine (dispatch.sh:205-391). Two stages attempt writes remediation IAM now denies -- stage semantics never updated to match the IAM intent |
| 10 | `non_model_aua` feeds smartx timeseries (implicit fresh) | Reads a feed **frozen since 08-06** (its writer is the dark main chain) -- silently stale input, no staleness tell at the consumer |

## PART A3 -- THE OPEN DECISION, ILLUMINATED (EC2 chain: legacy or unique?)

**The question dissolves under measurement: they are not alternatives.** The floor consolidator
reads `gold/mdpf_revamp/_aggregate_aua` STAGING (:87) -- which `mdpf_aggregate_aua.py` (a chain
stage) produces from the bucket's feeds. One pipeline, two runtimes, series-coupled. What is TRUE:

- **Uniquely produced by the chain (or its feeders) and consumed downstream:** `non_model_aua` +
  `etf_net_assets` + inflection feeds + bronze (consumed by aggregate + smartx timeseries);
  the aggregate staging itself (consumed by the floor); the accrual leg's gold writes.
- **Already IAM-severed (dead weight in the chain):** Stage 3.5 legacy emit + Stage 5 OWNTS.
- **Already superseded:** the flat bell write (disabled 07-23); the platinum flat key (moved).
- **Cutover consequence, stated for the owner, not ruled by me:** "kill the EC2 chain" is really
  FOUR separable acts -- (i) re-home the feeder writes, (ii) re-home the aggregate (W1a already
  staged its consumer-side repoint), (iii) re-home accrual's partner_roster + code sync, (iv) delete
  the IAM-severed stages that are already dead. The smartx read edge (client-facing) migrates with
  (i). Nothing here waits on the "legacy vs unique" fork -- it was a false fork.

## PART A4 -- THE FIVE-ATOM SCHEDULING READ (pack 01's first live use)

| leg | A1 write-card. | A2 date-label | A3 trigger | A4 re-delivery | A5 settle | composition verdict |
|---|---|---|---|---|---|---|
| cron lambdas -> feeds | single/day | content as-of (`as_of_date` col, DATA-verified) | cron 03:30Z TUE-SAT | consumers take newest partition | unmeasured | OK; A5 hole marked |
| main chain -> feeds/bronze | single/day | mixed (as-of cols; bronze run-date) | **sentinel event, source DEAD 07-31; no clock floor** | idempotent skips | >=2d (BD custody, measured upstream) | **VIOLATES law-2 (trigger cannot fire; nothing floors it)** |
| aggregate -> staging | single/day | run-date key `{date}.json` | ~13:00Z (W3 ruled clock; producer identity INFERRED) | version-guard, downgrade REFUSED (:1315) | n/a | OK -- the version guard is the estate's best A4 cell |
| floor -> portal/gold | only-on-change | data-as-of derived from content | cron 13:30Z | put-with-readback | n/a | OK |
| accrual -> portal/gold | daily | date grammar `{date}.json` | 13:40Z | overwrite | n/a | OK; config-read from code store flagged |
| publisher -> platinum | daily | as-of in manifest | 13:50Z | last-good re-serve | n/a | OK; hyphen-per-layer law holds |
| smartx -> per-firm bells | daily | latest-partition | ~11:30Z | overwrite | n/a | **ordering note: reads 03:30Z feeds same morning -- 8h slack, fine; but `non_model_aua` limb reads a 5-day-frozen input (law-4-adjacent, no tell)** |

## PART A5 -- DATA SHAPES (DATA-grounded: newest object per feed, pyarrow schema read)

- `model_aua_positions` (08-11, 7,230 rows): firm_id, partner_name, model_key, model_key_unmapped,
  cohort_class, account_id, household_id, as_of_date, model_value, custodian, source_pipeline, _ingested_at
- `model_composition` (08-11, 129 rows): firm_id, model_key, as_of_date, ticker, security_name,
  product_class, target_weight, actual_weight, is_opal_etf, source_pipeline, _ingested_at
- `partner_held_etf` (08-11, 4 rows): firm_id, ticker, as_of_date, rps_date_used, held_value,
  account_count, source_pipeline, _ingested_at
- `non_model_aua` (08-06, 1 row): firm_id, as_of_date, non_model_aua, partner_custody_total,
  model_aua_input, sma_aua_input, method, custody_scope, methodology_version, source_pipeline, _ingested_at
- `etf_net_assets` (08-06, 4 rows): ticker, as_of_date, net_assets, nav, shares_outstanding, source, _ingested_at
- Gold/serving artifact families: `portal/gold/mdpf/{scope}/{artifact-type}/{data-as-of}.json` +
  `_manifests/{data-as-of}/{process-ts}.json` (consolidator :18,30) · platinum per-firm
  `aggregate-aua-timeseries.json` + `aum-metrics.json` + `_manifests/` (hyphenated).
- Every feed carries `source_pipeline` + `_ingested_at` -- provenance columns already standard.

## PART B -- THE CANONICAL PER-PRODUCT PATTERN (structural atoms vs mdpf-specific)

**The target grammar already exists in live code** (`build_portal_gold_accrual.py:3`):
`s3://opal-data-assets/portal/{layer}/{product}/{scope}/{artifact-type}/{YYYY-MM-DD}.json` -- the
pattern extraction below generalizes what the truth shows working, parameterizing what diverges.

**STRUCTURAL atoms (recur per product -- these ARE the pattern):**
1. **One product root:** `opal-data-assets/portal/gold/{product}/` -- data plane, `{scope}/{artifact-type}/{data-as-of}`.
2. **`_code/`:** the product's deployed runtime artifacts. ONE deploy target; the DS deploy map
   points here; runners/lambdas pull from here. (mdpf today: 1 of ~50 artifacts moved.)
3. **`_manifests/`:** process manifests keyed `{data-as-of}/{process-ts}` -- the consolidator
   already writes this shape; it becomes law.
4. **A declared intermediate plane** (feeds/staging) INSIDE the product root (e.g. `_feeds/`,
   `_staging/`) -- mdpf's divergence: feeds live in a standalone bucket and staging lives at
   `gold/mdpf_revamp` OUTSIDE the root. Both are homeless atoms the pattern houses.
5. **ONE producer per served key** (the 07-23 producer-conflict ruling, generalized), **one runtime
   per leg**, and **a schedule floor on every leg** (an event accelerates, a clock floors -- delta
   row 4 is what its absence costs).
6. **Config data never lives in the code store** (partner_roster is the measured violation).
7. **Serving only via the platinum publisher** with the per-layer spelling law (underscore in gold,
   hyphen in platinum) kept explicit.
8. **THE ANDREW INVARIANT (045521Z + 045813Z correction, first-class): the per-product producer is
   a THIN ADAPTER -- endpoint -> raw -> silver(dedup/dtype) -> serve. RAW-FROM-ENDPOINT IS THE FIRM
   RULE; every served field traces to a raw endpoint field or a named calculated exception, and
   **the exception LIST is PROVISIONAL pending Andrew's ratified set** (CTO's own first enumeration
   was corrected within 30 minutes: NNA = net-new-assets, a FLOW, is DISTINCT from the non-fee-AUA
   residual, a BALANCE -- two calculated nodes, never one). A fat gold tier is a pattern
   VIOLATION.** Measured against mdpf: the feeder tier largely conforms (feeds carry near-raw
   vendor fields + provenance cols); the chain's derivation-heavy stages (OWNTS per-ticker
   ownership timeseries, the legacy emits) are exactly the over-derived residue -- and two of them
   are already IAM-dead. The invariant and the measured decay point the same direction. Candidate
   calculated exceptions THIS decomp measured (feed-level, for Andrew's list, not ruled here):
   `non_model_aua` (derived balance w/ methodology_version col) · aggregation rollups (the
   aggregate/consolidator sums) · `etf_net_assets` passthrough is raw-conforming.
9. **Provenance columns (`source_pipeline`, `_ingested_at`) on every intermediate** -- already
   uniform across all 5 feeds; keep as law.

**MDPF-SPECIFIC atoms (do NOT generalize):** the INF-sentinel convergence gate; BD settle-window
accommodation (A5>=2d); the partner-roster scope set; the 49F/SmartX vendor adapters; the accrual
bridge's derivation.

**ADVI cross-check (LIGHT SCAN, bounded -- not a decomp):** `portal/gold/` contains ONLY `mdpf/`
(measured) -- **advi has no product root at all**; its serving today rides per-FIRM gold trees
(bd/inf/cot) + advisor-scoped portal JSONs + its own runners (the 49F BD runner carries the same
code-pattern as mdpf's feeders but with `lag=1` ENV config vs mdpf's hardcodes -- ~A's matrix row
[U], unverified here). Same disease (scattered hardcoded deps, multiple runtimes, served bells,
no colocation), different anatomy (multi-firm x advisor-scope vs product-global). **The pattern
generalizes if two things parameterize: `{scope}` (firm for mdpf; firm x advisor for advi) and the
intermediate plane's fan-out (advi's per-advisor artifacts are orders of magnitude more keys).**
The structural atoms 1-9 transfer unchanged; nothing in the advi shape contradicts them. Verdict:
GENERALIZES-WITH-TWO-PARAMETERS -- proven to light-scan depth only, honestly marked.

## META-TEST -- how atom_decomp handled a real, messy, cross-cutting case

**Where it shone:**
1. **It caught its own sources lying -- the test's point.** Six of ten delta rows falsify RECORDS
   (census, registry, kill-list, memory, the task map itself), found because Rule 22a forced every
   actual_state cell onto live/telemetry/source grounding. The decomp did NOT re-serialize the
   contracts; the contracts appear only in believed_state cells.
2. **Boundary-visibility held (the pack-01 claim):** the decisive facts (series coupling via
   STAGING_PREFIX; the dead sentinel; the accrual leg's existence; the frozen-vs-live bell split)
   are all ATOM-BOUNDARY facts invisible inside any single stage.
3. **The method's own validator sharpened MY artifact twice:** it refused my malformed constraints
   block, then refused an UNMEASURED cell carrying a value (no-bare-values). Both were real
   nonconformances. A method whose instruments catch its operator is working.
4. **The scheduling axis pack earned its place on first live use:** the A1-A5 table (A4) localized
   the two real composition violations in minutes; A5's "unmeasured is a marked hole" phrasing is
   exactly what feed rows needed.
**Where it strained:**
5. **Single-seat focus vs the fan-out design:** Rule 14c's missioned fan-out + independent
   certification were OMITTED (boundary). Status=DRY, UNCERTIFIED -- the standing certifier (CVO)
   has not signed; per Rule 14e nothing here is certified truth until then.
6. **Instrument gaps surfaced mid-run:** `comp-pipescript deployed` rendered only 1 of mdpf's 6
   declared code layers (7 of 49 objects checked -- its own denominator went unstated);
   `comp-estate`'s served-key rows carried a 404 key and a conflated runner claim. Both routed as
   findings, neither trusted.
7. **The rectangle's field-grain strains on heterogeneous entities:** edges, paths, IAM states and
   beliefs share one 8-field contract; 7 NOT_MEASURABLE cells are the cost of rectangularity over a
   mixed entity set. Honest, but a per-kind field contract would fit better -- a method extension
   candidate, not implemented (Build Ladder rung 1).
8. **Telemetry was the sharpest instrument in the estate** (the runner's own AccessDenied traceback
   out-grounds any IAM simulation) -- the method should say so: prefer the failure log of the real
   principal over simulate-principal-policy where one exists.

## BOUNDARIES (recorded, not discovered later)

Single-seat, ~40 minutes, read-only. NOT done: CloudWatch reads for the 08-06 manual-fire mechanism
and the 13:00Z producer identity (both INFERRED/UNTRACED, marked); alarm/checker liveness
(mdpf-freshness-checker -- UNMEASURED, moratorium context noted); smartx DEPLOYED-bytes diff vs
repo (repo + lambda-copy read; deployed-bytes not pulled); the advi scan is LIGHT by commission;
per-firm feed partitions beyond 49financial not sampled; org/-record mentions (281 DOC-band hits)
deliberately out of the edge census. The estate is mid-remediation: cells carry as-of stamps and
tonight's atomic window (@9eff54d274 clock change) may move cadence cells by tomorrow.
