# Deploy Completion Record
**Date opened:** 2026-09-29T19:40:49.959811+00:00
**Status:** OPEN
**Deploy:** OG-n-1: gateway aws_eip + association (egress address 54.197.78.28 moves once to an EIP)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~14
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply -target aws_eip.gw + aws_eip_association.gw | apply output line |  | OPEN |
| L2 | verify | describe-addresses associated with i-07dccb1615503ac99; PublicIpAddress equal; /mcp 401 | command output |  | OPEN |

## Log

- 20260929T194049Z OPENED by 0.9.0_WK_NFRA_OPLGTW~14 with 2 leg(s)
