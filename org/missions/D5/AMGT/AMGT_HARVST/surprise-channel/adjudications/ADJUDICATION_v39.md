# AMGT_HARVST -- CHANNEL HYGIENE (no round): closing two BLOCKING rows resolved on the record but never dispositioned

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~17:5xZ - **Source:** this seat's cross-round census,
`org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_Z_CHANNEL_CENSUS_ARMED_BLOCKING_20260930.md` (class B).

This seat wrote both rows as CARRIED in its tables at v36 and v37, but never disposed them in JSON, so the compile still read them
open.

| row | disposition | grounds |
|---|---|---|
| `Z-W70-S1` (BLOCKING: cached listing pages record no reach, so q-1 AC1 failed) | **GRADUATED** | Fixed by `aa-1` @`0df90b1535` ("a cached listing page records reach from its own dated hits"). aa-1's LAST `<status>` reads complete, and the replay reads wsj 2025-11-20..2026-09-23 where q-1 recorded none. |
| `Z-W78-S2` (BLOCKING: phase-A lib paths were granted in prose only) | **GRADUATED** | `<paths>` was fixed @`fcd217c797`. Phase A committed, and aa-3 phase B served `part-20260930T114206Z`, which this seat re-read at v37. |

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S49",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T17:50:00Z",
    "one_line": "Channel hygiene: Z-W70-S1 (fixed by aa-1 at 0df90b1535) and Z-W78-S2 (paths fixed at fcd217c797; phase B served) are resolved; graduated. This seat carried both in prose at v36/v37 without a JSON disposition.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log 0df90b1535: 'drain(AMGT_HARVST.TO-HVST-aa-1) ... a cached listing page records reach from its own da[ted hits]'; TO-HVST-aa-1 LAST <status> complete.",
        "git log fcd217c797: 'amend(AMGT_HARVST.TO-HVST-aa-3 AMENDMENT 2 paths ...)'; bloomberg/harvest/silver/article/date=2026-09-30/part-20260930T114206Z.parquet 11 rows (ADJUDICATION_v37)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W70-S1",
      "AMGT_HARVST-Z-W78-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Both rows blocked an order's criterion.",
    "world_is": "Both causes were fixed and the dependent acts completed.",
    "notes": "Class B of the 2026-09-30 census."
  }
]
```
