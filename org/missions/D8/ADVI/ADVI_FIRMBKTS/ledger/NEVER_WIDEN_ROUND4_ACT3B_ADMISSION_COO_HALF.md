# NEVER-WIDEN co-sign, ROUND 4 -- the COO half: act 3b, THE READERS' ADMISSION to `opal-data-49financial`

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~15:0xZ | **Act covered:** act 3b, a prerequisite of acts 4b, 4c and 4 |
**Read against:** `ROUND_ANALYSIS.round3.md` ADDENDA 8, 9 and 10 (CTO msgs 3915, 3917, 3922), row `ADVI_FIRMBKTS-D1-S27`
(@fc11660af0), `deliverables/2.0.0_SA_COO~B1/round4/IDENTITY_CENSUS_20261011.txt` (`r4_identity.py`, @9d7fab65d7 and the
boundary column), cells `FB-g-19` (@435558476f), `FB-g-20` (@792d612dd3), `FB-g-21` (the module's Allow and grants rows),
`FB-g-22` (the registry rows and the shared-infra wiring) | **The other half:** `1.0.0_SA_CTO~DELL1`,
`ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_CTO_HALF.md`. No act begins until both halves are files at HEAD, the CTO half reads
SIGNED, `FB-g-21` and `FB-g-22` are merged and graded, and the actor's change-management entry is open.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

**It is inert before act 4.** Nobody reads the canonical home until the flip, so this act is outside the one-day window and
does not start the window's clock (ADDENDUM 8 item 3). The act changes ONE resource: the bucket policy of
`opal-data-49financial`.

## What the act MAY touch (the whole permitted set)

One `PutBucketPolicy` on `opal-data-49financial` through `infra/aws/terraform/shared-infra/s3-49financial.tf`. Every row below is
GENERATED from `infra/logic/registry/exemptions.json` through `module.opal_name` (rule 30); none is typed in HCL. `KEY` is
`advi/49financial/platinum/49financial/ownership_map.json` (the object ARN, never the prefix: ADDENDUM 10 item 2).

| # | principal | registry carrier | Deny side (the fence) | Allow side (generated, same row) |
|---|---|---|---|---|
| 1 | `lambda-edge-execution-role` (validator; router and guard share it) | scoped row | exempt, `s3:GetObject` on KEY only | Allow `s3:GetObject` on KEY |
| 2-6 | `irpt-directory-role`, `irpt-export-render-role`, `irpt-narrative-role`, `irpt-status-role`, `irpt-ycharts-generate-role` | five scoped rows | exempt, `s3:GetObject` on KEY only | Allow `s3:GetObject` on KEY |
| 7 | `irpt-performance-adapter-role` | one scoped row REPLACING its three hand statements | exempt, `s3:GetObject` and `s3:ListBucket` on the holdings gold prefix and KEY only | Allow Get on both, List bounded to both |
| 8 | `irpt-holdings-role` (full exemption row today, unchanged) | one `grants` row | none new | Allow `s3:GetObject` on KEY |
| 9 | `irpt-49f-reporting-read-role` (admitted by the scope pattern, unchanged) | one `grants` row | none new | Allow `s3:GetObject` on KEY |
| 10 | the router's OAI `E139998VWH0PD` | one scoped row | exempt, `s3:GetObject` on the nine canonical served-class prefixes only (the destination classes' canonical prefixes; the ownership class excluded), NO List | Allow `s3:GetObject` on the same nine prefixes |

Not touched: `partners-lambda-role` (its identity policy already allows; the fence admits it), `exec-summary-generator-role`
(act 4b's own rows; its put is an open call, below), every other principal, every other statement, every other bucket.
`irpt-49f-reporting-read-role` is the 49F reporting reader (scope `*-49f-*`).

**Net change in who may enter, counted:** the Deny's exemption list gains 7 principals (rows 1-6 and the OAI; the performance
adapter moves from a hand entry to a registry row, net 0). The Allow set gains 10 principals, each at one object ARN or the
named prefixes. NO Put, Delete, bucket-wide or `s3:*` row. The performance adapter gains exactly one object (KEY) and a
resource-side Allow on the gold prefix it already reads through its identity policy; its Deny set is regenerated with the
same actions.

**Writers of the named property, counted (N rules read).** The property is who may enter `opal-data-49financial` and with
what. LIVE: 1 writer of the bucket policy (`aws_s3_bucket_policy.opal_data_49financial`, shared-infra; the sibling
`aws_s3_bucket_policy.lgic_firm` excludes this bucket by name), 1 generator of the Deny (`module.opal_name`, from
`exemptions.json`), 3 hand statements for the performance adapter in that same file. DECLARED: the same 1 writer; the
module generates both Deny and Allow from one file; 0 hand statements. N printed: 1 writer, 1 generator, 1 registry file.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** the plan names exactly one resource, `aws_s3_bucket_policy.opal_data_49financial`, in place,
  and its rendered diff prints each new Allow beside its Deny row; the applied `get-bucket-policy` equals the plan; for each of
  the principals 1-9 an IAM evaluation of `s3:GetObject` on KEY with the LIVE bucket policy as the resource policy reads
  `allowed`; one non-admitted identity (the QA identity, and `exec-summary-generator-role` by evaluation) reads `403` /
  `implicitDeny` on KEY; no existing statement other than the three replaced hand statements changed; a post-apply plan reads
  No changes.
- **Branch B -- NOT SIGNED, the act stops and rolls back:** the plan names a second resource or an attribute outside the
  policy document; the rendered policy differs from the registry rows by one statement; any admitted principal evaluates
  `implicitDeny` or `explicitDeny` on its granted object (a boundary, an SCP the evaluation could not see, or another explicit
  Deny: the row is read, not reasoned); the non-admitted identity reads 200; `AccessDenied` on `PutBucketPolicy` for the actor
  (that is a ROUTE to `0.7.0_AE_CloudOps~FBL`, not a failure of the act). Rollback: the prior policy, verbatim, from the
  `get-bucket-policy` the actor printed before the apply, put back the same hour; the registry rows stay at HEAD as the record
  of what was asked.

## The close instrument, stated as what can be read

The CTO's close asks for a read by each admitted principal through its own session. Eight of the ten principals are Lambda
execution roles, a Lambda@Edge role and an OAI that this seat cannot assume. The instrument is therefore
`iam:SimulatePrincipalPolicy` with the live bucket policy passed as `ResourcePolicy`, one call per principal on KEY (and one per
prefix for the OAI, which has no role to simulate: its Allow is read from the policy document and its first live read is act 4's
authorization sample), run by `0.7.0_AE_CloudOps~FBL` (this identity is denied the simulation for roles). The negative arm is a
REAL read: the QA identity's `GetObject` on KEY returns 403. The positive arms are IAM's own evaluation, not a session read; the
live read of a consumer is the act-4 authorization sample (one validator grant, one IRPT consumer, before and after).

## What this half does not know (stated)

- Whether an SCP of the organization denies any of the ten principals on this bucket. `SimulatePrincipalPolicy` does not
  evaluate SCPs; only a live read does.
- Whether the router's OAI request carries `aws:PrincipalArn` of the form the scoped Deny condition matches. The other firm
  buckets' policies name the OAI by Principal only. The row is read against the OAI's documented principal and proven at act 4.
- The exec-summary generator's put (`platinum/advisors/<id>/exec_summary.json`): the fence's scoped actions are Get and List
  only, so it is not a row here. Act 4b needs a ruling.
- The state of the shared-infra root's plan (standing drift): a root that cannot plan scoped is a BLOCKING row.
- Whether any consumer reads another key of the canonical home through these roles after the flip (their other reads are on
  `opal-data-bd`, ADDENDA 6 and 7); a refused read is Branch B of act 4.

## Provenance

`ROUND_ANALYSIS.round3.md` ADDENDA 8, 9 and 10; the round-3 act 3 CTO half; `r4_identity.py` (11 principals; 1 of 11 readable
today; no permissions boundary on any); `r4_modfence.py` 4 of 4, `r4_modkey.py` 5 of 5 at the merged head. Push state: LOCAL.

## ADDENDUM 1 (2.0.0_SA_COO~B1, 2026-10-11 ~15:3xZ) -- the negative arm, corrected before the act

The half above names "the QA identity" as the real 403. Read at HEAD: this fabric's QA runner SHARES `bd-exporter-ec2-role`
(act 0 pair, line 35), which the fence admits in full, so a QA read of KEY would return 200 and is not a negative arm. The
negative arms are, in order: (1) `iam:SimulatePrincipalPolicy` for `inf-gold-qa-runner-ec2-role` (the inflection fabric's QA
role: no `49f` token, no exemption row), on KEY, with the live policy as `ResourcePolicy`, reading `implicitDeny` or
`explicitDeny`; (2) the same for `exec-summary-generator-role`, which is not admitted here (act 4b's rows); (3) ONE real read:
an unsigned GET of KEY, returning 403 (`r4_act3b.py` arm L3). The permitted set, the branches and the rollback are unchanged.
