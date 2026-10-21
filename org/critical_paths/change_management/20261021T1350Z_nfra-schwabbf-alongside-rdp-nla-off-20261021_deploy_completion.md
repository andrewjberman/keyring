# Deploy Completion Record
**Date opened:** 2026-10-21T13:50:32.570642+00:00
**Status:** OPEN
**Deploy:** RETROSPECTIVE entry (act already done, recorded by 0.7.0_AE_CloudOps~NFRA1 under TO-AL-r5 for 2.0.0_SA_COO~SA): RDP Network Level Authentication turned OFF on the Alongside Schwab Box. ACT: SSM command 144a3975-2edc-44ca-82ca-2972536ccc6e (AWS-RunPowerShellScript, executed 2026-10-21T13:45:06Z) run by 1.0.0_SA_CTO with Andrew present. TARGET: instance i-0825aa0ed88342d67, registry value HKLM:/SYSTEM/CurrentControlSet/Control/Terminal Server/WinStations/RDP-Tcp UserAuthentication, BEFORE 1, AFTER 0 (the command's own output; the issuer read back 0 at ~13:5xZ). REASON: mstsc through localhost:13389 (the SSM port forward) refused on NLA at Andrew's sitting. CONTAINMENT: the security group has ZERO ingress rules (read again 13:50Z), RDP is reachable only through the IAM-gated SSM forward, and the Windows Administrator password is still required. PLANNED REVERSAL: set UserAuthentication back to 1 after the sitting, on the issuer's GO (TO-AL-r5 step B); the change affects new connections only. The runbook gains the known fix (TO-AL-r5 step A).
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | restore NLA=1: set UserAuthentication to 1 on RDP-Tcp of i-0825aa0ed88342d67 over SSM after the sitting (TO-AL-r5 step B, on the issuer's GO) | get-registry read-back 1, quser still lists the administrator session, security group ingress count 0 |  | OPEN |

## Log

- 20261021T135032Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
