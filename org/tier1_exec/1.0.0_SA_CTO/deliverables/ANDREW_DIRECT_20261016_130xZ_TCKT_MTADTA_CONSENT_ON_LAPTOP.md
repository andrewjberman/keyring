# ANDREW_DIRECT 2026-10-16 ~13:0xZ -- the TCKT_MTADTA app consent is done on the laptop box

**Channel:** the dell1 `1.0.0_SA_CTO~DELL1` terminal, after this seat gave him the PowerShell steps. Recorded by `1.0.0_SA_CTO~DELL1`, same
turn.

## His words, VERBATIM

> send this over to laptop MSTR and CTO, it needs to be done on that box

## What it settles

- **Where:** call `dell1-20261016T090558Z-d9cb` (register the collector app and grant `ActivityFeed.Read` admin consent) is run on the laptop.
  The steps and the card were relayed to `0.0.0_AB_MSTR` and `1.0.0_SA_CTO` (laptop) through `0.0.0_AB_MSTR~DELL1`. The card and
  `register_app.py` are on origin/CLOUD.
- **What is unchanged:**
  - the act is his consent;
  - the secret goes straight to `m365-metadata/trino/api-credentials`, not through a seat;
  - the rest of round 2 runs on dell1 under `2.0.0_SA_COO~S1`.
- **The return path:** the laptop reports "consented" plus the client id to this seat. The call closes on that report.

-- 1.0.0_SA_CTO~DELL1
