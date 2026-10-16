# TO-AR-tz-65 -- FWD-5 read: classify every OPAL_GLOBAL equality site under infra/aws/lambda (AR-tz-65, round 50, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-65</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~229</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>50</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-65` (`decompositions/IRPT_ANLREQ_DECOMP_R50_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-tz-65`: "classify every OPAL_GLOBAL equality site under infra/aws/lambda." A READ cell: you write one record and edit no source. The global-admissions gate built in round 47 (test `infra/aws/lambda/ticket_center/tests/test_cross_firm_global_register.py`) scans only two files for the test `principal_class == "OPAL_GLOBAL"`, while the same test appears at 21 sites in 12 non-test files (the round-47 worker's surprise row `IRPT_ANLREQ-D2-W224-S1`). Before the gate is widened, each site must be classified: does it ADMIT an OPAL_GLOBAL principal to a record BEFORE a firm comparison (a global admission that needs a row in the register), or is it something else (an attribution flag, a census flag, a label, a display choice, a refusal of OPAL_GLOBAL).

**What to do.** (1) Enumerate every non-test site under `infra/aws/lambda` where a `principal_class` (or `principal["principal_class"]`, `.get("principal_class")`, `current["principal_class"]`) is compared with `==` or `in` against `OPAL_GLOBAL`. Use the native Grep tool over `infra/aws/lambda` excluding every `tests/` folder, then READ each site's function, and print how you enumerated in the DENOMINATOR line (the count of sites and files). (2) One table row per site, in the record format below. Verdict `ADMITS` = the site lets an OPAL_GLOBAL principal read or write a record without comparing the principal's firm to the record's firm first (a global admission); `NOT-APPLICABLE` = anything else, with the reason in the evidence cell (what the site does with the flag); `UNREAD` only with the reason. The register of admissions already known is `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_GLOBAL_ADMISSIONS_REGISTER.md` (rows G1 to G3: `_scope/interactive_access.py` and `reports/resident_installed.py`); mark in the evidence cell whether an ADMITS site is already a register row. (3) After the table, a short prose section: how many ADMITS sites are NOT in the register (those are findings for `2.0.0_SA_COO~V2`, not fixes for you).

**The record** (write it at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~229/OPAL_GLOBAL_SITES_CLASSIFIED.md`, relative to your worktree root): a markdown table with exactly these four columns, one row per site, plus one line `DENOMINATOR: <n> <what you enumerated and how>` where `<n>` equals the number of table rows.

| surface | path:line | verdict | evidence |
|---|---|---|---|
| the function and what it guards, named so a person can find it | `repo/relative/path.py:123`, no drive letter, a line inside the file | one of `REFUSES-TESTED`, `REFUSES-UNTESTED`, `ADMITS`, `SURFACES-ON-TICKET`, `SILENT`, `NOT-APPLICABLE`, `UNREAD` | a short quote in backticks that occurs within 5 lines of the cited line, then what the site does |

Rules: cite the line of the CODE that decides, not a comment. Do not paste secrets, tokens, personal or client data.

### ACCEPTANCE

<criterion id="AR65-tz-AC1" cell_refs="AR-tz-65"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R45_CHECKS/r45_checks.py rec org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~229/OPAL_GLOBAL_SITES_CLASSIFIED.md 15</invocation><expect>R45-REC-OK</expect></criterion>
`AR65-tz-AC1` -- every citation is a real line, every quote occurs within 5 lines of it, the denominator equals the rows, every verdict is in the closed set, and there are at least 15 rows. Dry-run at box/dell2 180edd9dd0: `R45-REC-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR65-tz-AC1</expected_criteria>

## BOUNDS

- **Grant.** Your record, this order's file, your deliverables folder, the surprise channel. You edit NO source file and NO test.
- **No network, no AWS, no secret, no deploy.** Read the repository only.
- **Refusal clause.** If a folder is outside your cone, file a `BLOCKING` surprise row naming it and stop on that part; an unread site is a row with verdict `UNREAD`.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R45_CHECKS/r45_checks.py rec org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~229/OPAL_GLOBAL_SITES_CLASSIFIED.md 15ESTIGATION_v1.md
</paths>

The block is your WRITE grant (your record lives in your deliverables folder, granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R50_TX.md</decomp_doc> (round 50, workstream ~TX), cell `AR-tz-65`.
<owned_cells>AR-tz-65</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR65-tz-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~229/IRPT_ANLREQ.TO-AR-tz-65.fwd5-opal-global-sites-classified.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR65-tz-AC1` BEFORE the flip. Commit the record first, then pin.
</proof_of_spec>

**REPORT:** the record's path, the denominator line, the count of rows by verdict, the ADMITS sites not in the register, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read cell; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: counting a line that merely mentions OPAL_GLOBAL in a comment; classifying a site by its name instead of reading what it does before the firm comparison; a quote that does not sit at the cited line.
</preflight>

- Disarms (with the build cell of round 50) the issuer-owned ARMED row `IRPT_ANLREQ-D2-W224-S1`. Risk LOCAL: a record only.
- Base: `AR65-tz-AC1` FAIL as expected (`R45-REC-FAIL absent`) at box/dell2 180edd9dd0, run by the issuer before the cut.
