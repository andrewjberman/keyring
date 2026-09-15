# Deploy Completion Record
**Date opened:** 2026-09-15T02:29:15.576812+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ri-2: the chatter-axis producer consolidates into the harvest root and is repointed at the LIVE harvest tables
**Authored by:** 0.9.0_WK_AMGT_RESAPP~17
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-amgt_resapp-10-2 branch commits (consolidation ea6cd450fa + AC12 builder 6cb6442158 + this ledger entry) | commit hash on the worker branch |  | OPEN |
| L2 | activation | terraform apply of .scratch/ri2.tfplan into harvest/tfstate (6 imported producer resources; 0 add, 4 change, 0 destroy) | Apply complete! line with 0 destroyed |  | OPEN |
| L3 | verify | live amgt-resapp-chatter-axis function code hash + amgt-resapp-chatter-axis-lambda-policy Resource ARNs | get-function-configuration CodeSha256 equals the local zip sha256 b64 AND get-role-policy shows harvest tables with 0 opal-amgt- tokens |  | OPEN |
| L4 | verify | QA invoke of amgt-resapp-chatter-axis and today's TRENDING_CHATTER partition in opal-harvest-security-metrics | StatusCode 200 with no FunctionError, rows_written greater than 0, and a non-zero COUNT for today against a zero COUNT for 2026-09-13 |  | OPEN |

## Log

- 20260915T022915Z OPENED by 0.9.0_WK_AMGT_RESAPP~17 with 4 leg(s)
