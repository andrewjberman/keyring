# TO IRPT_DASHBD.TO-DB-b-146 -- the shared code table's class for the one "Other Fee" row, printed beside the method's rule: agreement closes the row, disagreement is a row against the table

<to_id>IRPT_DASHBD.TO-DB-b-146</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~119</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-76 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_76_20261011.md` @d70feb6d15, item 3, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v32.md` @305103f259 | **Rows:** IRPT_DASHBD-D2-W113-S3, IRPT_DASHBD-D2-W115-S1 | **Decomp cell:** `DB-b-146` (decomposition section 79) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-142 (drained @fc42bbcab0).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-119` (branch `wk-irpt-dashbd-77-119`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~119/`. Read first: the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v32.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why.** On ONE of the 235 flow days of the 51 contested segments, the custodian's ledger carries an "Other Fee" expense row that the
served flow does not count. DB-b-142 classed it by the method's rule: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` line 706 keeps a FEE-ADMIN expense
inside the return, and lines 713-717 build the flow set without it. But that worker took FEE-ADMIN from the rule's text, not from the
row's own code: the feed's transaction code for that row and the shared code table's class for it were outside its read (row
W115-S1). The CTO: "One read closes it. The shared code table's class for that one fee row, printed beside the method's rule the
reviewer confirmed. Agreement closes the row; disagreement comes back as a row against the table, not the method."

**The cell (`DB-b-146`).** Read-only.
1. **How the producer classes a transaction.** Read `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` around lines 536-552 and 700-732: which input carries
   a transaction's code, which table or mapping turns a code into a class (EXTERNAL, FEE-MANAGEMENT, FEE-ADMIN, ...), and where that
   table lives (a file in the repo, or a served table). `table` {file or address, how_read (file and line of the producer's read)}.
2. **The one row.** From ~115's private table (`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~115/`) take the account and day of the
   not-reproduced flow day; read the feed's row or rows for that account and day with the narrow projection; find the one that is the
   "Other Fee" expense (by its type and its position among that day's rows, not by its amount written anywhere); take its code.
   `row_class`: the class the code table gives that code. If the feed has no such row, or two candidates you cannot tell apart
   without an amount, or a read is denied: `row_class: "NOT_ESTABLISHED"`, `agree: "NOT_ESTABLISHED"`, `why`.
3. **Beside the method's rule.** `method_rule` {file, line, quote}: the line that says what the method does with that class.
   `agree`: true if the table's class is one the method keeps inside the return (so the served flow rightly omits it); false if the
   table classes it as a flow the method counts (then the served flow is missing a flow on that day: file a row AGAINST THE TABLE or
   the served number as the evidence shows, with the class names, and name it in `row`).
4. `client_figures: 0`, `s3_writes: 0`. Class names, code VALUES only if they are short category codes and not account numbers, file
   and line quotes: no account id, no client name, no amount. The check refuses a record holding any run of 8 or more digits. Private
   files go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~119/`. Record `FEE_ROW_CLASS.json`.

<criterion id="DB77-2-AC1" cell_refs="DB-b-146"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r77/p77_round77.py" . DB77-2-AC1</invocation><expect>DB77-2-AC1 PASS</expect></criterion>
`DB77-2-AC1` -- the shared code table's class for the one fee row is read and set beside the method's rule cited from the code, and they are said to agree, to disagree with a row, or not to be established. Base: FAIL.

<expected_criteria>DB77-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: for the ONE account and day worker ~115 identified (read from its private table, never written into the repo), the custodian feed's transaction row or rows the served flow is built from (the producer's `fact_trn` input: its address from the producer's own code), with a projection of the transaction code and type columns and the date; and the shared code table that classes a transaction code (its address from the producer's code). No other account, no other day, no other firm. A denial is recorded verbatim, not retried by another route, and the class reads NOT_ESTABLISHED.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~119/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W119-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~119/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-146.fee-row-class-in-the-code-table.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 79 (round 77), cell `DB-b-146`.
<owned_cells>DB-b-146</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB77-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~119/IRPT_DASHBD.TO-DB-b-146.fee-row-class-in-the-code-table.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB77-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how the code table is read by the producer (file and line); the class it gives that fee row's code (the class name, not an amount); the method's rule quoted with file and line; whether they agree; what you could not read; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one narrow read of one firm's feed for one day and of a code table; nothing served, nothing written but a record.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
