# FANOUT 04 — C4 decommission surface (verbatim agent report, received 2026-08-12 ~20:40Z)

**Agent scope:** everything that defines, consumes, names, snapshots, or gates on C4. **Evidence
class: agent-derived. Harness note: the raw agent output had control-tag entities neutralized
(`&lt;` escapes); normalized here, content untouched.**

---

**Scope scanned:** 26,104 files in comp-find's repo scope (1 unreadable, not searched). Workspace
root `C:\Users\AndrewBerman\Desktop\ajb_workspace`, branch CLOUD.

## 0. HEADLINE: THE SURFACE IS FAR SMALLER THAN IT LOOKS

**MEASURED — there is exactly ONE code read of C4 data in the entire repo:**
`org\modules\graph\opal_estate_infrastructure.py:660` — `segs = d["c4_segments"]`

Everything else is prose, docs, or historical record. Two structural facts make this true:
1. **C4 IS NOT IN THE GRAPH.** `LAYER_FIELD_ANATOMY.md:411-412` — *"C4 IS NOT IN THE GRAPH. A query
   for C4/Segment node types returns 0 rows. It is a pure YAML registry."* Independently confirmed
   (§4).
2. **NO D-RAIL TERMINATES AT C4.** `LAYER_FIELD_ANATOMY.md:473` — *"C4 carries no obligation, no
   contract, no freshness."* `:409` — *"nothing is derived FROM C4, things are FOUND through it."*

**The engine is NAME-AGNOSTIC.** `cmd_segments()` (:644-686) iterates `segs.items()` generically,
reads five optional fields — `display_name` :672, `registry` :673, `flags` :674, `verticals_served`
:675, `high_signal` :676. **No segment name is hardcoded anywhere in the engine.** Renaming/removing
segments breaks no code path; deleting the `c4_segments` KEY → fail-loud KeyError branch :661-664
(rc=2).

## 1. FILES THAT DEFINE OR ENUMERATE C4 / SEGMENTS

### 1a. AUTHORITATIVE DEFINITION (the data)
| File | Lines | What |
|---|---|---|
| `org\modules\graph\NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` | **494-578** | `c4_segments:` — THE registry. Keys :495 partner-data, :514 market-intelligence, :532 interactive-products, :545 access-delivery, **:560 estate-infrastructure** |
| same | **392-492** | `c4_subject_function_grid:` (RATIFIED 2026-08-12, :393). Segment→row/column map :458-462; overlap law :463-482; non-summable :483-492 |
| same | **307-326** | `c4_verticals:` — SUPERSEDED (§6) |
| same | 376-386 | C4 SEGMENTS header comment |
| same | 613-620 | `terminology_law.segments_vs_verticals` |
| same | 1, 28, 100, 112, 200 | scattered C4 prose |

### 1b. TERM REGISTRY (SYSTEM_DEFINITIONS.yaml)
- **:130-133 `C4:`** — authority points at both `#c4_segments` and `#c4_subject_function_grid`;
  `sits_at: ladder rung 4; STABLE canon`
- **:135-138 `Segment:`** — five names inline; **already spells `andrew-infrastructure`**
- **:190-191 `World_Model:`** — spine *"C4 segments -> C3(i|ii) -> C2 -> C1 -> C0"* — **breaks on
  dissolution** (named as INVERTED by R1)
- **:43-51** — Subject (`sits_at: C4 grid, axis 1 (rows)`) and Function (axis 2) — both cite the grid
- **:13-14** — v2.1/v2.0 changelog carrying the grid law + rename; **:23-24** v1.2/v1.1 (C4→C0 schema)
- **:202** — `authority: infra/system/ontology/C0_C1_C2_C3_C4_SYSTEM_LAYERS.md (serving law)`

### 1c. THE LADDER DOC — SERVED VERBATIM BY A LIVE TOOL MODE
`infra\system\ontology\C0_C1_C2_C3_C4_SYSTEM_LAYERS.md` — served byte-for-byte by `comp-estate
--layers` (`opal_estate_infrastructure.py:497`, `cmd_layers()` :493). C4 assertions at :2, :11-12,
**:25** (`C4 SEGMENTS 5 LEGISLATED, never discovered`), :122-124, :131, :135, :142, :152, :159, :162.
**INFERRED:** the FILENAME itself encodes C4 — renaming it breaks `cmd_layers()` :497 and the
citations at `SYSTEM_DEFINITIONS.yaml:202` + its own :159.

### 1d. THE FIELD-ANATOMY DOC
`infra\system\ontology\LAYER_FIELD_ANATOMY.md` — **:404-479** the entire C4 section; **:416
enumerates all five names as `estate-infrastructure`** (stale vs the rename); :443 (13 sys-* names);
:469-479 (edges). Plus :1, :20, :32-33, :37, :47, :179, :379, :384.

### 1e. SECOND (VESTIGIAL) YAML DEFINITION SITE
`org\modules\graph\NFRA_ONTOLOGY_RULE_BANK.yaml` — **:675-692** a `c4_verticals:` block whose
`status:` still reads **`RATIFIED 2026-07-30`** and whose `invariant:` still asserts *"DECLARED,
never discovered."* Only the inline `#` comment redirects to the canonical file. **:713-714**
`c4_note:` (*"C4 SEGMENTS remain legislated registries of C3.i; verticals_served stays a DERIVED
VIEW"*).

### 1f. THE DECISION RECORD ITSELF
`org\tier1_exec\4.0.0_SA_CRO\deliverables\ANDREW_DIRECT_20260812_C4_DISSOLUTION_C3II_INFERENTIAL_KIMI_ESTATE_PIPELINE.md`
— R1 (:36-44) self-declares what it inverts; R5 (:63-71) commissions the spec incl. comp-estate.

## 2. CODE CONSUMERS (exhaustive)

**Denominator: `grep -rn "c4_segments" --include=*.py` across the repo returned exactly 1 hit.**

| # | File:line | Nature | Breaks? |
|---|---|---|---|
| 1 | `opal_estate_infrastructure.py:660` | **THE ONLY DATA READ** | **YES — hard**, KeyError rc=2 |
| 2 | same :644-686 | `cmd_segments()` | YES — the mode |
| 3 | same :849-851 | `--segments` argparse flag | YES |
| 4 | same :876-877 | dispatch | YES |
| 5 | same :665-667 | banner prose "C4 SEGMENTS" + route string | Cosmetic |
| 6 | same :681-685 | footer denominator + ladder prose | Cosmetic |
| 7 | same :1,5,15 | module docstring | Cosmetic |
| 8 | same :493-497 | `cmd_layers()` serves the C4-named doc | Indirect (§1c) |
| 9 | `estate_infrastructure_cli.py:354-355` | legacy footer "C4 -> C3 no rail…" | Cosmetic, user-facing |
| 10 | `.tools\tool_index.py:2231,2235,2241,2249,2261,3107,3132` | **generated comp-which routing index** — :3132 `'--segments'` in subcommands; :2261 the C4 use_case | **YES — routing** |
| 11 | `.tools\comp-estate:5` | shim docstring | Cosmetic |

### EXERCISED (not merely read)
- `comp-estate --segments` → rc=0, `denominator: 5 segments`, emits all five incl.
  `estate-infrastructure  (Estate Infrastructure)`.
- `comp-which "which C4 segment does my question live in"` → **routes to comp-estate --segments at
  score 1.50, top of 75 tools** — the comp-which surface IS a live consumer via tool_index.py.

### --matrix and --layers — CLARIFICATION
- **`--matrix` (:579) does NOT touch C4.** Grep for `segment|c4_|C4` in :579-643 → no hits. It is the
  C3.i × C3.ii cross-partition matrix. **Survives C4 dissolution untouched.**
- **`--layers` (:493) touches C4 only by serving the ladder doc verbatim** (§1c).

### REGISTRY / CONTRACT SURFACES (route agents to the mode)
- `graph-call-manifest.yaml` — :1274 use_case, :1275 canonical_call, :1280 freshness
  ("--segments/--matrix are VIEW-COMPILED"), :1284 notes ("ONE SCHEMA C4 -> C3(i|ii)…; 5 segments"),
  :1760 tools_index entry.
- `comp-output-contracts.yaml` — :673 ("C4 segments (stable canon) -> C3 systems -> chains"), :681.
- `CLAUDE.md:80` — the comp-tools table row naming --segments as an ontology view.

## 3. SEGMENT NAMES AS LITERAL STRINGS

**TWO FALSE-POSITIVE CLASSES CONTAMINATE THE NAIVE SEARCH — both measured:**
**(A)** `market-intelligence` matches inside `sys-market-intelligence-engine` — a **C3.i system name,
not a C4 segment**. In the canonical: 8 occurrences, 6 are sys-prefixed, only 2 the segment. In
`c3ii_semantic_scan.py:36,38` + `_v2.py:55,57`: all 4 hits are the system inside a vertical→system
map. **Those CRO scripts are NOT C4 consumers.**
**(B)** filename slugs and prose: `C3II_SEMANTIC_SCAN_V2_OUTPUT_20260811.json` shows 13 hits — walked
structurally, **all 13 are one docs/briefs path inside BM25 doc lists**. NOT a consumer. Same for
`rcg\ledger\LABELS.jsonl:3203` and the 0.1.0_*_MarketIntelligence pod TO files.

### TRUE SEGMENT-NAME LITERALS
Search over the four unambiguous names → **18 files**: LIVE/DEFINITIONAL (5) — the canonical,
SYSTEM_DEFINITIONS:136, LAYER_FIELD_ANATOMY:416, C0_C1_C2_C3_C4_SYSTEM_LAYERS:11-12, engine+shim
docstrings. DESIGN DOCS (2) — `OPAL_KIMIPIPELINE_STATE_FRICTION_DESIGN.md:373`,
`projects\ATOM_DECOMP\07_BASE_RETRO_TEST_AGAINST_RCN0006.md:43`. HISTORICAL (11) — the dissolution
record, AWS_ESTATE_CENSUS_20260730 files, CVO~C coherence-base docs, staleness audit, CVO handoff+log.

> Note: `CVO_C_THIRD_SYSTEM_PROJECT_COHERENCE_BASE_20260807.md:59-62` records comp-estate REFUSING
> `estate-infrastructure` — *"'estate-infrastructure' is NOT a known C3.ii vertical"* — an agent
> already conflated a C4 segment name with a C3.ii vertical name. On the record.

### THE LIVE NAME DRIFT — MEASURED
`estate-infrastructure` → `andrew-infrastructure` (Andrew-direct 2026-08-12) **landed in the prose
layer and NOT in the data**: SYSTEM_DEFINITIONS:136 + changelog v2.1 + canonical:460 spell
`andrew-infrastructure`; **the actual `c4_segments` KEY (canonical:560), the live tool output,
LAYER_FIELD_ANATOMY:416, and C0_C1_C2_C3_C4_SYSTEM_LAYERS:11-12 all still spell
`estate-infrastructure`.** The tool emits a name the term registry says was retired.
`andrew-infrastructure` appears in exactly 3 files — never in the data it names.

## 4. SNAPSHOT / CACHE FILES — NONE materialize segment data. Zero.

| File | `segment` | pos. control `named_thread` | pos. control `chain` | bytes |
|---|---|---|---|---|
| `estate-coverage-manifest.yaml` | **0** | 135 | 4 | 41,800 |
| `estate-coverage-resolver.json` | **0** | 141 | 28 | 174,978 |

Positive controls fired, so the zero is a real absence. Independently corroborates
LAYER_FIELD_ANATOMY:412 by a different derivation. **CONSEQUENCE: `c4_segments` in the canonical YAML
is the SOLE materialization of C4.** No cache to invalidate, no snapshot to regenerate, no graph node
to drop.

## 5. GATES, HOOKS, CI — NONE depend on C4.

Scanned all 8 executable hooks in `.tools\hooks\`, `.github/`, `.claude/settings.json`,
`.claude/settings.local.json`. **Zero hits for `c4_segments` or `--segments`.** comp-tool-hud.sh
mentions comp-estate only in advisory nudge text pointing at OTHER modes. `comp-manifest-check` — 0
occurrences of comp-estate/segment/c4; the binary stays, so the manifest gate is unaffected.

**FALSE POSITIVES on "C4" — do not chase:** `opal_estate_infrastructure.py:980` (`--self-test`
control #C4 in a C0-C5 series, not the rung); `comp-tools.yaml:215` + `graph-call-manifest.yaml:252`
("C4 dogfood", a comp-similar PRD control id); `comp-coverage-map.yaml:952` (`AC4`, debtscan
acceptance criterion).

## 6. `c4_verticals` — VESTIGIAL. Superseded, checksum/lineage only, read by ZERO code.

Canonical :307-326, banner :307-313: *"SUPERSEDED SECTION (layer claim retired; checksum + candidate
record retained). VERTICALS WERE RE-SLOTTED TO C3.ii on 2026-07-30… never cite this section for a
layer assignment."* Fields: :315 `superseded_by: c3_ii_semantic_verticals` · :316-322 definition
("SUPERSEDED 2026-07-30…") · :323 `count_checksum: 29` ("a checksum, not the source") · :324
`pending_candidates_awaiting_naming: []` — empty · :325-326 naming_ladder_binding.

Vs `c4_segments`: superseded vs live; 3 metadata fields + empty list vs 5 keyed entries; ZERO code
readers vs 1; no tool output vs --segments. Never siblings — `c4_verticals` is the pre-2026-07-30
name for the layer; the naming act (*"Segments may be a better name than Verticals"*, :376-379)
renamed the layer and moved verticals down to C3.ii. It is the fossil of that move.

**BUT IT IS DUPLICATED, AND THE DUPLICATE IS NOT MARKED SUPERSEDED** — `NFRA_ONTOLOGY_RULE_BANK.yaml:675-692`
still reads `RATIFIED 2026-07-30` + *"DECLARED, never discovered"*; a YAML parser sees a RATIFIED
section; it also **contradicts R2**. **INFERRED:** the canonical's own supersession banner (:311-312)
records this drift class being caught once before (*"one canon file was carrying two contradictory
layer assignments for 'vertical'"*) — the RULE_BANK copy was not remediated in that pass.

## 7. RESIDUAL / NOT-FOUND (with controls)

- **Portal/frontend: NO consumer.** All five names + c4_segments over `portal/src/` → 1 hit,
  `TenantLayoutConfig.ts:255`, a comment about a data path, not the segment. Positive control: 387
  .ts* files reached.
- **No Terraform, Lambda, S3 key, or served artifact** references C4. `inf-pipeline/alarms.tf:175`
  ("a silent partner-data freeze") is comment prose.
- **The sys-causality-engine RETIREMENT-PENDING flag** (canonical:517, market-intelligence.flags) is
  the ONLY populated `flags:` across all five segments (grep denominator 1). R1 names it as moving to
  the annotation layer. Rendered by :674.

## 8. OPEN ITEMS CARRIED IN THE C4 BLOCK (would be orphaned)

From canonical :471-482: `open_adjudications.model-portfolios` (:472-474, ROW×ROW) ·
`open_adjudications.ops-internal` (:475-477, spans two rows) ·
`semantically_suspect_not_a_defect.portfolio-management` (:478-482) · `function.build` (:446-452,
PROVISIONAL, settled by the placement pass).

**INFERRED:** these live inside `c4_subject_function_grid`, which the dissolution PRESERVES. Not
orphaned — but R1 states *"membership computes from the grid"*, and per
`overlap_law.measured_2026_08_12` (:468-470) current membership is a **hand-assigned 38 slots over 29
verticals, not computed. The computation R1 assumes does not exist yet** — MEASURED: no code in the
repo derives segment membership from the grid (the only reader, :660, reads the hand-written lists).
