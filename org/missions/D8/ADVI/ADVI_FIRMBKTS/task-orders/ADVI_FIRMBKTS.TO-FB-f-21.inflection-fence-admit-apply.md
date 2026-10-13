# ADVI_FIRMBKTS task order -- `FB-f-21` -- THE INFLECTION FENCE ADMITS `irpt-performance-adapter-role`, READ-ONLY, ONE PREFIX (ONE BUCKET POLICY, `1 to change`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-21</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one bucket policy changes in place; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the actor at step 1 (the laptop identity applied the other firm-bucket policies of this project's pairs; the simulate of step 2 is its own read). No grant is created beyond the one scoped row.
comp-adversary: RUN by the issuer -- the row renders THREE added statements on `opal-data-inflection` and none on any other bucket (`terraform console`, no provider: 49financial's 20 scoped statements byte-identical before and after). Blindness: the plan and the simulate are the actor's; dell1's identity cannot simulate.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-f-21` (round 4, workstream `INFLFENCE`; CLIENT-FACING since 2026-10-13 00:04Z: run it NOW)

`irpt-performance-adapter` is refused `s3:ListBucket` on `opal-data-inflection` by `DenyForeignFirmPrincipals`: its role
`irpt-performance-adapter-role` is not in that statement's exception list (the 10-08 fence admitted `irpt-holdings-role` only). The
deny is latent, not a deploy effect (CloudTrail, adapter logs). The cluster lead's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INFLECTION_PERFORMANCE_DENY_OWNER_APPLIER_AND_PAIR_20261013.md` names ADVI_FIRMBKTS the owner and
you the applier. THE PAIR: CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_INFLECTION_FENCE_ADMIT_IRPT_PERFORMANCE_ADAPTER_20261013.md` @354a12bc04 and COO half `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_INFLECTION_FENCE_ADMIT_IRPT_PERFORMANCE_ADAPTER_COO_HALF.md`, both SIGNED; read both in full first.

The registry row is merged on `box/dell1` (`infra/logic/registry/exemptions.json`, key `opal-data-inflection`: principal
`irpt-performance-adapter-role`, actions `s3:GetObject` and `s3:ListBucket`, prefix `irpt/inflection/gold/holdings_performance_daily/`),
commit `61cc536c29`. Take it into your checkout first (`git merge-base --is-ancestor 61cc536c29 HEAD`).

### 1a. The steps, in order

0. **Gate.** Both halves read SIGNED at their pins; `61cc536c29` is an ancestor of HEAD; the registry row reads as above and `python lib/opal_naming.py validate` exits 0. Any not so: STOP, a BLOCKING row.
1. **Read before you write, print each:** `aws s3api get-bucket-policy --bucket opal-data-inflection` saved to the entry's evidence folder (the rollback document); the identity side, `simulate-principal-policy` of `arn:aws:iam::313476888478:role/irpt-performance-adapter-role` for `s3:ListBucket` on `arn:aws:s3:::opal-data-inflection` with `s3:prefix` = `irpt/inflection/gold/holdings_performance_daily/` (WITHOUT the resource policy: the identity side alone): it must read allowed. If the identity policy does not allow it, the row alone cures nothing: STOP and say so.
2. **The entry.** Open the change-management entry BEFORE the write (scope: the `shared-infra` root, ONE resource `aws_s3_bucket_policy.lgic_firm["inflection"]`, the pair, the saved prior policy, rollback = `put-bucket-policy` of it). Commit it and its sentinel first.
3. **Plan, scoped.** `.tools/safe-apply.sh` plan limb in `infra/aws/terraform/shared-infra` with `-target='aws_s3_bucket_policy.lgic_firm["inflection"]'`: `Plan: 0 to add, 1 to change, 0 to destroy`, and the policy document's diff is exactly THREE ADDED statements (`DenyScopedExemption1AnyOtherAction`, `DenyScopedExemption1ObjectsOutsidePrefix`, `DenyScopedExemption1ListingOutsidePrefix`). Any other resource, or a removed or changed statement (a hand edit since 10-08): STOP, a BLOCKING row.
4. **Apply** through `.tools/safe-apply.sh` on that saved plan (never a bare `terraform apply`). Print its start and end times.
5. **Read after, print each:** (a) the live policy carries the three statements; (b) `simulate-principal-policy` WITH `--resource-policy` = the live policy: `s3:ListBucket` on the prefix reads allowed; `s3:ListBucket` on another Inflection prefix reads denied; `s3:PutObject` under that prefix reads denied; a foreign-firm principal not on the list still reads explicitDeny; (c) one Inflection holdings-performance request answers 2xx, if a seat that can read the answer is live (if not, say so: the log read in AC3 is the measure); (d) the `explicit deny` lines in `/aws/lambda/irpt-performance-adapter` stop.
6. **Close the entry** with the outputs, and a Branch B rollback if (b) reads wrong (re-put the saved policy, read it back).

## 2. BOUNDS

1. One bucket policy, three statements, one principal, one prefix, read-only. No other bucket, resource, principal, action or prefix.
2. No apply if the plan names a second resource or changes anything but the three added statements.
3. No change to the adapter's code or role; no invalidation, no alert, no monitor.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-f-21.inflection-fence-admit-apply.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-21"><invocation>cd infra/aws/terraform/shared-infra &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target='aws_s3_bucket_policy.lgic_firm["inflection"]' 2&gt;&amp;1 | grep -E "^(Plan:|No changes)"</invocation><expect>^No changes\.</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-21"><invocation>timeout 60 aws s3api get-bucket-policy --bucket opal-data-inflection --query Policy --output text | grep -o "DenyScopedExemption[0-9]*[A-Za-z]*" | sort -u | paste -sd" " -</invocation><expect>^DenyScopedExemption1AnyOtherAction DenyScopedExemption1ListingOutsidePrefix DenyScopedExemption1ObjectsOutsidePrefix$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-21"><invocation>timeout 90 aws logs filter-log-events --log-group-name /aws/lambda/irpt-performance-adapter --region us-east-1 --start-time $(( ($(date +%s) - 600) * 1000 )) --filter-pattern '"explicit deny"' --query "length(events)" --output text</invocation><expect>^0$</expect></criterion>
</proof_of_spec>

AC1 reads that the scoped plan is empty after the apply; AC2 that the live policy carries exactly the three scoped statements; AC3 that no
`explicit deny` line landed in the last ten minutes (a zero is only as strong as the traffic: step 5(c) prints whether a request ran).
Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry in the SAME commit as the proof instance; flip `<status>` to `complete` only when AC1 to AC3 pass.
Report once to `2.0.0_SA_COO~B1` through the laptop manager: the plan's three-statement summary, the simulate lines, the entry id,
AC1 to AC3 outputs, whether step 5(c) ran, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the cluster lead's ruling @af61c60689 (client-facing). Workstream `INFLFENCE`. If `0.7.0_AE_CloudOps~FBL` cannot
take it this hour, dell1's own CloudOps lane applies under the same pair (one applier, named in the ledger), but dell1's identity
cannot simulate: the plan and the policy read would carry the proof.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~01:3xZ, on `0.7.0_AE_CloudOps~FBL`'s row S22):** the issuer typed the resource address with the
BUCKET name as its `for_each` key; the real key is `inflection`, so `-target` and AC1 as written matched no instance (AC1 read vacuous). Every
occurrence now reads `aws_s3_bucket_policy.lgic_firm["inflection"]`. `0.7.0_AE_CloudOps~FBL` planned and applied with the real key
(01:17:20Z-01:18:05Z, 0 add 1 change 0 destroy). Step 5(c) was NOT RUN (no invocation of the adapter after the apply): the 2xx
read-back is owed by the seat that can request an Inflection performance answer (named in the issuer's message); AC3's zero is labelled
"no traffic behind it" until then.

<status>complete</status>
<round>4</round>
<workstream>INFLFENCE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-21</to_id>
<slot>~FBL</slot>
<fabric>laptop</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
