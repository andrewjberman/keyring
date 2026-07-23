# 0.4.0_DS_ClientPlatform — canonical-key pass SERVED + 3F-BF1 interpolator LANDED STAGED

**archetype:** BUILD
**secondary_archetypes:** VALIDATE, GUARD, SCRIBE

**Window:** 2026-07-23 ~03:51Z → ~04:22Z. Andrew-direct "I need both right now immediately"
(via CTO 035108Z + COO 035501Z; corroborated on the committed record @a41c582ba + @782ebd208 +
@6b2dc9cf7 before firing — tonight's verify-before-execute pattern, second exercise).

## Arc 1 — canonical-key pass (SERVED, dual co-sign)

- **Merge grounded before executing:** CTO's order said "the long_term archetypal key" + predicted
  "5 → 4-canonical" — ambiguous over two keys with $31M riding. Crosswalk pinned it
  (`mdpf_revamp_model_crosswalk.py:6` — opal_long_term_conservative == SmartX "Opal Conservative
  Growth"; `:92` served display "Long Term"). Flagged the count discrepancy instead of forcing it;
  **CTO retracted his 5→4 (his arithmetic error, 040015Z) and Andrew directly confirmed "Yeah
  there's 5 models" (via COO 040340Z).** Refuse-to-guess-against-the-record vindicated twice.
- **Executed** @`ab1f0074b`: CG → opal_long_term_conservative (display "Long Term"); Income
  harmonized OUT of the trend by_model into the named per-date residual ($1,242,005.29) via a
  routing constant SHARED slice↔pair; pending_canonical_ruling EMPTY; identities PASS pinned to
  tonight's partitions (07-22 × 07-20 per "same partitions").
- **SERVED** 0405Z on COO counter-sign 040340Z (independent verify: identities to the cent,
  count-axis 294-not-442, key set, ETags) + CTO pre-signed half: three ETags
  `1b283841dd19… / 55b1f1a48e00… / 3e555439135e…` pin-asserted + byte-compared. Ledger amendment
  @`867f128cb`. DE render-verifies "Long Term"/canonical-blue live.
- **04:00Z conditioned trend leg: pre-flight AXIS STALE (427 absent) → correctly did NOT fire**
  (COO's hard gate held); trend re-emitted with correct keys, honest-absent; dissolves into the
  6d dispatcher fix. Note: fact_holdings 07-21 landed (B5 delivery) — dim values-forward next build.

## Arc 2 — 3F-BF1 interpolated-backfill producer (STAGED, mutant-green)

@`65a8fa92f`: producer (lock 1) + **standalone validator (lock 2, imports nothing from the
producer — independence mutant-proven)** + CVO mutant set **11/11 GREEN before anything serves**.
Schema per CRO @`708661904` verbatim; per-firm carrier per the incumbent `:578` emit; enum
byte-exact; washout-keyed confidence (never cosine).

- **Floor:** CRO answered the routed ambiguity 041139Z — source = bronze `rebalancer_model_detail`
  `hierarchy[].createdAt` (stored attribute; **silver SLIMMED it — Rule-17 finding, CRO routing to
  CTO**). Floor = max(strategy_createdAt, account_first_existence); implemented sharper as
  date-restricted fuzzy candidate sets (a strategy can't be matched before it existed) + max()
  backstop; **DERIVED from bronze at run time** (ruling 9), guid-keyed (vendor names carry a typo +
  near-dupes). 175 live lock-1 refusals this run.
- **Run shape (anchor 07-22):** band 05-28→07-21; 34 custody-measured dates + 12 backwalk dates
  (flows-adjusted carry, no fabricated market_move — drift absorbed into label + lower confidence);
  3,240 account-dates ABSENT (holes degrade honest); zero §8.1 warnings. Staged artifact 67,120B
  listing-verified; **fact_holdings ETag byte-identical before/after (zero-bronze/silver-write
  exercised control).** Upgrade-ready: labels derive from run-time data — qt5 real data shrinks the
  band on re-run, no rebuild.
- **Held at the next gate:** serve waits on DE's BF2 accessor + the at-artifact co-sign pair.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep`/`comp-glob` | crosswalk long_term keys; cohort_provenance in mdpf | PASS | the $31M merge-target grounding + the incumbent carrier grounding |
| `.tools/commit-gate.sh` | slice+pair; BF1 trio ×2 | PASS (1 ruff fix, 1 test-crudeness fix) | |
| mutant set | 11 tests | **11/11 GREEN** | planted-point, both-enum-strings+case, two-lock, independence, V6 |
| dry-runs + upload runs | slice, pair (pinned + unpinned), interpolator ×2 | identities/gates PASS | the unpinned pair run surfaced value_date auto-advance to 07-21 → pinned per "same partitions" |
| `s3api head-object` | pins ×3, silver ETag control ×2 | PASS | pin-assert + untouched control |
| rail-checked `aws s3 ls` | partition/key enumeration ×4 | — | enumeration not freshness; markers logged |

## MCP traffic

CTO override 035108Z + 5-vs-4 flag→retraction 040015Z · COO BF1 GO 035501Z + counter-sign 040340Z +
BF1 report 042205Z · CRO floor ambiguity 040720Z → answer 041139Z · DE shape Qs → grounded answers
040127Z + republish ping 040535Z.

## Next

- **[DE]** BF2 accessor + guard test against the staged interpolated artifact; live render-verify.
- **[CTO+COO]** at-artifact co-sign when the interpolated series is ready to serve; 6d dispatcher leg.
- **[me]** comp-validate configs (pair + interpolator) + the 294/296 reconciliation note — named debt.

## POST-ARC TRIGGERS (banked 043xZ from 0.6.2's recovery circulation 043149Z)

1. **CENSUS RE-RUN (my S2 reconcile-trigger, now live):** recovered qt5/qt4 raw landed for
   07-09..07-22 (allocations ~1,500 rows/date; unrealized 67K-161K/date) -- silver converts on the
   normal 02:00Z cycle, so fact_allocations/fact_unrealized completeness denominators CHANGE after
   tomorrow's conversion. Re-run the affected census legs then.
2. **qt4 ROW-COUNT REGIME-SHIFT LENS (asked of DS explicitly):** 161.4K (07-09..13) -> 77.8K
   (07-14) -> ~67K (07-15..21) inside the recovered span. Determine column-shape vs dedup vs real
   book movement AFTER conversion lands; candidates = the 06-30 template re-persist (208 dims) +
   a vendor-side change. NOBODY reads the step as book movement before this lens runs.
3. **07-22 QUARANTINE (no live exposure):** both tables' 07-22 = likely mid-materialization
   partials (158/412 rows vs ~1,515/~67K neighbors), disposition at CTO. My producers consume
   NEITHER table (pair: model tables + holdings; interpolator: transactions + holdings + bronze
   model_detail) -- exposure checked, zero. Do not consume until resolved.
4. **VALUE-LEG SPEC INPUT:** raw probe exports for six historical windows (05-15..07-14) retained
   at opal-data-cot code/bronze/probe_results/ -- CRO holds the optional value-leg-to-05-15 spec;
   my re-run trigger stays armed for measured VALUE landings only (assignment permanently
   interpolated per the CURRENT-STAMPED verdict).

## GLOBAL AGGREGATOR BUILD DESIGN (banked 050xZ pre-implementation; Andrew-direct wire 050005Z)

Scope = the MEASURED Global fold (interpolated band rides its own gate). Producer =
`dim_mdpf_aggregate_aua_timeseries.py` `build_global_artifact` (:1172) gains the cottonwood leg,
read from the ALREADY-SERVING slice artifact (gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries
.json) -- no re-pull, no new ingest (COO wire binding).

**THE LOAD-BEARING FOLD RULE (structurally-absent vs gap):** cottonwood's series starts 07-21.
- date < cottonwood first covered date -> STRUCTURALLY ABSENT: global sum proceeds 49F+INF
  (history unchanged), provenance vector marks cottonwood: absent. Treating this as a GAP would
  null ~420 dates of global history; treating it as 0 fabricates (the $107.2M false-dip class).
- date >= first covered but value None -> REAL GAP: poisons the sum per the existing row-level
  null-coherence law. Discriminator = the slice's covered_dates/first_tracked_date meta.
**Additions per spec R-2 interim + DE contract (my 050149Z):** ADDITIVE flat point_class[] derived
any-cohort at Global (my derivation; DE reads never re-derives); cohort_provenance[] gains the
cottonwood slot; meta.partners_basis = per-firm basis map (49financial: schwab-rps / inflection:
eclipse+orion / cottonwood: bd-datamining-holdings) + fee_scope labels (sect-1.3: full-49F,
model-INF, model-COT) -- NEVER one blended basis string (0824/0833 law). by_model: cottonwood's 5
post-merge keys are ALL canonical (subset of GLOBAL_MODEL_KEYS) -- carrier-vs-gap logic extends
to the third leg, union count unchanged at 9. non_model: cottonwood slice carries honest-None ->
rides an audit-style field like inflection's 2b, NEVER the basis-B headline (which stays 49F-only
per Andrew's ruling). Headline identity UNCHANGED in form; cottonwood enters opal_aggregate only
on its covered dates.
**R-4 guards:** radial (dim_mdpf_aum_metrics) + bell-curve (dim_mdpf_account_distribution) each
gain the structural source != timeseries-tail assertion (current-snapshot inputs only).
Gates: staged-only, zero bronze/silver, ETag control, co-sign at artifact with DE's Global render.

## GLOBAL WIRE — BUILD SCOPE COMPLETE (051x-052xZ; serve rides the co-sign sequencing)

All four deliverables landed, each exercised: **fold** @745572fe4 (structurally-absent-vs-gap,
additive point_class[]/cohort_provenance[], partners_basis/fee_scope maps, cottonwood leg pin,
fixture-exercised 2 scenarios); **R-4 guards** @7c8320da4 (radial measured-frontier assert +
bell-curve snapshot-source assert, both ways); **FLAG-2 frontier preserve** @265e04607 (CTO ruling
051427Z: enumerated SMA keys + in-band count_as_of + non-enumerated-still-poisons, both ways;
unblocked the SMA seam I found + routed — live --firm all dry-run PASSES on the fresh 07-21
frontier: global model $1,548,108,403.71 / aggregate $1,825,641,501.51 / by_model{9}; COO
counter-sign requested at the artifact); **distribution fold** @fa491f9b6 (units SIDECAR from the
pair producer — one computation, two grains, no cross-tree import, no blended double-count;
global dry-run funded 7,863 / $1.672B / cottonwood inside the canonical keys).

**Also this window:** COO's co-sign pre-check caught the staged interpolated artifact PREDATING
the washout cap → re-emitted from the capped producer (67,146B, 05:19:42Z) — **the cap BITES on
the real blend: early band ~0.50 → 0.01–0.05 (18/46 dates distant-terminal substitutions),
preventing a ~50x confidence over-claim from being co-signed.** Staged pair/metrics ETags now
differ from served pins by generated_at only (values identical — NOT content drift; served
co-signed copies stand).

**Serve path (external gates):** CVO delta-sign → DE renders (band + Global view) → co-sign pairs
at the artifacts → serve. Backtest projection = separate dispatch (CRO design), not this lane yet.

## FLAG-2 CLOSE-OUT NOTES (053xZ)

- **Condition 5 converted to a CONTROL** @1e3999969: committed runnable
  tests/test_global_fold_flag2.py (5/5) -- both CTO cases + no-preserve-no-stamp + the fold's two
  absent-vs-gap laws. COO runs it to complete the counter-sign.
- **NAMED LIMITATION (COO obs, 053028Z): count_as_of is ENTRY-level** -- multiple interior SMA
  count gaps from different source dates would share one stamp. Fine for the trailing
  frontier-lag case that exists today (single-source by construction); if a MID-series SMA count
  gap ever appears, the stamp-granularity question re-opens as its own delta, never silently.

## GLOBAL SERVE ARC -- state at the Andrew-definition gate (135xZ)

**Band SERVED** (1202Z, ETag 3c3879c0, ledger amendment 2 @ea804ef26). **Global trio STAGED** with
all five CTO pre-sign conditions verified on bytes; COO fee-basis cell triply-grounded (their
phantom None-NB retracted -- read-key error, values present). **Serve then HARD-HELD on two gates
that both closed into ANDREW'S DEFINITION WORD:**
1. **Cottonwood basis (Andrew 134545Z)**: two-source overlay properly referenced -- landed
   @189336618 (basis string + structured meta.cottonwood_basis in pair/spine/radial + the standing
   COTTONWOOD_BASIS_METHODOLOGY record, grounded file:line). Carrier sweep denominator 10:
   5 under-stated artifacts enumerated; re-emits held to ride ONE churn with (2).
2. **49F leg ($43.8M) -- MECHANISM NAMED, ZERO RESIDUAL, ACCEPTED (COO 135503Z)**:
   $43,837,915.18 = $20,344,172.42 DEFINITION (full-envelope fact_rps_s2 vs legacy
   schwab_canonical partial-cash -- the D-2 named delta @6eb54c186; the $1.64B reference IS that
   legacy baseline, $1,644,993,954.34 @07-17 common) + $23,493,742.76 GENUINE GROWTH
   (07-17->07-21 day-by-day in the series) + $0 defect (D-3: model ties served; non_model
   identity-enforced). **The finding flipped the decision from which-NUMBER to which-DEFINITION**;
   options routed to Andrew (converged rec: he defines the business-logic subsection incl. the
   $33.76M cash-leg treatment; I build to it on real sources).
**Wave plan (CTO 134712Z)**: A = per-firm 49F+INF keys (P1-renderer + DE positional-shape evidence
gate); B = Global trend + radial + distribution + corrected cottonwood artifacts (basis delta-sign
+ renders + counter-signs). NEXT AT ME: Andrew's definition -> build the 49F subsection leg ->
re-emit everything in one churn (incl. the 5 basis carriers + NB-1) -> renders -> co-signs ->
publish per wave.
