# ANDREW-DIRECT 2026-08-27 — `/account-api/*` EGRESS GRANTED, TIER-3 EXERCISED, NIXON + TRACEY ACTIVE

**Lane:** `0.4.0_DS_ClientPlatform~Z` · **Project:** `OPAL_TAXSMA` (PRD D3)

## THE WORD, VERBATIM

> *"yes egress approved for account-api, activate nixon and tracey"*

⭐ **THIS IS THE GATE THE CODE NAMES BY NAME.** Two modules were waiting on this exact sentence:
- `taxsma_resolver.py:16-19` — tier-3 *"is a NEW egress surface -> HARD-GATED on Andrew's explicit
  egress-word extension (PRD D3). Never called without it."*
- `insurance_leg.py:83-85` — refuses `accountdetailsearch` because it is *"a DIFFERENT PROJECT'S gate
  (OPAL_TAXSMA PRD D3, taxsma_resolver.py:15-19)"*.

**This record exists so the lift has a durable carrier.** The refusals cite a *word*; a word with no
record is unauditable, and the next seat to read those lines needs to find this file.

---

## 1. THE LADDER, WALKED IN ORDER — TIER-1 FIRST, NOT STRAIGHT TO THE EGRESS

⛔ **The egress was authorized; that is not a reason to spend it.** Tier-1 is zero-egress and was
re-run first, because the two accounts were enrolled `pending_resolution` when they were *absent from
the xref*, and the xref is a daily partition that may since have moved.

| | result |
|---|---|
| latest partition | `blackdiamond/49f/silver/dim_account_xref/date=2026-08-24/data.parquet`, **6,201 rows** |
| Chiles **control** | **1 exact hit**, `bd_internal_id=22596361` — the xref read works |
| Nixon / Tracey | **0 hits** |

**AND THE ABSENCE WAS PROVED, NOT ASSUMED.** A grain-mismatched join key manufactures absence, so
every plausible rendering was swept: zero-padded-10, unpadded-int, dashed, last-4, substring, and
**every one of the 10 columns**. Nixon and Tracey return **0 occurrences frame-wide**; Chiles returns
3. The key form is confirmed zero-padded-10 by the control's own leading zero.

⚠ **NOTED, NOT DIAGNOSED:** the newest partition is `date=2026-08-24` while today is `2026-08-27`.
Per the trading-calendar rule this is **not** called stale here — counting trading days is a separate
act and no freshness verdict is claimed. Flagged only because *if* the xref advances, newly-traded
accounts may resolve at tier-1 for free.

## 2. TIER-2 SKIPPED ON THE RECORD, NOT RE-TESTED

`taxsma_resolver.py:10-14` records the 2026-07-21 Andrew-authorized probe: the sanctioned
`portfolioreporting` surface returns a **masked last-4** and accepts no exact-number filter.
**"Do not re-test"** — honored. Re-running it would have been repetition, not corroboration.

## 3. TIER-3 — AND MY FIRST TWO ATTEMPTS WERE WRONG, WHICH THE CONTROL CAUGHT

⛔ **THE POSITIVE CONTROL FAILED FIRST, AND THAT IS THE ONLY REASON THIS RECORD IS TRUSTWORTHY.**

| attempt | result | what it would have produced |
|---|---|---|
| `POST /account-api/query/accountdetailsearch`, body `{}` | 25 rows, **all annuity** (`LNANN_`, `METVA_`) | Chiles **0 matches** |
| 9 guessed paging/filter bodies (`take`, `page`, `skip`, `pageSize`, `searchText`, `filters`…) | **identical 25 rows every time** | Chiles **0 matches** |
| `RelationshipAccountDetailSearch`, guessed body | 25 rows, `accounts` **empty** | Chiles **0 matches** |

**Had I reported off any of those, the finding would have been "Nixon and Tracey are not in Black
Diamond" — with three independent-looking confirmations.** They were all one broken retrieval. A
failed retrieval returns a *value*, and that value reads exactly like an absence.

⭐ **THE FIX CAME FROM A CAPTURE, NOT A GUESS.**
`data/black_diamond/API/domains/insurance/endpoints/payloads/account_detail_search.json` holds a
real `requestBody`: the schema is **`limit`/`offset`** (not `take`/`skip`), a wildcard
`search: {"id":["**"],"name":["**"]}`, and an **`include` block that must set `accounts: true`** —
which is why nested accounts came back empty and every guess got the server default of 25.

⛔ **ONE FIELD WAS DELIBERATELY NOT COPIED FROM THE CAPTURE.** Its
`accountTypeId: [1,2,3,18,19,20,22,21,59]` is an **annuity-type filter** from the *insurance*
capture. Copying it wholesale would have excluded Schwab account types and **manufactured the very
absence this exercise exists to disprove** — a borrowed payload carries its author's scope.

## 4. THE RESOLUTION — EXACT, 1 OF 1, CONTROL PASSED IN THE SAME SWEEP

**DENOMINATOR: 4,686 relationships → 9,830 accounts**, `accountNumber` populated 9,830 / 9,830.

| account | schwab # | matches | `internalId` | external id | relationship |
|---|---|---|---|---|---|
| **Chiles — CONTROL** | `0027265115` | **1** | **22596361** ✅ *expected 22596361* | `z0822596361` | Chiles, Colby & Nicole |
| **Nixon** | `0084073310` | **1** | **22659431** | `z0822659431` | Nixon, Matthew & Malita |
| **Tracey** | `0076459710` | **1** | **23221671** | `z0823221671` | Tracey, Shawn |

**EXACT on the full account number. No fuzzy, no last-4, no surname — the PRD ss.2 non-negotiable.**
Every target returned **exactly one** match; the fail-loud arm was never reached.

⭐ **AN INDEPENDENT CROSS-CHECK NOBODY ASKED FOR:** the external ids decompose under the resolver's
own `_BD_ID_RE` (`^z\d{2}(?P<internal>\d+)$`) to `22659431` and `23221671` — **the internalIds the
same rows carry in a different field.** Two fields agreeing is a second instrument, not a restatement.

## 5. THE ACTIVATION

`status=active` is **not a flag flip**: `taxsma_registry.py:81-84` refuses `active` without a resolved
`bd_internal_id`. The resolution *is* the activation.

⛔ **MERGE, NEVER REBUILD.** `enroll()` replaces `accounts[idx]` **wholesale**, and `_validate_entry()`
fills any absent `ENTRY_FIELD` with `None` — so a candidate built from scratch would have silently
blanked `client_name` / `trade_start_date` / `strategy`. Each candidate was the **existing entry plus
the resolution**, and a field-preservation check ran after: **`lost_fields=NONE` for both.**

**VERIFIED BY RE-READING S3, not from the call's return value:**

```
0027265115  active              22596361   Chiles
0035940058  pending_resolution  None       Bump
0076459710  active              23221671   Tracey, Shawn      <- was pending_resolution
0084073310  active              22659431   Nixon, Matthew & Malita  <- was pending_resolution
0091939812  pending_resolution  None       Macy
```
`list_active()` → **3 accounts** the daily ETL will now pull (was 1).

## 6. SCOPE, AND WHAT WAS NOT DONE

- **`Bump` (0035940058) and `Macy` (0091939812) remain `pending_resolution`.** The word named Nixon
  and Tracey; the method now exists and would very likely resolve both, but **widening an activation
  beyond the two accounts named is the sovereign's call, not this lane's.**
- **`DRY_RUN=0` was set in the probe process's environment ONLY.** Nothing was persisted, no Lambda
  env changed, no Terraform touched. The estate's default remains `DRY_RUN=1` (fail-closed).
- **`taxsma_resolver.py` STILL RAISES `NotImplementedError` at tier-3.** The method is proven but the
  code is unchanged — `infra/aws/lambda/**` is **DT/AE lane** under Rule 13, not DS's to commit.
  §7 is the spec for whoever owns it.
- **VENDOR CALL COUNT, stated because it is a cost:** ~39 search requests + 5 token mints. **10 of
  those 39 were spent on the wrong schema** — the price of an uncaptured request body.

## 7. SPEC FOR THE TIER-3 BUILD (owner: DT/AE lane — NOT built here)

```
surface  POST /relationship/request/query/RelationshipAccountDetailSearch   (auth: clientview)
body     {"include": {"total": true, "accounts": true, "accountCount": true, ...},
          "onlyActiveRelationships": true, "limit": 200, "offset": <page>,
          "sort": "name", "order": "asc", "search": {"id": ["**"], "name": ["**"]}}
         ⛔ do NOT copy accountTypeId from the insurance capture -- it excludes Schwab types
page     read `total` from a limit=1 probe, then page offset until offset >= total
match    EXACT on account.accountNumber == normalize_schwab(x) or its unpadded form; require
         len(hits) == 1; raise on 0 or >1. NEVER last-4, NEVER name.
control  Chiles 0027265115 -> internalId 22596361 MUST resolve in the SAME sweep, or the
         result is INADMISSIBLE. This is not optional -- it is the only thing that
         distinguishes a real absence from a broken query, and it caught three of mine.
```

**AND THE `/account-api/*` SURFACE ITSELF IS A SEPARATE, UNSOLVED QUESTION.** `accountdetailsearch`
answered 200 and returned unmasked numbers — confirming the PRD's premise — but **ignored every body
shape tried** and returned a fixed 25-row annuity slice. `0.6.0_AE_PartnerETL` had already recorded it
as **PROSE-ONLY, 0 captured payloads, UNEXERCISED**; that is now **EXERCISED with a null result on
the request contract**, which is worth more than the prose but is not a working call. The relationship
surface is what works, and it is the *sanctioned* one.
