# MDPF_PROVCANON — stage-3 CHARTER + operative-surface ENUMERATION (pre-decomp)

**Author:** 2.0.0_SA_COO · 2026-08-21 · **Stage:** 3 of the DIRECTIVE EXECUTION PIPELINE (Rule 27)
**Authority:** Andrew ratification @8e40cb7861; CTO stage-1/2 landing @11267259a7; PRD
`docs/architecture/MDPF_PROVCANON_PRD.md`.
**Status:** ⛔ **THIS IS NOT THE DECOMP.** It is the charter (package "Compile the assessment") plus a
measured surface enumeration. The certified rectangle does not exist and no TO may cite this file as a
cell. See §4 for why, and for what stage 3 actually costs.

## 1. CHARTER

- **Objective:** ONE INTENT PER KEY for served MDPF provenance, IDENTICAL key set + shape across all four
  scopes and both producer trees, reader tolerance retiring only on observed completion at every scope.
- **Decision it enables:** the tolerance drop (R-1 retire) and the served-key schema flip.
- **Authority / mutation mode:** read-only for the decomp itself; no producer edit is authorized by stage 3.
- **Scope:** scopes `49financial`, `inflection`, `cottonwood`, `global`; trees `data/mdpf/scripts/**` and
  `data/assets/scripts/gold/**`; serving `opal-data-assets portal/gold/mdpf/{scope}/…` +
  `opal-data-portal-v2 platinum/mdpf/{scope}/…`; reader `portal/src/**`.
- **Invariants:** no pixel change (2026-08-15 presentation ruling); no shadow path / parallel emitter /
  standing comparator (2026-08-04 veto); scheduled 13:30Z path only; NEVER#3 both halves at any served
  schema flip.
- **Consumer boundary:** the portal read path. Any non-portal consumer of these keys is OUT until named.
- **Exclusions (stated, not assumed):** T-B Half-1 count-carry re-point (landed, executing, exercised);
  DE's R-1 tolerant reader. Neither is this project's work; neither is reverted.

## 2. OPERATIVE SURFACES — MEASURED, and the PRD named THREE of them

`comp-find -i`, denominators printed, scanned scope 9,801 files (6 UNREADABLE, not searched — binaries;
recorded as a coverage limitation per package Rule 6, not as absence).

Token census: `cohort_provenance` 117 · `cohort_source` 6 · `partner_provenance` 11 · `point_class` 191 ·
`non_model` 886.

| # | surface | class | in PRD §3? |
|---|---|---|---|
| 1 | `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` | producer (gold) | ✅ named |
| 2 | `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` | producer (other tree) | ✅ named |
| 3 | `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` | producer / `point_class` derivation | ✅ named |
| 4 | `data/assets/scripts/gold/build_cottonwood_interpolated_backfill.py` | **BACKFILL producer** | ❌ **NOT NAMED** |
| 5 | `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py` | **BACKFILL producer** | ❌ **NOT NAMED** |
| 6 | `data/mdpf/scripts/backfill/eclipse_vintage_reconstruction.py` | **BACKFILL (`point_class`)** | ❌ **NOT NAMED** |
| 7 | `data/assets/scripts/gold/validate_interpolated_backfill.py` | **VALIDATOR** | ❌ **NOT NAMED** |
| 8 | `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py` | **producer (`point_class`, other artifact)** | ❌ **NOT NAMED** |
| 9 | `portal/src/lib/pairedProvenanceRead.ts` | reader | ✅ named |
| 10 | `portal/src/pages/ModelPortfolios.tsx` | **reader (second)** | ❌ **NOT NAMED** |

**SIX OF TEN SURFACES WERE NOT NAMED IN THE PRD.** That is not a criticism of the PRD — it is
purpose-level BY DESIGN and says so. It is the evidence that stage 3 is load-bearing rather than
ceremonial: a decomp built from the PRD's territory paragraph would have produced cells over three
producer surfaces, and its proof-of-spec would have passed **green over a 3-of-10 denominator**, silent
about the rest. That is the exact failure I argued this morning — *a non-MECE decomp yields a
proof-of-spec whose holes are invisible by construction.*

### 2a. THREE SURFACE CLASSES THE PRD'S "PRODUCERS" LINE DOES NOT REACH

- **BACKFILL PRODUCERS (#4, #5, #6).** They write HISTORICAL vintages. A canonical-form change asks a
  question the PRD does not: *does backfilled history conform, or is history exempt?* Both answers are
  defensible; **neither is free**, and an unasked question here becomes a mixed-shape archive.
- **A VALIDATOR (#7).** It asserts against today's shape. On a shape change it either breaks loudly
  (good) or **passes vacuously** (the instrument-that-cannot-fail class this fabric hit twice today).
  Which one it does is a MEASUREMENT, not an assumption.
- **A SECOND READER (#10).** The PRD names one reader. Retiring the tolerance against a one-reader model
  when two exist is how a "complete" cutover leaves a live consumer behind.

### 2b. `non_model` IS NOT SCOPED LIKE THE OTHER THREE KEYS

PRD §4 carries "is `non_model` a leg of the class channel?" as ONE open contract question, sitting
beside three provenance keys of 6–117 hits. **`non_model` measures 886 hits** — it is a general MDPF
model/non-model concept, not a provenance leg. Answering **YES** ("every scope emits it") therefore
touches a surface an order of magnitude larger than the keys it would join, and the blast radius is not
visible from the question's phrasing. **This must be decided BEFORE cells are cut, and with the 886
denominator in front of the decider** — not inside a rename, and not on the assumption that it is a
peer-sized question.

## 3. WHAT REMAINS TO BE A DECOMP

Per the package: entity-by-field rectangle from the declared schema (every cell born UNMEASURED) · the
OWNER's DOMAIN BAR stated BEFORE measurement · status-missioned fan-out (verify MEASURED / fill
UNMEASURED / kill-or-promote INFERRED / challenge NOT_MEASURABLE) · iterate UNTIL DRY · certification
with the sealed-mutant protocol. Cells additionally need executor class + placement, the `point_class[]`
coupling as its own cell, and dependency edges with **observed-completion** triggers.

## 4. ⛔ A STRUCTURAL FINDING ABOUT STAGE 3 ITSELF — surfaced now, not at TO time

**THE CANONICAL ATOM-DECOMP IS NOT A SOLO ACT, AND RULE 27 ASSIGNS IT TO ONE SEAT.** The package
requires (a) **STATUS-MISSIONED FAN-OUT** — multiple agents returning declared patch shapes, merged only
through the validator; and (b) **CERTIFICATION SIGNED BY THE STANDING CERTIFIER SEAT, NEVER THE AUTHOR**,
with a sealed mutant and, under the SHARED-TREE RULE (M-C), withheld artifacts living outside the shared
tree until closure.

So stage 3 as ratified reads as a COO deliverable, and is in fact **a COO-OWNED RUN REQUIRING A FAN-OUT
COHORT AND A SEPARATE CERTIFIER**. Consequences, stated plainly:

1. **A COO cannot both author and certify.** Certifier must be another seat (CVO is the natural standing
   certifier; CVO is ALSO the channel owner under Rule 27 — worth checking that those two roles on one
   project do not collide).
2. **Stage 3 has a seating cost nobody costed.** The pipeline's own single-point-of-failure risk (which I
   raised at 64938 and which was answered at the COO level) is larger than it looked: it is not "a dark
   COO stops TOs from existing", it is **"a dark COO *or an unavailable fan-out cohort or certifier*
   stops TOs from existing."**
3. **THE FIRST CASE IS WHERE THIS IS CHEAPEST TO FIX.** Andrew mandated enforcement — *"I do not want to
   be dealing with this shit ever again"* — and a pipeline whose stage 3 cannot be resourced will be
   discovered at the first deadline instead of at the first project.

**NOT A REQUEST TO CHANGE THE RULE.** Andrew ratified it hours ago and the correct response to a
resourcing gap is to resource it, not to relitigate the law. Routed to CTO for the seating shape and to
MSTR for the seats.

## 5. WHAT I AM NOT DOING

Not cutting cells; not writing acceptance criteria; not issuing TOs; not certifying anything; not
answering §4's `non_model` question (it is Andrew's or a decided decomp act, and §2b changes what it
costs). **No TO may cite this file as a cell** — it is charter + enumeration, and the enumeration's own
status is MEASURED-BUT-UNCERTIFIED.
