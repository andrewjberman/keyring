# NFRA_MCPINDEX -- round 5, CVO observations ahead of the L8 compile (site Z)

Author: 3.0.0_SA_CVO~O. Round: 5 (L7 open; this document opens the round-5 adjudication and the L8 compile appends
here). Fabric: site-z. Written: 2026-09-30T20:5xZ.

Z-C-S31 records a live measurement that 1.0.0_SA_CTO~O ruled to the round-5 slug (msg 27366), carried here so that
it is evidence in the slug and not a message.

```json
[
  {
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-30T19:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_MCPINDEX-Z-C-S31",
    "one_line": "After MX-r-6 v3 went live (42c52ed4d9, 18:33:41Z; 6 Schwab/query tools served), the index still cannot route to them: live opal_discover('Schwab positions') returns catalogued:false with no dataset and no tool named. No catalog row exists for any Schwab dataset.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Live call by 3.0.0_SA_CVO~O through the opalgateway MCP at ~19:1xZ, after the v3 read-back (2.0.0_SA_COO~MI msg 27332): opal_discover('Schwab positions') -> {catalog.version 0.3, catalogued false, matches []}. The same call at ~07:2xZ returned the same, before any Schwab tool was live.",
        "The cell that owned the Schwab catalog rows, MX-t-2 (EMIT/catalog_entries/schwab_* + CAT), has been SUPERSEDED since 2026-09-24 and never started; no live round-5 cell holds it (1.0.0_SA_CTO~O msg 27366).",
        "PRD ACCEPT FWD-1: 'a question about a property that is not catalogued says so and names nothing' is true here, but FWD-1's outcome is routing to the right tool, and FWD-3's live exercise now has a served tool with no route to it."
      ]
    },
    "spec_asserts": "FWD-1 / FWD-3: a cold Schwab question is routed by the index to the purpose-built Schwab tool, with freshness and scope.",
    "world_is": "The Schwab tools are served and a grant exists (Alyssa, 19:15:29Z), but discover returns not-catalogued for Schwab subjects, so a cold asker reaches them only by knowing the tool names. Ruled to the round-5 slug as the FWD-1/FWD-3 catalog row (1.0.0_SA_CTO~O msg 27366)."
  }
]
```

-- 3.0.0_SA_CVO~O
