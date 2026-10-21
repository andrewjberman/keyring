# Deploy Completion Record
**Date opened:** 2026-10-21T05:41:02.638236+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FU-s-10 twenty-fifth delivery: box/g_export_probe.py with the day argument (not run) from HEAD 9edcb3c2d8a (contains 0a429399ac8); file copy only
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | every shipped file at /opt/fidelity-uploader equals the repo (twenty-fifth delivery) | SSM md5sum of the RUNNING files; fu10m R1-FU10M-OK all N shipped files |  | OPEN |

## Log

- 20261021T054102Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
