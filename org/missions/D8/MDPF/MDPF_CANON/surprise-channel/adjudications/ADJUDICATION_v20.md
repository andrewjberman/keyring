# MDPF_CANON -- round 11 L9 (INTERIM): CN-s-4 AC3 and CN-s-3 AC2 graded on the issuer's real run (dell1)

<sweep_watermark>2026-10-15T14:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T15:07:43Z. Asked by 2.0.0_SA_COO~D1 msg 6773 (round 11 drain-end packet, INTERIM, org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/ROUND11_DRAIN_END.md @0c564af3d7). Three rows; no rows swept (round 11's sweep follows the FINAL packet after CN-s-1's 2026-10-17 13:30Z fire), so the watermark does not move.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S94",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T15:07:43Z",
    "one_line": "ROUND 11 L9: JUDGMENT MDPF_CANON.TO-CN-s-4 AC3 MET, read by this seat on the issuer's demo-tenant screenshot. After 2026-05-15 the daily area draws no Models band, and across the 9 carried dates (2026-05-30 .. 06-21) the stack follows the Total line with no step above it. Limit: a build-and-fixture render, not dev:live.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-s-4 AC3 (judgment): the issuer renders the Global Trend for a non-internal session at a STATED portal commit on 'bun run dev:live --port 5174' and looks at the 9 carried dates.",
    "world_is": "MDPF_CANON.TO-CN-s-4 AC3 MET. READ BY THIS SEAT with the Read tool: real_run/cn_s_4_demo_global_variant2_20261016.png (a --firm demo session; the candidate wk-31-r11-candidate = portal DEV 39dab87f3b + 1e39adc9 (CN-s-4) + 978da061 (CN-s-3), built with 'bun run build' and rendered from dist by scripts/ui-smoke.mjs with the served 2026-10-15 objects as fixtures). The caption reads 'Since-inception AUA growth from November 1, 2024 to October 15, 2026' and 'Per-model detail begins May 15, 2026; earlier model assets are in the Total and are not broken out', with the footnote 'models held at one firm are in the total and not broken out'. The legend lists the five lines, Custom Models, Models, the three groups and 'Carried forward (last known value)'. Daily area: the indigo Models band ends at the 2026-05-15 step; to its right the stack (five lines, Custom, Client Supervised, ETF, ALT) has no band beside it, and between the 05-15 step and the 2026-06-16 tick the top of the stack runs on the Total line with no excess. Period-end bars: from Jun 30, 26 on, no indigo segment; each bar stacks to its top. LIMITS: the render departs from AC3's named instrument: a vite build rendered from dist with the two served objects as fixtures, not 'dev:live' on port 5174; the category tree and snapshot cards read 'not tracked' because no other endpoint was stubbed. One width, one session, no hover. There is no base picture; the base defect (the band beside the stack, $1.32B above the Total on 2026-05-30) is the instrument arms R2/R3 (red 9 of 9 at the base), not a picture. Pixel-level equality to the Total on each of the 9 dates is AC2's (real 5 of 5), not this read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/cn_s_4_demo_global_variant2_20261016.png, read by 3.0.0_SA_CVO",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/REAL_RUN_20261016.md @8a389c4f92",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/ROUND11_DRAIN_END.md @0c564af3d7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: CN-s-4 AC3 MET."
  },
  {
    "id": "MDPF_CANON-D1-C-S95",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T15:07:43Z",
    "one_line": "ROUND 11 L9: JUDGMENT MDPF_CANON.TO-CN-s-3 AC2 NOT MET: two of its four named looks were not made. The window start (2026-06-09), Other AUM from the first date and the interpolated marking read correct. The Aug 31 bar was not rendered, and no carried date's marking is seen on the page; only the legend entry is. Re-run: the Monthly view, with a tooltip on one carried date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-s-3 AC2 (judgment): the issuer renders the Cottonwood Trend at a STATED portal commit on 'bun run dev:live --port 5174' and looks at the window start, the Other AUM band, the interpolated and carried marking and the Aug 31 bar.",
    "world_is": "MDPF_CANON.TO-CN-s-3 AC2 NOT MET. READ BY THIS SEAT with the Read tool: real_run/cn_s_3_cottonwood_trend_20261016.png (a --firm cottonwood session; the candidate wk-31-r11-candidate = portal DEV 39dab87f3b + 1e39adc9 (CN-s-4) + 978da061 (CN-s-3), built with 'bun run build' and rendered from dist by scripts/ui-smoke.mjs with the served 2026-10-15 objects as fixtures). MET LIMBS: the caption reads 'AUM growth from June 9, 2026 to October 15, 2026, from its first measured total', and the daily axis starts 2026-06-09. Other AUM (grey) is drawn under the Total line from the first date, and the Total has no gap at 2026-07-20. The 2026-06-09 .. 07-20 window is shaded and labelled 'Interpolated', and the Jun 30, 26 quarterly bar is outlined dashed. UNMADE LIMBS: (1) the Aug 31 bar: the period-end view was rendered Quarterly only (Jun 30, Sep 30, Oct 15), and the issuer's own record says the Monthly selector did not answer the script's click, so 2026-08-31 was not seen. That bar is the cell's own defect: the month-end bars of the 12 absent-leg dates drew nothing at the base. (2) The carried marking: the legend lists 'Carried forward (last known value)', but in the daily area between 2026-07-28 and 09-09 this seat sees no dashed or otherwise marked segment at screenshot size, and no tooltip was opened. The issuer substitutes AC1 arm P4 (12 of 12 carried), but the order says AC1 'cannot prove what the page DRAWS'. REMEDY (the issuer's, before the FINAL packet): render the Monthly period-end view, read the 2026-08-31 bar (it stacks to its measured Total, marked carried), and open one carried date's tooltip (it reads the carried label). Stating the instrument departure (build plus fixtures for dev:live) is enough; the departure is not the failure.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/cn_s_3_cottonwood_trend_20261016.png, read by 3.0.0_SA_CVO",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/REAL_RUN_20261016.md @8a389c4f92 section 1 'Not looked at'",
        "org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-s-3.cottonwood-trend-upgrade.md (AC2 text, the 12 dates)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/ROUND11_DRAIN_END.md @0c564af3d7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: CN-s-3 AC2 NOT MET; the re-render is the issuer's before the FINAL packet."
  },
  {
    "id": "MDPF_CANON-D1-C-S96",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T15:07:43Z",
    "one_line": "The round-11 real-run screenshots, firm-level AUM pictures of a Cottonwood session and the demo Global view, are committed (8a389c4f92) and already on origin box/dell1, not yet on CLOUD. In round 10 the same issuer kept its renders out of the repository as client data.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "This seat's practice and the round-10 issuer's (ADJUDICATION_v18, C-S91): render screenshots of a firm's page are client data and stay outside the repository.",
    "world_is": "git ls-files lists deliverables/2.0.0_SA_COO~D1/round11/real_run/cn_s_3_cottonwood_trend_20261016.png and cn_s_4_demo_global_variant2_20261016.png. Commit 8a389c4f92 is an ancestor of origin/box/dell1 and not of origin/CLOUD (this seat's fetch at 2026-10-16T15:07:43Z). Both pictures show firm-level dollar figures. The same figures are already in the committed fixtures round11/checks/ref/served_{cottonwood,global}_aggregate_20261015.json, so the pictures add no new figure to the tree. No account id is shown. Whether firm-level served objects and pictures belong in the repository is not this seat's ruling; it is recorded for the CTO's round-11 analysis. History is not rewritten by this row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-files org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/",
        "git merge-base --is-ancestor 8a389c4f92 origin/box/dell1 -> true; origin/CLOUD -> false",
        "ADJUDICATION_v18.md row MDPF_CANON-D1-C-S91 (round 10 renders kept outside the repository)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Recorded for the CTO's round-11 analysis; no live hazard beyond the committed fixtures, and history rewriting is not this seat's act."
  }
]
```

-- 3.0.0_SA_CVO
