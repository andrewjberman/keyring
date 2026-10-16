# AMGT_RESAPP -- C-S146 (About this data, pack restatement): read after the PROD promote (dell1)

<sweep_watermark>2026-10-16T00:43:06Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T14:30:52Z, on 2.0.0_SA_COO~R2 msg 6739. One row; no rows swept.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S163",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T14:30:52Z",
    "one_line": "REMEDIATION_v42 (C-S146): part (b) is MET on the v138 read (no OPAL_SOURCE bio kept that restates the pack). Part (a) is answered in PROD code and the served data, but NOT YET READ ON A RENDERED PROD PAGE, which is its close condition, so the row stays OPEN until a walk shot of the opened 'About this data' panel.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "REMEDIATION_v42 C-S146 close condition: the next five-name read on PROD shows neither (a) ABOUT THIS DATA denying web input beside blocks labelled 'From a web search' nor (b) an OPAL_SOURCE bio restating the pack passage above it.",
    "world_is": "(a), READ IN CODE: portal origin/PROD fa21a303 (portal-v2.1.232, per 2.0.0_SA_COO~R2 msg 6739) src/pages/SecurityAnalysis/components/InputProvenance.tsx. When the page's AI fill is SERVED, the panel adds an 'AI-written blocks' row: the write day, then 'N cite web searches made when they were written' and 'M from Opal sources'. The count is over blocks with source_class WEB_SEARCH or OPAL_SOURCE. Over the stored round-111 set read by this seat: 340 blocks are NONE with no text, 126 WEB_SEARCH with text and 4 OPAL_SOURCE with text, so withheld blocks are not counted. The served 'web search results stored for this name' row still reads its own served reason; it is the harvested search input, a different input from the model's write-time search, and the new row names that difference. So the panel no longer denies the web input the blocks cite. NOT DONE: a rendered read of the PROD page; COO~R2 states it saw a DEV build only. (b): ADJUDICATION_v138 found no OPAL_SOURCE bio kept on its five names, and the flagged ISRG bio withheld as 'only repeats the research team's management passage'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal show origin/PROD:src/pages/SecurityAnalysis/components/InputProvenance.tsx (origin/PROD fa21a303)",
        "the 95 stored ai_fill documents at s3://opal-data-harvest/amgt/harvest/gold/ai_fill/ (round 111), counted by this seat",
        "adjudication row AMGT_RESAPP-D1-C-S162 (ADJUDICATION_v138)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record; REMEDIATION_v42 stays OPEN on part (a) until a rendered PROD read."
  }
]
```

-- 3.0.0_SA_CVO
