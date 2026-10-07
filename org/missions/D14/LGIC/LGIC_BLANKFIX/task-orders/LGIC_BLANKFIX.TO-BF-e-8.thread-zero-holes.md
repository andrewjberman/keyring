# TO LGIC_BLANKFIX.TO-BF-e-8 -- round 2 BF-e-8: the thread again -- the fills wired into the run, no line with a hole, and the run read by a seat that built none of it

<to_id>LGIC_BLANKFIX.TO-BF-e-8</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-8` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** FWD-1, FWD-3 |
**depends_on:** BF-e-1, BF-e-2, BF-e-3 merged; handed by continuation

---

## WORKER FACE

### CONTEXT

**Where the project stands.** Round 1 built one command: `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline`
prints one line per name of that root, each of kind `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED` or `HOLE`, and exits 1 while any
line is a `HOLE`. Its last run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`: 140 names, 10 right, 101 fix,
6 not asked, 1 pattern, 6 carded, 16 holes. The modules, all under `lib/`: `opal_naming.py` (`grade(name, type) -> (verdict,
canonical)`, `census_repo()`, `census_tf_names()`), `opal_naming_scope.py` (`root_items(root)`), `opal_naming_rootmap.py`
(`load_map`, `resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py` (`word_for`, `cadences`),
`opal_naming_keyfill.py` (`fill_keys`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read the ones your cell touches or
calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new
dependency. The bar for the library's own suite: `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider` fails six
named tests at the base (see `lib/tests/test_opal_naming_fourth_verdict.py` for the list); no test that passes at the base may fail.

### THE CELL

`BF-e-8`. Three cells merged before this order is handed give the run what it lacked: `opal_naming_cadence.verdict_for` (the
schedule's word, and whether a carried word agrees), `opal_naming_policyrole.system_for` (an inline policy's system from its
role), and a bucket-aware `opal_naming_keyfill.fill_keys` (classes `PATTERN`, `LEGACY`, `REFUSED-CROSS-FIRM`, `ADDRESS`,
`UNDECIDED`). You wire them into `lib/opal_naming_rootcheck.py` and run the thread. Read the three modules as merged; report any
that does not match this paragraph.

**Change** `lib/opal_naming_rootcheck.py` (`decide` and what feeds it):
1. **Inline policy.** For an `IAM_POLICY` name whose canonical carries `{system}` and whose declaration `policy_roles(root)` knows:
   fill `{system}` from its role's system (`FIX`, the complete name). Unresolved role: `HOLE` with the role row's basis.
2. **Cadence.** For an `EVENT_RULE` or `SCHEDULE`: the word is the SCHEDULE's. A `{cadence}` blank is filled from it. A name that
   already CARRIES a word the schedule contradicts (`agrees=False`) is not `RIGHT` and not a finished `FIX` on the carried
   word: print `FIX` with the canonical rebuilt on the schedule's word. A schedule the reader still cannot name: `HOLE`, as today.
3. **Keys.** `REFUSED-CROSS-FIRM` prints as a new kind `REFUSED`: "this key belongs to another firm's store" and both firms. It is
   counted in the last line (`refused=N`) and it does NOT make the run exit 1: it is a finding about the code, stated whole, not
   a blank. `UNDECIDED` stays `HOLE`.
4. **Carded.** A `CARDED` line prints the card's own reason: the card's `card` text up to its first sentence end, and the whole
   correct name where the card gives one. It keeps the kind `CARDED`.
5. **Layers.** Nothing to build: `openpyxl-layer` prints `NOT-ASKED` once the registry's lane removes its row; report what it
   prints on your run.
Last line: `ROOTCHECK ok=True root=... items=N right=N fix=N not_asked=N pattern=N carded=N refused=N hole=N`, the seven counts
summing to `items`.

**Extend** `lib/tests/test_opal_naming_rootcheck.py`: one case per new behaviour above; no `FIX` line containing `{`; the DIFFERENCE
CONTROL kept (one unfillable cadence makes the run return 1; fillable returns 0); a `REFUSED` line alone returns 0.
Last line unchanged in shape: `ROOTCHECK-TEST ok=True cases=N`.

**Run the thread** and save its whole output to
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/THREAD_TRACE_round2_bd-pipeline.txt`.
If `hole` is not 0, do NOT force it: report every `HOLE` line whole and why it remains. `BE8-AC2` then fails as written and you
say so; that is a correct outcome of this order.

### ACCEPTANCE

<criterion id="BE8-AC1" cell_refs="BF-e-8"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BE8-AC1` -- each new fill is reachable, no fix carries a blank, and an unfillable part still fails the run.

<criterion id="BE8-AC2" cell_refs="BF-e-8"><invocation>python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only</invocation><expect>hole=0</expect></criterion>
`BE8-AC2` -- the real root through the real modules prints no hole.

<criterion id="BE8-AC3" cell_refs="BF-e-8" judgment="true"/>
`BE8-AC3` (judgment) -- a seat that built none of the check reads the saved trace to the end and can act on every line without asking a question, and tells a name that is wrong apart from a name that is not asked for a system. You record the trace's path and NO verdict.

<expected_criteria>BE8-AC1,BE8-AC2,BE8-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- The judgment criterion gets its artifact path and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-8`.
<owned_cells>BF-e-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE8-AC1, BE8-AC2, BE8-AC3 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-e-8.thread-zero-holes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE8-AC1,BE8-AC2,BE8-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the saved trace's path; every `HOLE`, `REFUSED` and `CARDED` line whole; the two formerly `-daily` rules' lines; what `openpyxl-layer` prints; commits.

### AMENDMENT 1 (2.0.0_SA_COO~G, 2026-10-07) -- the state you start from, measured after the three merges

- The three cells are merged, and the registry moved under them: eleven service words are now `purpose_word`, the
  `openpyxl-layer` row is gone, and ruled event rules live in `infra/logic/registry/event_rules.json`. The run on the trunk at
  hand time: `ROOTCHECK ok=True root=infra/aws/terraform/bd-pipeline items=140 right=9 fix=109 not_asked=9 pattern=1 carded=6
  hole=6`. The cadence holes are already gone, because the grader itself now reads the interval forms; rule 2 above still
  stands (wire `verdict_for`, so the run and the reader are one reader, and use its `canonical` for a ruled event rule).
- The six lines still `HOLE`: four inline policies no service word leads (`pipeline-chain` twice, `runner-shared-read`,
  `gold-layer-trigger`), which rule 1 fills from the role; and the two Cottonwood-path keys, which rule 3 prints as `REFUSED`.
- Row `LGIC_BLANKFIX-W3-S3`: today the run prints those two keys with a generic reason. A `REFUSED` line prints the key row's
  own `basis` and `bucket`.
- `opal_naming_cadence.verdict_for(row)` returns `word`, `carried`, `agrees` and `canonical`; under the ratified rules a
  Monday-to-Friday daily rule reads `agrees=True`. Your test's contradicted case must therefore use a real contradiction (a
  name carrying `daily` on `rate(15 minutes)`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- holes removed by relabelling them (REFUSED is only the cross-firm class and is counted on the last line; UNDECIDED stays HOLE; the seven counts sum to the scope's count); a weekday rule still finished as daily (rule 2; a test case); a hole forced to zero to pass AC2 (the face says a failing AC2 is a correct outcome); BLIND: names of the root that live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE8-AC1 base PASS at the base (the round-1 test; it must still pass after the build, with the new cases); BE8-AC2 base FAIL as expected (ran at the cut: hole=16).
