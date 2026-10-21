# Deploy Completion Record
**Date opened:** 2026-10-21T07:10:30.064630+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T075536Z
**Deploy:** NFRA_OPLGTW OG-rl-19 R3c (round-47 dual-read release): two in-place role-policy updates (schwab_data_read_policy, schwab_catalog_read_policy) by safe-apply (0 add, 2 change, 0 destroy), the gate read as the catalog role (NoSuchKey/empty), then release 2923d1ee99 on live ref 8e3eddf959; slot 07:00Z-11:30Z; one gateway restart of about 16 s
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| terraform | activation | two in-place IAM role-policy updates applied by safe-apply of a saved plan, 0 add 2 change 0 destroy | proof: W/R3C_SERVED.json | org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json | CLOSED 20261021T075535Z |
| gate-read | verify | catalog-role gate read before the code deploy answers NoSuchKey and an empty list | proof: W/R3C_SERVED.json | org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json | CLOSED 20261021T075535Z |
| release | ec2-baked-asset | release 2923d1ee99 deployed through safe-ec2-deploy.sh, marker equal | proof: W/R3C_SERVED.json | org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json | CLOSED 20261021T075536Z |
| read-back | verify | 15-minute unarmed read-back, dual read old and new locations, probe 13 lines | proof: W/R3C_SERVED.json | org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json | CLOSED 20261021T075536Z |

## Log

- 20261021T071030Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 4 leg(s)
- 20261021T075535Z LEG terraform closed: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json
- 20261021T075535Z LEG gate-read closed: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json
- 20261021T075536Z LEG release closed: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json
- 20261021T075536Z LEG read-back closed: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/R3C_SERVED.json
- 20261021T075536Z CLOSED -- all 4 legs proven
