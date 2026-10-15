# ADVI_COTBKF -- the Cottonwood 10-year backfill from Commonwealth

```json
{
 "project": "ADVI_COTBKF",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.10",
 "step": 4,
 "brief_ref": "docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md@902feb3a4f",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-06. **Priority:** Andrew's word.
**Brief:** `docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md` @902feb3a4f (`4.0.0_SA_CRO`).
**Andrew's words:** the order, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_16xxZ_COTTONWOOD_COMMONWEALTH_10Y_BACKFILL_SPEC.md`
("Disregard MSTR instruction on using a cottonwood specific bucket. We will use the opal-data-asset format"); the three calls,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_172xZ_COTTONWOOD_BACKFILL_THREE_CALLS_SENSITIVE_IN_FIRM_BUCKET.md`.
**Status RATIFIED (v0.3):** Andrew, "All agreed but we need daily granularity when it comes to FWD 3" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_174xZ_COTTONWOOD_BACKFILL_ALL_AGREED_FWD3_DAILY.md`). FWD-3 amended in
place to daily; both R20 departures acknowledged; the restricted prefix's readers named.
**Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO wrote the brief.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An analyst picks one Cottonwood account and reads its whole transaction history, as far back
         as Commonwealth recorded it, from Opal's own store, and can trace each row to the file
         Commonwealth sent
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

  FWD-3  An analyst reads each Cottonwood account's returns day by day, after fees, back to 2013
         DONE WHEN  EXERCISED -- one account's daily returns read across the whole span, and checked
                    against the monthly figures Commonwealth reported
         ACCEPT     for any Cottonwood account in the delivery, an analyst reads its return for any single
                    day from 2013 to June 2026; strung together over a month, the days give the same
                    return Commonwealth reported for that month, or the difference is shown with its
                    reason; a day that cannot be worked out says so and is never filled in; Commonwealth's
                    own monthly, yearly and since-inception returns, with its benchmark, are readable beside
                    them as reported
         SOURCE     brief O3; Andrew, "we need daily granularity when it comes to FWD 3"

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

  FWD-9  A client's history follows them when Commonwealth moved them to a new account number
         DONE WHEN  EXERCISED -- one client read across an account change inside Commonwealth, oldest
                    account to newest
         ACCEPT     where a client's account was replaced by a new one inside Commonwealth, an analyst
                    reads the client's history as one line from the oldest account to the newest, and
                    sees which account each row came from; a link that cannot be shown is listed with
                    its reason, never guessed
         SOURCE     round 1 finding, row ADVI_COTBKF-S2: no single account spans 2013 to 2026; every 2013
                    account ends by 2017-12
```

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-SOURCE: Commonwealth is a registered source | the naming registry's owner (`4.0.0_SA_CRO`, lane `PLATFORM_LOGIC_DOCS`) | One VENDOR row, key `commonwealth`, display name "Commonwealth Financial Network", owner D8 (Andrew: "COmmonwealth is a source"). The row LANDED @8e39143feb (the registry's owner); builder output read at L4: `address('commonwealth','cottonwood','bronze','crm','date=2026-06-23')` -> `s3://opal-data-assets/commonwealth/cottonwood/bronze/crm/date=2026-06-23`. Every address in this project is builder output printed in the order that writes it, with ONE declared exception: the CRM zip's home in the firm bucket (C-SENSITIVE), for which `address()` has no route. That key is written once, in the R20 register entry Andrew acknowledges, and nowhere else is typed. |
| C-HOMES: where each layer lives | the canon (`infra/logic/02_DOCTRINE.md` R4, R9, R10); Andrew's order | Bronze and silver of client custodial data have ONE home, `opal-data-assets`, key grammar `{source}/{scope}/{tier}/{table}/{partition}` (the builder reads `address('blackdiamond','cottonwood','bronze','crm','date=2026-06-23')` -> `s3://opal-data-assets/blackdiamond/cottonwood/bronze/crm/date=2026-06-23` at L4; the `commonwealth` form follows the row). Scope is the firm, `cottonwood`; Commonwealth's advisor plan IDs and rep codes are entity identifiers and sit in the partition, never the scope (R2). |
| C-RAW: the delivery kept as received (FWD-2) | this project | The five delivered zips are written once, byte for byte, never unpacked in bronze (R9). A manifest beside them carries each file's name as shipped, size and SHA-256, and both dates: the data's date and the received date. |
| C-DATE: which date labels the delivery | Andrew's call 2, "Yes agreed" | The partition date is the vendor's stamp, `date=2026-06-23`; the received date (2026-10-06) is in the manifest. |
| C-SENSITIVE: the most sensitive details (FWD-7) | Andrew's call 1, "Agreed", and his "maybe" on the bucket | Tax IDs, dates of birth, driver's license and passport numbers exist ONLY in the raw delivered files. The silver tables carry each person without those four fields; a date of birth becomes the birth year. This departs from R10's every-column rule and is declared as an R20 register entry for Andrew's acknowledgement. **Placement of the raw files that carry those fields** (the CRM zip, which holds contacts and insurance): Andrew's thought is that they "maybe" stay in `opal-data-cottonwood` rather than `opal-data-assets`. This PRD proposes exactly that, as a second R20 departure: the CRM zip is written to the Cottonwood firm bucket under a prefix readable by a small named group only; the other four zips go to `opal-data-assets` per C-HOMES. Both departures ACKNOWLEDGED by Andrew ("All agreed", record 174xZ); no byte of the CRM zip is written before C-RESTRICTED's policy is live. |
| C-RESTRICTED: the firm-bucket prefix for the CRM zip (FWD-7) | the bucket's Terraform owner (`infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`, lane `CLOUD_OPS_OR_ETL`, an AE seat); Andrew names the readers | ONE prefix in `opal-data-cottonwood`, its key fixed in the R20 entry. Its bucket policy DENIES every read to every principal except the named group, and denies every write except the one landing role, once. The named group, by Andrew's word ("All agreed"): Andrew alone, plus a break-glass role used only on his word; no agent seat is in it. The policy is a Terraform change in that file, applied by its owner under a never-widen pair, and proven by one refused read from an agent's identity and one allowed read by the group. Nothing is written to the prefix before the policy is live. |
| C-DAILY: daily returns are derived, not delivered (FWD-3) | this project; Andrew's word for any outside price vendor | MEASURED by the brief (F2): the performance file holds Month, Year and Inception-to-date rows only. Daily returns are built: (1) daily holdings per account rebuilt from the transactions, each account's opening state from its own history (positions exist for one day only, 2026-06-23, 83 of 1,533 accounts); (2) each holding valued daily with a closing price; (3) a daily after-fee time-weighted return with the day's flows taken out; (4) the days chained per month and compared with Commonwealth's monthly return, each month graded MATCH within a stated tolerance or DIFF with its reason. Price history is read from Opal's existing stores first (build ladder rung 2), with the coverage of those stores over these securities printed; a security no Opal store prices leaves its days UNPRICED, and any outside price vendor (Bloomberg, Yahoo Finance or other) waits for Andrew's per-use word. A day not computable is UNKNOWN, never interpolated. |
| C-SILVER: typed tables (FWD-1, 3, 4) | this project | One typed parquet table per delivered data file, holding EVERY row of the file: two identical lines are two rows, each carrying its source line number; "de-duplicated" means only that re-landing the same delivery adds nothing. Row count equals the file's record count (a quoted field may span lines), printed beside it; transactions, performance, positions, and one per CRM file; every vendor column kept except C-SENSITIVE's four; hive partitions; each row carries the file it came from. |
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

1. Performance and positions to silver (Commonwealth's own figures); then the daily return build (C-DAILY), its price-coverage read first.
2. The coverage table (FWD-6).
3. On Andrew's acknowledgement of C-SENSITIVE: the CRM zip to its home, CRM tables to silver without the four fields (FWD-4, FWD-7).
4. The imaging archives to bronze; the document index; unique documents unpacked (FWD-5).
5. The account crosswalk (FWD-8).

## 4. WORKSTREAMS AND OWNERS

- One workstream; COO lane `2.0.0_SA_COO~C` (this seat's reading of Andrew's "All agreed"; seating is `0.0.0_AB_MSTR`'s).
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
| S10 | FWD-3 | the daily return build: daily holdings, daily valuation, daily after-fee return, the monthly MATCH/DIFF grade | unmeasured (price coverage unread) | build | S03, S04 | no interpolated day |
| S05 | FWD-4, FWD-7 | the CRM zip's home and the CRM silver tables without the four fields | held (brief F3, F6) | wire | S01, S09, Andrew's acknowledgement | R20 entries first |
| S09 | FWD-7 | the restricted prefix's bucket policy in `s3-lgic-firm-buckets.tf` | unmeasured | wire | Andrew names the group | live before any write |
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

## v0.2 (1.0.0_SA_CTO, 2026-10-06) -- CONTRACTS fixes on `3.0.0_SA_CVO`'s review @35572399b9

C-SOURCE: the row has landed (the stale "builder refuses" line replaced) and the CRM zip's firm-bucket key is the one declared exception, written only in the R20 entry. C-RESTRICTED added: the prefix's owner, its deny-by-default policy, Andrew naming the readers. Manifest S09. The ENDPOINT is not edited.

## v0.3 (1.0.0_SA_CTO, 2026-10-06) -- RATIFIED on Andrew's "All agreed"; FWD-3 amended to daily

FWD-3 amended in place (id unchanged; outcome was right and its grain too coarse, Andrew's word). C-DAILY added; manifest S10. C-SENSITIVE and C-RESTRICTED carry his acknowledgement and the named readers. The ENDPOINT changed, so the ratified-text half re-opens for `3.0.0_SA_CVO`.

## v0.4 ADDENDUM (1.0.0_SA_CTO, 2026-10-06, L10 of round 1) -- two rulings from this seat's own read of the WORLD cells

**Read by this seat (not the producer's report):** the landed ClientDelivery zip's SHA-256 is
`a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b`, equal to the manifest AND to the same member read directly
from Andrew's `Files.zip` (FWD-2 bronze: PASS). The transactions file holds 1,416,497 records (1,416,500 physical lines: three records of one account carry a line break inside
a quoted note, row ADVI_COTBKF-S3, recounted by this seat as records); silver holds 1,415,137 rows = 1,416,497 less 1,360
record-level repeats. Nothing else is unexplained.

1. **C-SILVER clarified: every delivered row is kept.** Without a transaction id, two identical lines may be two real events (two
   equal reinvestments on one day); dropping them changes flows and every daily return built on them (FWD-3). The word
   "de-duplicated" was this seat's and is now bounded to re-landing. Silver transactions is rebuilt with all 1,416,497 records and the
   source record number on each (corrected from "1,416,500 rows" on row S3: lines, not records).
2. **FWD-1 amended in place and FWD-9 added** on row S2: no single account spans 2013 to 2026, so FWD-1 reads "as far back as
   Commonwealth recorded it"; following a client across a Commonwealth account change is FWD-9 (next unused id).

Ruled under the self-adjudication order (`ANDREW_DIRECT_20260903_052xZ_..._TWO_READS.md`). The ENDPOINT changed: the ratified-text
half re-opens for `3.0.0_SA_CVO`.

## v0.4 ADDENDUM 2 (1.0.0_SA_CTO, 2026-10-07 ~01:3xZ) -- the price source for C-DAILY, Andrew's word

Measured by `2.0.0_SA_COO~C` (`deliverables/0.9.0_WK_ADVI_COTBKF~8/PRICE_NEED_20261007.json` @c907766ef4): 4,634 securities, 3,421,735
security-days (equity 1,453,884; ETF 331,153; fund 752,921; fixed income 688,679; other 195,098). Opal's own stores cannot serve them
(other firms' buckets; no fixed income). Andrew at this terminal, VERBATIM: "i like the yahoo finance vs bloomberg rec". C-DAILY's price
source is therefore: **Yahoo Finance for equity, ETF and fund securities; Bloomberg at site Z for fixed income and other**, the Bloomberg
leg drawing on `bbg_budget.py` behind the production reserve. Prices land once per security in the securities history MDPF_SECHIST
owns (C-SERIES), never in another firm's bucket. A security neither source prices leaves its days UNPRICED. Contracts only; the
ENDPOINT is unchanged.

## ADDENDUM v0.5 -- a withholding is an outflow; the re-mint uses the served instant's pin (L10; CONTRACTS changed: the ratified-text half re-opens)

- **Source:** this seat's round-65 analysis @1e9128413f section 3 item 3 (Class D), its round-68 analysis @b3a272fffc, and `3.0.0_SA_CVO`'s
  slug for round 68, `surprise-channel/remediations/REMEDIATION_v39.md` @22e2566c22, item 1, re-derived by that seat's own diff. The ENDPOINT
  is unchanged.
- **The method.** A tax withholding taken from an account is an external outflow on its date, whether or not the source carries a
  withdrawal row beside it. The form in use until now (`method_r28`) counted it only when a withdrawal row existed; that was a defect of
  the form, and it read the withholding as a loss. `method_r29`, which counts it, is the default from this addendum.
- **What it changes in the served table: 2 day files, and no other.** Measured at the served instant's pin, where the control between the
  two methods is exact with inputs held equal. The list is the one in the round-68 packet; a re-mint that would replace any other file is
  not this addendum's and is a STOP.
- **The re-mint uses the served instant's pin, not today's store.** Today's store has grown by four spin-off entries that move 30 further
  day files; none of the four has a date on which its factor can be checked (row D2-W103-S1), so none is applied. Using the served pin
  keeps them out by construction. They enter the store's effect only by a later addendum, per event, with its evidence.
- **Stated, not hidden:** 41 withholding days are blank under both methods for want of a price. If priced later they will read under
  `method_r29`. That is a future change to the served table and comes under its own pair when it happens.
- **The re-mint itself** is a move of served output: its own pair, naming the 2 day files, the pin, both branches and every reader of the
  served table with one read through each.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.6 -- ADDENDUM v0.5's method sentence, narrowed to what the method does (L10; CONTRACTS changed: the ratified-text half re-opens)

- **Source:** `3.0.0_SA_CVO`'s refusal of the v0.5 ratified-text half,
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_PRD_v0.5_RATIFIED_TEXT_REVIEW_20261011.md` @41c87025f4. Accepted. v0.5's sentence was
  written by this seat without reading the method; the lines below were read by this seat before this addendum
  (`data/assets/scripts/silver/commonwealth_flows.py` lines 105 to 111, 160, 176 to 196, 234 and 250).
- **v0.5's first bullet ("The method") is REPLACED by this:**
  - `method_r29` is `method_r28` plus one rule: **a FEDERAL or STATE tax withholding row (types `ftax`, `stax`) on the account's CASH LINE
    is an external outflow on its date, with or without a same-day cash withdrawal.** Under `method_r28` such a row was an outflow only
    when it rode a same-day withdrawal; alone, it stayed inside the return as a cost.
  - **FOREIGN tax (`frntax`) is NOT covered and stays inside the return, as it does today:** it is withheld at source out of the holding's
    own income, on the security's line, so the income the account books is already net of it.
  - A withholding row that is not on the cash line is not covered by the rule.
- **A later seat does not "conform" the code to a wider reading.** The method is the code at those lines; this text describes it. Moving
  foreign tax to a flow would be a different method, with its own number, its own comparison at a pin and its own addendum.
- v0.5's other bullets stand as written: 2 day files and no other; the served instant's pin; the 41 blank withholding days; the re-mint
  under its own pair.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.7 -- the re-mint's true extent, and that it is NOT made now (L10; CONTRACTS changed: the ratified-text half re-opens)

- **Source:** `2.0.0_SA_COO~C2`'s drain-end record for round 69,
  `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_69_DRAIN_END_20261011.md` @f689ae32cc, section 1, read whole by this seat; not re-run. The
  issuer met v0.5's own STOP and wrote no half. That was the addendum working. The ENDPOINT is unchanged.
- **v0.5's sentence "What it changes in the served table: 2 day files, and no other" is WITHDRAWN. It was wrong.** It counted the days whose
  RETURN moves. The served day file also carries `external_flow` on blank rows, and `method_r29` moves that cell too. As the record
  measures it: the return moves on 2 account-days (2014-12-03 and 2020-11-13); `external_flow` moves on 44 day-file rows over 43 dates (the
  worker's count; the issuer's own count on the silver table is 47 rows over 46 dates, and the 3-row difference is attributed, not
  reconciled). So a re-mint under `method_r29` replaces **43 day files**, by the worker's count.
- **And it is not only day files.** The adapter builds only from the SERVED silver tables, so three silver objects are re-served first,
  which changes `run_commit` and `cash_leg` on every row of all three (1,691,729, 21,102,041 and 82,593 rows). No code path re-mints an
  existing day file today. The served build also used a hold list of three CUSIPs that the round-68 comparison did not.
- **Ruled: the re-mint is NOT made now.** It would re-serve some 23 million silver rows and build a new write path to correct 2 returns
  and 42 cells of a blank row, in a table no released reader consumes: the readers found are the adapter's own verify and build and the
  serve script's verify. Further corrections to this same table are already open (the 41 unpriced withholding days, the one close series
  about 6.6 times low and the scan for others, the four spin-off entries, the rule for a receipt after an account's assets left). **One
  re-serve carries all of them, once, when that list is closed.** Each time the table is re-served for one item, every row's `run_commit`
  moves again.
- **`method_r29` stays the default for the next build**, as v0.6 states it. Until that build the served table is `method_r28`'s, and it
  carries a KNOWN, STATED defect: on 2 account-days a federal or state withholding sits inside the return. They are named above.
- **What un-parks it, whichever comes first:** the correction list closes; or a reader of this table is to be released. No reader of the
  Cottonwood return history is released on the `method_r28` table: the re-serve comes first, under its own pair, naming all three silver
  objects, every day file it replaces, the hold list, the pin and every reader.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.8 -- the price basis for fund securities, and where it may come from (L10; CONTRACTS changed: the ratified-text half re-opens)

- **Author:** `1.0.0_SA_CTO~DELL2`, 2026-10-12 ~01:5xZ. This is also the ROUND-79 ANALYSIS. **Sources:** the reviewer's slug
  `surprise-channel/remediations/REMEDIATION_v47.md` @77527824fd (msg 6272), read whole; the issuer's drain end
  `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_78_DRAIN_END_20261012.md` @7af967bc1b, its section 2 read; this PRD's v0.4
  ADDENDUM 2 read at its lines. Every number is the worker's, the issuer's or the reviewer's. This seat measured nothing.
- **What is established.** The price store has ONE price column. For the 15 funds it is not the unadjusted close (equal on 3.2 to
  10.2 percent of dates), and by year its median runs from 0.46 of the traded price in 2020 to 1.00 in 2026. That it is a
  dividend-adjusted series from an earlier pull is INFERRED; no field says so. The unadjusted close exists for every one of the
  20,718 held trading days of the 15 funds, in a vendor cache that is a folder on one box and that no build reads.

**CONTRACT C-BASIS.**

1. **A fund security is priced at its AS-TRADED close: the unadjusted close of the day.** A distribution is carried by the
   project's own flow rows, never by the price. This is what reproduces the price paid on 14 of the 15 funds.
2. **The basis is a FIELD on every price the back-fill reads and on every row of the minted table that a price made.** Two values,
   a closed set over one axis (how the price treats distributions): `AS_TRADED` and `ADJUSTED`. A price whose basis is not stated is
   read as not stated and prices nothing; it is never assumed to be either. A reader of the minted table that needs one basis
   rejects the other on that field. One remedy (re-pricing from an as-traded source) moves `ADJUSTED` and not-stated; it does not
   move `AS_TRADED`.
3. **The source is the one v0.4 ADDENDUM 2 already names: the securities history that MDPF_SECHIST owns (C-SERIES), where "prices
   land once per security".** It is NOT the price store, and it is NOT the cache folder. The cache proves the values exist; it is
   not a landed, scheduled source and no build may read it. **No second lander is built for this project.** IRPT_BCKEND PRD v0.46
   answer 1 asks for landed unadjusted bars for its own grading; that is the same need and it is met by the same history, so the
   two projects do not each land prices.
4. **Until that history holds an as-traded close for a held fund day, that day is UNPRICED** (v0.4 ADDENDUM 2's own rule), and the
   minted table says so in the basis field. It is not priced from the store.
5. **The 15 funds' classing is re-derived after the re-pricing, from the price paid, and not from the flat-charge allowance.** The
   allowance fails its own bar; it could only excuse units, so it did not make a fund fail, but no class rests on it.

- **Row ADVI_COTBKF-D2-S131 stays BLOCKING** and its ruling stays in force: no rebuild of a holdings partition dated before
  2026-06-08 for this firm, no consumer attached to the minted table, until C-BASIS is built and its proof graded.
- **Rows D2-W149-S1 and D2-W149-S2, accepted, owner this seat.** S2 widens the question past the 15 funds: 308 of 4,000 tickers
  carry more than one asset name and the build reads by ticker. Item 2 of the list below sizes it for what this firm held.
- **The proof.** For the 15 funds, re-priced from the history: the trades that reproduce the price paid within the project's own
  tolerance, counted before and after, per fund; and one fund-day read from a price whose basis is `ADJUSTED` is refused by the
  minted table's reader. Graded by the reviewer.

**ENRICHMENT LIST for round 79 (reads; nothing built).**
1. MDPF_SECHIST as it stands: its owner and fabric, whether the securities history exists, its fields, whether it carries a basis,
   which of the 15 funds and which held days it covers. Counts and dates, the denominator printed. If it is another fabric's, the
   read is of the shared tree and its register row only, and the ask goes through 0.0.0_AB_MSTR~DELL2.
2. Of the securities this firm held, how many have a ticker carrying more than one asset name, and for each whether its held days
   are priced from its own rows. Counts only.
3. What wrote the live store object: which code, which run, whose (row D2-W149-S1), from the object's two retained versions and
   the tree's history.

**Acts only Andrew can do:** none.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.9 -- C-BASIS item 2 replaced: the basis field is the one the build already has (L10; CONTRACTS changed)

- **Author:** `1.0.0_SA_CTO~DELL2`, 2026-10-12 ~02:0xZ. **Source:** the reviewer's refusal of v0.8 (`3.0.0_SA_CVO` msg 6278, review
  @118f800793, read whole). **The refusal is right.** v0.8 item 2 minted two tokens, `AS_TRADED` and `ADJUSTED`, without a census,
  and this seat had not read the build it was writing a field for. Read since, by this seat:
  `data/assets/scripts/silver/commonwealth_daily_valuation.py:186-199`, `:211`, `:246-258`;
  `commonwealth_split_level_probe.py:1-5`. v0.8's items 1, 3, 4 and 5 stand. **Item 2 of v0.8 is WITHDRAWN and its two tokens are
  not used anywhere.**

**The census (native search, word boundary, case-insensitive, over `data/`; this seat, counts as printed).**
- `as_traded_close`: 71 occurrences in 26 files. 2 in this project's valuation build, where it is a VALUE of the per-point column
  `basis` (`:211`); 69 in 25 files under `data/mdpf/scripts/`, where it is a COLUMN of the securities history's own writers. One
  meaning in both: the close a security traded at.
- The constants `BASIS_AS_TRADED_CLOSE` and `BASIS_STORE_POINT`: 7 occurrences in 3 files, all this project's build and its tests.
- `price_basis` (the RUN-level option `store` or `as_traded`, and a member of `sources.json`): found in 18 files under `data/`. It
  is a different grain (one value per run or per source) and is not the field this contract writes.
- The reviewer's census is adopted for the rest: `AS_TRADED` upper-case is a served blank-reason token
  (`commonwealth_account_return_daily.py:523`); the four series classes `as_traded`, `dividend_adjusted`, `mixed`, `other` have 61
  occurrences in 15 files. Not searched by this seat: `infra/` beyond three candidate tokens (0 hits), `portal`, `docs`.

**C-BASIS item 2, as it now reads.**

2. **The basis of a price is the build's existing per-point column `basis`, with its existing closed two values, and it is carried
   onto every row of the minted table that a price made.** No token is added.
   - `as_traded_close`: the point is the vendor's `Close` for the day with this project's split scaling applied on top. The
     vendor's `Close` alone is split-ADJUSTED and not dividend-adjusted, so it is the price traded at only for a day with no later
     split; **the value means the traded price only AFTER the split scaling**, and a point that has not passed it is not written
     with this value.
   - `store`: the price store's point as it stands. What it does with distributions is NOT KNOWN for that point.
   - Four postulates. Domain: every price point the valuation reads; both values are assigned at one place (`:252`, `:258` on) and
     no third exists there. Same grain: one per point. One axis, one intent: where the point came from, which is what fixes what is
     known of its basis. State: re-pricing from an as-traded source moves `store` to `as_traded_close`; it does not move
     `as_traded_close`.
   - **For a fund security, a `store` point prices nothing:** the day is UNPRICED (item 4). A reader of the minted table that needs
     the traded price rejects `store` on this field.
3. **The four series classes are the census's and stay the census's: a class of a whole SERIES, never written to the minted
   table.** They stop deciding what is substituted for a fund. Today the as-traded basis replaces only series classed
   `dividend_adjusted` or `mixed` (`:190-191`); the 15 failing funds are classed `other`, so they kept their store points, and that
   is the mechanism of the defect. **Under C-BASIS every fund security is substituted whatever its class.** For other security
   types the classes keep their present use.

- **The proof gains one arm:** a fund that has split inside the back-fill, priced before and after its split, reproduces the price
  paid on both sides. If no held fund split, the run says so with the count searched.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.10 -- C-BASIS: what `as_traded_close` means against the split scaling, corrected on the read (L10; CONTRACTS changed)

- **Author:** `1.0.0_SA_CTO~DELL2`, 2026-10-12 ~02:4xZ. **Sources:** `2.0.0_SA_COO~C2` msg 6372 and its record
  `deliverables/0.9.0_WK_ADVI_COTBKF~152/BASIS_VALUE_AGAINST_SPLIT_SCALING.json` (merged 12a3c98e51), the lines read by the issuer;
  `1.0.0_SA_CTO~DELL1`'s ruling relayed in msg 6357 (its file @479d6deba0 on origin/box/dell1, read by the two issuers, not by this
  seat); the reviewer's note on v0.9 (msg 6284). This seat read no code for this addendum.
- **v0.9's sentence is WITHDRAWN:** "the value means the traded price only AFTER the split scaling, and a point that has not
  passed it is not written with this value." It described a build that does not exist. Measured: the value is written inside the
  substitution (`commonwealth_daily_valuation.py:271`, `:283`), the price input carrying it is written (`:976-978`) BEFORE the split
  plan runs (`:983-984`), the split step works on a frame with no basis column and records nothing per point, and a point can leave
  marked `as_traded_close` and unscaled on 9 of 11 paths. This seat asked for that read because it doubted its own sentence; the
  doubt was right.

**C-BASIS item 2, the meaning of the value, as it now reads.**

- `as_traded_close` on a point says WHERE THE POINT CAME FROM: an as-traded source. It does not by itself say the point is the
  price the security traded at. That holds only when the point is free of any later split's adjustment.
- **Under C-BASIS the one as-traded source for a fund is dell1's `as_traded_close` column** (v0.8 item 3; dell1's ruling: one lander,
  its demand queue). That column already has later splits undone. **So a point read from it IS the traded price, and this build's
  own split scaling is NOT applied to it:** applying it would scale the same split twice (row ADVI_COTBKF-D2-W151-S1).
- **The cached vendor Close is no longer a source for a fund point** (v0.8 already bars the cache as a source). On that path the
  value meant "the vendor's Close, split-adjusted, scaling applied afterwards and unrecorded"; no fund point is written from it
  under C-BASIS, so the value has one meaning in what C-BASIS mints.
- For security types this contract does not re-price, the value keeps the meaning the build gives it today, with the limit just
  measured: it does not record whether the split scaling reached the point. That is row material for those types and is not
  settled here.

- **The proof, replacing v0.9's split arm.** (a) A fund that split inside the back-fill, priced from dell1's column on a day
  before and a day after its split, reproduces the price paid on both, with this build's split step shown NOT to have touched
  those points (the count of fund points the split step changed is zero). (b) If no held fund split, the run says so with the
  count searched. Graded by the reviewer.
- **Round 79's list is unchanged.** The request file to dell1's queue is cut (msg 6361); nothing on dell2 fetches a price.

-- 1.0.0_SA_CTO~DELL2
