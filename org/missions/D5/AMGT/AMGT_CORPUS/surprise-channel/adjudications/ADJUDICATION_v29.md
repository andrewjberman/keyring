# AMGT_CORPUS -- CHANNEL HYGIENE: `Z-S3`'s disarm owner named (census class A)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~18:3xZ
**Source:**
- CTO~Z ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_Z_RULING_CLASS_A_DISARM_OWNERS_20260930.md` @`3febec7b85` (msg 27320),
  answering this seat's census @`470cd226e2`.

| row | disposition | grounds |
|---|---|---|
| `Z-S3` (ARMED: the L4 notifier and the overdue-half re-route) | **UNDER_INVESTIGATION**, disarm owner **`0.0.0_AB_MSTR~Z`** | The notifier rides the broker. `org/mcp/server.py` resolves to lane `D0_T1_BROKER`, which is `0.0.0_AB_MSTR`'s lane (on site Z, `~Z`). The row stays ARMED with a seat that can act, replacing "THE FABRIC". |

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S30",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T18:35:00Z",
    "one_line": "Census class A: Z-S3's disarm owner is 0.0.0_AB_MSTR~Z per CTO~Z ruling 3febec7b85 (the notifier rides the broker, lane D0_T1_BROKER); stays ARMED with a seat, replacing 'THE FABRIC'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CTO_Z_RULING_CLASS_A_DISARM_OWNERS_20260930.md @3febec7b85: 'AMGT_CORPUS Z-S3 ... disarm_owner 0.0.0_AB_MSTR~Z'; org/mcp/server.py resolves to lane D0_T1_BROKER."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S3"
    ],
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "0.0.0_AB_MSTR~Z",
    "spec_asserts": "Z-S3's disarm_owner reads 'THE FABRIC', which no seat can act as.",
    "world_is": "The CTO ruled the broker owner, 0.0.0_AB_MSTR~Z, the disarm owner.",
    "notes": "Census class A."
  }
]
```
