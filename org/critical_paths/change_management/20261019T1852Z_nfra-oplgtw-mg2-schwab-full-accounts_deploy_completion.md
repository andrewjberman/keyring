# Deploy Completion Record
**Date opened:** 2026-10-19T18:52:22.281259+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-mg-2 Phase B (option b): re-activate ALYSSA's Schwab grant at each granted master's current account set (only scope.accounts changes); ANDREW's grant HELD (his email_deny would be re-created); database-only, no deploy, no delete
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| andrew-write | verify | Andrew's grant is HELD under option (b): not activated, grant revision unchanged | proof: W/MG2_ANDREW_HELD.md and the live grant revision equal to the Phase A record |  | OPEN |
| alyssa-write | verify | Alyssa's record activated through ops/schwab_entitlement_admin.py activate under opal-gateway-access-admin, approver Andrew Berman, only scope.accounts changed | proof: the ACTIVATED line in W/MG2_WRITE.md |  | OPEN |
| read-back | verify | a strongly consistent read of the live store: Alyssa's new grant revision active, per-master counts equal the current sets, the rest of the scope hashes unchanged, and decide() on the live grant admits the four read tools and refuses schwab_prepare_download | proof: W/MG2_AFTER.json and W/MG2_READBACK_DECIDE.json and mg2.AC2 |  | OPEN |

## Log

- 20261019T185222Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
