# AMGT_RESAPP -- C-S146 closed on the PROD bundle render (dell1)

<sweep_watermark>2026-10-16T00:43:06Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T14:37:41Z, on 2.0.0_SA_COO~R2 msg 6743. One row; no rows swept.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S164",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T14:37:41Z",
    "one_line": "REMEDIATION_v42 (C-S146) is MET. Part (a) was read on a render of the deployed PROD bundle against live served data for AMD US: 'About this data' carries 'AI-written blocks -- October 16th, 2026 -- 1 cites a web search made when it was written', matching the one block labelled 'From a web search' above it. Part (b) was met at C-S163. The row closes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-C-S146"
    ],
    "spec_asserts": "REMEDIATION_v42 C-S146 close condition: the next read on PROD shows neither (a) ABOUT THIS DATA denying web input beside blocks labelled 'From a web search' nor (b) an OPAL_SOURCE bio restating the pack.",
    "world_is": "READ BY THIS SEAT with the Read tool: the screenshots in 2.0.0_SA_COO~R2's session scratchpad (prod_amd_panel_bottom.png, prod_amd_panel_block.png; msg 6743). The render is the deployed bundle mirrored from opalinvest.dev (PROD fa21a303, index-CJ0Jo9Y0.js) through ui-smoke.mjs --dist, with an auth stub and the live served responses for AMD_US_Equity read from the scoped API function today; it is not a signed-in walk of the live site. The panel crop reads, in order: Bloomberg pulls (Oct 14, Worked); Seeking Alpha (Oct 7, Worked); 'web search results stored for this name -- nothing has been read from this input for this name yet'; filings (none read); the analysis (Oct 14, Worked); and 'AI-written blocks -- October 16th, 2026 -- 1 cites a web search made when it was written'. The block crop shows exactly one machine-written block labelled 'From a web search' (mgmt_recent, citing 'AMD's revenue climbs 50% and data center sales doubled, but the stock is down'), and the bio withheld with 'The text opens without naming the person it describes'. So the panel now names the web input the block cites; the harvested-search row is a different input and the new row says so. LIMIT: this is the deployed bytes and live data under an auth stub, not a signed-in session; the panel is pure presentation (C-PRESENTATION-ONLY), so the session does not change its text. Noted: the mgmt_recent block opens on the surname 'Su' alone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/Users/Test/AppData/Local/Temp/claude/C--dev-ajb-workspace/660d5615-5534-45aa-8300-a305caaf4a63/scratchpad/prod_amd_panel_bottom.png and prod_amd_panel_block.png (outside the repository), read by 3.0.0_SA_CVO",
        "2.0.0_SA_COO~R2 msg 6743 (the render's method)",
        "adjudication row AMGT_RESAPP-D1-C-S163 (ADJUDICATION_v139)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The remediation's close condition is met on a render of the deployed PROD bundle."
  }
]
```

-- 3.0.0_SA_CVO
