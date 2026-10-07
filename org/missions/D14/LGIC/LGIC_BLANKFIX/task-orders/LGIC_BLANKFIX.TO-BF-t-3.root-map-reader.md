# TO LGIC_BLANKFIX.TO-BF-t-3 -- round 1 BF-t-3: the root map -- one entry says which system, firm and source a root's names belong to

<to_id>LGIC_BLANKFIX.TO-BF-t-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-t-3` (`decompositions/LGIC_BLANKFIX_DECOMP.md`) | **outcome_ref:** FWD-1 (hop 4), FWD-7 (thin) |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**What the check is.** `python lib/opal_naming.py census --repo` reads names from the repository and grades each with
`grade(name, type) -> (verdict, canonical)`. `census_repo()` (`lib/opal_naming.py`) returns `(items, stats)`; each item is a dict
`{"plane": "repo", "type": <node type>, "current": <the name>, "where": "<repo-relative file>:<line>"}`. A canonical form may carry a
blank written in braces: `{system}`, `{cadence}`, `{source}`, `{scope}`. `grade()` raises `opal_naming.RaiseDefect` for a name it
cannot place. Import the library with `sys.path.insert(0, "lib")` then `import opal_naming`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency.

**The root of this round** is `infra/aws/terraform/bd-pipeline/` read together with the Lambda source folders it deploys (at the cut:
`infra/aws/lambda/bd-pipeline/`). Measured at the cut on the repository plane: the root's `.tf` files give 96 graded names, 12 with a
`{system}` blank and 9 with a `{cadence}` blank; the source folder gives 37 graded names, 16 with a `{source}/{scope}` blank, and 6
names skipped by the cards in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json`.

### THE CELL

`BF-t-3`, the thread's hop 4. Andrew ruled on 2026-09-21 that the registry's name-to-system rows are to be compiled from a small
handwritten map of Terraform root to system, with only genuine exceptions written by hand. No such map and no reader exist. You
build the reader and you PROPOSE the entry for this round's root. You do not write the registry: the map file is landed by another
seat from your proposal.

**Facts you need.** `infra/logic/registry/resources.json` holds handwritten rows of the shape `{name, type, system, evidence}`; a
row fills the `{system}` blank for a name whose own words resolve no system. `infra/logic/registry/systems.json` holds the system
keys and `scopes.json` the firms. The schema's rule SY1 (`org/standards/NAMING_SCHEMA.json`, `system.vendor_through_tiers`): a
resource that builds a firm's data from ONE vendor's feed is that vendor's integration (system = the vendor key, for example
`blackdiamond`); a resource that combines feeds takes the product that owns the combination (for example `advi`). So one root can
hold more than one system: the map gives the root's default and names the exceptions.

**Build** `lib/opal_naming_rootmap.py` (a new module; do not edit `lib/opal_naming.py`):

1. `load_map(path) -> dict`. The file is JSON: `{"_about": "...", "roots": {"<root folder name>": {"system": "...", "scope": "...",
   "source": "...", "evidence": "...", "exceptions": [{"name": "...", "type": "...", "system": "...", "evidence": "..."}]}}}`.
   `system` must be a key of `systems.json`, `scope` a firm form `scopes.json` knows, `source` a source the key grammar knows
   (read how `opal_naming.key()` validates a source and use the same check); a value that is none of these raises `ValueError`
   naming the root and the field. The path is always an argument; bake no default path.
2. `resolve(map, root, name, type) -> dict | None`: `None` when the root has no entry; else `{"system", "scope", "source",
   "basis"}` where `basis` is `"exception"` when `(name, type)` matches an exception (its `system` replaces the default) and
   `"root-default"` otherwise.
3. A command line: `python lib/opal_naming_rootmap.py reference ROOT --map PATH` takes every name `opal_naming.census_tf_names()`
   finds in the root's `.tf` files that ALSO has a row in `resources.json` (the reference answers), and compares the row's system
   with `resolve()`'s. Prints one line per name and a last line `ROOTMAP-REFERENCE ok=True root=... rows=N agree=N disagree=0`;
   `ok=False` when any disagrees or `rows` is 0. `python lib/opal_naming_rootmap.py views --map PATH` runs
   `opal_naming.generate()` into two temporary folders, once as the repository stands and once with the map file copied into a
   temporary copy of the registry folder, and compares every generated file byte for byte. Last line
   `ROOTMAP-VIEWS ok=True files=N changed=0`; `ok=False` when any file differs (a registry-side file that moves a generated view is
   a deploy, and the issuer must know before the file lands).

**Write the proposal** at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/ROOT_MAP_PROPOSED.json`: the map file with ONE root, `bd-pipeline`.
Derive its default system, firm and source from the root's own `.tf` and Lambda code (which vendor's feed it ingests, for which
firm) and from the registry rows that already place names of this root; every existing row whose system differs from the default
becomes an exception with that row's evidence. State in `evidence` what you read. Where SY1 leaves a name's system undecided on
the evidence in the repository, do not guess: leave it out of the exceptions and list it in your report.

**Build** `lib/tests/test_opal_naming_rootmap.py`, runnable as a plain script, on a small map it writes to a temporary folder: a
name listed as an exception resolves to the exception's system, and THE SAME name with the exception removed resolves to the root
default (the difference control); an unknown root resolves to `None`; an unknown system key raises. Last line
`ROOTMAP-TEST ok=True assertions=N`.

### ACCEPTANCE

<criterion id="BF3-AC1" cell_refs="BF-t-3"><invocation>python lib/tests/test_opal_naming_rootmap.py</invocation><expect>ROOTMAP-TEST ok=True</expect></criterion>
`BF3-AC1` -- the reader resolves a default and an exception, and the exception changes the answer.

<criterion id="BF3-AC2" cell_refs="BF-t-3"><invocation>python lib/opal_naming_rootmap.py reference infra/aws/terraform/bd-pipeline --map org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/ROOT_MAP_PROPOSED.json</invocation><expect>ROOTMAP-REFERENCE ok=True</expect></criterion>
`BF3-AC2` -- the proposed entry reproduces every registry row that already places a name of the root (the real neighbour).

<criterion id="BF3-AC3" cell_refs="BF-t-3"><invocation>python lib/opal_naming_rootmap.py views --map org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/ROOT_MAP_PROPOSED.json</invocation><expect>ROOTMAP-VIEWS ok=True</expect></criterion>
`BF3-AC3` -- the map file moves no generated view. A fourth criterion is not needed.

<expected_criteria>BF3-AC1,BF3-AC2,BF3-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- You do not create or edit any file under `infra/logic/`. The proposal lives in your deliverables folder only.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootmap.py
lib/tests/test_opal_naming_rootmap.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `org/standards/NAMING_SCHEMA.json`, every file under `infra/logic/registry/`, every file under `infra/aws/terraform/bd-pipeline/` and `infra/aws/lambda/bd-pipeline/`, `infra/aws/lambda/ci/lambda-source-map.json`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md`.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md</decomp_doc> (round 1), cell `BF-t-3`.
<owned_cells>BF-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-AC1, BF3-AC2, BF3-AC3. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-t-3.root-map-reader.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF3-AC1,BF3-AC2,BF3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; the proposal's path and its `bd-pipeline` entry printed; the count of reference rows and of exceptions; every name SY1 left undecided, with what evidence is missing; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a map entry that contradicts rows Andrew already approved (AC2 compares against every such row of the root, and refuses a zero denominator); a reader that bakes the proposal's path so the fixture becomes the product (the path is an argument; the face says so); a registry-side file that silently moves a shipped generated view (AC3); a guessed system for a name SY1 does not decide (listed, not guessed); BLIND: names of the root that live only in AWS and not in the .tf files.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @47ef4c98cc section 2 (THREAD); decomposition round 1 @f15f222030. Base dry-run at the cut: BF3-AC1, BF3-AC2, BF3-AC3 base FAIL as expected (files absent).
