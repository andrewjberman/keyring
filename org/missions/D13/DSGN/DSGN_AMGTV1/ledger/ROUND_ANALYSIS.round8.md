# DSGN_AMGTV1 -- ROUND 8 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~03:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26869, subject *"L10 slug DSGN_AMGTV1 round 8 @d4f7cd10c7"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v10.md`. Issuer: `round8/DRAIN_END_READ.md` @`8fad06dc49` (msg 26865).

**Round 8 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`q-1` MET: the day's articles are on pixels for the first time.**
  - Shot `115` shows 992 HK 08-13 "STRONGEST FIRST" with two rows.
  - `timeline-days.json` records 6 opened days: 3 empty at ~1.6-1.9 s, 2 with rows at 5.3 s and 5.6 s, 0 failed, 0 at the
    ceiling.
  - The CVO verified "strongest first" on the served order: the sort key is tier, then `mention_count` DESC, then time
    (`timeline_api.py:132-139`). 08-13 reads wsj 8 then sa 5; 02-12 reads sa 9 then wsj 7.
  - **This seat read that walk G opened an EVENT:** `{'via': 'event', 'security': '992 HK', 'date': '2026-02-12', 'state':
    'rows', 'waited_ms': 5577}`. So "opening one lists its articles" is exercised too.
- **`q-2` MET, with residuals:** every footer shows a date and a source. The lead line reads the long date with no invented
  time.
- **`q-3` PARTIAL:** the headers match Positioning's, but the values do not (section 2, ruling 1).
- `Z-W4-S1` GRADUATED. No ARMED row remains in this channel.

## 2. RULINGS

1. **FWD-2's grain -- this seat's round-7 ruling 5 was wrong in effect, and is corrected.**
   - Ruling 5 gave the column Positioning's LABEL for the same key. That matched the header and hid a grain mismatch.
   - Positioning's "Sub Asset" holds Opal's buckets ("Large", "High Yield"). The lead list's `sub_asset_class` for single names
     holds GICS sectors ("Energy", "Information Technology"). A PM reads "Energy" and "Large" as values of one field.
   - **RULED:** a column is headed by what its VALUES are. The single-name `sub_asset_class` column is headed **"Sector"**, and
     the unserved finer field is "Industry group (finer than Sector)".
   - Asset class shows in display case ("Equity"), and a long value is shown whole, never truncated.
   - The label follows the grain, so no producer change is needed. If Opal later serves an equity bucket for single names, it
     gets its own "Sub Asset" column.
2. **FWD-5: the strength that orders the day is SHOWN.** Each article row shows its `mention_count` in words ("named 8 times").
   A PM can then see why a row leads. It is served already, so no producer ask.
3. **FWD-11 residuals: CELL 3.**
   - Article times in the estate's one form (no raw ISO, no "(instant)").
   - "Dated" is dropped so the lead line matches the other footers.
   - The second line is rewritten in plain words, for example "This list is from September 28th; the newest available."
   - The Positioning model window's missing source is the reference page's gap and is not cut here.
4. **HARVST FWD-5 and FWD-6, page half: MET on this walk. Grading belongs to AMGT_HARVST's next analysis.**
   - FWD-5: a company's timeline opened, a day picked, and its articles listed strongest first.
   - FWD-6: events listed with lead headlines, and one opened to its articles.
   - The evidence standard is the one this project used for FWD-10: a walk on the 5174 dev build at portal DEV head. Promotion
     to the served portal is the integrator's act and carries it to users.

## 3. FWD GRADES

- **FWD-4, FWD-9, FWD-10: REALIZED**, standing.
- **HARVST FWD-5, FWD-6: page half MET** (ruling 4). HARVST grades the whole.
- **FWD-2: NOT REALIZED.** The grain is misheaded (ruling 1), and names show on 7 of 22 rows (AMGT_RESAPP r51 cell 5).
- **FWD-11: NOT REALIZED.** Three form residuals remain (ruling 3).
- **FWD-3: NOT REALIZED** (the same AMGT_RESAPP names ask).
- **FWD-1: NOT REALIZED, 5 of 6 hops** (AMGT_RESAPP r51 cell 6, the driver series).
- **3 of 11 REALIZED, plus 2 page halves met.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 9 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **The column heading follows the grain ("Sector"); display case; no truncation** | FWD-2 | Ruling 1. The census prints each column's heading beside a sample of its values on every walked list. |
| 2 | **The day's rows show their strength** ("named N times") | HARVST FWD-5 | Ruling 2. |
| 3 | **Article times, the lone "Dated", and the system-voice line** | FWD-11 | Ruling 3. |

**Fan-out:** 3, independent. The round's walk re-grades FWD-2 and FWD-11 by name, with a signed-out control first.

**Carried, NOT cells:**
- names on 22 of 22 rows and the driver series (AMGT_RESAPP r51 cells 5-6, then its one build);
- the `/timeline/day` latency (AMGT_HARVST).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Remove this project's drained worker checkouts `/c/tmp/wk-dsgn-amgtv1-18..31`, `C:/tmp/cood-r7-root/portal` and
  `C:/tmp/cood-r8-root/portal` [recursive delete, CLAUDE.md Agent Autonomy]. The list is COO~D's round-8 read, section 5.

## Compiler Tools

- The CVO's v10: shots `005`, `115` and `146`, its `/timeline/day` reads, and the sort-key read at `timeline_api.py:132-139`.
- This seat: a read of `tmp/ui-walk/20260930T023916Z/timeline-days.json` (6 rows, one `via: event`).
