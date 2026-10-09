# NFRA_OPLGTW task order -- `OG-tm-1` -- add the Tax SMA master 08403355 to the daily pull, its silver conversion and the gateway's reader roles (PRD v2.0 item 5(b)-(c), FWD-13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~39</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the live daily-pull rules are cron(45 9,21 * * ? *) (08335338) and cron(15 10,22 * * ? *) (08242234); the new rule must sit at least 30 minutes from both (box-wide SDD session lock). One new EventBridge rule is created; no alarm, monitor or notification.
comp-iam: RUN -- `comp-iam role gateway-schwab-read-role` and `... gateway-schwab-catalog-read-role` return 'No role matching' (the TF index does not carry these builder-named roles), so the APPLIED plane was read instead at the cut: iam:SimulatePrincipalPolicy (r32/checks/tm1.AC3.py) reads explicitDeny on every schwab/08403355/ served and completion prefix for both roles, and the bronze and fact_acc controls denied for both masters. Phase B changes three IAM surfaces by Terraform (the SI2 box role's schwab/08403355/{bronze,_ops,meta/pulls}/* writes as for the other masters; the silver trigger scope; the two gateway roles' new-master prefixes), each named in the never-widen ask with its plan.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is Andrew-direct ~17:4xZ answer 1 and ~21:2xZ "asap" (records @116d52009d, @6233bae5de), PRD v2.0 item 5 (@e43ee663be, signed @5924aaedbe), round-31 analysis section 4a item 7 (@8ca3947b86).
EGRESS CLASS, declared: VENDOR (Schwab SDD) FROM THE SI2 BOX ONLY, in Phase B: the scheduled pull of 08403355 and one ad-hoc QA pull through the same SSM document, on Andrew's answer 1. No egress from the workstation.
</preflight>

## 1. THE CELL -- `OG-tm-1` (decomposition addendum R3-T.30, round 32 item 7)

Your previous order, `OG-en-1`, measured whether Schwab returns files for `08403355` in the same shape as `08335338`.
Andrew's word (2026-10-08 ~17:4xZ, answer 1, verbatim): *"WE should assess if this works and if so, and we get the data
in the same shape (via running it exactly same structure), then it needs to be added to the daily job."* At ~21:2xZ:
*"the tax sma schwab master tested and added to the daily pull and opalgateway asap."* PRD v2.0 item 5: the master joins
only after (a) the list-only run matches the control, (b) the daily puller, its schedule (at least 30 minutes from the
other two), the box's write grant and the silver conversion carry it in the SAME structure as the other two masters,
and (c) a day lands, converts and qualifies.

**STEP 0, the condition (AMENDMENT A1, issuer, 2026-10-09 ~00:0xZ).** `OG-en-1`'s record
(`deliverables/0.9.0_WK_NFRA_OPLGTW~39/g5_enumerate_record.json`, drained @8ba9b3d865) reads: 08403355 `FILES`, 226
files over 2026-09-08..2026-10-08, 13 types, per-type counts EQUAL to the control's on all 13; the control's one extra
type is `slm` (22 files, the `{master}.CS{MMDDYY}.{TYPE}.zip` form), so `types_only_in_08335338` is `["slm"]` and
`grammar_equal` is false only through `slm`. PHASE A proceeds on that record (it changes nothing live). Whether the
`slm` absence is "the same shape" is `1.0.0_SA_CTO~O`'s ruling, given before or with its half; the ask must carry it:
(a) whether the puller, the silver converter or any consumer REQUIRES an `slm` file per master/date (read their code),
(b) what the silver conversion and the completion record do for a master/date with no `slm` input, and (c) the CTO
half's place to state the shape ruling. PHASE B does not start without that ruling at HEAD. Any OTHER difference from
the record above (a third-run read, a changed count) is a STOP: write `W/tm1_condition.result.md` and report.

### PHASE A -- build and plan; NO world act

Every change mirrors the existing two masters exactly; never a new structure.
1. `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` line 31: the ValidateSet gains `'08403355'`. Nothing else.
2. `infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf`: one entry in `local.si2_daily` for
   `"08403355"` with label `"Tax SMA"` and a cron at least 30 minutes from every fire time of the other two
   (e.g. `cron(45 10,22 * * ? *)`: 30 minutes after 08242234 and 60 after 08335338; state your choice and its gaps).
3. `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf` (and `iam.tf` only if it lists masters): the box's
   grants for `schwab/08403355/` exactly as `schwab/08335338/` has them (bronze, `_ops`, `meta/pulls`).
4. `infra/aws/terraform/opal-assets/silver.tf`: `silver_source_scopes.schwab` and a `silver_event_rules` row
   `"schwab-08403355"` exactly as `"schwab-08335338"`; `monolith.tf`'s master list likewise. Do NOT add any
   notification on `schwab/08403355/meta/complete/` (the 49F accelerator is 08335338's alone).
   Read `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` for any hard-coded master list; change it only if
   the converter refuses an unknown master, and then only that list.
5. `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf`: the two gateway Schwab roles reach
   `schwab/08403355/silver/{dim_position,dim_balance,dim_asset,dim_transaction}/` and
   `schwab/08403355/meta/complete/` exactly as they reach the other masters' prefixes, and nothing else.
6. Do NOT edit `org/standards/NFRA_OPLGTW_CONTRACT.json` or its deploy copy (another cell owns them this round).
   Write the exact contract lines the master needs (`masters` entry `"08403355": "TaxSMA"`, four `data_prefixes`, one
   `completion_prefixes`) into `W/tm1_contract_hookup.json`; the issuer adds them at the merge.
7. Plan each of the three roots with `bash .tools/safe-apply.sh` in its PLAN mode (read the script's header for the
   form; never bare `terraform`). Save each plan's summary and resource list to `W/plans/<root>.txt`.
8. Write `W/NEVER_WIDEN_ASK_OG-tm-1.md` in the form of
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-gw-2_20261003.md`: the blast
   radius per resource and per S3 prefix (it must be the new master's keys and the three IAM/rule surfaces only), the
   writer census of `schwab/08403355/` (who will write each prefix), every `ObjectCreated` consumer of those prefixes,
   the rollback per resource, the S3 code-object replacement (before ETag `0017f9b549ca9f8013704f50c4327bed`, after
   the new bytes' MD5) and the ad-hoc QA pull's timing. Halves owed: `1.0.0_SA_CTO~O` and `2.0.0_SA_COO~O`.
9. Commit Phase A and REPORT. Then STOP: the issuer continues you with the signed halves' paths, or with a ruling.

### PHASE B -- after both halves are signed AND site Z's applier has applied (the issuer's continuation names both)

The applies are NOT yours. On Andrew's word of 2026-10-08 ~22:0xZ (relayed by `0.0.0_AB_MSTR~Z`, msg 32057), site Z's
deploys are applied by `0.7.0_AE_CloudOps~Z`. After the halves, the issuer cuts that seat an apply order naming your
Phase A commit, the three roots' targeted resources, the code-object upload and the NEVER-2 ledger entry
`nfra-oplgtw-og-tm-1-taxsma-master`, which that seat opens and closes. You are continued once it reports.
10. Read back from AWS what the applier applied: the three roots' resources, and the code object's ETag equal to the
    MD5 of your edited puller.
11. One ad-hoc QA pull of `08403355` through the SAME path the new rule runs (`AWS-RunPowerShellScript` with the
    rule's own input, read back from `aws events list-targets-by-rule`), outside [09:15,11:05) and [21:15,23:05) UTC
    and outside your new rule's own hour. This is a QA run of a scheduled producer, not a deploy. Then wait for the
    silver conversion and the completion record, and read them.
12. A read-back that disagrees with the signed ask is a BLOCKING row naming `2.0.0_SA_COO~O` and the applier; you
    change nothing in AWS yourself.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~39/`.

## 2. BOUNDS

- No Phase B act before both halves are at HEAD and the applier has reported. You apply nothing and upload nothing. Only `schwab/08403355/` and the three named IAM/rule surfaces move.
- The two existing masters' rules, grants, prefixes and data are unchanged; no other firm's prefix is touched.
- No gateway release and no contract edit here. No alarm, monitor or notification is created.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; override a gate; RDP or the SI2 GUI.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1
infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf
infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf
infra/aws/terraform/canonical-schwab-ec2/iam.tf
infra/aws/terraform/opal-assets/silver.tf
infra/aws/terraform/opal-assets/monolith.tf
infra/aws/terraform/opal-gateway/schwab_reader_iam.tf
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~39/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W39-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after the applier's ledger is closed and the QA day qualified)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tm1.sh AC1; echo "exit=$?"</invocation><expect>(?s)\(a\) code object -Master ValidateSet: \[[^\]]*'08403355'.*\(c\) targets 1; RunPowerShellScript True; box True; runs -Master 08403355 -Target monolith True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tm1.sh AC2; echo "exit=$?"</invocation><expect>(?s)qualified with every object present [1-9]\d*.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-tm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tm1.sh AC3; echo "exit=$?"</invocation><expect>(?s)RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live code object, rule and target carry the new master, 30+ minutes from the other two.
- `AC2`: one 08403355 day landed, converted and QUALIFIED by the gateway's own rules, every served object present.
- `AC3`: the live gateway roles reach the new master's served prefixes and nothing else (IAM simulation, with the
  bronze and `fact_*` denials of both masters as the control).

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-tm-1.taxsma-master-daily-add.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If all three criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the read-back of each applied resource; the code-object ETags; the QA pull's
   command id and the qualified date; the contract hookup lines; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), section 4a item 7; queued after `OG-en-1` in slot ~39, handed by continuation.
- PRD v2.0 item 5(b) says (b) "is placed with an AE lane by the issuer's order". This issuer places it in its own L7
  worker slot under the spine (workers are this project's only L7 executors; the round's TF and release acts have run
  this way since round 3), with the never-widen halves of the CTO and the COO before any act, and names the puller's
  owning lane `0.6.2_AE_PartnerETL` in the ask. Its APPLIES go to site Z's applier `0.7.0_AE_CloudOps~Z` (Andrew-direct
  ~22:0xZ, msg 32057), which is the AE lane the PRD names. Stated to `1.0.0_SA_CTO~O` at the issuance.
- The gateway's contract lines ride `OG-cm-1`'s contract file as a merge hookup; the gateway serves 08403355 only
  after the release that carries that contract (`OG-rl-15` or the next).
- Deeper history for 08403355 than the puller's 30-day lookback is not in this cell; it is a row for the CTO.
- A1 (2026-10-09): STEP 0 rewritten on OG-en-1's record (the slm-only difference); graded by no gate limb as a
  modification of a non-<placeholders> order (GATE (viii) grades only an order declaring <placeholders>; this one
  declares NONE, so viii applies and reads NONE).
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>32</round>
<slot>~39</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
