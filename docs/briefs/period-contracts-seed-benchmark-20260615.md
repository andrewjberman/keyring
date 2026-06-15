# Period-Contracts seed — `graph_contracts` schema + the benchmark contract (worked example)

**Author:** 0.4.0_DS_ClientPlatform~A (Andrew-direct 2026-06-15, follow-on to closed NFRA_PIPESCRIPT)
**Status:** SEED / proposal — for CTO schema-ratify + AE Iceberg stand-up + CVO contract-authoring.
**Why:** the BMKAUD incident (Model Portfolios /performance tab, 1M column; 2026-06-01,
`docs/briefs/benchmark-yang-truth-audit-20260601.md`) was a SEMANTIC break — a SmartX override
replaced the canonical Yang-PKL benchmark numbers, and SmartX's `1M = last-complete-calendar-month`
differed from Yang's trailing 1M. Structure was fine (fresh, present, a valid float); no alarm
fired; Andrew caught it by eye, then a multi-day hand audit reconstructed who-writes-what.

A **period_contract** is the machine-readable invariant that would have caught it: it is both the
**reference frame** the Nessie/Iceberg version history is diffed against AND the **allow-list** the
diff is judged by. Versioning a graph without semantic anchors only tells you "stuff moved"; the
contract turns the snapshot diff into "what flipped, and of those which crossed a line nobody re-drew."

This is the machine encoding of the existing **never-widen** doctrine (CLAUDE.md NEVER: don't move
served output without CTO+COO sign-off) pushed down to the value layer: a benchmark source/period
flip IS a served-output-SEMANTICS movement; the ratified contract edit IS the sign-off, recorded.

---

## 1. `graph_contracts` — the versioned table (globgrph Nessie `main`, beside `graph_nodes`/`graph_edges`)

Co-located on the SAME Nessie branch as the graph it constrains, so every contract edit is an
attributable Nessie commit and the contract time-travels with the edges. Net-new table (no collision).

```sql
CREATE TABLE globgrph.graph_contracts (
  contract_id        STRING,                 -- identity, e.g. 'benchmark-model-portfolios'
  surface            STRING,                 -- constrained node: critical-surface id + pipescript thread
  artifact_keys      ARRAY<STRING>,          -- the served artifacts this contract governs
  canonical_writer   STRING,                 -- the ONLY IAM principal allowed to write them
  canonical_producer STRING,                 -- the producer lambda + DAG branch
  source_of_truth    STRING,                 -- the upstream canonical input
  period_defs        MAP<STRING,STRING>,     -- column -> window definition (the SEMANTIC contract)
  models             ARRAY<STRING>,
  forbidden_writers  ARRAY<STRING>,          -- known non-canonical principals (violation if observed)
  enforcement        STRUCT<iam_backstop:STRING, surface_gate:STRING, value_check:STRING>,
  ratified_by        ARRAY<STRING>,          -- the never-widen sign-off authorities
  ratified_at        STRING,                 -- the AUTHORIZING Nessie commit / date
  status             STRING                  -- active | superseded
) USING iceberg;
```

Iceberg snapshots + Nessie commits give the two queries below for free (`comp-aws diff --snapshot`
/ cross-snapshot `comp-kuzu` over the existing `cloud.diff.snapshot` surface).

---

## 2. The first contracted surface — the benchmark (worked seed)

Binds onto the existing SEV1 registry entry `model_portfolios.benchmark` (critical-surfaces.yaml:
"Benchmark Comparison panel + BenchmarkHeatmap (performance tab), ModelPortfolios.tsx ~L1857-1937,
activeTab=='performance'") and the pipescript thread `model-portfolios/yang-benchmarks-etf-returns`.

```yaml
- contract_id: benchmark-model-portfolios
  surface: "critical-surfaces:model_portfolios.benchmark (SEV1) | pipescript:model-portfolios/yang-benchmarks-etf-returns"
  artifact_keys:
    - s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json
    - s3://opal-data-portal-v2/json/benchmarks/benchmark_returns.json
    - s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json
    - s3://opal-data-portal-v2/json/benchmarks/etf_returns.json
  canonical_writer: yang-pipeline-lambda-role
  canonical_producer: "yang-model-portfolio-benchmarks (ProcessBothPKLs branch)"
  source_of_truth: "s3://opal-data-portal-v2/benchmarks/data_YYYYMMDD_v1.pkl  # Yang PKL (BMKAUD WS-1)"
  period_defs:
    "1D":  "prior-trading-day -> as-of"
    "WTD": "week-start(Mon) -> as-of"
    "MTD": "month-start -> as-of  (PARTIAL current month)"
    "1M":  "trailing-1-calendar-month -> as-of"   # NOT last-complete-calendar-month = the SmartX violation
    "1Q":  "trailing-3-calendar-months -> as-of"
    "YTD": "year-start -> as-of"
    "1Y":  "trailing-365-CALENDAR-days, TOTAL return (incl dividends)"   # feca94a1f: 365 not 252, total not price
    "3Y":  "trailing-3Y, annualized"
    "SI":  "since-inception, annualized"
    "_rfr_tenor":    "duration-matched per model: UST/ST=1Y, INT=5Y, LTC/LTA=10Y (2c18f0c06)"
    "_return_basis": "TOTAL return (dividends included) + calendar-day arithmetic"
  models: [UST, ST, INT, LTC, LTA]
  forbidden_writers:
    - smartx-model-monthly-pull        # the override source: 1M=last-complete-calendar-month != contract (ROOT CAUSE)
    - opal-generate-benchmark-returns  # EC2 smartx-exporter generate_benchmark_performance.py, own period-math (dormant dual-writer)
    - smartx-ingestion-role            # latent writer (BMKAUD writer census)
    - news-pipeline-role               # latent writer (BMKAUD writer census)
  enforcement:
    iam_backstop: "DenyNonYangWriteBenchmarks on opal-data-portal-v2/json/benchmarks/* (b1a3543c9)"
    surface_gate: "comp-surface-check SEV1 (model_portfolios.benchmark in critical-surfaces.yaml)"
    value_check:  "comp-validate / benchmark period-def test vs the Yang PKL (codifies BMKAUD WS-2)"
  ratified_by: [1.0.0_SA_CTO, 2.0.0_SA_COO]   # never-widen sign-off authorities
  ratified_at: "<the Nessie commit that lands this contract = the authorizing record>"
  status: active
  provenance: "BMKAUD 2026-06-01 (benchmark-yang-truth-audit-20260601.md); revert 80224d674; Deny b1a3543c9"
```

---

## 3. The two queries the versioning catalyzes

**Q1 - WHAT FLIPPED (snapshot diff, the raw motion):**
```
comp-aws diff --snapshot <baseline-pin>            # baseline = e.g. last Friday's Nessie pin
  over (graph_edges UNION graph_contracts)
  filtered to artifacts in any active contract.artifact_keys
-> the set of {writer-edges, contract rows} that CHANGED in the window.
```

**Q2 - WHICH SHOULDN'T HAVE (contract JOIN, the signal):**
```
for each contracted artifact A:
   observed = MATCH (w)-[:WRITES]->(:Artifact {key:A}) at HEAD          # who writes it now
   intruders = observed - {contract[A].canonical_writer}
   IF intruders == {}:                                  -> CLEAN
   ELIF a ratified graph_contracts edit re-declared canonical_writer in the window:
                                                        -> SANCTIONED (the never-widen sign-off)
   ELSE:                                                -> UNSANCTIONED FLIP, exit 2  (page)
```
The `ELSE` clause is the whole game: it separates **intended** ("we deliberately re-declared the
source, here's the ratified commit") from **regression** ("a writer appeared and nobody re-drew the
line"). A raw edge-diff can't make that call -- edges move every nightly redeploy. The contract is
the noise filter.

---

## 4. BMKAUD replayed against it

- **T0** - contract: `canonical_writer=yang-pipeline-lambda-role, 1M=trailing`. Graph: one WRITES edge (yang). CLEAN.
- **T1 (override lands)** - SmartX wiring adds a write-path into the benchmark artifact; Nessie HEAD advances. **No `graph_contracts` edit accompanies it.**
- **Next graph refresh / commit-time `comp-surface-check`** - Q1 surfaces `+smartx -> json/benchmarks`; Q2 marks it **UNSANCTIONED** (smartx is in `forbidden_writers`, not `canonical_writer`; no ratified contract edit) -> exit 2, **days before** Andrew eyeballs a wrong 1M.
- **The number itself** (SmartX-1M != Yang-1M) - caught by the OTHER limb of the SAME contract: `period_defs."1M" = trailing-1-calendar-month` is the assertion the `value_check` (codified WS-2) runs the served column against.

Structure (graph diff) + policy (contract JOIN) + value (period-def check) -- three limbs, one declaration.

---

## 5. The pipescript surface (DS lane, follow-on)

`pipescript` already reads per-thread `debtscan_flags` + `reachability_status` with strict
false-clean discipline; the contract slots in as one more authoritative field:
- `pipescript --contract <thread>` -> declared `canonical_writer` / `period_defs` / `ratified_by` + observed writer drift.
- `pipescript --flipped --since <snapshot>` -> each window flip tagged SANCTIONED / UNSANCTIONED(exit 2) / **uncontracted (LOUD `unreviewed`, never silently "fine")** -- the same false-clean rule, now on the value layer.

---

## 6. Rollout + ownership

1. **CTO** - ratify the `graph_contracts` schema + the never-widen-as-ratified-commit semantics.
2. **AE (globgrph lane)** - stand up the Iceberg table on Nessie `main` + the Q1/Q2 diff queries (`comp-aws diff` extension); wire Q2 into `comp-surface-check` so a SEV1 contracted-surface commit runs the contract JOIN.
3. **CVO** - author the contract rows, SEV1 set first: `model_portfolios.benchmark` (this seed), then AUM (`getAUMMetrics`/MDPF aggregate) + NNA (advisor_nna_canonical). One census, written down once as an enforced invariant -- vs re-audited by hand every time someone touches the tab.
4. **DS (this lane)** - wire `pipescript --contract` / `--flipped` to surface the field.

Finite, high-value list (the SEV1 critical surfaces). A flip is only as catchable as the surface is
contracted -- but that is exactly the census BMKAUD already did once, now durable.
