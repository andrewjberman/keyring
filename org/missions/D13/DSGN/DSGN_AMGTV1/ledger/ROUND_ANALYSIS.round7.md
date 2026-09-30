# DSGN_AMGTV1 -- ROUND 7 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~01:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26839, subject *"L10 slug DSGN_AMGTV1 round 7 @51a24070f3"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v9.md`. Issuer: `round7/DRAIN_END_READ.md` @`556ee6a3a6` (msg 26835) and
`ROUND7_CLOSE_WALK.md`.

**Round 7 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **The judgments:**
  - `s-1` MET: a name with no call reads "No call on this name yet" plus a reason in words.
  - `s-4` MET: served classification columns, with no PASS badge.
  - `s-2` MET on the windows, with one residual.
  - `s-3` PARTIAL: the event list and the "Not searched" wording are on the page; the articles of an opened day are not.
- **The walker restoration is graduated.** The CVO's runs read pick 3 of 3, thread 3 of 3, day 3 of 3 and sign-in 6 of 6.
- **The skeleton is attributed by measurement.** The walker shoots 1,500 ms after a day press. The deployed `/timeline/day`
  answers in about 5.5 s for a day with articles (5.49, 5.63 and 5.69 s) and about 1.5 s for an empty day. So every opened
  day was shot before its response landed. No page loading code changed (`fd4deb75..ab7e1e49`).

## 2. RULINGS

1. **FWD-5: the walker waits for STATE, not time.**
   - After a day press, the walker waits for the day list to show article rows or its designed empty or failed state (a
     `data-` attribute the panel sets), with a ceiling of at least 15 s. It records which of the three it saw.
   - A ceiling hit is recorded as its own result, never as a skeleton shot.
   - Then 992 HK 2026-08-13 (2 articles) is walked again and "strongest first" is graded on the pixels.
2. **The day route's ~5.5 s latency is a served defect for AMGT_HARVST, not this project.**
   - An analyst waits 5 s or more for two articles, and it holds warm, so it is not a cold start.
   - It is routed to 2.0.0_SA_COO~H as a round-24 input: profile `/timeline/day` against the parts it reads, then a fix under
     that project's pair.
   - This project grades the page on whatever the route returns. It does not wait on the fix.
3. **FWD-6: the event LIST inside the timeline panel meets the grading lines.**
   - The DONE WHEN is "the timeline shows the event runs ... each with its lead headline, and opening one lists its
     articles". The ACCEPT is "marked events with a headline".
   - The title's word "spans" names the concept; it is not a separate criterion, and no span drawing is cut.
   - FWD-6 remains NOT REALIZED on its last clause, "opening one lists its articles". That clause shares ruling 1's timing
     and is graded on the same re-walk.
4. **The `s-2` residual (the lead panel's source line, "Source: ranked 2026-09-28 from Bloomberg prices (32 names) (requested
   2026-09-30)"): IT COUNTS.**
   - It sits where a window's footer sits, and FWD-11 reads "every footer". It takes the one form: the date in words through
     `formatPanelTimestamp`, then "Source: ...".
   - The ranking carries a date and no time, so it renders DATE ONLY. It must not invent a time.
   - The requested date may follow as a second clause in words.
5. **"Sub-asset class" showing sector names while "sector" is listed unserved: a LABEL defect on this page, not a producer
   defect.**
   - Measured: the classifier's rows carry `sub_asset_class` at the GICS-sector grain for equities ("Industrials",
     "Financials") and a SEPARATE, finer `sector` field ("Banks" under "Financials";
     `lib/research/api/tests/test_list_rows_classification.py:56`, `:93`). So the served column is right, and the unserved
     field's label is ambiguous.
   - The page names each field with the label the Positioning breakdown uses for the same key (the round-7 AC already binds
     "laid out like the Positioning breakdown").
   - If Positioning has no label for `sector`, the page names it by its grain, for example "industry group, finer than
     sub-asset class". It is never a second "sector".

## 3. FWD GRADES

- **FWD-4, FWD-9, FWD-10: REALIZED**, standing.
- **FWD-11: NOT REALIZED.** Posture and window footers are met. The lead-list source line (ruling 4) is the one open footer.
- **FWD-2: NOT REALIZED.**
  - The columns are served, but the unserved field's label is wrong (ruling 5).
  - Places moved is unserved (an AMGT_RESAPP ask).
  - Names show for 7 of 22 rows (AMGT_RESAPP's crosswalk-name fallback, ruling 7 of round 6).
- **FWD-3: NOT REALIZED.** Names are served for only some lines (the same AMGT_RESAPP ask).
- **FWD-1: NOT REALIZED, 5 of 6 hops.** The thesis driver's chart series is AMGT_RESAPP's.
- **HARVST FWD-5 / FWD-6: NOT REALIZED on the page.** Both are graded at round 8's re-walk (rulings 1 and 3).
- **3 of 11 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 8 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **The walker waits for day STATE** (rows, empty or failed) with a ceiling of 15 s or more, recorded in `timeline-days.json` | HARVST FWD-5, FWD-6 | Ruling 1. The negative arm: a day whose route is held past the ceiling records "ceiling", never rows. The re-walk opens 992 HK 2026-08-13 and one event, and grades "strongest first". |
| 2 | **The lead-list source line in the one footer form, date only** | FWD-11 | Ruling 4. It reuses `formatPanelTimestamp`. The census prints every footer on the walked pages in one form. |
| 3 | **Classification labels follow Positioning's labels per key; the unserved field is named by its grain** | FWD-2 | Ruling 5. The census prints each column's label beside Positioning's label for the same key. |

**Fan-out:** 3, independent. The round's walk grades FWD-2, FWD-11 and HARVST FWD-5/6 by name, with a signed-out control first.

**Routed, NOT cells here:**
- the `/timeline/day` latency, to AMGT_HARVST (ruling 2);
- names for the other 15 rows, places moved, and the thesis driver's series, to AMGT_RESAPP (standing asks).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Remove the merged worker checkouts `/c/tmp/wk-dsgn-amgtv1-18` .. `-28` and the scratch `C:/tmp/cood-r7-root/portal` [recursive
  delete, CLAUDE.md Agent Autonomy]. His ~20:2xZ word covered 9-17 only. Every branch is kept.

## Compiler Tools

- The CVO's v9: its reads of shots `005`, `015`, `017`, `019`, `116` and `117`, its timed direct invocations of `/timeline/day`,
  and the `walk.mjs` settle history.
- This seat: a Grep for `sub_asset_class` over `lib/research` (13 hits; the classifier's two-grain rows in the test fixtures).
