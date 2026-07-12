# 14-Cohort DAILY AUM Tracking -- Capability Assessment + Build Plan

**Author:** 3.0.0_SA_CVO~A | **Date:** 2026-07-12 | **For:** Andrew (via 0.0.0_AB_MSTR RAVC)
**Assignment:** Andrew-direct -- assess our automated DAILY recording of 14 AUM cohorts + plan to make all 14
bullet-proof-daily BEFORE Manav's manual weekly tracker goes away.
**Sovereign clearance:** 49F/bd/Schwab ban LIFTED for CVO~A, THIS assessment only, **READ + PLAN only** (zero
writes/deploys). All grades grounded on LIVE/served artifacts + source (Rule 22a), cited. This plan SAYS what to
build; **building is a separate future authorization.**
**Orientation (Andrew framing 234238Z):** QUIET INTERNAL MUST-SOLVE. (1) NO external comms -- nobody was contacted
(not Manav, not any human); everything below is grounded on OUR pipelines/source/live artifacts/box config. (2) This
is a CONCRETE BUILD BLUEPRINT, not a survey: each gap carries **exactly what to build + which lane builds it + what
sovereign clearance it needs**, ready to execute on Andrew's go. The goal is actually-solved-and-bullet-proof, fast.

---

## 0. HEADLINE FINDINGS (the bullet-proof risks Andrew is worried about)

1. **The 49F block is NOT fresh-daily -- it is ROLLED-FORWARD-STALE since 2026-07-06.** The core daily rollup
   (`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json`) generates files ~daily, but the latest
   (`2026-07-10.json`, generated 07-10T14:53Z) carries `as_of_date=2026-07-06` with
   `rolled_forward_partners={49financial:2026-07-06}`, `source_vintage.status=BEHIND`. So all 7 49F cohorts' AUM is
   a roll-forward of 07-06, not a fresh daily record -- the BD-stale convergence-defer. Inflection is fresh (07-10).
2. **The SECOND Schwab master account 08335338 (Black Diamond) is NEVER pulled -- it appears in 0 of 21,153
   files.** The entire Schwab+BD ingest is hardcoded to master **08242234** (SmartX default). Any assets under
   08335338 are a **SILENT daily gap** -- unrecorded, unalarmed. This is the exact bullet-proof failure named.
3. **No single daily bucket.** The 14 cohorts + per-partner ETF ownership are FRAGMENTED across
   opal-data-portal-v2/mdpf, opal-data-etfs, the avgcap bd<->RPS recon, and schwab/bd silver. The convergence goal
   (ONE consistent daily bucket) is a real build, not a re-wire.
4. **Per-partner TRUE ETF ownership is half-persisted:** inflection's ETF holdings ARE in the daily served
   `etf_decomposition`; 49F's ETF ownership exists ONLY in the avgcap recon (a separate ETFS_AVGCAP surface), NOT
   folded into the daily aggregate.

---

## 1. WHAT WE HAVE -- per-cohort grade (grounded evidence)

Core artifact: MDPF `aggregate_aua/{date}.json` -- a convergence-gated daily per-partner-decomposed rollup
(feeders: WS-B 49F/SmartX model, WS-C Inflection, WS-D2 ETF net-assets, WS-E 49F non-model). Grade key: SOLID =
fresh daily record + artifact; PARTIAL = recorded but stale/gated/indirect; MISSING = no daily record.

| # | Cohort | Source-master / feeder | Daily record today? | Grade | Evidence |
|---|---|---|---|---|---|
| 1 | DIVZ (ETF) | opal-data-etfs + WS-D2 net-assets | fund net-assets DAILY (etf_history.csv 07-12) | **SOLID** (fund-level) | etf_decomposition DIVZ total_net_assets=274,962,771 @2026-07-10; opal-data-etfs/etf_history.csv mtime 07-12 18:00 |
| 2 | IDVZ (ETF) | same | DAILY net-assets | **SOLID** | etf_total_net_assets=176,926,387 |
| 3 | PFOE (ETF) | same | DAILY net-assets | **SOLID** | etf_total_net_assets=80,961,056 |
| 4 | PFDE (ETF) | same | DAILY net-assets | **SOLID** | etf_total_net_assets=145,541,570 |
| 5 | Dividend SMA | mdpf 49F by_model (cohort_class=sma) | via 49F block -> STALE 07-06 | **PARTIAL** | model_value=18,536,958.91, 40 accts; under rolled-forward 49financial |
| 6 | Opal Equity Growth SMA | mdpf 49F by_model (sma) | via 49F block -> STALE 07-06 | **PARTIAL** | model_value=4,843,817.65, 46 accts; rolled-forward |
| 7 | Inflection (Opal Models) | WS-C / advi-inf spine | FRESH 07-10 | **SOLID** | as_of_by_partner.inflection=2026-07-10; opal-data-inf/gold/meta/pipeline-complete.json 07-10T10:52 |
| 8 | 49F Schwab (custody) | 08242234 native + bd; **08335338 NOT pulled** | 08242234 stale 07-06; 08335338 = NONE | **PARTIAL + SILENT GAP** | 08242234 book fed; 08335338 = 0/21,153 files |
| 9 | 49F SMArtX (platform) | WS-B SmartX REST API (enterprises/allocations) | via 49F block -> STALE 07-06 | **PARTIAL** | model_aua=1,400,957,639; vendor-API dep (SmartX REST) |
| 10 | 49F Ultra ST | mdpf 49F by_model opal_ultra_short_term | STALE 07-06 | **PARTIAL** | model_value=46,369,894, 174 accts |
| 11 | 49F ST | opal_short_term | STALE 07-06 | **PARTIAL** | 107,829,750, 693 accts |
| 12 | 49F Intermediate | opal_intermediate | STALE 07-06 | **PARTIAL** | 292,752,737, 1592 accts |
| 13 | 49F LT Conservative | opal_long_term_conservative | STALE 07-06 | **PARTIAL** | 750,069,142, 3149 accts |
| 14 | 49F LT Aggressive | opal_long_term_aggressive | STALE 07-06 | **PARTIAL** | 203,936,115, 1386 accts |

**Tally: 5 SOLID (4 ETFs fund-level + Inflection) / 8 PARTIAL (all 49F-decomposition cohorts, stale via the 07-06
roll-forward) / 1 with a SILENT GAP (49F Schwab, the 08335338 portion).** The 8 PARTIALs are all a SINGLE root
cause: the 49F block is stale because the BD 49F feed is behind and the mdpf gate rolls it forward.

## 2. THE SCHWAB DUAL-MASTER-ACCOUNT ASSESSMENT (MSTR add)

**(a) Does the box/REST pull BOTH masters?** NO -- only **08242234** (SmartX). Grounded: `08335338` = 0 matches in
21,153 files (clearance-scoped comp-grep --include-held). The box probe (`infra/aws/ec2/canonical-schwab-si2/
schwab_sdd_probe.py`) CAN enumerate masters (`FetchDetails/UserMasters.aspx`) but the ingest is hardcoded 08242234:
`convert_schwab_trn_to_parquet.py DEFAULT_ACCOUNT='08242234'`, `sync_schwab_onedrive_to_s3.py default 08242234`, the
sdd-download/history box scripts (master 08242234), the RPS/xref universe (`schwab_master_account 0008242234`), the
49-schwab-conv ingest skill. **08335338 assets = a silent daily gap.**

**(b) 08335338 look-back / 2021 completeness?** Currently **ZERO** in our estate (not pulled). And even the CURRENT
master 08242234 only reaches **2024-04-12** in our estate (`convert_schwab_trn_to_parquet`: "496 TRN files covering
2024-04-12 -> 2026-04-20"). So the 2021-complete target for 08335338 is a **source-fetch question**: whether Schwab
SDD `DownloadHistory` serves 08335338 back to 2021 -- confirming that requires a LIVE Schwab SDD query (a vendor
egress, separately gated -- NOT done here). We hold 2021 data for NEITHER master today.

**(c) Cohort -> source-master map:** ETFs 1-4 -> opal-data-etfs/WS-D2 (fund-level, master-agnostic). Inflection ->
WS-C/advi-inf (not Schwab). 49F cohorts 8-14 + SMAs 5-6 -> **master 08242234** (SmartX REST for models via WS-B; bd
holdings + Schwab-RPS via 08242234 native ingest). **NO cohort currently maps to 08335338** -- which is precisely
why 08335338 assets are invisible: no cohort is defined against it.

## 3. PER-PARTNER TRUE ETF OWNERSHIP (ETFS + avgcap -- MSTR convergence add)

- **ETF net-assets (fund totals):** DAILY + SOLID. opal-data-etfs (daily/, etf_history.csv fresh 07-12) + WS-D2 ->
  mdpf etf_decomposition. Projects: ETFS_CANON (daily Dynamo), ETFS_NETAST (closed->WS-D), ETFS_SECIDX.
- **Per-partner ownership -- FRAGMENTED:** inflection's holdings of each ETF ARE resolved daily in the served
  etf_decomposition (`held_by_partner=[{inflection, held, ownership_pct}]`). **49F's ETF ownership is NOT** -- it
  lives only in **avgcap** (`data/etfs/scripts/gold/avgcap_bd_rps_recon.py`, ETFS_AVGCAP.W1): a bd<->Schwab-RPS
  account-level recon (RPS=number-of-record, bd lags ~4%), 49F universe = xref schwab_master 0008242234. It is a
  cross-check recon, NOT persisted into the daily aggregate. So DIVZ/IDVZ/PFOE/PFDE per-partner ownership is
  daily for inflection, and only-in-a-side-recon for 49F.

## 4. THE BUILD BLUEPRINT (per gap: EXACT build + owner lane + clearance)

| Gap | EXACTLY what to build | Owner lane | Clearance needed |
|---|---|---|---|
| **G1: 49F block stale -- 8 cohorts roll-forward from 07-06** (root cause of every 49F PARTIAL) | Diagnose the BD 49F feed lag (bd silver `allocations/{date}.parquet` alternates 46K/1.2M 07-07..07-10 -> stub/partial landings; the mdpf convergence gate `GATE_ENFORCE=1` defers on BD_MAX_LAG_TRADING_DAYS>2). FIX: make the 49F bd feed land a FULL fresh allocations parquet daily (kill the stub-alternation) so the gate stops rolling 49F forward. Verify: served `as_of_by_partner.49financial` advances to current. | **DS** (data/black_diamond bd silver feed) + **AE** (mdpf-daily-trigger convergence gate) | **49F/bd sovereign lift** (touches opal-data-bd + data/black_diamond) -- Andrew decision |
| **G2: Schwab master 08335338 never pulled (silent gap)** | Extend the box/REST ingest (`infra/aws/ec2/canonical-schwab-si2/schwab_sdd_probe.py` already lists masters via UserMasters.aspx) to ENUMERATE all session masters + PULL 08335338's RPS/TRN/ACC files; add 08335338 to `convert_schwab_trn_to_parquet`/`sync_schwab_onedrive_to_s3` (today hardcoded `DEFAULT_ACCOUNT='08242234'`); ingest to schwab/bd silver; DEFINE which cohort(s) 08335338 assets are (49F Schwab-BD custody). | **AE** (canonical-schwab-si2 box + the 49-schwab-conv ingest) | **49F/Schwab sovereign lift** (opal-data-schwab, opal-data-bd, the box) -- Andrew decision |
| **G3: 08335338 + 2021 look-back** | INTERNAL box-fetch (NOT a human ask): extend the box `sdd-history.ps1` (today DownloadHistory for 08242234) to pull 08335338's full DownloadHistory + backfill silver; the source-depth-to-2021 is answered by the SDD's own history response (a system read, not asking anyone). Note even 08242234 only holds 2024-04-12+ today, so 2021 depth is contingent on what SDD serves. | **AE** (box DownloadHistory + backfill) | 49F/Schwab lift **+ a vendor-egress authorization** for the Schwab SDD history calls (availability-is-not-authorization) |
| **G4: 49F per-partner ETF ownership not in the daily aggregate** | Fold `avgcap_bd_rps_recon` (49F ETF ownership, bd<->RPS) into the daily `mdpf_aggregate_aua.py` etf_decomposition so `held_by_partner` carries 49F alongside inflection -- a per-partner-per-ETF-per-day ownership row. | **DS** (mdpf gold `mdpf_aggregate_aua.py` + avgcap) | 49F-partial (reads bd/RPS silver -- clearance-scoped read; the daily persist writes Opal-side portal-v2, not bd) |
| **G5: no single daily bucket (the convergence)** | Promote the extended mdpf aggregate_aua to THE one daily artifact: add a custody dimension (both Schwab masters), the folded per-partner ETF ownership (G4), and one row per cohort. Served to the ModelPortfolios/AUM surface as the single source. | **DS** (mdpf gold emitter) + **AE** (served artifact + portal proxy) | Opal-side build; depends on G1-G4 DATA |
| **G6: per-cohort freshness stamp + alarm** | Emit `{cohort, source_master, value, as_of, state: fresh\|rolled_forward\|missing}` per cohort per day; add a per-cohort staleness alarm (today only partner-level roll-forward + one global `mdpf-freshness-checker`). Makes "49F LT Conservative stale since 07-06" a daily-visible per-cohort fact. | **DS** (emitter) + **AE** (CloudWatch alarm) | Opal-side build (no sovereign) |

## 5. THE PLAN + SEQUENCING (prioritized, actionable; 49F-gated flags explicit)

**BUILDABLE NOW (Opal-side, no sovereign decision):**
- **P0.1 -- per-cohort freshness stamp + the one-bucket skeleton (G5/G6).** Extend mdpf aggregate_aua to emit a
  per-cohort daily row with `{cohort, source_master, value, as_of, fresh|rolled_forward|missing}` -- so every one of
  the 14 (+ETF-ownership rows) has a visible daily state. This makes the CURRENT staleness (the 8 PARTIALs) LOUD
  per-cohort instead of hidden in a partner roll-forward. It is the skeleton of the one consistent bucket.
- **P0.2 -- fold 49F per-partner ETF ownership into the daily aggregate (G4).** avgcap already computes it; persist
  it daily into etf_decomposition.held_by_partner (49F alongside inflection). Reads bd/RPS (clearance-scoped);
  writing the daily persist is Opal-side (opal-data-portal-v2/mdpf), not a bd/schwab write.

**GATED ON A 49F/SCHWAB DECISION (Andrew must decide the sovereign pipelines are in-scope to touch):**
- **P1.1 -- unstick the 49F daily freshness (G1).** The single highest-leverage fix: it un-PARTIALs 8 of 14
  cohorts. Diagnose why bd silver allocations lag / alternate-size and why the mdpf gate rolls 49F forward from
  07-06; make the 49F feed land fresh daily. (This is the sovereign bd/RPS pipeline -- flagged.)
- **P1.2 -- pull the second Schwab master 08335338 (G2).** Add 08335338 to the box/REST enumeration + ingest;
  define which cohort(s) its assets belong to (49F Schwab-BD custody). Closes the silent gap.
- **P1.3 -- the 08335338 (and 2021) look-back (G3).** Live Schwab SDD DownloadHistory for 08335338 + backfill;
  requires a vendor-egress authorization + confirming SDD serves 2021.

**CONVERGENCE (the IDEAL, after P0+P1 data exists):**
- **P2 -- ONE consistent daily bucket.** Promote the extended mdpf aggregate_aua to the single daily artifact
  holding all 14 cohorts + per-partner ETF ownership + both Schwab masters, each with its own freshness stamp,
  served to the ModelPortfolios/AUM surface -- so Manav's manual weekly tracker can retire against a per-cohort
  daily-verified record.

## 6. THE FAST PATH TO BULLET-PROOF (must-solve) + the honest interim risk

**Fastest route to actually-solved:** the 8 PARTIALs collapse to ONE fix (G1 -- the 49F feed freshness) and the one
silent gap collapses to ONE fix (G2 -- pull 08335338). So the critical path is short:
1. **P0.1 (build NOW, Opal-side):** the per-cohort freshness stamp (G6) -- turns "is it bullet-proof?" from a manual
   audit into a daily-visible per-cohort fact, and is the skeleton of the one bucket. No sovereign clearance. Do first.
2. **G1 + G2 (on Andrew's go, with the 49F/bd + 49F/Schwab lift for the BUILDERS):** un-stale the 49F feed (un-PARTIALs
   8 of 14) and pull 08335338 (closes the silent gap). These two are the whole must-solve.
3. **G4/G5/G3 fold in:** per-partner ETF ownership -> the one daily bucket -> the 2021 look-back.
With G1+G2 done and P0.1 proving each of the 14 updates daily, all 14 are bullet-proof-daily.

**Honest interim risk (must be stated):** until G1+G2 land, 8 of 14 cohorts are recorded-but-stale (rolled forward
from 07-06) and the 08335338 assets are unrecorded. So TODAY the automated record is NOT yet a safe replacement for
the manual weekly backup -- the manual tracker is the safety net for exactly those gaps until they close. The
blueprint above is the fast, complete path to remove that dependency; it is ready to execute the moment Andrew gives
the go + the builder clearances.

*Grounded per-cohort on live/served artifacts + source (Rule 22a). READ+PLAN only -- no pipeline was modified. The
49F/bd/Schwab reads were under Andrew's scoped clearance for this assessment and do not extend beyond it.*
