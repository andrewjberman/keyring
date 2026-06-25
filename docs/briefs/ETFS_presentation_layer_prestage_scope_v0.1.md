# ETFS — PRESENTATION-LAYER PRE-STAGE SCOPE v0.1 (per-partner ETF ownership: ingestion → presentation output)

**Author:** 0.4.0_DE_ClientPlatform (DE, presentation lane) | **Date:** 2026-06-25 | **archetype:** EXPLORE
**For:** Andrew (FORM-PICK, pending via CVO) → 1.0.0_SA_CTO (design-gate) → DE build | **cc:** 3.0.0_SA_CVO (ingestion→presentation verify owner), 0.5.0 (ETFS metric lane), 0.4.0_DS
**Trigger:** Andrew-direct (DM to CVO, verbatim): *"we need this BY PARTNER, recording DAILY. We need the TERRAFORMS, any associated resources, and pipeline data flow created and VALIDATED from INGESTION to PRESENTATION OUTPUT."* The metric pipeline terminates at `opal-data-etfs` S3 JSON today; there is NO presentation layer. **That layer = this scope.**

---

## 0. THE LOAD-BEARING DESIGN CONSTRAINT — cross-partner = OPAL-INTERNAL ONLY (firm separation)

`opal-data-etfs` is the **audited cross-firm AGGREGATION bucket** (ETFS_SETUP write-out model): each partner's producer writes ONLY its own `daily/{partner}/*` slice reading ONLY its own firm bucket; the reader reads ONLY `opal-data-etfs` and **never cross-reads a firm bucket** (NEVER#1 / IAM-Deny intact). The presentation shows **49F vs Inflection vs Cottonwood side-by-side** — a CROSS-partner comparison. **Therefore the presentation surface is an OPAL-INTERNAL view (opal-capital staff scope) and can NEVER be routed into a partner's firm-scoped tenant** (a Cottonwood user seeing 49F's ownership = a NEVER#1 firm-separation incident). Every form below is gated opal-internal-only; this is the single non-negotiable.

---

## 1. THE TWO CANDIDATE FORMS (Andrew picks)

### FORM A — Portal PANEL (opal-internal ADVI/admin surface)
A new panel on an **opal-internal-scoped** portal surface (NOT a partner tenant) rendering the cross-partner per-ETF ownership.
```
  Opal ETF Ownership by Partner            [daily | monthly-avg]  [DIVZ IDVZ PFDE PFOE]
  ┌───────────────────────────────────────────────────────────────────────┐
  │  Stacked bar / grouped bar: ownership_value per ETF, partner-colored    │
  │   DIVZ  ▓▓▓▓▓ 49F  ▓▓▓ Inflec  ▓▓ COT                                    │
  │   IDVZ  ▓▓▓▓  ...                                                        │
  │  + time-series line (inf/cot daily, 49F monthly points) + account_count │
  │  + monthly-avg (AVGCAP) overlay; honest per-partner granularity labels  │
  └───────────────────────────────────────────────────────────────────────┘
```
- **Pros:** reuses portal infra (auth, CloudFront, React, ApexCharts/Recharts, the chart house-style); interactive (toggle ETF, daily↔monthly, drill, time-machine); lives where Andrew already works; one consistent UX with ADVI.
- **Cons:** requires a NEW opal-internal-only route/scope (the ADVI dashboard is tenant-scoped today — a cross-partner panel needs an internal-staff gate + a non-tenant served path; build it WRONG and it's a firm-sep incident); more infra (served artifact + CloudFront behavior + Lambda@Edge scope-gate); rides the portal release cycle.
- **Best if:** Andrew wants it integrated + interactive in the portal he already uses.

### FORM B — Standalone REPORT / dashboard (opal-internal artifact)
A standalone **daily-regenerated** artifact — a generated dashboard page (or deck/PDF via the deck engine) showing the same cross-partner per-ETF ownership, refreshed each producer cycle, delivered to an opal-internal location (S3-served internal page, or emailed/Teams-posted).
```
  ETF Ownership — Daily Recording — 2026-06-24
  ┌─ per ETF: table {partner × ownership_value × account_count × as_of} ─┐
  │  DIVZ   49F $—(monthly 06-18)  Inflec $30.1M(06-24)  COT $—(06-22)   │
  │  IDVZ   ...                                                          │
  ├─ monthly-avg (AVGCAP) summary + MoM delta                            │
  └─ granularity footnotes per partner (source_as_of)                    │
```
- **Pros:** NO firm-sep routing risk (inherently an opal-internal artifact, not in the tenant portal — simplest gate); fastest to ship; decoupled from portal releases; natural fit for *"recording DAILY"* (a daily report cadence); can be auto-delivered (email/Teams/S3).
- **Cons:** static (less interactive than a panel); a separate surface to maintain; not in the portal UX.
- **Best if:** Andrew wants a recurring internal **record** (his word: *"recording daily"*) more than an interactive portal surface.

| Axis | A: Portal Panel | B: Standalone Report |
|---|---|---|
| Firm-sep risk | higher (needs a new internal-scope gate in a tenant-scoped portal) | lower (inherently internal artifact) |
| Interactivity | high (toggles/drill) | low (static snapshot) |
| Time-to-ship | longer (route+scope+component) | shorter (producer + template) |
| "recording daily" fit | medium (live, not a record) | high (a dated daily record) |
| Infra added | served artifact + CF behavior + edge scope-gate | served artifact + a render step |
| Maintenance | portal release cycle | standalone cadence |

*(Not mutually exclusive long-term — B can ship first as the daily record, A follow as the interactive surface reading the same served artifact. Recommend asking Andrew if he wants B-first-then-A or one.)*

---

## 2. DATA CONTRACT (grounded against live `opal-data-etfs`)

**Daily** — `opal-data-etfs/daily/{partner}/{YYYY-MM-DD}.json` = array, one row per ETF:
`{schema_version, partner, date, etf_ticker, ownership_value, account_count, source_artifact, source_as_of}`
**Monthly** — `opal-data-etfs/monthly/{YYYY-MM}.json` = SINGLE cross-partner file:
`{month, methodology, generated_utc, as_of_cap, per_partner_etf:[{partner, month, window:{start,end,calendar_days,partial}, etfs:[{etf, monthly_avg_ownership_value, trading_day_mean_diagnostic, written_days, ...}]}]}`
**Config** — `opal-data-etfs/config/etf_universe.json` = `{tickers:[DIVZ,IDVZ,PFDE,PFOE]}` (runtime-read; universe changes are 1 edit → presentation must render the universe dynamically, not hardcode 4).

**Presentation field → contract map:**
| Presentation element | Source field |
|---|---|
| Ownership $ (per partner per ETF) | daily `ownership_value` / monthly `monthly_avg_ownership_value` |
| # accounts holding | daily `account_count` |
| ETF set (columns/series) | `config.tickers` (dynamic) |
| Daily time-series | `daily/{partner}/*` over date range |
| Monthly-avg + MoM | `monthly/*.per_partner_etf[].etfs[]` |
| Vintage / freshness label | `source_as_of` (daily) / `as_of_cap` + `window.partial` (monthly) |

## 3. SERVED PATH options (DE recommends a presentation producer)
The etfs bucket is a DATA bucket, NOT CloudFront/portal-routed today. Two ways to present:
- **(i) NEW presentation artifact (RECOMMENDED):** a small presentation-producer (reader role, reads only `opal-data-etfs`) rolls the per-partner daily + the cross-partner monthly into ONE served artifact, e.g. `opal-data-etfs/platinum/etf_ownership_dashboard.json` (cross-partner, opal-internal). Keeps the single-audited-reader model; one artifact both forms consume; recompute on each producer refresh (event-chained). **Firm-sep clean** (no per-tenant routing — it's an internal artifact).
- **(ii) Read etfs direct via a new opal-internal API** (Lambda aggregates daily/monthly on read) — more live but adds a runtime read-path + its own scope-gate. Heavier; only if real-time is required.
**Recommendation:** (i) — a presentation-producer artifact, served opal-internal-only. Both Form A and Form B read it.

## 4. GRANULARITY HANDLING (honest per-partner labels — the COTETL serve-time-vintage lesson)
Live reality (grounded 2026-06-25):
| Partner | Daily availability | Effective granularity |
|---|---|---|
| Inflection | daily → 06-24 (current) | **DAILY** |
| Cottonwood | daily → 06-22 (minor gaps 06-19..21) | **DAILY** (near-current) |
| 49 Financial | daily only 06-15..06-18 then FROZEN | **MONTHLY** (Schwab-RPS batch; 49F-daily is silver-fire-gated — BD daily canonical/holdings frozen at 06-19 until Andrew's silver-fire GO) |
| Monthly (all 3) | `monthly/*` capped `as_of_cap=06-18` | cross-partner monthly-avg |

**Rule the presentation MUST encode:** label each partner's series by its REAL granularity + `source_as_of`; render 49F as monthly points (NOT interpolated daily); never imply 49F is daily-fresh. When 49F-daily unlocks (silver-fire GO), the same surface upgrades 49F to daily with zero structural change (it just gets daily rows). Graceful "49F monthly / inf+cot daily" by design.

## 5. WHAT'S SERVABLE TODAY (ingestion proven; presentation is the gap)
Producers live this session (deploys: W1-inf `20260623T1544Z`, W3-cot `20260625T1352Z`, W2-49f `20260625T1747Z`); monthly AVGCAP served (05 + 06). So ingestion→S3 is DONE for all 3 partners; **the only missing leg is S3→presentation** — exactly this scope. A Form-B daily report could ship reading the live artifacts immediately; Form-A needs the internal-scope route built first.

## 5b. DECISION (Andrew form-pick 2026-06-25, via in-session ask + COO `175929Z`) — BUILD SPEC

**FORM = B (STANDALONE DAILY REPORT only)** — not the portal panel, not B-then-A. Reason: lowest firm-sep risk, fastest, fits "recording DAILY", no tenant-route work.
**PRIMARY CUT = TOTAL-FIRST** — lead with total Opal-fund AUM per partner, then both by-ETF and by-partner breakdowns.

### Report spec (total-first standalone daily report)
```
  OPAL ETF OWNERSHIP — DAILY RECORDING — <as_of_date>
  ───────────────────────────────────────────────────────────────
  TOTAL Opal-fund AUM by partner (sum over the 4 ETFs):
     49 Financial   $<sum>   (monthly, as_of 06-18)
     Inflection     $<sum>   (daily,   as_of 06-24)
     Cottonwood     $<sum>   (daily,   as_of 06-22)
     ── Opal-funds total $<grand_sum>
  ───────────────────────────────────────────────────────────────
  BY ETF (partners side-by-side)            [config-driven universe]
     DIVZ   49F $—  | Inflec $30.1M | COT $—   | row total
     IDVZ   ...
     PFDE / PFOE ...
  BY PARTNER (ETFs side-by-side)
     Inflection   DIVZ $30.1M | IDVZ $23.3M | PFDE $19.0M | PFOE $11.0M
     49 Financial / Cottonwood ...
  ───────────────────────────────────────────────────────────────
  MONTHLY-AVG (AVGCAP) + MoM delta   |   per-partner granularity footnotes (source_as_of)
```
- Universe **config-driven** (render `config.tickers` dynamically — adding an ETF must not need a report edit).
- **Granularity honesty:** label each partner's REAL granularity from `source_as_of`; 49F = monthly (silver-fire-gated), inf/cot = daily; never imply 49F-daily before the silver fire. 49F upgrades to daily on Andrew's GO with zero structural change.
- **Opal-INTERNAL only** (cross-partner; never a tenant route).

## 6. NEXT (the gated chain)
Andrew FORM-PICK (A / B / B-then-A) → CTO design-gate (the served-path + the opal-internal scope-gate are the arch decisions; firm-sep is the bar) → DE build (presentation-producer artifact + the chosen form) → CVO ingestion→presentation validation (the AC: pixels/report match the served etfs artifact, firm-sep intact, granularity honest). TERRAFORMS/resources: the presentation-producer Lambda + its reader IAM + (Form A) the CloudFront behavior/route — scoped at design-gate. **No build yet — this is the decision-ready pre-stage.**
