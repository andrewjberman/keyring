# Deploy Completion Record
**Date opened:** 2026-10-19T18:52:22.281259+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T190050Z
**Deploy:** NFRA_OPLGTW OG-mg-2 Phase B (option b): re-activate ALYSSA's Schwab grant at each granted master's current account set (only scope.accounts changes); ANDREW's grant HELD (his email_deny would be re-created); database-only, no deploy, no delete
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| andrew-write | verify | Andrew's grant is HELD under option (b): not activated, grant revision unchanged | proof: W/MG2_ANDREW_HELD.md and the live grant revision equal to the Phase A record | proof: HELD under option (b) (COO and CTO halves): W/MG2_ANDREW_HELD.md; Andrew's grant revision read unchanged (1) in the live store at 2026-10-19T18:58Z (W/MG2_AFTER.json); no record of his was written and no email_deny was created | CLOSED 20261019T190049Z |
| alyssa-write | verify | Alyssa's record activated through ops/schwab_entitlement_admin.py activate under opal-gateway-access-admin, approver Andrew Berman, only scope.accounts changed | proof: the ACTIVATED line in W/MG2_WRITE.md | proof: ACTIVATED profile_revision=6 grant_revision=6 (W/MG2_WRITE.md), through ops/schwab_entitlement_admin.py under opal-gateway-access-admin, approver Andrew Berman, at 2026-10-19T18:58Z; only scope.accounts changed (scope without accounts hashes equal to Phase A) | CLOSED 20261019T190049Z |
| read-back | verify | a strongly consistent read of the live store: Alyssa's new grant revision active, per-master counts equal the current sets, the rest of the scope hashes unchanged, and decide() on the live grant admits the four read tools and refuses schwab_prepare_download | proof: W/MG2_AFTER.json and W/MG2_READBACK_DECIDE.json and mg2.AC2 | proof: strongly consistent live read (W/MG2_AFTER.json): Alyssa profile and grant active at revision 6, per-master counts 7599 and 7690 equal the current sets, scope without accounts unchanged; decide() on her LIVE grant admits the four read tools and refuses schwab_prepare_download (W/MG2_READBACK_DECIDE.json); 1 email_deny record in the store, unchanged | CLOSED 20261019T190050Z |

## Log

- 20261019T185222Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261019T190049Z LEG andrew-write closed: proof: HELD under option (b) (COO and CTO halves): W/MG2_ANDREW_HELD.md; Andrew's grant revision read unchanged (1) in t
- 20261019T190049Z LEG alyssa-write closed: proof: ACTIVATED profile_revision=6 grant_revision=6 (W/MG2_WRITE.md), through ops/schwab_entitlement_admin.py under opa
- 20261019T190050Z LEG read-back closed: proof: strongly consistent live read (W/MG2_AFTER.json): Alyssa profile and grant active at revision 6, per-master count
- 20261019T190050Z CLOSED -- all 3 legs proven
