# Deploy Completion Record
**Date opened:** 2026-10-07T15:56:08.506692+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T155916Z
**Deploy:** ADVI_COTBKF r14 E1: crosswalk + account_links re-applied on the one signing table (opal-data-assets/commonwealth/cottonwood/silver/{crosswalk,account_links}/date=2026-06-23/, 4 objects; pins fatOX6x0/RGQHH1zi/OQ9YHJ3h/JY3f29AV)
**Authored by:** 2.0.0_SA_COO~C2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | crosswalk replaced | VersionIds moved; read back 1533 rows, 471 MATCHED | applied 15:57Z rc 0 from dell2 (code @79e9c35429, one signing table): crosswalk.parquet fatOX6x0... -> wv5z6zeRnWQrPGfO3UcmrxlIaz3ozzLZ (148,093 B), crosswalk.csv RGQHH1zi... -> 4MzpNZ7sd3UZoMzXR.8AInpZdRN59MmM (711,988 B); read-back 1,533 rows, 471 MATCHED; run line near_matches_applied=0 near_matches=22 | CLOSED 20261007T155915Z |
| L2 | verify | account_links replaced | VersionIds moved; read back 1450 rows, 212 LINKED, B3S605711->B3S676722 LINKED, RGY003616 NOT_LINKED | applied 15:5xZ rc 0: account_links.parquet OQ9YHJ3h... -> iSS.QIb0709_7o8G3Wkt0eLLHRMpb5hc (145,773 B), account_links.csv JY3f29AV... -> 19fOZaSljGiZwG84sytzy0ICwOSYezWz (885,007 B); read-back 1,450 rows, 212 LINKED; B3S605711 -> B3S676722 LINKED; RGY003616 NOT_LINKED LEFT_COMMONWEALTH | CLOSED 20261007T155916Z |
| L3 | verify | rule-change diff vs the new applied tables | crosswalk_changed=0 account_links_changed=0 | commonwealth_rule_change_diff.py against the newly applied tables: RULE-CHANGE-DIFF crosswalk_changed=0 crosswalk_matched_after=471 account_links_changed=0 account_links_linked_after=212; branch A | CLOSED 20261007T155916Z |

## Log

- 20261007T155608Z OPENED by 2.0.0_SA_COO~C2 with 3 leg(s)
- 20261007T155915Z LEG L1 closed: applied 15:57Z rc 0 from dell2 (code @79e9c35429, one signing table): crosswalk.parquet fatOX6x0... -> wv5z6zeRnWQrPGfO3
- 20261007T155916Z LEG L2 closed: applied 15:5xZ rc 0: account_links.parquet OQ9YHJ3h... -> iSS.QIb0709_7o8G3Wkt0eLLHRMpb5hc (145,773 B), account_links.cs
- 20261007T155916Z LEG L3 closed: commonwealth_rule_change_diff.py against the newly applied tables: RULE-CHANGE-DIFF crosswalk_changed=0 crosswalk_matche
- 20261007T155916Z CLOSED -- all 3 legs proven
