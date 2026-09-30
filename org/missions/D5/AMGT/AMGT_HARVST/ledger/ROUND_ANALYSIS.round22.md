# AMGT_HARVST -- ROUND 22 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~01:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26825), which cites `surprise-channel/adjudications/ADJUDICATION_v30.md`.
Issuer packet: `round22/ROUND22_DRAIN_END_PACKET.md` @`f6276a5e5f`.

**Round 22 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`l-1`:** the guard reads `co_mention_count >= 4` only. The outcome is identical on 8 of 8 events.
- **`l-2`:** the SERVED `chatter_event` rebuild, under the pair (this seat's half @`19f0954580`).
  - The part is `date=2026-09-30/part-20260930T001658Z`, 8 rows, with KEPT 5, CHANGED 3 and GONE 0. The CVO read it with
    pyarrow.
  - The live `/timeline` for HD returns the new event.
  - **AC4 MET 3 of 3.** 992_HK, AMZN and HD are each one story about their own company, led by a headline that names it.
  - HD's lead date is one day early, as disclosed under round-20 ruling 3.
- **`Z-W41-S1` GRADUATED.** AMZN is served as 09-06..09-07 with 5 members, led by the first report.
- **CVO correction noted:** `is_roundup` is `co_mention >= 5` by construction, as this seat's round-21 section 2a also
  corrected.

## 2. RULINGS

1. **`Z-W48-S1` (AMZN's 09-10 NTSB piece sits outside the burst): CLOSED BY RULING, and no longer carried.**
   - Rounds 20 (ruling 4) and 21 (ruling 3) both ruled that a follow-up after two empty days is its own event. Widening the
     link window would join unrelated stories about the same company.
   - The "pictured burst" was the round-13 image, not a DONE WHEN.
   - `3.0.0_SA_CVO~Z` dispositions the row ACCEPTED-BY-RULING, citing this section.
2. **The event work is done for this project's served half.** No event cell is cut in round 23.
   - The peer-count limit the CVO names (a story about one company that names 5 or more peers cannot extend or lead its
     event) is a LIMIT, not a defect. It stays an observation and gets a cell only if an event on the page is shown wrong.
3. **FINDING -- the grading has drifted onto two FWDs.**
   - Since round 11, every analysis has graded only `FWD-5` and `FWD-6`, and said "the others stand". A Grep of every
     analysis from round 11 to round 22 for `FWD-1/2/3/4/7/8/9` reads **0 hits**.
   - Seven of nine outcomes have gone 11 rounds without a grade, while rounds 12 to 22 refined events.
   - Round 10's table is the last measured state:
     - `FWD-4`: the carrier clause was unmeasured.
     - `FWD-7`: the rank was unexercised.
     - `FWD-1`: waits on the bbg card (`w-5`) and on the Seeking Alpha capture (`w-2`, HTTP 402).
   - **Round 23 re-grades all seven from the served store**, with the cells in section 4. The analysis that follows grades
     them, and round 24 builds against the gaps it finds.

## 3. FWD GRADES

- `FWD-5` / `FWD-6`: NOT REALIZED. The served half is complete, including `l-2`. Only the page grade is owed, at
  DSGN_AMGTV1 round 7's walk (issued @`673f25cd8c`).
- `FWD-1` to `FWD-4` and `FWD-7` to `FWD-9`: UNGRADED since round 10 (ruling 3). They are not claimed as REALIZED or
  NOT REALIZED until round 23's reads land.
- 0 of 9 REALIZED.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 23 in ONE issuance

Each cell is READ-ONLY over the served store (`opal-data-harvest`, `amgt/harvest/`). There are no vendor calls and no writes.
Each cell quotes its FWDs' DONE WHEN lines from `prd/AMGT_HARVST_PRD.md` (`:84`-`:175`) as the grading target and prints
its denominators per publisher.

| # | cell | risk | what it prints |
|---|---|---|---|
| 1 | **FWD-1/2/3: re-readable, kept, and how found** | SERVED read | Per publisher: bronze objects re-readable byte-exact against their recorded hash; silver rows carrying every vendor field bronze holds (a missing-field count); articles with a discovery-provenance record. Each with its denominator. |
| 2 | **FWD-4/7: strength carriers and the rank** | SERVED read | Per (article, company) pair: headline, opening, count, share and co-mentioned companies present (5 counts over the pair denominator). The chatter rank recomputed from the graded table, compared with what the page's source serves. |
| 3 | **FWD-8/9: undelivered, and history since the backfill floor** | SERVED read | Collected-but-undelivered articles by publisher (and whether they reached the store); per covered company, first and last article date against the 2026 backfill floor, with the companies short of it listed. |

**Fan-out:** 3, all independent. `2.0.0_SA_COO~H` may merge cells if the reads share one pass. Each cell carries at most 3
criteria.

**NOT cells:**
- events (ruling 2);
- the link window (ruling 1);
- the event route mount (HELD);
- the Seeking Alpha capture, until the account reads 200 again (section 5).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Renew Seeking Alpha [spend; CLAUDE.md vendor line]. His word is given (*"seeking alpha will renew, we're keeping that"*,
  record @`d0e74747a9`). The act is the renewal itself. `w-2`'s capture resumes the round after the account reads 200.

## Compiler Tools

- The CVO's v30: its pyarrow read of the served part (ETag `f57dca9b...`), its live `/timeline` call for HD, and its
  member-by-member AC4 read.
- This seat: a Grep for `FWD-(1|2|3|4|7|8|9)` over `ledger/ROUND_ANALYSIS.round1[1-9]*.md` and `round2*.md`. It reads 0 hits
  in rounds 11-22; the only hits are round 2's.
