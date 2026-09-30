# DSGN_AMGTV1 ROUND 6 -- L8 COMPILE + L9 ADJUDICATION (nine judgments, two projects)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~23:5xZ
**Input:** `2.0.0_SA_COO~D`'s `round6/ROUND6_CLOSE_WALK.md` @`8906e6690`, msg 26782. The packet was read to EOF (5,784 B).
**Walk E:** `tmp/ui-walk/20260929T232112Z/` (156 shots, `lead-lists.json`), read by this seat:
- `lead-lists.json` in full;
- PNGs `007`, `013`, `014`, `015`, `017`, `110`, `116`, `144`, `146`.

**L7 re-measured, not adopted:** `AV-u-1`..`AV-u-5` all read `complete` on their LAST `<status>` tag.
**Grading rule:** each u-4 judgment is graded against its FWD's own ACCEPT, read at `prd/DSGN_AMGTV1_PRD.md` (FWD-1, FWD-2, FWD-11)
and at `AMGT_HARVST/prd/AMGT_HARVST_PRD.md` (FWD-5, FWD-6).

---

## 1. L9 -- NINE JUDGMENTS

| criterion | verdict | what the page shows |
|---|---|---|
| **u-2 AC3** (every Posture cite and the footer read as words, FWD-10) | **MET** | `110` (SAP GY): "Citation not resolved -- the research pack does not say the comparable's industry group"; "Size difference between the two companies (log of market value): 0.1047 (from how the comparable was chosen)"; footer "10 of the 18 citations can be shown on this page; the research pack checked 18 of 18 against its sources". The v7 residuals ("rung name", "log cap distance", "the object's comparable selection", "bundles") are gone. |
| **u-3 AC3** (with one picked, the rest fade -- lines and dots; names only where served, FWD-3) | **MET** | `007`: the unpicked dots now mute with their lines, and 992 HK is followable. The legend reads "Valero Energy Corp", "Petroleo Brasileiro SA" and "ASML Holding NV" where a name is served, and tickers elsewhere. |
| **u-1 AC3** (a failed timeline reads as a designed error; a PARTIAL day says which publishers were searched, never "covered"; the legend reads on the band, FWD-5/11) | **PARTIAL** | **Legend: MET.** `116`, `014` read "COMPLETE -- PARTIAL -- DENIED" in band ink with swatches. **The error state and the PARTIAL wording were never on a walked pixel:** the walk had 0 API issues and no PARTIAL day was opened, so the planted 500 and the served-fixture render are the only evidence. **A contradiction on the face:** `014` (VLO) captions an all-DENIED series "No coverage found in this range yet -- every day above is a real, honest zero". A denied day was never read, so it is not a real zero. |
| **u-4 AC3 -- DSGN FWD-1** (the thread, hop by hop) | **PARTIAL -- 5 of 6 hops** | 1. Valero is picked by name, "Valero Energy Corp" #2 (`013`). 2. The header reads as four cards (`014`). 3. The Financials window opens: "Enterprise value USD 117B / Net debt USD 5.93B", with "2026-09-29 \| Source: Bloomberg" (`015`). 4. **The Thesis reads as three cards, but not "under the main chart":** the chart is a designed empty state, "The series for the thesis driver ... is not in the model data yet" (`014`). 5-6. The Recommendation opens and says whose view it is: "a machine's draft from the company's filing, not the research team's recommendation". Each citation names its document, down to "VLO US'S 10-K, FILED 2026-02-25 -- ITEM 7 ... PARAGRAPH 72" (`017`). The walk used real data under a signed-in account. ⚠ Each machine line carries a "PASS" badge on the face. |
| **u-4 AC4 -- DSGN FWD-2** (every row: name, ticker, Opal's asset class, sub-asset class and sector, period figure, places moved) | **NOT MET** | `lead-lists.json`: **22 rows over the four lists; 7 show a served name (SERVED), 15 do not (NOT_SERVED); 0 of 22 show a classification or places moved.** Breakout x Chatter has **0 rows**. Trending x Chatter ranks BA and HD at "chatter 0/100 (0 mentions)". |
| **u-4 AC5 -- DSGN FWD-11** (indistinguishable beside Market, Positioning and Philosophy; every footer a time and a source; no raw code, id or path anywhere) | **NOT MET** | **Raw codes on the face:** `116` (992 HK) prints its served posture reason in the header verbatim: "ABSENT -- no call was made: comparable null: R-1 carries no held member ... no landed model_block_992_HK_Equity.json (AMGT-s-1's record is the only permitted subject read -- F2/G-24, no new Bloomberg call) ...". That is a file name, a project code, ruling ids and a status word. The census never saw it because it measures VLO, INTU and SAP only. The text is `/thesis`'s own served prose (this seat's invocation found `model_block_992` in the payload). **Footers differ in form:** the references read "September 28th, 2026, 5:00p ET \| Source: Bloomberg" (`144`, `146`), while Security Analysis reads "2026-09-29 \| Source: Bloomberg": no time, and the ISO form round 5's v-6 standardised on. **Windows match:** the hero window is the same piece (`015` vs `146`). **Cards:** the references build them as dark bands, which is the C3 breach the packet raises for the CTO. |
| **u-4 AC6 -- AMGT_HARVST FWD-5** (click any day: its articles, strongest first) | **NOT MET on pixels -- never exercised** | The day click works and opens "2026-09-29'S ARTICLES, STRONGEST FIRST", but every walked newest day was denied or empty (`116`, `110`). **This seat's invocation of 992 HK's 2026-08-13** returns **2 articles** (wsj "Lenovo Posts Record Revenue ...", sa "Lenovo Group jumps on strong Q1 revenue ...") **with `data_status DENIED`**. So when a day with articles is opened, the page will print "DENIED DAY -- RETRIEVAL WAS DENIED FOR THIS DAY" above real articles. |
| **u-4 AC7 -- AMGT_HARVST FWD-6** (bursts appear as marked events with a headline) | **NOT MET** | `timeline:no-event-element` on all four names. 992 HK has served events (AMGT_HARVST v28: 02-12, 05-22, 08-13). `116`'s chart shows bars near them and marks none. |

## 2. L8 -- THE CHANNEL COMPILE

`_latest_dispositions('.', 'DSGN_AMGTV1')` returns **19 items: 10 GRADUATED, 1 DISMISSED_WITH_REASON, 8 UNDER_INVESTIGATION**
(8 files).

| row | disposition | grounds |
|---|---|---|
| `Z-W23-S1`, `Z-W23-S2` (BLOCKING: two harness anchors moved by u-5's attributes) and `Z-W23-S3` (their resolution under AMENDMENT 1) | **GRADUATED** | This seat's runs. `modelPattern.harness.cjs` reads "CHECKS-OK 12 of 12". `round6/checks/attrs.cjs` reads "FWD-30 ATTRIBUTES: 3 of 3 arms", with "sheet cells with a year 190 ... value == served 190" and "visible changed: []". |
| `Z-W4-S1` (ARMED: does the export follow the page) | **CARRIED** | **The page now carries the values** (`attrs.cjs`, above). **But AMGT_RESAPP's FWD-30 grader still reads identity-only facts**: its figure keys are still tuples like `('FISCAL', 'SALES_REV_TURN', '2020')` on the u-5 page. So the value blind spot measured in AMGT_RESAPP v59 closes only when that grader reads `data-model-cell`'s value. That is an AMGT_RESAPP cell. |
| `Z-W8-S1`, `Z-W5-S1`, `Z-S2`, `Z-W11-S1` | **CARRIED**, INERT | unchanged |

## 3. FOR THE ROUND-6 ANALYSIS

1. **FWD-11, the served posture reason renders raw** (`116`). Either the page shows a designed empty state for a posture ABSENT,
   or AMGT_RESAPP serves words. C-PRESENTATION-ONLY says a missing value reads "in plain words ... never a project code".
   **Extend the census to every walked name**, since it missed 992 HK.
2. **The page's own date form now diverges from the reference pages'.** v-6 made Security Analysis ISO with no time; the
   finished pages read "September 28th, 2026, 5:00p ET". FWD-11's "a time and a source" and "the same pieces" point to the
   references' form. The CTO rules which one is the house form.
3. **DENIED vs articles:** a day can be served DENIED while carrying articles (992 HK 08-13). The page's "retrieval was
   denied" label and VLO's "real, honest zero" caption both misread `data_status`. That is AMGT_HARVST's field and the page's
   wording.
4. **FWD-2's columns** (classification and places moved) are unbuilt, and whether the served list rows carry them is unmeasured.
   **FWD-6's event layer** is a page cell over events HARVST already serves.
5. **The walker should open a day with articles** (for example 992 HK 2026-08-13) so that FWD-5 can be graded on pixels.
6. **The "PASS" badge** on each Recommendation line is a status word on the face (FWD-11).

## 4. L10 PRECONDITION

1. **Every task order terminal:** 5 of 5. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W23-S1..S3` GRADUATED on this seat's runs; `Z-W4-S1` CARRIED with its
   measured reason. **MET**
3. **Every judgment criterion graded:** 9 of 9. u-2 and u-3 are MET; u-1 and FWD-1 are PARTIAL; FWD-2, FWD-11, FWD-5 and FWD-6
   are NOT MET. **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S9",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T23:50:00Z",
    "one_line": "L9 round 6 on walk E: u-2, u-3 MET; u-1 PARTIAL; FWD-1 PARTIAL (5 of 6 hops, the Thesis chart is an empty state); FWD-2 NOT MET (7 of 22 rows named, 0 classified); FWD-11 NOT MET (992 HK's header prints 'model_block_992_HK_Equity.json ... AMGT-s-1 ... F2/G-24' verbatim; footers ISO without time vs the references' long form); HARVST FWD-5 never exercised (992 HK 08-13 serves 2 articles as DENIED), FWD-6 NOT MET (no event layer).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AV-u-1..AV-u-5 read 'complete' on their LAST <status> tag.",
        "lead-lists.json: Trending x Chatter 2 rows (SERVED 2), Trending x Price 10 (SERVED 3, NOT_SERVED 7), Breakout x Chatter 0, Breakout x Price 10 (SERVED 2, NOT_SERVED 8); fields [lead, name_state, text, ticker] -- no classification, no places moved.",
        "Shot 116 (992 HK header): 'ABSENT -- no call was made: comparable null: R-1 carries no held member ... no landed model_block_992_HK_Equity.json (AMGT-s-1's record is the only permitted subject read -- F2/G-24, no new Bloomberg call)'; deployed /thesis for 992_HK_Equity carries 'model_block_992' in its payload.",
        "Shots 144/146 footers 'September 28th, 2026, 5:00p ET | Source: Bloomberg' vs 015 '2026-09-29 | Source: Bloomberg'.",
        "Deployed /api/scoped/amgt/security/992_HK_Equity/timeline/day/2026-08-13 -> 200, data_status DENIED, 2 articles (wsj, sa, tier A).",
        "Shot 014: VLO all-DENIED series captioned 'No coverage found in this range yet -- every day above is a real, honest zero'.",
        "modelPattern.harness.cjs 'CHECKS-OK 12 of 12'; round6/checks/attrs.cjs 'FWD-30 ATTRIBUTES: 3 of 3 arms', 'value == served 190'; sweep.py page_facts FIGURES keys still ('FISCAL', mnemonic, year) on portal fd4deb75.",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 19 items (10 GRADUATED, 1 DISMISSED_WITH_REASON, 8 UNDER_INVESTIGATION), 8 files."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W23-S1",
      "DSGN_AMGTV1-Z-W23-S2",
      "DSGN_AMGTV1-Z-W23-S3"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @8906e6690 asserts 5 orders terminal, walk E VALID with the signed-out control YES, and per-criterion observations for nine judgments across DSGN_AMGTV1 and AMGT_HARVST.",
    "world_is": "True as read. The walk is the first to grade the endpoint outcomes: FWD-1 is nearly there, FWD-2/6 are unbuilt, FWD-5 was not exercised on a day with articles, and FWD-11 fails on a raw served reason the census could not see and on a date form that now diverges from the reference pages.",
    "notes": "FOR THE ROUND-6 ANALYSIS: (1) 992 HK's raw posture reason in the header; census every walked name; (2) the house date form (ISO vs 'September 28th, 2026, 5:00p ET'); (3) DENIED-with-articles and the 'real, honest zero' caption; (4) FWD-2 columns and FWD-6 event layer; (5) walk a day with articles; (6) the PASS badge."
  }
]
```
