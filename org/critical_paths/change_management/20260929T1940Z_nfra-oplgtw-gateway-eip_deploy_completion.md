# Deploy Completion Record
**Date opened:** 2026-09-29T19:40:49.959811+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T200846Z
**Deploy:** OG-n-1: gateway aws_eip + association (egress address 54.197.78.28 moves once to an EIP)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~14
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply -target aws_eip.gw + aws_eip_association.gw | apply output line | safe-apply apply -auto-approve -target aws_eip.gw -target aws_eip_association.gw rc=0; Plan 2 to add 0 change 0 destroy; eip 3.214.118.242 eipalloc-093d97376b28d2388 eipassoc-03d10cd025b196726 | CLOSED 20260929T200846Z |
| L2 | verify | describe-addresses associated with i-07dccb1615503ac99; PublicIpAddress equal; /mcp 401 | command output | describe-addresses: 3.214.118.242 eipassoc-03d10cd025b196726 on i-07dccb1615503ac99; PublicIpAddress=3.214.118.242; https://mcp.opalinvest.dev/mcp unauth HTTP 401 www-authenticate Bearer resource_metadata; old 54.197.78.28 | CLOSED 20260929T200846Z |

## Log

- 20260929T194049Z OPENED by 0.9.0_WK_NFRA_OPLGTW~14 with 2 leg(s)
- 20260929T200846Z LEG L1 closed: safe-apply apply -auto-approve -target aws_eip.gw -target aws_eip_association.gw rc=0; Plan 2 to add 0 change 0 destroy;
- 20260929T200846Z LEG L2 closed: describe-addresses: 3.214.118.242 eipassoc-03d10cd025b196726 on i-07dccb1615503ac99; PublicIpAddress=3.214.118.242; http
- 20260929T200846Z CLOSED -- all 2 legs proven
