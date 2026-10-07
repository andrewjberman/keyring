# TO LGIC_BLANKFIX.TO-BF-t-6 -- round 1 BF-t-6: the root check -- one line per name of the root, every line one of six kinds

<to_id>LGIC_BLANKFIX.TO-BF-t-6</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-t-6` (`decompositions/LGIC_BLANKFIX_DECOMP.md`) | **outcome_ref:** FWD-1 |
**depends_on:** BF-t-1, BF-t-2, BF-t-3, BF-t-4, BF-t-5 merged; handed by continuation

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

`BF-t-6`, the thread's hops 2 (Run) and 7 (Read). An engineer runs the check on one root and reads one line per name. You compose
the five modules merged before this order is handed into that one run.

**The modules you call** (all under `lib/`, merged at HEAD when you start; read each before you call it and report any that does
not match the line below):
- `opal_naming_scope.root_items(root) -> (items, stats)`: the root's names, with `stats["source_dirs"]`.
- `opal_naming.grade(name, type) -> (verdict, canonical)`: four verdicts; the fourth is the one named in the schema's
  `grade.verdicts` beside `CONFORMANT`, `ALIAS`, `OUT-OF-PATTERN` (read its spelling from `org/standards/NAMING_SCHEMA.json`; do
  not type it).
- `opal_naming_rootmap.load_map(path)`, `resolve(map, root_name, name, type) -> dict | None` with `system`, `scope`, `source`.
- `opal_naming_cadence.cadences(root) -> list[dict]` with `current`, `where`, `word`, `basis`.
- `opal_naming_keyfill.fill_keys(items, root_entry) -> list[dict]` with `current`, `where`, `class`, `canonical`, `basis`.

**Build** `lib/opal_naming_rootcheck.py` (a new module; edit none of the five):

`check_root(root, map_path, not_judged=None, out=print, report_only=False) -> int`. For every item of the root, in order, print
exactly ONE line `KIND type current -> detail  [where]`, the kind decided by the first test that applies:

1. `CARDED`: `("repo", current)` is in the card list (`not_judged`, default: the repository's own
   `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json`). Detail: "skipped by a card the
   repository holds". The run writes no card and takes none from outside the repository.
2. `PATTERN`: the current name has a variable segment (`opal_naming._VAR_RE`), or `fill_keys` classed it `PATTERN`. Detail: "a code
   pattern, not a name" and the variable.
3. `HOLE`: `grade()` raises. Detail: the raise text.
4. `RIGHT`: verdict `CONFORMANT`. Detail: the name.
5. `NOT-ASKED`: the fourth verdict. Detail: "this kind of name is not asked to carry a system" and the canonical.
6. Otherwise the name is wrong (`ALIAS` or `OUT-OF-PATTERN`). Complete the canonical: replace `{system}` from `resolve()`'s
   `system` -- EXCEPT for a name of type `IAM_POLICY` whose `basis` is `root-default` (AMENDMENT 1: an inline policy follows its
   role, so the root's default does not decide it; leave its `{system}` unfilled and it prints as `HOLE` with the detail "an
   inline policy takes its role's system; the root map does not decide it"); replace `{cadence}` from the `cadences()` row with the same `where` when its `word` is not `None`; for a key, take
   `fill_keys`'s `canonical` when its class is `ADDRESS`, and print kind `RIGHT` with detail "legacy store, keeps its address" when
   its class is `LEGACY`. If the completed form carries no `{`: `FIX`, detail the complete correct name. If a `{` remains: `HOLE`,
   detail the partial form and, in plain words, what could not be filled and why (the cadence row's `basis`, the key row's `basis`,
   or "no map entry for this root").

Last line `ROOTCHECK ok=True root=... items=N right=N fix=N not_asked=N pattern=N carded=N hole=N`; `ok=True` when the six counts
sum to `items` and `items` equals `len(root_items(root)[0])`. Return 1 when `hole > 0` and `report_only` is false, else 0. Command
line: `python lib/opal_naming_rootcheck.py ROOT --map PATH [--report-only]`, exit code = the return value.

**Build** `lib/tests/test_opal_naming_rootcheck.py`, runnable as a plain script, calling `check_root`'s line-deciding function on
hand-made items with the five modules' answers supplied as plain data: one case per kind; no `FIX` line containing `{`; and the
DIFFERENCE CONTROL: the same item set returns 1 with one unfillable cadence and 0 when that cadence is fillable. Last line
`ROOTCHECK-TEST ok=True cases=N`.

`HOLE` lines are EXPECTED on this root at the cut (a 15-minute rate, weekday crons and one pattern-only rule have no cadence word).
Do not suppress them and do not invent a word: print them. Report every `HOLE` line whole.

### ACCEPTANCE

<criterion id="BF6-AC1" cell_refs="BF-t-6"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BF6-AC1` -- every kind is reachable, no FIX line carries a blank, and an unfillable part is what makes the run fail.

<criterion id="BF6-AC2" cell_refs="BF-t-6"><invocation>python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only</invocation><expect>ROOTCHECK ok=True</expect></criterion>
`BF6-AC2` -- the real root, through the five real modules: one line per name, the counts summing to the scope's own count.

<expected_criteria>BF6-AC1,BF6-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- The hookup `census --root` in `lib/opal_naming.py` is NOT yours: the issuer adds it at the merge.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `org/standards/NAMING_SCHEMA.json`, every file under `infra/logic/registry/`, every file under `infra/aws/terraform/bd-pipeline/` and `infra/aws/lambda/bd-pipeline/`, `infra/aws/lambda/ci/lambda-source-map.json`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md`. You also read `infra/logic/registry/root_map.json`, `lib/opal_naming_scope.py`, `lib/opal_naming_rootmap.py`, `lib/opal_naming_cadence.py`, `lib/opal_naming_keyfill.py` and `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/ROOT_MAP_PROPOSED.json`.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md</decomp_doc> (round 1), cell `BF-t-6`.
<owned_cells>BF-t-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF6-AC1, BF6-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-t-6.root-check.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF6-AC1,BF6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; every `HOLE` and every `CARDED` line whole; the count per kind; any module whose behaviour did not match this face; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- the landed map, and the registry owner's condition

- The root map is LANDED: `infra/logic/registry/root_map.json` @650452aae2 (`4.0.0_SA_CRO`, msg 106224). `BF6-AC2` runs on it, not on
  the proposal. Read its `_about.not_decided`.
- That seat's condition, made mechanical in rule 6 above: the root default supplies no system for an `IAM_POLICY` name. Such a name
  prints `NOT-ASKED` when the grader returns `NO-SYSTEM-ASKED`, and `HOLE` otherwise.
- The scope gives this root TWO source folders (`infra/aws/lambda/bd-pipeline` and `infra/aws/lambda/historical-prices-scheduler`),
  140 names at the last read. Use `stats["source_dirs"]`; type no folder.
- `fill_keys` also returns rows of class `UNDECIDED` (a `cot` key under this root): print them as `HOLE` with the row's `basis`.
- A name `grade()` raises on is a `HOLE` (rule 3); six such keys exist in this root's source folder.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a line with a blank printed as FIX (rule 6 and AC1 refuse it); a name dropped so the list looks clean (AC2: the six counts sum to the scope's own item count); a hole hidden by --report-only (the flag changes the exit code only, never a line; the difference control in AC1 runs without it); a card written for the run (the face forbids it; FWD-5); BLIND: names of the root that exist only in AWS -- this round's run is the repository plane.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @47ef4c98cc section 2 (THREAD); decomposition round 1 @f15f222030. Base dry-run at the cut: BF6-AC1, BF6-AC2 base FAIL as expected (files absent). STAGED on the other five merges; handed to slot ~1 by continuation.
