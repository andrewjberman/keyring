# Better Cottonwood account matching: the CRM upload, name matching, and every identity column on both sides (2026-10-15 ~18:2xZ)

**Author:** `4.0.0_SA_CRO~DELL2`, on Andrew's word (record `ANDREW_DIRECT_20261015_175xZ_BETTER_MATCHING_CRM_KEY_AND_COLUMN_RUN.md`
@628b6102dc).

**Method:** read-only, Cottonwood data only. **No PII value was printed, written or reported.** Values were read in memory, names were
compared as salted hashes, and every value-bearing scratch file was deleted.

**Today's crosswalk:** `data/assets/scripts/silver/commonwealth_crosswalk.py`, live at
`s3://opal-data-assets/commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.csv`.
- R1 (same number) matched 0.
- R2 (in-kind holdings fingerprint) matched all 471 of 1,533.
- Reverse match: 460 of 860 active BD accounts matched; 387 none (168 new clients after the migration).

## 1. The CRM upload exists, and agents are locked out of it by Andrew's own rule

- **What:** `CRM_CottonwoodCapitalAdvisors.zip`, one of the five members of the Commonwealth delivery `Files.zip` (row S1,
  `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md:26`).
- **Its home:** `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip`, register
  exception X15 (`infra/logic/06_CONFORMANCE_LEDGER.md`).
- **Access:** under Andrew's **C-RESTRICTED** call, the prefix denies every read except Andrew and one emergency-access role. The landing is
  Andrew's own act through that role (PRD `ADVI_COTBKF_PRD.md:111-112`; decomposition round 4 :71).
- **Measured:**
  - `head-object` returns 403 to the dell2 agent user. That is consistent with the deny, and cannot tell "landed" from "not landed".
  - The prefix lists empty to this user.
  - The delivery manifest in `opal-data-assets` lists only the other 4 files.
  - The coverage statement says "CRM: NOT COVERED ... held back behind the C-RESTRICTED prefix" (rows S7, W19-S1).
- **So:** its columns are unmeasured, and the intermediary-key test against it could not run.

## 2. Name matching: never tried before

The crosswalk has only R1 and R2. Every "name" in the ADVI_COTBKF records is a security or asset name, never an account name.

## 3. Identity-bearing columns (names only; fill rate)

| Side | Table | Columns |
|---|---|---|
| Commonwealth | positions / transactions / performance | `AccountNumber` / `Account_Number` (1.00), `Advisor_ID` (4 distinct) |
| Commonwealth | `account_links` | `old_account`, `new_account` (0.15: Commonwealth's own renumbering, 212 linked), `client_line` (1.00, 1,256 distinct), `newest_account` |
| Commonwealth | `document_index.listing_fields` | `DisplayName` (8,770 rows, with `Acct`), `ClientName` (932, with `Account`), `HouseholdName` (1,239), `AccountNumber` / `ReportName` (1,034). 738 of 1,533 accounts have a document |
| Black Diamond | `accounts_dimension_latest` (1,005) | `account_id`, `account_name` (0.85), `account_display_name` (0.83), `relationship_id` (1.00) / `relationship_name` (0.85), `account_open_date` / `first_transaction_date` (0.80), `account_type` / `account_registration_type` (0.86), client city/state/zip (0.85) |
| Black Diamond | `fact_holdings` | `AccountID`, **`Account Number`** (the CUSTODIAN number, 1,001 distinct) |
| Black Diamond | `advisor_assignments` | rep fields, 1 distinct value: unusable |

Neither readable side carries a tax ID or date of birth. By design (C-SENSITIVE) those live only in the CRM zip.

## 4. Measured join rates

**R1 against the custodian number.** R1 compared against BD's internal `account_id`. Against BD's custodian `Account Number`:
- 89 Commonwealth accounts are equal;
- positive control: the 2 already matched among them agree with R2;
- **87 NEW deterministic forward links;**
- all 87 are closed BD accounts outside the active set, so they add 0 to the 387 unmatched active accounts.

**Exact account name** (normalized, salted-hash, token-sorted), unmatched Commonwealth (1,062) x unmatched active BD (387):
- 43 hits, **30 unique 1:1**;
- 29 corroborated (date window 29, same registration class 18, holdings candidate 5);
- positive control: only 93 of 462 already-matched pairs agree on exact name, because the two systems format names differently.

**Name to household** (token overlap >= 0.6):
- positive control: unique household and correct 138, **wrong 0**; 7 multi-household; 317 no hit. Name is a precise household key with about
  30% recall;
- within the correct household, registration class alone picks the right account 45 times and the wrong one 15 times, with 78 ambiguous. So
  name plus class is **not** deterministic;
- applied to the unmatched: only 232 of the 1,062 carry a document name. 59 reach a unique household; 16 reach one unmatched active account of
  the same class.

**Commonwealth `client_line` siblings:** 89 unmatched Commonwealth accounts share a client line whose matched siblings sit in one BD household.
For 39 of them, that household holds an unmatched active account.

## 5. Options, ranked

| # | Option | Yield (measured where possible) | Tier (FWD-9: a link is never guessed) | Needs |
|---|---|---|---|---|
| 1 | **The CRM zip:** Andrew reads it, or names a reader under C-RESTRICTED | Unmeasured. If it carries old and new numbers or a tax ID, it is the only true stable key, and likely settles most of the 101 "no identifier" | deterministic | **Andrew** |
| 2 | **R3, custodian-number equality** | 87 forward links; 0 active | deterministic (control 2 of 2) | code only |
| 3 | **R4, name to household, then a narrowed holdings fingerprint inside the household, plus the date window** | household stage 138/0 precise; ~59 unmatched reach a household now | deterministic only when the fingerprint passes; else candidate | a CTO rule for the inside-household bar |
| 4 | **Client-line propagation** (a matched sibling sets the household, then option 3's inside step) | 89 households, 39 touching unmatched active accounts | candidate | -- |
| 5 | **Exact name 1:1 plus a second field** | 29 corroborated, almost all by date | candidate for a person (15 wrong class picks in control) | a person |
| 6 | **A mapping file** (old to new numbers) from Cottonwood or Black Diamond | full, if supplied | deterministic | a request to Cottonwood |

168 of the 387 unmatched active accounts are new clients after the migration. No predecessor exists to find.

## Not read

- The CRM zip (403, restricted).
- The imaging `CLNT` PDFs.
- BD bronze (only completion markers present).
- Holdings overlap inside a household (option 3's yield is estimated, not run).
- Other firms' data (cross-firm rule).

-- 4.0.0_SA_CRO~DELL2
