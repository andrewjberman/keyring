# TO IRPT_DASHBD.TO-DB-b-132 -- the manifests copy the five thresholds and their claims and nothing else: one function both writers use, so whatever else a thresholds file holds stays out of a served object by construction

<to_id>IRPT_DASHBD.TO-DB-b-132</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~106</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-69 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_69_20261011.md` @90cb3e774b, section 4 item 2, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` @595332678c | **Rows:** IRPT_DASHBD-D2-W100-S3 | **Decomp cell:** `DB-b-132` (decomposition section 72) | **outcome_ref:** FWD-11 | **depends_on:** none to start; its DRAIN waits for DB-b-130 (the apply runs the producer from the shared tree and its packet states the manifest's thresholds object unchanged).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-106` (branch `wk-irpt-dashbd-70-106`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~106/`. Read first: section 2 (item 2) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is wrong.** `build_manifest` (the daily returns manifest) and `emit_method_row` (the method row's manifest) in
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` both write `"thresholds": thresholds`: the WHOLE input object. The last tracked 49 Financial thresholds
file carried 24 keys, two of them holding account-number-shaped digit runs (row W100-S3). The CTO: "the manifests copy the five thresholds
and their claims and nothing else."

**The cell (`DB-b-132`).**
1. **Readers first.** Find every reader of a manifest's `thresholds` object (the gold producer, the handler under
   `infra/aws/lambda/investor-reporting/reporting-gold/`, the silver mint `data/assets/scripts/silver/commonwealth_account_return_daily.py`,
   the reporting read under `infra/aws/lambda/investor-reporting/reporting/`): `readers`: [{file, line, reads}]. If a reader needs a key
   that is neither one of the five values nor `threshold_claims`, STOP with a row and build nothing.
2. **One function.** Add `served_thresholds(thresholds)` to the producer: it returns a NEW dict holding exactly the five values of
   `THRESHOLD_VALUES` (each as given, null allowed) and `threshold_claims` (the five claims as `threshold_claims_of` resolves them, so an
   input with no claims serves the defaulted ones), and nothing else. Both writers serve `served_thresholds(thresholds)`; the literal
   `"thresholds": thresholds` no longer occurs in the file. The tie-out value and its claim are columns of the method row already and are
   not added to this object.
3. **Tests** under `data/assets/scripts/gold/irpt_reporting/tests/`: an input carrying extra keys (one named like a per-account member, with
   a made-up 9-digit key) yields a returns manifest and a method manifest whose `thresholds` object holds none of them. `tests` {passed,
   failed}; the folder's existing tests must not newly fail (some pin the manifest's thresholds object: bring them to the new shape and say
   which). Record `MANIFEST_THRESHOLDS.json`: {function, call_sites, keys_before, keys_after, readers, tests}.
4. No release, no upload, no `upload=True` call. The method row's COLUMNS do not change; the contract does not change.

<criterion id="DB70-2-AC1" cell_refs="DB-b-132"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r70/p70_round70.py" . DB70-2-AC1</invocation><expect>DB70-2-AC1 PASS</expect></criterion>
`DB70-2-AC1` -- the producer's two manifest writers serve only the five thresholds and their claims, through one function, and no whole-object copy is left. Base: FAIL.

<expected_criteria>DB70-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~106/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W106-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~106/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-132.manifests-copy-five-thresholds-only.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 72 (round 70), cell `DB-b-132`.
<owned_cells>DB-b-132</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB70-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~106/IRPT_DASHBD.TO-DB-b-132.manifests-copy-five-thresholds-only.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB70-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the function and its two call sites (file:line); what a manifest's thresholds object holds before and after (key names); every reader of a manifest's thresholds object you found, with file and line and what it reads; the tests; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; two manifest writers in the producer; nothing is served until a later release or upload under its own pair. The signed R45 release builds from its four pins and does not carry this.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
