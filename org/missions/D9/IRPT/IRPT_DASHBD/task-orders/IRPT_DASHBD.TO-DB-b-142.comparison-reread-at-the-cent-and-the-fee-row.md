# TO IRPT_DASHBD.TO-DB-b-142 -- the ledger comparison re-read at the cent over all 51 contested segments, and the one fee row classed by the method's own rule for a flow

<to_id>IRPT_DASHBD.TO-DB-b-142</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~115</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-75 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_75_20261011.md` @06b01d9b88, item 3, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v31.md` @ac4a24a07d | **Rows:** IRPT_DASHBD-D2-W113-S3 | **Decomp cell:** `DB-b-142` (decomposition section 77) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-140 (drained @f7b1cc4571).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-115` (branch `wk-irpt-dashbd-75-115`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~115/`. Read first: the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v31.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why.** DB-b-138 and DB-b-140 compared the custodian's ledger with the served flow at a tolerance of the larger of 1.00 or 0.1
percent. At that tolerance 18 of the 51 contested segments differed, on 50 flow days, all reproduced by counting each transaction id
once. Row W113-S3: at the CENT one more differing day appears in one segment, where the ledger carries a small "Other Fee" expense row
the served flow does not. And the other 33 segments were never re-read by transaction id. The CTO: "the comparison re-read at the cent,
and the one fee row classed by the method's own rule for a flow, cited from the code."

**The cell (`DB-b-142`).** Read-only; you change no code and no served thing. Reuse ~113's scripts and downloads under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~113/` (read in place; its `b2_read.py` shows the re-read that keeps the transaction id
and portfolio group); yours go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~115/`.
1. **All 51 segments, at the cent.** For every flow day of every one of the 51 (not the 18 alone), the custodian's external-flow day
   total with EACH TRANSACTION ID COUNTED ONCE against the served day flow, tolerance half a cent. `segments` {total: 51,
   agree_at_cent, differ_at_cent}; `flow_days` {total, differing_at_cent, reproduced_by_id_once, not_reproduced}, where
   `differing_at_cent` counts the days whose NAIVE sum differs at the cent, `reproduced_by_id_once` those the rule brings to the cent
   and `not_reproduced` the rest. For the not-reproduced days: `residual_days`: [{count, transaction_types (names only), note}].
2. **The fee row.** Find the day row W113-S3 names (and any other not-reproduced day). Then read the METHOD'S OWN RULE for what is a
   flow: in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (the served flow's construction, near the lines ~113 cited: 536-552, 706, 713-732,
   1305-1323) and the method row's stated flow and fee treatment (`METHOD_ROWS`, `fee_basis`, `fee_treatment`). Quote the lines that
   decide whether an account-level fee or an "Other Fee" expense is an external flow, a fee, or neither: `fee_row` {transaction_type,
   method_rule {file, line, quote}, is_flow_by_the_method (bool), reason}. If the method says it is a flow and the served flow omits
   it, that is a defect in the served number: a row, with the day count. If the method says it is not a flow, the custodian's
   external-flow label and the method differ by definition: say so; that is not a defect.
3. **The tie-out's state**, restated: `tieout_state` {total: 244, classed: 185, contested: 51, unclassed: 8, called_closed: false}.
   You move no segment between groups and do not rule on the contested timing question.
4. `client_figures: 0`, `s3_writes: 0`. Counts, transaction TYPE names, rules and code quotes only: no account id, no client name, no
   dollar amount. The check refuses a record holding any run of 8 or more digits. Record `CENT_REREAD.json`.

<criterion id="DB75-2-AC1" cell_refs="DB-b-142"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r75/p75_round75.py" . DB75-2-AC1</invocation><expect>DB75-2-AC1 PASS</expect></criterion>
`DB75-2-AC1` -- the comparison is re-read at the cent over the 51 segments with each transaction id counted once, every remaining difference is counted, and the fee row is classed by the method's own rule cited from the code. Base: FAIL.

<expected_criteria>DB75-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: 49 Financial's OWN Black Diamond transactions tree and its served `account_return_daily` gold, exactly the prefixes workers ~108 and ~113 read (take them from their scripts, never typed), and only for what their downloads do not hold: ~113's re-read kept the transaction id for 17 accounts; the other 33 segments' accounts need the same columns. No other firm's prefix, no other bucket. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~115/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W115-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~115/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-142.comparison-reread-at-the-cent-and-the-fee-row.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 77 (round 75), cell `DB-b-142`.
<owned_cells>DB-b-142</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB75-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~115/IRPT_DASHBD.TO-DB-b-142.comparison-reread-at-the-cent-and-the-fee-row.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB75-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; at the cent, how many of the 51 segments agree and differ and on how many flow days; how many differing days the id-once rule reproduces and how many it does not, with what the unreproduced days hold (transaction TYPE names only); the fee row: its type, the method's rule quoted with file and line, and whether the method counts it as a flow; the tie-out's state; what you read; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; reads of one firm's custodian tree and its served gold; nothing served, nothing written but a record.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result and is not widened.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
