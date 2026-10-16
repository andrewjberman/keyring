# TO-AR-tx-44 -- FWD-4 map: what each hop's failure does today and whether the ticket says so (AR-tx-44, round 45, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tx-44</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~213</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>45</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tx-44` (`decompositions/IRPT_ANLREQ_DECOMP_R45_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-tx-44`: "FWD-4 map: what each hop's failure does today and whether the ticket says so." A READ cell: you write one record and edit no source. The record is a cited-line table that a script checks, so every claim is a place in the repository.

**Surface:** the hops of the FWD-1 chain, from the hop map `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/trace/FWD1_HOP_MAP.md` (20-odd hops from the form to the package on the ticket) and the code that runs each hop.

**What to do.** For EVERY hop in the hop map, one row: the line of the code that handles that hop's failure (a refusal, an exception handler, a dead-letter, a status write), what it does (the ticket gains a failure note: SURFACES-ON-TICKET; a log or a queue only: SILENT; the request just stops: SILENT; the hop refuses with a closed reason that a person can read on the ticket: SURFACES-ON-TICKET), and the test that exercises that failure (cite) in the evidence cell if one exists. State the hop number in the surface cell. Do NOT propose an alarm, a monitor or a notification; the standing moratorium forbids building one. Where the answer is that the failure is only a gate or an owned row, say so in the evidence cell.

**Where to start:** the hop map above, `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md:59-63` (FWD-4's DONE WHEN: 'the generator down, the commentary refused, the attach refused'), `data/transcripts/scripts/commentary/lambda_handler.py` (the COMMENTARY-POST outcomes `POSTED`, `ALREADY_SET`, `REFUSED`, `FAILED`, `NO_TICKET`), and the resident's packaging refusal rows.

**The record** (write it at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~213/FWD4_PER_HOP_FAILURE_MAP.md`, relative to your worktree root): a markdown table with exactly these four columns, one row per enumerated item, plus one line `DENOMINATOR: <n> <what you enumerated and how>` where `<n>` equals the number of table rows.

| surface | path:line | verdict | evidence |
|---|---|---|---|
| the route, hop or read path, named so a person can find it | `repo/relative/path.py:123`, no drive letter, a line inside the file | one of `REFUSES-TESTED`, `REFUSES-UNTESTED`, `ADMITS`, `SURFACES-ON-TICKET`, `SILENT`, `NOT-APPLICABLE`, `UNREAD` | a short quote in backticks that occurs within 5 lines of the cited line, then what it shows |

Rules: cite the line of the CODE that decides (the check, the handler, the write), not a comment or a doc. `UNREAD` is a legal verdict for anything you did not open, with the reason in the evidence cell: a row that says `UNREAD` is honest, a row that claims a read it did not make is a defect. Add a short prose section under the table naming anything you could not enumerate and why. Do not paste secrets, tokens, personal or client data.

### ACCEPTANCE

<criterion id="AR44-tx-AC1" cell_refs="AR-tx-44"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R45_CHECKS/r45_checks.py rec org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~213/FWD4_PER_HOP_FAILURE_MAP.md 10</invocation><expect>R45-REC-OK</expect></criterion>
`AR44-tx-AC1` -- the record's citations and quotes check out against the repository, the denominator equals the rows, every verdict is in the closed set, and there are at least 10 rows. Dry-run at box/dell2 b1ad686188: `R45-REC-FAIL absent: ...` -- FAIL as expected. The checker's own `--self-test` (green record plus four mutants refused) reads `R45-SELFTEST-OK`.

<expected_criteria>AR44-tx-AC1</expected_criteria>

## BOUNDS

- **Grant.** Your record, this order's file, your deliverables folder. You edit NO source file and NO test.
- **No network, no AWS, no secret, no deploy.** Read the repository only.
- **Refusal clause.** If a surface named above does not exist at your base, say so as a row with verdict `UNREAD` and the reason, and file no stub. If the cone of your worktree lacks a folder you need, file a `BLOCKING` surprise row naming the folder (`IRPT_ANLREQ-D2-W213-S<k>`, next unused under `surprise-channel/`); do not guess.
- **No proposals of alarms, monitors or notifications.** A finding is a row in the table.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention, and your record lives there). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R45_TX.md</decomp_doc> (round 45, workstream ~TX), cell `AR-tx-44`.
<owned_cells>AR-tx-44</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR44-tx-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~213/IRPT_ANLREQ.TO-AR-tx-44.fwd4-per-hop-failure-surfacing-map.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR44-tx-AC1` BEFORE the flip. Commit the record first, then pin.
</proof_of_spec>

**REPORT:** the record's path, the denominator line, the count of rows by verdict, anything you could not enumerate, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read cell; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage 8f17f7b84b: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: a citation to a doc or comment instead of the code that decides; a quote that does not sit at the cited line; a test counted as proof that mocks the very check it claims to prove; a claimed read that was not made.
</preflight>

- Cut on the CTO's parallelization ruling, Move 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, msg 8742): `2.0.0_SA_COO~T2` takes IRPT_ANLREQ FWD-4. Risk LOCAL: a record only.
- Base: `AR44-tx-AC1` FAIL as expected (`R45-REC-FAIL absent`) at box/dell2 b1ad686188, run by the issuer before the cut.
