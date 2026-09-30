# AMGT_HARVST -- ROUND 23 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~02:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26848, subject *"L10 slug AMGT_HARVST round 23 @13c22d9e18"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v32.md`. Issuer packet:
`deliverables/2.0.0_SA_COO_H/round23/ROUND23_DRAIN_END_PACKET.md` @`825e15`.

**Round 23 is CLOSED. The project is NOT closed.** This analysis grades the seven FWDs left ungraded since round 10
(round-22 ruling 3). Each grade reads a DONE WHEN from `prd/AMGT_HARVST_PRD.md` against the round's measurement.

---

## 1. THE GRADES

| FWD | grade | the measurement it rests on | the gap, in the DONE WHEN's own words |
|---|---|---|---|
| **1** re-readable as sent | **NOT REALIZED** | bronze sha256 matches 126 of 126, but **104 of 126 are `normalised_record` rebuilds**; listing pages are stored for wsj 2 and sa 2; 0 of 120 articles link their listing object | "re-opened ... and matches what was received, byte for byte": what was received is not stored for 104; "and the listing page that found it": linked for 0 |
| **2** every sent field kept | **NOT REALIZED** | missing fields: sa 5/46, others 0; **6 sa bronze articles have no silver row**; the company-and-date query works (Lenovo 09-23: 14 rows) | "every field present ... appears typed": sa 5 fields and 6 rows. See ruling 2 on "by company". |
| **3** how found | **NOT REALIZED** | kind and words present; **rank and page only for sa (5) and wsj (11)**; duplicate keys 0/120; no run records exist | "its position in the results": missing for barrons, bbg and ft; "a second run the same day fetches no article we already hold": unexercised |
| **4** strength per pair | **REALIZED** | 6 of 6 carriers on **304/304** pairs; the grade re-derived from stored silver text matches 304/304; a negative control mismatches 52; 0 silver pairs missing from gold | met on every clause, on the whole served population |
| **7** rank by strength | **NOT REALIZED** | the live producer `amgt-resapp-chatter-axis` reads `CHATTER_AXIS_SOURCE=legacy` (the CVO's `get-function-configuration`; tf `chatter-axis-schedule.tf:70`), so raw counts drive the rank; raw vs graded correlate 0.83 over 36, and 6 companies rank 5 or more places higher on raw; **the served rank list holds 2 rows** | "computed from the graded daily table": it is not |
| **8** undelivered reach the store | **REALIZED** | the desktop inventory `progress.sqlite3` holds 120 bodies and 121 links: **120/120 bodies in bronze and silver, 121/121 links in silver, 0 duplicates** | met. The DONE WHEN's denominator IS the desktop's holding, so an off-store inventory (`Z-W55-S1`) is the right instrument, not a defect. The 241 `pending` outbox rows are not a delivery signal (packet). |
| **9** history since 01-01 | **NOT REALIZED** | of 191 covered names, 11 reach the floor, 54 start after it, **126 have no article**; a pre-run plan exists for Lenovo only; the daily series is dense by construction | "for each security ... the backfill has run from 2026-01-01", and "printed before the run": neither holds beyond Lenovo |

**Tally: 2 of 9 REALIZED (FWD-4, FWD-8).** FWD-5 and FWD-6 are graded at DSGN_AMGTV1 round 8's re-walk.

## 2. RULINGS

1. **FWD-1: stored rebuilds are not the publisher's bytes, and past originals are not recoverable. The fix is going forward.**
   - The collector stores each response body AS RECEIVED, beside its rebuild, and links every article to the listing
     object that found it.
   - The DONE WHEN's "one run on the validation security" is then exercised on the next live collection.
   - The 104 existing rebuilds stay, labelled for what they are. No re-fetch is cut to replace them.
2. **FWD-2's "query by company" is a query over the MENTION JOIN (gold's alias-matched mentions), not over silver's
   `discovered_for`.**
   - `discovered_for` means "found while searching for" (`Z-W53-S4`: sa rows tagged 992 HK carry AES and Barrick titles).
     It stays as FWD-3's provenance carrier, which is its true meaning.
   - The query that answers "by company" is the silver-to-mention join. That is a query definition, not a build, and cell 2
     proves it.
3. **FWD-3's "a second run the same day fetches no article we already hold" is exercised with a COUNTING stub transport,**
   not a live re-run. The run writes a run record, the second run's fetch count for held keys must read 0, and a planted
   new key must read 1.
4. **FWD-7: the source flips from `legacy` to `gold` under a never-widen pair, AFTER the expected diff is measured.**
   - This is an applied-plane change to a scheduled producer, one variable, through `safe-apply`.
   - First, the served rank's **2 rows** are explained. A rank list of 2 cannot show "a company named once in passing ...
     no longer outranks". If the list is short because of the window or its filter, the grading population is set before
     the flip.
   - The flip's pair then names the expected rank moves, read from the producer's `gold` branch at signing.
5. **FWD-9: the backfill plan is printed for EVERY covered name before any run.** That is pages per publisher per name, from
   the listing sizes the collector already knows, with no vendor call. The run itself is a vendor act under R-21's scripted
   grant, and Seeking Alpha's leg waits on the renewal (section 5).
6. **The 6 sa bronze objects with no silver row (`Z-W53-S3`) are FWD-2's.** They are in cell 2.

## 3. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 24 in ONE issuance

| # | cell | outcome | risk | note |
|---|---|---|---|---|
| 1 | **The collector keeps the received bytes and links the listing object; rank and page for every publisher; a run record** | FWD-1, FWD-3 | LOCAL | Rulings 1 and 3. The counting stub proves held keys fetch 0 and a planted new key fetches 1. Recorded fixtures stand in for publishers; no vendor call. |
| 2 | **sa's 5 missing fields and the 6 missing rows in silver; the company query over the mention join** | FWD-2 | LOCAL, then a silver rebuild under a pair if it moves served rows | Rulings 2 and 6. The query prints, for Lenovo 09-23, rows by mention against rows by `discovered_for`, with the AES and Barrick rows falling out. |
| 3 | **Why the served rank holds 2 rows, and the `gold` rank's expected diff** | FWD-7 | LOCAL read | Ruling 4. Prints the served list's population rule and the `legacy`-vs-`gold` rank on the same window, with a denominator. |
| 4 | **The `CHATTER_AXIS_SOURCE=gold` flip** | FWD-7 | WORLD, under a pair and a NEVER-2 entry | It depends on cell 3. The expected diff comes from cell 3, and the rollback is the variable back to `legacy`. |
| 5 | **The backfill plan for all 191 covered names** | FWD-9 | LOCAL | Ruling 5. It prints pages per publisher per name and the total, before any run. |
| 6 | **`/timeline/day`: profile, then fix** | FWD-5 (latency) | LOCAL profile; the fix under a pair | Routed from DSGN_AMGTV1 round 7 ruling 2: about 5.5 s for a day with articles, warm. |

**Fan-out:** 5 now (cells 1, 2, 3, 5 and 6). Cell 4 follows cell 3.

**NOT cells:**
- re-fetching the 104 rebuilt originals (ruling 1);
- the backfill run itself, until cell 5's plan is read;
- events.

## 4. WHAT CHANGED IN THE GRADE BOOK

- This project read "0 of 9" from round 12 onward without measuring seven of the nine. **Two were already met** (FWD-4 and
  FWD-8), and the five others have NAMED gaps.
- The next analysis grades against these rows, not "as round N left them".

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Renew Seeking Alpha [spend]. His word is given (@d0e74747a9). FWD-1's five-publisher run and FWD-9's sa leg need the account
  to read 200.
- Remove the drained worktrees `wk-hvst-r23-53/54/55` and those listed earlier [recursive delete, CLAUDE.md Agent Autonomy].

## Compiler Tools

- The CVO's v32: its `get-function-configuration amgt-resapp-chatter-axis` read, the tf and lambda source lines, and its reading
  of the `Z-W53-S4` rows.
- The packet's section-2 table (seven measurements, a close run of 7 of 7 scripts at rc 0).
- The PRD's FWD-1..9 DONE WHEN lines, read at `:84`-`:175`.
