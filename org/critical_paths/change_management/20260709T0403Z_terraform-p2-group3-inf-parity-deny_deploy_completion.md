# Deploy Completion Record
**Date opened:** 2026-07-09T04:03:41.561597+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T040924Z
**Deploy:** NFRA_TERRAFORM-P2 BATCH C group 3: inf-parity cross-firm Deny belt (27 roles, additive) -- dual GO: CTO 035928Z + COO 040050Z
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit + push cross-firm-deny.tf | hash pushed | 7d7cb42c4 pushed to CLOUD (6dc083d3b..7d7cb42c4) | CLOSED 20260709T040356Z |
| L2 | activation | safe-apply(HALTGT) inf-pipeline -- 27 aws_iam_role_policy adds | apply complete 27-add/0-change/0-destroy | safe-apply(HALTGT) passed checkpoint; Apply complete! Resources: 27 added, 0 changed, 0 destroyed (from saved gated plan, commit 7d7cb42c4) | CLOSED 20260709T040515Z |
| L3 | verify | live get-role-policy: Deny LANDED on ALL 27 inf roles (applied truth) | 27/27 cross-firm-bucket-deny present with Sid=DenyCrossFirmBuckets | live get-role-policy swept all 27 inf roles (bug-fixed loop, in-loop count asserted): 27/27 carry inline policy cross-firm-bucket-deny with Sid=DenyCrossFirmBuckets + Effect=Deny + exactly 2 bd ARNs + 2 cot ARNs + ZERO opal-data-inf. missing=none, wrong-scope=none. | CLOSED 20260709T040923Z |
| L4 | verify | DENY-TEST exercised: simulate-principal-policy -- an inf role is ACTUALLY denied s3 on bd/cot | explicitDeny verdict from simulate (behavior, not config-read) | DENY-TEST EXERCISED via aws iam simulate-principal-policy (behavior, not config-read). s3:GetObject+s3:PutObject vs opal-data-bd/probe.txt AND opal-data-cot/probe.txt: explicitDeny on BOTH actions x BOTH buckets for inf-gold-layer-ec2-role, inf-exporter-ec2-role, inf-bronze-runner-ec2-role, inf-eventbridge-ssm-role. explicitDeny (not implicitDeny) proves the BELT is the deciding control -- incl. on inf-eventbridge-ssm-role which has no S3 Allow (implicitDeny -> explicitDeny = the Allow-drift defense working). | CLOSED 20260709T040923Z |
| L5 | verify | INF-OWN-ACCESS-INTACT: simulate inf role vs opal-data-inf | allowed verdict (proves no over-restriction) | INF-OWN-ACCESS-INTACT, exercised. (i) inf-gold-layer-ec2-role s3:GetObject+PutObject on opal-data-inf/gold/probe.json = allowed,allowed; ListBucket opal-data-inf = allowed. (ii) inf-gold-qa-runner-ec2-role on a GENUINELY-allowed ARN: GetObject gold/canonical/* = allowed, PutObject qa/* = allowed (an initial implicitDeny on gold/probe.json was my probe ARN falling outside that role's pre-existing prefix-scoped Allow -- implicit, not explicit, so not belt-caused; ran it down + re-tested). (iii) OVER-RESTRICTION SENTINEL across ALL 27 roles: s3:ListBucket vs arn:aws:s3:::opal-data-inf returned explicitDeny for 0/27 -- the belt over-restricted NO inf role on its own bucket. | CLOSED 20260709T040923Z |

## Log

- 20260709T040341Z OPENED by 0.5.0_AE_OpalETL with 5 leg(s)
- 20260709T040356Z LEG L1 closed: 7d7cb42c4 pushed to CLOUD (6dc083d3b..7d7cb42c4)
- 20260709T040515Z LEG L2 closed: safe-apply(HALTGT) passed checkpoint; Apply complete! Resources: 27 added, 0 changed, 0 destroyed (from saved gated plan
- 20260709T040923Z LEG L3 closed: live get-role-policy swept all 27 inf roles (bug-fixed loop, in-loop count asserted): 27/27 carry inline policy cross-fi
- 20260709T040923Z LEG L4 closed: DENY-TEST EXERCISED via aws iam simulate-principal-policy (behavior, not config-read). s3:GetObject+s3:PutObject vs opal
- 20260709T040923Z LEG L5 closed: INF-OWN-ACCESS-INTACT, exercised. (i) inf-gold-layer-ec2-role s3:GetObject+PutObject on opal-data-inf/gold/probe.json = 
- 20260709T040924Z CLOSED -- all 5 legs proven

---

## ADDENDUM (post-close, per CTO light-condition 040449Z) -- the CORRECTED pre-apply grounding

Appended after CLOSE, not backdated: CTO required the corrected sweep evidence live in the ledger record
rather than only in the correction message, so the strengthened (a) is on the permanent record.

**Gate (a), APPLIED baseline -- the CORRECTED sweep (the one the apply actually rests on):**
- `ROLES PROCESSED: 27 / 27` -- **asserted in-loop against the expected count**, not assumed.
- `INLINE POLICIES SEEN: 82` (the first sweep saw only 79 -- it skipped roles).
- **`opal-data-bd` / `opal-data-cot` references across all 82 inline policies: ZERO.**
- Managed attachments: AWSLambdaBasicExecutionRole (21), AmazonSSMManagedInstanceCore (4), none (2);
  neither AWS-managed policy grants `opal-data-*` S3.
- 23 of 27 roles reference their own bucket (`opal-data-inf`). The 4 that do not: inf-assets-trigger,
  inf-ec2-launch-monitor, inf-ec2-retry-launch, inf-eventbridge-ssm.
=> CONCLUSION (load-bearing): no inf role held any legitimate bd/cot access, so the Deny could not
   over-restrict a real access path. Now grounded on the COMPLETE role/policy set.

**The bug that made the FIRST sweep wrong (named, so it is not repeated):**
`while read -r role; do aws ...; done < roles.txt` -- the `aws` CLI **consumes the loop's stdin**, silently
skipping iterations. It produced a confident, wrong census (79 policies / 22 own-bucket roles) and
manufactured a PHANTOM finding against `inf-unified-account-dim-daily-role` (a role that is entirely healthy).
Guard: iterate from an array (no stdin redirect), redirect `</dev/null` on every `aws` call inside the loop,
and **assert processed-count == expected-count INSIDE the loop**. A sweep that can silently skip iterations
must prove its own completeness.

**Mis-run check, named (CTO condition):** one verification `awk` one-liner used an off-by-one field index
(`$3`/`$5` against fields that were `$2`/`$4`) and therefore printed EVERY line under a "must be ZERO" header
-- it would have read as a clean pass to a skimming reader. The **authoritative** check was the
`grep -vE 'bd=0 cot=0'` filter, which returned nothing (= zero foreign-bucket refs), corroborated by direct
inspection of all 82 emitted lines. The numbers in this addendum come from the checks that actually work.
An earlier ARN-count loop likewise printed 0s from broken shell escaping and was re-run with fixed-string
`grep -F` rather than allowed to stand as a pass.

**What this addendum does NOT change:** gate (b) (27 add / 0 change / 0 destroy) and gate (c) (Deny Resource
== {bd, bd/*, cot, cot/*}, ZERO opal-data-inf) are both PLAN-derived, and (c) was independently re-grounded by
CTO reading `cross-firm-deny.tf`'s locals directly. The check that could actually have broken the inf pipeline
never depended on the buggy sweep. Both GOs were re-affirmed explicitly post-correction (CTO 040449Z,
COO 040419Z) -- neither sent `[STOP]`.
