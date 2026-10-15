# NEVER-WIDEN co-sign, ROUND 88 -- the COO half: ONE job reads the restricted CRM zip (grant, job, withdrawal)

**Signer:** `2.0.0_SA_COO~C1` | **Date:** 2026-10-15 ~19:4xZ | **Acts covered:** (1) a targeted Terraform apply that adds ONE IAM role and ONE reader exception; (2) the matching job that assumes the role and reads ONE key in memory; (3) the withdrawal of both, the same day the job ends |
**Authority:** Andrew-direct 2026-10-15 ~19:0xZ, VERBATIM: "I agree with (a), let's see what we can do with that for now." (laptop record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_190xZ_D3CC_A_ONE_JOB_READS_RESTRICTED_CRM_ZIP.md` @6e96dd543a, relayed by `0.0.0_AB_MSTR~DELL1` msg 6143); the CTO's ruling `ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` amendment 5 (msg 6146) |
**The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_CTO_HALF.md` (not yet written when this half was signed) |
**Read against:** `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` lines 185-290 at HEAD (the three CRM Deny statements, `lgic_crm_readers`, `lgic_crm_writers`, the break-glass role and its inline policy), and the applied state recorded in rows `ADVI_COTBKF-D2-S105` (the break-glass role exists, created 2026-10-11T09:05:05Z) and `D2-S91` |

**Verdict:** SIGNED for the blast radius below, and ONLY it, once the CTO half is signed. Until then no apply is planned for application and the job is not staged.

## What changes in the world

Today the CRM zip's prefix `commonwealth/<firm>/bronze/crm/` in the firm bucket denies every read except the console user and the break-glass role. No agent can read it (FWD-7). After the act, for the length of ONE job: a new role, assumable by the agents' shell user, can `GetObject` the ONE key
`s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip`, and the read-Deny lets that role's ARN through. After the withdrawal, both are gone and a re-plan reads no changes.

## What the act MAY touch (the whole permitted set)

| object | what moves | bound | rollback |
|---|---|---|---|
| `aws_iam_role` (new; name from `lib/opal_naming name()` via the `opal_name` module, never typed; a builder refusal is a registry row to add, `infra/logic/registry/`) and its inline policy | created | trust: ONE principal, the agents' shell user (the user the console-only sign-in's note names as the agents' identity), `sts:AssumeRole`, no wildcard, no service; max session 3600 s; policy: `s3:GetObject` on the one key above, NOTHING else (no `GetObjectVersion`, no `List`, no `Put`) | `terraform destroy -target` of the same two addresses, or the withdrawal order |
| the firm bucket policy, the statement `DenyRestrictedReadExceptReaders` | the new role's ARN is added to the readers list that statement's `ArnNotLike` reads (`lgic_crm_readers`) | the READ deny only. The LIST deny (`DenyRestrictedListExceptReaders`) and the WRITE deny (`DenyRestrictedWriteExceptBreakglass`) are unchanged: the role neither lists nor writes. The lift is prefix-wide in the bucket policy; the EFFECTIVE access is the intersection with the role's own allow, which names the one key | remove the ARN; a re-plan then reads no changes |

**The honest statement of the exception's width:** an IAM Deny cannot be lifted for one key inside a prefix by resource; the bucket-policy exception is therefore prefix-wide for the READ deny, and the ONE-KEY bound is the role's allow policy (an explicit Deny wins over an Allow, a missing Allow is a deny: any other key under the prefix stays unreadable to the role). The ruling's "for that key only" is met on the effective access, and this half signs that reading. If the CTO reads it as a requirement for a bucket-policy exception scoped by resource, the apply is not planned until the CTO says so.

**No other object moves**: not the break-glass role, not the console user, not `lgic_crm_writers`, not any other bucket policy statement, not any other firm bucket. `terraform plan` before the apply must show exactly these changes and no others; any other change is the stop.

## Writers of the named property, counted

The property is "who may read an object under the restricted CRM prefix". **N = 1 writer file** (`s3-lgic-firm-buckets.tf`) and **1 rule**: the Deny reads `local.lgic_crm_readers`; to read, a principal must be in that list. This act adds one entry to it. (Account-level IAM Allow policies are not writers of the property: the Deny governs any principal not on the list.) The population measured is the repository's Terraform; an out-of-band edit of the bucket policy would not appear.

## Both branches named

- **The CRM zip has not been landed** (Andrew lands it himself through the break-glass role; the CRO's read could not tell, 403 on `head-object`): the role's `head-object` returns 404. The job records `NOT_LANDED`, reads nothing, and the withdrawal runs the same day. The grant is not kept "for later".
- **The zip is landed:** the job reads it once, in memory (never to disk), and writes only the allow-listed columns (below).
- **The role is assumed and the read is refused:** the job records the exact error and stops; withdrawal runs.

## What the job MAY emit

Account-link rows with EXACTLY the columns `commonwealth_account, bd_account_id, rule, tier` (ids, a rule name, a tier; these are the columns the crosswalk already carries), plus counts. No CRM column value leaves the job: no name, tax id, date of birth, address, driver's-license or passport number, and no value of any other CRM column. A criterion reads the output's column set against that allow-list and fails on any other column. The job's run record is the log: start, end, role, the one key, row counts; the CloudTrail S3 data event for the GET is read beside it if the trail records data events, and the record says plainly if it does not. Links are graded by FWD-9: DETERMINISTIC only on a stable key (an old/new account number, or a tax id matched inside the job against an identifier Black Diamond carries); otherwise CANDIDATE.

## What the act may NOT do

Read any other key or prefix in the firm bucket; write anything to S3 or to disk from the CRM content; keep the role or the exception past the job's last day; copy the zip, a member, a header row's values, or a sample row into a log, a message, a commit or a scratch file; contact Cottonwood (option (c) is not sent); change the crosswalk as served (the links are an output for a person to read, wired in by a later act under its own pair).

## Order of the act, and its stop

1. Both halves signed. 2. Ledger entry opened in `org/critical_paths/change_management/` (with the `.open_deploys/` sentinel) naming the removal as its rollback, BEFORE the plan. 3. Targeted `terraform plan` read: exactly the two changes. 4. `bash .tools/safe-apply.sh` scoped to those addresses; read-back by `get-role` and the bucket policy. 5. The job (one run). 6. The withdrawal the same day; a re-plan reads no changes; the entry closed with the run record. **Stop:** a plan with any other change, an apply that leaves one of the two halves landed without the other, a job that writes a column outside the allow-list, or a job still unfinished at 23:59Z of the day the role was created: the withdrawal runs regardless and the finding is the report.

-- `2.0.0_SA_COO~C1`
