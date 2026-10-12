# NFRA_OPLGTW task order -- `OG-ap-12` -- APPLY: grant `sqs:ChangeMessageVisibility` on the silver DLQ; schwab runs the OG-ap-11 build; grade on the next 12:15Z sweep

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-12</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-12</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- opal-assets-silver-schwab fires on bronze ObjectCreated for three masters and on the 12:15Z sweep; the daily pulls land 09:45/10:15/10:45Z and 21:45/22:15/22:45Z. Apply outside [09:15,11:35)Z, [12:00,12:50)Z and [21:15,23:35)Z. The live grade USES the scheduled 12:15Z sweep; no ad-hoc sweep invoke. No cron, alarm or monitor is created.
comp-iam: RUN-BY-ISSUER at the cut (2026-10-12 ~13:08Z) -- simulate-principal-policy opal-assets-silver-schwab-role, sqs:ChangeMessageVisibility on arn:aws:sqs:us-east-1:313476888478:opal-assets-silver-dlq reads implicitDeny (1 role of the 7 attached; CTO read etf implicitDeny too). The act adds the one action to the one shared policy opal-assets-silver-dlq-access (7 roles via list-entities-for-policy). Each already holds sqs:DeleteMessage on the same queue; the DLQ has no RedrivePolicy (CTO read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed pair: COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-ap-12_20261012.md @031aec9026, CTO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_OG-ap-12_20261012.md @2a3205e69d.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-12` (decomposition addendum R3-T.46)

OG-ap-11 deployed the schwab per-family DLQ drain. On the real 12:15Z sweep, `drain_dlq` failed at
`data/assets/scripts/silver/schwab_runtime.py:319`: returning a foreign family's record calls
`sqs:ChangeMessageVisibility`, and the role lacks it (row Z-S97). This order grants that one action and leaves the schwab
converter on the OG-ap-11 build. READ both halves; they BIND.

1. **Ledger** `nfra-oplgtw-ap12-dlq-visibility`: the entry AND its sentinel are committed first. The entry names the
   policy leg, plus the schwab leg if step 3 has to move code.
2. **Grant.** In `infra/aws/terraform/opal-assets/silver.tf`, add `"sqs:ChangeMessageVisibility"` to the Action list of
   statement `SilverDlqSendAndDrain` in `aws_iam_policy.silver_dlq_access`. The Resource stays the one queue. Update the
   comment above the resource and the policy `description` to name the action.
   - Run TF from a worktree of box/sitez HEAD, never a release branch root.
   - Run `bash .tools/safe-apply.sh` with `-target=aws_iam_policy.silver_dlq_access`.
   - The plan, read at rc=0, shows exactly `0 to add, 1 to change, 0 to destroy` on that address, and the policy
     document diff is the one action plus the description. Any other row is a STOP.
   - Read back: a live `simulate-principal-policy` for `opal-assets-silver-schwab-role` and
     `sqs:ChangeMessageVisibility` on the DLQ ARN reads `allowed`.
3. **Schwab code.** Read live `opal-assets-silver-schwab` `CodeSha256`.
   - If it equals `code_sha256` in `W/ap11_build.json` (`YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk=`), the OG-ap-11
     rollback was not applied. Move no code. Revert in source any rollback commit of the pin and package (`7161de0da4`)
     so that `local.silver_build_commit.schwab` and the package directory again equal the OG-ap-11 build. A targeted
     plan on the schwab function then reads `0 to change`.
   - If it equals `prior_code_sha256`, the rollback was applied. Re-deploy the OG-ap-11 build by the OG-ap-11 path: the
     pin moves to the commit whose `data/assets/scripts/silver/` tree equals the package directory, then
     `safe-apply -target` the one function. The plan reads 1 to change: the code fields and `OPAL_BUILD_COMMIT`.
   - Never use `aws lambda update-function-code`. Write `W/ap12_build.json` = `{"code_sha256", "path": "kept|redeployed"}`.
4. **Close** the ledger. Set `infra/aws/lambda/ci/lambda-source-map.json`'s schwab entry to the live build, commit, and
   run AC1.
5. **The live grade** on the NEXT scheduled 12:15Z schwab sweep after step 4.
   - Before ~12:10Z, plant TWO synthetic on-failure-shaped DLQ records, each marked `"synthetic": "OG-ap-12"` and naming
     no real bronze key: one naming `opal-assets-silver-eclipse` (foreign) and one naming `opal-assets-silver-schwab`.
   - After the sweep, the foreign record is still in the queue and absent from the schwab sweep's report (run log or
     backfill-status), and the schwab record is gone and present in the report.
   - Write `W/AP12_GRADE.json` = `{"sweep_run_id", "sweep_was_scheduled", "foreign_survived_schwab_sweep",
     "foreign_absent_from_schwab_report", "schwab_drained_and_reported"}`.
   - The foreign synthetic is then removed by the 16:00Z eclipse sweep (old code), or by you by its own receipt handle.
     Record which.
   - Run AC2 and report once to `2.0.0_SA_COO~O`.
6. **Rollback**, if any read-back disagrees: revert the action by the same targeted apply, and the schwab code to
   `prior_code_sha256` and its prior pin by the same path. Then file an ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- In scope: the one policy (one action), the schwab converter, and the two synthetic DLQ records. No other policy,
  role, queue or function, and no real message deleted by you.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; an ad-hoc sweep invoke; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-assets/silver.tf
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-ap12-dlq-visibility.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after the ledger close, AC2 after the next 12:15Z sweep)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap12.AC1.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*sqs:ChangeMessageVisibility on arn:aws:sqs:us-east-1:313476888478:opal-assets-silver-dlq: allowed.*live CodeSha256 equals the OG-ap-11 build: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap12.AC2.sh; echo "exit=$?"</invocation><expect>(?s)foreign_survived_schwab_sweep=True; foreign_absent_from_schwab_report=True; schwab_drained_and_reported=True; sweep_was_scheduled=True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the grant is live and schwab runs the per-family build. `AC2`: on the real scheduled sweep, schwab keeps only
  its own.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-12.dlq-visibility-grant-apply.proof_of_spec.json`. Validate it after
your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip
the ONE `<status>` tag to `complete` only if both PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 35, workstream APPLY-R35-G. Cause: row Z-S97 (the issuer's comp-iam defect on OG-ap-11). OG-ap-11 closes
  `failed` (AC2 FAIL) whichever way its rollback went; this order carries the fix.
- A1 (issuer, 2026-10-12 ~21:4xZ, row Z-S98): step 2's "and the policy `description`" is STRUCK. An `aws_iam_policy`
  description forces replacement, so it contradicts the step's own plan bar. The applier was right to keep the
  description bytes and change the comment only (@5911f27f74). The plan bar stands: 0 add, 1 change, 0 destroy.
  - At 21:3xZ: the grant is live (ap12.AC1 simulate `allowed`); schwab is still the pre-drain build
    (`uibjggn...`, `b3e481b261`); ledger `nfra-oplgtw-ap12-dlq-visibility` is still OPEN, past its 4 h window.
  - The schwab leg runs outside [21:15,23:35)Z and before [09:15,11:35)Z, so the 2026-10-13 12:15Z sweep grades it.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).
- Pre-cut (2026-10-12 ~13:08Z), both FAIL as expected:
  - ap12.AC1: no ledger; simulate implicitDeny; live code = the OG-ap-11 build.
  - ap12.AC2: grade absent.

<status>pending</status>
<round>35</round>
<workstream>APPLY-R35-G</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
