# TO-AR-ty-57 -- FWD-4 design read: the ticket service's service-principal write routes and what the portal shows (AR-ty-57, round 46, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-ty-57</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~220</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>46</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-ty-57` (`decompositions/IRPT_ANLREQ_DECOMP_R46_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-ty-57`: "FWD-4 design read: which ticket routes a service principal can write, with what fields, and what the portal shows." A READ cell: you write one record and edit no source. Round 45 mapped the failure of each hop of the FWD-1 chain (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~213/FWD4_PER_HOP_FAILURE_MAP.md`): 24 hops are SILENT because no code writes a failure note on the ticket. The commentary function (principal `svc-commentary`) is admitted only to the route `commentary-draft`; the resident and the packager have their own principals. Round 46 needs to know whether a failure note could ride a route that already exists, or needs a new ticket-service route (a design question the CTO owns), before anything is built. No alarm, monitor or notification is proposed: a failure note on the ticket is a field a person reads on the ticket.

**What to do.** In `infra/aws/lambda/ticket_center/lambda_function.py` (and its tests under `infra/aws/lambda/ticket_center/tests/`), enumerate EVERY route or operation that a SERVICE principal (a caller that is not a staff or client user: `svc-commentary`, `svc-irpt-packager`, `svc-analyst-intake`, the resident's principal, any other `svc-*` the service names) is admitted to write. Print how you enumerated in the DENOMINATOR line. One row per route and service principal: the line of the admission, and the verdict:
- `ADMITS` the principal may call it; say in the evidence cell the FIELDS it writes on the ticket (quote one);
- `SURFACES-ON-TICKET` the field it writes is displayed on the ticket page (cite the portal file and line in the evidence cell, quote it);
- `SILENT` the field is stored but the portal does not display it;
- `NOT-APPLICABLE` / `UNREAD` as honest answers.
Then add rows (verdict `NOT-APPLICABLE` or `UNREAD` where you cannot decide) answering in their evidence cells: (a) is there any existing free-text or status field on an analysis-request ticket that a service principal may write and the page shows (a status, a note, an activity entry); (b) which of the FWD-1 hops in the round-45 record (hops 6 to 14) already holds a principal that could write it. Cite the code; do not propose a build.

**The record** (write it at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~220/FWD4_TICKET_WRITE_ROUTES_MAP.md`, relative to your worktree root): a markdown table with exactly these four columns, one row per item, plus one line `DENOMINATOR: <n> <what you enumerated and how>` where `<n>` equals the number of table rows.

| surface | path:line | verdict | evidence |
|---|---|---|---|
| the route and principal, named so a person can find it | `repo/relative/path.py:123`, no drive letter, a line inside the file | one of `REFUSES-TESTED`, `REFUSES-UNTESTED`, `ADMITS`, `SURFACES-ON-TICKET`, `SILENT`, `NOT-APPLICABLE`, `UNREAD` | a short quote in backticks that occurs within 5 lines of the cited line, then what it shows |

Rules: cite the line of the CODE that decides, not a comment or a doc. `UNREAD` is a legal verdict for anything you did not open, with the reason in the evidence cell. Do not paste secrets, tokens, personal or client data.

### ACCEPTANCE

<criterion id="AR57-ty-AC1" cell_refs="AR-ty-57"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R45_CHECKS/r45_checks.py rec org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~220/FWD4_TICKET_WRITE_ROUTES_MAP.md 6</invocation><expect>R45-REC-OK</expect></criterion>
`AR57-ty-AC1` -- every citation is a real line, every quote occurs within 5 lines of it, the denominator equals the rows, every verdict is in the closed set, and there are at least 6 rows. Dry-run at box/dell2 39eef25c48: `R45-REC-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR57-ty-AC1</expected_criteria>

## BOUNDS

- **Grant.** Your record, this order's file, your deliverables folder. You edit NO source file and NO test.
- **No network, no AWS, no secret, no deploy.** Read the repository only.
- **Refusal clause.** If a surface named above does not exist at your base, say so as a row with verdict `UNREAD` and the reason; if the cone lacks a folder, file a `BLOCKING` surprise row naming it.
- **No proposals of alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your record lives in your deliverables folder, granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R46_TX.md</decomp_doc> (round 46, workstream ~TX), cell `AR-ty-57`.
<owned_cells>AR-ty-57</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR57-ty-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~220/IRPT_ANLREQ.TO-AR-ty-57.fwd4-ticket-write-routes-map.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR57-ty-AC1` BEFORE the flip. Commit the record first, then pin.
</proof_of_spec>

**REPORT:** the record's path, the denominator line, the count of rows by verdict, anything you could not enumerate, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read cell; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage c39947a0a2: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates (the new test file(s) or record, and the proof instance). Traps named for the worker: a test that mocks the very guard it claims to prove; a lookup that misses before the firm binding is reached, which proves nothing about the binding; a test that passes with the guard removed; a cited line that is a comment instead of the code that decides.
</preflight>

- Cut on the CTO's Move 2 (msg 8742): FWD-4 "as gates and owned rows, never a new alarm". Risk LOCAL: a record only.
- Base: `AR57-ty-AC1` FAIL as expected at box/dell2 39eef25c48.
