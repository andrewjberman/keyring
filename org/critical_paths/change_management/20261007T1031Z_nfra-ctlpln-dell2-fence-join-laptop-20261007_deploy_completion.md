# Deploy Completion Record
**Date opened:** 2026-10-07T10:31:24.067865+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN round 4 CT-d-2 dell2 fence join -- BOX: THE LAPTOP. AMENDMENT 1 form: ONE targeted safe-apply of exactly TWO resources, aws_s3_bucket_policy.opal_data_49financial and aws_s3_bucket_policy.lgic_firm[inflection]. The COTTONWOOD fence is DELIBERATELY NOT APPLIED: its policy carries three unapplied ADVI_COTBKF restricted-CRM-prefix statements (8e58736597, 'nothing applied') that no -target can separate from the dell2 change, so the CTO ruled it waits for the rider's own never-widen pair (1.0.0_SA_CTO~DELL2 / 2.0.0_SA_COO~C2). Both halves amended and signed: COO @66730b8e06, CTO @341eeb04bd. Plan measured 0 to add, 2 to change, 0 to destroy.
**Authored by:** 0.7.0_AE_CloudOps~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | targeted safe-apply of the two fence bucket policies at the laptop | plan reads EXACTLY 0 to add / 2 to change / 0 to destroy on aws_s3_bucket_policy.opal_data_49financial and aws_s3_bucket_policy.lgic_firm[inflection]; each diff is the single added principal arn:aws:iam::313476888478:user/cloudops-dell2-agent-user inside DenyForeignFirmPrincipals ArnNotLike; the cottonwood POLICY resource absent from the plan; safe-apply completes 0 added 2 changed 0 destroyed |  | OPEN |
| V1 | verify | AC1 fence-join static check | python infra/aws/terraform/shared-infra/tests/check_dell_fence_join.py reads rows=3/3 typed_in_tf=0 cross_firm_leaks=0 ... ok=True |  | OPEN |
| V2 | verify | live-vs-prior document comparison, all three buckets | the 49financial and inflection LIVE policies each equal their saved PRIOR document plus exactly the one dell2 principal (parsed comparison + planted-mutant control); the COTTONWOOD live policy is BYTE-EQUAL to PRIOR_bucket_policy_opal-data-cottonwood_20261007.json (sha256 49f1cf260f0f18d5f52244c2a48bb5159765dd293633b750a9f0fbad39dcc7ae) as the proof this act did not touch it |  | OPEN |
| V3 | verify | simulator arms against each LIVE bucket policy | cloudops-dell2-agent-user s3:GetObject allowed on 49financial and inflection; dell2 STILL NOT allowed on cottonwood (the new negative arm); cloudops-dell1-agent-user NOT allowed on either applied bucket; one unlisted previously-refused principal named from the census still refused; one previously-admitted principal still allowed (the control) |  | OPEN |
| V4 | verify | AC2 census + AC3 re-plan + the expected cottonwood pending plan | dell_fence_census.py --live reads gap_dell2=1 (cottonwood remains), dell2_admitted 23/24, dell1_admitted unchanged 21/24, gap_dell1 still 0; re-plan of the two targets -detailed-exitcode reads exit=0; and a plan of lgic_firm[cottonwood] ALONE still shows the dell2 principal plus the three rider statements pending -- reported as EXPECTED, not drift |  | OPEN |

## Log

- 20261007T103124Z OPENED by 0.7.0_AE_CloudOps~E with 5 leg(s)

---

## BOX

**THE LAPTOP.** Executor `0.7.0_AE_CloudOps~E`, seated by `2.0.0_SA_COO~C` under task order
`NFRA_CTLPLN.TO-APPLY-4.dell2-fence-join-apply-laptop` @f35aab83cc, AMENDMENT 1 @aefcf32c11 (the amendment governs where it and the
order differ). Applying identity, read before the act: `arn:aws:iam::313476888478:user/Andrew_Berman`.

## WHY THIS IS A TWO-BUCKET APPLY AND NOT A THREE-BUCKET ONE

The first (three-target) plan was REFUSED by this seat at the plan gate and nothing was applied; no ledger entry was opened, because
step 4 sits behind the gate. Recorded at commit `54295756ad`, reported as msg 106147.

The counts were right (0 add / 3 change / 0 destroy) and all three fences gained the dell2 principal, but the cottonwood policy's diff
ALSO added three whole statements -- `DenyRestrictedReadExceptReaders`, `DenyRestrictedListExceptReaders`,
`DenyRestrictedWriteExceptBreakglass`, restricting `opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/*` to two named
principals. Those were declared by `ADVI_COTBKF.TO-CB-d-4` at `8e58736597` (`0.9.0_WK_ADVI_COTBKF~15`), whose own commit subject ends
"nothing applied". That commit is an ancestor of `526a1a27ac`, the trunk the COO half cites as its read point, so the statements were
already in `s3-lgic-firm-buckets.tf` when both halves were written; neither half saw them because neither seat planned the root.
Condition 1 of both halves ("each policy's diff is the one added principal and nothing else") voided the act, as written.

**No `-target` can separate them: the rider sits inside the SAME resource as the dell2 change.** The CTO ruled form (a): apply the two
clean resources now; the cottonwood fence is applied later, once, carrying BOTH the rider and the dell2 principal, under the rider's
own never-widen pair (`1.0.0_SA_CTO~DELL2` / `2.0.0_SA_COO~C2`).

**The cottonwood registry row stays in `exemptions.json`** (landed @e7ac51a04c). It is unapplied, by design, until that second apply.
**Until then dell2 remains fenced out of the cottonwood bucket**, and IRPT work reading Cottonwood firm data keeps using the laptop
read proxy.

## BLAST RADIUS -- what this act may touch

Two S3 bucket policies. No IAM object, no other bucket of the 24 the census reads, no object, no served output.

| # | resource | bucket | action |
|---|---|---|---|
| 1 | `aws_s3_bucket_policy.opal_data_49financial` | `opal-data-49financial` | one principal added to `DenyForeignFirmPrincipals` `ArnNotLike` |
| 2 | `aws_s3_bucket_policy.lgic_firm["inflection"]` | `opal-data-inflection` | the same one principal added |
| -- | `aws_s3_bucket_policy.lgic_firm["cottonwood"]` | `opal-data-cottonwood` | **NOT APPLIED, deliberately** (see above) |

**What dell2 gains, at full width, not as a read-only grant:** the fence stops refusing it on those two buckets, so its own two IAM
policies then apply there -- read, list and PUT of objects, plus the create policy's bucket-level configuration actions. Its own Deny
statements still refuse any delete of an object or bucket and any lifecycle configuration on `opal-data-*`.
**dell1 gains nothing:** it is admitted to no bucket (0 of 7 registry keys), and the census found `gap_dell1=0`.

## ROLLBACK PER KEY -- S3 VERSIONS NO BUCKET POLICY

There is no prior version to restore from AWS, so the saved documents ARE the rollback. Saved BEFORE the apply, with SHA-256:

| bucket | prior document | sha256 | bytes |
|---|---|---|---|
| `opal-data-49financial` | `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PRIOR_bucket_policy_opal-data-49financial_20261007.json` | `8eebec0e403200073f43133e2990a23fdb33ff16cd240624258792c3fcd21b25` | 2513 |
| `opal-data-inflection` | `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PRIOR_bucket_policy_opal-data-inflection_20261007.json` | `96ddbfe2badb1a8eb4039eb110962761ce287221a8c55fa140eee942ba592285` | 501 |
| `opal-data-cottonwood` (not applied; saved as the UNTOUCHED control) | `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PRIOR_bucket_policy_opal-data-cottonwood_20261007.json` | `49f1cf260f0f18d5f52244c2a48bb5159765dd293633b750a9f0fbad39dcc7ae` | 501 |

The saved bytes are the EXACT document string S3 returns, so `s3api put-bucket-policy --policy file://<saved>` replays it
byte-for-byte. Primary rollback: `4.0.0_SA_CRO` removes the two rows in its own lane and the same targeted `safe-apply` runs again.
Same-window fallback if that route is blocked: `put-bucket-policy` of the saved document, one bucket at a time, then the Terraform
re-apply to reconcile state. **Triggers:** AC1 failing, an AC3 regression, either live policy ceasing to equal
prior-plus-one-principal, or the cottonwood live policy ceasing to be byte-equal to its saved document.
**Not undone by any rollback:** anything dell2 writes to those two buckets while the grant stands.

## BOTH BRANCHES

- **Applied:** dell2's seats read and land on the 49financial and inflection buckets under their own policies; the read-proxy through
  the laptop ends for those two; dell2 stays fenced out of cottonwood.
- **Not applied, or the plan differs:** dell2 stays fenced out of all three; the registry rows stay unapplied and the CRO is told.

## PRE-APPLY EVIDENCE IN HAND

- `exemptions.json` last touched exactly `e7ac51a04c`, authored `4.0.0_SA_CRO` -- CTO condition 4 (the owning lane wrote the rows).
- `lib/opal_naming.py validate`: OK, 53 system rows, 13 scope rows, 41 warnings, **0 refusals**.
- The two `.tf` files are byte-identical at `3ec42c56bf` and HEAD, proven POSITIVELY by blob hash (`rev-parse <ref>:<path>` EQUAL both
  files) rather than by an empty diff, because `3ec42c56bf` never touched them -- so the order's "diff prints nothing" gate is
  satisfied for a different reason than it reads. A control proves the pathspec instrument can see a change on these exact paths
  (`8e58736597^..HEAD` is non-empty).
- AC1: `FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=0 evaluator_allowed=3/3 negative_arm=denied other_rows_changed=0
  validator=ok ok=True`.
- Registry census: dell2 admitted to exactly 3 of 7 bucket keys; dell1 to 0.
- Two-target plan, read-only: `Plan: 0 to add, 2 to change, 0 to destroy`; 2 resource blocks (`grep -c`, denominator printed);
  19 changed lines of which every ADDED line is the dell2 principal and NO line is removed; the cottonwood POLICY resource absent
  (0 matches, with a working control: the same pattern for inflection matches 2); zero rider Sids in the plan; zero
  `must be replaced` / `will be destroyed` / `-/+` markers. Saved:
  `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PLAN_shared-infra_dell2_fence_join_TWOBUCKET_20261007.txt`.
- The targeted argv was ECHOED BACK before use (the amendment requires it): both `-target=` strings arrive intact through MSYS,
  brackets and quotes preserved.

## THE ROOT'S INIT -- NOT A STOP, and what it revealed

The order made this the executor's first read, with a registry provider FETCH as a STOP. **No fetch was made and none was needed.**
`terraform v1.15.8`; `.terraform.lock.hcl` pins `hashicorp/aws 5.100.0`; the local plugin cache holds exactly that version. Init ran
with registry installation DISABLED (`-plugin-dir=C:/Users/AndrewBerman/.terraform.d/plugin-cache`) and reported "Using hashicorp/aws
v5.100.0 from the shared cache directory", rc=0.

`-reconfigure` was required because the on-disk backend record is an older structure. Checked BEFORE using it: the record's bucket,
key and region (`opal-313476888478-terraform-state` / `shared-infra/tfstate` / `us-east-1`) are identical to the declared block at
`main.tf:11-15`, so it re-pointed at the SAME state. The control on that: `state list` then returned 252 resources including all three
fence policies.

Surfaced as row `NFRA_CTLPLN-S12` (@a162b02c50): the root's `.terraform/plugin_path` had pointed at a DELETED Desktop tree belonging
to a different root, which is why `.terraform/providers` was empty. Corrected as a side effect of the required init; census after:
1 `plugin_path` file across `infra/aws/terraform`, 0 carrying a foreign path.

## INSTRUMENT NOTES carried into the verify legs

`simulate-principal-policy` has four false-DENY modes (multi-ARN in one call, unevaluated `Condition`, unvalidated action names,
wrong-grain ARN) and one false-ALLOW mode measured on THIS project: it matches the ARN against the policy's `Resource` patterns and
never asks whether the ARN names anything. So leg V3 passes ONE resource ARN per call, runs its controls as SEPARATE invocations, and
reads an `allowed` as "the policy admits an ARN of that shape", never as proof an object exists.
For a bucket-policy question the resource-policy arm is what decides, so each call supplies the LIVE policy document explicitly
rather than relying on the principal's identity policy alone.
