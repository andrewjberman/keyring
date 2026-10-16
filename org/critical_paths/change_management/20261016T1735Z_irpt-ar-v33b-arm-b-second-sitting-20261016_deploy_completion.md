# Deploy Completion Record
**Date opened:** 2026-10-16T17:35:37.670376+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T173919Z
**Deploy:** IRPT_ANLREQ TO-RUN-AR-v33 AMENDMENT 2 (4d95db7e0d), sitting 2 SECOND PASS, ARM B ONLY: ONE transient staff-only users row fwd1-staff-r41b@opal.invalid (helper blob f368e9d9, minted and removed read back ABSENT), the DEV dev server on localhost:5174 (started here, stopped here), a page read of the packaged ticket TCK-20261014-2965a5e0 with the Open tab clicked and the ticket confirmed listed first; NO ticket write, no fixture
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | verify | preconditions: blobs, XA RULED, users row ABSENT, port 5174 free | the printed reads | AMENDMENT 2 (4d95db7e0d) present; COO half 19bc898d, CTO half 8d94f034, helper f368e9d9, checker 1a96ed42 equal; XA-f98b RULED; users row ABSENT (consistent); port 5174 free; ticket B open with a package | CLOSED 20261016T173918Z |
| B2 | s3-prefix | mint (U1 staff-only), sign in, sidebar link, Open tab clicked, ticket listed, page read, status reads counted, screenshot | lines S3 P3 and the NOTE U1 | second mint MINT-OK READBACK-OK, U1 role=user userType=test-filer firmId=opal-capital entitlement_rows=0 status=active; real login form; sidebar link; Open tab clicked; TCK-20261014-2965a5e0 listed before the read; words_shown NO, package block YES, page intact, 0 status reads; screenshot ar_v33_b_page.png | CLOSED 20261016T173918Z |
| B3 | verify | the user removed ABSENT consistent and GSI, the dev server stopped | the NOTE R1 | helper remove: ABSENT GSI and ABSENT CONSISTENT; dev server started at 17:36:18Z stopped (bun, vite, node; port 5174 free) | CLOSED 20261016T173919Z |

## Log

- 20261016T173537Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
- 20261016T173918Z LEG B1 closed: AMENDMENT 2 (4d95db7e0d) present; COO half 19bc898d, CTO half 8d94f034, helper f368e9d9, checker 1a96ed42 equal; XA-f98b
- 20261016T173918Z LEG B2 closed: second mint MINT-OK READBACK-OK, U1 role=user userType=test-filer firmId=opal-capital entitlement_rows=0 status=active; 
- 20261016T173919Z LEG B3 closed: helper remove: ABSENT GSI and ABSENT CONSISTENT; dev server started at 17:36:18Z stopped (bun, vite, node; port 5174 fre
- 20261016T173919Z CLOSED -- all 3 legs proven
