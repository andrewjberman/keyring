# Deploy Completion Record
**Date opened:** 2026-09-20T12:07:22.872033+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260920T120844Z
**Deploy:** IRPT_BCKEND IB-rtf-3 THIRD HAND (GO 98485): the bounded test principal on packet blob a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4 -- K1 opal-users-v2 PROFILE + K1b opal-partner-49financial created, exercised by real signed requests on the NOW-SERVING directory route, K1b then K1 deleted and verified. RECORDED RETROACTIVELY: this entry was opened AFTER the run (11:43:00-11:58:24Z), not before it -- a departure from open-before-act, disclosed rather than papered over. Nothing is half-landed: the lifecycle is verified four ways and residue reads 0 of 79 / 0 of 79 / 0 of 11.
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-users-v2 K1 PROFILE item create | consistent GetItem read-back + digest (passwordHash excluded) | K1 created 2026-09-20T11:43:03Z: PK USER#usr_irptrte_1789904581; read back (consistent GetItem): True; attributes 10; digest (passwordHash excluded) a0e075754d1645629a36d2c97ca6c8f66626486623b82999f44325a917178834 | CLOSED 20260920T120842Z |
| L2 | activation | opal-partner-49financial K1b item create | consistent GetItem read-back + digest | K1b created 2026-09-20T11:43:03Z: read back (consistent GetItem): True; attributes ['advisorKey', 'email']; digest 38128b5af38684f1b279e9f2f0d47380085a8cbb2b7102b06947c824338e0977 | CLOSED 20260920T120842Z |
| L3 | verify | K1b DELETED FIRST | consistent base-table GetItem returns no Item | K1b DeleteItem -> consistent GetItem returns no Item: True at 2026-09-20T11:43:28Z | CLOSED 20260920T120843Z |
| L4 | verify | K1 DELETED | consistent base-table GetItem returns no Item | K1  DeleteItem -> consistent GetItem returns no Item: True at 2026-09-20T11:43:29Z | CLOSED 20260920T120843Z |
| L5 | verify | refresh with the issued refresh token after K1 delete | refused 1 of 1 | REFRESH with the issued refresh token after K1's delete: HTTP 404; access token minted=False -> REFUSED (1 of 1) | CLOSED 20260920T120843Z |
| L6 | verify | the access token after its exp | refused 401 1 of 1 + residue scan | the access token after exp: GET status -> HTTP 401 -> REFUSED 401 (1 of 1) \| INTERVAL: [2026-09-20T11:43:03Z, 2026-09-20T11:58:12Z] (K1 create, max of the deletes verified, the last access-token exp, the refresh refused) \| residue 0 of 79 / 0 of 79 / 0 of 11 | CLOSED 20260920T120844Z |

## Log

- 20260920T120722Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
- 20260920T120842Z LEG L1 closed: K1 created 2026-09-20T11:43:03Z: PK USER#usr_irptrte_1789904581; read back (consistent GetItem): True; attributes 10; di
- 20260920T120842Z LEG L2 closed: K1b created 2026-09-20T11:43:03Z: read back (consistent GetItem): True; attributes ['advisorKey', 'email']; digest 38128
- 20260920T120843Z LEG L3 closed: K1b DeleteItem -> consistent GetItem returns no Item: True at 2026-09-20T11:43:28Z
- 20260920T120843Z LEG L4 closed: K1  DeleteItem -> consistent GetItem returns no Item: True at 2026-09-20T11:43:29Z
- 20260920T120843Z LEG L5 closed: REFRESH with the issued refresh token after K1's delete: HTTP 404; access token minted=False -> REFUSED (1 of 1)
- 20260920T120844Z LEG L6 closed: the access token after exp: GET status -> HTTP 401 -> REFUSED 401 (1 of 1) | INTERVAL: [2026-09-20T11:43:03Z, 2026-09-20
- 20260920T120844Z CLOSED -- all 6 legs proven
