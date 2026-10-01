# AMGT_RESAPP -- CHANNEL HYGIENE (no round): closing one ARMED row superseded on the record but never dispositioned

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~17:5xZ - **Source:** this seat's cross-round census,
`org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_Z_CHANNEL_CENSUS_ARMED_BLOCKING_20260930.md` (class B).

| row | disposition | grounds |
|---|---|---|
| `Z-S314` (ARMED: any live `--rebuild-pool` regresses served `/thesis` sentences) | **GRADUATED** | `Z-S316` (CTO msg 27185) re-classified it. The dropped sentences are the verbatim gate's HOLD working as designed (`quoted_spans []`), and a live rebuild runs only under a signed pair. Only a manual invocation reaches it: 0 of 208 local scheduled tasks invoke it (this seat, v62). This seat wrote "superseded by Z-S316" at v63 without a JSON disposition. |

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S434",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T17:50:00Z",
    "one_line": "Channel hygiene: Z-S314 is superseded by Z-S316 (the HOLD is working as designed; a live rebuild runs only under a pair; 0 of 208 scheduled tasks invoke it); graduated. v63 said 'superseded' in prose only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AMGT_RESAPP-Z-S316 one_line: 'Correction of AMGT_RESAPP-Z-S314 and Z-S313 (CTO msg 27185): a D-1 regeneration dropping ASML's 8 served sentences is C-VERBATIM-GATE HOLD working as designed'.",
        "ADJUDICATION_v62: scheduled tasks scanned 208, actions matching rebuild-pool/draft 0."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S314"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Z-S314 records a live rebuild regressing served sentences as a defect.",
    "world_is": "Re-ruled as the gate's HOLD by design, and reachable only under a signed pair.",
    "notes": "Class B of the 2026-09-30 census."
  }
]
```
