# TO IRPT_DASHBD.TO-DB-b-135 -- the 90 unclassed tie-out segments: the custodian's two-sided dollar read, classed by cause, counts only

<to_id>IRPT_DASHBD.TO-DB-b-135</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~108</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-69 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_69_20261011.md` @90cb3e774b, section 4 item 5, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` @595332678c | **Rows:** IRPT_DASHBD-D2-W104-S1 | **Decomp cell:** `DB-b-135` (decomposition section 72) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** none (it reads DB-b-129's membership, drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-108` (branch `wk-irpt-dashbd-70-108`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~108/`. Read first: section 3 (item 4) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is asked.** DB-b-129 classed 154 of the 244 UNEXPLAINED tie-out segments and left 90: their event dates agree, the day counts are
equal, the gap is above 0.35 percentage points, and no record in the tree names a cause (row W104-S1; record
`deliverables/0.9.0_WK_IRPT_DASHBD~104/UNEXPLAINED_244.json`). The CTO: "The custodian read that would class them is ordered as one
read-only cell, counts by cause."

**The cell (`DB-b-135`).** Read-only; you change no code and no served thing.
1. **Take the 90** from `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~104/membership.json` (outside the repo; read in place) and
   reproduce the count. A different count is a STOP with a row: the denominator is 90.
2. **The two-sided dollar read**, the shape the 74 restated segments got (the `W73_S1_EVIDENCE` shape; find it under
   `deliverables/0.9.0_WK_IRPT_DASHBD~73/` and the cells it cites): per segment, the custodian's beginning and ending value, net additions,
   net gains, fees and income against Opal's side for the same window. Read how reader ~35 reached the custodian tables
   (`deliverables/0.9.0_WK_IRPT_DASHBD~35/`) and reuse its reader; write no new reader where one exists. Everything you download or derive
   per segment stays under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`.
3. **Class each by cause**, each class with a RULE a reader could re-apply to the two sides' numbers (for example: the gap is the
   custodian's fee to within the tolerance; the two sides differ in the beginning value; income is counted on one side only). A cause is
   a property of the two sides' data, not a guess. Every one of the 90 lands in exactly one class or in the remainder.
   `UNCLASSED_90.json`: {denominator: 90, classes: [{cause, count, rule}], remainder {count, why}, s3_reads {prefixes, objects},
   read_denied (text, or null), client_figures: 0, s3_writes: 0}.
4. Counts only in the repo and in your report: no account id, no client name, no dollar amount of any account. The check refuses a
   record that holds any run of 8 or more digits.

<criterion id="DB70-5-AC1" cell_refs="DB-b-135"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r70/p70_round70.py" . DB70-5-AC1</invocation><expect>DB70-5-AC1 PASS</expect></criterion>
`DB70-5-AC1` -- the 90 unclassed segments are classed by cause from the custodian read with a stated rule per class, and the classes and the remainder sum to 90. Base: FAIL.

<expected_criteria>DB70-5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: 49 Financial's OWN Black Diamond tree as reader ~35 used it (the transactions prefix and the valuation tables that reader names; take every address from that reader's code or record, never typed), limited to the accounts and date windows of the 90 segments. No other firm's prefix, no other bucket. A denial is recorded verbatim, not retried by another route; the segments it blocks go to the remainder with that reason.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W108-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~108/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-135.unclassed-90-custodian-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 72 (round 70), cell `DB-b-135`.
<owned_cells>DB-b-135</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB70-5-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~108/IRPT_DASHBD.TO-DB-b-135.unclassed-90-custodian-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB70-5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how you took the 90 from DB-b-129's membership; what you read (prefixes and object counts, no key holding an account id); ONE table of classes: cause, count, the rule; the remainder and why; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; reads of one firm's custodian tree; nothing served, nothing written but a record.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result and is not widened.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
