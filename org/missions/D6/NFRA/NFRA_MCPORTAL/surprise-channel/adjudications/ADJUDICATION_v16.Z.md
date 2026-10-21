# NFRA_MCPORTAL -- MP-z-6 AC2 on the served capture: leg (a) read, leg (b) still owed (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v16. Fabric: site-z. Recorded: 2026-10-21 ~07:5xZ.

**Input:** `2.0.0_SA_COO~MP` ferry 20261021T071500Z. The capture is
`deliverables/2.0.0_SA_COO~MP/gwz/capture/served_breakdown_capture_20261021.json` @ff7b9d015d, read whole.
- It was taken host-side and read-only at the live gateway `8e3eddf959`, at 07:07:57Z, over the live catalog md5
  `bdfee515ec34`.
- Its probe, `_host_probe.py`, was read whole: it computes the handler's own `_compute()` body and applies the page's
  segment rule.

**TO-MP-z-6 AC2: NOT MET (it supersedes Z-C-S66 only in that leg (a) is now read).**

## Leg (a): MET on what is shown, by this seat's own read, and bounded

- **The probe's own 0 is circular.** It counts `shown_not_of_this_segment` with the handler's `_index_pair`, the same
  function that builds `index_pairs`, so its 0 holds by construction.
- **So I read the 16 shown index names against their segment myself:**
  - blackdiamond / cottonwood shows 7 `silver_cottonwood_fact_*` tables;
  - commonwealth / cottonwood shows 5 `silver_commonwealth_cottonwood_*`;
  - eclipse / inflection shows 2 `silver_eclipse_inflection_*`;
  - orion / inflection shows 2 `silver_orion_inflection_*`.
- Every one names its own firm, and the vendor-qualified ones name their own vendor.
- **No index of one vendor appears under another vendor's segment.** The defect Andrew saw on 10-19, Black Diamond indexes
  on Schwab tools, is not on the served page.
- **The bound: 4 of the 8 segments show NO index at all.** These are blackdiamond / 49financial, schwab / 49financial,
  smartx / 49financial and smartx / multi.
  - Their tools carry `index_pairs`, and none is of their own pair, so 197 indexes are hidden by the rule.
  - The criterion asks for "the tools and indexes on each". On those four segments, Schwab among them, the page shows tools
    and no indexes. Leg (a) passes them only vacuously.
  - Whether that is right (their tables are cataloged under another bucket or pair) or a gap (rows missing their 49F pair)
    is a completeness question. NFRA_MCPINDEX's routing table, leg (b), is the instrument that answers it.

## Leg (b): still owed

- The routing table on record is over candidate catalog e (md5 `03d2dbbae1f0`), not the served `bdfee515`.
- `2.0.0_SA_COO~MI` owes the run against the served catalog. The COO~MP ferry says so too.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S67",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T07:50Z",
    "one_line": "L9 re-grade, NFRA_MCPORTAL.TO-MP-z-6 AC2 (judgment): NOT MET -- leg (a) is read on the served capture (8e3eddf959, catalog bdfee515): the 16 shown indexes each name their own segment and no Black Diamond index sits under a Schwab segment, but 4 of 8 segments (the three 49financial ones and smartx/multi) show tools with no index at all; leg (b), the routing table over the SERVED catalog, is still owed.",
    "class": "OBSERVATION",
    "spec_asserts": "ROUND_ANALYSIS.z-round1.md:29-35: (a) under every vendor/firm segment every index shown belongs to it; (b) NFRA_MCPINDEX v0.19's routing table reads 0 MISROUTED (display) for /gateway; the criterion asks for every vendor or channel, the tools and indexes on each.",
    "world_is": "served_breakdown_capture_20261021.json @ff7b9d015d: totals {shown 16, not of their segment 0 (circular: the probe uses the handler's own _index_pair), hidden 197, unresolved 0}; shown names: 7 silver_cottonwood_fact_* under blackdiamond/cottonwood, 5 silver_commonwealth_cottonwood_* under commonwealth/cottonwood, 2 silver_eclipse_inflection_* and 2 silver_orion_inflection_* under their segments; blackdiamond/49financial, schwab/49financial, smartx/49financial and smartx/multi list tools with shown []. Routing table on record: candidate e (03d2dbbae1f0), not the served catalog.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/gwz/capture/served_breakdown_capture_20261021.json @ff7b9d015d (read whole; every shown name read by this seat)",
        "deliverables/2.0.0_SA_COO~MP/gwz/capture/_host_probe.py (read whole)",
        "ADJUDICATION_v15.Z.md#NFRA_MCPORTAL-Z-C-S66 (leg (b)'s object)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: TO-MP-z-6 AC2 NOT MET, superseding Z-C-S66. Leg (a) MET on what is shown, bounded by the four index-less segments. It re-grades when 2.0.0_SA_COO~MI's routing table over the served catalog lands: 0 MISROUTED (display), and an answer for the four empty segments (cataloged elsewhere, or a missing pair)."
  }
]
```

-- 3.0.0_SA_CVO~Z
