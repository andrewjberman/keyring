# ANDREW-DIRECT 2026-10-14 ~18:3xZ -- 49F Black Diamond may be read from opal-data-bd; the target layout for BD and firm gold

**Recorded by:** 1.0.0_SA_CTO~Z, site Z terminal. **Projects:** NFRA_OPLGTW (FWD-22), NFRA_MCPINDEX (FWD-22).
**Amends:** `ANDREW_DIRECT_20261014_150xZ_CLIENT_DATA_ONLY_OPAL_DATA_ASSETS_VENDOR_SILVER.md` (opal-data-bd excluded "at this time").
**Context:** the CTO reported that 49F Black Diamond holdings and transactions exist only in `opal-data-bd`, so under the
silver-only rule 49F BD would be "not served".

## His words (verbatim)

> We can allow 49F Black Diamond pulls from opal-data-bd, you're right that's fine. Eventually that data and it's
> operations should all be in opal-data-assets, in LGIC_NAMING canonical path form agreeing with how everything else is
> structured for 49 in there, in essence the black diamond folder in opal-data-assets would have both Cottonwood and 49
> Financial data, then the eventual opal-data-49financial firm bucket would have the gold layers from Black Diamond for
> 49 as well as the gold layers from Schwab, both in canonical LGIC_NAMING path structure.

## What it decides (recorder's reading; the verbatim governs)

1. **Now:** the gateway's 49F Black Diamond client tools may read `s3://opal-data-bd/silver/` (49F only). Every other
   client source stays the `opal-data-assets` vendor silver folders.
2. **Target (eventually; not a gateway act):**
   - 49F Black Diamond data and its operations move into `opal-data-assets/blackdiamond/`, in LGIC_NAMING canonical path
     form. That folder then holds both Cottonwood and 49 Financial.
   - The firm bucket `opal-data-49financial` holds 49F's gold layers from Black Diamond and from Schwab, both in canonical
     LGIC_NAMING path structure.
   - This is a pipeline migration (rule 30 / R19: each existing pipeline reaches conformance through its own migration
     project). It touches dell1's firm-bucket work (ADVI_FIRMBKTS, P3), so it is relayed MSTR to MSTR.
