# TO-AR-tx-43 -- FWD-5 map: the front door and the portal, and what a seat-driven other-firm sign-in needs (AR-tx-43, round 45, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tx-43</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~212</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>45</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tx-43` (`decompositions/IRPT_ANLREQ_DECOMP_R45_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-tx-43`: "FWD-5 map: the front door and the portal, and what a seat-driven other-firm sign-in needs." A READ cell: you write one record and edit no source. The record is a cited-line table that a script checks, so every claim is a place in the repository.

**Surface:** the routes the browser calls for a ticket, its package files and the commentary through the front door (CloudFront and the API behind it) and the portal's own client code and tests under `portal/src/` (the Ticket Center page and its API endpoints), plus the existing run harness that signs in a synthetic staff principal for FWD-1 (the TO-RUN-FWD1 driver and mint helper named in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/`).

**What to do.** Enumerate the browser-reachable routes that return a ticket, a package file or the commentary, and for each the line where the signed-in user's firm is checked or SILENT, the existing test (cite) or REFUSES-UNTESTED. THEN answer in the same table, as rows with verdict `UNREAD` or `NOT-APPLICABLE` where you cannot decide, what a seat-driven exercise 'a sign-in at another firm tries the ticket and each package file and is refused' (PRD FWD-5 DONE WHEN) would need on DEV: the kinds of principal the harness can mint, whether a principal for a SECOND firm exists or could be minted by the same helper, and which routes the exercise would call. Cite the harness code for each claim.

**Where to start:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/` (search the FWD1 driver and mint helper by name: `TO-AR-y-345` is the driver-and-mint-helper build), `portal/src/api/endpoints/`, and the PRD lines `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md:65-68`.

**The record** (write it at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~212/FWD5_FRONT_DOOR_AND_PORTAL_MAP.md`, relative to your worktree root): a markdown table with exactly these four columns, one row per enumerated item, plus one line `DENOMINATOR: <n> <what you enumerated and how>` where `<n>` equals the number of table rows.

| surface | path:line | verdict | evidence |
|---|---|---|---|
| the route, hop or read path, named so a person can find it | `repo/relative/path.py:123`, no drive letter, a line inside the file | one of `REFUSES-TESTED`, `REFUSES-UNTESTED`, `ADMITS`, `SURFACES-ON-TICKET`, `SILENT`, `NOT-APPLICABLE`, `UNREAD` | a short quote in backticks that occurs within 5 lines of the cited line, then what it shows |

Rules: cite the line of the CODE that decides (the check, the handler, the write), not a comment or a doc. `UNREAD` is a legal verdict for anything you did not open, with the reason in the evidence cell: a row that says `UNREAD` is honest, a row that claims a read it did not make is a defect. Add a short prose section under the table naming anything you could not enumerate and why. Do not paste secrets, tokens, personal or client data.

### ACCEPTANCE

<criterion id="AR43-tx-AC1" cell_refs="AR-tx-43"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R45_CHECKS/r45_checks.py rec org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~212/FWD5_FRONT_DOOR_AND_PORTAL_MAP.md 5</invocation><expect>R45-REC-OK</expect></criterion>
`AR43-tx-AC1` -- the record's citations and quotes check out against the repository, the denominator equals the rows, every verdict is in the closed set, and there are at least 5 rows. Dry-run at box/dell2 b1ad686188: `R45-REC-FAIL absent: ...` -- FAIL as expected. The checker's own `--self-test` (green record plus four mutants refused) reads `R45-SELFTEST-OK`.

<expected_criteria>AR43-tx-AC1</expected_criteria>

## BOUNDS

- **Grant.** Your record, this order's file, your deliverables folder. You edit NO source file and NO test.
- **No network, no AWS, no secret, no deploy.** Read the repository only.
- **Refusal clause.** If a surface named above does not exist at your base, say so as a row with verdict `UNREAD` and the reason, and file no stub. If the cone of your worktree lacks a folder you need, file a `BLOCKING` surprise row naming the folder (`IRPT_ANLREQ-D2-W212-S<k>`, next unused under `surprise-channel/`); do not guess.
- **No proposals of alarms, monitors or notifications.** A finding is a row in the table.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention, and your record lives there). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R45_TX.md</decomp_doc> (round 45, workstream ~TX), cell `AR-tx-43`.
<owned_cells>AR-tx-43</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR43-tx-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~212/IRPT_ANLREQ.TO-AR-tx-43.fwd5-front-door-and-portal-firm-map.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR43-tx-AC1` BEFORE the flip. Commit the record first, then pin.
</proof_of_spec>

**REPORT:** the record's path, the denominator line, the count of rows by verdict, anything you could not enumerate, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read cell; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage 8f17f7b84b: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: a citation to a doc or comment instead of the code that decides; a quote that does not sit at the cited line; a test counted as proof that mocks the very check it claims to prove; a claimed read that was not made.
</preflight>

- Cut on the CTO's parallelization ruling, Move 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, msg 8742): `2.0.0_SA_COO~T2` takes IRPT_ANLREQ FWD-5. Risk LOCAL: a record only.
- Base: `AR43-tx-AC1` FAIL as expected (`R45-REC-FAIL absent`) at box/dell2 b1ad686188, run by the issuer before the cut.
