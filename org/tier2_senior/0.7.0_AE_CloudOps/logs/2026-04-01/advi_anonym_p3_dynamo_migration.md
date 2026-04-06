# ADVI_ANONYM P3 -- DynamoDB Migration + Test Accounts -- 0.7.0_AE_CloudOps

**Date:** 2026-04-01
**Task Order:** ADVI_ANONYM.009.ae-dynamo-migration-test-accounts

---

## Objective

Three DynamoDB operations on opal-users-v2: (1) batch update opal-capital users
from tier=internal to tier=advisor, (2) create FIRM#mockadv, (3) create 3 test accounts.

---

## Operation 1: Tier Migration

**Scan result:** 14 opal-capital USER records with tier=internal (+ 1 FIRM META record)

**Updated:** 13 users (skipped andrew@opalinvest.com per constraint)

| PK | Email |
|----|-------|
| USER#usr_03c46749f8a7 | jim@opalinvest.com |
| USER#usr_99b641c31d96 | jeanette@opalinvest.com |
| USER#usr_379860be7479 | user@opalinvest.com |
| USER#usr_fcd972257abd | lauren@opalinvest.com |
| USER#usr_262505fd8cfa | wayne@opalinvest.com |
| USER#usr_91abace15084 | yang@opalinvest.com |
| USER#usr_44d7e5a2bcb7 | adam@opalinvest.com |
| USER#usr_4cba1315fd0e | keith@opalinvest.com |
| USER#usr_1fca89a90772 | austin@opalinvest.com |
| USER#usr_3579e8d512bf | wade@opalinvest.com |
| USER#usr_4cbbad76772c | manav@opalinvest.com |
| USER#usr_a5ae550bd45a | aj@opalinvest.com |
| USER#usr_6ce8f8fdb8de | menachem@opalinvest.com |

**Post-migration scan (tier=internal, firmId=opal-capital):** 2 records remain -- both expected:
- USER#usr_7f83e30de95f (andrew@opalinvest.com) -- intentionally skipped per TO constraint
- FIRM#opal-capital META -- FIRM record, not a user, out of scope

All USER records updated. 0 unintended internal-tier opal-capital users remain.

---

## Operation 2: FIRM#mockadv Created

| Field | Value |
|-------|-------|
| PK | FIRM#mockadv |
| SK | META |
| firmId | mockadv |
| name | MockADV |
| tier | advisor |
| s3Bucket | opal-data-bd |
| domain | mockadv.test |
| status | active |
| createdAt | 2026-04-01T00:00:00Z |

Verified via get-item: confirmed.

---

## Operation 3: Test Accounts Created

| PK | role | firmId | advisorId | Verified |
|----|------|--------|-----------|---------|
| USER#user@opalinvest.com | user | opal-capital | -- | OK |
| USER#travis.penfield@49financial.com | admin | 49financial | -- | OK |
| USER#chase.bertrand@49financial.com | user | 49financial | Chase Bertrand | OK |

---

## Chase Bertrand advisorId Confirmation

Checked s3://opal-data-bd/gold/advisors/ for architect folder names.
Folder: `Chase Bertrand/` -- exact match.
advisorId written: `"Chase Bertrand"` (case-sensitive confirmed).

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD (no code changes, DynamoDB only)

13 opal-capital users migrated from tier=internal to tier=advisor.
FIRM#mockadv created. 3 test accounts created and verified. Chase Bertrand
advisorId confirmed against gold data folder name.

---

## Next Steps

1. **[DS 0.4.0_DS_ClientPlatform]** ADVI_ANONYM.007 code changes can now be tested against real DynamoDB records.
2. **[DT 0.4.0_DT_ClientPlatform]** Deploy Lambda after DS + AE both signal complete.
