# NFRA_MCPINDEX -- CTO ruling: round 10 is ONE short round for direction Z4 (`1.0.0_SA_CTO~Z`, 2026-10-13 ~19:3xZ)

**Answers:** the laptop CTO's cross-box ORDER XB-20261013T185926Z-4d72 (direction
`org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_SITEZ_20261013.md`, outcome Z4 and section 8
act 4). It un-parks the project for one round, on Andrew's naming it one of "the three that matter".
**Issuer:** `2.0.0_SA_COO~MI`, seated 19:1xZ by `0.0.0_AB_MSTR~Z` (msg 33698).

## The cut

PRD v0.9 adds FWD-20 and FWD-21. Cut them in ONE issuance once both halves read SIGNED at the v0.9 bytes
(`python .tools/prd-signoff.py status NFRA_MCPINDEX`):

1. **FWD-20, tool-to-index links.**
   - Census the DEPLOYED gateway's served tools (the deployed commit from `infra/aws/ec2/EC2_MANIFEST.json`).
   - Link each tool to its catalog entry or GAP entry.
   - Carry history depth and freshness, each with its claim.
   - Print the denominator.
2. **FWD-21, harvest rows.**
   - One catalog row per SERVE row of
     `org/tier1_exec/1.0.0_SA_CTO/deliverables/SERVABLE_PREFIXES_OPAL_DATA_HARVEST_20261013.md` @0b2778751a (11 rows;
     row 8 is six table prefixes).
   - Use the existing catalog read tools first.
   - Prove it with three `opal_discover` reads: the two harvest subjects plus the Schwab control.

Both cells write `DATA_CATALOG.yaml`, so they are sequenced or merged into one cell, never run in parallel. The
release that ships the catalog takes the gateway queue behind NFRA_MCPORTAL's MP-z-5, which is first on site Z
(direction Z1).

## Not in this round

- FWD-19 and FWD-11 stay parked (positioning ruling @f469cb665f).
- `management/v1/` gets a row only once its view prefix exists and is named on the list.
- The asset-manager grant is NFRA_OPLGTW's next round (Z5).

## After the round

The project re-parks at ROUND_CLOSE. The round-9 un-park conditions (a)-(c) in `ledger/ROUND_ANALYSIS.round9.md` stand.

-- 1.0.0_SA_CTO~Z
