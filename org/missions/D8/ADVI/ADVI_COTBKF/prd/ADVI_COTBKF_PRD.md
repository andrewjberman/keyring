# ADVI_COTBKF -- the Cottonwood 10-year backfill from Commonwealth

```json
{
 "project": "ADVI_COTBKF",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md@902feb3a4f",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-06. **Priority:** Andrew's word.
**Brief:** `docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md` @902feb3a4f (`4.0.0_SA_CRO`).
**Andrew's words:** the order, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_16xxZ_COTTONWOOD_COMMONWEALTH_10Y_BACKFILL_SPEC.md`
("Disregard MSTR instruction on using a cottonwood specific bucket. We will use the opal-data-asset format"); the three calls,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_172xZ_COTTONWOOD_BACKFILL_THREE_CALLS_SENSITIVE_IN_FIRM_BUCKET.md`.
**Status DRAFT:** the ENDPOINT below is proposed; Andrew's yes to the eight outcomes is owed before RATIFIED.
**Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO wrote the brief.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An analyst picks one Cottonwood account and reads its whole transaction history, 2013 to
         June 2026, from Opal's own store, and can trace each row to the file Commonwealth sent
         DONE WHEN  EXERCISED -- one real account's history read end to end and one row traced back
         ACCEPT     an analyst names one Cottonwood account and reads every transaction Commonwealth
                    recorded for it, oldest to newest, from Opal's store; for any row they can say which
                    delivered file it came from. Nothing is read from Box, from a download folder or
                    from a spreadsheet someone made
         SOURCE     brief PART I, the candidate thread

  FWD-2  Anyone can find the whole Commonwealth delivery in Opal's store, exactly as it arrived
         DONE WHEN  EXERCISED -- each delivered file found and its size and fingerprint matched
         ACCEPT     all five files Commonwealth shipped are in Opal's store, byte for byte, each with its
                    size and fingerprint written down beside it; nobody has to go back to Box or to a
                    download folder for any of it
         SOURCE     brief O1

  FWD-3  An analyst reads each Cottonwood account's monthly and yearly returns, after fees, back
         to 2013
         DONE WHEN  EXERCISED -- one account's returns read across the whole span
         ACCEPT     for any Cottonwood account in the delivery, an analyst reads its monthly, yearly and
                    since-inception returns after fees, with the benchmark Commonwealth recorded beside
                    them, as Commonwealth reported them
         SOURCE     brief O3

  FWD-4  An analyst reads Cottonwood's client relationship records as Commonwealth held them
         DONE WHEN  EXERCISED -- one household read with its people, relationships and activity
         ACCEPT     households, the people in them, how they are related, the advisors, insurance
                    policies and the logged activity are readable as Commonwealth kept them
         SOURCE     brief O4

  FWD-5  An analyst finds any client document by account, type and date, and opens it
         DONE WHEN  EXERCISED -- one statement and one tax form found by account and date and opened
         ACCEPT     a person searches by account, document type and date and opens the one document
                    they need, without unpacking an archive by hand; a document that appears in more than
                    one advisor's archive is listed once
         SOURCE     brief O5; F4 (duplication across the three archives)

  FWD-6  A person can see what this backfill covers and what it does not
         DONE WHEN  EXERCISED -- the coverage read by someone who was not told it
         ACCEPT     a person can tell, for each kind of record, how far back it goes: thirteen years of
                    transactions and returns, ten of activity, twelve months of statements, two tax
                    years, one day of positions; nobody mistakes one for another
         SOURCE     brief O6; F5; PART III item 4

  FWD-7  Cottonwood clients' most sensitive personal details are held only where Andrew decided,
         and a reader can say who can see them
         DONE WHEN  EXERCISED -- the places those details exist listed, and an unauthorised read refused
         ACCEPT     tax numbers, dates of birth, driver's license and passport numbers exist only where
                    Andrew said they may; anyone can list those places and who can read each; a person
                    without that right who tries is refused
         SOURCE     brief O7; F6; PART V; Andrew's call 1

  FWD-8  An analyst can line up an old Commonwealth account with the same client's account today,
         or see that the match is not yet known
         DONE WHEN  EXERCISED -- the match list read for every account in the delivery
         ACCEPT     for each Commonwealth account, a person sees the matching current Cottonwood account,
                    or a plain statement that it is not yet matched, and why
         SOURCE     brief O8
```

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-SOURCE: Commonwealth is a registered source | the naming registry's owner (`4.0.0_SA_CRO`, lane `PLATFORM_LOGIC_DOCS`) | One VENDOR row, key `commonwealth`, display name "Commonwealth Financial Network", owner D8 (Andrew: "COmmonwealth is a source"). MEASURED at L4: the builder refuses `address('commonwealth', ...)` today. No address in this project is typed by hand: each is builder output printed in the order that writes it, after the row lands. |
| C-HOMES: where each layer lives | the canon (`infra/logic/02_DOCTRINE.md` R4, R9, R10); Andrew's order | Bronze and silver of client custodial data have ONE home, `opal-data-assets`, key grammar `{source}/{scope}/{tier}/{table}/{partition}` (the builder reads `address('blackdiamond','cottonwood','bronze','crm','date=2026-06-23')` -> `s3://opal-data-assets/blackdiamond/cottonwood/bronze/crm/date=2026-06-23` at L4; the `commonwealth` form follows the row). Scope is the firm, `cottonwood`; Commonwealth's advisor plan IDs and rep codes are entity identifiers and sit in the partition, never the scope (R2). |
| C-RAW: the delivery kept as received (FWD-2) | this project | The five delivered zips are written once, byte for byte, never unpacked in bronze (R9). A manifest beside them carries each file's name as shipped, size and SHA-256, and both dates: the data's date and the received date. |
| C-DATE: which date labels the delivery | Andrew's call 2, "Yes agreed" | The partition date is the vendor's stamp, `date=2026-06-23`; the received date (2026-10-06) is in the manifest. |
| C-SENSITIVE: the most sensitive details (FWD-7) | Andrew's call 1, "Agreed", and his "maybe" on the bucket | Tax IDs, dates of birth, driver's license and passport numbers exist ONLY in the raw delivered files. The silver tables carry each person without those four fields; a date of birth becomes the birth year. This departs from R10's every-column rule and is declared as an R20 register entry for Andrew's acknowledgement. **Placement of the raw files that carry those fields** (the CRM zip, which holds contacts and insurance): Andrew's thought is that they "maybe" stay in `opal-data-cottonwood` rather than `opal-data-assets`. This PRD proposes exactly that, as a second R20 departure: the CRM zip is written to the Cottonwood firm bucket under a prefix readable by a small named group only; the other four zips go to `opal-data-assets` per C-HOMES. Both departures wait for his acknowledgement before any byte of the CRM zip is written; the other zips do not wait. |
| C-SILVER: typed tables (FWD-1, 3, 4) | this project | One typed, de-duplicated parquet table per delivered data file: transactions, performance, positions, and one per CRM file; every vendor column kept except C-SENSITIVE's four; hive partitions; each row carries the file it came from. |
| C-DOCUMENTS: one index, unique documents (FWD-5) | Andrew's call 3, "Agreed" | The 51 listing files become one de-duplicated document index (account, type, date, page count, source archive or archives). Each UNIQUE document is unpacked once into a declared documents table; the three archives also stay whole in bronze. |
| C-COVERAGE: what the backfill covers (FWD-6) | this project | One coverage table, generated from the data itself: for each record kind, its earliest and latest date and its row count. The brief's measurements (F5) are the expectation, not the source. |
| C-CROSSWALK: old account to current account (FWD-8) | this project | A first crosswalk from Commonwealth account to current Cottonwood account; every Commonwealth account is either matched, with the rule that matched it, or listed as not yet matched with the reason. No match is guessed. |
| C-FIRM | law (CLAUDE.md section 5) | Every key is under the `cottonwood` scope; no other firm's data is read or written; `.tools/ds-precommit-check.py`'s cross-firm guard grades the scripts. |
| C-ONE-TIME | law (no shadow pipeline) | A one-time backfill beside the current Cottonwood feeds, never duplicating them. A later Commonwealth delivery lands beside this one under its own date partition, renaming nothing. |
| C-MORATORIUM | law | No alert or monitor. |
| C-SCOPE-OUT | brief PART II | No gold, nothing on a page, no client release, no further pull from Commonwealth or Box. Which product reads this history is a later decision. |

## 1. The arc

**Start.** A 3.2 GB Box download in Andrew's Downloads folder, the only copy Opal has. **End.** The delivery is in Opal's store as
received; its history is typed and readable back to 2013; its documents are findable one by one; the most sensitive details are
where Andrew put them; the coverage is stated; old accounts are matched to current ones or plainly marked.

## 2. THREAD -- FWD-1, round 1

1. The Commonwealth registry row lands (C-SOURCE); the builder prints every bronze and silver address this round writes.
2. The transactions zip and the performance zip are uploaded from Andrew's Downloads to bronze, with the manifest (C-RAW, C-DATE).
3. The transactions file becomes the silver transactions table (C-SILVER).
4. An analyst picks one account, reads its history 2013 to 2026, and traces one row to its file.

Round 1 does not touch the CRM zip (it waits for Andrew's acknowledgement of C-SENSITIVE) or the imaging archives.

## 3. ENRICHMENT BACKLOG (ordered)

1. Performance to silver (FWD-3); positions to silver.
2. The coverage table (FWD-6).
3. On Andrew's acknowledgement of C-SENSITIVE: the CRM zip to its home, CRM tables to silver without the four fields (FWD-4, FWD-7).
4. The imaging archives to bronze; the document index; unique documents unpacked (FWD-5).
5. The account crosswalk (FWD-8).

## 4. WORKSTREAMS AND OWNERS

- One workstream; its COO lane is UNSEATED; seating is `0.0.0_AB_MSTR`'s on Andrew's word.
- Silver scripts are DS-lane work under rule 13 (commit to QA deploy); uploads to S3 are writes into a new prefix, under a ledger entry.
- The registry row is `4.0.0_SA_CRO`'s (lane `PLATFORM_LOGIC_DOCS`).
- Andrew's Downloads copy is the input; its fate after landing is his.

## 5. Rulings closed at L4

1. One home for bronze and silver, `opal-data-assets`, except the CRM zip, proposed for the Cottonwood firm bucket (C-SENSITIVE).
2. The vendor's date labels the delivery.
3. Sensitive fields: raw files only; silver without them; birth year kept.
4. Documents unpacked once, de-duplicated; archives kept whole.
5. Nothing is typed as an address; all is builder output after the row lands.

## 6. SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | verb | depends_on | bound |
|---|---|---|---|---|---|---|
| S01 | all | the `commonwealth` VENDOR row in `infra/logic/registry/systems.json` | measured (builder refuses today) | wire | -- | the registry's owner lands it |
| S02 | FWD-2 | bronze: the five zips and the manifest (sizes, SHA-256, both dates) | held (brief F1) | wire | S01 | byte for byte |
| S03 | FWD-1 | silver transactions (1,416,497 rows, 20 columns, per the brief) | held | wire | S02 | every column, row lineage |
| S04 | FWD-3 | silver performance (88,654 rows) and positions (469) | held | wire | S02 | as reported |
| S05 | FWD-4, FWD-7 | the CRM zip's home and the CRM silver tables without the four fields | held (brief F3, F6) | wire | S01, Andrew's acknowledgement | R20 entries first |
| S06 | FWD-5 | the document index and the unique documents | held (brief F4) | wire | S02 | de-duplicated |
| S07 | FWD-6 | the coverage table | unmeasured | wire | S03-S06 | generated from the data |
| S08 | FWD-8 | the account crosswalk | unmeasured | wire | S03 | no guessed match |

## 7. BRIEF COVERAGE

| Brief heading | Carried | Consuming sections |
|---|---|---|
| PART I, thread and O1-O8 | the thread; eight outcomes | ENDPOINT; section 2 |
| PART II, boundary | owns landing, silver, index, registry row, coverage, crosswalk; relies on the canon, the Cottonwood pipelines, MDPF_SECCLASS; no gold | C-SCOPE-OUT; section 4 |
| PART III, bar | answered from the store; history without a spreadsheet; no stray sensitive field; spans not confused; a later delivery lands beside | FWD-2, FWD-1, FWD-7, FWD-6, C-ONE-TIME |
| PART IV, F1-F7 | five zips; the history files; the CRM; the archives and their duplication; coverage; sensitive fields; the canon's homes | C-RAW, C-SILVER, C-DOCUMENTS, C-COVERAGE, C-SENSITIVE, C-HOMES |
| PART V, must be true | the registry row; Andrew's word on sensitive fields; the date; where PDFs live; cross-firm guard; no shadow; the Downloads copy | C-SOURCE, C-SENSITIVE, C-DATE, C-DOCUMENTS, C-FIRM, C-ONE-TIME, section 4 |

-- 1.0.0_SA_CTO
