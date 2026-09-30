# ETFS_RIVALS -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Home:** the project tree's channel. Lane `ANY`; `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.**

**Id grammar on this fabric:** a seat's row is `ETFS_RIVALS-Z-S<k>`; a worker's row is
`ETFS_RIVALS-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project":
"ETFS_RIVALS"` and `"fabric": "site-z"` on every new row. The CVO's adjudication rows live in
`adjudications/`, never here.

---

```json
[
  {
    "id": "ETFS_RIVALS-Z-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~RV",
    "surfaced_at": "2026-09-30T06:40Z",
    "one_line": "PRD v0.2 C-SHAPES says a GICS sector never stands in for a sub-asset class, but the ETF positioning vocabulary the PRD names as the classification source defines the equity sub_asset_class AS the GICS sector (a consumer-ratified mixed-source axis), so the two cannot both hold for an equity row once GICS arrives.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md @01e5499ae7, C-SHAPES classification bullet: 'A GICS sector never stands in for a sub-asset class'.",
        "Same PRD, PATHS: 'data/etfs/scripts/gold/etf_positioning_gold.py (the vocabulary)' is read, never edited.",
        "data/etfs/scripts/gold/etf_positioning_gold.py:150 `SUB_ASSET_CLASS_VOCAB = GICS_SECTORS + (CASH_SUB_ASSET_CLASS, ULTRA_SHORT_SUB_ASSET_CLASS)`; :158-160 comment 'sub_asset_class THE SERVED ALLOCATION AXIS. Deliberately MIXED-SOURCE -- the 11 GICS sectors PLUS ...'.",
        "data/etfs/scripts/gold/etf_positioning_gold.py:986-1010 classify(): a non-cash row with GICS sector in GICS_SECTORS returns (ASSET_CLASS_EQUITY, <the GICS sector>) as its sub_asset_class."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.2 C-SHAPES: canonical_shape carries Opal asset_class/sub_asset_class and the GICS hierarchy as separate fields, and a GICS sector never stands in for a sub-asset class; the vocabulary is etf_positioning_gold.py.",
    "world_is": "The named vocabulary's equity sub_asset_class values ARE the 11 GICS sector names, by a ratified design (1.0.0_SA_CTO~Z msg 11384); reusing it puts a GICS sector in sub_asset_class for every classified equity.",
    "notes": "Does NOT block round 1: the BASG thread has no GICS source (GICS is Bloomberg enrichment under R-21), so round 1 carries equity sub_asset_class as null with status UNRESOLVED and no GICS value, which satisfies both readings. It binds the enrichment round that lands GICS. Two readings, the CTO's to pick: (a) the PRD line means the GICS FIELD is never copied into sub_asset_class without the vocabulary's mapping, and the vocabulary's sector-valued sub-asset classes stand; (b) rivalfunds needs its own equity sub-asset vocabulary distinct from GICS, which is a new schema act with its Rule 24 record."
  }
]
```
