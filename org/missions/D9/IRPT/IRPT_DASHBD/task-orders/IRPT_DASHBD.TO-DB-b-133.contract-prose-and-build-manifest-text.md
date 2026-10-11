# TO IRPT_DASHBD.TO-DB-b-133 -- the contract's two prose lines stop naming an outcome id as the cause of row 3's absent income, and the tracked Cottonwood build manifest's stale text is corrected or its refusal recorded

<to_id>IRPT_DASHBD.TO-DB-b-133</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~107</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-69 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_69_20261011.md` @90cb3e774b, section 4 item 3, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` @595332678c | **Rows:** IRPT_DASHBD-D2-W103-S2, IRPT_DASHBD-D2-W102-S1 | **Decomp cell:** `DB-b-133` (decomposition section 72) | **outcome_ref:** FWD-11 | **depends_on:** none to start; its DRAIN waits for DB-b-130 (the apply reads the build manifest's method_row).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-107` (branch `wk-irpt-dashbd-70-107`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~107/`. Read first: section 3 (item 3) and 4 (item 3) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**The cell (`DB-b-133`).** Two parts. No code changes.
1. **The contract** `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json`: two prose members still give "FWD-3 does not separate income" as the cause of
   method row 3's absent income (line 6, the `authored_under` history; line 35, the `income_basis` column's `meaning`). Reword each so the
   cause is the METHOD, in the words the producer now states for row 3 (read `METHOD_ROWS[3]` in
   `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`): a positions-based method values the account from its positions and cash, so income is inside that value
   and is not separated from it. The history line may still say WHICH task order made the change; it must not give the outcome id as the
   cause. No column, enum, example row or `schema_hash` moves; `contract_version` stays 0.6.0 (a prose change). `contract_lines`:
   [{member, before, after}].
2. **The build manifest** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json` (another project's tracked record; the CTO ordered its stale text
   corrected, row W102-S1): its `columns_null.method_version` text still reads "NULL on purpose...", while the adapter stamps 3. Change
   THAT ONE text member to what the adapter does, in the words the adapter's own `COLUMNS_NULL` entry now uses (read it in
   `data/assets/scripts/silver/commonwealth_account_return_daily.py`). Change NOTHING else in the file: its `method_row` member is an input
   of a pending apply and the check pins it byte for byte; keep the file's indentation and key order (load, change one member, dump the
   same way, then diff: exactly one line differs). If `safe-commit` REFUSES the file for its lane, do NOT override and do not use `--force`:
   restore the file (`git checkout -- <file>`), and record `build_manifest_text: "REFUSED_BY_LANE"` with `refusal` (the gate's text).
   Otherwise `build_manifest_text: "CORRECTED"` with `before` and `after`.
Record `PROSE_LINES.json`: {contract_lines, schema_hash_unchanged, build_manifest_text, before, after, refusal}.

<criterion id="DB70-3-AC1" cell_refs="DB-b-133"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r70/p70_round70.py" . DB70-3-AC1</invocation><expect>DB70-3-AC1 PASS</expect></criterion>
`DB70-3-AC1` -- the contract's two prose lines are worded for the method with its schema hash unchanged, and the build manifest's stale text is corrected or its lane refusal recorded. Base: FAIL.

<expected_criteria>DB70-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~107/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W107-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~107/
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-133.contract-prose-and-build-manifest-text.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 72 (round 70), cell `DB-b-133`.
<owned_cells>DB-b-133</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB70-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~107/IRPT_DASHBD.TO-DB-b-133.contract-prose-and-build-manifest-text.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB70-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; each of the two contract lines before and after; that the schema hash did not move; the build manifest's text before and after, or the refusal verbatim; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; prose in a contract file and one text member of a tracked build record; nothing served, no code.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
