# W-29 — the M-A..M-I method-read disposition (Andrew-direct 08-14: "handled next session")

**Author:** `4.0.0_SA_CRO` (method steward — rectangle/atom_decomp METHOD homed here, 08-11
ratification; site-Z applications stay theirs, findings route in as inputs) · 2026-08-18 ~16:4xZ ·
**archetype:** IMPLEMENT
**Corpus:** `workflows/atom_decomposition/runs/comp-verdict-tools/20260811T1931Z/METHOD_READ.md`
@8cc474bfb7 (author `0.8.0_AE_CloudComp~Z`, routed to this seat per the 194438Z re-home; + CVO~Z's
necessary-inequality item, 201715Z refinement). **Authority to handle:** Andrew-direct 2026-08-14
~20:20Z at this terminal, VERBATIM: *"note that those 9 review items from the other log need to be
handled next session."*

**Where amendments land:** schema —
`projects/ATOM_DECOMP/skill/atomic-decomposition/references/ssot_establishment.schema.json`;
method text — `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md` step 14(e.1) (the
steward-amendment precedent from the handover merge). All schema changes are BACKWARD-COMPATIBLE
by construction (`oneOf` legacy+new, optional fields, additive enum).

## Dispositions

| item | disposition | landed where | note |
|---|---|---|---|
| M-A `semantic_layer_refs` marker taxonomy | **ADOPT** (CTO~Z ruled the fix 191711Z; this lands it in the schema) | schema: items `oneOf` [legacy string, `{ref, role: SEMANTIC \| PRIOR_UNDER_TEST}`] | new packets use the marked form; legacy packets stay valid |
| M-B bootstrap semantic layer | **ADOPT** | schema description on `semantic_layer_refs` + SKILL.md (e.1) | first-of-domain = own declared frame + ratified law, role-marked; citing nothing else is CONFORMING |
| M-C K.1 shared-tree disk-layer leak | **ADOPT** | SKILL.md (e.1) SHARED-TREE RULE | withheld artifacts live outside the shared tree; run dir at packet-HEAD IS the packet; K.2 names residual routes |
| M-D `PLANT_MUTANT` mission | **ADOPT** | schema: `patch_meta.mission` +1 enum value, **patch-only** — the rubric mission enum deliberately does NOT carry it (a plant is not a work mission; Rule-24 intent coherence) | removes the mandated lie; no leak surface (plant patch withheld under K.1 regardless) |
| M-E `changes_applied` cycle field | **ADOPT** | schema: `run_manifest.cycles.items.changes_applied` (optional integer) | DRY becomes machine-readable from run.json alone; legacy manifests valid |
| M-F relations plane optional at instrument grain | **RECORD (positive)** | SKILL.md (e.1) GRAIN NOTE | absence of the relations plane on an instrument subject is conforming, not a hole |
| M-G typed denominator | **ADOPT** | schema: `evidence.denominator` `oneOf` [legacy string, array of `{n, of_what, unit, contained_in?}`] | role-swap of true numbers becomes a validator catch (that run's mutant validated rc=0 under the free string — exercised); `contained_in` makes the necessary-inequality pass mechanical (CVO~Z refinement) |
| M-H `count_unit` axis | **ADOPT via M-G** (M-H's own stated preference) | the typed entry's `unit` field | unit (lines/occurrences/ast_nodes) is its own axis; `count_grain` CLASS\|INSTANCE untouched — two axes, two fields (Rule-24) |
| M-I method-read as leak carrier | **ADOPT** | SKILL.md (e.1) DISCLOSURE-WINDOW RULE | any author artifact in an open certification window is under K.1 until verdict — run dir AND routed commentary |
| + CVO~Z necessary-inequality pass | **ADOPT** | SKILL.md (e.1) first clause + M-G's `contained_in` | checkable-for-impossibility before measurement; declared nesting makes it mechanical |

## Verification (all run post-edit, this commit)

- Schema parses; `ssot_validate.py --self-test` = 0 failures.
- **Backward compat, full census:** 51 run artifacts validated — **49 PASS** (every previously-passing
  artifact still passes), 2 FAIL both in `portal-page-cma/20260811T1729Z` — **PRE-EXISTING**, proven
  by running the identical file against the HEAD-vintage schema copy (same single violation,
  `'meta' is a required property`); that run is the abandoned first cma attempt, superseded by
  1801Z which passes.
- **14/14 positive+negative controls** on the four new forms: each accepts its positive, refuses its
  mutants (missing `unit`, stray key, bogus role, bogus mission, string `changes_applied`, empty
  refs), legacy forms stay valid, and the rubric enum REFUSES `PLANT_MUTANT` (the patch-only scope
  is itself control-tested).

## Scope notes

- `docs/architecture/OPAL_ANALYST_PRD.md` §9.8.1 (site-Z's program PRD, the K/K.1/K.2 bindings home)
  is **deliberately not edited from this seat** — applications stay site-Z's; the method package is
  the steward's surface and SKILL.md (e.1) now carries the rules with their M-item provenance. If
  CTO~Z wants the PRD bindings text to absorb M-C/M-I verbatim, that is their edit, cited here.
- W-29 CLOSES with this record. The walk-list successor items (W-24 placement pass → W-02) are
  unchanged behind it.
