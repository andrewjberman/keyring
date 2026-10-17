# Deploy Completion Record
**Date opened:** 2026-10-17T08:33:32.774570+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS TO-SC-e111b: ship TWO files s3://opal-data-bd/code/gold/E_18.detect_new_securities.py (ETag a7820a20 VersionId wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB -> md5 f5c03ee6) and gold_dispatch.sh (ETag 882a910b VersionId .bNYVetB5sGV8bZki7EgXBfChCH_uPyE -> md5 165933f6), then leg Q E_18 single on the runner. Sentinel org/critical_paths/.open_deploys/secclass-e111b-e18-repoint-ship-dell1-20261017.json; entry org/critical_paths/change_management/ (name printed at open). Rollback: both files by the base VersionIds then safe-deploy of base bytes.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 13.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | Step 0 reads: served ETags, md5 of repo files, runner stopped, no trigger-pending, open ledgers across worktrees | read outputs in the log | 08:30-08:50Z: served E_18 ETag a7820a20 VersionId wb5QYkh7 (base) and gold_dispatch.sh ETag 882a910b VersionId .bNYVetB5 (base); repo md5 f5c03ee6 and 165933f6 equal the built values, HEAD contains d812b466fd; runner i-01003b035d2988dfb stopped (LaunchTime 04:00:46Z); gold/trigger-pending.json 404; open_deploys read across 27 worktrees (123 unique files): the ledgers naming opal-data-bd code/gold (advi-firmbkts fb-f-9, fb-j-3, fb-j-7, bd-gold-etf-classifier-cash-type, secclass-e102) each carry a CLOSED completion record in change_management; none touches E_18 or gold_dispatch.sh as an open act | CLOSED 20261017T083357Z |
| P | verify | Leg P: code/gold IsLatest census and etf-classifications state to deliverables E111_LEGP_* | file paths, key and page counts | deliverables/E111_LEGP_20261017.json: code/gold 1 version page, 370 versions seen, 100 delete markers seen, 290 latest keys; deliverables/E111_LEGP_TABLE_20261017.json: etf-classifications 3 scan pages, 11375 items, seeded present 13/13, held-out absent 9/9, first 200 sorted keys with last_updated recorded | CLOSED 20261017T083357Z |
| D1 | s3-prefix | s3://opal-data-bd/code/gold/E_18.detect_new_securities.py | safe-deploy comp-pipescript deployed MATCH line, served ETag f5c03ee6 | safe-deploy.sh E_18 rc 0 (HALT_ACK=1 for the already-read GO msg 7445): VERIFY OK comp-pipescript deployed data/black_diamond/scripts/gold/E_18.detect_new_securities.py; served ETag f5c03ee69eaa1810159aefb6e2145bb4, new VersionId ij219ZfHeFTL7H_e8evmlrOipp2QHz_c at 2026-10-17T08:36:35Z (rollback VersionId wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB) | CLOSED 20261017T083901Z |
| D2 | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh | safe-deploy comp-pipescript deployed MATCH line, served ETag 165933f6 | safe-deploy.sh gold_dispatch.sh is a no-op (.sh outside its deploy scope: 'no deploy-scope script files detected'); shipped by aws s3 cp --sse AES256 as in FB-j-3/FB-j-7 at 08:38:26Z; served ETag 165933f6dd0068a649f9757d9b86f303 equals repo md5, 76036 bytes, new VersionId fzd8_e.BSTe4C757WgGhHx88DBf.v0iy (rollback VersionId .bNYVetB5sGV8bZki7EgXBfChCH_uPyE); comp-pipescript deployed finds the .sh ABSENT IN TREE [bd-gold] (it indexes scripts only), so the MATCH is by e108_shipped_check md5 | CLOSED 20261017T083901Z |
| C | verify | e108_shipped_check.py reads E108-SHIPPED ok=True; pre/post code/gold census shows only the two moved | check line, census diff | e108_shipped_check.py: E108-SHIPPED ok=True e18=f5c03ee6\|f5c03ee6\|MATCH dispatch=165933f6\|165933f6\|MATCH e18_old_list_lines=0 dispatch_syntax=0 chain=True; code/gold census deliverables E111_LEGP_20261017.json 290 keys vs E111_LEGD_AFTER_20261017.json 290 keys: added=0 removed=0 moved=[E_18, gold_dispatch.sh] | CLOSED 20261017T083901Z |
| Q | verify | Leg Q Branch 1: runner service stopped first, BD_PLATINUM_MODE=canonical gold_dispatch.sh --single E_18 no --upload; exit 0, no ERROR, 9 held-out unresolved, etf-classifications unchanged | CommandIds, lines, table diff |  | OPEN |
| G | git | ledger, deliverables and logs committed | commit hash with push state |  | OPEN |

## Log

- 20261017T083332Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 7 leg(s)
- 20261017T083357Z LEG V closed: 08:30-08:50Z: served E_18 ETag a7820a20 VersionId wb5QYkh7 (base) and gold_dispatch.sh ETag 882a910b VersionId .bNYVetB5
- 20261017T083357Z LEG P closed: deliverables/E111_LEGP_20261017.json: code/gold 1 version page, 370 versions seen, 100 delete markers seen, 290 latest k
- 20261017T083901Z LEG D1 closed: safe-deploy.sh E_18 rc 0 (HALT_ACK=1 for the already-read GO msg 7445): VERIFY OK comp-pipescript deployed data/black_di
- 20261017T083901Z LEG D2 closed: safe-deploy.sh gold_dispatch.sh is a no-op (.sh outside its deploy scope: 'no deploy-scope script files detected'); ship
- 20261017T083901Z LEG C closed: e108_shipped_check.py: E108-SHIPPED ok=True e18=f5c03ee6|f5c03ee6|MATCH dispatch=165933f6|165933f6|MATCH e18_old_list_li
