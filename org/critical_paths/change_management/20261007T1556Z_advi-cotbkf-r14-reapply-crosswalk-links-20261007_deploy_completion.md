# Deploy Completion Record
**Date opened:** 2026-10-07T15:56:08.506692+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF r14 E1: crosswalk + account_links re-applied on the one signing table (opal-data-assets/commonwealth/cottonwood/silver/{crosswalk,account_links}/date=2026-06-23/, 4 objects; pins fatOX6x0/RGQHH1zi/OQ9YHJ3h/JY3f29AV)
**Authored by:** 2.0.0_SA_COO~C2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | crosswalk replaced | VersionIds moved; read back 1533 rows, 471 MATCHED |  | OPEN |
| L2 | verify | account_links replaced | VersionIds moved; read back 1450 rows, 212 LINKED, B3S605711->B3S676722 LINKED, RGY003616 NOT_LINKED |  | OPEN |
| L3 | verify | rule-change diff vs the new applied tables | crosswalk_changed=0 account_links_changed=0 |  | OPEN |

## Log

- 20261007T155608Z OPENED by 2.0.0_SA_COO~C2 with 3 leg(s)
