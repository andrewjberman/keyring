# MDPF_STRATID -- FWD-1 L9 grade on the Global-view page read

<sweep_watermark>2026-10-09T15:53Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T15:53:00Z. Packet: 2.0.0_SA_COO~S1 msg 2698. FWD-1 MET: Global PFDE $410K = Cottonwood PFDE $410K on the page, total up by exactly that.

```json
[
  {
    "id": "MDPF_STRATID-C-S6",
    "project": "MDPF_STRATID",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T15:53:00Z",
    "one_line": "FWD-1 MET: someone for Andrew (the signed-in seat walk, per the CTO's round-1 analysis R1) opened the Global view after the 13:30Z scheduled run and read it. Global (All) > SMAs > ETF Strategies > PFDE reads $410K, and Cottonwood's own view > SMAs > ETF Strategies > PFDE reads $410K (both served 410,420.98); Global's total rose by exactly that amount and nothing else (ADJUDICATION_v2 C-S4: opal_aggregate_aua = base + tax + sma_additive 410,420.98; Client untouched). Every page figure agrees with the served category-views 2026-10-08 (VersionId eCS4t0Te, written 13:31:41Z). The served-data grade (C-S4) and this page read together close FWD-1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_STRATID PRD FWD-1 DONE WHEN 'EXERCISED -- Andrew (or someone for him) has opened the Global view after a scheduled run and read it'; spine L9.",
    "world_is": "FWD-1 MET: someone for Andrew (the signed-in seat walk, per the CTO's round-1 analysis R1) opened the Global view after the 13:30Z scheduled run and read it. Global (All) > SMAs > ETF Strategies > PFDE reads $410K, and Cottonwood's own view > SMAs > ETF Strategies > PFDE reads $410K (both served 410,420.98); Global's total rose by exactly that amount and nothing else (ADJUDICATION_v2 C-S4: opal_aggregate_aua = base + tax + sma_additive 410,420.98; Client untouched). Every page figure agrees with the served category-views 2026-10-08 (VersionId eCS4t0Te, written 13:31:41Z). The served-data grade (C-S4) and this page read together close FWD-1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T154815Z/shots/002--portfolios-press-SMAs.png (Global SMAs $50.28M; ETF Strategies $21.46M: Dividend SMA $17.08M, Opal Equity Growth SMA $3.97M, PFDE $410K)",
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T154815Z/shots/008--portfolios-open-SMAs-Separately-managed.png (Cottonwood SMAs $7.87M; ETF Strategies $1.78M: Dividend SMA $1.37M, PFDE $410K)",
        "org/missions/D8/MDPF/MDPF_STRATID/deliverables/2.0.0_SA_COO~S1/FWD1_SEAT_WALK_GLOBAL_VIEW_20261009.md @1b5bc0d5c8",
        "ADJUDICATION_v2 row MDPF_STRATID-C-S4 @28203a2257"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  }
]
```
