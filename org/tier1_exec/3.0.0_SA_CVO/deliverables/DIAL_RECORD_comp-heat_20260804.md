# DIAL RECORD — comp-heat — CLOSE, P8 routed (the Kimi meta-analysis instrument dial)

**Dialer/Verifier:** 3.0.0_SA_CVO · **Date:** 2026-08-04 ~1945–2015Z (Andrew-present; his word
opened the dial and re-sequenced the Kimi Phase-0 sitting to GATE on it — this dial is
CRITICAL PATH for the vertical). **Consumer anchor (P1):** the Kimi v3 Friction battery
(design ruling: BATTERY WRAPS, instruments stay generic; trajectory = report-as-persistence).
**Method:** DIALED_TOOL_FLOW_DESIGN_20260731.md. **Baselines:** `dial_baselines/comp-heat_P0_20260804.txt` @1f0c44b06.

## VERDICT: DIALED-PENDING-P8 — consumable as-is by the ruled battery design; gaps are declarative

| Phase | Verdict | Evidence (exercised) |
|---|---|---|
| P0 | PASS | Units: `.tools/comp-heat` (self-contained wrapper) -> engine org/modules/heatmap/ (heat_map.py S0 + object_freshness.py O1); 4 modes. Baselines Q1–Q5 rc-direct: freshness bands w/ denominators (404 files: 51/185/168), drift live (193 rows incl. the just-written baseline file at 0.00d — self-inclusion proven), score deterministic golden (45d@30d -> 0.3536 COLD), JSON valid {scope, half_life_days, summary, paths, cold_subtrees} |
| P1 | PASS | Shim docstring RICH (purpose, ADVISORY-ONLY/read-only, distinct-from-comp-freshness, composition note); tools_index `does:` matches. Consumer anchor now explicit (battery F-figures) |
| P2 | PASS (CH-4) | Single name; the freshness/heat name-pair is disambiguated comp-heat-side; the claimed RECIPROCAL link is stale (below) |
| P3 | GAP = CH-0, CH-2 | NO output contract (pending tail — and the battery's wrap layer builds against exactly this contract, so it jumps the backfill queue); `federated` mode LIVE but undeclared in tools_index subcommands [freshness, drift, score] |
| P4 | PASS (CH-3) | hot/warm/cold band vocab shared with comp-pulse's vital-signs; `--json` consistent; no `--head` (adopt-as-touched). CH-3 semantics gap below |
| P5 | PASS (data) | Named in: manifest rows (2 entries), coverage-map (2 blocks, accurate), comp-describe/pulse does-lines, and NOW the State/Friction design (F-figures). No stale claims found beyond CH-4 |
| P6 | PASS (1 defer) | Boundary: age=0 -> recency 1.0 HOT; half-life discrimination on SCORE proven (0.3536 vs 0.7071); bogus path -> rc=0 WITH honest explanatory message (not silent-empty); DEFERRED-WITH-REASON: `federated` (Trino run-task transport; cost + SCTY-gated endpoint; convert on first battery need) |
| P7 | CENSUS, no deletions | Engine orbit LARGER than shim-declared: + object_locality.py, object_recommend.py (the O3 guardrailed recommends-to-delete leg — correctly NOT wired into this tool), object_report.py, heatmap_object_emitter.py, ms_heat_index.py + **ms_heat_index.json (3.1MB, GENERATED, UNTRACKED in-tree)**. ms-strand note: the ms_heat pair is adjacent to the audit's ms-cloud zero-coverage gap — possibly the seed of that coverage |
| P8 | OPEN — ROUTED | Non-dialer descent; route with next seat pick |

## Findings

- **CH-3 (MED — the consumer-relevant one): bands are FIXED AGE CUTOFFS (hot<=7d, warm<=30d),
  INDEPENDENT of `--half-life`** — confirmed at source (HeatParams.hot_days/warm_days; half_life
  drives recency_score only). Exercised: 45d reads COLD at BOTH 30d and 90d half-life while
  recency moves 0.3536 -> 0.7071. hot_days/warm_days are NOT CLI-exposed, so a caller reasonably
  assumes --half-life moves bands; it never does. A battery consuming BANDS must know this.
  Fix shape: declare the semantics in help + the contract; optionally expose --hot-days/--warm-days.
- **CH-0 (prioritization):** no output contract — elevated past the normal backfill order because
  the battery wrap layer builds against it; this record is the declare-by-exercise material.
- **CH-2 (LOW-MED):** `federated` live but unregistered in the subcommand declaration.
- **CH-4 (LOW):** the shim claims "both help texts cross-link"; comp-freshness --help contains
  ZERO comp-heat mentions (clean re-probe on a file). Half the pair is aspirational.
- **CH-1 (LOW):** bogus path -> rc=0 with an honest message — better than silent-empty; the rc
  question folds into the PRD's family miss-semantics ruling, not a per-tool fix.
- **CH-5 (LOW):** 3.1MB generated ms_heat_index.json untracked in the engine dir (it shows up in
  the tool's own drift output); P7 classification GENERATED, homing decision with the ms-strand.

## Method note

The tail-rc pipe class struck a THIRD time this session (my cross-link probe read head's rc and
manufactured a false "verified") — caught by clean re-probe before the record carried it. Three
strikes, three seats, all self-caught: the dial law (rc direct, display after) is earning its place.

## DECLARED RE-DIAL TRIGGERS

1. Output-contract declaration landing (converts CH-0; verify against this record).
2. CH-3 semantics declaration/exposure landing.
3. **The battery integration landing** (the wrap layer consuming comp-heat --json — verify the
   consumed fields match this record's captured shape; the design's F-figure denominators are
   battery-layer artifacts by CTO~B's ruling).
4. comp-cochange landing (sibling battery instrument, shared seam — verify the pair's
   denominator conventions agree).
5. Engine change >~50 lines across heat_map.py / object_freshness.py; band-threshold change.
6. `federated` registration-or-retirement decision.
7. P8 descent completion.

— 3.0.0_SA_CVO

## CLUSTER VERIFY + FEDERATED EXERCISE -- dial closes ZERO SKIPS, 2026-08-05 ~0020Z

0.2.0_DS's four-item cluster verified by my own battery: **BASIS-IN-OUTPUT landed verbatim to
Andrew's ruling** (band <- age vs barriers + the score formula, every mode incl. per-row);
**COMPARE mode real** (verdict prints WITH its own rule inline; both sides' full basis;
per-window series w/ commits-per-side; zero-history rc=2 refusal -- the family rule on this
tool too); **CH-2 CLOSED** (compare + federated registered; contract entry at HEAD via the
@3293a0cda sweep, true author 0.2.0_DS per COO's attribution note -- the 26-declared gate count
already included it); **CH-0 CLOSED** (the no-contract finding dies with the entry).
**FEDERATED EXERCISED LIVE** (the P6 deferral converts): in-VPC Fargate -> Trino REST ->
CloudWatch round trip green, real join result (heat_band census over the federated universe:
cold=330 / warm=27 / hot=17, avg scores printing). UNIVERSE NOTE for the contract: the
federated view is MODULE-grain (374 modules via the module:-node join) vs the local modes'
22,889-file grain -- two universes, both now declared surfaces; the dual-vintage line
(graph-table + code_heat-parquet) remains the declared shape. **comp-heat: DIALED, all phases
closed, no skips, no armed residuals beyond the standing re-dial triggers.**
