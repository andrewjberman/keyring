# TO-AR-tf-75 -- FWD-4 read: how a seat drives each failed hop ON PURPOSE (AR-tf-75, round 54, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tf-75</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~233</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>54</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tf-75` (`decompositions/IRPT_ANLREQ_DECOMP_R54_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-tf-75`: "how a seat drives each failed hop on purpose." FWD-4's DONE WHEN (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` lines 59 to 63): the generator down, the commentary refused, the attach refused; each failure is DRIVEN on purpose and the ticket names the step and what happens next. The rule of this fabric is that no outcome is a wait: every outcome must be provable by an act a seat can take on demand, the organic case kept as the negative arm. The CTO ruled the design (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`; org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md row C-HOP-FAILURE): the silent hops write one set-once `hop_failure` = `{hop, code, at}` on the job row, `irpt-status` returns the code with its words, and the ticket page reads it. Before the release, the exercise itself must be designed. A READ cell: you write one record and edit no source.

**What to do.** For EACH of these failures, one or more rows saying HOW a seat could cause exactly that failure on the DEV estate on demand, using only the repository: (a) the ready-signal send fails (`READY_SIGNAL_SEND_FAILED`); (b) the commentary draft is refused (`COMMENTARY_DRAFT_REFUSED`) and failed (`COMMENTARY_DRAFT_FAILED`); (c) the packager refuses (`PACKAGER_REFUSED`) and fails (`PACKAGER_FAILED`); (d) the generator is down, meaning the resident does not take the job (an existing path: the job waits, no `hop_failure` is written, the status route reads the phase). Start from the round-45 per-hop map `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~213/FWD4_PER_HOP_FAILURE_MAP.md` (hops 6 to 14 and their cited lines) and the code it cites in `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`, `ycharts/research/opal_packager.py`, `data/transcripts/scripts/commentary/lambda_handler.py` and the draft store `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py`. For every row say, in the evidence cell: the code line that decides the failure (cite it), the cheapest input or configuration a seat would change to trigger it (an invalid body, an unbound principal, a tenant outside an allow-list, a queue URL left unset, a closed code the packager already refuses, a stopped service), whether that change is a repository-only act (a test double, an offline harness) or needs a LIVE act on DEV (then say which live resource and that it is a WORLD act for a CloudOps seat under a pair, and how it is put back), and what the status route would read afterwards. Use the verdict `ADMITS` for a failure a seat CAN drive with the stated act, `NOT-APPLICABLE` where the failure cannot be driven without damaging live data (say why), `UNREAD` only with the reason. Do not propose an alarm, a monitor or a notification.

**The record** (write it at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~233/FWD4_DRIVE_ON_PURPOSE_MAP.md`, relative to your worktree root): a markdown table with exactly these four columns, one row per failure-and-trigger, plus one line `DENOMINATOR: <n> <what you enumerated and how>` where `<n>` equals the number of table rows. At least 8 rows.

| surface | path:line | verdict | evidence |
|---|---|---|---|
| the failure and the trigger, named so a person can find it | `repo/relative/path.py:123`, no drive letter, a line inside the file | one of `REFUSES-TESTED`, `REFUSES-UNTESTED`, `ADMITS`, `SURFACES-ON-TICKET`, `SILENT`, `NOT-APPLICABLE`, `UNREAD` | a short quote in backticks that occurs within 5 lines of the cited line, then the trigger, repository-only or live, and what the status route reads |

After the table, a short prose section: which failures a seat can prove offline today, which need a live act, and the smallest live act per hop. Cite the line of the CODE that decides, not a comment. No secret, token, personal or client data.

### ACCEPTANCE

<criterion id="AR75-tf-AC1" cell_refs="AR-tf-75"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R45_CHECKS/r45_checks.py rec org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~233/FWD4_DRIVE_ON_PURPOSE_MAP.md 8</invocation><expect>R45-REC-OK</expect></criterion>
`AR75-tf-AC1` -- every citation is a real line, every quote occurs within 5 lines of it, the denominator equals the rows, every verdict is in the closed set, and there are at least 8 rows. Dry-run at box/dell2 6ddf55422c: `R45-org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~233/FWD4_DRIVE_ON_PURPOSE_MAP.md-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR75-tf-AC1</expected_criteria>

## BOUNDS

- **Grant.** Your record, this order's file, your deliverables folder, the surprise channel. You edit NO source file and NO test.
- **No network, no AWS, no secret, no deploy.** Read the repository only.
- **Refusal clause.** If a folder is outside your cone, file a `BLOCKING` surprise row naming it and stop on that part; an unread path is a row with verdict `UNREAD`.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your record lives in your deliverables folder, granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R54_TX.md</decomp_doc> (round 54, workstream ~TX), cell `AR-tf-75`.
<owned_cells>AR-tf-75</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR75-tf-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~233/IRPT_ANLREQ.TO-AR-tf-75.fwd4-drive-on-purpose-map.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR75-tf-AC1` BEFORE the flip. Commit the record first, then pin.
</proof_of_spec>

**REPORT:** the record's path, the denominator line, the count of rows by verdict, which failures are offline-provable and which need a live act, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read cell; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: proposing a trigger that damages live data or needs a secret; a quote that does not sit at the cited line; calling a failure drivable when the code path needs a state the trigger cannot reach; confusing the generator being down (no hop_failure, the phase is read) with a written failure.
</preflight>

- Free work around the release block: FWD-4's DONE WHEN is an exercise, and the exercise needs a design before the release. Risk LOCAL: a record only.
- Base: `AR75-tf-AC1` FAIL as expected (`R45-org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~233/FWD4_DRIVE_ON_PURPOSE_MAP.md-FAIL absent`) at box/dell2 6ddf55422c.
