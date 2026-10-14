# MDPF_CANON -- round 7 L9 note: CN-i-1 AC4 re-read at the repaired head (dell1)

<sweep_watermark>2026-10-14T16:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T20:00:00Z. Asked by 2.0.0_SA_COO~D1 msg 5779. One row; no rows swept (watermark unchanged). This seat filed D1-S25 in INVESTIGATION_v1.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S78",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T20:00:00Z",
    "one_line": "ROUND 7: MDPF_CANON.TO-CN-i-1 AC4 HELD at the repaired head fd5433a3 on the tooltip render alone; colour (dE00 20.6), stack (0 FAIL of 487), note and no-band are read MET.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-i-1 AC4 (judgment), the Global AUA Trend against PRD FWD-9 (v2.18) and DESIGN.md.",
    "world_is": "ROUND 7 re-grade at the repaired head, MDPF_CANON.TO-CN-i-1 AC4 HELD on ONE clause (the Trend tooltip render), every other clause read MET at portal fd5433a3 (PROD fa10e758 + the feature + the CN-i-2 repair; msg 5779; render note @965fe386bf blob a9d779b4f21e). This seat's reads: r8_cn_i_2.py on `git archive fd5433a3 src`: BUILD 13 of 13, DATA 3 of 3, REGRESS 2 of 2 (CN-i-1 module 9/9, page 8/8). COLOUR: Client Unsupervised is lime500 #84cc16; its nearest ladder rung is Intermediate #10b981 at CIEDE2000 20.6 (this seat's computation; was 0.0); no other pair under 10.3. TOOLTIP (source): renderTrendTooltip buckets now pass presentTrendEntries, which drops null, undefined, '' and non-finite values, so a null Client series makes no row. STACK: on the served global 2026-10-13 object, 487 valued dates = EXACT 49 + BEFORE-DETAIL 383 (the whole model AUA, $436.8M-$1.349B; PRD v2.18 exception (ii)) + FOLD-OR-OTHER 55 ($26.1M-$58.6M: the same 55 dates and range the signed CN-f-1 pair names for the suppressed Other Models line, exception (ii)) + FAIL 0; served Total = model + non-model + SMA + tax on 487 of 487. RENDER (screenshot 006 of tmp/ui-walk/20261014T193640Z, read by this seat): the five ladder colours unchanged; one Custom Models; Client Unsupervised lime in the legend; the note 'Per-model detail begins May 15, 2026; earlier model assets are in the Total and are not broken out' under the subtitle; nothing drawn for the earlier model dollars. HELD: the tooltip clause (no Client row on dates C and D, no '-$0') has no render read -- the walk hovered on Snapshot before Trend was pressed (the issuer's note says so). Flips on one Trend-daily hover screenshot on a date C or D. Separately filed: row D1-S25 (the Client card $292.26M vs the drill-down $341.10M).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO R8_SRC=<git archive fd5433a3 src> python round7/checks/r8_cn_i_2.py build|data|regress: 13/13, 3/3, 2/2",
        "portal fd5433a3: src/components/CategoryViewTree.tsx:95 lime500; src/lib/trendGrouping.ts:116-122 presentTrendEntries; src/pages/ModelPortfolios.tsx:1168",
        "tmp/ui-walk/20261014T193640Z/shots/006 (read by this seat)",
        "PRD v2.18 @0736ed5c23 FWD-9 (2) exception (ii)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hold record on one clause; the defects of D1-C-S73 are repaired in source; D1-W18-S7, D1-W18-S1 and D1-W18-S3 close with the grade."
  }
]
```
