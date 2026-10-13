# TO IRPT_DASHBD.TO-DB-b-170 -- the 2 segments with no flow day get their reason from the closed list by a tracked cell: the accrual correction closes both, the uncorrected control misses both; round 89's rule reused unchanged

<to_id>IRPT_DASHBD.TO-DB-b-170</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~135</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>90</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6986, ROUND-90 ANALYSIS @d573cb1cb8 section 3 item 3 and PRD v0.13 decision 11b | **Rows:** NONE | **Decomp cell:** `DB-b-170` (decomposition section 92) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-167 (drained @b70da0aa6a).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-135` (branch `wk-IRPT_DASHBD-135`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~135/`. Your private folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~135/` (create it).

**Why.** Of the 90 stored tie-out segments, 88 carry a flow day and 2 do not. Round 89 reasoned the 12 flow segments neither convention closes; PRD v0.13 decision 11b counts all 90, so the 2 no-flow segments owe a reason too, found by a TRACKED cell, not a scratch script. The issuer's scratch read (counts only, not evidence) found that both miss uncorrected and both pass the accrual identity
and close when it is applied. Your cell reproduces that with a tracked module and a control, or reports otherwise.

**The cell (`DB-b-170`).** A read and a private count over worker ~108's stored tables, on the copy held under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~133/copy/` (read-only; `members90.pkl` is not in it and is not needed). You change no served code.
1. **Read the model first.** `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_neither_reasons.py` (round 89's tracked module: `make_w`, `test_missing`, `income_pairs`, `accrual_identity`, `accrual_r`, `closes`, the corrections; import it by path, do not edit it; it points the stored folder at the copy above) and
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/RULE.md` (the committed rule, sha256 `fc50363af10dfad3d0088a4220c68132b8a02c41859941e8ab30c7be53361f55`). **The rule is REUSED UNCHANGED: you write no new rule file.** Reasons 2 and 3 of the closed list test a flow day, so neither can apply to a segment with no flow day; reasons 1, 4 and 5 can.
2. **Write ONE new tracked module** `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_noflow_reasons.py` (ASCII, passes `bash .tools/commit-gate.sh`) that: selects the segments of the 90 with NO flow day inside the window (assert 2, else stop); asserts the population (90 segments, 86 accounts, 88 with a flow day); applies the rule's closed-list tests in its order and the rule's corrections to each of the 2, with the same gross and the same
   relink (`bd_default`, which equals `end` on a segment with no flow); prints counts only. **Control:** the uncorrected recomputation (`bd_default` and `end`) closes 0 of the 2.
3. **Record** `NOFLOW_2_REASONS.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `rule` {`file`: "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/RULE.md", `sha256` (of its bytes), `reused_unchanged`: true}; `reasons_list` (the six names of round 89, in order); `code` {`file`, `sha256`, `tracked`: true}; `population` {`segments`: 90, `accounts`: 86,
   `no_flow_segments`: 2, `flow_segments`: 88}; `by_reason` (the six names: int, summing to 2); `evidence` (for each reason above 0 except UNEXPLAINED: {`kind`: "count" or "day_offsets", `values`: [ints]}); `corrected` {`reasoned`, `closed_within_tolerance`} (both equal 2 minus UNEXPLAINED); `uncorrected_closes_among_2` 0; `reads` {`vendor_calls`: 0, `secret_reads`: 0, `s3_writes`: 0};
   `served_values_changed`: false; `limits`. NO account id, client name, amount or run of eight or more digits. If the result is not BD_ACCRUED_INCOME 2, the criterion does not pass as written: report your measurement and file a row (counts only); do not repair.

<criterion id="DB90-3-AC1" cell_refs="DB-b-170"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r90/p90_round90.py" . DB90-3-AC1</invocation><expect>DB90-3-AC1 PASS</expect></criterion>
`DB90-3-AC1` -- the record exists with the keys above; the rule is round 89's unchanged; the code is tracked and hashes to the stated sha256; the population reproduces 90 segments, 86 accounts, 2 without a flow day; the reason counts sum to 2 and both are `BD_ACCRUED_INCOME`; every reasoned segment closed within 0.35 pp when corrected; the uncorrected control closes 0 of 2;
zero vendor calls, secret reads and S3 writes; no served value changed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB90-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. `tieout_neither_reasons.py`, `tieout_flow_timing.py`, round 89's `RULE.md` and every stored table are READ ONLY.
- **No vendor call and no secret read.** No S3 access (the tables are local), no Lambda, Terraform or IAM act, no deploy, no push.
- **No client data in what you write.** Counts and booleans only; nothing derived from the private tables goes anywhere but the private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W135-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~135/
org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_noflow_reasons.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-170.no-flow-segments-reasons-by-a-tracked-cell.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 92 (round 90), cell `DB-b-170`.
<owned_cells>DB-b-170</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB90-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~135/IRPT_DASHBD.TO-DB-b-170.no-flow-segments-reasons-by-a-tracked-cell.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB90-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the six counts; the control; the evidence for each used reason; the module's commit; any row ids. Counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private read and a counts-only record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access is granted or needed; the stored tables are local.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and the control is the uncorrected recomputation.
lane: the <paths> block IS the grant.
</preflight>
