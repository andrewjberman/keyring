# TO-AR-t-32 -- the commentary Lambda's module logger emits INFO, so the COMMENTARY-POST line reaches CloudWatch (AR-t-32, round 42, workstream T, direct act)

<to_id>IRPT_ANLREQ.TO-AR-t-32</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~191</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>42</round>
<workstream>~T</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~T (commentary) | **Decomp cell:** `AR-t-32` (`decompositions/IRPT_ANLREQ_DECOMP_R42_T.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-t-32`: "`lambda_handler.py` sets its module logger to INFO at import, so its INFO lines (`COMMENTARY-POST`, `commentary draft stored`) reach the platform handler; a new test file proves it WITHOUT any test-side level override and proves the POST line is emitted at the module's own level. Fakes only."

Work in your worktree; every path is relative to its root. `data/transcripts/scripts/commentary/lambda_handler.py:57` defines `LOG = logging.getLogger(__name__)` and logs `COMMENTARY-POST request_id=%s outcome=%s status=%s code=%s` at INFO on the queue path. Nothing sets a level; in the AWS Lambda Python runtime the root logger is WARNING, so INFO records from this logger are dropped and the line never reaches CloudWatch (measured: one live run at 17:00:52Z logged no application line). `data/transcripts/scripts/tests/test_commentary_route_switch.py:47-52` hides this because its `_run` wraps the call in `caplog.at_level(logging.INFO, logger=lh.LOG.name)`.

**Build:**
1. In `lambda_handler.py`, directly after the `LOG = ...` line, set that logger's own level to INFO (`LOG.setLevel(logging.INFO)`), with a one-line comment saying why (the runtime's root level drops INFO). Change nothing else in the file.
2. `data/transcripts/scripts/tests/test_commentary_logging.py` (new, fakes only, no network), exactly two tests:
   - `test_module_logger_emits_info_without_any_test_side_override`: imports the module the way `test_commentary_route_switch.py` does, and asserts `lh.LOG.isEnabledFor(logging.INFO)` is True with the root logger left at WARNING (set it to WARNING in the test and restore it) and with NO `caplog.at_level` and no `setLevel` call in the test.
   - `test_post_line_is_emitted_at_the_modules_own_level`: runs the same fake queue path the `_run` helper in `test_commentary_route_switch.py` builds (reuse its fakes; import the helper or copy its fake ports, your choice), root logger at WARNING, and asserts one `COMMENTARY-POST request_id=<id> outcome=POSTED status=200 code=-` record is captured by a handler you attach to `lh.LOG` yourself (a `logging.Handler` subclass that appends `getMessage()`), not by `caplog.at_level`.
   Keep every existing `test_commentary_*.py` green.

### ACCEPTANCE

<criterion id="AR32-t-AC1" cell_refs="AR-t-32"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R42_CHECKS/r42_checks.py lg1</invocation><expect>R42-LG1-OK</expect></criterion>
`AR32-t-AC1` -- both named tests pass. Dry-run at box/dell2 b1ad686188: `R42-LG1-FAIL absent` -- FAIL as expected.

<expected_criteria>AR32-t-AC1</expected_criteria>

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **No network, no AWS, no secret.** You deploy nothing; the packaged copy under `infra/aws/lambda/transcripts-pull/dist/` is build output and is not yours.
- **Refusal clause.** If `lambda_handler.py` already sets a level at your base, or the helper in `test_commentary_route_switch.py` cannot be reused, keep to the two test names and the one-line fix, file a surprise row (`IRPT_ANLREQ-D2-W191-S<k>`, next unused under `surprise-channel/`) and say so in the report. Write no code outside the paths below.
- **Your worktree is sparse.** If an import fails for a missing folder, that is a row (`BLOCKING`), not a reason to stub: name the folder in the row.

<paths>
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/tests/test_commentary_logging.py
data/transcripts/scripts/tests/test_commentary_route_switch.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R42_T.md</decomp_doc> (round 42, workstream T), cell `AR-t-32`.
<owned_cells>AR-t-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR32-t-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~191/IRPT_ANLREQ.TO-AR-t-32.commentary-logger-level.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR32-t-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the one-line change, the two test names, the check line, commits.

---

<preflight>
comp-blast: RUN (by reading) -- `lambda_handler.py` is imported by the packaged copy under `infra/aws/lambda/transcripts-pull/dist/` (build output, not edited) and by the commentary tests; the change adds a logger level and removes nothing. Nothing is deployed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change; fakes only.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage cc9b86edcd: the neighborhood is the decomposition only, 0 unproven dependencies, the two flagged paths are this order's own outputs (absent until built). Traps named for the worker: a test that sets the level for itself and so cannot fail; a handler attached to the root logger instead of `lh.LOG`; a fix applied to `entry.py` instead of the module that logs the POST line.
</preflight>

- Cut on the issuer's own measured read (decomposition R42_T): the live run at 17:00:52Z, `~Y2` msg 8551, the draft store's `get_ref`. Risk LOCAL, direct act (about 20 product lines).
- Base: `AR32-t-AC1` FAIL as expected (`R42-LG1-FAIL absent`) at box/dell2 b1ad686188, run by the issuer before the cut.
