# Deploy Completion Record
**Date opened:** 2026-09-29T03:42:55.464991+00:00
**Status:** OPEN
**Deploy:** Performance adapter reads the holdings-basis gold for 49F (TO-IB-pr-201/202; PRD v0.19 rulings 10, 12): code (holdings_gold.py + retained/installed/entry + schema OPAL_HOLDINGS) + adapter IAM (performance root) + 49F bucket fence (shared-infra); engine read retires in the same act; applies AFTER window 21 closes
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live qfxZ0DzB: only the named members differ (+holdings_gold.py); flat + ~Y zip_module_census; cold start with /var/task mapped |  | OPEN |
| P1 | verify | plans for both roots | performance root plan: role policy + lambda code only; shared-infra plan: bucket policy only; no other change |  | OPEN |
| D1 | activation | apply shared-infra bucket fence + performance root | halves at HEAD; W21 closed; CRO before-read (49F YTD/1Y + a retained engine report + COT/INF controls); safe-apply both; readback CodeSha + policies; real cold-start invoke; re-plan 0 |  | OPEN |
| A1 | verify | the Performance page | 49F figures served OPAL_HOLDINGS with page words; a retained engine report not reopened; COT and INF unchanged; both readers counted |  | OPEN |

## Log

- 20260929T034255Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
