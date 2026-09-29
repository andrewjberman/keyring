# Deploy Completion Record
**Date opened:** 2026-09-29T15:15:34.377774+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T153156Z
**Deploy:** WINDOW 23: one principal for ~D's single signed-in directory search (AD-10 step 1 A1); packet blob 033aeb0362 @c7f86d5205
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming 033aeb0362; directory-search pin s0riHZ9h re-read; users census before; put + read-back | Both halves at HEAD naming blob 033aeb0362 (@c7f86d5205): CTO 102861 (@7044462936; condition: ~D records the portal commit its localhost build runs -- tree 8b18dbb79c shared by DEV 18899c96 / PROD 9a8f6c71; carried into the A leg), CRO 102862 (@5a81a03a12; conditions: pin + census equal, HAR field set with account_masks absent and 0 outside routes -- a different set is the named FAIL with AD-10 rollback keys, K1-CRED/K1 read-backs inside the cap). Pin re-read 15:17Z: irpt-directory-search s0riHZ9h (DirectoryEntry 27d9a8f7). Census before 15:17:28Z: users 51 digest 76cbe66b, SELECTION# 115 (W23_USERS_CENSUS_BEFORE). Pre-read 1790695048 ABSENT; K1 put USER#usr_irptuiwalk_1790695048 at 15:17:35Z (uiwalk), read-back digest 29c2e20d EQUAL; K1-CRED put (value not printed). Cap 15:47:35Z. | CLOSED 20260929T151811Z |
| A | verify | ~D's one signed-in directory search | field set per entry, account_masks absent, request time, scrubbed HAR (record path) | ~D 102868, record org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/a1-directory-search-20260929.md @f181812603: search 15:23:43.387Z, one firm, GET directory/browse 200, 100 entries; ONE field set (access, cohort, display_name, ids, masked_discriminator, permitted_capabilities, permitted_scope, revision, termination); account_masks absent in 0 of 800 entries across all 8 directory GETs. CTO condition: build portal 18899c96, tree 8b18dbb7 == origin PROD 9a8f6c71's tree, 0 tracked changes, dev:live on 5174. Scrubbed HAR a1-20260929.har in place, 711 entries, leak-free. | CLOSED 20260929T153155Z |
| D1 | verify | credoff after sign-in + K1 delete <=30 min | ParameterNotFound; consistent read no item | credoff after ~D's sign-in (15:18:47Z, 102865): K1-CRED ParameterNotFound at 15:20:05.666Z. Walk closed 15:25:33Z; delete 1790695048 at 15:30:49Z: K1 consistent GetItem no Item (VERIFIED), K1-CRED ParameterNotFound -- inside the 15:47:35Z cap. | CLOSED 20260929T153155Z |
| A1 | verify | route + write trace | HAR 0 outside login/refresh/directory-search/read routes; users == baseline | HAR a1-20260929.har (711 entries): writes login 1, refresh 6, directory/resolve 5, nothing else; every other request a GET of the portal read routes (the record states 7 extra page-load and firm-pick reads beyond the one search); 0 outside the classes. USERS 51 -> 51 digest 76cbe66b equal, SELECTION# 115 -> 115 (W23_USERS_CENSUS_BEFORE/AFTER). | CLOSED 20260929T153156Z |

## Log

- 20260929T151534Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260929T151811Z LEG C1 closed: Both halves at HEAD naming blob 033aeb0362 (@c7f86d5205): CTO 102861 (@7044462936; condition: ~D records the portal comm
- 20260929T153155Z LEG A closed: ~D 102868, record org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/a1-directory-search-20260929.md @f181812
- 20260929T153155Z LEG D1 closed: credoff after ~D's sign-in (15:18:47Z, 102865): K1-CRED ParameterNotFound at 15:20:05.666Z. Walk closed 15:25:33Z; delet
- 20260929T153156Z LEG A1 closed: HAR a1-20260929.har (711 entries): writes login 1, refresh 6, directory/resolve 5, nothing else; every other request a G
- 20260929T153156Z CLOSED -- all 4 legs proven
