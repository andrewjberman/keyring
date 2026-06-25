# ETFS — CANONICAL OUTPUT + CHARTS DESIGN v0.1 (daily row-store + the marquis monthly)

**Author:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-25 | **archetype:** EXPLORE
**For:** Andrew (design review) → 1.0.0_SA_CTO (design-gate) → DE/DS/AE build | **cc:** 2.0.0_SA_COO, 3.0.0_SA_CVO, 0.5.0, 0.4.0_DS
**Builds on:** the live ETFS pipeline (`opal-data-etfs` daily/monthly) + `etf_ownership_dashboard.py` (5c..81b) + `avgcap_monthly_average.py`.

> **GRAIN DECISION (Andrew 2026-06-25): PARTNER-NOW, END-CLIENT-LATER (phased).** Phase 1 canonizes + charts at PARTNER
> grain (49F/Inflection/Cottonwood) — ships on the live pipeline, no ingestion change. Phase 2 refines to per-end-client
> (household) grain when the producers are expanded. The canonical key carries a `client_id` (= partner in P1; =
> `{partner}#{household}` in P2) + a `grain` tag + an always-present `partner` field, so Phase 2 is a KEY REFINEMENT, not a
> schema rewrite. Everything below is forward-compatible by construction. **"client" = partner for Phase 1.**

---

## 0. Two tiers, two jobs
| Tier | Canonical form | Charts? | Why |
|---|---|---|---|
| **DAILY** | a **row in DynamoDB** (keyed, queryable) | **NO** | a daily snapshot — just the recorded value; no presentation. The keyed store is what the monthly charts query for their series. |
| **MONTHLY** | a **rich artifact** (the marquis) — daily values per ETF per client + current/average summary + delta charts | **YES** | the key output. Average level accented at top; charts at 3 cuts × 2 windows. |

---

## 1. CANONICAL DAILY FORM — DynamoDB row (no charts)

**Table `opal-etfs-ownership-daily`** (recommend DynamoDB over S3-JSON for keyed date-range queries — the chart series need `(client#etf, date BETWEEN d1..d2)`, an O(range) Dynamo query vs an O(N-files) S3 scan).

| Attribute | Phase-1 value | Note |
|---|---|---|
| **PK** `client_etf` | `{client_id}#{etf}` e.g. `inflection#DIVZ` | the per-client/ETF series key (chart cut 3) |
| **SK** `date` | `2026-06-24` | range-queryable for period + lookback windows |
| `client_id` | `inflection` (=partner P1; `inflection#hh_338` P2) | the forward-compatible client key |
| `partner` | `inflection` | ALWAYS present → partner rollups work at any grain |
| `grain` | `"partner"` (P2: `"household"`) | consumers know the level |
| `etf` | `DIVZ` | |
| `ownership_value` | `30086717.40` | the recorded daily value |
| `account_count` | `476` | |
| `source_as_of` | `2026-06-24` | honest vintage (batch cadence) |
| `source_artifact` | `s3://opal-data-inf/gold/holdings/2026-06-24.parquet` | provenance |
| `ingested_utc` | ISO | write time |

**GSIs** (for the other two chart cuts):
- **GSI-etf**: PK `etf`, SK `date` → per-ETF-all-clients series (cut 1).
- **GSI-client**: PK `client_id`, SK `date#etf` → per-client-all-ETFs (cut 2 / client totals).

**Feed (firm-sep preserved):** the existing per-partner daily producers keep writing `opal-data-etfs/daily/{partner}/{date}.json` (each writing ONLY its own prefix, reading ONLY its own firm bucket — the write-out model intact). A small **internal fan-in Lambda** (etfs-reader-IAM only) upserts each landed daily slice → DynamoDB rows. No producer cross-reads; Dynamo is downstream of the audited etfs bucket. (Alt: producers write Dynamo directly with per-partner-scoped write IAM — viable but spreads the Dynamo grant across 3 firm roles; the fan-in keeps a single internal writer. Recommend fan-in.)

---

## 2. CANONICAL MONTHLY FORM — the marquis artifact

`opal-data-etfs/platinum/etf_ownership_monthly_{YYYY-MM}.json` (extends `avgcap_monthly_average.py` — same calendar-day carry-forward average, now the full canonical monthly). Top-down, **average accented**:

```jsonc
{
  "month": "2026-06", "schema_version": "1.0", "internal_only": true,
  "generated_utc": "...", "as_of_cap": "2026-06-24",

  // === MARQUIS (top, ACCENTED) -- AVERAGE level is THE number ===
  "marquis": {
    "metric": "monthly_average_ownership_value",         // AVGCAP calendar-day carry-forward
    "grand_total_average": 593732130.00,                 // big accented hero number
    "per_client_average": [                              // ranked
      {"client_id":"49financial","partner":"49 Financial","average_total": 509354175.00},
      {"client_id":"inflection","partner":"Inflection","average_total": 83336939.00},
      {"client_id":"cottonwood","partner":"Cottonwood","average_total": 1041016.00}
    ]
  },

  // === SUMMARY -- client aggregates: CURRENT level + AVERAGE level (+ deltas) ===
  "summary": {
    "per_client": [{
      "client_id":"inflection","partner":"Inflection",
      "current_total": 83336939.00, "current_as_of":"2026-06-24",
      "average_total": 83336939.00,                       // marquis (avg)
      "delta_period":  {"abs": 1234567.0, "pct": 0.015},  // current vs month-start
      "delta_lookback":{"abs": 9876543.0, "pct": 0.13, "since":"2026-05-15"}
    } /* ...per client... */],
    "grand": {"current_total":..., "average_total":..., "delta_period":{...}, "delta_lookback":{...}}
  },

  // === DAILY VALUES per ETF per client (the granular backing matrix) ===
  "daily_per_client_etf": [
    {"client_id":"inflection","partner":"Inflection","etf":"DIVZ",
     "series":[{"date":"2026-06-01","ownership_value":...,"account_count":...,"source_as_of":...}, ...]}
    /* ...one entry per (client, etf)... */
  ],

  // === CHART DATASETS -- delta over PERIOD + over LOOKBACK, at 3 cuts ===
  "charts": {
    "per_etf":        [{"etf":"DIVZ","period":{...},"lookback":{...},"series":[{"date","value"}...]} ...],
    "per_client":     [{"client_id":"inflection","period":{...},"lookback":{...},"series":[...]} ...],
    "per_client_etf": [{"client_id":"inflection","etf":"DIVZ","period":{...},"lookback":{...},"series":[...]} ...]
  }
}
```
- **Marquis = AVERAGE** (AVGCAP monthly average). Hero-accented at the very top — the grand-total average + per-client averages, ranked.
- **Summary** carries BOTH current (latest in-month daily) AND average (marquis) per client, with the two deltas.
- **`daily_per_client_etf`** is the daily matrix the spec requires ("daily values per ETF per client"), sourced from the DynamoDB rows for the month.
- **`charts`** carries series + delta numbers; the presentation renders them (no compute at render time).

---

## 3. CHART SPEC — 2 windows × 3 cuts = 6 families (monthly only)

| Window | per-ETF (general) | per-client | per-client/ETF |
|---|---|---|---|
| **PERIOD** (this month: first→last in-month value) | ETF total across clients, month series + Δ | client total, month series + Δ | client×ETF, month series + Δ |
| **LOOKBACK** (all available history, since first slice) | ETF total across clients, full series + Δ | client total, full series + Δ | client×ETF, full series + Δ |

- **Chart type:** time-series line/area of `ownership_value`; annotate the start→end **delta (abs + pct)** as the callout. Multi-series where natural (per-ETF = 4 lines; per-client = 3 lines; per-client/ETF = the drill, one line + Δ).
- **Lookback bound** = per series' earliest available slice (Inflection 2026-05-15 clock, Cottonwood 2026-06-08, 49F since RPS-daily start) — honest "since {date}" label, never back-filled before data exists.
- **Daily tier renders NO charts** — daily is the DynamoDB row only.

### Delta semantics
- `delta_period`  = value(last in-month) − value(first in-month);  `pct` = abs / first.
- `delta_lookback`= value(latest) − value(earliest-available);     `pct` = abs / earliest; `since` = earliest date.
- Carry the daily-granular / batch-cadence honesty (49F batch-delivered) into the series gaps — carry-forward for the average (AVGCAP D1), raw points for the chart with a "batch-delivered" footnote so a flat 49F segment between batches isn't read as zero movement.

---

## 4. BUILD (phased) — who does what
**Phase 1 (partner grain — ships on the live pipeline):**
1. **AE** — provision `opal-etfs-ownership-daily` DynamoDB (TF) + GSIs + the internal fan-in Lambda (etfs-reader IAM, daily-slice → Dynamo upsert) + its schedule/event-chain.
2. **DE (me)** — the canonical MONTHLY producer (extend `avgcap_monthly_average.py` → `etf_ownership_monthly.py`): read the Dynamo daily rows for the month → emit the marquis + summary(current+avg+deltas) + `daily_per_client_etf` + the 6 chart datasets → `platinum/etf_ownership_monthly_{YYYY-MM}.json`. + the monthly PRESENTATION (deck/report) rendering the marquis-accented + charts (deck-gen per the periodic-deck scaffold).
3. **DS** — confirm the daily compute grain + the AVGCAP average definition stays the marquis; validate the daily matrix ties to source.
4. **CVO** — firm-sep cert (cross-client monthly stays Opal-internal) + value-parity (daily matrix ties to the live daily slices).

**Phase 2 (end-client grain — later):** producers expanded to emit per-household × ETF rows (`client_id = {partner}#{household}`, `grain="household"`); same canonical schema, finer key; charts gain the per-end-client cut. PII handling: per-household is PII → pseudonymize in the internal artifact + the internal-only gate stays the bar (no tenant route, ever).

---

## 5. OPEN ITEMS for the design-gate
1. **Marquis-average definition** — confirm the marquis = AVGCAP monthly average (calendar-day carry-forward). Default YES (it's the existing "average" metric). [DS/Andrew]
2. **DynamoDB vs S3 for daily** — recommend DynamoDB (keyed range queries for the chart series). Confirm. [CTO/AE]
3. **Fan-in vs direct-Dynamo-write** — recommend the internal fan-in Lambda (single internal writer, firm-sep clean). [CTO/AE]
4. **Lookback horizon cap** — full available history, or a cap (e.g. 12M)? Default full (data is young). [Andrew]
5. **Delivery of the monthly** — the periodic deck (deck-gen, per `ETFS_periodic_deck_scaffold_v0.1.md`) + the JSON artifact; internal push/drop. [Andrew/CTO]
