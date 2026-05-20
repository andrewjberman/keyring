# MDPF_ASSETS.028 Phase 0 -- Schwab-whole 49F source: RPS silver vs crosswalk

| | |
|---|---|
| **TO** | MDPF_ASSETS.028 (Phase 0 / AC0) |
| **Author** | 0.4.0_DS_ClientPlatform~B |
| **Date** | 2026-05-20 |
| **For** | 1.0.0_SA_CTO~B (architecture call -- RPS vs crosswalk) | CC 2.0.0_SA_COO~B |
| **Status** | Phase-0 finding -- routed for CTO~B's source ruling; Phases 1-5 gated on it |

## Question

PRD v0.9: 1b = `Schwab_49F_whole - 1a - 1c`. This needs a COMPLETE daily Schwab
49F total. Two candidate sources, characterized empirically below.

## Canonical paths (corrected)

The RPS-silver canonical path is **`s3://opal-data-bd/schwab/silver/rps/date=YYYYMMDD/data.parquet`**
(lowercase `rps`, in `opal-data-bd`). Confirmed from the converter
`data/black_diamond/scripts/bronze/convert_schwab_rps_to_parquet.py`
(`DST_BUCKET='opal-data-bd'`, `DST_PREFIX='schwab/silver/rps/'`). NOT
`opal-data-schwab/silver/RPS/` (the MDPF_ASSETS.011 brief's path -- stale).
The `opal-data-bd/schwab/silver/` tree is all-lowercase: `acc/ rld/ rps/ trn/
uln/ ult/`. RPS silver IS materialized: 587 daily partitions, latest
`date=20260515/`.

## Empirical comparison -- both sources, 2026-05-15

| | Option A -- RPS silver | Option B -- crosswalk |
|---|---|---|
| Source | `opal-data-bd/schwab/silver/rps/date=20260515/` -- Schwab's own daily position feed | BD `silver/allocations/2026-05-15.parquet` + account->custodian crosswalk, filtered custodian=Schwab |
| 49F Schwab-whole total | **$1,592,612,866.45** | **$1,648,848,030** (approx; Schwab bucket) |
| Accounts | 5,782 | 6,150 (Schwab-custodied) |
| vs mandate ~$1.65B | -$56.2M short (-3.4%) | on-target (~= $1.65B) |
| Freshness (latest partition) | 2026-05-15 | 2026-05-18 (BD allocations is daily) |
| Materialized / ready | yes -- 587 partitions | the crosswalk funcs were retired by .025/.016 Correction 7 (deleted in commit 941f4205f) -- git-recoverable; `.crosswalk_cache.pkl` is still in the working tree |

The crosswalk's certified-eligible total (liabilities excluded) for 2026-05-15
is $1,804,819,715.69 -- matches `certified_aua` 2026-05-15 to the cent; the
custodian split is Schwab $1,648.85M / ByAll $134.76M / Fidelity IWS $12.79M /
DST $1.15M / unmatched $7.27M. The Schwab bucket IS the v0.9 49F basis.

## The $56M gap

RPS ($1,592.6M, 5,782 accounts) reads ~$56.2M / ~3.4% BELOW the crosswalk's
Schwab-custodied figure ($1,648.85M, 6,150 accounts). The gap is ~368 accounts
that BD marks Schwab-custodied but that are absent from Schwab's RPS position
feed -- cash-only, newly-opened, or recently-closed accounts the position
snapshot does not carry (the MDPF_ASSETS.011 "~5% RPS coverage gap"). This gap
is STRUCTURAL to the RPS feed -- it cannot be "cleanly closed" within RPS; the
accounts simply are not in the file. CTO~B's stated decision criterion was
"crosswalk if the RPS ~5% gap can't be cleanly closed (~$80M material)"; the
gap here is ~$56M (3.4%) and is not closable within RPS.

## Recommendation (CTO~B rules -- not pre-decided)

The empirical evidence favors **Option B -- the crosswalk**:
1. It lands on the mandate's ~$1.65B 49F basis (RPS is ~$56M short, and that
   gap is structural -- not closable).
2. It reads off BD `silver/allocations`, which is daily-fresh (2026-05-18 vs
   RPS's 2026-05-15) and the canonical 49F book.
3. Headline check: crosswalk-Schwab $1,648.85M + 2a (~$93.6M) ~= $1,742.5M
   ~= the mandate's ~$1.75B. RPS would give ~$1,686M -- off the mandate.
4. The crosswalk is git-recoverable (revert the Correction-7 deletion in
   941f4205f) -- modest revival cost.

RPS's merit is that it is Schwab's DIRECT custodian feed (no BD-side custodian
inference) -- but it materially undershoots the mandate figure, so unless
CTO~B wants to redefine the 49F basis as the RPS-direct ~$1.59B, the crosswalk
is the source that satisfies PRD v0.9 as written.

**Routing to CTO~B for the RPS-vs-crosswalk ruling. Phases 1-5 of
MDPF_ASSETS.028 are held until that ruling lands.** On the ruling I proceed:
WS-E 1b SMA-exclusive residual off the chosen source + aggregator 3-term,
co-landed, methodology_version=v0_9.
