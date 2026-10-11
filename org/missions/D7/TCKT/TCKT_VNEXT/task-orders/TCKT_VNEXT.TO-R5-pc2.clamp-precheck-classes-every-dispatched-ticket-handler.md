# TO TCKT_VNEXT.TO-R5-pc2 -- the clamp precheck lists every ticket handler the deployed code dispatches, each with a class

<to_id>TCKT_VNEXT.TO-R5-pc2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~24</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>PC</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R5-pc-2` (`decompositions/TCKT_VNEXT_DECOMP_R5.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~24`. Your worktree is `C:/tmp/tckt-r5-24` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~24 <0.9.0_WK_TCKT_VNEXT~24@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/clamp_precheck/clamp_precheck.py` (tests beside it, `test_clamp_precheck.py`, 16 passing) is run before every live act on the ticket
service. It downloads the deployed package, checks it against the source map and the recorded commit, and prints one line
per host and a totals line `READ27 <clamped>/<total>` over a FROZEN list of 27 routes
(`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json`). For the ticket host it proves that
seven named handlers (`HANDLERS`, line 45) call a firm-clamp helper. The ticket service now dispatches MORE handlers than
those seven (a package route, two commentary routes, a submit route), and `READ27 27/27` says nothing about them: it is true
of its 27 and silent about the rest. A reader of that line takes it for the whole service.

### THE CELL `R5-pc-2`

Add a SECOND read to the precheck, beside the first. **The `READ27` line, the per-host lines and the existing table rows must
stay byte-identical for the same inputs** (other tools and orders match that line).

1. From the DEPLOYED ticket member (the bytes the precheck already downloads; never the tree), find every handler function
   that `lambda_handler` dispatches to: walk `lambda_handler`'s body with `ast` and collect the names of module-level
   functions it calls whose result it returns. That list is the denominator; do not type a list of handlers.
2. Give each dispatched handler exactly ONE class, decided from that handler's own source in the deployed member:
   - `PROFILE_SCOPE`: it calls one of `CLAMP_HELPERS` or `CLAMP_WRAPPERS` (directly; the existing `_called_names` helper is
     the pattern);
   - `ENV_FIRM_LIST`: it reads a module constant whose name ends `_ALLOWED_FIRMS` and compares a firm against it;
   - `SUBMIT_CONTEXT_FIRM`: it is the submit handler, whose firm comes from the authorizer context (read the deployed
     member to see how `submit` derives the firm; class it by the code, and say in your report which lines decide it);
   - `UNCLASSED`: none of the above.
   A handler may satisfy more than one rule; report the FIRST in the order above and list the others in the table row.
3. Print, AFTER the existing lines, one line per dispatched handler (`handler <name> <CLASS>`) and one totals line
   `TICKET_HANDLERS <classed>/<dispatched>`. Add the rows to the JSON table under a NEW top-level key `ticket_handlers`
   (the existing keys and rows unchanged).
4. Exit code: unchanged when every dispatched handler is classed. If ANY dispatched handler is `UNCLASSED`, the exit code is
   non-zero even when `READ27` is full, and the line says which handler.
5. No AWS call and no network call in tests: the tests use the file's existing fakes for the package and the source map.
   Never run `clamp_precheck.py` itself against live AWS. No non-ASCII. No change outside `<paths>`.

### ACCEPTANCE

<criterion id="R5-pc2-AC1" cell_refs="R5-pc-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py pc2-classes</invocation><expect>PC2-CLASSES-OK</expect></criterion>
`R5-pc2-AC1`: these tests exist in `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/clamp_precheck/test_clamp_precheck.py` and pass:
`test_every_dispatched_ticket_handler_is_listed_with_a_class` (a fake deployed member whose `lambda_handler` dispatches N
handlers yields N rows), `test_a_handler_that_calls_a_clamp_helper_is_classed_profile_scope`,
`test_the_two_commentary_handlers_are_listed_and_classed` (use the REAL handler file from the worktree,
`infra/aws/lambda/ticket_center/lambda_function.py`, as the member's bytes: `commentary_draft_ticket` and
`commentary_sent_ticket` both appear with a class that is not `UNCLASSED`, and the test prints the class of every handler),
`test_a_dispatched_handler_with_no_class_makes_the_exit_nonzero`,
`test_the_read27_line_and_its_table_rows_are_unchanged` (same inputs, the old line and rows byte-equal).

<criterion id="R5-pc2-AC2" cell_refs="R5-pc-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py pc2-regress</invocation><expect>PC2-REGRESS-OK</expect></criterion>
`R5-pc2-AC2`: the whole precheck test file passes (at least 21 passed, 0 failed: the 16 at the base plus the 5 new). No existing test changes.

<expected_criteria>R5-pc2-AC1 R5-pc2-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (missing tests) and AC2 FAIL (16 passed, below 21), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W24-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~24/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/clamp_precheck/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~24/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md</decomp_doc> (round 5), cell `R5-pc-2`.
<owned_cells>R5-pc-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R5-pc2-AC1 R5-pc2-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~24/TCKT_VNEXT.TO-R5-pc2.clamp-precheck-classes-every-dispatched-ticket-handler.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R5-pc2-AC1,R5-pc2-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commit, **the class the REAL handler file gives EVERY dispatched handler, as a list (name and
class), and any that came out UNCLASSED named FIRST**, the lines that decide the submit handler's class, the sha256 from
`git show HEAD:org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/clamp_precheck/clamp_precheck.py | sha256sum`, and any row ids. If the real handler file yields an UNCLASSED handler, do
NOT invent a class to make it pass: file ONE row, class BLOCKING, and report it.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arm is the test that a dispatched handler with no class fails the precheck even when READ27 is full.
</preflight>

Source: CTO msg 5932 ("Owed next, one cell: the clamp precheck's census names the two commentary routes with their class") and the applier's row TCKT_VNEXT-D2-S45 (the 27 is a frozen round-3 set). Workstream PC; same issuer. Decomposition `TCKT_VNEXT_DECOMP_R5.md` AMENDMENT 6.
