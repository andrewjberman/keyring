# Deploy Completion Record
**Date opened:** 2026-07-16T18:23:47.411093+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260716T184601Z
**Deploy:** Grant bd-exporter-ec2-role read on opal-data-assets/schwab/08242234/silver (in-monolith home) -- unblocks ~A's L4 trn_nna source-flip; CTO-routed 181602Z, CTO apply gate
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit new aws_iam_role_policy.bd_exporter_monolith_schwab_read | hash pushed | commit 87f5940a7 (new aws_iam_role_policy.bd_exporter_monolith_schwab_read) | CLOSED 20260716T184601Z |
| L2 | activation | bd-pipeline targeted apply (plan shown at CTO gate -> GO -> safe-apply -> 0-diff) | plan 1/0/0 pure-add + apply + 0-diff | safe-apply 1/0/0 (Creation complete) -> targeted re-plan 'No changes' | CLOSED 20260716T184601Z |
| L3 | verify | 22a: simulate-principal-policy ONE resource/call (GetObject exact key + separate positive control) + post-apply live get-role-policy (desired+applied) | simulate allowed + live policy present | 22a full layering: simulate GetObject exact key arn:...opal-data-assets/schwab/08242234/silver/* = allowed (ONE resource); ListBucket +context s3:prefix=schwab/08242234/silver/ = allowed; POSITIVE CONTROL GetObject opal-data-bd/* separate invocation = allowed (simulator discriminates); APPLIED live get-role-policy shows both Sids MonolithSchwabSilverGet + MonolithSchwabSilverList present. Exercised end-to-end read = ~A's leg on CTO word. | CLOSED 20260716T184601Z |

## Log

- 20260716T182347Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260716T184601Z LEG L1 closed: commit 87f5940a7 (new aws_iam_role_policy.bd_exporter_monolith_schwab_read)
- 20260716T184601Z LEG L2 closed: safe-apply 1/0/0 (Creation complete) -> targeted re-plan 'No changes'
- 20260716T184601Z LEG L3 closed: 22a full layering: simulate GetObject exact key arn:...opal-data-assets/schwab/08242234/silver/* = allowed (ONE resource
- 20260716T184601Z CLOSED -- all 3 legs proven
