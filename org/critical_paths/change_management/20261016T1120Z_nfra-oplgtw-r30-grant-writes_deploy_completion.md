# Deploy Completion Record
**Date opened:** 2026-10-16T11:20:19.698386+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-mg-1 Phase B: the two r30 grant writes -- R1 Andrew's principal and R2 the Bloomberg mirror, each one activate under opal-gateway-access-admin; all three halves signed at ask sha256 757f5146afee (COO 020264306c, CTO c92d6c7c07, CVO 5c4025b899), GO msg 34954
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| r1-write | activation | R1: Andrew's principal, one activate of X/r1_candidate.json (profile restricted + grant revision 1, 13 calendar months) through schwab_entitlement_admin under opal-gateway-access-admin, base revisions None | proof: ACTIVATED line recorded in W/MG1_WRITE.md, then the profile and grant read back from the store at revision 1 restricted |  | OPEN |
| r2-write | activation | R2: the Bloomberg principal, one activate of X/r2_candidate.json, the exact mirror of R1, same role, base revisions None | proof: ACTIVATED line recorded in W/MG1_WRITE.md, then the profile and grant read back at revision 1 restricted, scope equal to R1 with zero differing keys |  | OPEN |
| read-back | verify | both records read back live from the store, R2 scope equals R1, Alyssa's profile and grants unchanged, no address in any file | proof: mg1.AC2 PASS and Alyssa's canonical item hash equal before and after |  | OPEN |

## Log

- 20261016T112019Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
