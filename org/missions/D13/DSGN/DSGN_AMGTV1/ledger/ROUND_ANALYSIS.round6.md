# DSGN_AMGTV1 -- ROUND 6 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~23:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26786, citing `surprise-channel/adjudications/ADJUDICATION_v8.md`. Issuer
packet: `deliverables/2.0.0_SA_COO~D/round6/DRAIN_END_READ.md` @`8906e66901` (msg 26781).

**Round 6 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

5 of 5 orders are terminal. Walk E is valid. The CVO graded nine judgments: 2 MET, 2 PARTIAL, 4 NOT MET.
- **MET: u-2 (FWD-10) and u-3 (FWD-3's pick and fade).**
  - Every Posture cite and the footer read as words.
  - Unpicked lines and dots mute together.
  - Served names label their lines: "Valero Energy Corp", "Petroleo Brasileiro SA", "ASML Holding NV".
- **PARTIAL: u-1.**
  - The legend reads on the band.
  - The error state and the PARTIAL wording were never on a walked pixel.
  - VLO's all-DENIED series is captioned "a real, honest zero", which is false.
- **PARTIAL: FWD-1, 5 of 6 hops.** The Thesis sits under a designed empty chart ("the series for the thesis driver ... is not
  in the model data yet").
- **NOT MET: FWD-2, FWD-11, HARVST FWD-5 and HARVST FWD-6.**
- **The page now carries values on `data-model-cell`** (`attrs.cjs`: 190 of 190 equal to served). AMGT_RESAPP's round-50
  cell 1 must read them; its grader is still identity-only.

## 2. RULINGS

1. **FWD-11, the raw posture reason on 992 HK (lead item): the page never prints a served reason verbatim when the status
   is ABSENT. The producer serves words.**
   - The header printed `/thesis`'s own prose: a file name (`model_block_992_HK_Equity.json`), a project code
     (`AMGT-s-1`), ruling ids (`F2/G-24`) and a status word.
   - **Page:** an ABSENT posture renders the estate's designed empty state, "No call on this name yet", plus one plain
     reason class from the served status. C-PRESENTATION-ONLY forbids rewriting served prose, so the page shows the
     designed state instead of the text.
   - **Producer ask (AMGT_RESAPP):** the served reason names no file, code or id.
   - **The census covers EVERY walked name**, not VLO, INTU and SAP only. It missed 992 HK.
2. **The house footer form: the REFERENCE pages' form.**
   - FWD-11's ACCEPT is "indistinguishable beside Market, Positioning and Philosophy" and "every footer reads as a time and
     a source".
   - The references read "September 28th, 2026, 5:00p ET | Source: Bloomberg". Security Analysis reads "2026-09-29 |
     Source: Bloomberg": no time, and a different form.
   - **Security Analysis uses the estate's shared footer component** (C-ESTATE-FIXTURES), so the form is the component's.
     Where a served vintage has no time, the footer prints the date in the same long form and says it is a date.
   - Round-5 v-6's ISO standard is superseded for footers. The page's in-body data dates stay ISO, where a date is data,
     not a footer.
3. **What "the same pieces" means against reference pages that break C3 (packet item 4).**
   - FWD-11 is graded on the estate COMPONENTS: the cards, windows, charts, empty states and footers of
     C-ESTATE-FIXTURES; the footer form; and no raw codes.
   - It is **not** graded on copying the reference pages' band counts or contrast. Market has 10 bands, Positioning 6, and
     Positioning reads 46-50 contrast findings: those are those pages' defects, not the standard.
   - C3 (one dark band per view) stands on Security Analysis.
   - The reference pages' breaches are recorded as an observation for their owners, not DSGN's scope.
4. **DENIED with articles (992 HK 2026-08-13: 2 articles, `data_status DENIED`): the page's wording is wrong, the field is
   not.**
   - By HARVST's rule, DENIED means no publisher's listing search reached that day. It does not mean retrieval failed, and
     it does not mean zero.
   - The page says "Not searched on this day", never "retrieval was denied". A day with articles lists them under that
     line.
   - The all-DENIED caption never says "honest zero". It says the range was not searched.
5. **FWD-2's columns: MEASURE, then build.** The served list rows carry name and classification since `ww-2`, but whether
   they carry "places moved" is unmeasured. The cell renders what is served and prints the census. An unserved column
   becomes a RESAPP ask, never a page computation.
6. **The "PASS" badge on Recommendation lines** is a status word on the face (FWD-11). It is removed from visible text and
   kept as a data attribute.
7. **FWD-3's names for every ranked line: a producer ask.**
   - Names show only where `etf-classifications` holds the ticker. For example, 7 of 22 list rows show a served name.
   - The crosswalk carries every registered name's display name (for example `HITACHI LTD`).
   - AMGT_RESAPP falls back to the crosswalk name when `etf-classifications` lacks one, and labels the source.

## 3. FWD GRADES

- **FWD-4, FWD-9: REALIZED**, standing.
- **FWD-10: REALIZED.** u-2 is MET on the walked names; every cite and the footer read as words.
- **FWD-3: NOT REALIZED.** The pick, dates, colours and fade are met; names are served for only some lines (ruling 7).
- **FWD-1: NOT REALIZED, 5 of 6 hops.** The thesis driver's chart series is not in the model data. That is a producer
  gap, carried to AMGT_RESAPP.
- **FWD-2, FWD-11: NOT REALIZED** (rulings 1, 2, 5 and 6).
- **HARVST FWD-5 / FWD-6: NOT REALIZED on the page.**
  - FWD-5 was never exercised on a day with articles.
  - The FWD-6 event layer is unbuilt; the events are served (cell 3).
- **3 of 11 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 7 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **Posture ABSENT as a designed empty state; the census covers every walked name** | FWD-11 | Ruling 1. The planted positive control is 992 HK's served reason, which must never reach visible text. |
| 2 | **Footers use the estate's shared footer component and form** | FWD-11 | Ruling 2. One footer form, identical beside the reference pages. |
| 3 | **Timeline: "Not searched" wording, the event layer, and a day with articles walked** | HARVST FWD-5, FWD-6 | Ruling 4. `[data-timeline-event]` marks each served event with its headline. The walker opens 992 HK 2026-08-13 (2 articles) and grades "strongest first" on pixels. |
| 4 | **FWD-2's columns from served fields; the PASS badge removed** | FWD-2, FWD-11 | Rulings 5 and 6. Render the served classification, and places moved if served; the census prints each list's column coverage. |

**The round's walk grades FWD-2, FWD-11, HARVST FWD-5 and HARVST FWD-6 by name, with a signed-out control first.
Fan-out:** 4.

**Producer asks to AMGT_RESAPP** (its next open list):
- a posture reason in words, with no file, code or id (ruling 1);
- a crosswalk-name fallback for ranked names (ruling 7);
- "places moved", if cell 4 measures it unserved;
- the thesis driver's chart series (FWD-1 hop 4).

**NOT cells:**
- the reference pages' band and contrast defects (their owners);
- "$1,234" in drafted prose (carried).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- The merged worker checkouts `wk-dsgn-amgtv1-18..25`. Removing them is a recursive delete [CLAUDE.md Agent Autonomy];
  his ~20:2xZ word covered 9-17 only.

## Compiler Tools

- The CVO's v8: nine L9 judgments on walk E's shots, its `/thesis` invocation (`model_block_992` in the payload), its
  992 HK 2026-08-13 day read (2 articles, DENIED), and `attrs.cjs` (190 of 190).
- The COO's packet section 4.
