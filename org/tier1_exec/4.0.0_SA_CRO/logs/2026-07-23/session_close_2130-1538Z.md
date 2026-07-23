# CRO Session — Cottonwood-into-MDPF: backfill mechanism campaign + the three-band design program

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (qt5 temporal adjudication), IMPLEMENT (design specs), COORDINATE (CVO/CTO/COO chains)

**Agent:** `4.0.0_SA_CRO` (Chief Research Officer) · **Window:** 2026-07-22 ~21:30Z → 2026-07-23 15:38Z
**Commits:** 12 (26f218a75 → 88a0204ad) · **MCP:** ~55 messages handled; significant below.

---

## What this session delivered

Four Andrew-direct/commissioned design deliverables for the Cottonwood-into-MDPF program, plus a full
vendor-probe campaign that produced a high-stakes verification verdict. The through-line: **each honesty call
got a control that can fail in BOTH directions, not just the convenient one** — which is what caught a false
TEMPORAL verdict and a wrong-axis suppression threshold before either shipped.

### 1. Daily-snapshot append spec (@26f218a75) — accepted as build TO 3F-G8b
`COTTONWOOD_DAILY_MODEL_SNAPSHOT_APPEND_SPEC`. Finding: gold `dim_model_portfolio` already computes per-model
daily count+value (read the 07-22 parquet: 9 rows, `assignment_date` × `value_date` in-band) but lands as
unqueryable `date=` partitions. Spec = append-only series (`dim_model_portfolio_daily` per CTO naming rule) +
one-object query surface, FAIL-LOUD identities per append, backfill-compatible keying. CTO accepted as 3F-G8b.

### 2. BD backfill-mechanism campaign (@88bba912b + 5 addenda) — VERDICT: CURRENT-STAMPED
`COTTONWOOD_BACKFILL_MECHANISM_CAMPAIGN`. Full BD-estate sweep → exactly one live path (qt5 allocations
past-window, account-strategy dim already selected). Andrew opened a vendor egress window; 0.6.2 ran a
read-only R0-R3 pairing pass (his mechanics, my adjudication). **Final verdict = CURRENT-STAMPED assignment,
grounded 3 ways** (0 real assignment changes across 778+ accts vs today; `createdAt` stable 22/22 across
partitions = real birth dates, so models appearing in pre-creation windows are the current-stamp artifact;
window-integrity IGNORED flag correct). The fabric (incl. 0.6.2's strong parsimony read) leaned TEMPORAL for
~1h on evidence that proved temporal EXISTENCE+VALUE, NOT temporal ASSIGNMENT — the direct-assignment test
caught the conflation. **No false TEMPORAL shipped, no PIT-assignment fabricated.** Two self-corrections on
the record: my 02:12Z HTTP 500 was a self-inflicted run-body bug (not a vendor failure); the freeze is
vendor late-materialization (recoverable), not a run break.

### 3. Interpolated-backfill design spec (@8272fa0ed → @708661904) — CVO-SIGNED, building
`COTTONWOOD_INTERPOLATED_BACKFILL_DESIGN`. Labeled interpolated model-AUM band over the ~05-28→07-21 gap:
value reconstructed backwards through the healthy transactions feed, fuzzy assignment overlay, terminal-model
aggregation. Went through full CVO tandem review; adopted the incumbent provenance vocabulary wholesale
(interop = the honesty), one pinned delta then held (CVO R-5). Computed the terminal-washout coefficients
(MEASURED, not asserted) — key finding: cosine does NOT predict washout, so confidence keys on washout.
CVO-signed @816d48cc9; built as 3F-BF1/BF2 under COO decomposition.

### 4. Backtest-projection design spec (@88a0204ad) — envelope FIRM, in CVO tandem
`COTTONWOOD_BACKTEST_PROJECTION_DESIGN`. THIRD provenance class `backtest_projection`: composition valued over
ETF price history for pre-creation dates (hypothetical, never actuals). Grounded gate surfaced: ETF prices are
NOT in-estate (market buckets = FRED macro only) → price source is a DECISION (holdings-derived/public/ycharts).
Andrew "go" confirmed the envelope firm; in CVO tandem review.

### Method rulings issued (my lane, awaiting CVO bless)
- **BF1 confidence cap (item-2):** substitution confidence keyed to terminal `washout(U,R)`, not flat 0.50;
  invariant = a substitution can't claim confidence above its terminal overlap.
- **BF1 forced-guess epsilon:** caught that BOTH proposed values (0.10, 0.50) were wrong-AXIS. 0.50 is the
  confidence CEILING of a legit weak match → over-suppresses real AUM. Correct metric = absolute match-quality
  vs the MEASURED known-real-member floor (valley of the distribution). COO accepted; serve HELD pending
  DS measure + CVO bless.

---

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-which` | ETF price source hunt | PARTIAL | near-tie, no clean route; fell back to direct search |
| `comp-grep` | `price` in data/ | PASS | surfaced the price-col ref; no ETF-price producer |
| safe-commit surface-check + risk-reflex | every commit (12) | PASS | all "no critical surface"; risk-reflex REFLEX CLEAN each |
| raw `aws s3` (rail-checked) | monolith silver/gold + market buckets + probe exports | PASS | structural inventories + verdict grounding; each carried `# rail-checked` |

**What worked:** the raw S3 reads (rail-checked) grounded every verdict on live artifacts — the createdAt
stability test, the qt5 window exports, the "ETF prices not in-estate" finding. **What failed:** comp-which
didn't route the price-source question (near-tie across comp-aws/pipescript). **Gap found:** none new; the
Rule-17 flag (silver dropped `createdAt`) is a data-model gap routed to CTO, not a tool gap.

## Files / artifacts (see commit messages for per-file detail)

- 4 briefs + 1 harness under `org/tier1_exec/4.0.0_SA_CRO/{briefs,scripts}/` (see @26f218a75, @88bba912b,
  @8272fa0ed, @88a0204ad; harness `cot_qt5_temporal_probe.py` @7f2291783).
- `RECON_REGISTER.md` + `briefs/README.md` index rows updated.
- Raw probe exports retained by 0.6.2 at `s3://opal-data-cot/code/bronze/probe_results/qt5_window_*.xlsx`.

## MCP — significant only

- **Andrew-direct (via CTO relay):** daily-snapshot ask; interpolated-backfill order; backtest-projection order.
- **Rulings received:** CTO R-1 (adopt incumbent vocabulary), CTO gate on future template-probe, CTO v1.21
  (my probe carries full temporal verdict), Andrew vendor-egress window ("get it done now").
- **Rulings/verdicts issued:** qt5 CURRENT-STAMPED (to CTO+COO+0.6.2); BF1 confidence-cap; BF1 epsilon.
- **CVO tandem:** interpolated spec signed; backtest spec + 2 BF1 method rulings in review.

## Blockers

**None.** All open items are in-lane at other agents (CVO tandem verdicts on backtest + 2 BF1 rulings; DS/DE
builds; CTO Global aggregator) — awaited-not-blocked. Vendor surface released by 0.6.2 after the sweep.

## Current State (handoff surface)

- **3F-G8b** (daily-snapshot append): accepted, DS building. Spec @26f218a75.
- **3F-BF1/BF2** (interpolated backfill): CVO-signed @816d48cc9, DS/DE building. Spec @708661904. TWO method
  rulings pending CVO bless: confidence-cap (min(margin, washout(U,R))) and forced-guess epsilon (measured at
  the known-real-member match-score valley). Serve HELD until both bless + DS re-emits + co-sign reconvenes;
  COO value-limb caught a ~$108M forced-guess cliff (pre-06-15 degenerate model set) — the epsilon fix.
- **Backtest projection** (third band): envelope firm, CVO tandem in progress. Spec @88a0204ad. Open DECISION
  at Andrew/CTO: ETF price source (holdings-derived ~06-08-floor / public pull / ycharts-egress) + visual
  continuity-vs-purity. Price source is the one real build gate.
- **qt5 arc closed:** CURRENT-STAMPED (no assignment backfill); interpolated is the only assignment path.
  qt5 value-leg refinement (real dated value to ~05-15) DECLINED by DS for v1 (available-not-taken). Recovery
  sweep landed 10 frozen daily dates as value-real/assignment-current-stamped/never-PIT (0.6.2/CTO).
- **Rule-17 flag** routed to CTO: silver dropped per-model `createdAt` (bronze `rebalancer_model_detail` only);
  `fact_model_roster.last_update` is the revaluation stamp, NOT creation — silver passthrough on next touch.

## Next Steps

- **[4.0.0_SA_CRO]** Hold for CVO tandem verdicts on the backtest spec + the 2 BF1 method rulings; fold each as
  a pinned R-5 delta on bless. Answer per-run divergences from DS on BF1/G8b.
- **[3.0.0_SA_CVO]** Backtest tandem review; bless BF1 confidence-cap + epsilon invariants.
- **[0.4.0_DS_ClientPlatform]** Measure the epsilon (real-member match-score valley), re-emit BF1; G8b build.
- **[Andrew/1.0.0_SA_CTO]** Backtest ETF price-source decision + visual call.
