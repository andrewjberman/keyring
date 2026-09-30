# AMGT_CORPUS -- CHANNEL HYGIENE (no round): closing three gating rows resolved on the record but never dispositioned

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~17:5xZ - **Source:** this seat's cross-round census,
`org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_Z_CHANNEL_CENSUS_ARMED_BLOCKING_20260930.md` (class B).

`_latest_dispositions` read these three rows as UNDER_INVESTIGATION, although their resolution is committed. Each disposition below
cites the commit that resolved it.

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S19` (ARMED: z-1's premise "about 199 outside the band") | **DISMISSED_WITH_REASON** | An issuer premise error, not a hazard. The census read 37 outside the band and 450 zeros, and the issuer ruled it @`717cbb0a14`. z-1 drained against the measured population. Nothing remains to disarm. |
| `Z-W1-S20` (ARMED: a test pins the zero-dividend family UNRESOLVED) | **GRADUATED** | Ruled @`717cbb0a14`: the zero rule lives in `unit_from_basis_zero` via `build_entries`, not in `classify_unit`, so the pinned test and the family both hold. z-1 is complete, and its AC2 reads 38 passed. |
| `Z-W2-S17` (ARMED: y-5 AC4's superseded assertion) | **GRADUATED** | Ruled by AMENDMENT 2 @`bd28136864`. y-5 drained @`94301d5a9c` with AC4 reading 15 passed, and this seat's v26 census read 0 of 35,678 sign contradictions. |

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S28",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T17:50:00Z",
    "one_line": "Channel hygiene: Z-W1-S19 is an issuer premise error ruled at 717cbb0a14, not a hazard; dismissed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log 717cbb0a14: 'ruling(AMGT_CORPUS round 24, 2.0.0_SA_COO~X): Z-W1-S19 the order premise \"about 199 outside the band\" was the issuer's restatement miss'.",
        "_latest_dispositions(AMGT_CORPUS) read Z-W1-S19 UNDER_INVESTIGATION before this row."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S19"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An issuer premise error (a restated count), ruled at 717cbb0a14; the order drained against the measured population, so no hazard remains to disarm.",
    "spec_asserts": "Z-W1-S19 records z-1's premise count as wrong.",
    "world_is": "The premise was ruled and z-1 completed on the measured population.",
    "notes": "Class B of the 2026-09-30 census."
  },
  {
    "id": "AMGT_CORPUS-Z-C-S29",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T17:50:00Z",
    "one_line": "Channel hygiene: Z-W1-S20 (ruled at 717cbb0a14; z-1 complete) and Z-W2-S17 (ruled by AMENDMENT 2 at bd28136864; y-5 drained at 94301d5a9c) are resolved; graduated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log 717cbb0a14 (issuer ruling on Z-W1-S19/S20); TO-CRPS-z-1 LAST <status> complete.",
        "AMENDMENT 2 bd28136864; drain 94301d5a9c; ADJUDICATION_v26: 0 of 35,678 plain sign labels contradict their value."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S20",
      "AMGT_CORPUS-Z-W2-S17"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Both rows record a test assertion that conflicted with the ruled rule.",
    "world_is": "Both were ruled and the orders completed green.",
    "notes": "Class B of the 2026-09-30 census."
  }
]
```
