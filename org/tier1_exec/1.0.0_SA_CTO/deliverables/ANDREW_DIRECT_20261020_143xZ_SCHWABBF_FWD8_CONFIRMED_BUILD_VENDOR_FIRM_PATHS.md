# ANDREW-DIRECT 2026-10-20 ~14:3xZ -- NFRA_SCHWABBF: FWD-8 confirmed; co-sign and build; Schwab lands under vendor/firm paths

Given at the laptop 1.0.0_SA_CTO terminal, answering the v0.2 summary. VERBATIM:

> "thats fine, get this cosigned and then let's get it built. this should be pulling into opal-data-assets in LGIC NAMING path standards,
> abiding by the path structure that already exists in that bucket. it should be very easy its just schwab vendor and 49 firm for the 0840
> and cottonwood firm for the various master accounts"

## What it settles

1. **FWD-8 is CONFIRMED** ("thats fine").
2. **Go:** co-sign (the CVO's ratified-text half), then build.
3. **Path form: vendor, then FIRM.** Measured with the builder at ~14:3xZ: `address('schwab','49financial','bronze','acc','date=...')` returns
   `s3://opal-data-assets/schwab/49financial/bronze/acc/date=...`, and `cottonwood` returns `.../schwab/cottonwood/...`. That is the
   bucket's existing vendor/firm shape (`blackdiamond/49financial/`, `blackdiamond/cottonwood/`, `orion/inflection/`). The firm for each
   master comes from its scope row: 0824, 0833 and 0840 are `49financial`, and the four Cottonwood masters are `cottonwood`. PRD v0.3
   C-KEYFORM carries it.

-- 1.0.0_SA_CTO (laptop)
