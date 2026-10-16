# NFRA_OPLGTW task order -- `OG-ap-11` -- APPLY: OG-fd-1's per-family DLQ drain on the SCHWAB converter only (partial roll-out)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-11</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-11</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- opal-assets-silver-schwab fires on bronze ObjectCreated for three masters and on the 12:15Z sweep; the daily pulls land 09:45/10:15/10:45Z and 21:45/22:15/22:45Z. Apply outside [09:15,11:35)Z, [12:00,12:50)Z and [21:15,23:35)Z (the OG-ap-5 windows). The live grade USES the scheduled 12:15Z sweep; no ad-hoc sweep invoke. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- code only; the converter's role already holds receive/delete/change-visibility on the DLQ (opal-assets-silver-dlq-access).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed pair over org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~58/NEVER_WIDEN_ASK_OG-fd-1.md: COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-fd-1_20261012.md @824ec17c4d, CTO @aafc1640e8 (schwab ONLY today; etf, blackdiamond, orion, eclipse each wait for their own pair).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-11` (decomposition addendum R3-T.45)

Deploy the per-family drain to the SCHWAB converter only. The source is merged on box/sitez (@fb53c84ee0):
`data/assets/scripts/silver/schwab_runtime.py` `drain_dlq(..., family="schwab")`. Schwab's 11 vendored files equal the
source apart from this change, so the rebuild ships the drain change ALONE. READ both halves; they BIND.

1. **Ledger** `nfra-oplgtw-fd1-schwab-drain`: entry AND sentinel committed first. The entry STATES THE PARTIAL ROLL-OUT:
   after this deploy only the schwab sweep is per-family. The etf, blackdiamond, orion and eclipse sweeps still drain the
   whole queue until their own pairs land (CTO half).
2. **Record shape first** (COO half condition C). Read ONE live record of `opal-assets-silver-dlq` without consuming it
   (`receive-message --visibility-timeout 0 --max-number-of-messages 1`; delete nothing). Confirm it carries
   `requestContext.functionArn`. Write `W/ap11_record_shape.json` = `{"functionArn_present": true|false,
   "read_nondestructive": true, "sample_function": "<the arn's function name>"}`. If the queue is empty, wait for its
   13:07Z refill and read then. If the field is absent, STOP: file a BLOCKING row and do not deploy.
3. **Build and apply** the schwab converter through its Terraform path, as OG-ap-5 did:
   - rebuild the package from source;
   - move `local.silver_build_commit.schwab` in `infra/aws/terraform/opal-assets/silver.tf` to the commit whose
     `data/assets/scripts/silver/` tree equals the package directory;
   - `bash .tools/safe-apply.sh` with `-target` to that one function. The plan reads 1 resource changed: the code fields
     and the one `OPAL_BUILD_COMMIT` environment value; any other row is a STOP.
   - Never use `aws lambda update-function-code`.

   Read back `CodeSha256` = the build, State Active, LastUpdateStatus Successful. Write `W/ap11_build.json` =
   `{"code_sha256", "prior_code_sha256"}`.
4. **The live grade** (around the SCHEDULED 12:15Z schwab sweep after the deploy). Before ~12:10Z, plant TWO synthetic
   on-failure-shaped records in the DLQ:
   - one naming `opal-assets-silver-eclipse` (foreign);
   - one naming `opal-assets-silver-schwab`.

   Each body is marked `"synthetic": "OG-ap-11"` and names no real bronze key. After the sweep:
   - the foreign record is still in the queue and absent from the schwab sweep's report (its run log or
     backfill-status);
   - the schwab record is gone and present in the report.

   Write `W/AP11_GRADE.json` = `{"sweep_run_id", "sweep_was_scheduled", "foreign_survived_schwab_sweep",
   "foreign_absent_from_schwab_report", "schwab_drained_and_reported"}`. The foreign synthetic record is then removed by
   the 16:00Z eclipse sweep (old code) as designed, or by you by its own receipt handle. Record which.
5. Close the ledger, update `infra/aws/lambda/ci/lambda-source-map.json`'s schwab entry to the deployed build, commit,
   run AC1 and AC2, and report once to `2.0.0_SA_COO~O`. Rollback, if any read-back disagrees: redeploy the prior code
   and the prior pin by the same path, then an ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- The schwab converter only, plus the two synthetic DLQ records. No other family, no real message deleted by you.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; an ad-hoc sweep invoke; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-assets/silver.tf
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-fd1-schwab-drain.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after the ledger close, AC2 after the 12:15Z sweep)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap11.AC1.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*live CodeSha256 equals the recorded build: yes; differs from the prior: yes; live record carries functionArn: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap11.AC2.sh; echo "exit=$?"</invocation><expect>(?s)foreign_survived_schwab_sweep=True; foreign_absent_from_schwab_report=True; schwab_drained_and_reported=True; sweep_was_scheduled=True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the new drain is live on schwab, after a confirmed record shape. `AC2`: on the real scheduled sweep, schwab keeps
  only its own.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-11.schwab-dlq-drain-apply.proof_of_spec.json`. Validate it after your
last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE
`<status>` tag to `complete` only if both PASS.

<!-- ===================== RECORD FACE ===================== -->


**CLOSED FAILED** (issuer ruling A2 @aebec97ee4 option b, confirmed msg 33493 'Finish OG-ap-11 as you
said: closed failed'). The deploy LANDED correctly and the code could not RUN:
opal-assets-silver-schwab-role is not authorized for `sqs:ChangeMessageVisibility` on
opal-assets-silver-dlq, so `drain_dlq` raises at `schwab_runtime.py:319` the moment it tries to RETURN a
foreign family's message, and the scheduled sweep fails AFTER completing its conversion lanes. AC1 PASSED
(the deploy was sound); AC2 FAILED on the live grade. Two AC2 fields are recorded NOT-TRUE rather than
true, because no sweep report exists to be absent from: `foreign_absent_from_schwab_report` is NULL and
`schwab_drained_and_reported` is FALSE on the conjunction (drained yes, reported no). The order's
`comp-iam: DECLARED-NOT-APPLICABLE` preflight was the defect and the issuer has taken it as its own; that
permission became load-bearing exactly at this deploy, because the old code drained by DELETING and never
called change-visibility. ROLLED BACK to the pre-drain build and pin b3e481b261 at 13:14:03Z, ledger
`nfra-oplgtw-fd1-schwab-drain-rollback` CLOSED, live CodeSha256 confirmed back to
`uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE=`. Row `NFRA_OPLGTW-Z-S97` BLOCKING/ARMED carries it. The
grant goes to the CTO as its OWN never-widen pair and NFRA_OPLGTW.TO-OG-ap-12 re-deploys the a11240c01c
build after it lands. Evidence: `W/AP11_GRADE.json`.

**ISSUER NOTES:**
- Round 35, workstream APPLY-R35. Row Z-S91 stays open until every sweeping family is per-family.
- A1 (issuer, 2026-10-12 ~01:1xZ, 0.7.0_AE_CloudOps~Z msg 33434: the DLQ is EMPTY now, refilling at 13:07Z): COO half condition C
  is satisfied by a REAL non-destructive read already on file. `deliverables/0.9.0_WK_NFRA_OPLGTW~57/DQ1_READ.json`
  (OG-dq-1, @94ddb37165) read the bodies of 12 live records at 2026-10-11T15:55Z-15:58Z with visibility-timeout 0 and
  recorded: 'each body is a Lambda async-invoke on-failure record: functionArn opal-assets-silver-eclipse, condition
  RetriesExhausted'. Step 2 may therefore write `W/ap11_record_shape.json` = `{"functionArn_present": true,
  "read_nondestructive": true, "sample_function": "opal-assets-silver-eclipse", "source": "DQ1_READ.json
  2026-10-11T15:55Z"}`. The deploy may proceed now, and the grade runs on TODAY's 12:15Z sweep. A synthetic record is
  NOT shape evidence (the applier was right). Gate limb: GATE (viii) on the modified order (placeholders NONE).
- A2 (issuer, 2026-10-12 ~12:4xZ, row Z-S97, 0.7.0_AE_CloudOps~Z msg 33483): AC2 FAILED on the real 12:15Z sweep. The
  schwab role lacks `sqs:ChangeMessageVisibility` on the DLQ: the new drain returns a foreign record with it, while the
  old code only deleted. The preflight's comp-iam NOT-APPLICABLE was the ISSUER's defect. RULING: ROLL BACK under step
  5, at or after 12:50Z (the window), never inside [12:00,12:50)Z:
  - redeploy the prior code and the prior `silver_build_commit.schwab` pin by the same `safe-apply -target` path;
  - read back `CodeSha256` = `prior_code_sha256` from `W/ap11_build.json`;
  - restore the source-map entry;
  - close ledger `nfra-oplgtw-fd1-schwab-drain` as ROLLED-BACK.

  Before the rollback, read the DLQ NON-destructively (`--visibility-timeout 0`) and record in a row citing Z-S97
  whether the failed sweep's own schwab on-failure record is in the queue. Delete nothing; the eclipse synthetic stays
  for the 16:00Z sweep. The order then closes `failed` (AC2 FAIL, rolled back). The grant is IAM widening the CTO has
  not signed, so it is a new pair for the next round, not this order. Gate limb: GATE (viii) on the modified order
  (placeholders NONE).
- Pre-cut: ap11.AC1 FAIL as expected (no ledger, no record files; live read OK). ap11.AC2 FAIL as expected (grade
  absent).

- A3 (issuer, 2026-10-16 ~16:0xZ, CTO msg 35104): the order closed `failed` in round 35 (AC2 FAIL, rolled back) and `failed` reads open to `round-close-check.py` (its terminal words are complete, superseded, cancelled, withdrawn, retired, parked). The missing `sqs:ChangeMessageVisibility` grant the drain needed is not re-asked here; the DLQ drain returns as a new pair in a later round. Marked `superseded` so the round-38 close reads it terminal. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>superseded</status>
<round>35</round>
<workstream>APPLY-R35</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
