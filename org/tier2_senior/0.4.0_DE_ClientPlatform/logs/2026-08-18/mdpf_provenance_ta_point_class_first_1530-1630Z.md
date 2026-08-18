# MDPF_PROVENANCE.T-A — `point_class[i]` FIRST at every grain; slots refine; `carried` known — 0.4.0_DE_ClientPlatform

**Window:** 2026-08-18 ~1530–1630Z · **Archetype:** BUILD+VERIFY (frontend contract change, no pixel change)
**Task Order:** MDPF_PROVENANCE.T-A (`org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/MDPF_PROVENANCE.T-A.reader-precedence-point-class-first.md` @49dd8469d1 — amended in place same window: carried→ORDINARY is RULED, Andrew-direct ~1500Z via COO 160737Z)
**Authority:** CTO ruling `docs/architecture/MDPF_PROVENANCE_CANONICAL_FORM_RULING_20260818.md` @fc74f8f6b4 §2 R-1. Session context: RESET-RELAUNCH (Andrew ~1503Z), first act per the 49F push plan §5.

## What shipped

Portal DEV commit **`edcc503e`** (author line mine, unpushed — lanes commit, MSTR integrates):

- `src/lib/pairedProvenanceRead.ts` — the R-1 order: **(1)** `flatClassReader` — `point_class[i]` canonical at every per-firm grain (present + length-aligned; misaligned = warn, never index-guess); **(2)** `refineWithSlot` — a well-formed dated class-enum slot REFINES the cohort series (model slot for by_model; custody for the firm aggregate + non-model band) under the `CLASS_STRENGTH` contradiction law (weaker slot ⇒ warn + flat wins; missing slot/entry ⇒ no refinement, no warn; slot `absent` refines the LEG only; flat `absent` = the producer's headline value-presence verdict ⇒ slot stands for its leg); **(3)** predates-contract `measured` only with no flat — the legacy path (`slotClass`/`derivedFirmClass` + the P1 malformed-channel warn) unchanged. `carried` joins the enum (VALID + `carried_at_declared_cadence(` prefix + `deriveAggregateClass` rank interp > reconstructed > carried > absent-all > measured); pixels ordinary per the RULING. Global readers name-tolerant `partner_provenance ?? cohort_provenance` (T-C drops).
- `scripts/paired-provenance-read-exercise.mjs` — extended (never a second instrument): PA-1..PA-6 legs, `--fortyninef`/`--cottonwood`, AC-8 fixture (1) rewritten to the ruled order.

Workspace: proof-of-spec instance `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/MDPF_PROVENANCE.T-A_PROOF_OF_SPEC.json` — **VALID rc=0**, PA-1..PA-7 all PASS.

## Acceptance (live artifacts 2026-08-18T13:50Z, BEFORE = HEAD @e8b1fb07)

| leg | before → after |
|---|---|
| PA-1 malformed-channel warn (inflection) | 1/load → **0** (49f shadowed by the shared warnOnce key; 0 → 0) |
| PA-2 Global `undefined at <date>.model` | **3,192** (456×7 measured exactly; ruling est. ~3,178 on the 08-17 read) → **0** |
| PA-3 Global `carried` | degraded + warn → **carried ×5, zero warns** |
| PA-4 contradiction | warn fires verbatim + flat wins; slots-ignoring MUTANT passes PA-1..3 and fails 7×PA-4 + PA-6-band (44→0) — able-to-fail shown |
| PA-5 unknown strings | loud degrade on all 4 paths incl. `carried_zzz`/`Carried` |
| PA-6 numbers/pixels | inflection agg sum 78,629,186,559.76 over 447/447 both sides; band extents unchanged (cottonwood **44==44**, REFAREAS 0,1 both trees); PNG diffs: global/cottonwood 60px = the 8×8 animated status dot; inflection 20,707px all ≤9/255 channel delta (AA jitter, zero content) |
| PA-7 reconstructed regression | ×7 at exactly the served dates, all series |

Suite: **110/110 AFTER · 93/110 BEFORE · 102/110 mutant.** Determinism: two same-input runs byte-identical. Runs persisted in session scratch (`run_AFTER.txt`, `run_AFTER_2.txt`, `run_BEFORE_head.txt`, `run_MUTANT_ignoreslots.txt`); PNGs `portal/.frontend-dev/screenshots/mdpf_ta_{inflection,global,cottonwood}_{BEFORE,AFTER}.png`.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| comp-to | `comp-to MDPF_PROVENANCE.T-A.reader-precedence-point-class-first` | PASS — session TO_ID set |
| comp-transform | `schema-check ModelPortfolios` | WARN types-resolution only (tool's known shape on this page, same as FE-2) |
| comp-transform | `ternary-audit ModelPortfolios` | no union-typed vars to audit (TabType only); enum-mode coverage carried by the bun suite |

(`comp-which`/`comp-find` not needed — the file set was named by the TO; raw reads were Rule-21-legal native Read/pipe-grep drills into files already localized.)

## Surprises (banked, no action)

1. **Cottonwood flat `absent` ×44 beside interpolated slots with plotted values** (the 3F-BF2 band) — a literal flat-wins would erase the Andrew-ordered band. Implemented per the producer's own `_flat_point_class` semantics (flat `absent` = headline value-presence verdict; slot stands for its leg). Banked to COO 154643Z + CTO 154658Z same turn, proceeded without hold; CTO can overrule with one line.
2. BEFORE malformed-warn is memo-shadowed across artifacts (module-level key `dates[0]+length` identical for inflection/49f) — browser saw 1/load fabric-wide, not 1 per artifact.
3. Live Global PA-2 denominator 3,192 (artifact advanced one date past the ruling's read).

## State / next

- Portal DEV: `edcc503e` on top of `e8b1fb07`, tree on DEV, unpushed. **[0.0.0_AB_MSTR]** push at next integration.
- **[2.0.0_SA_COO]** validate + close T-A (this log + the proof-of-spec instance + the PA-1/PA-2 before/after; CTO reads PA-1/PA-2 on the live artifacts per the TO).
- **[this seat]** next: T-C (08-20, drop the Global name tolerance — GATED on T-B's producer rename landing on the scheduled path) → OPAL_ADVIPOINTERS.P4-REPOINT-49F (08-22, GO'd 160737Z; first act = per-key read-surface enumeration, per-key flip only after CVO pin+cert cited in the commit).

— 0.4.0_DE_ClientPlatform
