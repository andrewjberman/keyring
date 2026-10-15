# MDPF_CANON -- round 9 L9: CN-p-2 AC4 graded on the real-data variants (dell1)

<sweep_watermark>2026-10-15T14:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T14:40:00Z. Asked by 2.0.0_SA_COO~D1 msg 6033 (addendum @4695b47f47). One row; no rows swept, so the watermark does not move.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S89",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:40:00Z",
    "one_line": "ROUND 9 L9: JUDGMENT MDPF_CANON.TO-CN-p-2 AC4 MET on the PROD module over the real 2026-10-14 objects: Variant 2 carries 0 single-firm cells, Variant 1 draws Custom Models with no gap from 2026-05-15, and the session gate is right in PROD code. The browser draw of a non-internal session is the stated limit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-p-2 AC4 (judgment): the Global Trend at a stated portal commit, for an internal session and for a demo-tenant claim set, against the producer's deployed arrays and the spec's oracle.",
    "world_is": "ROUND 9 L9, JUDGMENT MDPF_CANON.TO-CN-p-2 AC4: MET. Replaces the hold D1-C-S84 (ADJUDICATION_v15) on new evidence: 2.0.0_SA_COO~D1 msg 6033, org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/CN_P_2_REAL_DATA_VARIANTS_20261015.md @4695b47f47. THIS SEAT RE-RAN IT: round9/checks/measure_real_variants.ts (UNROLLED=1) over the three gold objects this seat fetched itself (s3://opal-data-assets/portal/gold/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries/2026-10-14.json, written by the 13:31Z scheduled run). It imports from the portal checkout, whose trendGrouping.ts, pairedProvenanceRead.ts and modelPortfolioColors.ts are each blob-equal to origin/PROD c3b21a40e2 (git hash-object vs rev-parse). Read: 497 rows, frontier 2026-10-14. VARIANT 2 (every non-internal session): the 383 rows before 2026-05-15 each carry one Models band (383 of 383) and 0 single-firm model cells; Custom Models is suppressed on 55 dates. VARIANT 1 (internal): the 383 earlier rows carry 1,915 single-firm cells and no band, and Custom Models runs from 2026-05-15 (26.25M) to 2026-10-14 (68.88M) with 0 nulls after its first value (the roll-forward Andrew asked for), 34.30M at 2026-06-30. Total, Client Supervised, ETF Strategies and ALT Strategies are equal in both variants on all 497 rows. SESSION SELECTION, read in PROD code: ModelPortfolios.tsx:385-389 sets the mode from internal = isInternal() || isDev(), and :451-464 fetch the 49 Financial and Inflection series only when the scope is global and internal, so a demo or partner claim never fetches a single-firm series. INTERNAL RENDER: Andrew saw the internal Trend before the roll-forward amendment ('It looks good! ... need rollforwards for the Custom Models', relayed in msg 5968 and recorded at org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261015_01xxZ_COO_D1_TREND_LOOKS_GOOD_CUSTOM_ROLLFORWARD_THEN_PROD.md), and approved the PROD promote. LIMIT: no browser draw of a non-internal session was made. The criterion's render clause is met for the internal session by Andrew's own look; for the demo claim it is met by the function the page calls and by the gate that selects it, read on the PROD bytes. What stays unshown is the chart layer's draw of rows already proven to carry no single-firm value, which is a presentation risk, not a leak.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO: DATA_DIR=<own fetch> UNROLLED=1 bun run round9/checks/measure_real_variants.ts, then counts over its output: v2 pre rows 383, band 383, model cells 0; v1 pre rows 383, band 0, model cells 1915; v1 custom first 2026-05-15, nulls after 0; v2 suppressed 55; group differences 0",
        "portal: git hash-object src/lib/{trendGrouping,pairedProvenanceRead,modelPortfolioColors}.ts equal to origin/PROD c3b21a40e2 blobs",
        "portal origin/PROD:src/pages/ModelPortfolios.tsx:385-389 and :451-464",
        "org/mcp/inbox/1.0.0_SA_CTO/~DELL1/read/20261015T010919Z_2.0.0_SA_COO_D1_Andrew-direct__Trend__looks_good___Custo.md (msg 5968)",
        "adjudications/ADJUDICATION_v15.md MDPF_CANON-D1-C-S84"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: AC4 MET; not a hazard."
  }
]
```
