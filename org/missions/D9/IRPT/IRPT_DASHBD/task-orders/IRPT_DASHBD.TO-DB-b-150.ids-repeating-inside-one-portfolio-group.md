# TO IRPT_DASHBD.TO-DB-b-150 -- the transaction ids that repeat INSIDE one portfolio group in the original store: counts by cause, or stated unexplained -- a read

<to_id>IRPT_DASHBD.TO-DB-b-150</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~123</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>78</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5827 (2026-10-11 ~20:52Z), second item | **Rows:** IRPT_DASHBD-D2-W113-S2 | **Decomp cell:** `DB-b-150` (decomposition section 80) | **outcome_ref:** every consumer of that store | **depends_on:** DB-b-143 (drained @cf125a14d4).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-123` (branch `wk-irpt-dashbd-78-123`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~123/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** On 2026-10-06 the original Black Diamond transactions store held 22,573 transaction ids with more than one row. The portfolio
group explains most: the same transaction once per group. But 590 of those ids ALSO have two or more rows inside ONE group, which the
group does not explain (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~116/ORIGINAL_STORE_SHAPE.json`). It matters in the opposite
direction from the repetition: the served readers dedupe on the transaction id, so if those same-group rows are REAL separate rows (two
legs, a split, a correction and its original), a dedupe on the id alone drops one. The CTO: "the 590 ids repeating inside one group:
counts by cause, or stated unexplained."

**The cell (`DB-b-150`).** A read. You change no code.
1. **Reproduce the count** on the same day with DB-b-143's projection (its private script is under
   `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~116/`): `denominator` = ids with two or more rows inside one portfolio group. A
   count other than 590 is reported as measured with how it differs (the store may have been rewritten since: row W116-S2), not forced.
2. **What differs between the rows of one id inside one group**, on the non-money, non-account columns: nothing at all (exact
   duplicates on every column you may read), or a column that tells them apart. `causes`: [{cause, ids, rule}], for example: exact
   duplicate on all readable columns; differs in action or type (two legs of one transaction); differs in a date (a re-post); differs
   in a load or sequence column. Each cause is a RULE over the readable columns that a reader could re-apply; an id whose rows differ
   in more than one way sits under a cause named for the combination. `unexplained` {ids, why}: ids you cannot place, including those
   where the only possible difference is in a column you may not read: say exactly that.
3. **What it means for the readers, stated and not fixed:** for each cause, one sentence on whether a dedupe keyed on the transaction
   id alone keeps the right number of rows (`dedupe_on_id_alone`: "correct", "drops a real row" or "cannot tell without a money
   column"). A cause where it drops a real row is ONE ROW naming the readers DB-b-143 listed as keyed on the id (class OBSERVATION;
   ARMED only if you can show a served number is wrong today). You correct nothing.
4. `s3_writes: 0`. No account id, client name or amount; the check refuses a record holding any run of 8 or more digits. Private files
   go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~123/`. Record `SAME_GROUP_REPEATS.json`.

<criterion id="DB78-3-AC1" cell_refs="DB-b-150"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r78/p78_round78.py" . DB78-3-AC1</invocation><expect>DB78-3-AC1 PASS</expect></criterion>
`DB78-3-AC1` -- the ids that repeat inside one portfolio group on one day are counted and each is placed under a cause with a rule or under unexplained with why. Base: FAIL.

<expected_criteria>DB78-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: the SAME one day of the original Black Diamond transactions store DB-b-143 read (2026-10-06; its address from its record), with the descriptive columns it read plus any other NON-money, NON-account column the object holds that can tell two rows of one id and one group apart (a sequence, a lot, a leg, a status, a load stamp). NO money column and NO account column. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~123/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W123-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~123/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-150.ids-repeating-inside-one-portfolio-group.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 80 (round 78), cell `DB-b-150`.
<owned_cells>DB-b-150</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB78-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~123/IRPT_DASHBD.TO-DB-b-150.ids-repeating-inside-one-portfolio-group.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB78-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the day and how many ids repeat inside one group (and that you reproduced DB-b-143's count or how yours differs); ONE table of causes: cause, ids, the rule; the unexplained ids and why; whether a reader that dedupes on the transaction id alone would drop a real second row; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one read of one day; nothing is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one governed read; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
