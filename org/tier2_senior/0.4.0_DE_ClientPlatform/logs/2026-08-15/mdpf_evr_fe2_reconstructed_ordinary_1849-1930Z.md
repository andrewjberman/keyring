# MDPF_EVR.FE-2 — `reconstructed` renders ORDINARY (Implementation B: own enum member, measured-identical pixels, label preserved) — 0.4.0_DE_ClientPlatform

**Date:** 2026-08-15 (session 1849Z–~1930Z)
**Task Order:** MDPF_EVR.FE-2 (`org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/MDPF_EVR.FE-2.render-reconstructed-as-ordinary.md` @78cb9b23e7)
**Status:** COMPLETE (both portal commits landed on DEV; proof-of-spec VALID rc=0; report to COO cc MSTR)
**Portal DEV commits:** `778ea780` (core Implementation B) → `e8b1fb07` (AC-8 per-firm flat `point_class[]` read, COO-ruled)
**Workspace CLOUD commit:** this log + the proof-of-spec instance (see Files Modified)
**Archetype:** feature-implementation, spec-proven

---

## Objective

Andrew-direct at the MSTR terminal 2026-08-15, VERBATIM: *"yes they should render as ordinary points"* (LD-0417; FE-1 cancelled @bc686bde7e). Make the 7 `reconstructed` MDPF inflection points render visually indistinguishable from measured points with no console warn, while `pointClass === 'reconstructed'` stays true in the paired-read output and the served data — Implementation B (own enum member + measured-identical styling), NOT Implementation A (mapping to `'measured'`, rejected by name). Portal main tree stays on DEV.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-to | `comp-to MDPF_EVR.FE-2.render-reconstructed-as-ordinary` | PASS | session TO_ID set (race-free per-session file) |
| comp-blast | `comp-blast pairedProvenanceRead` | WARN | NOT-FOUND in the canonical kuzu graph (denominator 20656 nodes) — an honest NOT-FOUND with its universe printed, not a "nothing breaks" clear; consumer census done by import grep (2 src files, 2 scripts). ~2 min runtime (auto full rebuild of the kuzu DB behind Nessie HEAD). |
| comp-find | `comp-find 'pointClass\|PointClass' portal/src` | PASS | DENOMINATOR: 37 hit(s) across 409 file(s) @HEAD; 44 @e8b1fb07 (2 files) |
| comp-transform schema-check | `comp-transform schema-check ModelPortfolios` | PASS | no MISSING; one [WARN] types-resolution (no co-located types.ts), advisory |
| comp-transform ternary-audit | `comp-transform ternary-audit ModelPortfolios` (+ `--var pointClass`, `--var PointClass`) | PASS | "All ternaries on union-typed variables are exhaustive" |
| provenance-read-guard | `node portal/scripts/provenance-read-guard.mjs` | PASS | OK: no unlabeled reads |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py …/MDPF_EVR.FE-2_PROOF_OF_SPEC.json AC-1,…,AC-8` | PASS | `structural=jsonschema \| acceptance rows=8 \| violations=0` VALID **rc=0** (positional id form) |
| /frontend-dev (ui-smoke) | `node scripts/ui-smoke.mjs portfolios <png> --port 5175 --select inflection --fixtures <served artifacts>` | PASS | REFAREAS 0 per-chart; PNG read (AC-6); PIL pixel-diff vs the core-B PNG as a control |
| /watcher | armed once at load | PASS | Monitor task b7cu473x9; delivered 4 COO messages during the session |

**What worked:** comp-transform (schema-check + ternary-audit) as the Rule-20 pre-commit pass; the bun exercise with `--module/--page` overrides made BEFORE / MUTANT / AFTER runs one command each; ui-smoke `--fixtures` fed the SERVED platinum artifacts so the local render was the real data.
**What failed:** comp-blast could not resolve a portal lib module by name (NOT-FOUND, honest); the first ui-smoke run without fixtures rendered an empty page (local dev has no backend) — fixtures required.
**Gap found:** no comp-tool answers "who consumes this TS module's exports" for portal libs (comp-blast is function/artifact-graph keyed); import grep filled it.

---

## Work Completed

### 1. Startup + GO
- /watcher armed (task b7cu473x9, no orphan, `/cygdrive/c` prefix); XXX.md protocol (serial file, A.2 audit-archive rc=1 lane-deferred, A.3 96/97 comp-tools + forwarder RAN, owned-paths hook present, agent_context set, B.1 to-check --all: 11 active TOs incl. FE-2 pending).
- COO GO 185230Z for FE-2 @04224a5435; ACK 185312Z; amendments received + adopted: AC-7 able-to-fail (@4d72e5a701), scope ruling (i) APPROVED + AC-8 (@ae6efb9cc8), AC-7 DISPLAY-ONLY vs VALUE-AFFECTING split with before/after numbers (@78cb9b23e7).

### 2. Grounding on the SERVED artifacts (`s3://opal-data-portal-v2/platinum/mdpf/{inflection,global,49financial,cottonwood}/aggregate-aua-timeseries.json`, publisher `written_at` 2026-08-15T13:50Z)
- **Premise correction (surfaced 190236Z, COO VERIFIED + ruled 190348Z):** the inflection `cohort_provenance` has 445 entries with **no `date` key** and SOURCE NAMES in the slots (`{custody:'Orion', model:'Eclipse'}` ×438; `model:'reconstructed(evr-1.0.0) -- eclipse/inflection/reconstructed/ (EVR)'` ×7) → `provenanceIndex` (`pairedProvenanceRead.ts:245-252` @684e67de) returns null → the ENTIRE per-firm read was predates-contract → all 445 points labelled `measured`, the 7 reconstructed included, via the fail-safe (a 4th collapse point, not `:294`). The class IS served on that slice: `point_class[]` = {measured 438, reconstructed 7}, `count_provenance` same, aligned to `dates[]`.
- Where `reconstructed` DID reach the reader as an unknown string: Global `point_class[]` (reconstructed ×2, plus `carried` ×5 — out of scope) → warn + estimate-class in the derived pointClass, no pixel at Global (07-23 materiality ruling empties `trendInterpolatedDates` at global); `count_provenance` (inflection 7, global 1) → `readCountTotalSeries` has ZERO consumers.

### 3. Core Implementation B — portal `778ea780` (DEV)
- `pairedProvenanceRead.ts`: `PointClass` gains `'reconstructed'` as its OWN member; `VALID` includes it; `resolvePointClass()` accepts the bare value and the producer's STRICT `reconstructed(` prefix form (the `carried_at_declared_cadence(...)` precedent) — everything else stays the LOUD degrade; `deriveAggregateClass()` = THE ONE precedence owner (interpolated > reconstructed > absent(all) > measured); `derivedFirmClass` routes through it (collapse #2 gone); `slotClass` / `readGlobalPointClass` / `readCountTotalSeries` carry the known member with no warn.
- `ModelPortfolios.tsx :727-746`: Global aggregate row passes `globalClassAt(i)` through verbatim, else `deriveAggregateClass` (collapse #3 gone). Every render treatment keys on `=== 'interpolated_estimate'` only → reconstructed renders ordinary by construction.
- `scripts/paired-provenance-read-exercise.mjs` (+ `bun run test:provenance-read`): AC-1..AC-5, AC-7, AC-8 legs; `--module/--page/--inflection/--global`.

### 4. AC-8 per-firm flat array read — portal `e8b1fb07` (DEV), COO-ruled fail-safe ORDER
- `perFirmFlatClassReader()`: (1) well-formed cohort channel → slots; (2) malformed/absent cohort AND `point_class[]` present AND length-aligned → array is the derivation owner (unknown strings still degrade LOUD; malformed-channel warn still fires); (3) neither → predates-contract measured. Misaligned array = malformed → warn + (3), never index-guess. Wired into `readModelSeries` / `readFirmAggregateSeries` / `readNonModelSeries`; the `point_class?` field doc amended in place with the order.

### 5. Evidence runs (all with the served artifacts)
| Run | Result |
|---|---|
| AFTER, final tree e8b1fb07 | **75 PASS / 0 FAIL / 0 SKIP** (2 same-input runs byte-identical, sha 7dadb1776744) |
| core-B only 778ea780 | 63 PASS / 4 FAIL — the 4 are the AC-8 live legs (able-to-fail for AC-8) |
| BEFORE, HEAD 684e67de copies | 32 PASS / 35 FAIL |
| MUT-A weakened degrade (any string passes) | 27 FAIL — AC-5 on all 4 reader paths; unknown class RELABELLED measured via derivedFirmClass |
| MUT-B loose `startsWith('reconstructed')` | 12 FAIL — `reconstructed_zzz`, `reconstructedX(evr)` wrongly accepted |
| MUT-C `return { cls: 'measured' }` fall-through restored | 7 FAIL — AC-2 rows 1,2,4,6 "got measured" + AC-7 reports the relabel |
| MUT-P page 2-way ternary restored | 3 FAIL — AC-3 ×2 + AC-7 page names line 743 |
- **AC-7 VALUE-AFFECTING numbers, live inflection, HEAD → e8b1fb07:** band-extent set size **0 → 0**; `interpolatedRanges` **[] → []**; non-model interpolated points 0 → 0; aggregate value sum **78,209,487,100.32 → identical** (445/445 non-null). Only LABELS move: aggregate/models/non-model {measured 445} → {measured 438, reconstructed 7}; count {measured 438, interpolated_estimate 7} → {measured 438, reconstructed 7} (0 consumers); Global derived {measured 403, interpolated_estimate 42, absent 9} → {measured 403, reconstructed 2, interpolated_estimate 40, absent 9} (Global band emptied by ruling). **ZERO served or rendered numbers move.**
- **AC-6:** `/frontend-dev` PNG `portal/.frontend-dev/screenshots/mdpf_evr_fe2_inflection_after.png` (1440×2315; inflection selected; served-artifact fixtures): no band, no dashed overlay, no "Interpolated" legend entry, REFAREAS 0 per chart; the 7 dates indistinguishable from neighbours; color law clean. **Control:** vs the core-B PNG (`…_coreB_778ea780.png`, all-measured labels): 60 of 3,333,600 pixels differ, all in an 8×8 box at (105,2212) = the animated "Orion Connected" status dot in the Data Source footer; both chart panels pixel-identical.

### 6. Proof-of-spec
- `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/MDPF_EVR.FE-2_PROOF_OF_SPEC.json` — 8 rows AC-1..AC-8, mutant FIRED-AS-EXPECTED, determinism STABLE; `proof-of-spec-check.py` positional form → VALID **rc=0**.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Implementation B, not A | TO constraint; A inverts `:29` and asserts a reconstructed value is measured. |
| Recognise the producer's `reconstructed(...)` slot form (STRICT prefix) | It is the producer's own declared vocabulary on cohort slots/Global legs (measured live); the `carried_at_declared_cadence(...)` precedent; strict `(` so near-misses still degrade (MUT-B pins it). |
| One exported precedence owner `deriveAggregateClass` used by BOTH derivedFirmClass and the page | Otherwise a consumer re-implements a 2-way collapse and relabels; also makes AC-3/AC-7 unit-testable and able-to-fail. |
| Surface the per-firm date-less channel as a scope surface BEFORE building around it | TO: "report immediately if a consumer cannot carry the class without a wider change"; COO ruled (i) as its own commit + AC-8. |
| Global `readGlobalPointClass` NOT given the length guard | The misaligned guard was ruled for the per-firm read; changing Global behaviour is outside scope. Declared. |
| Screenshots stay in the untracked `.frontend-dev/screenshots/` dir | Predecessor practice; PNGs not committed; paths cited. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/lib/pairedProvenanceRead.ts` | enum member + VALID + resolvePointClass + deriveAggregateClass + reader carries; then perFirmFlatClassReader + field-doc amendment | Yes — portal `778ea780`, `e8b1fb07` (DEV) |
| `portal/src/pages/ModelPortfolios.tsx` | Global aggregate row carries the class; import | Yes — portal `778ea780` |
| `portal/scripts/paired-provenance-read-exercise.mjs` | new bun exercise (AC-1..8, mutants, live legs) | Yes — portal `778ea780`, `e8b1fb07` |
| `portal/package.json` | `test:provenance-read` script | Yes — portal `778ea780` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/MDPF_EVR.FE-2_PROOF_OF_SPEC.json` | new | Yes — workspace (this commit) |
| this log | new | Yes — workspace (this commit) |

---

## Blockers

None. (No push: lanes commit, integrators push — MSTR owns the portal DEV push per the TO's cross_domain_coordination.)

---

## Current State

> Both portal commits are on DEV (`778ea780` core B, `e8b1fb07` AC-8), unpushed, portal tree on DEV. On the served inflection slice the paired read now returns `reconstructed` at exactly 2026-05-20, 05-29, 06-30, 07-10, 07-13, 07-14, 08-05 and `measured` at 438; at Global the 2 reconstructed dates carry through; zero warns mention reconstructed; the band extent is empty before and after; the rendered chart panels are pixel-identical between "all measured" and "7 reconstructed" trees. Proof-of-spec instance VALID rc=0. The producer/consumer contract mismatch (date-less `cohort_provenance` beside an aligned `point_class[]`) is routed by COO to CTO — not closed here; the FE fail-safe order is correct under either canonical answer.

---

## Next Steps

1. **[2.0.0_SA_COO] validate + close FE-2** — evidence: this log, the proof-of-spec instance, portal `778ea780` + `e8b1fb07`, PNG paths above.
2. **[0.0.0_AB_MSTR] push portal DEV** when integrating (lanes commit, integrators push).
3. **[1.0.0_SA_CTO] canonical-form question** on the inflection per-firm provenance channel (date-less slots vs aligned `point_class[]`) — routed by COO 190730Z; not mine.
4. **[2.0.0_SA_COO] 49financial cohort_provenance surprise** (count-identical distribution to cottonwood, 411 custody-absent on a ~$1.7B firm) — received + routed by COO; not mine.

— 0.4.0_DE_ClientPlatform
