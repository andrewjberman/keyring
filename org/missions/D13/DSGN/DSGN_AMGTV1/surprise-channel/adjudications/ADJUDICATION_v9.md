# DSGN_AMGTV1 ROUND 7 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~01:5xZ
**Input:** `2.0.0_SA_COO~D`'s `round7/ROUND7_CLOSE_WALK.md` @`556ee6a3a`, msg 26836. The packet was read to EOF (4,843 B).
**Walk F:** `tmp/ui-walk/20260930T012605Z/` (158 shots, `lead-lists.json`, `timeline-days.json`, `netlog.tsv`), read by this seat:
- PNGs `005`, `015`, `017`, `019`, `116`, `117`;
- `timeline-days.json`, `netlog.tsv`.

**L7 re-measured, not adopted:** `AV-s-1`..`AV-s-4` all read `complete` on their LAST `<status>` tag. Four judgments.

---

## 1. L9 -- FOUR JUDGMENTS

| criterion | verdict | what the page shows |
|---|---|---|
| **s-1 AC4** (a name with no call reads as a designed empty state in words; no file name, code or id, FWD-11) | **MET** | `116` (992 HK header): "Posture (as of 2026-09-16): No call on this name yet -- no comparable company could be matched to this name yet". The v8 raw reason (`model_block_992_HK_Equity.json`, `AMGT-s-1`, `F2/G-24`) is gone. |
| **s-2 AC4** (every footer reads as a time and a source in the reference pages' one form, FWD-11) | **MET on the windows; one residual** | `015`: "September 28th, 2026, 10:47p ET \| Source: Bloomberg". That is the form of the Market and Positioning footers (`144`/`146` in walk E). **Residual:** the lead panel's source line still reads "Source: ranked 2026-09-28 from Bloomberg prices (32 names) (requested 2026-09-30)" (`005`). That is ISO with no time. It is a list caption rather than a window footer, and the CTO rules whether it counts. |
| **s-4 AC4** (every row: name, ticker, Opal's asset and sub-asset class where served, laid out like the Positioning breakdown, the unserved columns named once, no PASS, FWD-2/11) | **MET** | `005`: columns Name / Asset class / Sub-asset class, and BP/ LN reads "--". "Not served for this list yet: sector, places moved since the last run. The research data team adds them." `017`: the Recommendation lines carry no PASS badge. ⚠ **The served "Sub-asset class" values are sector names** ("Energy", "Information Technology", "Utilities"), while "sector" is named as not served. A PM reads a sector under one heading and "sector: not served" under another. Either the producer's sub-asset class for equities is the GICS sector, or the label is wrong; AMGT_RESAPP owns the field. |
| **s-3 AC4** (a PM opens a day and reads its articles strongest first under "Not searched on this day"; the coverage bursts appear as marked events with a headline, HARVST FWD-5/6) | **PARTIAL** | **Events:** `116` lists "COVERAGE EVENTS -- PRESS ONE TO OPEN ITS FIRST DAY" with 992 HK's three served events, each with its headline, dates and article count (e.g. "Lenovo Posts Record Revenue ... -- 2026-08-13 to 2026-08-14, 3 articles"). **That meets FWD-6's ACCEPT, "marked events with a headline"**, but as a list under the chart, not the "spans on that timeline" of FWD-6's own title. Wording: "2026-08-13: not searched on this day -- 2 found anyway", and the legend reads "NOT SEARCHED". **Articles strongest first: not reached on pixels** (section 2). |

## 2. ⭐ WHY THE DAY'S ARTICLES NEVER RENDERED -- MEASURED: WALKER TIMING AGAINST A SLOW ROUTE, NOT A PAGE FAILURE

The packet left it "unproven either way". This seat measured three things.

1. **Every day opened in walk F sits on the skeleton, including days with no articles.** That is `116` (992 HK 08-13), `117`
   (992 HK 09-29, 0 articles) and `019` (VLO 09-29, 0 articles). In round 6, under the same walker step, VLO's 09-29
   rendered "DENIED DAY ... No articles this day".
2. **The walker did not change its settle,** and no page loading code changed:
   - `walk.mjs` settles 1,500 ms after a day press. That arrived with u-4 in round 6 (`e26e817087`) and is unchanged at
     `4a0628755b`.
   - The portal diff `fd4deb75..ab7e1e49` touches `TimelinePanel.tsx` only for wording and the event list (`0f9780a5`). No
     fetch or loading code changed.
3. **The deployed day route is slow,** timed by this seat against `opal-amgt-scoped-api` (`Um3BOJ+jcVc3...`) by direct invocation:

   | day | articles | response time |
   |---|---|---|
   | 992 HK 2026-08-13 | 2 | 5.49 s, and 5.63 s on a warm repeat |
   | 992 HK 2026-02-12 | 2 | 5.69 s |
   | VLO 2026-09-29 | 0 | 1.53 s |

   **A day with articles takes about 5.5 s, warm. An empty day takes about 1.5 s, right at the walker's settle.**

**Reading:** the walker shoots at 1.5 s, before a 1.5-5.7 s response lands, so it records a skeleton whichever branch the page
would render. Round 6's VLO day landed just inside the settle; round 7's did not. This is not proof that the page renders the
articles, because the walk never saw them. But it removes the reason to suspect the page. The packet's static render
(timeline7.cjs arm 1) lists the served shape.

**Two findings for the analysis:**
- **The walker must wait for the day's rows or its state, not a fixed 1.5 s.** Otherwise FWD-5 cannot be graded.
- **A ~5.5 s wait for a day's articles is PM-visible latency on the served route** (AMGT_HARVST's `/timeline/day`). It holds on
  repeat calls, so it is not a cold start.

## 2a. SMALLER OBSERVATIONS

- `117` shows the tooltip "2026-09-29: not searched on this day." and `019` shows "Every day in this range was not searched yet,
  so no articles were looked for -- a blank day here is not a quiet day." **The v8 contradiction ("a real, honest zero" on an
  all-DENIED series) is fixed.**

## 3. L8 -- THE CHANNEL COMPILE

`_latest_dispositions('.', 'DSGN_AMGTV1')` returns **21 items: 13 GRADUATED, 1 DISMISSED_WITH_REASON, 7 UNDER_INVESTIGATION**
(9 files).

| row | disposition | grounds |
|---|---|---|
| `Z-W28-S1` (BLOCKING/ARMED: the walker lost AV-u-4's steps) and `Z-S4` (resolves it: the integrator merge `8b3f8e8833` dropped them; restored at `4a0628755b`) | **GRADUATED** | This seat's runs: `pickstep.cjs` "WALK PICKS A NAME: 3 of 3 arms"; `walkthread.cjs` "WALK GRADES BY NAME: 3 of 3 arms"; `walkday.cjs` "WALK OPENS A DAY BY DATE: 3 of 3 arms"; `detect.mjs` "SIGN-IN DETECTOR: 6 of 6 cases". Walk F used the restored steps (thread and day both present). |
| `Z-W4-S1` (ARMED: does the export follow the page) | **CARRIED** | as in v8: the page carries the values; AMGT_RESAPP's grader does not yet read them |
| `Z-W8-S1`, `Z-W5-S1`, `Z-S2`, `Z-W11-S1` | **CARRIED**, INERT | unchanged |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W28-S1` and `Z-S4` GRADUATED on this seat's runs; `Z-W4-S1` CARRIED. **MET**
3. **Every judgment criterion graded:** 4 of 4. s-1 and s-4 are MET; s-2 is MET with a residual; s-3 is PARTIAL. **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S10",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T01:50:00Z",
    "one_line": "L9 round 7 on walk F: s-1, s-4 MET; s-2 MET on windows (lead-panel caption still ISO); s-3 PARTIAL -- events listed with headlines (FWD-6 ACCEPT, as a list not spans), articles never rendered because the walker settles 1.5 s and the deployed day route answers in ~5.5 s for a day with articles (timed by this seat), not a page failure; Z-W28-S1 and Z-S4 graduate on the restored walker checks.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AV-s-1..AV-s-4 read 'complete' on their LAST <status> tag.",
        "Shots 116/117/019 (walk F): the day list is a loading skeleton on 992 HK 08-13 (2 articles), 992 HK 09-29 (0) and VLO 09-29 (0); timeline-days.json 'pressed: true, article_rows_in_page_order: []'.",
        "Direct invocation of opal-amgt-scoped-api (Um3BOJ+jcVc3...) /timeline/day: 992_HK 2026-08-13 200, 2 articles, 5.49 s and 5.63 s; 2026-02-12 200, 2 articles, 5.69 s; VLO 2026-09-29 200, 0 articles, 1.53 s.",
        "walk.mjs history: 'await settle(page, 1500)' after the day press since e26e817087 (round 6), unchanged at 4a0628755b; portal diff fd4deb75..ab7e1e49 touches TimelinePanel.tsx only in 0f9780a5 (wording, event list).",
        "Shot 015 footer 'September 28th, 2026, 10:47p ET | Source: Bloomberg'; shot 005 columns Name / Asset class / Sub-asset class, 'Not served for this list yet: sector, places moved since the last run.'; shot 017 no PASS badge; shot 116 'Posture (as of 2026-09-16): No call on this name yet -- no comparable company could be matched to this name yet'.",
        "pickstep.cjs 3 of 3, walkthread.cjs 3 of 3, walkday.cjs 3 of 3, detect.mjs 6 of 6 (this seat's runs).",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 21 items (13 GRADUATED, 1 DISMISSED_WITH_REASON, 7 UNDER_INVESTIGATION), 9 files."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W28-S1",
      "DSGN_AMGTV1-Z-S4"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @556ee6a3a asserts 4 orders terminal, walk F VALID, and per-criterion observations, leaving FWD-5's skeleton 'unproven either way'.",
    "world_is": "True as read, and the skeleton is now attributed by measurement: a fixed 1.5 s settle against a day route that answers in ~5.5 s for a day with articles. FWD-5 on pixels waits on the walker, and the route's latency is itself a PM-visible finding.",
    "notes": "FOR THE ROUND-7 ANALYSIS: (1) the walker must wait for the day's rows or its state; (2) ~5.5 s on AMGT_HARVST's /timeline/day for a day with articles; (3) the served 'Sub-asset class' shows sector names while 'sector' is listed unserved -- AMGT_RESAPP's field or label; (4) FWD-6 events are a list, not spans on the timeline; (5) the lead panel's source line is ISO without a time."
  }
]
```
