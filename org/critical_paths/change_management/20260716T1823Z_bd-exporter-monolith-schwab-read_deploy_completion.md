# Deploy Completion Record
**Date opened:** 2026-07-16T18:23:47.411093+00:00
**Status:** OPEN
**Deploy:** Grant bd-exporter-ec2-role read on opal-data-assets/schwab/08242234/silver (in-monolith home) -- unblocks ~A's L4 trn_nna source-flip; CTO-routed 181602Z, CTO apply gate
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit new aws_iam_role_policy.bd_exporter_monolith_schwab_read | hash pushed |  | OPEN |
| L2 | activation | bd-pipeline targeted apply (plan shown at CTO gate -> GO -> safe-apply -> 0-diff) | plan 1/0/0 pure-add + apply + 0-diff |  | OPEN |
| L3 | verify | 22a: simulate-principal-policy ONE resource/call (GetObject exact key + separate positive control) + post-apply live get-role-policy (desired+applied) | simulate allowed + live policy present |  | OPEN |

## Log

- 20260716T182347Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
