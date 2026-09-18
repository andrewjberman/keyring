# Deploy Completion Record
**Date opened:** 2026-09-18T14:39:08.022282+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW.TO-OG-i-4 -- pilot host resize t4g.nano to t4g.small on aws_instance.gw (i-07dccb1615503ac99). G-A lifted by Andrew-direct org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_140xZ_FOUR_CARDS_ANSWERED_GA_YES_SPRINT_EMPLOYEES.md@80558e1508 (Call 1: Yes go ahead), scoped to this stop/start only.
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply resize of aws_instance.gw instance_type via saved planfile (0 add, 1 change, 0 destroy) | terraform apply output + before/after describe-instances |  | OPEN |
| L2 | verify | post-apply live host state: instance type/arch/running, systemd opal-gateway active, unauthenticated /mcp 401 resource challenge, existing-user latency baseline (OG-p-1 OGP1-AC11 instrument/window) re-taken | SSM host reads + HTTPS probe + CloudWatch p95 read |  | OPEN |

## Log

- 20260918T143908Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 2 leg(s)
