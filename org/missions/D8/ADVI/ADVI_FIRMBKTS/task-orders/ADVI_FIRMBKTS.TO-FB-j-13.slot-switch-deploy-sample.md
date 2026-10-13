# ADVI_FIRMBKTS task order -- `FB-j-13` -- DEPLOY THE SLOT SWITCH AND THE NAME GUARD (THIRD APPLY, SWITCH ON) AND READ A SECOND TEN-ADVISOR SAMPLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-13</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the actor's own identity reads and runs `safe-apply` scoped to one function (code and one environment key); one `lambda:InvokeFunction` with `dry_run: true`; no grant is added.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a plan other than 0/1/0 with exactly one added key, a changed listing, any NNA bullet, an empty sample and an unclosed ledger. Blindness: the record proves the mechanics, not that the texts are right; the CTO reads them.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-13` (round 7; the CTO's rulings (a) and (b) on the ten-advisor sample)

`FB-j-11` adds the slot switch, the client-name guard and the Terraform carrier `disabled_slots`. You deploy that code with the switch ON
(`top_nna_mover` disabled), then dry-run the same kind of sample again, so the CTO and Andrew read the four good slots from the code that
would actually serve. A THIRD apply of this function's code, under the pair's addendum 2.

### 1a. Steps

1. **Preconditions (read, recorded):** `FB-j-11` merged and its criteria PASS at the merged HEAD; the pair's addendum 2 is signed on both
   sides at the current bytes (COO `ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF_ADDENDUM_2.md`, the CTO's matching addendum;
   name both commits). Read the COO addendum first: it permits exactly ONE added environment key.
2. **Entry** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the first write: current `CodeSha256` (`8gbyCaYi896QYTm7MRxbLob7FCHWF5B9DKscxCgRPHY=`
   at the cut), prior artifact VersionId, the pair, the rollback.
3. **Build:** `bash infra/aws/lambda/ci/build-and-upload.sh exec-summary exec-summary-generator`; then
   `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_execeq2.py --zip-prior <deployed.zip> --zip-new <built.zip>` must read `EXEC READS: prior and new canonical EQUAL`.
4. **Plan, scoped:** in `infra/aws/terraform/exec-summary`, `.tools/safe-apply.sh`'s plan limb with
   `-var platinum_mode=canonical -var disabled_slots=top_nna_mover -target=aws_lambda_function.exec_summary_generator`. It must read
   `0 to add, 1 to change, 0 to destroy`: the code hash AND exactly ONE added environment key `EXEC_SUMMARY_DISABLED_SLOTS`
   (the six existing keys unchanged). Anything else: STOP, a BLOCKING row. Omitting `-var platinum_mode=canonical` removes
   `BD_PLATINUM_MODE`: the one way to get this wrong.
5. **Apply** on that saved plan; read back `CodeSha256` and the environment (keys and values).
6. **List** the served prefix (`advi/49financial/platinum/advisors/*/exec_summary.json`) before, ONE dry run of TEN pre-screened ids
   (`{"dry_run": true, "advisor_ids": [...]}`; the ten of `FB-j-10` if you can, so the CTO compares), list after: IDENTICAL.
7. **Read:** `top_nna_mover` bullets must be 0; the other four slots' bullets non-empty; the function's log: any `[SLOT_DROPPED]` lines by class.
8. **The sample for reading:** `SLOT_SWITCH_ARTIFACTS.json` and `SLOT_SWITCH_FIGURES.json` (one row per bullet: slot, headline and detail verbatim and
   the figures from its `evidence_keys`); if an artifact carries a client name or an id, record the count and withhold that text.
9. Close the entry. Do NOT invoke without `dry_run`.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_SWITCH_SAMPLE.json`

```json
{"order": "FB-j-13", "read_at": "<ISO UTC>", "calls": ["aws lambda invoke ...", "..."],
 "deployed_version": "CodeSha256 ...", "pair": {"coo_half_addendum2": "<commit>", "cto_half_addendum2": "<commit>"},
 "plan": {"add": 0, "change": 1, "destroy": 0, "env_keys_added": ["EXEC_SUMMARY_DISABLED_SLOTS"]},
 "ledger_closed": true, "advisors": 10, "listing_before": 158, "listing_after": 158,
 "nna_bullets": 0, "bullets_returned": 0, "drops": 0, "classes": {}, "claim": "measured"}
```

## 2. BOUNDS

1. One scoped apply of one function's code plus ONE environment key; ONE dry-run invocation; reads otherwise. No non-dry invocation, no S3
   write, no other env change, no rule change.
2. Print no secret, no client name and no account or relationship id.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-13.slot-switch-deploy-sample.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-13"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py switchsample --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_SWITCH_SAMPLE.json</invocation><expect>^SWITCHSAMPLE record ok bullets=[1-9][0-9]* nna=0 drops=[0-9]+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-13.slot-switch-deploy-sample.proof_of_spec.json`. Commit the record and the two sample files FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Row ids `ADVI_FIRMBKTS-D1-S<k>`. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the plan, the counts, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PARKED at the cut: owner `2.0.0_SA_COO~B1`; un-park conditions (all): `FB-j-11` merged and PASS; the pair addendum 2 signed by both halves (the COO addendum is the issuer's, authored at the cut; the CTO's matching addendum asked); the issuer amends `<status>` and messages FB1 citing this order. The CTO's ruling: (a) `top_nna_mover` disabled by config for the first regeneration, (b) the PII guard learns client display names, then the sample is offered to Andrew before `FB-j-4`. The Terraform variable is `disabled_slots` (default empty: no key).

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~11:0xZ):** the CTO's ADDENDA 4-5 of his FB-j-6 half (ddbaf334d1) sign the third apply and add two requirements: (i) dry-run the SAME ten advisors as `FB-j-10` (the keys of its `DRYRUN10_ARTIFACTS.json`), so the two samples compare per advisor; (ii) PROVE THE NAME GUARD ON THE WITHHELD ONE: the advisor whose `top_nna_mover` bullet leaked a client display name in `FB-j-10` must come back with the slot switched off (zero NNA bullets) and the other four slots' bullets free of the name; record that advisor's result by ordinal only (no id, no name). Also, from now on hash relationship ids AT WRITE TIME in every file you write (see `FB-j-14`). The plan's only diffs are the code hash plus `EXEC_SUMMARY_DISABLED_SLOTS`; the other environment keys stay byte-unchanged (the plan record names that). The COO addendum 2 is at 89f2099f0a and the CTO's at ddbaf334d1. Still parked on `FB-j-11` merged and PASS only.

<status>parked</status>
<round>7</round>
<workstream>SLOTSWITCHDEPLOY</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-13</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
