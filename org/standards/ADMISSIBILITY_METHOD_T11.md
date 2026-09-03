# ADMISSIBILITY METHOD (T11) -- what evidence a validator is shown for an artifact

**Status:** BUILT 2026-09-03 by `4.0.0_SA_CRO` on Andrew's word at the CRO terminal (*"yes, add T11 to the
build order"*, then *"DO it"*). The slot in `comp-adversary`'s DECLARED EXCLUSIONS carried this seat's name from
2026-08-19 (*"T11 admissibility method: named slot, ships when CRO's method ratifies"*) and was empty until now.
**Enforced by** `.tools/comp-adversary` source 3 (`decomp_neighborhood`), self-test control 6.
**Spec:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/SPEC_CANONICAL_FLOW_V3_SUBAGENT_WORKERS_ONE_SHOT_DISPATCH_20260903.md`
section 12 step 5 and section 13 L-4.
**Applies to** any artifact `comp-adversary compose` is run against.

---

## THE METHOD, IN ONE SENTENCE

**An evidence item is ADMISSIBLE to the validator of an artifact when it sits on the artifact's own dependency
graph in the decomposition -- never merely because it shares a directory with something the author cited.**

## WHY THIS FILE EXISTS

Before it, `comp-adversary` answered *"what might the author not have seen"* with FILESYSTEM ADJACENCY: the
directory siblings of every path the artifact cited. **MEASURED 2026-09-03 on `NFRA_COMPEFFICACY.TO-CE-T-2`:**
93 "uncited siblings", the first twenty-five being `org/mcp/.exec-sum-state`, `org/mcp/broker.db-shm`,
`org/mcp/agent-spawn-audit.log` -- the neighbours of ONE cited path (`org/mcp/comp-tool-runs.jsonl`) -- while the
five cells the task order actually depended on, their proof instances and the PRD rows it named appeared nowhere.
The tool's own exclusion list said so: *"neighborhood = directory siblings only."* A validator handed that list
reads noise wearing evidence clothing, and the CVO's L9 time goes to discarding it.

## WHAT IS ADMISSIBLE, in order

For an artifact that carries a delimited `<decomp_doc>` and `<owned_cells>` (a tree task order), or a proof-of-spec
instance whose `decomp_ref.to_ref` names one:

| # | admissible item | where it comes from | what the declaration prints |
|---|---|---|---|
| 1 | **the decomposition** the owned cells live in | `<decomp_doc>` | its path at read-vintage |
| 2 | **the dependencies, ONE HOP, from BOTH carriers** | the decomposition's `depends_on` column for each owned cell; AND the cell ids the task order's own `<decomp_ref>` body names outside `<owned_cells>` | both lists; the ids in both, decomp-only, TO-only; the RAW `depends_on` text per owned cell (so a DROPPED / RETIRED word stays visible) |
| 3 | **the task orders that own each dependency** | `task-orders/*.md` under the project whose `<owned_cells>` names the cell | path; or `NO task order owns this cell` |
| 4 | **their proof-of-spec instances** at read-vintage | `deliverables/*/<to-stem>.proof_of_spec.json` | path; or `UNPROVEN` -- and a count `UNPROVEN dependencies: N of M` |
| 5 | **the PRD**, with the sections the artifact names | `prd/*_PRD.md` under the project; tokens `s.N[.N]`, `FWD-N`, `T-N`/`G-N`/`R-N` found in the artifact | path + the token list, so the validator opens THOSE sections |

**NOT admissible when 1-5 resolve:** directory siblings of cited paths. They are **DEMOTED to a declared exclusion
carrying their count** (*"directory-sibling neighborhood: DEMOTED -- N sibling(s) withheld"*). Withheld, never
silently dropped: the number is the validator's to question.

**The packet (stage 4) then digests the MEMBERS** -- items 1-5 -- under the existing salience rule, and prints
`domain: neighborhood members` so a reader can tell which set was selected from.

## WHEN IT DOES NOT RESOLVE

The artifact carries no `<decomp_ref>`; or its `<decomp_doc>` / `<owned_cells>` are undelimited; or the decomposition
does not sit under a project tree's `decompositions/` folder (the legacy flat root); or the decomposition file is
absent at read-vintage. Then **directory siblings stand as the neighborhood, and the declaration says which reason**
(*"T11: decomposition neighborhood NOT RESOLVED (<reason>) -- filesystem adjacency stands"*). A fallback that looks
like a graph read is the failure this clause prevents.

## NON-APPLICATION, stated so nobody reads past it

- **ONE HOP.** The dependency set is the owned cells' DIRECT `depends_on`. Transitive closure -- the dependency's
  dependencies -- is a v2 limb. A validator reading `dependencies (ONE HOP): 5` has been told the boundary.
- **Pipe-split tables.** The `depends_on` column is read by splitting the markdown row on `|`. A literal `|` inside a
  cell shifts columns for that row. The raw text is printed so a shifted read is visible, not silent.
- **Ids by token.** Dependency ids are extracted from a PROSE column by the cell-id grammar
  (`org/standards/DECOMP_CELL_ID_CONVENTION.md`). A cell named in that column as DROPPED still extracts; the raw text
  beside it carries the word. The method hands the validator the id AND the sentence; it does not adjudicate the
  sentence.
- **The first `*_PRD.md`** under `prd/` is the PRD. A project with two is out of contract.
- **Flat-root projects** (`org/projects/<CODE>/`) do not resolve; they get the pre-T11 neighborhood, declared.

## THE CONTROL

`comp-adversary --self-test` control 6: a planted project tree (Q-a-2 depends on Q-a-1; Q-a-1 owned by a task order
with a proof; a PRD; the artifact also citing a real repo path so siblings exist). GREEN asserts the graph section,
the dependency in BOTH carriers, the proof found, the PRD tokens, a non-zero sibling demotion, `UNPROVEN 0 of 1`, and
the T11 exclusion line gone. **RED was measured on the pre-T11 binary against the real TO-CE-T-2:** the section
name is absent and 93 siblings print -- every conjunct fails there.

## WHAT CHANGES FOR THE VALIDATOR

Under canonical flow v3 (spec section 5), the CVO is the seat that goes deep. This method is what it goes deep ON:
the artifact's chain -- decomposition, dependencies from both carriers with their disagreements, the proofs that
exist and the ones that do not, and the PRD sections in play. Not the broker's database files.
