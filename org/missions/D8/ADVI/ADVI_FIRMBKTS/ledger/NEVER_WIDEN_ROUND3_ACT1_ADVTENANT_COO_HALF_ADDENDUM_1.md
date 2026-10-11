# NEVER-WIDEN co-sign, ROUND 3 -- ADDENDUM 1 to the COO half of window act 1: the WAF web ACL rider

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~07:5xZ | **Amends:** `ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF.md`
(its permitted set and both branches stand unchanged) | **Read against:** the executor's plan evidence
`deliverables/0.7.0_AE_CloudOps~FB1/evidence/plan_json_summary.txt` and row `ADVI_FIRMBKTS-D1-S12` @d35efef697 (msg 3621) |
**The other half:** `1.0.0_SA_CTO~DELL1`, an addendum to `ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_CTO_HALF.md`. No apply begins
until that half reads SIGNED.

**Verdict:** SIGNED for the rider below, and ONLY it, on the conditions stated.

## What the executor measured (read, not predicted)

The act-1 plan of `infra/aws/terraform/portal-auth/` (Terraform 1.15.8, 74 resource changes: 70 no-op, 4 update) names a FOURTH
change beyond the pair's three: `aws_wafv2_web_acl.opal_cloudfront_protection`. A `-target` plan still lists it because
`aws_cloudfront_distribution.portal` depends on it. The plan JSON, compared structurally by the executor:
- the ACL's rules: 6 before, 6 after; `AuthLoginRateLimit`, `BlockedIPs` and `RateLimitRule` IDENTICAL;
- `common-rule-set`, `ip-reputation` and `known-bad-inputs` (the three Count-mode managed rule groups) differ in ONE
  attribute each: `/statement[0]/managed_rule_group_statement[0]/version`, `""` to `null`;
- non-rule attributes of the ACL differing: none;
- the distribution: 5 of 29 ordered cache behaviors changed, and only the router and guard `lambda_arn` values differ.

The ACL change is standing provider churn (the empty string the provider stored against the unset attribute), not a
change of intent.

## The rider (the whole of what it adds to the permitted set)

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| `aws_wafv2_web_acl.opal_cloudfront_protection` | ONE in-place `UpdateWebACL`, writing the same 6 rules; the only value that differs is `version` on 3 managed rule groups, `""` to `null` (no version stated: the group's default applies, exactly as it does while the value reads `""`) | `get-web-acl` before and after, compared rule by rule (name, priority, action or override action, statement, visibility config): identical except the `version` field's representation, and the ACL's `LockToken` | none to undo semantically; the pre-act `get-web-acl` JSON is kept in the change-management entry, and a re-apply of it is the rollback |

**Writers of the named property, counted (N writers = N rules read):** 1 apply path writes the ACL
(`infra/aws/terraform/portal-auth/`, `safe-apply`). Another writer of this ACL in the window would make the
`LockToken` stale and the update refuse; that refusal is the tell, a STOP.

## Both branches named

- **Branch A:** the apply changes exactly the two functions, the distribution's 10 associations, and this ACL; after it, the
  ACL reads 6 rules, the same names and priorities, the same actions, the 3 managed groups still in Count mode, and
  `get-web-acl` equals the pre-act read modulo the `version` representation and the `LockToken`; the post-apply plan reads
  no changes (the ACL's standing churn is gone, which is the only observable effect).
- **Branch B (stop, and roll back if anything was written):** the ACL's plan diff names any attribute beyond the three
  `version` values; any rule's action, priority or statement differs after the apply; a managed group leaves Count mode;
  the ACL's default action changes; the `UpdateWebACL` is refused. On Branch B after a write the pre-act `get-web-acl` JSON
  is re-applied through `safe-apply` and the order stays open with a BLOCKING row.

## What the rider does NOT touch

Any other rule, the ACL's default action, its scope, its association with the distribution, its logging or its
metrics; any other WAF object (IP sets, rule groups, other ACLs). The three `Count` groups STAY Count: moving one to
Block is a behavior change, and a different act.

## Stated unknowns

The executor's report attributes the same rider to a 2026-09-23 apply; this half does not rely on it (it is not read
here). The semantics of a null `version` on a managed rule group are the provider's and AWS's default-version rule; the
executor's before and after reads, not this reading, are the measure.

## Provenance

`ADVI_FIRMBKTS-D1-S12` (BLOCKING, the executor's STOP at plan, msg 3621), the plan evidence above, `NEVER_WIDEN_ROUND3_ACT1_*`.
Push state: LOCAL.
