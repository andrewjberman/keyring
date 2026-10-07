# TO LGIC_BLANKFIX.TO-BF-t-5 -- round 1 BF-t-5: the key classes -- each storage key of the root is a whole address, a legacy store, a pattern, or listed

<to_id>LGIC_BLANKFIX.TO-BF-t-5</to_id>
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

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-t-5` (`decompositions/LGIC_BLANKFIX_DECOMP.md`) | **outcome_ref:** FWD-1 (hop 6), FWD-4 and FWD-8 (thin) |
**depends_on:** BF-t-3 merged (the root's map entry); handed by continuation

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

`BF-t-5`, the thread's hop 6. For a storage key written in Lambda source, `grade()` prints the canonical key with `{source}` and
`{scope}` blanks (for `gold/trigger-pending.json`: `{source}/{scope}/gold/trigger-pending.json`). The schema says those blanks are
filled "from the bucket". Nobody has classified these rows. You build the classifier.

**Facts you need.** The items are `census_repo()` items of type `S3Key` (and `S3_BUCKET`) whose `where` is under a Lambda source
folder of the root; at the cut `infra/aws/lambda/bd-pipeline/` holds 16 such rows with a blank, one of them `silver/%s/`.
`infra/logic/registry/legacy_addresses.json` lists stores that keep a legacy address (read its `_about` and how
`opal_naming._on_list()` / `_legacy_list()` match a key against it; reuse those functions). The root's map entry (module
`lib/opal_naming_rootmap.py`, merged before this order is handed: `load_map(path)`, `resolve(map, root, name, type)`) gives the
root's `source` and `scope`. `opal_naming._VAR_RE` is the library's own test for a variable segment (`{...}`, `*`, `%s`).

**Build** `lib/opal_naming_keyfill.py` (a new module; do not edit `lib/opal_naming.py` or `lib/opal_naming_rootmap.py`):

1. `fill_keys(items, root_entry) -> list[dict]`: for each item whose graded canonical carries a blank other than `{system}` or
   `{cadence}`, one dict with `type`, `current`, `where`, `class`, `canonical` (or `None`) and `basis`. The classes, tested in this
   order so they are disjoint:
   - `PATTERN`: the CURRENT name has a variable segment (`_VAR_RE` matches). `canonical` is `None`; `basis` names the variable.
   - `LEGACY`: the key matches an entry of `legacy_addresses.json`. `canonical` is the current key; `basis` names the entry.
   - `ADDRESS`: `root_entry` is not `None`; `canonical` is the graded canonical with `{source}` and `{scope}` replaced by the
     entry's `source` and `scope`. If any `{` remains after the replacement the row is `UNDECIDED`, not `ADDRESS`.
   - `UNDECIDED`: none of the above; `canonical` is `None`; `basis` says what is missing.
   An item `grade()` raises on is skipped and counted. A key whose own path names a different firm or source than the root entry
   (for example a `cot` file under a 49 Financial root) is `UNDECIDED` with that conflict as its basis: do not fill it.
2. A command line: `python lib/opal_naming_keyfill.py dir SOURCE_DIR --root ROOT_NAME --map PATH` filters `census_repo()`'s items to
   those whose `where` is under `SOURCE_DIR`, resolves the root entry from the map, prints one line per classified row, and a last
   line `KEYFILL-DIR ok=True dir=... rows=N address=N legacy=N pattern=N undecided=N raising=N`; `ok=True` when the four classes sum
   to `rows`, `rows` equals an independent count of the folder's graded items carrying such a blank, and no `ADDRESS` canonical
   contains `{`, `%s` or `*`.

**Build** `lib/tests/test_opal_naming_keyfill.py`, runnable as a plain script: one case per class on small hand-made items; and the
DIFFERENCE CONTROL: the same plain key classed `ADDRESS` with a root entry and `UNDECIDED` with `root_entry=None`. Last line
`KEYFILL-TEST ok=True cases=N`.

### ACCEPTANCE

<criterion id="BF5-AC1" cell_refs="BF-t-5"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BF5-AC1` -- each class is reachable, and the root entry is what turns a listed key into a whole address.

<criterion id="BF5-AC2" cell_refs="BF-t-5"><invocation>python lib/opal_naming_keyfill.py dir infra/aws/lambda/bd-pipeline --root bd-pipeline --map org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/ROOT_MAP_PROPOSED.json</invocation><expect>KEYFILL-DIR ok=True</expect></criterion>
`BF5-AC2` -- every blank key of the root's source folder is classed, and no printed address has a hole.

<expected_criteria>BF5-AC1,BF5-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_keyfill.py
lib/tests/test_opal_naming_keyfill.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `org/standards/NAMING_SCHEMA.json`, every file under `infra/logic/registry/`, every file under `infra/aws/terraform/bd-pipeline/` and `infra/aws/lambda/bd-pipeline/`, `infra/aws/lambda/ci/lambda-source-map.json`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md`. You also read `lib/opal_naming_rootmap.py` and `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/ROOT_MAP_PROPOSED.json`.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md</decomp_doc> (round 1), cell `BF-t-5`.
<owned_cells>BF-t-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF5-AC1, BF5-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-t-5.key-classes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF5-AC1,BF5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the root's rows by class, every `UNDECIDED` row with its basis; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a pattern printed as a complete address (PATTERN is tested first; AC2 refuses any ADDRESS carrying a variable); a cot key filled with the 49 Financial firm because it sits in this folder (the face names the conflict case as UNDECIDED; cross-firm law); a legacy store given a new address it is not meant to move to (LEGACY is tested before ADDRESS); BLIND: which bucket a key is used with at run time -- the class is decided from the repository text and the map, not from a live read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @47ef4c98cc section 2 (THREAD); decomposition round 1 @f15f222030. Base dry-run at the cut: BF5-AC1, BF5-AC2 base FAIL as expected (files absent). STAGED on BF-t-3's merge; handed to slot ~3 by continuation.
