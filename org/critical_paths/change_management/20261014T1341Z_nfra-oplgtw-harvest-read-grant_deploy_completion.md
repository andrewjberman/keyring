# Deploy Completion Record
**Date opened:** 2026-10-14T13:41:35.084378+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-hv-2 ACT 1: the harvest read grant on gateway-global-internal-reader-role (3 halves signed, C1-C3)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the targeted plan immediately before the apply reads 1 to add, 0 to change, 0 to destroy (C3) | the Plan: line from the saved plan file the apply consumes |  | OPEN |
| L2 | activation | safe-apply lands ONLY aws_iam_role_policy.int_reader_harvest_read; the role carries gateway-global-harvest-read-policy | the apply output plus get-role-policy read-back of the one name, and the pre-existing internal-reader policy unchanged |  | OPEN |
| L3 | verify | the internal reader role reads the served prefixes and nothing else | three isolated simulate-principal-policy calls (packs allowed, wsj/harvest allowed, zzz-not-served implicitDeny) written to W/HV2_IAM_SIM.json |  | OPEN |

## Log

- 20261014T134135Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
