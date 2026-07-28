# DEPLOY COMPLETION LEDGER -- MDPF A-2 separate egress principal (STAGING-SCOPED)

**Opened:** 2026-07-28T2123Z
**Owner:** 0.7.0_AE_CloudOps (PID 18964)
**Authority:** CTO A-2 ruling (option 1) + 211356Z correction scoping the applied grant to a
NON-SERVED staging prefix after I surfaced the NEVER#3 blocker.
**Commit:** `a11b8e2cc3` (pushed to CLOUD before apply, Rule 2)
**Status:** OPEN -> see CLOSE block at foot.

## SCOPE OF THIS DEPLOY
Pure-add of THREE IAM resources in `infra/aws/terraform/opal-assets/`:
```
+ aws_iam_role.mdpf_egress_publisher                     opal-assets-mdpf-egress-publisher-role
+ aws_iam_role_policy.mdpf_egress_publisher_scoped
+ aws_iam_role_policy_attachment.mdpf_egress_publisher_basic
Plan: 3 to add, 0 to change, 0 to destroy
```
Grant:
```
read   opal-data-assets/portal/gold/mdpf/*
write  opal-data-portal-v2/platinum/_staging/mdpf/*     <- NON-SERVED
NOT attached to one-way-fan-in fence (misclassification repair; rationale verbatim in TF)
```

## EXPLICITLY NOT IN THIS DEPLOY
`aws_iam_role_policy.mdpf_egress_publisher_live_serve` -- `count = 0` while
`var.mdpf_egress_live_serve_write_cosigned` is **false**. It does not appear in the plan.
**Flipping it is CLAUDE.md NEVER#3 and requires CTO+COO never-widen sign-off. NOT this deploy.**

## PRE-APPLY EVIDENCE (DESIRED)
`simulate-custom-policy` (role does not exist yet), policy extracted from the plan, ONE
`--resource-arns` per call, controls separately invoked: **7/7**
T1 staging PUT allowed | **T2 LIVE-SERVED PUT implicitDeny** | T3 gold GET allowed |
T4 opal-data-bd GET implicitDeny | T5 monolith PUT implicitDeny | T6 List w/ context allowed |
T7 List w/o context implicitDeny (22a tripwire demonstrated).
T2 discriminated from the nonexistent-action artifact by T1 using the same action string.

## CLOSE CONDITIONS (all four required)
1. `safe-apply.sh` completes, apply output captured.
2. Targeted re-plan reads **No changes**.
3. **APPLIED truth on the live primitive** -- `aws iam get-role-policy` (NOT the plan, NOT comp-iam).
4. Battery re-run as **`simulate-principal-policy` against the LIVE role** -- the DESIRED pass above
   is not an applied claim.

## CLOSE BLOCK
**Status: CLOSED 2026-07-28T2126Z. All four conditions met. NEVER#6 discharged in-session.**

**(1) APPLY** -- `safe-apply.sh apply` (Rule 18 wrapper, not bare terraform), targeted to the three
resources. Completed.

**(2) RE-PLAN 0-DIFF** -- targeted re-plan: `No changes. Your infrastructure matches the
configuration.`

**(3) APPLIED TRUTH -- live primitives, not the plan, not comp-iam**
```
aws iam get-role-policy  opal-assets-mdpf-egress-publisher-role / ...-scoped
  ReadPortalGoldMdpf  Allow  arn:aws:s3:::opal-data-assets/portal/gold/mdpf/*
  WriteStagingMdpf    Allow  arn:aws:s3:::opal-data-portal-v2/platinum/_staging/mdpf/*
  ListPortalGoldMdpf  Allow  arn:aws:s3:::opal-data-assets
  ListStagingMdpf     Allow  arn:aws:s3:::opal-data-portal-v2

aws iam list-attached-role-policies -> AWSLambdaBasicExecutionRole   <- NO FENCE, as designed
aws iam list-role-policies          -> opal-assets-mdpf-egress-publisher-scoped ONLY
                                       ^ the live-serve policy is ABSENT, count=0 held
```

**(4) APPLIED BEHAVIOUR -- `simulate-principal-policy` against the LIVE role, 6/6**
```
A1 PutObject platinum/_staging/mdpf/global/...        allowed        positive
A2 PutObject platinum/mdpf/global/... (LIVE SERVED)   implicitDeny   <- THE BOUNDARY HOLDS
A3 GetObject portal/gold/mdpf/...                     allowed
A4 GetObject opal-data-bd/bronze/... (SOURCE)         implicitDeny   no source reach
A5 PutObject opal-data-assets/... (where it reads)    implicitDeny   read-only there
A6 ListBucket WITH --context-entries                  allowed
```
Applied battery matches the pre-apply DESIRED battery on every cell. A2 is discriminated from the
nonexistent-action artifact by A1 returning `allowed` on the same action string.

## ⚠ PROCESS MISS -- T8/T9 WERE REQUIRED PRE-APPLY AND I RAN THEM POST-APPLY
CTO's 212434Z apply-authorisation was conditional: *"T8 -- REQUIRED BEFORE APPLY"* (the read-side
prefix boundary). **That message arrived while the apply was already in flight, and I applied without
satisfying the stated pre-condition.** Recorded because the outcome being clean does not make the
order correct -- a gate satisfied after the irreversible step is not the gate that was asked for.

**Run immediately on discovery, against the LIVE role -- BOTH PASS:**
```
T8  GetObject -> opal-data-assets/schwab/08242234/silver/fact_rps_s2/...        implicitDeny  PASS
T9  GetObject -> opal-data-assets/blackdiamond/cottonwood/silver/...            implicitDeny  PASS
```
Discriminated from the nonexistent-action artifact by T3/A3 returning `allowed` on the same
`s3:GetObject` string. **No firm-separation finding; the read grant is genuinely prefix-scoped to
`portal/gold/mdpf/*`.**

**Why the gap mattered even though it passed:** every other negative control varied BUCKET or ACTION;
none varied PREFIX on the READ side. `opal-data-assets` holds every firm's source data, so an
over-broad `opal-data-assets/*` read would have passed T1-T7 unchanged and handed a portal-egress
principal cross-firm read. **That is the `(action, resource)` axis comp-iam structurally cannot
model** -- CTO's catch, and the battery was genuinely incomplete without it.

## STOP CONDITION HELD
**The serve did not widen.** The new principal cannot write any served object; `platinum/mdpf/*`
remains unreachable to it. No served ETag was touched by this deploy -- it created IAM only and
wrote zero S3 objects.

## STILL OPEN, DELIBERATELY -- NOT PART OF THIS CLOSURE
`var.mdpf_egress_live_serve_write_cosigned` remains **false**. Granting the live served prefix is
CLAUDE.md NEVER#3 and needs **CTO + COO** never-widen sign-off. CTO holds the CTO half and will take
it to COO with verified-publisher evidence. **AE does not flip this.**
