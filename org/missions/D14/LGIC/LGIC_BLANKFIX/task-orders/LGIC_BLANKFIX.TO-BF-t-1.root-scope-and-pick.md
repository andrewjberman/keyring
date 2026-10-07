# TO LGIC_BLANKFIX.TO-BF-t-1 -- round 1 BF-t-1: the root scope -- the names the check reads for one Terraform root, and the pick of the round's root

<to_id>LGIC_BLANKFIX.TO-BF-t-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-t-1` (`decompositions/LGIC_BLANKFIX_DECOMP.md`) | **outcome_ref:** FWD-1 |
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

`BF-t-1`, the thread's hops 1 (Pick) and 2 (Run). Today the check has no way to read one root: it reads the whole repository. You
build the scope and you record which root the round runs on.

**Build** `lib/opal_naming_scope.py` (a new module; do not edit `lib/opal_naming.py`):

1. `root_items(root) -> (items, stats)`. `root` is a repo-relative Terraform root folder such as `infra/aws/terraform/bd-pipeline`
   (a trailing slash is accepted). `items` is the subset of `opal_naming.census_repo()`'s items that belong to the root, in
   `census_repo()`'s order: every item whose `where` file is under the root folder, plus every item whose `where` file is under a
   Lambda source folder the root deploys. `stats` is a dict with `root`, `tf_files` (the count of the root's `.tf` files that gave
   an item or were read), `source_dirs` (the list of source folders tied to the root) and `source_dir_basis` (a dict, one entry per
   source folder, naming the evidence that ties it to the root). Derive the tie from the repository, never from a typed list:
   read how the root's own `.tf` files point at Lambda source (for example a `source_dir`, `filename` or `path.module` reference
   into `infra/aws/lambda/`), and read `infra/aws/lambda/ci/lambda-source-map.json`. Where two kinds of evidence disagree, or a
   source folder is claimed by two roots, say so in `source_dir_basis` and file one row. An unknown root raises `ValueError`.
2. `root_table() -> list[dict]`: one dict per Terraform root under `infra/aws/terraform/` that has at least one item, with `root`,
   `items`, `group_a`, `group_b`, `group_c`, `group_d`, `pattern`, `raising`, `carded`. Grade each item with `opal_naming.grade()`
   (catch `RaiseDefect`: it counts under `raising`); apply the card file named above (an item whose `("repo", current)` matches a
   card's `("plane", "name")` counts under `carded` and is not graded). An item whose name carries `{`, `%s` or `*` counts under
   `pattern` and in no group. Otherwise a graded item whose canonical carries `{system}` is group A when its type is
   `LAMBDA_LAYER`, or its name is one PascalCase token with no hyphen, or its first token is in `systems.json`
   `refused_keys.purpose_word`; else group B. A canonical carrying `{cadence}` (and no `{system}`) is group C. A canonical carrying
   any other blank is group D.
3. A command line: `python lib/opal_naming_scope.py items ROOT` prints one line per item (`type`, `current`, `where`) and a last line
   `SCOPE-ITEMS ok=True root=... items=N tf_items=N source_items=N source_dirs=N`. `python lib/opal_naming_scope.py table` prints
   the table and a last line `SCOPE-TABLE ok=True roots=N items=N assigned=N unassigned=N`, where `assigned + unassigned` equals
   the length of `census_repo()`'s items (an item under no root and no tied source folder is unassigned; a source folder tied to
   two roots is assigned to neither and counted unassigned), and `ok=False` when the sum does not hold. `python
   lib/opal_naming_scope.py pick` prints, for each root that holds at least one item in EACH of groups A, B, C and D, its row, then
   the pick: the qualifying root with the fewest items. Last line
   `SCOPE-PICK ok=True root=... items=N group_a=N group_b=N group_c=N group_d=N qualifying=N`, `ok=False` when no root qualifies.

**Build** `lib/tests/test_opal_naming_scope.py`, runnable as a plain script. It asserts on the REAL repository, not a fixture:
every item `root_items( + ROOT + )` returns has its `where` under the root or under a folder in `stats["source_dirs"]`; the count
equals an independent filter of `census_repo()`'s items by those same prefixes; a root with no tied source folder returns only
items under itself; an unknown root raises `ValueError`. Last line `SCOPE-TEST ok=True assertions=N`.

**Record the pick** in your report: the `SCOPE-PICK` line whole. The issuer expected `bd-pipeline`; if the pick is another root,
that is a finding to report, not a defect to fix.

### ACCEPTANCE

<criterion id="BF1-AC1" cell_refs="BF-t-1"><invocation>python lib/tests/test_opal_naming_scope.py</invocation><expect>SCOPE-TEST ok=True</expect></criterion>
`BF1-AC1` -- the scope returns exactly the root's names, checked against the real `census_repo()` (the seam's real neighbour).

<criterion id="BF1-AC2" cell_refs="BF-t-1"><invocation>python lib/opal_naming_scope.py table</invocation><expect>SCOPE-TABLE ok=True</expect></criterion>
`BF1-AC2` -- every repository name is assigned to one root or counted unassigned; the sum is the denominator.

<criterion id="BF1-AC3" cell_refs="BF-t-1"><invocation>python lib/opal_naming_scope.py pick</invocation><expect>SCOPE-PICK ok=True</expect></criterion>
`BF1-AC3` -- at least one root holds all four groups, and the pick is printed with its counts.

<expected_criteria>BF1-AC1,BF1-AC2,BF1-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_scope.py
lib/tests/test_opal_naming_scope.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `org/standards/NAMING_SCHEMA.json`, every file under `infra/logic/registry/`, every file under `infra/aws/terraform/bd-pipeline/` and `infra/aws/lambda/bd-pipeline/`, `infra/aws/lambda/ci/lambda-source-map.json`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md`. You also read every `.tf` file under `infra/aws/terraform/` to tie source folders to roots.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md</decomp_doc> (round 1), cell `BF-t-1`.
<owned_cells>BF-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF1-AC1, BF1-AC2, BF1-AC3. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-t-1.root-scope-and-pick.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF1-AC1,BF1-AC2,BF1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; `stats["source_dir_basis"]` for the picked root; the list of unassigned items' folders with counts; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a scope that silently drops the Lambda sources and so never shows a storage key (the cut's base measurement: 110 of 111 key blanks sit in source files; AC1's independent filter and AC3's group_d bound it); a typed folder list standing in for a derived tie (the face asks for the evidence per folder); a source folder claimed by two roots counted twice (assigned to neither, counted, one row); BLIND: a Lambda whose source is tied to its root only at deploy time by a script outside the .tf files.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @47ef4c98cc section 2 (THREAD); decomposition round 1 @f15f222030. Base dry-run at the cut: BF1-AC1, BF1-AC2, BF1-AC3 base FAIL as expected (files absent).
