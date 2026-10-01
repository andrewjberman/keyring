# Deploy Completion Record
**Date opened:** 2026-10-01T09:16:03.657221+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS item 6: ONE new canonical row, CEMIX (equity / EM / active / fund), written by seed-etf-classifications.py with no flag at seed-source blob c280a8b152 and script blob d48358a5cc; halves COO+CTO SIGNED @37ac46eed2 (NEVER_WIDEN_HALF_REQUEST_SECCLASS_CEMIX_CANONICAL_ROW_20261001.md); rollback is a corrected seed row, no item is deleted
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | verify | the write: pre-run dry run reads 1 of 139 (CEMIX), 0 conflicts; the run; get-item readback; second dry run reads 0 of 139 | script output + get-item | Pre-run dry run 09:16Z: 139 tickers in the module, 138 already correct, 1 to write (CEMIX), 0 CONFLICT lines. Run 09:17:41Z-09:18:02Z, seed-etf-classifications.py with no flag at seed-source blob c280a8b152 / script blob d48358a5cc: rows to write 1 of 139, Items written 1, untouched 138, rc 0. Readback 09:19Z (get-item, consistent read): ticker CEMIX asset_class equity sub_asset_class EM management_style active sector 'Emerging Markets' name 'Causeway Emerging Markets Fund Institutional Class' instrument_kind fund classified_by seed updated_by seed-script last_updated 2026-10-01T09:17:42Z. Table count 2,658 (2,657 before). Second dry run: 139 of 139 already correct, 0 to write. | CLOSED 20261001T091940Z |
| R | verify | the one real run: local Cottonwood Holdings build, 97 of 97 CEMIX nodes equity / EM basis TABLE, no other symbol changes class against the 00:51Z build; names the alias rule that fired and counts the other symbols it classes (CTO half item 1) | build census | Local Cottonwood build of holdings_snapshot.py (--firms cottonwood --dry-run --local-out, no upload), built 10:02Z-10:50Z against the live table, business_date 2026-09-29: 97 of 97 nodes with symbol CEMIX read equity / EM, basis TABLE (67 ASSIGNED 2,039,120.10 USD; 26 OBSERVED 836,730.89 USD; 4 ASSIGNED 200,276.77 USD). Against the 00:51Z build of the same business date: 15,354 actual SECURITY nodes and 541,193,988.39 USD in both; 1,511 symbol/description/basis groups in both; 0 of the 1,508 non-CEMIX groups changed class or sub class. CTO half item 1: the alias rule that fired is the bd-securities row NAME::CAUSEWAY EMERGING MARKETS INSTL (classified_by gpt-4o-mini, confidence 0.6, needs_review true, fixed_income); what else that layer classes today is row MDPF_SECCLASS-S7 @913a7c2f38 (7,108 NAME:: rows; 54 / 819 / 1,478 Holdings nodes at 49 Financial / Cottonwood / Inflection). A first build attempt failed at its last step on the Windows path limit and wrote nothing. | CLOSED 20261001T105431Z |
| S | verify | served: 14:15Z irpt-holdings-snapshot publication, one Cottonwood selection reads CEMIX under Equity and class totals tie (CTO half item 4: this is the acceptance) | page read |  | OPEN |

## Log

- 20261001T091603Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
- 20261001T091940Z LEG W closed: Pre-run dry run 09:16Z: 139 tickers in the module, 138 already correct, 1 to write (CEMIX), 0 CONFLICT lines. Run 09:17:
- 20261001T105431Z LEG R closed: Local Cottonwood build of holdings_snapshot.py (--firms cottonwood --dry-run --local-out, no upload), built 10:02Z-10:50
