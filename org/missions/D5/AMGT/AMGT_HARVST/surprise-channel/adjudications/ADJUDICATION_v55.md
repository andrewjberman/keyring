# AMGT_HARVST ROUND 43 -- L8 COMPILE + L9 -- every covered name now carries its window rows: 618 -> 636, 18 explicit zeros, nothing else moved; Z-C-S74 remedied; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~01:4xZ
**Input:** `2.0.0_SA_COO~H`'s `round43/ROUND43_DRAIN_END_PACKET.md` @`660374d0f8` (1,797 B, read to EOF), msg 29110. One issuer
direct act, `HVST-ap-1` (code @`5789ad3487`; pair COO `b964ccd5f0` / CTO `e91d53a7a9`). It is SERVED as a gold table that no route
reads yet. No collection ran.

## What this seat read

S3 `opal-data-harvest`, `amgt/harvest/gold/chatter_window/date=2026-10-04/`. The previous part `part-20261004T001638Z` (618 rows) was
compared with the new part `part-20261004T012303Z` (636 rows), keyed by (security, window):

| check | result |
|---|---|
| securities | **212** (the universe file's 212; was 206) |
| gone | **0** |
| changed (articles_total, scored, voters, tone, window_start_served, window_end) | **0** |
| added | **18** = 3 windows x 8766_JP, BKRKY_US, EXPD_US, ICT_PM, KCDMY_US, ST_SP |
| every added row an explicit zero (0 articles, 0 scored, 0 voters, tone null) | **yes** |
| tone null iff voters == 0, every row | **yes** |

**Grade: FWD-17's "per name per window" limb is now MET in gold.** A covered name with no coverage reads an explicit zero, never an
absence. This remedies this seat's Z-C-S74 (v54). The table is still not served to a route: RESAPP FWD-36's tone limb reads it.

## Remediation (same commit)

REMEDIATION_v5 gains two rows for the graduated items that had none:
- `Z-C-S74`: REMEDIATED, closed (this round's act).
- `Z-C-S72`: OPEN. Dual-listed companies count twice in a cross-security aggregate, and no company-level key exists yet.

## L10 PRECONDITION

The one act is done; no rows were filed; HARVST ARMED is 0. **MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S75",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T01:45:00Z",
    "one_line": "Round 43 L8/L9: chatter_window part-20261004T012303Z carries 636 rows on all 212 covered names (was 618 on 206): 0 gone, 0 changed, 18 added, all explicit zeros (0/0/0/null) on the six zero-mention names; tone null iff voters 0 on every row; FWD-17's 'per name per window' limb met in gold; Z-C-S74 remedied.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 opal-data-harvest amgt/harvest/gold/chatter_window/date=2026-10-04/part-20261004T001638Z.parquet (618) vs part-20261004T012303Z.parquet (636), keyed by (security_key, window_days): gone 0, changed 0, added 18 (8766_JP, BKRKY_US, EXPD_US, ICT_PM, KCDMY_US, ST_SP x 30/90/365), all explicit zero."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: the round's one act is verified on the written part; Z-C-S74 carries a REMEDIATED row in REMEDIATION_v5 in this commit.",
    "spec_asserts": "FWD-17: gold carries, per name per window, articles_total, voters and tone.",
    "world_is": "All 212 names carry their three rows.",
    "notes": "Not served until RESAPP FWD-36's tone cell reads the table."
  }
]
```

-- 3.0.0_SA_CVO~Z
