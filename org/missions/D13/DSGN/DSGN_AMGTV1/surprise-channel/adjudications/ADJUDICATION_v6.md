# DSGN_AMGTV1 ROUND 4 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~19:4xZ
**Input:** `2.0.0_SA_COO~D`'s `round4/ROUND4_CLOSE_WALK.md` @`e4620fa1f9`, msg 26673. The packet was read to EOF (6,534 B).
**PNGs read by this seat, walk C (`tmp/ui-walk/20260929T191345Z/`, 103 shots):** `004`, `005`, `051`, `093`, `099`. All five
are signed-in pages. This seat also ran its own signed-out walk (`tmp/ui-walk/20260929T193404Z/`, shot `001`).
**L7 re-measured, not adopted:** `AV-w-1`..`AV-w-6` all read `complete` on their LAST `<status>` tag at HEAD. Five of them
carry 1 judgment each; w-1 carries none.

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions('.', 'DSGN_AMGTV1')` returns **16 items: 9 UNDER_INVESTIGATION, 7 GRADUATED**. Two of the open rows are
ARMED: `Z-S1` and `Z-W4-S1`.

| row | disposition | grounds |
|---|---|---|
| `Z-S3` (a walk step on the sign-in page reported 0 findings) | **GRADUATED** | Served by AV-w-1, and verified on this seat's own runs. `walkvoid.sh` printed "walker rc=3; WALK VOID lines=1; account lines=0" and then "SIGNED-OUT CONTROL: the walk FAILS on the sign-in page: YES", exit=0. `detect.mjs` passed "6 of 6 cases" including both negative arms, exit=0. A direct walker run logged "WALK VOID: step /security-analysis-load landed on the sign-in page" with rc=3, and its shot `001` IS the Opal sign-in page ("Welcome back", email and password fields). Walk C's five shots graded below are signed-in pages, so walk C's zero-void claim holds on the pixels. |
| `Z-W13-S1` (Git Bash mangles `--route`) | **GRADUATED** | This seat's run from Git Bash reached `/security-analysis-load`, not a `C:/Program Files/Git/...` path. walk.mjs's strip works where the row said it did. |
| `Z-W8-S2` (codes on the Posture face) | **CARRIED, narrowed** | The figure-mnemonic half is served: shot `099` reads "Operating margin, FY2025: 26.1332%". The preset-code and passage-id halves stand; see w-5 below. |
| `Z-W4-S1` (ARMED: does the export follow the page) | **CARRIED** | Half (a) is served (round 3). Half (b), the export's wording from one served definition, is AMGT_RESAPP `ww-4`: `complete` at HEAD, and its L8 is owed in that project. This row is not graded from here. |
| `Z-S1` (ARMED: move FWD-1's thread to a covered name) | **CARRIED** | the CTO's ENDPOINT call |
| `Z-W5-S1`, `Z-W8-S1`, `Z-S2`, `Z-W11-S1` | **CARRIED** as INERT notes | unchanged this round |

## 2. L9 -- THE FIVE JUDGMENTS

| order | verdict | what the page shows |
|---|---|---|
| **w-2 AC3** (the list reads each ticker as a PM types it) | **MET** | `004`: "992 HK", "VLO US", "ASML NA", "BP/ LN", "RWE GR", "9433 JP", "2317 TT", "WALMEX* MM". Each is whole, as the terminal takes it. |
| **w-3 AC4** (the Model tab reads every missing, refused and unmeasured line as a plain sentence, with no status label) | **MET** | `093`: the tiles read "Not measured yet". All 19 unit lines read "In the research pack, but this page cannot show it yet because its unit is not set up here." Also "No year-on-year growth rows: the pack carries none and this page computes none." and "2026E, 2027E, 2028E: not in the pack -- it carries fiscal years 2016 to 2025 only." There are 0 REFUSED/ABSENT/SERVED labels, where round 3 had 18+. Two observations follow in section 3. |
| **w-4 AC3** (Exec Management: no second band; the detail says in words where the list was looked for) | **MET** | `051`: the Exec panel header is white, and the page's one dark band is the name header. "Read detail": "Where we looked: the company's 10-K, section 'Item 10. Directors, Executive Officers and Corporate Governance' (filing 0000896878-26-000037). The section did not list officers in a form this page can read." One residual: the served machine reason is still appended verbatim ("no declared shape read this section (4 usable line(s), 0 candidate(s)) ..."). |
| **w-5 AC3** (Posture: the comparable's gaps said once; every cite reads as words) | **PARTIAL** | Gaps once: **MET**. `099` shows three bullets plus ONE line, "The comparable's evidence is incomplete: 3 source(s) are missing from ANET US's pack." The three figure cites the cell built read as words: **MET**. "Every cite": **NOT MET, 8 of 18 read as words.** The other 10 carry a code or status token: 7 passage ids ("... carries passage P0102 ...", P0118, P0094, P0106, P0091, P0108, and "filing passage P0201"); 2 read "fit score PFOE: no score (status ABSENT; 0 of 16 factors present (16 code(s) named by the preset))"; 1 reads "membership: held in PFDE". The shortfall lies outside the cell's build, which named the figure cites only, but inside the criterion's words and the design law ("A code ... never in visible text"). It is an FWD-10 remainder that no cell served. |
| **w-6 AC3** (with ten or more names: one legend, dates that do not overlap, one name a PM can pick and follow) | **PARTIAL** | One legend: **MET** (`005`, the buttons below the chart). Dates: **MET on overlap**, with a defect: the rightmost tick is clipped at the chart edge ("2026-09" then cut). Pick-and-follow: **UNGRADED**. Walk C never clicked a legend button, walk.mjs has no legend step (0 matches for `data-series-ticker` / `legend`), so no pixel shows a picked line. Colour: 10 distinct strokes. This seat computed CIE76 distance over all 45 pairs of the built palette (portal DEV 09bd04b1 `RankedChart.tsx`). The closest pair is VLO US `#f59e0b` vs WALMEX* MM `#fb923c` at dE 18.1, which reads as two oranges on the band. Next is VLO vs 9433 JP at 25.7. Labels are tickers because no company name is served (the packet's item 6, a producer ask). |

## 3. OBSERVATIONS FOR THE ROUND-4 ANALYSIS (not grades)

1. **The Model tile names are the worker's reading of letter codes.** "Peers V" became "Peer valuation score" and
   "Divergence D" became "Forecast divergence score", because `types.ts` defines neither. If the producer means something
   else, the page mislabels a score. C-PRESENTATION-ONLY would want the served label or the producer's definition.
2. **The Model's Base case reads as a contradiction to a PM.** `093` prints "The research team's Base case is not served on
   this page yet." and, three lines below, "Base case: 159.61 EUR (adjusted consensus EPS (FY1) x adjusted trailing-median
   P/E)". Both are true: the first is the team's case, the second the rule's. The face does not say which is which.
3. **w-6: the pick is untested on pixels.** The cheapest proof is a walker step that clicks one `data-series-ticker` button
   and screenshots it. The right-edge date clip and the VLO/WALMEX colour pair are page defects for the same view.
4. **w-5's remainder:** passage ids, preset codes and "status ABSENT" in the Posture cites. This is `Z-W8-S2`'s standing
   half and the packet's items 1-2.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 6 of 6. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** 2 ARMED, both CARRIED with reasons. **MET**
3. **Every judgment criterion graded:** 5 of 5. w-2, w-3 and w-4 are MET; w-5 is PARTIAL (8 of 18 cites in words); w-6 is
   PARTIAL (pick UNGRADED). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S6",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T19:45:00Z",
    "one_line": "L9 round 4 on walk C and this seat's own runs: w-2, w-3, w-4 MET; w-5 PARTIAL (gaps once MET, 8 of 18 cites in words -- 7 passage ids, 2 PFOE status-ABSENT, 1 PFDE); w-6 PARTIAL (one legend MET, dates MET but the last tick clipped, pick UNGRADED, VLO/WALMEX dE 18.1); Z-S3 and Z-W13-S1 graduate on this seat's signed-out walk.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AV-w-1..AV-w-6 read 'complete' on their LAST <status> tag at HEAD.",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 16 items, 9 UNDER_INVESTIGATION, 7 GRADUATED; ARMED Z-S1, Z-W4-S1 carried.",
        "Z-S3, this seat's runs: walkvoid.sh -> 'walker rc=3; WALK VOID lines=1; account lines=0', 'SIGNED-OUT CONTROL: the walk FAILS on the sign-in page: YES', exit=0; detect.mjs -> 'SIGN-IN DETECTOR: 6 of 6 cases', exit=0; walk.mjs --no-login -> 'WALK VOID: step /security-analysis-load landed on the sign-in page', rc=3; shot tmp/ui-walk/20260929T193404Z/shots/001 is the sign-in page.",
        "w-2 shot 004: '992 HK', 'BP/ LN', 'WALMEX* MM', '9433 JP', '2317 TT' whole.",
        "w-3 shot 093: 'Not measured yet' x3 tiles; 19 x 'In the research pack, but this page cannot show it yet because its unit is not set up here.'; 0 status labels.",
        "w-4 shot 051: white Exec header; 'Where we looked: the company's 10-K, section 'Item 10. ...' (filing 0000896878-26-000037). The section did not list officers in a form this page can read.'",
        "w-5 shot 099: 'The comparable's evidence is incomplete: 3 source(s) are missing from ANET US's pack.' once; 18 cites (footer '10 of 18 cite(s) resolved'), of which 10 carry P0xxx / PFOE / PFDE / 'status ABSENT'.",
        "w-6 shot 005: one legend of 10 buttons; rightmost tick clipped; palette (portal DEV 09bd04b1 RankedChart.tsx) min CIE76 dE over 45 pairs = 18.1, #f59e0b VLO US vs #fb923c WALMEX* MM; walk.mjs has no legend-click step."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S3",
      "DSGN_AMGTV1-Z-W13-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @e4620fa1f9 asserts 6 orders terminal, walk C VALID with the WALK VOID guard live, and each judgment's observations on walk C.",
    "world_is": "True as read. The guard was proven on this seat's own signed-out walk. Two judgments are PARTIAL on clauses the pixels either contradict (w-5, 10 of 18 cites carry codes) or never exercised (w-6, the pick).",
    "notes": "FOR THE ROUND-4 ANALYSIS: (1) the Posture cites' passage ids, preset codes and 'status ABSENT' (w-5 remainder, Z-W8-S2); (2) a walker step that clicks one legend button, plus the right-edge date clip and the VLO/WALMEX colour pair (w-6); (3) the Model tile names need the producer's definition, not the worker's reading of 'Peers V' / 'Divergence D'; (4) the Model face prints 'Base case is not served' above a served rule Base case without saying which is which; (5) the Exec detail still appends the served machine reason verbatim."
  }
]
```
