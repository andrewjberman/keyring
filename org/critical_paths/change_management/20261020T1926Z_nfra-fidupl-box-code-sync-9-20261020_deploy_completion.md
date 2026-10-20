# Deploy Completion Record
**Date opened:** 2026-10-20T19:26:04.004572+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T192704Z
**Deploy:** NFRA_FIDUPL FU-s-10 ninth delivery: signin.py changed at 132dc9c3061 (REPAIR 11; file copy only)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | every shipped file at /opt/fidelity-uploader equals the repo (ninth delivery) | SSM md5sum of the RUNNING files; fu10m R1-FU10M-OK all N shipped files; fu10x R1-FU10X-OK | Ninth delivery of the full shipped set (15 files) from HEAD 0facf7d9d24 (contains 132dc9c3061; canonical-fidelity unchanged to 1801509afd2) over SSM, sha256 HASH-MATCH. Changed against the eighth delivery: signin.py 06be9b1a5b756f73ba186b275076399f only; the other 14 files are unchanged (adapters f84edd5e, agent_drive 60ed0988, attribute 98cde679, backfill fec1bfa2, agent_fill a6fba948, bootstrap 27e66450, daily c8990cfc, run 6f48b4d6, fetch c9c1164b, gswitch fc7ea8e2, land 95a9295c, quo_otp fe03ef28, signin_recon 29e96c69, split e2b250cf). fidupl_round_checks.py fu10m: R1-FU10M-OK all 15 shipped files match the repo on the box. fu10x: R1-FU10X-OK Xvfb present and a headed Google Chrome launches under it (scratch launch, issuer-authorized). File copy only: no bootstrap, no sign-in, nothing under profile or profile-agent, fidelity-agent-chrome.service not started, instance left running. | CLOSED 20261020T192704Z |

## Log

- 20261020T192604Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 1 leg(s)
- 20261020T192704Z LEG L1 closed: Ninth delivery of the full shipped set (15 files) from HEAD 0facf7d9d24 (contains 132dc9c3061; canonical-fidelity unchan
- 20261020T192704Z CLOSED -- all 1 legs proven
