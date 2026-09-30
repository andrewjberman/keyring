# DSGN_AMGTV1 ROUND 5 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~22:1xZ
**Input:** `2.0.0_SA_COO~D`'s `round5/ROUND5_CLOSE_WALK.md` @`e531011a6e`, msg 26733. The packet was read to EOF (6,747 B).
**PNGs read by this seat, walk D (`tmp/ui-walk/20260929T214728Z/`, 106 shots):** `001`, `007`, `054`, `096`, `102`. All five
are signed-in pages. The signed-out control is the packet's own `walkvoid.sh` run (YES, rc=3).
**L7 re-measured, not adopted:** `AV-v-1`..`AV-v-7` all read `complete` on their LAST `<status>` tag at HEAD. Six carry a
judgment each; v-7 carries none.

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions('.', 'DSGN_AMGTV1')` returns **16 items: 9 GRADUATED, 7 UNDER_INVESTIGATION** (7 files). Two open rows
are ARMED: `Z-S1` and `Z-W4-S1`. Round 5 added no row.

| row | disposition | grounds |
|---|---|---|
| `Z-S1` (ARMED: move FWD-1's thread to a name the team covers) | **DISMISSED_WITH_REASON -- stamped on the CTO's ruling** | `ROUND_ANALYSIS.round4.md` section 2, ruling 3 (@`177c576c80`). FWD-1 stays on Valero; hop 6 is met by the page's honest line; FWD-6 is walked on INTU; there is no ENDPOINT change. The swap this row asked for is ruled unnecessary, so its clock stops. |
| `Z-W8-S2` (codes on the Posture face: mnemonics, preset code, UNRESOLVED) | **GRADUATED** | Served by AV-v-1. Shot `102` reads **0 passage ids, 0 preset codes and 0 status words across all 18 cites** (section 2). |
| `Z-W4-S1` (ARMED: does the export follow the page) | **CARRIED** | Half (b)'s producer act, AMGT_RESAPP `ww-4`, is complete and served. This seat's controlled run in AMGT_RESAPP ADJUDICATION_v58 shows the export and the HEAD page still disagree on 33 names' absences, because of the page's wording. The row's question is still open, and it is the same two-writers item as AMGT_RESAPP `Z-S297`. |
| `Z-W8-S1`, `Z-W5-S1`, `Z-S2`, `Z-W11-S1` | **CARRIED** as INERT notes | unchanged |

## 2. L9 -- THE SIX JUDGMENTS

| order | verdict | what the page shows |
|---|---|---|
| **v-1 AC3** (every Posture cite reads as words a PM follows -- no passage id, preset code or status word -- and an uncarried passage says so) | **MET** | `102`, 18 cites. The **6** uncarried passages read "cite not resolved -- a filing passage the research pack cites, which no drafted sentence on this name's thesis quotes, so this page does not carry its text". The carried one names "the company's filing, ITEM 5. OPERATING AND FINANCIAL REVIEW AND PROSPECTS / paragraph 140". The fit scores read "No fit score for this name on one of the model portfolios' screens yet: none of its 16 factors has a value." The membership cite reads "Held in 1 of the model portfolios at the 2026-09-15 snapshot." Figures are in words. **0 of 18** carry a passage id, preset code or status word, against **10 of 18** at round 4. ⚠ Residual: 3 cites still read as machine phrasing outside the clause's named classes. They are "comparability log cap distance: 0.1047 (the object's comparable selection)", "no rung name for the comparable ...", and "no industry group ... on the object's comparable selection". The footer's "on the bundles this page reads (the object validated 18 of 18 ...)" is the same. |
| **v-2 AC4** (ten or more names: every line its own colour, the last date whole, one picked name followable) | **MET** | `007`: the picked 992 HK draws full and thick while the other nine are muted, and it can be followed across all six dates. The last tick "2026-09-28" is whole. **Colour, recomputed by this seat** from portal DEV `4f927ad0` `RankedChart.tsx`: 12 opaque strokes. The minimum CIE76 distance is **46.8 over the 10 drawn** (PBR `#ff3300` vs WALMEX `#ff9900`) and 44.8 over all 12, up from 18.1 at round 4. ⚠ Residual (packet input 3): the muted lines' point dots stay bright, so unpicked series still read as dotted columns. |
| **v-3 AC3** (the lead panel reads its ranking's history in one plain sentence; the load view carries one dark band) | **MET** | `007`: "Of the 30 dates in the window, 6 have a published ranking; the latest is 2026-09-28." `001`: one dark lead panel with the source caption inside its body and no darker footer. The walker's `design:bands` check fires on no step (packet). |
| **v-4 AC4** (the Model face never shows two Base cases without saying whose; the divergence tile says what it diverges from) | **MET** | `096`: the only "Base case" on the face is headed "THE RESEARCH TEAM'S BASE CASE", sourced "THE RESEARCH TEAM'S PACK, SAP RESEARCH PACK 2026 06 12_V1". The rule's line prints its served label, "Historical-multiple reference: 159.61 EUR (Bloomberg consensus EPS (FY1) x adjusted trailing-median P/E)", as the order directs: a served label AS SERVED, and "Opal's rule-based" only when no label is served. The tile reads "DIVERGENCE FROM CONSENSUS FORECAST". The round-4 contradiction is gone. |
| **v-5 AC3** (Exec detail says where it looked, in words, with no machine reason) | **MET** | `054`: "Where we looked: the company's 10-K, section 'Item 10. Directors, Executive Officers and Corporate Governance' (filing 0000896878-26-000037). The section did not list officers in a form this page can read." It ends there. |
| **v-6 AC3** (the page's own dates in one form; the timeline legend reads on the band) | **MET** | The page's own dates are all ISO: "Updated 2026-09-29", "identity as of 2026-09-25", "2026-01-01", "2026-08-31 TO 2026-09-29". The long form is served prose, as ruled at the cut. **Legend, measured by this seat on `096`'s pixels** against band `#192643`: DENIED ink about **4.8:1**, PARTIAL about **4.1:1**. Both read, and both clear the walker's 3:1 floor. ⚠ PARTIAL sits under 4.5:1. |

## 3. OBSERVATIONS FOR THE ROUND-5 ANALYSIS (not grades)

1. **INTU's `/timeline` 500 does not reproduce on the function.** This seat invoked `/api/scoped/amgt/security/INTU_US_Equity/timeline`
   on the deployed `opal-amgt-scoped-api` at ~22:0xZ. It returned **HTTP 200, 99,843 B**, and SAP and VLO both returned 200 as
   controls. The walk's 500 came through the local 5174 route, so either the fault was transient or it sits on the dev path.
   The page defect stands either way: on that 500 the band showed a **loading skeleton**, not a designed error state
   (`054`).
2. **The team's Base case prints "unit $ as written in the team's pack" on a EUR-quoted name.** The figures are 144.28-237.58,
   against a price of EUR 184.18. They are printed as served; whether the pack's unit is right is the research team's call.
3. **The Historical-multiple reference does not say whose it is.** The order admits the served label, but a PM reading it
   beside "THE RESEARCH TEAM'S BASE CASE" is not told it is Opal's rule. A producer label naming the owner would settle it.
4. **v-1's residual machine phrasing:** 3 cites plus the footer (section 2).
5. **v-2:** the muted lines' dots should mute with their lines.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 7 of 7. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S1` DISMISSED_WITH_REASON on ruling 3; `Z-W4-S1` CARRIED with its
   measured reason. **MET**
3. **Every judgment criterion graded:** 6 of 6 MET. **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S7",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T22:15:00Z",
    "one_line": "L9 round 5 on walk D: v-1..v-6 all MET -- Posture cites 0 of 18 with a code (was 10 of 18), the pick followable with min stroke dE 46.8 (was 18.1), one band, whose-Base-case said, Exec detail without the machine reason, one date form with the legend at ~4.1-4.8:1; Z-W8-S2 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AV-v-1..AV-v-7 read 'complete' on their LAST <status> tag at HEAD.",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 16 items, 9 GRADUATED, 7 UNDER_INVESTIGATION, 7 files; ARMED Z-S1, Z-W4-S1.",
        "Shot 102 (walk D): 18 cites, 6 x 'cite not resolved -- a filing passage the research pack cites, which no drafted sentence on this name's thesis quotes, so this page does not carry its text', 'the company's filing, ITEM 5. OPERATING AND FINANCIAL REVIEW AND PROSPECTS / paragraph 140', 2 x 'No fit score for this name on one of the model portfolios' screens yet: none of its 16 factors has a value.', 'Held in 1 of the model portfolios at the 2026-09-15 snapshot.'",
        "Shot 007: 992 HK picked, full and thick, nine muted; last tick '2026-09-28'. Palette from git -C portal show 4f927ad0:src/pages/SecurityAnalysis/components/RankedChart.tsx: 12 hexes, min CIE76 dE 46.8 over the first 10, 44.8 over 12.",
        "Shot 096: 'THE RESEARCH TEAM'S BASE CASE', 'Historical-multiple reference: 159.61 EUR (Bloomberg consensus EPS (FY1) x adjusted trailing-median P/E)', 'DIVERGENCE FROM CONSENSUS FORECAST', 'Updated 2026-09-29'; legend pixels vs band (25,38,67): DENIED (215,117,123) 4.80:1, PARTIAL (204,105,96) 4.11:1.",
        "Shot 054: Read detail ends '... The section did not list officers in a form this page can read.'",
        "Deployed /api/scoped/amgt/security/INTU_US_Equity/timeline ~22:0xZ: status 200, 99843 B; SAP_GY and VLO_US 200."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W8-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @e531011a6e asserts 7 orders terminal, walk D VALID with the signed-out control YES, and per-judgment observations on walk D.",
    "world_is": "True as read on the pixels and on this seat's own palette, contrast and endpoint reads. Every round-4 PARTIAL clause is now met; the residuals are machine phrasing in 3 Posture cites, bright dots on muted lines, a skeleton on a 500, and a Historical-multiple reference that does not say whose it is.",
    "notes": "FOR THE ROUND-5 ANALYSIS: (1) the page's error branch on a /timeline failure shows a loading skeleton; the 500 did not reproduce on the function (200 at ~22:0xZ); (2) SAP's team Base case reads 'unit $' on a EUR name -- research team's call; (3) a producer label saying whose the Historical-multiple reference is; (4) 3 Posture cites and the footer in machine phrasing; (5) mute the dots with their lines; (6) PARTIAL legend ink ~4.1:1."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S8",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T22:15:00Z",
    "one_line": "Z-S1 stamped DISMISSED_WITH_REASON on 1.0.0_SA_CTO~Z's round-4 analysis ruling 3 (@177c576c80): FWD-1 stays on Valero, hop 6 is met by the page's honest line, FWD-6 is walked on INTU, no ENDPOINT change -- the covered-name swap the row asked for is ruled unnecessary.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round4.md section 2 ruling 3: 'Z-S1 (ARMED, carried four rounds): RE-RULED here so that it can be stamped DISARMED ... 3.0.0_SA_CVO~Z stamps Z-S1 DISARMED at its next compile, on this ruling.'",
        "Walk D shot 096 (SAP GY) shows the research team's Base case served where the pack carries one; FWD-6's walk name INTU carries team cases (AMGT_RESAPP ADJUDICATION_v58: team_cases 95 of 95 names as the dossier holds them)."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled by 1.0.0_SA_CTO~Z, ROUND_ANALYSIS.round4.md section 2 ruling 3 (@177c576c80): FWD-1's thread stays on Valero and hop 6 is met by the page's honest line that the team's case is not in their pack yet; FWD-6 is walked on INTU; no ENDPOINT change. The covered-name swap is unnecessary.",
    "spec_asserts": "Row Z-S1 asserts FWD-1's thread name cannot carry hop 6 because Valero's team cases are absent, and asks for a move to a name the team covers.",
    "world_is": "Valero's team cases are still absent, and the CTO ruled that hop 6 is met by the page's honest line on Valero, not by a swap. The hazard (an unmeetable hop) is removed by ruling, not by data.",
    "notes": "The DISARMED stamp the ruling names is carried here as the item's disposition; an investigation item has no disarm.state field."
  }
]
```
