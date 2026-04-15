# CTO Session 28 — ADVI_ROLLUP Registration

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-04-15
**Trigger:** Andrew directive to roll every outstanding ADVI work item into one master project. Source: DS post-presentation master brief at `org/tier2_senior/0.4.0_DS_ClientPlatform/briefs/2026-04-15_post_presentation_master_summary.md`.

## Decision — Option A (absorb)

Presented two structural options:
- A. Absorb: close `ADVI_FNTEND` / `BDPL_ASTDIM` / `BDPL_CNPRCS` as merged into `ADVI_ROLLUP` with wave-based sequencing.
- B. Umbrella: keep children active, add a coordination doc on top.

Andrew picked A. Task order filenames are preserved (renaming would break git history and compiler-log rows); only registry ownership moves.

## Actions

### Authored
- `docs/architecture/ADVI_ROLLUP.md` — Master PRD with 6-wave structure, dependency graph, compiler-run matrix for 17 new TOs, risk register, success criteria.
- `org/projects/ADVI_ROLLUP.json` — Project registered, `absorbs: ["ADVI_FNTEND", "BDPL_ASTDIM", "BDPL_CNPRCS"]`, wave structure + phase + blocking populated.

### Deleted
- `docs/architecture/ADVI_ROLLUP_MASTER_WAVE.md` — superseded umbrella draft (untracked, no commits). Replaced by `ADVI_ROLLUP.md` under Option A.

### Edited (absorption metadata)
- `org/projects/ADVI_FNTEND.json` — `status: active → merged`, `merged_into: ADVI_ROLLUP`, `merged_as: Wave 3`.
- `org/projects/BDPL_ASTDIM.json` — `status: active → merged`, `merged_as: Wave 1`.
- `org/projects/BDPL_CNPRCS.json` — `status: active → merged`, `merged_as: Waves 0 + 2`.

### Dashboards
- `org/projects/REGISTRY.md` — removed ADVI_FNTEND / BDPL_CNPRCS / BDPL_ASTDIM rows from Active; added ADVI_ROLLUP row; added the three as "Merged 2026-04-15" entries in Completed table with pointer notes.
- `org/tier1_exec/1.0.0_SA_CTO/prompt.md` — Active Projects table shows ADVI_ROLLUP in place of the three absorbed projects; Recently Completed/Merged section flags the merges.
- `org/tier1_exec/2.0.0_SA_COO/prompt.md` — Pod Delivery Dashboard updated identically; recently-merged note added.

## Wave structure (from PRD)

| Wave | Label | Source item(s) | Owners |
|---|---|---|---|
| W0 | Tactical thaw | #1 + #2 (3-bond scoped exceptions + WP-11 formalization) | DS |
| W1 | BD pipeline foundation (ex ASTDIM) | #5 (only W7 remaining) | AE |
| W2 | BD canonical refactor (ex CNPRCS) | #6 (WP-3..WP-10) | DS + AE |
| W3 | ADVI frontend correctness (ex FNTEND) | #10 + #11 (+ B1 AE rerun) | RD + DE + DS + AE |
| W4 | Structural convergence | #7 ROLEAUA + #8 CANNNA + #9 SLEEVE | DS |
| W5 | Standalone point fix | #3 D_04 RFS window NNA | DS |

Item #4 (GEO 3-way NNA point fix) not taken — superseded by ADVI_CANNNA per DS brief §4 recommendation.

## TOs to author (COO, at decomposition)

17 new TOs, each with the compiler-run prerequisites listed in PRD §Compiler Tools:
1. `BDPL_CNPRCS.WP-3.ae-cusip-backfill-silver-transactions.md`
2. `BDPL_CNPRCS.WP-10.ds-account-id-lifecycle.md`
3. `BDPL_CNPRCS.WP-11.ds-scoped-price-overrides.md`
4. `ADVI_ROLLUP.RF01.ds-d04-window-nna-delta-fix.md`
5-10. `ADVI_ROLLUP.RA-P0..P5.ds-role-aua-canonical-convergence.md`
11-16. `ADVI_ROLLUP.CN-P0..P5.ds-nna-canonical-convergence.md`
17-20. `ADVI_ROLLUP.SL-P0..P3.ds-sleeve-reconstruction.md`
21. `ADVI_ROLLUP.FE01.de-cost-basis-year-bucket-parameterize.md`

(List in PRD has 8 entries but with phase fan-out expands to 21 distinct TOs.)

Existing staged TOs carry forward unchanged: `3-bond-phantom-scoped-exceptions.md`, `BDPL_ASTDIM.W2/W4`, `BDPL_CNPRCS.WP-4..WP-9`, `ADVI_FNTEND.B0..B8/D6/B1-rerun`.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| N/A | Rollup PRD absorbs three existing PRDs; fresh per-wave compiler runs deferred to COO TO-authoring time per §Compiler Tools matrix in `ADVI_ROLLUP.md`. No new blast-radius changes since child PRDs were ratified. | Intentional |

Per-TO mandates and run matrix documented in PRD. COO MUST run the listed compiler commands before authoring each of the 17 new TOs.

## State
- Active projects post-rollup: `ADHC_DESIGN`, `ADVI_PROFAU`, `ADVI_ROLLUP`. (Down from 5.)
- Inactive / On Hold: `ADHC_TMSTEL`, `ADVI_INCMTL`.
- COO handoff briefing produced in chat.
