# DSGN_AMGTV1 -- ROUND 9 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~04:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26906, subject *"L10 slug DSGN_AMGTV1 round 9 @6f0de15483"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v11.md`. Issuer: `round9/DRAIN_END_READ.md` @`e196b68a97` (msg 26903).

**Round 9 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`p-1` MET:** the columns are headed "Asset Class" / "Sector" over the sector names, with "Equity" capitalised and no value cut
  short. The grain mismatch from round 8 is resolved.
- **`p-2` MET, with one residual:**
  - each article row reads "A wsj named 8 times August 13th, 2026, 12:55a ET", so the order explains itself;
  - the times convert correctly;
  - the same panel still prints ISO elsewhere.
- **`p-3` MET:** the lead footer has no "Dated", and the older-list line is in plain words.
- **`p-4` (Andrew-direct DIRECT-ACT):** the Security Analysis icon is in Tools. The dev and admin gate is intact, as this seat
  read at `App.tsx:134`.
- No BLOCKING or ARMED row is open in this channel (21 items: 16 GRADUATED).

## 2. RULINGS

1. **THE HOUSE DATE FORM (CVO v11 section 3.1): every date a person reads uses the reference pages' LONG FORM** ("September 28th,
   2026", and with a time "..., 10:47p ET" where one is served).
   - ISO stays only where no one reads it: `data-` attributes, URLs and export fields.
   - **Where the reference pages use a compact form for the same element** (chart axis ticks, for example), the page uses that
     compact form, taken from the reference page's own formatter and never invented.
   - Why: FWD-11's bar is "reads like the reference pages". Round 5's `v-6` made ISO the page's form before that bar existed, and
     each round since has fixed one surface. **One ruling now covers the whole page, so no further round re-decides it.**
   - It covers every surface the packet lists: identity as-of, posture as-of, the axis, the event dates, movement windows,
     "Updated", "filed", the day heading and tooltip, and the bare-date "Dated" paths in HeaderCards and ThesisCards.
2. **CORPUS's six outcomes rendered on the page** (AMGT_CORPUS round-20 analysis ruling 1, @609100db54): **cells 2 and 3.**
   - Cell 2, `dossier_fields`: pillars with citation and terms, the management passage beside the roster, and fund of record plus
     last stated position on the posture line and the Posture tab.
   - Cell 3, the team's cases:
     - the team's Upside and Downside from `model.team_cases`;
     - Opal's rule cases labelled as Opal's ("Opal's rule-based upside: the method is to be agreed");
     - a bare "Upside case: not in the pack yet" never sits beside a served team Upside.
   - The fields are served now (the CVO read IMB and AZN), so this is a page-only build.
3. **No K/M/B/T on an UNRESOLVED unit: cell 4** (AMGT_RESAPP round-50 addendum @7708a8506f).
   - A figure whose served unit is UNRESOLVED shows raw, with its UNRESOLVED label.
   - The six names (6501, 9433, 8316, 8035, 8766 JP and TSM US) are the planted population.
   - This alone lets FWD-30's same-unit-claim condition read true on the page.

## 3. FWD GRADES

- **FWD-4, FWD-9, FWD-10: REALIZED**, standing.
- **HARVST FWD-5, FWD-6: page half MET** (round 8), and promotion is pending.
- **FWD-2: NOT REALIZED.** Headings MET; names show on 7 of 22 rows (AMGT_RESAPP r51 cell 5, then its one build).
- **FWD-11: NOT REALIZED.** Footers and rows are in the long form; the remaining ISO surfaces are cell 1.
- **FWD-1: NOT REALIZED, 5 of 6 hops** (the driver series, AMGT_RESAPP r51 cell 6).
- **FWD-3: NOT REALIZED** (names).
- **3 of 11 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 10 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **One house date form across the page** | FWD-11 | Ruling 1. Census: 0 ISO dates in the visible text of the walked pages, with the ISO values still present in `data-` attributes as the control. |
| 2 | **`dossier_fields` rendered: pillars, management passage, fund of record, last stated position** | CORPUS FWD-10, 11, 15, 16, 18 | Ruling 2. The walk names one page per outcome; IMB is the served positive, and a name with an empty block shows the reason. |
| 3 | **The team's Upside and Downside rendered; Opal's rule cases labelled as Opal's** | CORPUS FWD-12 | Ruling 2. AZN is the planted case (team upside SERVED, rule upside ABSENT). |
| 4 | **Never scale an UNRESOLVED unit** | RESAPP FWD-30 | Ruling 3. The six names are planted; the control is a MEASURED name that still shows its scale. |

**Fan-out:** 4. Cells 2 and 3 may share one worker if their write sets overlap. That is the COO's call from the decomposition.

**Carried, NOT cells:**
- the names and driver series (AMGT_RESAPP r51);
- the `/timeline/day` latency, now about 5.8 s, which rides RESAPP r51 `zz-8` as HARVST `n-6`.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- The portal DEV merge and push [CLAUDE.md Portal]. Site-Z DEV carries rounds 6-9.
- Remove this project's drained worker checkouts [recursive delete].

## Compiler Tools

- The CVO's v11: shots `005` and `115`, and its `_latest_dispositions` read (21 items).
- The packet's section 4.
- This seat's `App.tsx:134` read, at the round-9 5174 move.
