# NFRA_GCONTR TO-3 — graph_contracts rows (SEV1+SEV2 v1 ceiling) + period_defs value-check

**Author:** 3.0.0_SA_CVO · **Date:** 2026-06-26 · **TO:** NFRA_GCONTR.TO-3
**GO:** COO 2026-06-26 (195310Z; TO-2 table-exists gate cleared) · **Schema:** PRD §3 (RATIFIED)
**Status:** AUTHORED-STAGED — 5 rows at their correct PENDING-* ratified_at; 2 ratify-asks routed.

## Phase-1 mandate (comp-surface-check list) — PASS, 0 drift
Scope ceiling confirmed exactly = SEV1 {model_portfolios.headline, model_portfolios.benchmark,
advisor_intelligence} + SEV2 {model_portfolios.peers, model_portfolios.aum}. Authored exactly
this set, nothing beyond (§9 ceiling).

## Grounding note (Rule 22)
Each `canonical_writer` / `canonical_producer` / `artifact_keys` is a FACTUAL claim grounded via
`pipescript <thread>` + the producer source. Where the exact IAM role-STRING is not yet pinned
(headline/aum/advisor_intelligence), the PRODUCER is grounded and the role-string is marked
`GROUND-CONFIRM-AT-RATIFY` — NOT invented. The exact principal is confirmed by AE's live Q2
writer-edge JOIN at in-VPC `--load-contracts` (post-signoff). All 5 rows are STAGED (unratified)
per the §3 `ratified_at` PENDING-* invariant, so the load-gate skips them until sign-off.

---

## SEV1 rows (ratified_by=[Andrew], STAGED at PENDING-ANDREW-SIGNOFF — §9 SEV1-FIRST)

### 1. benchmark-model-portfolios (the SEED / keystone — joint acceptance with TO-2 Q2)
```yaml
- contract_id: benchmark-model-portfolios
  surface: "critical-surfaces:model_portfolios.benchmark (SEV1) | pipescript:model-portfolios/yang-benchmarks-etf-returns"
  artifact_keys:
    - s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json
    - s3://opal-data-portal-v2/json/benchmarks/benchmark_returns.json
    - s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json
    - s3://opal-data-portal-v2/json/benchmarks/etf_returns.json
  canonical_writer: yang-pipeline-lambda-role           # GROUNDED (pipescript + seed + IAM Deny b1a3543c9)
  canonical_producer: "yang-model-portfolio-benchmarks (ProcessBothPKLs branch)"   # GROUNDED pipescript
  source_of_truth: "s3://opal-data-portal-v2/benchmarks/data_YYYYMMDD_v1.pkl  # Yang PKL (BMKAUD WS-1)"
  period_defs:
    "1D": "prior-trading-day -> as-of"
    "WTD": "week-start(Mon) -> as-of"
    "MTD": "month-start -> as-of  (PARTIAL current month)"
    "1M": "trailing-1-calendar-month -> as-of"          # NOT last-complete-calendar-month = the SmartX violation
    "1Q": "trailing-3-calendar-months -> as-of"
    "YTD": "year-start -> as-of"
    "1Y": "trailing-365-CALENDAR-days, TOTAL return (incl dividends)"   # feca94a1f
    "3Y": "trailing-3Y, annualized"
    "SI": "since-inception, annualized"
    "_rfr_tenor": "duration-matched per model: UST/ST=1Y, INT=5Y, LTC/LTA=10Y (2c18f0c06)"
    "_return_basis": "TOTAL return (dividends included) + calendar-day arithmetic"
  models: [UST, ST, INT, LTC, LTA]
  forbidden_writers:
    - smartx-model-monthly-pull        # ROOT CAUSE: 1M=last-complete-calendar-month != contract
    - opal-generate-benchmark-returns  # EC2 smartx-exporter dormant dual-writer
    - smartx-ingestion-role            # latent writer (BMKAUD census)
    - news-pipeline-role               # latent writer (BMKAUD census)
  enforcement:
    iam_backstop: "DenyNonYangWriteBenchmarks on opal-data-portal-v2/json/benchmarks/* (b1a3543c9)"
    surface_gate: "comp-surface-check SEV1 (model_portfolios.benchmark)"
    value_check: "period_defs.1M trailing-1-calendar-month vs Yang PKL (codifies BMKAUD WS-2)"
  ratified_by: [Andrew]                # SEV1 tier (§9) -- RETIERED from the seed's [CTO,COO]
  ratified_at: PENDING-ANDREW-SIGNOFF
  active: true
  provenance: "BMKAUD 2026-06-01; revert 80224d674; Deny b1a3543c9"
```

### 2. headline-model-portfolios (MDPF aggregate AUA — the headline number)
```yaml
- contract_id: headline-model-portfolios
  surface: "critical-surfaces:model_portfolios.headline (SEV1) | pipescript:mdpf"
  artifact_keys:
    - s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json     # primary served rollup
    - s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json         # per-date partition
  canonical_writer: "GROUND-CONFIRM-AT-RATIFY: mdpf-daily-runner EC2 (i-02448edb624a7a7cf) instance-profile role"  # producer GROUNDED, role-string to pin
  canonical_producer: "mdpf_aggregate_aua.py on mdpf-daily-runner (PLATINUM_BUCKET); convergence-gated by mdpf-daily-trigger on INF spine pipeline-complete.json + BD silver freshness"  # GROUNDED pipescript mdpf
  source_of_truth: "per-partner model-AUA feeders: 49F WS-B (wsb_49f_smartx_model_aua), Inflection WS-C, WS-D2 ETF netassets, WS-E 49F non-model"
  period_defs:
    "_grain": "daily aggregate-AUA timeseries; convergence-gated (GATE_ENFORCE=1 defers on BD-stale)"
    "_as_of": "max common date across all converged feeders -> each feeder vs its own calendar"
  models: []                           # aggregate, not per-model
  forbidden_writers:
    - "GROUND-CONFIRM-AT-RATIFY: any non-mdpf-runner principal writing platinum/mdpf/* (CVO to curate the census from Q2 first-run)"
  enforcement:
    iam_backstop: "GROUND-CONFIRM: prefix Deny on opal-data-portal-v2/platinum/mdpf/* (confirm exists)"
    surface_gate: "comp-surface-check SEV1 (model_portfolios.headline)"
    value_check: "convergence-gate honored: served as_of <= min(feeder as_of); no single-feeder advance past the gate"
  ratified_by: [Andrew]
  ratified_at: PENDING-ANDREW-SIGNOFF
  active: true
  provenance: "pipescript mdpf 2026-06-26; aum.ts:444 source comment"
```

### 3. advisor-nna-canonical (advisor_intelligence — firm-scoped NNA)
```yaml
- contract_id: advisor-nna-canonical
  surface: "critical-surfaces:advisor_intelligence (SEV1) | pipescript:advi-{bd,inf,cot}"
  artifact_keys:
    - s3://opal-data-{firm}/platinum/firm/advisor_nna_canonical.json   # firm in {bd,inf,cot}; served via shared-advisor-router Lambda@Edge FIRM_BUCKET_MAP
  canonical_writer: "GROUND-CONFIRM-AT-RATIFY: inf-gold-layer-runner EC2 (i-0ed5afded2ebd4ed4) role + bd/cot gold-runner equivalents"  # producer GROUNDED, per-firm role-strings to pin
  canonical_producer: "INF_D_00f.advisor_nna_canonical.py (OUTPUT_KEY platinum/firm/advisor_nna_canonical.json) on the {firm}-gold-layer-runner; D_* publisher leg"  # GROUNDED source-read data/inf/scripts/gold/INF_D_00f.advisor_nna_canonical.py:78
  source_of_truth: "NNA from Orion bronze (orion-api/{date}) -> silver -> gold NNA; fee_map + acct_dim joined (build_advisor_nna_canonical:454)"
  period_defs:
    "_grain": "per-advisor NNA canonical snapshot, data_as_of pinned"
    "_firm_scoped": "STRICT firm separation -- opal-data-{firm} bucket; cross-firm read is an IAM-Deny violation, not a contract WATCH"
  models: []
  forbidden_writers:
    - "GROUND-CONFIRM-AT-RATIFY: any non-{firm}-gold-runner writing opal-data-{firm}/platinum/firm/advisor_nna_canonical.json"
  enforcement:
    iam_backstop: "firm-bucket separation (cross-firm WRITES structurally IAM-denied)"
    surface_gate: "comp-surface-check SEV1 (advisor_intelligence)"
    value_check: "NNA canonical present + data_as_of fresh per firm; no silent bd-fallback (the D_00f silent-no-write class B1)"
  ratified_by: [Andrew]
  ratified_at: PENDING-ANDREW-SIGNOFF
  active: true
  provenance: "pipescript advi-inf 2026-06-26; INF_D_00f.advisor_nna_canonical.py source-read"
```

---

## SEV2 rows (ratified_by=[CTO,COO], STAGED at PENDING-CTO-COO-SIGNOFF — no Andrew gate)

### 4. peers-model-portfolios
```yaml
- contract_id: peers-model-portfolios
  surface: "critical-surfaces:model_portfolios.peers (SEV2) | pipescript:model-portfolios/yang-peer-performance"
  artifact_keys:
    - s3://opal-data-portal-v2/json/peers/peer_performance.json
  canonical_writer: yang-pipeline-lambda-role           # GROUNDED (same Yang pipeline)
  canonical_producer: "yang-generate-peer-performance (peer_excel branch; runs only when a peer Excel is in the upload manifest)"  # GROUNDED pipescript
  source_of_truth: "peer Excel upload (manifest-gated) -> peer_performance computation"
  period_defs:
    "_cadence": "INTERMITTENT -- gated on peer Excel upload (LastMod 2026-05-31); NOT a daily guarantee"
    "_return_basis": "confirm vs the benchmark _return_basis at ratify (peer comparability)"
  models: [UST, ST, INT, LTC, LTA]
  forbidden_writers:
    - smartx-model-monthly-pull        # same SmartX override risk as benchmark (peer numbers are comparison-adjacent)
  enforcement:
    iam_backstop: "GROUND-CONFIRM: prefix Deny on json/peers/* (confirm)"
    surface_gate: "comp-surface-check SEV2 (model_portfolios.peers)"
    value_check: "peer period basis matches the benchmark contract basis (comparability invariant)"
  ratified_by: [1.0.0_SA_CTO, 2.0.0_SA_COO]
  ratified_at: PENDING-CTO-COO-SIGNOFF
  active: true
  provenance: "pipescript model-portfolios 2026-06-26"
```

### 5. aum-model-portfolios
```yaml
- contract_id: aum-model-portfolios
  surface: "critical-surfaces:model_portfolios.aum (SEV2) | pipescript:smartx"
  artifact_keys:
    - "DDB opal-portal-market-data (AUM tables) via opal-portal-data-proxy /aum/* endpoints"   # aum.ts 'SmartX Portfolio Data'
  canonical_writer: "GROUND-CONFIRM-AT-RATIFY: yang-ingest-dynamodb role (writes opal-portal-market-data from data_pkl) -- confirm vs a dedicated smartx AUM ingest"
  canonical_producer: "yang-ingest-dynamodb (IngestDynamoDB state, batch-writes opal-portal-market-data); served by opal-portal-data-proxy (opal-portal-lambda-role) /aum/*"  # GROUNDED pipescript
  source_of_truth: "SmartX AUM portfolio data (data_pkl ingest)"
  period_defs:
    "_grain": "AUM summary / flows (start_aum/end_aum/aum_change); confirm the flow-window definition at ratify"
    "_note": "SmartX is CANONICAL here (vs FORBIDDEN for benchmark) -- the asymmetry is real and intentional; AUM is SmartX's authoritative surface"
  models: []
  forbidden_writers:
    - "GROUND-CONFIRM-AT-RATIFY: any non-canonical writer into the AUM DDB tables"
  enforcement:
    iam_backstop: "DDB table resource policy (confirm)"
    surface_gate: "comp-surface-check SEV2 (model_portfolios.aum)"
    value_check: "aum_change == end_aum - start_aum (internal-consistency); flow-window matches period_defs"
  ratified_by: [1.0.0_SA_CTO, 2.0.0_SA_COO]
  ratified_at: PENDING-CTO-COO-SIGNOFF
  active: true
  provenance: "pipescript mdpf/smartx 2026-06-26; aum.ts header"
```

---

## The period_defs value-check assertion (CVO-owned, §9 — codified WS-2)
The value limb (PRD §3.3): run a served column against its `period_defs`, independent of writer.

```
ASSERTION period_defs_value_check(contract, served_artifact):
  FOR each (col, window_def) in contract.period_defs WHERE col is a real served column:
    observed_window = derive_window(served_artifact[col])    # compute the actual period the served value covers
    IF observed_window != window_def:
      EMIT VIOLATION{contract_id, col, expected: window_def, observed: observed_window}  # value-limb break, ANY writer
  # canonical instance (BMKAUD): benchmark."1M"
  #   expected = trailing-1-calendar-month; a served 1M computed as last-COMPLETE-calendar-month = VIOLATION
  #   -> fires EVEN IF the writer is canonical (the WS-2 catch the structure/policy limbs miss)
```
- **Fires on a non-trailing 1M** (the BMKAUD replay PRD §4): expected `trailing-1-calendar-month`,
  observed `last-complete-calendar-month` (SmartX math) → VIOLATION, independent of who wrote it.
- **v1 = ADVISORY** (§9): the value-check WARNS; it does not exit 2 until the CTO hard-block ramp.
- Homes the WS-2 benchmark-truth-audit logic as a standing assertion (vs a hand re-audit each touch).

## Acceptance posture + the two ratify-asks
- **AC (rows authored + CVO-attested + staged):** 5 rows, exactly the §9 ceiling, each at its correct
  PENDING-* state. SEV1 NOT self-ratified (held at PENDING-ANDREW-SIGNOFF).
- **AC (value-check encoded + fires on non-trailing 1M):** above, BMKAUD-replay-aligned.
- **BMKAUD end-to-end (joint with TO-2 Q2):** the benchmark row's forbidden_writers (smartx-model-monthly-pull)
  + TO-2's Q2 JOIN = the UNSANCTIONED catch; the period_defs.1M assertion = the value catch. Joint Phase-3 replay to run with AE on the benchmark row at ratify.
- **Residual (honest):** 3 canonical_writer role-STRINGS + 4 forbidden_writers censuses marked
  GROUND-CONFIRM-AT-RATIFY (producers grounded; exact IAM principal confirmed by AE's live Q2 at load).

RATIFY-ASKS (routed at delivery):
1. **SEV1 (benchmark/headline/advisor_nna_canonical) → Andrew, via COO** (CC MSTR; /govern picks up if Andrew silent a cycle).
2. **SEV2 (peers/aum) → CTO + COO** (parallel, no Andrew gate).

— 3.0.0_SA_CVO
