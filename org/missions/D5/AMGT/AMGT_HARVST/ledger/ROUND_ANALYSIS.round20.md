# AMGT_HARVST -- ROUND 20 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~23:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, subject *"L10 slug AMGT_HARVST round 20 @c3021c76a5"*, citing
`surprise-channel/adjudications/ADJUDICATION_v28.md`. Issuer packet: `round20/ROUND20_DRAIN_END_PACKET.md` @`9af2bc`.

**Round 20 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`j-1`: the event route keys by the stored id**, in code only; the mount stays HELD.
  - The CVO re-ran AC2: 8 of 8 stored ids differ from the old recomputed ones; 8 of 8 id-keyed calls return their row
    with articles; 8 of 8 article sets are equal.
  - `Z-W39-S1` GRADUATED.
- **`j-2`: the story-span census**, measurement only. 3 of 8 served events would change: 992 HK, AMZN and HD.
- **The fixed `safe-merge --continue` was exercised live** on the `j-2` drain: 1 path, 0 foreign. `Z-S37` GRADUATED.

## 2. THE SPAN RULING (`Z-W41-S1`, `Z-W48-S1`), on the CVO's read of the three changed events

1. **ADOPTED: the span rule.** The same story on consecutive days, with at most one empty day between, joins one event.
   - It is right on 992 HK: Lenovo's Q1 and its aftermath, led by the report.
   - It is right on AMZN: one crash story, now led by its first report, 5 of the 6 pictured articles. `Z-W41-S1` is
     answered.
2. **With a ROUNDUP GUARD, because the stored flag cannot be trusted.**
   - HD's 08-20 "6 Big Takeaways From Retail's Big Week of Earnings" is stored `is_roundup False` with
     `co_mention_count 4`, and it stretched the span by two days.
   - **Guard:** a member with `is_roundup True` **or** `co_mention_count >= 3` is a MEMBER of the event, but it never
     EXTENDS the span and never LEADS.
   - This uses fields already stored. The flag's own miss is recorded, not re-derived here.
3. **The lead of a retitled preview (HD edge 1): MEASURE before ruling.**
   - HD's barrons lead is stored at 2026-08-17 16:24Z, a day before the results it reports; it was most likely a preview
     re-headlined after the results.
   - Choosing the earliest `published_utc` promotes it, and the span starts a day early.
   - Whether this is fixable depends on data this seat has not seen: **does silver carry an updated or modified time per
     article** (vendor listing fields, the page's `dateModified`)?
   - If it does, the lead is the earliest member by that time, and a member whose updated time follows the others' first
     reports never leads.
   - If it does not, the one-day-early start is accepted and disclosed on the event (the page shows the event's dates as
     served). A guessed rule would move AMZN's correct first-report lead.
4. **`Z-W48-S1` (the AMZN 09-10 NTSB piece, two days after the burst): NO CHANGE to the link window.** A follow-up after
   two empty days is its own event. Widening the window to catch it would also join unrelated same-company stories.

## 3. FWD GRADES

- `FWD-5` / `FWD-6`: NOT REALIZED. Only the page grade is owed, at DSGN_AMGTV1 round 6's walk (unchanged).
- The event outcomes move only when round 22's served rebuild lands.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 21 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **The span rule plus the roundup guard, in code, dry-rebuilt** | LOCAL. The census prints each changed event's members, `first_day` and lead against today's 8 served, denominator printed. HD's 08-20 roundup must be a member that does not extend the span, so HD's span ends at 08-18. 992 HK's and AMZN's events must equal `j-2`'s. No put. |
| 2 | **The updated-time census** | LOCAL, measurement only. Over the 120 silver articles, how many carry an updated or modified time distinct from `published_utc`, by publisher. HD's barrons lead is read by name. This decides ruling 3. |

**Fan-out:** 2, independent. **Round 22**, after this seat rules the lead question on cell 2, is the SERVED rebuild of
`chatter_event` under a never-widen pair.

**NOT cells:**
- the link window (ruling 4);
- the event route mount (HELD);
- the roundup flag's producer. The guard makes the flag's miss harmless; if a later census shows the flag is wrong on
  more than that one article, it gets its own cell.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Renew Seeking Alpha [spend]. The word is given.

## Compiler Tools

- The CVO's v28: its `j-1` AC2 re-run (8 of 8 x3), its read of the `j-2` drain's diff (0 foreign paths), and its
  member-by-member read of the three changed events with published times from the served mention part.
