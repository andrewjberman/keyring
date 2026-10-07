# TO LGIC_BLANKFIX.TO-BF-r-5 -- round 3 BF-r-5: the exercise again -- the root run live, 140 of 140 lines acted on from the line alone

<to_id>LGIC_BLANKFIX.TO-BF-r-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-r-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round3.md`) | **outcome_ref:** FWD-1, FWD-3 |
**depends_on:** BF-r-1 and BF-r-2 merged, and the registry acts their holes name landed; handed by AMENDMENT 1

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline` prints one line per name of
that root: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it
exits 1 while any line is a `HOLE`. Round 2's run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`: 140 names,
9 right, 113 fix, 9 not asked, 1 pattern, 6 carded, 2 refused, 0 holes. A seat that built none of it read that run and could act on
122 of the 140 lines from the line alone; its grade, with the 18 lines it could not act on, is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md` -- read it first. The modules are under `lib/`:
`opal_naming.py` (`grade`), `opal_naming_scope.py` (`root_items`, `root_table`, `contested`), `opal_naming_rootmap.py` (`load_map`,
`resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py` (`policy_roles`, `system_for`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read
the ones your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency. The bar for the library: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at
the base (194 passed); no test may fail after your build.

### THE CELL

`BF-r-5`. After `BF-r-1` and `BF-r-2` are merged and the registry's lane has landed what their holes name, run the thread and
save it. You build nothing in `lib/`.

1. Run `python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only` from the worktree root. Save the whole output to
   `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/THREAD_TRACE_round3_bd-pipeline.txt`.
2. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_trace_round3.py`: it runs the same command
   again, compares its output with the saved file line for line, and checks on the live output: `hole=0`; the seven counts sum to
   `items`; no `FIX` line contains `{`; every `NOT-ASKED` line contains "rename"; no two different current names of one type share
   a `FIX` target. Last line `TRACE-R3 ok=True items=N hole=0 differs=0`; `ok=False` on any failure, each named on its own line
   above.
If `hole` is not 0, do NOT force it: report every `HOLE` line whole and why it remains; `BR5-AC1` then fails as written and that
is a correct outcome of this order.

### ACCEPTANCE

<criterion id="BR5-AC1" cell_refs="BF-r-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_trace_round3.py</invocation><expect>TRACE-R3 ok=True</expect></criterion>
`BR5-AC1` -- the saved trace is the live run, and the live run has no hole, no shared target and no bare not-asked line.

<criterion id="BR5-AC2" cell_refs="BF-r-5" judgment="true"/>
`BR5-AC2` (judgment) -- `3.0.0_SA_CVO`, a seat that built none of the check, runs the root LIVE, reads it to the end, and can act on 140 of 140 lines from the line alone, telling a wrong name apart from one not asked for a system. You record the artifact's path and NO verdict.

<criterion id="BR5-AC3" cell_refs="BF-r-5"><invocation>python lib/tests/test_opal_naming_function_literal.py</invocation><expect>FNLITERAL-TEST ok=True</expect></criterion>
`BR5-AC3` (AMENDMENT 1) -- a literal held under a function name is typed a Lambda, the same literal elsewhere is not, and every retyped name in the repository became a Lambda.

<expected_criteria>BR5-AC1,BR5-AC2,BR5-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- AMENDMENT 1 adds two `lib/` files to your grant for its step 0; the rest of your build lives in your deliverables folder.
- In `lib/opal_naming.py` edit only the source-literal classifier and what feeds it its context. `grade()`, `_slots`, `_cadence_slot` and the Terraform reader are not yours.
- The judgment criterion gets its artifact path and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
lib/opal_naming.py
lib/tests/test_opal_naming_function_literal.py

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round2.md`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md</decomp_doc> (round 3), cell `BF-r-5`.
<owned_cells>BF-r-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BR5-AC1, BR5-AC3, BR5-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-r-5.exercise-again.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BR5-AC1,BR5-AC2,BR5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the trace's path; the count per kind; every line that is not `RIGHT`, `FIX` or `PATTERN`, whole; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- STEP 0, a reader fix ruled by the CTO, before the run

`1.0.0_SA_CTO` ruled (msg 106460) on the two EC2 names that share a target. It measured one machine, `bd-fees`
(`infra/aws/terraform/bd-pipeline/ec2.tf:86`). The other name is not a machine:
`infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py:52` reads
`FEES_RUNNER_FUNCTION = os.environ.get("FEES_RUNNER_FUNCTION_NAME", "bd-49f-fees-runner")`, a Lambda FUNCTION's name, and line 51
(`RUNNER_FUNCTION = os.environ.get("RUNNER_FUNCTION_NAME", "bd-49f-runner")`) is the same case. "The reader types that literal as
a Lambda function ... and the collision goes." This sentence of the cell no longer holds: "You build nothing in `lib/`."

**Why it happens.** `lib/opal_naming.py` `_census_classify(value, ctx, v, kinds)` types a kebab literal by its LAST token when
exactly one node type owns that token as a kind (`runner` is an EC2 kind), whatever name holds the literal. `ctx` is the name
context the literal sits under; read `_py_literals`, `_js_literals` and `census_source_names` to see what `ctx` carries for an
assignment, a keyword argument, a dict key and a call argument such as `os.environ.get("X_NAME", "literal")`.

**STEP 0, build in `lib/opal_naming.py`, minimally:**
1. A literal held under a FUNCTION-NAME context is typed `LAMBDA`, before the last-token rule. A function-name context is a
   holding name (the assignment target, the keyword, the dict key, or the environment variable's own name in an
   `os.environ.get` / `os.getenv` / `process.env` read) that contains the word `function` or `lambda` as a whole word part
   (`FEES_RUNNER_FUNCTION`, `RUNNER_FUNCTION_NAME`, `functionName`, `lambda_name`), case-insensitive. If `ctx` does not carry the
   environment variable's name or the assignment target for the `os.environ.get(...)` shape today, extend what feeds it.
2. Nothing else changes: a literal under no such context is typed exactly as today.

**And** `lib/tests/test_opal_naming_function_literal.py`, a plain script:
- on small source texts: the two shapes type their literal `LAMBDA`; the DIFFERENCE CONTROL: the SAME literal
  `bd-49f-fees-runner` under the name `FEES_RUNNER_INSTANCE` still types `EC2_INSTANCE`; a bucket and a secret literal are typed
  as before;
- on the real repository: the literals at lines 51 and 52 of that Lambda source are typed `LAMBDA`; and the whole-plane
  measurement: `census_repo()`'s items against the same items with your rule switched off (keep a module-level switch the test
  can flip, default on): every item whose type changed printed with its `where`; every changed item must have changed TO
  `LAMBDA`.
Last line `FNLITERAL-TEST ok=True fees_runner=LAMBDA runner=LAMBDA retyped=N other_changes=0 items=N`.

Then `python -m pytest lib/tests -q -p no:cacheprovider`: no test may fail. If a worked case or a card keyed on a name now misses
because the name's TYPE changed, report it; edit no card and no registry file. Then steps 1 and 2 of the cell.

**The other four holes** (stored-file paths skipped by a card that names nothing) are `4.0.0_SA_CRO`'s to answer in the registry
(same ruling). If any still prints `HOLE` when you run, `BR5-AC1` fails as written: report those lines whole; do not force it.

### AMENDMENT 2 (2.0.0_SA_COO~G, 2026-10-07) -- STEP 0b: the run reads the registry's key rulings

The four stored-file paths that print `HOLE` ("skipped by a card; the card gives no correct name and does not say none is owed")
are answered. `4.0.0_SA_CRO` landed `infra/logic/registry/key_rulings.json` @662cbb0be5 on the CTO's ruling: a new file, keyed
(bucket, key), each row carrying exactly one of `canonical` (the whole correct address) or `none_owed` (a plain sentence: no name
is owed, and why). Read its `_about` for the exact row shape; one row is a prefix whose key has no trailing slash, as the item
prints it. The card file is not edited and nothing reads these answers yet.

**STEP 0b, build in `lib/opal_naming_rootcheck.py`** (the files are added to your grant; the order of round 3 that held them,
`BF-r-2`, is merged before this order is handed):
1. Load the file from the registry folder (`opal_naming.REGISTRY_DIR`). For a stored-file item, match on (bucket, key): the
   bucket is the one `opal_naming_keyfill.bucket_of(item)` reads; a row whose bucket differs does not match.
2. A matched row is tested BEFORE the card: with `canonical`, the line is `FIX` when the canonical differs from the current key
   and `RIGHT` when it equals it, the detail the whole address; with `none_owed`, the line is `NOT-ASKED`, the detail "no name is
   owed for this stored file: " and the row's sentence, and "no rename is owed".
3. An item whose bucket cannot be read does not match any row; it keeps its card line and the reason says the bucket was not
   read.
4. Extend `lib/tests/test_opal_naming_rootcheck.py`: one case per branch, and the DIFFERENCE CONTROL: the same key matches a row
   of its own bucket and does not match the same row under another bucket. `ROOTCHECK-TEST ok=True` still.
Report what each of the four keys printed before and prints now.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a saved example graded in place of the live run (the check re-runs and diffs; FWD-1 says a saved example fails); zero holes read as the outcome (the judgment criterion BR5-AC2 is the outcome; AC1 is its floor); BLIND: names of the root that live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @ef7133ec9a (the CTO's enrichment list); decomposition round 3. Base dry-run at the cut: BR5-AC1 base FAIL as expected (file absent).
