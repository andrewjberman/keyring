# ANDREW-DIRECT 2026-08-05 -- THE CANONICAL MEDALLION FORM (estate-wide), + Phase-0 vertical 2 ratified

**Channel:** `1.0.0_SA_CTO~B` terminal, direct, during the Phase-0 one-at-a-time ratification sitting.

## VERBATIM (unedited -- the phrasing IS the ruling)

> "Yes this is a correct understanding regarding advi-cot. Permanent. Also should be coming from
> opal-data-assets/blackdiamond/. Something that should be made clear in these references is that
> data pipelines have a bronze (raw vendor) -> silver (parquet queryable) -> gold (various type
> processed analytics) structure. All assets will be housed in opal-data-assets. Serving layer will
> exist in opal-data-portal-v2/platinum. This is the canonical form we are building toward."

## 1. RATIFICATION: `advi-cot` = **PERMANENT** (Phase-0 vertical 2 of 29)

Source corrected: Cottonwood Advisor Intelligence comes from **`s3://opal-data-assets/blackdiamond/cottonwood/`**
-- the BLACK DIAMOND vendor tree, not a Schwab account. (49F's Black Diamond sibling is
`s3://opal-data-assets/blackdiamond/49f/`.) Ground-read, both verified below.

## 2. THE CANONICAL FORM -- FOUR TIERS, TWO BUCKETS

| Tier | Home | Andrew's definition, VERBATIM |
|---|---|---|
| **bronze** | `opal-data-assets/{vendor}/{firm}/bronze/` | "raw vendor" |
| **silver** | `.../silver/` | "parquet queryable" |
| **gold** | `.../gold/` | "various type processed analytics" |
| **platinum** | **`opal-data-portal-v2/platinum/`** | "Serving layer" |

**"All assets will be housed in opal-data-assets."** One asset bucket; the serving layer is the
ONLY thing that lives outside it, and it lives in `opal-data-portal-v2/platinum`.

**THIS IS A TARGET, STATED AS ONE: *"the canonical form we are building toward."*** It is not a
description of the estate today, and must never be cited as one. The measured deltas are in §4.

### Relationship to existing law -- this ADDS the fourth tier
CLAUDE.md Rules 17 / 17a already legislate the first three and AGREE with his definitions:
17a "BRONZE IS RAW AND UNTOUCHED ... PARQUET IS A *SILVER* FORMAT"; 17 "Silver = dedup + dtype
standardization ONLY"; gold carries the business logic. **What this ruling adds is PLATINUM as the
named SERVING tier with a named home** -- the tier CLAUDE.md's medallion rules do not currently
mention. The layer-purity principle of 17a ("each layer has exactly one job; doing a later layer's
job early is IRREVERSIBLE") extends to it: serving concerns belong in platinum, not in gold.

## 3. GROUND-READ (2026-08-05, `aws s3 ls`, not recollection)

```
s3://opal-data-assets/                    _probe/ blackdiamond/ code/ eclipse/ gold/ json/
                                          orion/ pathfinder/ portal/ schwab/ smartx/ trueshares/
s3://opal-data-assets/blackdiamond/       49f/  cottonwood/
      .../blackdiamond/cottonwood/        bronze/ gold/ meta/ silver/          <- CONFORMS
      .../blackdiamond/49f/               _ops/ bronze/ gold/ meta/ silver/    <- CONFORMS
      .../schwab/08335338/  (ADVI)        _ops/ bronze/ gold/ meta/ silver/    <- CONFORMS
      .../schwab/08242234/  (MDPF)        _ops/ bronze/ meta/ silver/          <- no gold/
s3://opal-data-portal-v2/platinum/        EXISTS
```

## 4. DELTA: WHERE THE ESTATE IS NOT YET CANONICAL (measured, not inferred)

**(a) `opal-data-assets` carries top-level prefixes outside the `{vendor}/{firm}/{medallion}` grammar:**
`gold/`, `json/`, `portal/`, `code/`, `_probe/`. A top-level `gold/` is a medallion tier hoisted to
where a VENDOR name belongs -- two different grains on one axis (Rule 24, same-grain postulate).

**(b) THE SERVING LAYER IS NOT CONSOLIDATED. `platinum/` exists, but as ONE OF ~25 SIBLINGS** in
`opal-data-portal-v2`: `json/`, `json-tiered/`, `metrics/`, `macro/`, `returns/`, `sentiment/`,
`valuation/`, `positioning/`, `portfolio-management/`, `benchmarks/`, `canon/`, `raw/`, `cache/`,
`assets/`, `metadata/`, ... **So "serving layer will exist in platinum" is the target; today serving
is spread across the bucket root.** This is consistent with -- and explains -- the PARKED
`json/mdpf/*` teardown. ⛔ Standing caution preserved: hyphenated `account-distribution.json` is a
LIVE SERVED PORTAL BELL; nothing in this ruling licenses treating any root-level serving key as
abandoned. **The direction is ratified; the migration is not authorized by it.**

**(c) `schwab/08242234/` (MDPF) has no `gold/`.** Incomplete against the four-tier shape rather than
violating it -- recorded as an observation, not a finding, since a tier that has not been built is
not the same as one built in the wrong place.

## 5. WHY THIS MATTERS TO THE KIMI PIPELINE SPECIFICALLY

v3's flow is a VERTICAL JOIN: every changed path resolves to its c3.ii vertical. A canonical
`{vendor}/{firm}/{tier}` grammar makes that join derivable from the path itself for conforming
trees; the §4 residue is exactly what would land in `unanchored`. **The canonical form is therefore
not just storage hygiene -- it is the substrate that makes the vertical join computable.** Folding
into the v3 design as an input; NOT re-opening the design on it.

## Routing
Recorded here (durable, this seat's author line) and BROADCAST same turn to `2.0.0_SA_COO`,
`1.0.0_SA_CTO`, `0.0.0_AB_MSTR`, `3.0.0_SA_CVO` per the `org/XXX.md` Andrew-direct law. This is an
estate-wide architectural ruling, not a Kimi-local one -- it binds DS/AE/DT lanes and belongs in
CLAUDE.md's deployment rules as the platinum tier. **Routing the CLAUDE.md edit to base
`1.0.0_SA_CTO` (law-file owner) rather than editing it from this seat.**
