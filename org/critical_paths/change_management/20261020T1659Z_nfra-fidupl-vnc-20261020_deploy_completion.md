# Deploy Completion Record
**Date opened:** 2026-10-20T16:59:45.396302+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T170308Z
**Deploy:** NFRA_FIDUPL FU-s-11 Part 1b: vnc-installed, Xvnc bound to localhost only on the Fidelity box (CTO ruling 8724)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | vnc-installed: tigervnc Xvnc listening on 127.0.0.1:5901 only on i-028e830f7226cc685 | SSM ss -ltn shows 127.0.0.1:5901 and no other VNC bind; RFB banner read locally on the box | SSM on i-028e830f7226cc685 (running throughout, boot 2026-10-20 13:03:50 unchanged): dnf install -y tigervnc-server-minimal dnf_rc=0, rpm tigervnc-server-minimal-1.14.1-3.amzn2023.0.6.x86_64, /usr/bin/Xvnc; systemd unit fidelity-vnc.service enabled and active, ExecStart Xvnc :1 -geometry 1440x900 -depth 24 -rfbport 5901 -localhost -SecurityTypes None -AlwaysShared; ss -ltn: LISTEN 127.0.0.1:5901 and [::1]:5901 only; RFB banner b'RFB 003.008' read from loopback; connection to the box's own NIC address refused (ConnectionRefusedError); security group fidelity-alongside-uploader-sg has 0 inbound rules. No password set, printed or stored; no ExtensionInstallForcelist policy installed; /opt/fidelity-uploader untouched. The SSM port forward itself was not run here (Session Manager plugin absent on this machine); the exact command is in FU-s-11_feasibility.md. | CLOSED 20261020T170308Z |

## Log

- 20261020T165945Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261020T170308Z LEG L1 closed: SSM on i-028e830f7226cc685 (running throughout, boot 2026-10-20 13:03:50 unchanged): dnf install -y tigervnc-server-mini
- 20261020T170308Z CLOSED -- all 1 legs proven
