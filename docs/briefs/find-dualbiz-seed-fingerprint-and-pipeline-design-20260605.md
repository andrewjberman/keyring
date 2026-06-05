# Dual-Business (Insurance + AUM) Lookalike Discovery — Seed Fingerprint & Pipeline Design

**Provisional project code:** `FIND_DUALBIZ` (FIND macro; sibling of `FIND_INSURE`; final code TBD with Andrew/CTO)
**Author:** 0.1.0_DS_MarketIntelligence
**Date:** 2026-06-05
**Origin:** Andrew-direct engagement 2026-06-05 — Sales-team thesis + three seed targets. "Reformat what we did [FIND_INSURE] around the new target."
**Status:** DISCOVERY / DESIGN — doc-of-record for the engagement kickoff. No pipeline code shipped yet.

---

## 1. Thesis (from Sales, restated)

Certain firms are **under-the-radar but doing very large insurance-policy transaction volume**, and have a strong vested interest in **building an Asset-Management / Wealth-Management (AUM) business in parallel** to the insurance business — because AUM is recurring revenue (long-term money-maker for the firm and the producer) versus one-time insurance commission. Opal wants a **top-of-funnel lead-generation pipeline** that finds firms comparable to three seed exemplars, ranked and tier-labeled for the IR team.

**Seeds:** `paracleteusa.com` (Paraclete — major Opal target), `49financial.com` (49 Financial — Opal's biggest client), `figmarketing.com` (FIG — oversees Paraclete and many similar firms).

---

## 2. The seeds are not three companies — they are one structure at three points of maturity

Empirical profiling (browser-UA fetch + SEC/FINRA public records, 2026-06-05) shows the three seeds are three **tiers of the same dual insurance+AUM organism**:

| Firm | Tier | Self-brand (verbatim) | Advisory / RIA structure | Audience |
|---|---|---|---|---|
| **FIG** (Financial Independence Group) | **Aggregator / IMO-FMO** (upstream wholesaler) | "product distributor in the insurance industry"; "Empowering FINANCIAL PROFESSIONALS"; est. 1976; "Family of Companies" | Commonly-controlled RIA = **Alphastar Capital Management** | B2B — recruits independent advisors |
| **Alphastar Capital Management** | **Bridge — affiliated RIA / TAMP** | "an RIA dedicated to empowering IARs"; "holistic wealth management that includes insurance as a key asset class"; RIA since 2011, "inaugural member of the Family of Companies" | The RIA itself; *"under common control with … FIG, an insurance wholesaler"* | B2B — advisors |
| **Paraclete Wealth Partners** | **Producing agency** (downstream) | "an insurance agency specializing in retirement income and distribution planning using insurance based products"; "Retirement Income. Stability. Legacy." | advisory *"offered through Alphastar Capital Management, LLC, a SEC-registered investment adviser … separate and independent entities"* | End-client (retirees) |
| **49 Financial** | **Integrated / evolved firm** | "values-based financial planning firm"; *"Two Are Better Than One"*; "Comprehensive Financial Planning" | **Own** RIA: "49 Wealth Management, LLC d/b/a 49 Financial, is an SEC registered investment adviser"; commissions via **Oakwood Capital Securities** (BD, "not affiliated entities"); custodian **Charles Schwab** | End-client (professional / pre-retiree / retiree / private wealth) + recruits advisors |

The organism: an **IMO/FMO wholesaler spawns a commonly-controlled RIA/TAMP** (FIG→Alphastar); **producing agencies plug into both** (Paraclete distributes insurance via FIG, advisory via Alphastar); some firms **internalize the whole stack under one roof** (49 = own RIA + own producer network + BD relationship).

---

## 3. The shared fingerprint

### 3.1 PRIMARY signal — the dual-entity disclosure boilerplate (near-deterministic)

The discriminator is **NOT** how loudly a firm markets "wealth management." Paraclete's entire public site is insurance / retirement-income; its AUM business surfaces **only in the disclosure footer**. That footer boilerplate is the highest-precision detector, because the legal requirement to separate commission (insurance) from advisory (SEC-registered) business forces every dual-business firm to print it:

- Paraclete: *"Investment advisory services offered through Alphastar Capital Management, LLC, a SEC-registered investment adviser. … Alphastar Capital Management and Paraclete Wealth Partners are separate and independent entities."*
- 49: *"49 Wealth Management, LLC d/b/a 49 Financial, is an SEC registered investment adviser. … All commissionable product sales are performed through and under the supervision of Oakwood Capital Securities … not affiliated entities."*

**Detector patterns (regex-class, case-insensitive):**
- `(investment advisory services|advisory services|securities) offered through [A-Z][\w .,&]+?,?\s+(a|an)?\s*(SEC[- ]?registered\s+)?(investment advis[eo]r|registered investment advis[eo]r|broker[- ]?dealer)`
- `d/b/a\s+[\w .,&]+?\b.*\bSEC[- ]?registered investment advis[eo]r`
- `separate and independent entities` | `not affiliated entities` | `under common control`
- `commissionable product sales` | `commission[- ]based fixed [Ii]nsurance products`

These named-entity hits (the RIA name, the BD name) are also **graph edges** — see §4 Engine B.

### 3.2 Tier-priority discriminators (per Andrew 2026-06-05)

Ranked desirability of what the pipeline surfaces:

1. **Producing agencies (HIGHEST).** Insurance-product-heavy, marketed in a **"financial security" / safety / protection / guarantee** register, with the RIA relationship in the disclaimer. This is the Paraclete shape and the #1 target class. Front-of-site marketing signature: "Retirement Income," "Stability," "Principal Protection," "guaranteed," "protect," "safe," "peace of mind," "legacy," "tax-free retirement."
2. **Integrated firms (CLOSE #2).** Own RIA + insurance under one roof (49 shape). Comprehensive-planning brand, but insurance is a named line and a BD relationship exists.
3. **Aggregators / IMO-FMO + RIA (WANTED, distinct class).** One layer of abstraction up (FIG/Alphastar shape). Still sought in scanning, but tagged as a different entity class — a network multiplier, not a direct producing lead.

The scorer and the output ranking weight to this order. Tier is an **emitted label**, not a filter — surface all three, route by tag.

### 3.3 Terminology clusters (verbatim, by register)

| Cluster | Exact on-site terms observed |
|---|---|
| **"Financial security" / safety register** (priority-1 producing signal) | "Retirement Income. Stability. Legacy."; "Principal Protection Programs"; "principal protection"; "Stability"; "Longevity"; "Power of Zero"; "tax-free retirement"; "sequence of returns risk"; "tax time bomb"; "protect income" |
| **Insurance-front** | "insurance agency"; "insurance based products"; "insurance products"; "commission-based fixed Insurance products"; "long term care"; annuity / annuities; IUL; FIA; life insurance; "distribution phase" |
| **Wealth arm** | "wealth management"; "investment management"; "asset management"; "managed money"; "model portfolios"; "Private Wealth"; "fractional family office"; "fiduciary"; "advisory services"; "investment advisory" |
| **RIA / structural** | "SEC registered investment adviser"; "RIA"; "IAR" / "Investment Adviser Representative"; "d/b/a"; "TAMP" / "turnkey asset management program"; "Form ADV"; "Family of Companies"; "under common control" |
| **BD / custody** | "broker-dealer"; named BD (e.g., "Oakwood Capital Securities"); "Charles Schwab" as custodian; "commissionable product sales" |
| **Licensing signature** | Series 7 / 6 / 66 / 24 held together (e.g., 49's CRO holds Series 7/6/66/24); CFP; ChFC — securities AND insurance licenses on the same producer |

### 3.4 Why the FIND_INSURE scorer must be re-tuned (not blindly reused)

FIND_INSURE's `score_web_gold` computes `am_prominence = high_signal_AM_weight / (high_signal_AM_weight + annuity_baseline_weight)` and labels `present`/`adjacent`/`absent`. Run on Paraclete, the **annuity baseline drowns the copy-level AM signal**, scoring Paraclete `adjacent`/`absent` — a false negative on a #1 target. The fix: **elevate the §3.1 disclosure-boilerplate presence to the dominant numerator**; the marketing-copy AM prominence becomes secondary. Insurance/annuity vocabulary is *expected and positive* for the producing tier (it is the "financial security" front), not a penalty.

---

## 4. Pipeline codification — reuse the FIND_INSURE medallion, swap the discovery front-end

The bronze→silver→gold→serving skeleton in `data/find/imo/scripts/` and the free **FINRA BrokerCheck** enrichment are reusable as-is. What changes: the **discovery front-end** (known-list-walk → seed-driven discovery) and the **scorer tuning**.

### Three discovery engines (cheapest / highest-precision first)

- **Engine B — Affiliation-graph walk (LEAD; free, structured, high-precision).** The §3.1 disclosure names the affiliated RIA/TAMP and BD. Pull each named RIA's **Form ADV** (SEC IAPD / `adviserinfo.sec.gov` / `reports.adviserinfo.sec.gov` — public, no auth) → it enumerates affiliated entities, DBAs, and the **IAR roster** → each IAR's producing agency is a fresh **producing-tier** lookalike (priority 1). Reverse-search ADVs for "under common control with [insurance wholesaler/IMO]" to find **aggregator-tier** firms. Reuses the existing FINRA/ADV client (`brokercheck_client.py`). Turns "find comparable companies" from fuzzy NLP into a mostly-deterministic public-records walk.
- **Engine A — Fingerprint scoring (re-tuned taxonomy).** New `config/term-taxonomy-dualbiz-v1.json` + a **disclosure-regex module** + recalibrated weights, validated so all 3 seeds score `present` and tier-classify correctly (Paraclete→producing, 49→integrated, FIG→aggregator). Runs on every candidate domain to confirm + assign tier + extract named RIA/BD.
- **Engine C — Fingerprint-query web search (recall extender; top-of-funnel breadth).** Distinctive-phrase queries (e.g. "retirement income distribution planning insurance" + "advisory services offered through"; "Power of Zero"; "Family of Companies" IMO RIA; "principal protection" "fiduciary") → candidate domains → feed Engine A. The broad net for firms not reachable via the ADV graph.

### Flow

```
3 seeds → derive fingerprint (taxonomy-dualbiz + disclosure-regex + weights)   [Engine A calibration]
        → discover candidates:  Engine B (ADV/BrokerCheck graph walk — free, precision)
                                Engine C (fingerprint web-search — recall)
        → crawl_web_bronze  (browser-UA curl; Playwright escape-valve for 403/JS)
        → parse_web_silver  (existing; Rule-17 passthrough, no field-slimming)
        → score_web_gold    (re-tuned: disclosure-signal dominant; emits tier + named RIA/BD + security-register score)
        → FINRA/ADV enrich  (free: producer Series-license + firm AUM confirmation)
        → build_companies_serving → tier-labeled, priority-ranked lookalike target list for IR
```

### 4.1 Output schema (serving — IR-facing)

Per candidate firm: `firm_name`, `domain`, `tier ∈ {producing, integrated, aggregator}`, `priority_rank`, `disclosure_hit` (bool + matched span), `named_ria`, `named_bd`, `security_register_score`, `insurance_front_score`, `am_signal_score`, `dualbiz_score` (composite), `discovered_via ∈ {adv_graph, web_search, seed}`, `adv_crd` / `finra_crd` (if resolved), `confirmed_aum` (from ADV), `notes`.

---

## 5. Scrape stack — browser-UA + Playwright, NO Bright Data (Andrew direct 2026-06-05)

- **Default fetcher = browser-UA curl.** Every seed served fine to a plain Chrome-UA `curl` (49's 403 was a default-UA bot block, not auth). Browser-UA headers are a **prerequisite** for all fetch + search steps.
- **Escape-valve = Playwright** for JS-challenge / Cloudflare sites (e.g. FIG `/family-of-companies/` returns 403 to curl, renders fine in a real browser). We have the Playwright MCP + a working node+Edge headless runtime; `crawl_web_scraping_browser_bronze.py` is the existing Playwright-class module to repurpose. A dedicated Playwright crawler for scale is acceptable.
- **Bright Data dependency: removed** from the new path. FIND_INSURE's `crawl_web_bronze.py` (Bright Data) is replaced by a browser-UA curl fetcher + Playwright fallback.

---

## 6. Open decisions / next steps

1. **Project code + registration** — provisional `FIND_DUALBIZ`; confirm with Andrew/CTO; register `org/projects/*.json` + REGISTRY row if formalized (2-step). Until then this is ad-hoc exploration under the engagement.
2. **Engine B PoC (recommended next build)** — walk the 3 seeds' named RIAs/BDs (Alphastar, Oakwood Capital) through SEC ADV + FINRA BrokerCheck to produce a first real batch of tier-labeled lookalike candidates. Free, fast, proves the highest-precision path.
3. **Engine A config + scorer re-tune** — author `taxonomy-dualbiz-v1` + disclosure-regex; validate all 3 seeds.
4. **Seed-set expansion** — is the universe seeded only by these 3, or should Sales supply more exemplars to broaden the fingerprint before we lock weights?
5. **Bucket** — reuse `opal-data-imo` under a new prefix, or a new `opal-data-find-dualbiz` bucket? (AE/CTO call at formalization.)

---

## Appendix — evidence

Seed HTML + extraction captured 2026-06-05 under `.runtmp/find_seed/` (49 home/about/professional). Paraclete + FIG profiled via browser-UA fetch + SEC/FINRA public records. SEC anchors: 49 Financial CRD 319484 (`adviserinfo.sec.gov/firm/summary/319484`); Alphastar Capital Management CRD 157423 (Form ADV `reports.adviserinfo.sec.gov/reports/ADV/157423/PDF/157423.pdf`).
