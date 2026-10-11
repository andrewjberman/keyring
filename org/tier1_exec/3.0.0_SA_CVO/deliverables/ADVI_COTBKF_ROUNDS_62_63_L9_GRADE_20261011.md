# ADVI_COTBKF rounds 62 and 63 -- L9 grade of CB62bj1-AC3 (FWD-7's break-glass role)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:31:33Z. Row ADVI_COTBKF-D2-S106.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_62_63_DRAIN_END_20261011.md @53af818717 (msg 4568)`. This seat read live IAM, CloudTrail and the saved plans itself.

| limb of CB62bj1-AC3 | verdict | this seat's evidence |
|---|---|---|
| the saved plan that was applied named only the two addresses | **MET** | The saved targeted plan holds 2 resource changes, both creates: the role and its inline policy. The plan taken after the apply shows neither changing |
| the inline policy read back carries the four actions on the restricted prefix and no delete | **MET** | Read live: GetObject, GetObjectVersion and PutObject on the cottonwood CRM prefix, and ListBucket conditioned to that prefix. No delete action, 1 inline policy, 0 attached policies, no boundary |
| no principal other than the console user can assume the role | **MET** | Read live: the trust policy holds 1 statement naming the console user alone |
| no agent assumed it | **MET** | CloudTrail, by the role's name since 09:00Z, read at 09:29Z: CreateRole and PutRolePolicy by the dell2 agent user, and no AssumeRole. RoleLastUsed is empty |

**Verdict: CB62bj1-AC3 MET.**

## Notes that do not change the grade

- **The trust statement carries no condition.** Anyone holding the console user's session can assume the role; there is no
  multi-factor condition on the role itself. That is what the pair signed. It is stated here so nobody assumes otherwise.
- **The third Deny statement on the firm bucket now has its one writer.** Until 09:05Z it admitted nobody (this seat's round 61
  note). Whether the console user can in fact assume the role and write is untested, by the pair: no agent may test it.
- **Who applied the bucket policy's statements before the role existed is unfound** (the CTO half's condition 6). No row is filed.
- CloudTrail lookups can lag by minutes; this read was taken 24 minutes after the create.
- The issuer's own defect stands on record: CB62bj1-AC1 names a path under `r62/` and the file is under `r63/`.
