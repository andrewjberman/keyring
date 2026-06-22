# CVO Research Brief -> CTO: ETFS macro / ETFS_AVGCAP (PRD-enabling)

**Author:** 3.0.0_SA_CVO | **Date:** 2026-06-22 | **For:** 1.0.0_SA_CTO (PRD generation) | **Origin:** Andrew-direct
**Status:** research/grounding only -- CVO does NOT author the PRD (CTO's lane) or any code. Every number is read from
the LIVE artifact. **v2 -- corrects a v1 Schwab artifact-selection error (ULN vs RPS), caught by Andrew; see Sec 3.**

---

## 1. The ask (scope-lock)

Track, **per Opal ETF, per partner, per month, the monthly AVERAGE ownership VALUE** -- the dollar market value of the
partner's client book held in each Opal ETF, averaged across the month.
- **Opal ETFs (4):** DIVZ, IDVZ, PFDE, PFOE.
- **Partners (3):** 49 Financial, Inflection Wealth Management, Cottonwood Capital Advisors.
- **Three deliverables in order:** (1) AVERAGING METHODOLOGY; (2) MAY numbers; (3) JUNE-MTD numbers.
- "Ownership value" = sum of position market value across the partner's accounts holding the ETF, per day, averaged over the month. It is AUM the partner has placed in Opal's funds.

---

## 2. Source map (VERIFIED live -- the spine)

Each partner has an Andrew-named authoritative source; all 4 ETFs confirmed present at `ticker + market_value + date + account` grain:

| Partner | Authoritative source | Bucket | **Holdings artifact** | Cadence | Coverage (live) |
|---|---|---|---|---|---|
| **49 Financial** | Schwab **full positions (RPS/BDRECPOS)** | `opal-data-schwab` | raw `bronze/rps/CRS{date}.RPS` -> silver `silver/RPS/` (**built by `/49-schwab-conv` RPS converter; silver/RPS currently EMPTY**) | daily-dated files, **monthly manual batch** (Andrew downloads -> AE converts) | raw bronze -> **2026-06-09**; silver/RPS **not yet populated** |
| **Inflection** | Orion holdings | `opal-data-inf` | `gold/holdings/{date}.parquet` | **daily** (Orion REST) | 2019 -> **2026-06-18** (clock starts 05-15, Sec 4) |
| **Cottonwood** | Black Diamond holdings | `opal-data-cot` | `gold/canonical/holdings/{date}.parquet` | daily | 2026-04-22 -> **2026-06-09** (FROZEN -- COTETL CurrentDay bug) |

**Live 4-ETF confirmation (firm-total market value):**
- **49F (Schwab RPS, 2026-05-08): $529.9M** -- DIVZ $163.5M / IDVZ $146.2M / PFDE $118.8M / PFOE $101.4M, ~5,245 accounts. (RPS parsed directly from the raw BDRECPOS feed; this is the AUTHORITATIVE number -- see Sec 3.)
- Inflection (inf gold/holdings, 06-18): $82.1M -- DIVZ $29.3M / IDVZ $23.1M / PFDE $18.7M / PFOE $11.0M.
- Cottonwood (cot gold/canonical/holdings, 06-09): $0.19M -- small/new book, 8 positions.

**Naming reconciliation:** `opal-data-bd` ("Black Diamond" pipeline, firm_id=49financial) and `opal-data-schwab` are TWO feeds of 49F's data -- BD (portfolio system) vs Schwab (custodian). Andrew picked Schwab. `opal-data-cot` is Cottonwood, also BD-sourced (`/blackdiamond/`). Distinct firm trees, never crossed (Sec 6).

### 2b. Canonical source-of-record + lineage (Andrew: "understand the canonical places we draw from")

| Partner | Canonical positions artifact | Producer / lineage | Estate-modeled? |
|---|---|---|---|
| **49 Financial** | Schwab **RPS/BDRECPOS** -- raw `bronze/rps/CRS{date}.RPS` (record-of-record) -> `silver/RPS/` (intended canonical, **EMPTY**) | manual monthly download -> **`/49-schwab-conv`** (AE) 5-table convert (ACC/**RPS**/TRN/ULN/RLD) | **UNDER-MODELED** -- pipescript threads only Schwab *transactions* + *unrealized-gains*; the full *positions* (RPS -> silver/RPS) is NOT a graphed producer->served thread. **PRD must build + register `silver/RPS` as the canonical 49F positions source.** |
| **Inflection** | Orion `gold/holdings/{date}.parquet` | `inf-api-positions` (cron) -> bronze -> `inf-silver-aggregator` (positions_daily) -> inf-gold chain | well-modeled (advi-inf thread) |
| **Cottonwood** | BD `gold/canonical/holdings/{date}.parquet` | `cot-bd-session-trigger` 4-phase (BD session -> bronze -> silver -> gold, B-holdings tier) | well-modeled (advi-cot thread) |

Inflection + Cottonwood have clean canonical `gold/holdings` artifacts with modeled producers. **49F's canonical positions source is THE gap** -- Schwab RPS lands raw in `bronze/rps` but `silver/RPS` is unbuilt and the positions path is not threaded in the estate graph. Canonicalizing 49F (build + register `silver/RPS`) is a P2 prerequisite, and is the concrete answer to "where do we draw 49F from": the Schwab BDRECPOS positions feed, not ULN (unrealized) and not bd (the lagging cross-check).

---

## 3. Schwab artifact correction + the REAL bd<->Schwab reconciliation (Andrew-caught)

**v1 ERROR (corrected):** v1 used `silver/ULN` for 49F and reported a ~1.85x "bd-vs-Schwab divergence." Andrew challenged it ("you are not looking at the correct fields for Schwab"). He was right: **`silver/ULN` is the UNREALIZED tax-lot file (`.ULN`), a ~half SUBSET of positions** (it carries only lots with cost-basis/unrealized-G/L detail; ~1,758 fewer accounts -- IRA/retirement positions absent). It was the only POPULATED positions-like silver table, because **`silver/RPS` -- the actual full-positions table -- is empty.**

**AUTHORITATIVE ground-truth (2026-05-08, 4 Opal ETFs), parsed direct from the raw Schwab feeds:**

| Source | 4-ETF total | DIVZ shares | What it is |
|---|---|---|---|
| **Schwab RPS / BDRECPOS** | **$529.9M** | 4.42M | **FULL positions feed (CORRECT)** -- `H1\|...\|49 WEALTH MANAGEMENT LLC\|...\|BDRECPOS`, D1 position rows, 0 material intra-file dups |
| bd canonical/holdings | $508.6M | 4.26M | ~96% of RPS -- bd is ~4% LOW, consistent with "BD lags Schwab" |
| silver/ULN (v1 error) | $274.2M | 2.27M | unrealized-lot SUBSET -- NOT total ownership |

**Completeness NAILED via the RPS control trailer:** the file's `T1` trailer self-reports **92,848 data records**; my parse captured D1(85,950)+D2(6,898) = 92,848 EXACTLY (+6 header/control rows = 92,854, the 2nd control). Ingest is COMPLETE -- no truncation, no double-count. The 4 Opal ETFs ($529.9M) = ~33% of 49F's total Schwab book ($1.59B D1 grand-total market value) -- a sane captive-fund share.

**So the apparent "2x" was an artifact-selection error, not a real divergence.** Resolving Andrew's two notes:
- "BD lags Schwab significantly" (msg-3) -> CORRECT direction: on the same date bd ($508.6M) is ~4% BELOW the true full Schwab (RPS $529.9M); bd lags/misses ~149 accounts. (The "significant" lag is largely TEMPORAL -- bd's freshness lag -- more than this same-date magnitude.)
- "274M is ~truth; bd doubles" (msg-4) -> OVERTURNED by ground-truth: true 49F = ~$530M (RPS), bd is ~right (slightly low), and $274M (ULN) is the undercount. bd is NOT double-counting.

**The reconciliation Andrew wants is still valid but small-magnitude now:** account-level classify **Schwab RPS vs bd** (in-both / BD-only / Schwab-only) via `opal-data-schwab/03_silver/account_xref/` -> surface any genuine "pre-existing at BD, not tracked by Schwab" positions AND explain the ~4% net gap (bd lag / missing accounts). Use **Schwab RPS as 49F's number-of-record**; bd is the cross-check.

---

## 4. Methodology (the "first task") + per-source cross-reference

All three sources are **daily** at the position grain, so a true daily average within a month is feasible. (49F's daily RPS values are directly computable from `bronze/rps` -- proven by the Sec-3 parse.)

**Recommended baseline:** for each (partner, ETF, month): `avg = mean over the month's days D of [ sum over accounts of market_value(ETF, D) ]`.

**Open methodology decisions (PRD must settle):**
1. **Day basis:** trading-day-mean vs calendar-day with last-known carry-forward over weekends/holidays. (Changes the denominator -- a real choice.)
2. **Partial-month handling:** average over AVAILABLE days + LABEL partial. Three partial cases now: Inflection May (05-15 start), 49F June (raw only to 06-09 + next download), Cottonwood June (post-freeze). Decide report-partial vs hold-until-complete.
3. **Inflection start -- PINNED 2026-05-15.** Orion positions backfill to 2019, but the Eclipse pull (`silver/eclipse/`+`bronze/eclipse/`) STARTS 2026-05-15 = onboarding. Clock = 05-15; May is partial (05-15..05-31). Pre-2026 history is out-of-clock per Andrew.
4. **Rollups:** per-ETF (spec) + optional per-partner-total + per-ETF-all-partners.
5. **Value basis:** end-of-day `market_value` (price x units), already in all sources.

**Per-source cross-reference / validation (Andrew-direct):**
- **49F:** Schwab RPS = number-of-record; **bd = cross-check** (the Sec-3 reconciliation surfaces BD-only + bounds confidence).
- **Inflection:** cross-reference via **Eclipse model-data** (Andrew: "the easiest way"). `silver/eclipse/{date}/portfolios_simple.parquet` maps `account_id -> model_id -> sleeve_portfolio` (845 portfolios @ 06-21). Method: which Eclipse MODELS hold the Opal ETFs (model target holdings) -> which accounts are on them -> reconcile model-EXPECTED exposure vs ACTUAL Orion positions. (Pin the model->target-holdings artifact in `silver/eclipse/`; `portfolios_simple` is the account->model half.)
- **Cottonwood:** (post-freeze) BD holdings only; same bd-schema -- a bd<->Schwab reconciliation may apply IF Cottonwood also custodies at Schwab. Out of scope until unfreeze.

---

## 5. Deliverable readiness (methodology / May / June-MTD) -- per partner

| | 49 Financial (Schwab RPS) | Inflection (Orion) | Cottonwood (BD) |
|---|---|---|---|
| **(2) MAY** | **Data EXISTS** in `bronze/rps` (all May daily files) -- directly parseable now (proven). Production needs `silver/RPS` populated via `/49-schwab-conv`. | **READY (partial):** full May present; clock from 05-15 => partial-month avg. | not required for May |
| **(3) JUNE-MTD** | **Partial + pending batch:** `bronze/rps` -> 06-09 only (monthly cadence); 06-10..present land at the next Schwab download (~early July). `silver/RPS` build needed. So 49F June-full ~early July. | **READY:** daily through 06-18; June-MTD now. | **BLOCKED:** frozen 06-09 (CurrentDay bug, ~$24M/6.5% AUA understatement). AE diagnosed fix (CurrentDay->Custom); cot June rides it. Needed by **July 1**. |

**Blockers for the PRD:**
- **B1 (49F, NEW framing):** `silver/RPS` is EMPTY -- the RPS converter (`/49-schwab-conv` step 3, AE-owned) must populate it from `bronze/rps`. This is the real "silver gap" (v1 mis-named it as a ULN gap). Raw RPS exists through 06-09. Gates the productionized 49F leg (one-off May numbers parseable from bronze now).
- **B2 (49F):** Schwab ingest is a MANUAL monthly batch (Andrew downloads -> `/49-schwab-conv`); latest 06-09. June-full 49F gates on the next download (~early July, aligning with the July-1 Cottonwood need).
- **B3 (Cottonwood):** COTETL freeze at 06-09 (CurrentDay fix in flight, AE). Gates cot June.

**Sequencing:** Inflection is build-ready now; 49F-May is computable now (bronze RPS) + needs silver/RPS for production; 49F-June + Cottonwood-June both converge ~early July (the July-1 window). A full 3-partner June view is an early-July artifact; methodology + May + Inflection-June proceed immediately.

---

## 6. Architecture & governance constraints (shape the PRD)

1. **NEVER cross firm buckets (CLAUDE.md NEVER #1 -- gate + IAM Deny).** ETFS_AVGCAP CANNOT single-query-join `opal-data-schwab` + `opal-data-inf` + `opal-data-cot`. Required shape: per-partner monthly-average computed WITHIN each pipeline/bucket, then published to a NEW deliberately-IAM'd **ETFS aggregation location** (new macro bucket, e.g. `opal-data-etfs`) that assembles the cross-partner view. The cross-firm aggregation is the one audited multi-source-read exception -- design its IAM explicitly, not as a bucket cross-reference inside a firm tree.
2. **New macro ETFS + project ETFS_AVGCAP:** `org/projects/ETFS_AVGCAP.json` with a **`prds` ARRAY** (`[{path,label,date}]`, NOT just the singular `prd` string -- /prd-check silently skips prd-string-only projects) + REGISTRY.md row + macro registration. PRD in `docs/architecture/`.
3. **Lanes:** DS = per-partner averaging scripts + the RPS-silver build logic; **AE = the Schwab ingest/`/49-schwab-conv` + new ETFS bucket + cross-firm-read IAM + the COTETL fix**; DE = portal surface only if wanted. CTO architects; COO decomposes.
4. **Validate on scheduled/batch artifacts, never ad-hoc gold runs.** Read the existing served/converted holdings; don't trigger pulls.
5. **Shared ETF-universe config** ({DIVZ,IDVZ,PFDE,PFOE}) -- one config across the 3 legs, not hardcoded x3.

---

## 7. Open decisions for the PRD (for CTO/Andrew)

- D1. Day basis: trading-day-mean vs calendar-day carry-forward. (4.1)
- D2. Partial-month: report-partial vs hold-until-complete. (4.2)
- D3. Inflection clock = 2026-05-15 (recommend; confirm). (4.3)
- D4. Rollups: per-ETF only vs + partner-total + per-ETF-all-partners. (4.4)
- D5. ETFS aggregation home + IAM (new `opal-data-etfs` + audited cross-firm reader). (6.1)
- D6. 49F: productionize `silver/RPS` (run `/49-schwab-conv` RPS converter) + confirm the Schwab monthly-download SLA. (B1/B2)
- D7. bd<->Schwab(RPS) account-level reconciliation -- surface BD-only + explain the ~4% gap. Separate TO? (Sec 3)
- D8. Output surface: data-only vs portal view. (6.3)

---

## 8. CVO bottom line

The metric is **fully supported** -- all 4 ETFs present in all 3 partners' authoritative sources at the right grain;
all 3 daily; true monthly-average feasible. The **central correction (v2):** 49F's source is the Schwab **RPS/BDRECPOS
full-positions feed** ($529.9M @ 05-08), NOT the `silver/ULN` unrealized-lot subset ($274.2M) I first used -- and at the
full-position grain **bd ($508.6M) approximately MATCHES Schwab** (bd ~4% low = lags), so there is no 2x bd double-count;
the apparent divergence was my artifact-selection error, caught by Andrew. The build is gated by THREE structural items
the PRD must absorb: (a) **`silver/RPS` is empty** -> run the AE-owned `/49-schwab-conv` RPS converter (raw exists to
06-09); (b) **Cottonwood freeze** (fix in flight); (c) the **no-cross-firm-bucket rule** -> per-partner-compute ->
ETFS-aggregate. Inflection is build-ready now; 49F-May computable from bronze now; 49F-June + Cottonwood-June converge on
~July-1. Recommend phasing: **P1** methodology + ETFS aggregation skeleton + Inflection leg (provable now) + the
bd<->RPS reconciliation -> **P2** 49F via silver/RPS -> **P3** Cottonwood post-freeze-fix, with May + June-MTD as the
P2/P3 acceptance artifacts.

-- 3.0.0_SA_CVO
