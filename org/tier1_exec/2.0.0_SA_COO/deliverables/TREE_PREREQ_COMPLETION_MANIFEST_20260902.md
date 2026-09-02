# TREE PREREQUISITE COMPLETION MANIFEST -- the set that goes to `3.0.0_SA_CVO` ONCE, when complete

**Authority:** Andrew-direct 2026-09-02 ~21:0xZ (@a8d63f097c), verbatim: *"Project tree prereq builds
are mandatory start point (call 3), split up work with CTO on that, and when you guys are completely
done issue it to CVO for review."* **Split acked** by `1.0.0_SA_CTO` 21:23Z (by artifact: COO = prereqs
1 + 3 + the contract; CTO = prereqs 4 + 5). **Reviewer:** `3.0.0_SA_CVO` base, event-gated on this
file reading COMPLETE in every row. **Spec:** s.8 prerequisites @31463f1286; calls RULED @5f8b774a5d.

**Row shape (both halves use it so the rows concatenate):**
`prereq | build | owner | state | commit | falsifier + denominator | residual (who, what)`
States: `RULED` (needs no build) · `BUILT` (exercised, committed) · `BUILT-UNCOMMITTED` (exercised,
lane blocks the commit, says which) · `OPEN` (not yet landed; owner named). **The set is COMPLETE when
no row reads OPEN or BUILT-UNCOMMITTED and every residual names a holder outside the two builders.**

## The rows

| # | prereq (spec s.8) | build | owner | state | commit | falsifier + denominator | residual |
|---|---|---|---|---|---|---|---|
| 0 | the contract as DATA (s.3a) | `org/standards/PROJECT_TREE.contract.json` v0.1.0 -- levels, regexes, folder contract, index shape, refusal ids, globs | 2.0.0_SA_COO | BUILT | @cb6e93e7f8 | the generator loads it and `--self-test` runs every refusal id it names (18/18); CTO's (5) harness instantiates its shape as a fixture | NONE -- a change is a versioned edit + the diff stated to `readers` |
| 1 | ratify the macro enum for D0/D8/D11 | Rule 24 record `MACRO_ENUM_RULE24_D0_D8_D11_20260902.md` (352-row word-boundary census, denominators printed) + carrier `org/missions/MACROS.yaml` (D0 [NFRA], D8 [ETFS, MDPF, AUTH], D11 [NFRA], all `ratification: PROPOSED`) | 2.0.0_SA_COO | record BUILT @cb6e93e7f8; carrier BUILT-UNCOMMITTED (lane `org/missions/**` = TIER0_MSTR; lands via CTO's (4) re-key or MSTR's commit -- MSTR asked 21:48Z) | @cb6e93e7f8 (record) | R2 mutants in `--self-test`: "macro not in enum -> [R2, R5]", "enum PROPOSED -> [R2, R5]"; live: MACROS.yaml 0 of 3 RATIFIED, tree refuses everything (measured) | **ANDREW** -- ratification per directive, verbatim, recorded on the carrier. The only sovereign item in the set. |
| 2 | `task-orders` vs `task_orders` | none -- RULED (hyphen, tree only, prospective) | -- | RULED | @5f8b774a5d | contract carries `task_orders_dir: task-orders` + the glob; CTO's (5) TO-discovery falsifier reads both roots | NONE |
| 3 | index generator + DIRECTIVES.yaml derive/validate, RED-FIRST | `.tools/missions-tree-index.py`: `check` (0/1/2, never writes) · `derive [--write]` (GENERATED entries only; DIRECTIVES.yaml VALIDATED, never written, exact additions printed) · `--self-test` | 2.0.0_SA_COO | BUILT | @cb6e93e7f8 | `--self-test` 18/18: empty-tree baseline; planted valid project RED (INDEX-MISSING) -> `derive --write` -> GREEN; one mutant per refusal asserting the EXACT id set; hand-written twin refused on write; MSTR register siblings ignored. **Live baseline:** tree=0, flat rows 352 (352 hand-written / 0 generated / 0 parse errors), DIRECTIVES.yaml 38 entries / 13 directives, 0 violations, rc 0. `commit-gate.sh` clean 1 of 1. | pytest wrapper of `--self-test` under `.tools/tests/` -> **0.8.0_AE_CloudComp** (lane TOOL_BATTERIES); not a blocker for the set |
| 4 | re-key lanes for `org/missions/**` ONLY | `.owned-paths.yaml` + `owned-paths-check.sh`, s.6 per-artifact lanes; write set from COO 21:48Z (a-f) | 1.0.0_SA_CTO | OPEN | -- | both directions through the validator's own harness (CTO's 15-row matrix) | -- |
| 5 | repoint each s.7 reader to BOTH roots | `to-pipeline-gate.py` (L3 reads the index; TO discovery adds `org/missions/D*/*/*/task-orders/*.md`; `FOO_BAR_BAZ -> FOO_BAR` walk-back RETIRED), `surprise-row-gate.py`, `surprise-watch.sh` (glob + watermark to `.tools/state/`) | 1.0.0_SA_CTO | OPEN | -- | each red-first through the REAL harness (5 s hook timeout, 90 s collection ceiling), against the contract's fixture shape, then re-run against the generator's real output | `missions.yaml` attach globs (s.7 "RETIRED -- the tree is the attach") -> **0.0.0_AB_MSTR**, asked 21:15Z |

## Not in the set (so nobody reads their absence as a gap)

- **Prereq 6-7 (the water tests themselves)** -- Andrew's, after the set is validated: *"once we're
  completely good to go on Call 3 setup and validated, we can use CLDGRPH as a water test, more
  details on that at that time."* `NFRA_CLDGRPH` first, then `ETFS_GUARDRAIL`, then
  `NFRA_COMPEFFICACY` registered fresh. No folder under `org/missions/D*/` exists until then; the
  generator's live baseline of 0 tree projects is the measured state of that bound.
- **Migration** -- none (s.8). 352 flat rows untouched; `org/projects/` stays their register.

## Surprise-channel observations raised while building (OBSERVATION class, routed, not chased)

- 2 of 352 flat rows carry a `project_code` beginning `projects\MDPF` (a path fragment in the code
  field). Pre-existing, flat, outside the tree. -> `3.0.0_SA_CVO`, session log.
- `OPAL_ANALYST` row says `directive: D6`; D6's `members.projects` is empty -- the one list-vs-field
  disagreement across 13 directives / 38 entries. -> `0.0.0_AB_MSTR` 21:48Z.
