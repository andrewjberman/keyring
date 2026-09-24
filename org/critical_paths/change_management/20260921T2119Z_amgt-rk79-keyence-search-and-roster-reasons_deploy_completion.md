# Deploy Completion Record
**Date opened:** 2026-09-21T21:19:31.296114+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260921T212253Z
**Deploy:** AMGT-rk-79: one CEO web search for 6861_JP_Equity under Andrew's per-use word plus readable roster reasons; in-place rewrites of management/v1/{6861_JP_Equity,CSL_AU_Equity,CAT_US_Equity}/2026-09-19.json
**Authored by:** 0.9.0_WK_AMGT_RESAPP~79
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | management/v1/6861_JP_Equity/2026-09-19.json | one new version, diff only roster_reason/absence_reason_evidence/ceo_profile/ceo_public_profile, SERP at most 3, model_usd at most 1.00 | POST 6861_JP_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'ceo_profile', 'ceo_public_profile', 'roster_reason'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status UNRESOLVED-SOURCE \| reason_none_free True \| roster_reason The Japanese annual securities report (Yuho) was found, but its officer section is empty, so no officers could be read from the filing.
POST CSL_AU_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'roster_reason'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status UNRESOLVED-SOURCE \| reason_none_free True \| roster_reason No filing could be matched to CSL: the SEC ticker belongs to a different company; the company files no recent 10-K with the SEC; no European (ESEF) annual report is filed under its LEI; neither the company website nor the ASX listing page led to an annual report within the crawl limit; and there is no national-regulator source for this listing yet.
POST CAT_US_Equity versions 4 delete_markers 0 changed_top ['absence_reason_class', 'absence_reason_evidence', 'roster_reason', 'roster_status', 'section_refers_to'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status INCOMPLETE-NO-CEO \| reason_none_free True \| roster_reason The 10-K lists its executive officers in Item 1D, which was not read, so this roster is incomplete.
6861 ceo CURATED None ceo_name Tetsuya Nakano serp_requests 1 fetches 3 model_usd 0.046700000000000005
CENSUS_AFTER RESOLVED-without-CEO 0 of 15 []
RAW {'6861_JP_Equity': 14, 'CSL_AU_Equity': 14, 'CAT_US_Equity': 12} MANAGEMENT_OBJECTS 18 FILINGS_OBJECTS 206
POOL objects 3 etag "7a1197377a0fff0e4e861ebc5208cf4a"
SERVED 6861_JP_Equity 200 equal_pre False SERVED None roster_status UNRESOLVED-SOURCE officer_count 1 reason_none_free True reading CONFIRMED reading_none_free True
SERVED CAT_US_Equity 200 equal_pre False ABSENT ROSTER_UNRESOLVED_NO_FALLBACK roster_status INCOMPLETE-NO-CEO officer_count 1 reason_none_free True reading None reading_none_free True
SERVED CSL_AU_Equity 200 equal_pre False SERVED None roster_status UNRESOLVED-SOURCE officer_count 14 reason_none_free True reading NOT_SEARCHED reading_none_free True
SIBLINGS_UNCHANGED 12 of 12 ['ASML_NA_Equity', 'BABA_US_Equity', 'BA_US_Equity', 'COST_US_Equity', 'HAL_US_Equity', 'HD_US_Equity', 'INTU_US_Equity', 'KMB_US_Equity', 'NU_US_Equity', 'PBR_US_Equity', 'SAP_GY_Equity', 'VLO_US_Equity'] | CLOSED 20260921T212253Z |
| L2 | verify | management/v1/CSL_AU_Equity/2026-09-19.json | one new version, diff only roster_reason/absence_reason_evidence, no vendor call | POST 6861_JP_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'ceo_profile', 'ceo_public_profile', 'roster_reason'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status UNRESOLVED-SOURCE \| reason_none_free True \| roster_reason The Japanese annual securities report (Yuho) was found, but its officer section is empty, so no officers could be read from the filing.
POST CSL_AU_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'roster_reason'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status UNRESOLVED-SOURCE \| reason_none_free True \| roster_reason No filing could be matched to CSL: the SEC ticker belongs to a different company; the company files no recent 10-K with the SEC; no European (ESEF) annual report is filed under its LEI; neither the company website nor the ASX listing page led to an annual report within the crawl limit; and there is no national-regulator source for this listing yet.
POST CAT_US_Equity versions 4 delete_markers 0 changed_top ['absence_reason_class', 'absence_reason_evidence', 'roster_reason', 'roster_status', 'section_refers_to'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status INCOMPLETE-NO-CEO \| reason_none_free True \| roster_reason The 10-K lists its executive officers in Item 1D, which was not read, so this roster is incomplete.
6861 ceo CURATED None ceo_name Tetsuya Nakano serp_requests 1 fetches 3 model_usd 0.046700000000000005
CENSUS_AFTER RESOLVED-without-CEO 0 of 15 []
RAW {'6861_JP_Equity': 14, 'CSL_AU_Equity': 14, 'CAT_US_Equity': 12} MANAGEMENT_OBJECTS 18 FILINGS_OBJECTS 206
POOL objects 3 etag "7a1197377a0fff0e4e861ebc5208cf4a"
SERVED 6861_JP_Equity 200 equal_pre False SERVED None roster_status UNRESOLVED-SOURCE officer_count 1 reason_none_free True reading CONFIRMED reading_none_free True
SERVED CAT_US_Equity 200 equal_pre False ABSENT ROSTER_UNRESOLVED_NO_FALLBACK roster_status INCOMPLETE-NO-CEO officer_count 1 reason_none_free True reading None reading_none_free True
SERVED CSL_AU_Equity 200 equal_pre False SERVED None roster_status UNRESOLVED-SOURCE officer_count 14 reason_none_free True reading NOT_SEARCHED reading_none_free True
SIBLINGS_UNCHANGED 12 of 12 ['ASML_NA_Equity', 'BABA_US_Equity', 'BA_US_Equity', 'COST_US_Equity', 'HAL_US_Equity', 'HD_US_Equity', 'INTU_US_Equity', 'KMB_US_Equity', 'NU_US_Equity', 'PBR_US_Equity', 'SAP_GY_Equity', 'VLO_US_Equity'] | CLOSED 20260921T212253Z |
| L3 | verify | management/v1/CAT_US_Equity/2026-09-19.json | one new version, diff only roster_status/roster_reason/section_refers_to/absence_reason_class/absence_reason_evidence, officers byte-equal, no vendor call, no fetch | POST 6861_JP_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'ceo_profile', 'ceo_public_profile', 'roster_reason'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status UNRESOLVED-SOURCE \| reason_none_free True \| roster_reason The Japanese annual securities report (Yuho) was found, but its officer section is empty, so no officers could be read from the filing.
POST CSL_AU_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'roster_reason'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status UNRESOLVED-SOURCE \| reason_none_free True \| roster_reason No filing could be matched to CSL: the SEC ticker belongs to a different company; the company files no recent 10-K with the SEC; no European (ESEF) annual report is filed under its LEI; neither the company website nor the ASX listing page led to an annual report within the crawl limit; and there is no national-regulator source for this listing yet.
POST CAT_US_Equity versions 4 delete_markers 0 changed_top ['absence_reason_class', 'absence_reason_evidence', 'roster_reason', 'roster_status', 'section_refers_to'] equals_allowed True schema_valid True contact_fields [] officers_equal True
   roster_status INCOMPLETE-NO-CEO \| reason_none_free True \| roster_reason The 10-K lists its executive officers in Item 1D, which was not read, so this roster is incomplete.
6861 ceo CURATED None ceo_name Tetsuya Nakano serp_requests 1 fetches 3 model_usd 0.046700000000000005
CENSUS_AFTER RESOLVED-without-CEO 0 of 15 []
RAW {'6861_JP_Equity': 14, 'CSL_AU_Equity': 14, 'CAT_US_Equity': 12} MANAGEMENT_OBJECTS 18 FILINGS_OBJECTS 206
POOL objects 3 etag "7a1197377a0fff0e4e861ebc5208cf4a"
SERVED 6861_JP_Equity 200 equal_pre False SERVED None roster_status UNRESOLVED-SOURCE officer_count 1 reason_none_free True reading CONFIRMED reading_none_free True
SERVED CAT_US_Equity 200 equal_pre False ABSENT ROSTER_UNRESOLVED_NO_FALLBACK roster_status INCOMPLETE-NO-CEO officer_count 1 reason_none_free True reading None reading_none_free True
SERVED CSL_AU_Equity 200 equal_pre False SERVED None roster_status UNRESOLVED-SOURCE officer_count 14 reason_none_free True reading NOT_SEARCHED reading_none_free True
SIBLINGS_UNCHANGED 12 of 12 ['ASML_NA_Equity', 'BABA_US_Equity', 'BA_US_Equity', 'COST_US_Equity', 'HAL_US_Equity', 'HD_US_Equity', 'INTU_US_Equity', 'KMB_US_Equity', 'NU_US_Equity', 'PBR_US_Equity', 'SAP_GY_Equity', 'VLO_US_Equity'] | CLOSED 20260921T212253Z |

## Log

- 20260921T211931Z OPENED by 0.9.0_WK_AMGT_RESAPP~79 with 3 leg(s)
- 20260921T212253Z LEG L1 closed: POST 6861_JP_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'ceo_profile', 'ceo_public_profi
- 20260921T212253Z LEG L2 closed: POST 6861_JP_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'ceo_profile', 'ceo_public_profi
- 20260921T212253Z LEG L3 closed: POST 6861_JP_Equity versions 4 delete_markers 0 changed_top ['absence_reason_evidence', 'ceo_profile', 'ceo_public_profi
- 20260921T212253Z CLOSED -- all 3 legs proven
