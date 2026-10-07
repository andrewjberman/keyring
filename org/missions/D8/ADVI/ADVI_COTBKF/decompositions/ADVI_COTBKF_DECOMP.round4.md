# ADVI_COTBKF decomposition -- ROUND 4 (issuer 2.0.0_SA_COO~C under /canonical-drive; drafted 2026-10-07 ~04:4xZ)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:** the CTO's round-2-3 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_R2_R3_20261007.md`
(msg 105940; five rulings, six-item ENRICHMENT LIST), on the CVO's grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md` @c4b54a904b. Issued after NFRA_CTLPLN's Dell cells
drained (@c649197dd0), as the analysis ordered.

**Rule 24.** Domain: the six enrichment items. Subtraction, each item against the world at the cut:
- Item 1 (imaging archives to bronze): DONE by the issuer's act in round 3 -- ledger `advi-cotbkf-r3-imaging-and-silver-20261007` CLOSED
  4/4 @97463796de; HKE/HJH/4XF read back by etag, the manifest holds 4 entries. No cell.
- Item 6 (the crosswalk's first version, FWD-8): DONE in round 3 (CB-c-3, CVO grade CB3c3-AC3 MET; silver `crosswalk` 1,533 rows read
  back). Its rulings-3/4 follow-ups are item 3 below. No separate cell.
- Item 5 (FWD-5): the INDEX is done (CB-c-2; silver `document_index` 11,119 rows); C-DOCUMENTS' second half -- each UNIQUE document
  unpacked once into a documents table -- is not. One cell.
- Items 2, 3, 4: one cell each, item 3 split by write set (FWD-9 links; FWD-8 scoring and the near-match list).
Five cells, one intent each, disjoint writes. **Not in this round (CTO):** the price pull itself, which waits on MDPF_SECHIST's store.

## Measured constraints (read at the base, 2026-10-07 ~03:5xZ-04:4xZ)

1. **Buckets:** `s3api list-buckets` = 40. Firms in the registry (`infra/logic/registry/scopes.json`, class `FIRM`): `49financial`
   (bucket `opal-data-49financial`, bucket alias `opal-data-bd`), `inflection` (alias `opal-data-inf`), `cottonwood` (`opal-data-cottonwood`,
   alias `opal-data-cot`). Cottonwood's own = USABLE; another firm's = BARRED; no firm in the address = USABLE (ruling 1).
2. **Legacy stores (ruling 2):** six rows landed by `4.0.0_SA_CRO` @4991b8b11b, `lib/opal_naming.legacy_address(<key>, **params)`:
   `cottonwood-silver-canonical-prices`, `cottonwood-gold-canonical-holdings` (date=), `rivalfunds-etfs-gold-security-market`,
   `etfs-bbg-testpull-ticker-history` (ticker=), `etfs-bbg-fund-daily` (date=), `portal-canon-return-daily-values`. Unknown key -> KeyError.
3. **Accounts:** 1,533 in silver transactions; the 2026-06-23 positions table holds 83 (`AccountNumber`, all in transactions); so **1,450
   end before 2026-06-23** (459 before 2018, 759 before 2026).
4. **Crosswalk (round 3, local run = served):** MATCHED 439, NOT_MATCHED 1,094 (`CLOSED_BEFORE_CURRENT_HISTORY` 758,
   `NO_CURRENT_ACCOUNT_HOLDS_POSITIONS` 263, `NO_SECURITY_POSITIONS` 37, `AMBIGUOUS` 36); **17** rows score in [0.65, 0.8).
5. **Documents:** `document_index` 11,119 rows, every one present and listed; 24,489 archive paths (202 docs in 1 archive, 8,464 in 2,
   2,453 in 3); doc types STMT 7,736, NCSD 1,239, TXRP 1,034, CLNT 932, ADVS 165, REPR 13. `document_id` = `<file_name>|<crc32 hex>|<bytes>`.
   Bronze: `plan_id=HKE/HKE.zip` 1,554,270,895 B, `plan_id=HJH/HJH.zip` 1,503,993,172 B, `plan_id=4XF/4XF.zip` 113,362,389 B.
6. **C-RESTRICTED:** R20 X15 (`4.0.0_SA_CRO` @3d5dd4bf52): the CRM zip's key
   `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip`; restricted prefix
   `commonwealth/cottonwood/bronze/crm/` (empty today). Readers (CTO ruling msg 105951): IAM user `Andrew_Berman_Console` (console login,
   0 access keys) plus one break-glass role `name('cloudops', <cottonwood scope>, 'restricted-breakglass', 'role')` ->
   `cloudops-cot-restricted-breakglass-role`, assumable only by that user; the single landing goes through that role. The agents run as
   `user/Andrew_Berman`, which is refused. File `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` (one for_each policy, one
   statement `DenyForeignFirmPrincipals`, live policy the same), granted to lane ADVI_COTBKF_C @b573ddee69 with
   `infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py`.

## The cells

| cell | what | serves | risk | chain / slot |
|---|---|---|---|---|
| `CB-d-1` | the price census COMPLETE over all 40 buckets and graded USABLE / BARRED; USABLE legacy stores read only through `legacy_address()`; no BARRED store read | FWD-3 | LOCAL | A, `0.9.0_WK_ADVI_COTBKF~12` |
| `CB-d-2` | FWD-9 for every account that ends before 2026-06-23 (1,450), chains followed to the newest account | FWD-9 | WORLD | B, `0.9.0_WK_ADVI_COTBKF~13` |
| `CB-d-3` | FWD-8: in-kind exits scored whatever their date; the 17-ish near-matches listed for Andrew, never applied | FWD-8 | WORLD | C, `0.9.0_WK_ADVI_COTBKF~14` |
| `CB-d-4` | C-RESTRICTED: the cottonwood bucket's restricted-prefix statements and the break-glass role; plan and simulation only | FWD-7 | WORLD | D, `0.9.0_WK_ADVI_COTBKF~15` |
| `CB-d-5` | C-DOCUMENTS: each unique document unpacked once into the documents table (planned and verified against bronze; the apply is the issuer's) | FWD-5 | WORLD | E, `0.9.0_WK_ADVI_COTBKF~16` |

## Write sets (disjoint)

- **CB-d-1:** `data/assets/scripts/analysis/commonwealth_price_census.py` (new; replaces `commonwealth_price_coverage.py`, deleted), `data/assets/scripts/analysis/tests/test_commonwealth_price_census.py`.
- **CB-d-2:** `data/assets/scripts/silver/commonwealth_account_links.py`, `data/assets/scripts/silver/tests/test_commonwealth_account_links.py`.
- **CB-d-3:** `data/assets/scripts/silver/commonwealth_crosswalk.py`, `data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py`.
- **CB-d-4:** `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`, `infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py`.
- **CB-d-5:** `data/assets/scripts/silver/commonwealth_documents.py`, `data/assets/scripts/silver/tests/test_commonwealth_documents.py`.
- Each: its deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 5 of 5 chains, cap 8` -- no cell consumes another's output this round.

## The issuer's acts (one change-management ledger entry, opened at the first apply)

1. After the drain: CB-d-2 and CB-d-3 `--apply` (silver `account_links`, `crosswalk` re-written for the same date), each read back; the
   near-match list goes to Andrew through `1.0.0_SA_CTO`.
2. CB-d-5 `--apply` (silver `documents`, about 11,119 objects), read back by count and a sample of SHA-256s; one statement and one tax form
   opened by account and date (FWD-5's DONE WHEN) for the CVO.
3. CB-d-4: the apply is the file's owner's under a never-widen pair; then Andrew lands the CRM zip through the break-glass role on his word.
