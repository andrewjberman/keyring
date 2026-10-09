# NFRA_OPLGTW task order -- `OG-ap-1` -- APPLY: the Tax SMA master 08403355 in the daily pull, its silver conversion and the gateway's reader roles (OG-tm-1 Phase B legs C, B, A)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-1</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the live daily-pull rules are cron(45 9,21 * * ? *) (08335338) and cron(15 10,22 * * ? *) (08242234); the new rule is cron(45 10,22 * * ? *); the silver sweep runs at 12:15Z. One EventBridge rule is created; no alarm, monitor or notification other than the one S3 bucket-notification rule silver-schwab-08403355.
comp-iam: RUN -- the APPLIED plane read at the cut (r32/checks/tm1.AC3.py, iam:SimulatePrincipalPolicy): the two gateway Schwab roles explicitDeny every schwab/08403355/ served and completion prefix; the bronze and fact_acc controls are denied for both masters. Three IAM surfaces change by Terraform: resources 3, 4, 6-8, 10, 11 of the table below.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed never-widen pair on OG-tm-1: COO half org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-tm-1_20261009.md @3998bbe5a7 and CTO half org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~O/NEVER_WIDEN_HALF_CTO_OG-tm-1_20261009.md @4149c01c23, over the ask org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~39/NEVER_WIDEN_ASK_OG-tm-1.md @b4375f2379.
EGRESS CLASS, declared: NONE from the applier's box beyond Opal's own AWS. The new rule's scheduled pulls reach Schwab SDD from the SI2 box (Andrew's answer 1, record @116d52009d).
</preflight>

## 1. THE CELL -- `OG-ap-1` (decomposition addendum R3-T.30; OG-tm-1's Phase B, re-addressed to the site Z applier)

Andrew-direct 2026-10-08 ~22:0xZ (relayed by `0.0.0_AB_MSTR~Z`, msg 32057): site Z's deploys are applied by you. This
order is the apply half of `OG-tm-1`: add master `08403355` (the Tax SMA master) to the daily Schwab pull exactly as the
two existing masters are set up. Both never-widen halves are signed (preflight). READ, in this order: the ask (its
sections 1, 3, 4, 5), the COO half, the CTO half. The halves BIND where they narrow the ask.

**The resources (the ask's section 1 table; apply by `-target` ONLY).** Two plan drifts are OUTSIDE this act and must NOT
ride it: `cot_rebalancer_runner_daily` (opal-assets) and `mcportal_grant_writer` (opal-gateway), row S5.

| # | Root / object | Target |
|---|---|---|
| 1 | canonical-schwab-ec2 | `aws_cloudwatch_event_rule.si2_daily["08403355"]` (create, `cron(45 10,22 * * ? *)`) |
| 2 | canonical-schwab-ec2 | `aws_cloudwatch_event_target.si2_daily["08403355"]` (create) |
| 3 | canonical-schwab-ec2 | `aws_iam_role_policy.schwab_si2_monolith_write` (in place) |
| 4 | opal-assets | `aws_iam_role_policy.silver_read_bronze["schwab"]` (in place) |
| 5 | opal-assets | `aws_s3_bucket_notification.monolith_bronze` (in place: +1 rule `silver-schwab-08403355`) |
| 6-8 | opal-assets | `aws_iam_policy.monolith_write_per_source["schwab"]`, `aws_iam_policy.silver_write_per_source["schwab"]`, `aws_iam_role_policy_attachment.silver_write["schwab:schwab"]` (replace; a seconds-long write-grant window) |
| 9 | opal-assets | `module.silver_converter["schwab"]` (in place: code hash and `OPAL_BUILD_COMMIT` 1f03a3f209 -> 47c3c75f11) |
| 10-11 | opal-gateway | `aws_iam_role_policy.schwab_data_read_policy`, `aws_iam_role_policy.schwab_catalog_read_policy` (in place) |
| 12 | S3 code object | `s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1`: ETag `0017f9b549ca9f8013704f50c4327bed` -> MD5 `e49aea76a8c634c9d49e6a7cccc51bdf` |
| 13 | S3 artifact | `opal-assets/opal-assets-silver-schwab.zip`: rebuilt from box/sitez HEAD, sha256 MUST equal `AzrzJS+91y57ylRdqGccFPGqWaqAGLFn/jhItkAQCzE=` before upload |

**Order and timing (the COO half section 3; the CTO half).**
1. Open the NEVER-2 ledger `nfra-oplgtw-og-tm-1-taxsma-master` (entry AND sentinel committed before the first act).
2. **Leg C:** rebuild the converter artifact from box/sitez HEAD (`BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh
   opal-assets opal-assets-silver-schwab`); its sha256 must equal row 13's, else STOP and report. Upload it, then apply
   opal-assets targets 4-9 with `bash .tools/safe-apply.sh`. Run 6-8 outside [09:15,11:35)Z and [21:15,23:35)Z and away
   from 12:15Z. Read back: the notification configuration holds 12 rules (11 before + `silver-schwab-08403355`); the
   converter's `CodeSha256` equals row 13.
3. **Leg B:** apply canonical-schwab-ec2 target 3; upload the puller to row 12's key with `--sse AES256` and read its ETag
   back. Outside [09:15,11:35)Z and [21:15,23:35)Z.
4. **Leg A last:** apply canonical-schwab-ec2 targets 1-2. The rule must not exist before legs C and B are in place.
5. **Gateway roles:** apply opal-gateway targets 10-11 (independent of the pull legs).
6. Close the ledger, commit, then run the criteria. A read-back that disagrees with the halves: roll back per the ask's
   section 4 and file an ARMED row naming `2.0.0_SA_COO~O`. Never leave it half-landed.
7. Report to `2.0.0_SA_COO~O` (one message: ledger closed, the three criteria, the apply commit). The QA pull is NOT
   yours: the issuer's worker runs it after your report.

Tell the puller's owning lane `0.6.2_AE_PartnerETL` at the apply, in one line, naming this order.

**AMENDMENT A1 (issuer, 2026-10-09 ~03:5xZ; your msg 32325, row NFRA_OPLGTW-Z-S68).** Legs C, B and the gateway roles
are landed (your AC2, AC3 PASS by output; the issuer re-grades at the drain). Leg A's refusal by the LGIC naming gate is
RULED option (c): the 08403355 rule takes the `lib/opal_naming.py` name (the gate's `schwab-canonical-si2-08403355-pull-daily`);
the two existing rules keep theirs (CLAUDE.md rule 30 non-application). Worker ~39 changes
`monolith-daily-schedule.tf` under OG-tm-1 A3 (@76dcd19c08). WAIT for the issuer's one line naming that drained commit,
then apply targets 1-2 (same addresses, `aws_cloudwatch_event_rule.si2_daily["08403355"]` and `..._target...`) from it,
read back, close the ledger, run the criteria (`tm1.sh AC1` now resolves the rule by the builder name). Keep the ledger
OPEN meanwhile; extend its window with `.tools/deploy_ledger.py` if it would lapse, never close it half. Rows take the
`NFRA_OPLGTW-Z-S<k>` form (your note; the order's `Z-AE-S<k>` cannot match SURPRISE_ID_RE).

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- `-target` lists only; never a whole-root apply; never bare `terraform`; never `aws lambda update-function-code`.
- Only `schwab/08403355/` keys and the resources above move. The two existing masters' rules, grants, prefixes and data
  are unchanged.
- No SSM send to the SI2 box, no ad-hoc pull, no Schwab call from your box.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-tm-1-taxsma-master.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (A1), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from the repo root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tm1.sh AC1; echo "exit=$?"</invocation><expect>(?s)\(a\) code object -Master ValidateSet: \[[^\]]*'08403355'.*\(c\) targets 1; RunPowerShellScript True; box True; runs -Master 08403355 -Target monolith True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)converter CodeSha256=AzrzJS\+91y57ylRdqGccFPGqWaqAGLFn/jhItkAQCzE=.*bucket notification rules: 12 \(want 12\); on schwab/08403355/bronze/: 1 \(want 1\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tm1.sh AC3; echo "exit=$?"</invocation><expect>(?s)RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live code object, rule and target carry the new master, 30+ minutes from the other two.
- `AC2`: the converter runs the rebuilt artifact, and the bucket holds exactly one new notification rule.
- `AC3`: the two gateway roles reach the new master's served prefixes and nothing else (bronze and fact_acc controls denied).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-1.taxsma-master-apply.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance>`, and flip the ONE `<status>` tag to `complete` only if all three PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32, workstream APPLY-TM1: OG-tm-1's Phase B re-addressed to the site Z applier (msg 32057), as the PRD v2.0
  item 5(b) "AE lane" placement. Cut after both halves (COO @3998bbe5a7, CTO @4149c01c23) and row S4's source mirror
  (drained @b831326e39: patch @47c3c75f11, repin @7af0b6bc3d, artifact sha256 matched).
- The QA pull (OG-tm-1 Phase B step 11) and AC2 of OG-tm-1 stay with worker ~39 after this order reports.
- A1 (2026-10-09): row Z-S68 ruled (c); Leg A waits on worker ~39's builder-named rule; row id form corrected.
  Graded by no gate limb as a modification.
- Pre-cut: tm1.AC1 base FAIL as expected (ValidateSet 08242234, 08335338; rule absent); ap1.AC3 base FAIL as expected
  (live CodeSha256 v2Bzt..., 11 rules, 0 on the new prefix); tm1.AC3 base FAIL as expected (the new prefixes
  explicitDeny; control denials hold).

<status>pending</status>
<round>32</round>
<workstream>APPLY-TM1</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
