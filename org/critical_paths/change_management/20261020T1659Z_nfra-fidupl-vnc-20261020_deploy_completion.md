# Deploy Completion Record
**Date opened:** 2026-10-20T16:59:45.396302+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FU-s-11 Part 1b: vnc-installed, Xvnc bound to localhost only on the Fidelity box (CTO ruling 8724)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | vnc-installed: tigervnc Xvnc listening on 127.0.0.1:5901 only on i-028e830f7226cc685 | SSM ss -ltn shows 127.0.0.1:5901 and no other VNC bind; RFB banner read locally on the box |  | OPEN |

## Log

- 20261020T165945Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
