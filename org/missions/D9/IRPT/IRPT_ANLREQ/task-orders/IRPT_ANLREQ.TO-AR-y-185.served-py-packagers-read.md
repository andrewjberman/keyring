# TO IRPT_ANLREQ.TO-AR-y-185.served-py-packagers-read -- the eight functions that package served.py, their pins and whether their tests see the status rule

<to_id>IRPT_ANLREQ.TO-AR-y-185</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-185` (`decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-185`, inlined) -- READ. Nothing is changed or called.

*Which functions package `served.py`, how, at what pin, and whether their tests run the pinned or the live file.* The CTO's census of `lambda-source-map.json` (235 functions) found 8; this cell re-reads it and adds what the pair needs.

**Read first:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_18_20261012.md` section 1 row D2-W54-S5, `infra/aws/lambda/ci/lambda-source-map.json`, the status rule at the shared tree head (`_authz/served.py` lines about 1157-1161, drained @0724e8a1ff) and the round-17 compile `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md` section 2 (`AR-y-172`).
The eight functions the CTO named: `irpt-performance-adapter`, `irpt-directory-search`, `irpt-narrative`, `irpt-ycharts-generate`, `irpt-export-render`, `irpt-holdings`, `irpt-status`, `irpt-49f-reporting-read-lambda`.

1. **Re-count** from the map: how many of the 235 functions package `served.py` (by member, glob or folder; say the rule you used and show a positive control and one negative control). If your count is not 8, name the difference.
2. **For each of the eight:** the map entry (members), `pin` (the source commit the map pins it at), `how_it_packages_served_py` (member name or folder), whether the pinned `served.py` blob EQUALS the head blob (`git show <pin>:<path>` hashed against head), `carries_status_rule` (true only if the pinned file holds the AR-y-172 rule), and `tests_run_against` (`pinned` or `live`: which `served.py` the function's own tests import; read the test folders and say what you read).
3. **Write `r18/SERVED_PY_PACKAGERS.json`:** `functions` (a list of eight objects with `function`, `pin`, `how_it_packages_served_py`, `carries_status_rule`, `tests_run_against`, `map_entry`), `map_denominator` (the count of functions scanned), `claim`, `not_read`, and `what_moves_together` (one paragraph: what must ship together for one internal caller to get one answer from all eight). A function whose pin you cannot read is named in `not_read`, never guessed.
4. **In your report:** the count and the rule, which functions' tests would not see the status rule, and what the pair must name.

### ACCEPTANCE

<criterion id="AR185-y-AC1" cell_refs="AR-y-185"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y185-read --root C:/dev/wk-irpt-anlreq-51</invocation><expect>Y185-READ-OK</expect></criterion>
`AR185-y-AC1`: the record names each of the eight functions with its pin and how it packages `served.py`, and states the map denominator, the claim and what was not read.

<criterion id="AR185-y-AC2J" cell_refs="AR-y-185" judgment="true"/>
`AR185-y-AC2J` (judgment, graded at L9, never by you): the count of packagers is measured with a positive and a negative control, each pin was read rather than assumed, and `tests_run_against` was read from the tests.

<expected_criteria>AR185-y-AC1 AR185-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md</decomp_doc>
<owned_cells>AR-y-185</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-185.served-py-packagers-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-185`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of the repository; nothing is changed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's census (8 of 235) against the cell; the lens: a count by one membership rule that misses a packager the rule does not see. The order requires a positive control and a negative control for the rule and the difference named.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-18 analysis item 4 (row D2-W54-S5: the status rule ships to every function that packages `served.py`, together, or the pair names each that stays). Base: `AR185-y-AC1` FAIL as expected (no record).
