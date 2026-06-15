# FIND_DUALBIZ — Comprehensive Session Log (2026-06-05, pre-sign-off)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DESIGN
**agent:** 0.1.0_DS_MarketIntelligence (Andrew-direct live engagement, turn-by-turn — NOT a dispatched TO)
**project:** FIND_DUALBIZ (formal as of this session — commit `ee9f25202`)

Andrew direct: "I just want it rigidly documented wherever possible… comprehensive session log… all relevant paths… current status… next steps as far as ranking on these various axes… maybe include some lusha/linkedin scanning, I have a feeling there is an ideal employee size, maybe 100-200 advisors." Leaving the office; do NOT pursue further tonight — notate everything.

---

## 0. One-paragraph state

Built a repeatable, parallelized discovery pipeline that finds small/mid dual-business producing agencies (insurance + AUM, the Paraclete shape) by reverse-searching the legally-required dual-entity disclosure footer. Current run: **315 firms scored, 156 disclosure-present**, ranked tier→insurance-density→security-density→WHOIS-age, exported to CSV on Andrew's desktop. Project is now formally registered with a governed PRD + an engineering design-of-record; all 4 open design decisions ruled by CTO. Build queue (P1: candidate-registry consolidation + FINRA/AUM qualification; P2: domain-age folded into composite) is fully unblocked. New forward axis captured below: Lusha/LinkedIn advisor-headcount as a band-centered ranking signal (Andrew hypothesis: sweet spot ~100–200 advisors).

---

## 1. All relevant paths

### Deliverable Andrew has now
- **CSV on desktop:** `C:\Users\AndrewBerman\Desktop\dualbiz-targets-2026-06-05.csv` (246 clean rows, ranked, 16 columns incl. domain-age)

### Serving outputs (authoritative 315-firm run)
- `data/find/dualbiz/scripts/.runtmp/dualbiz/2026-06-05/serving/dualbiz-targets-2026-06-05.json` (full 315, all fields)
- `…/serving/dualbiz-targets-2026-06-05.md` (ranked markdown table)
- `…/serving/dualbiz-targets-2026-06-05.csv` (source of the desktop copy)
- NOTE: a STALE earlier 53-firm run exists at `ajb_workspace/.runtmp/dualbiz/2026-06-05/serving/` — IGNORE; the authoritative tree is under `scripts/.runtmp/` (pipeline.py default `--root` is relative to cwd = scripts/).

### Scripts — `data/find/dualbiz/scripts/`
- `_util.py` — browser-UA curl `fetch()` (bytes-mode, cp1252-safe), Playwright headless-Edge `fetch_browser()` escape-valve, `html_to_text()`, `get_domain_age()` + `domain_age_score()` (WHOIS), slugify helpers
- `serp.py` — SERP harvester. `serp_brightdata()` uses the DEDICATED `serp_opal` zone (structured JSON). `ddg_search()` free fallback. `INDEPENDENT_PROVIDER_QUERIES` = 9 providers × disclosure-string variants. CLI `--engine brightdata --independent-only --pages N --out <file>`
- `harvest.py` — disclosure-search-result → producing-domain filter; `DIRECTORY_DENYLIST` + `PROVIDER_OWN` + `is_producing_candidate()`
- `discover.py` — merges tamp-seed rosters + globs `serp-harvested-*.json` → candidate list (THE GLOB HACK to be replaced by S2 registry)
- `fingerprint.py` — `score_firm()` scorer (disclosure regex + term clusters + tier + classification)
- `pipeline.py` — orchestrator, stages bronze→silver→gold→serving; bronze parallelized (ThreadPoolExecutor 20 workers), WHOIS parallelized (8 workers). CLI `--deep --root --date --no-browser`
- `broaden.py` — peer-provider discovery helpers (disclosure-string generator, tamp-block emitter)

### Config — `data/find/dualbiz/config/`
- `fingerprint-v1.json` — scoring weights (disclosure 50/45/15/10; clusters 8/7/6/5/3), tier rules, size screen, acquisition signal, ranking config
- `provider-seeds-v1.json` — 11 IMO↔RIA pairs w/ independence_status (FIG/Alphastar, Advisors Excel/AE, Gradient, CreativeOne, IMPACT, Simplicity, North Star, Equita = independent; AmeriLife/Brookstone, SMS/Sequent = acquired_megacap)
- `tamp-seeds-v1.json` — per-TAMP disclosure search strings + discovered rosters
- `serp-harvested-2026-06-05-v3.json` — **CORRECT** (serp_opal, 184 candidates)
- `serp-harvested-2026-06-05.json` (v1, 34) + `serp-harvested-2026-06-05-v2.json` (259) — **WRONG ZONE (one_shotter); PURGE in S2 cleanup** (still being globbed into the candidate set by discover.py)

### Docs
- `docs/architecture/FIND_DUALBIZ.md` (v0.1) — MY staged-architecture design-of-record (S0–S7 contracts, two-loop design, scoring/ranking schema, S6 qualification design)
- `docs/architecture/FIND_DUALBIZ_PRD.md` — CTO governed PRD (`4ac127a15`), rules the 4 open decisions
- `docs/briefs/find-dualbiz-seed-fingerprint-and-pipeline-design-20260605.md` — seed brief (`b1a9aa6d7`): thesis, fingerprint derivation, Engine-B PoC, evidence appendix

### Org / governance
- `org/projects/FIND_DUALBIZ.json` — formalized (`ee9f25202`); status active, pods [0.1.0, 1.0]
- `org/projects/REGISTRY.md` — FIND_DUALBIZ row formal (supersedes FIND_INSURE)
- Prior session logs (same dir): `work_1605Z.md` (seed profiling), `work_1815Z.md` (fingerprint brief), `work_1910Z.md` (pipeline codified), `work_1945Z.md` (harvester + saturation finding), `work_2010Z.md` (DDG SERP proven), `work_2201Z.md` (BD-scale + formalization terse log)

### Secrets Manager (us-east-1)
- `find-dualbiz/bright-data/serp` — SERP zone config `{"zone":"serp_opal",…}` (per-query SERP product)
- `find-insure/bright-data/api-key` — shared Bright Data API key
- `find-insure/lusha-ai/api-key` — **Lusha key (already present from FIND_INSURE) — relevant to the headcount axis below**

### Memory (fabric)
- `memory/feedback_serp_use_dedicated_serp_zone_not_unlocker.md` (+ MEMORY.md pointer) — never crawl SERPs through the unlocker zone

---

## 2. Process — how we got here (chronological)

1. **Seed profiling** — 3 Andrew seeds (paracleteusa.com, 49financial.com, figmarketing.com) = ONE insurance+AUM organism at 3 tiers (producing > integrated > aggregator). Found the PRIMARY signal: the legally-required dual-entity disclosure footer, not marketing-copy prominence (the FIND_INSURE am_prominence scorer false-negatived Paraclete).
2. **Fingerprint brief** authored as doc-of-record.
3. **Engine-B1 PoC** — disclosure-string reverse-search (`"offered through [RIA]"`) returns a TAMP's producing-agency roster directly; giant carriers never disclose a third-party TAMP so the size screen is nearly free.
4. **Pipeline codified** — full medallion (bronze→silver→gold→serving), Rule-17 silver passthrough.
5. **Broaden** — peer-provider discovery: reverse-engineer more IMO↔RIA pairs (Gradient, AE, Brookstone…).
6. **Independence axis + acquisition-negative ranking** — acquired_megacap (+20 penalty) sinks a roster below independents (Andrew: the acquirer already gave them AUM rails → no room for Opal).
7. **Playwright escape-valve** — JS/Cloudflare sites (trigger on thin stripped-text <400 chars).
8. **Roster harvester + SERP harvester** — DDG proven (rate-limits at volume) → Bright Data SERP.
9. **BD SERP zone correction (cost incident):** first sweeps used the `one_shotter` web-unlocker zone (premium residential-proxy bandwidth per fetch). Andrew stopped a 259-page run mid-execution. Fix = the DEDICATED `serp_opal` zone (per-query, structured JSON). Banked to memory.
10. **Scale:** added 5 providers + string variants → serp_opal sweep → 184 new candidates → **315 firms / 156 present.**
11. **WHOIS domain-age scoring** + **parallelization** (bronze 20 workers, WHOIS 8 workers; ~10min→~30s). Andrew asked the bottleneck question → sequential curl was the wall.
12. **CSV export** → desktop; opened top-20 + full-37 in Chrome for Andrew review.
13. **Formalization:** Andrew elevated (AskUserQuestion) → enrichment scope WHOIS+FINRA+AUM, register as formal project. Authored staged-arch doc → routed to COO → COO 2-step registry formalization (`ee9f25202`) → CTO governed PRD (`4ac127a15`) + 4 rulings.

---

## 3. Current ranking schema (the axes, as built)

Serving sort = 5-key tuple, compared left→right (later key only breaks ties on all earlier):
```
0. priority_rank + rank_penalty   (ASC)  — tier band + independence penalty (the GATE)
1. -insurance_match_count         (DESC) — Andrew: insurance language density FIRST
2. -security_match_count          (DESC) — then financial-security density
3. -dualbiz_score                 (DESC) — composite fingerprint
4. -domain_age_score              (DESC) — WHOIS age, tiebreaker only (being promoted, see §4)
```
- tier: producing=1, integrated=2, aggregator=3, unknown=4 (+10 giant_flag)
- penalty: independent/unknown +0, pe_rollup +10, platform +15, acquired_megacap +20 (+8 page-acquisition)
- CSV columns A–P: rank, firm, url, tier, disclosure(YES/ADJ/NO), insurance_density, security_density, dualbiz_score, domain_created, domain_age_years, domain_age_score, ria_tamp, provider_independence, named_ria, discovered_via, notes

---

## 4. Next steps — build queue (UNBLOCKED, all design forks ruled by CTO; DO NOT START until Andrew resumes)

**P1 (no blocking decisions):**
- **S2 — Candidate Registry (`registry.py`):** replace the `glob(serp-harvested-*.json)` hack with one canonical `config/candidates.json` (domain + provenance + first_seen, deduped). PURGES the wrong-zone v1/v2 results still polluting the candidate set.
- **S6 — Enrich/Qualify (`enrich.py`):** pull WHOIS out of gold into its own stage; add:
  - **FINRA BrokerCheck** (reuse FIND_INSURE `brokercheck_client.py`; public `api.brokercheck.finra.org`, free, no auth) → firm CRD, **registered-rep count**, Series-license profile (7/63/65/66/24), registration tenure, disclosure flags. Match rule: firm-name match required (name-only not counted).
  - **SEC Form ADV / IAPD AUM** (public) → regulatory AUM + account/client counts. RULING: producing-tier firms (operate under a third-party TAMP) DON'T file their own ADV → `aum: null` + `aum_note: "n/a (operates under [TAMP])"`, NO allocation proxy. AUM resolves only for integrated-tier firms + the TAMPs.
- **One canonical noise filter** — collapse the duplicate `harvest.py DIRECTORY_DENYLIST` and the CSV-writer `NOISE` set into one list used by both S1 and S7.

**P2 (CTO-ruled, after P1):**
- **Fold domain-age into the composite `dualbiz_score`** (`+5 if >10y, +3 if 5–10y, +1 if 2–5y, 0 if <2y`, cap +5) so age PULLS a firm up within its tier band, not just a tiebreaker. REMOVE from sort tuple element-4. Edit `fingerprint-v1.json` + S5 scorer.

**Other CTO rulings banked:** no new S3 bucket (local medallion; S3 only if a portal consumer surfaces); recall stays manual-only behind a `--recall` flag (revisit after 3 evaluation runs).

---

## 5. NEW FORWARD AXIS — Lusha/LinkedIn advisor-headcount (Andrew hypothesis, capture-only)

**Andrew's hunch (2026-06-05, pre-sign-off):** there is likely an IDEAL firm size for a dual-business lead — a sweet-spot band of roughly **~100–200 advisors** — and we can find headcount via Lusha / LinkedIn. Big enough to have real insurance volume + AUM ambition; small enough that Opal still has room to come in (a mega-roster is likely already platformed — same logic as the acquisition-negative signal).

**Why this is a strong axis (analysis):**
- It's a NON-MONOTONIC, band-centered signal — unlike the density axes. Too small (<~20 advisors) = thin volume/ambition; sweet spot (~100–200) = ideal; too large (>~500) = approaching platform/mega scale → likely already has AUM rails (NEGATIVE, mirrors acquisition penalty). Scoring should peak in the band and decay both directions (bucketed or Gaussian-ish around a center to be calibrated).
- **Two headcount sources, complementary:**
  1. **FINRA BrokerCheck registered-rep count** — precise, FREE, ALREADY in S6 scope. This is the truest "advisor" count (vs total employees). Caveat: producing-via-TAMP firms may show reps under the TAMP's CRD, not their own — needs handling.
  2. **Lusha company-enrich / LinkedIn company headcount** — `find-insure/lusha-ai/api-key` already in Secrets Manager; FIND_INSURE already built the Lusha org-chart enrichment (company search + enrich + contacts/prospecting, contact-reveal deferred for credit conservation). Reusable substrate. Gives total employee count + org-chart (titles, seniority) — fuller picture, costs Lusha credits.
- **Validation first:** before trusting the ~100–200 band, pull headcount for the 3 SEEDS (Paraclete / 49 Financial / FIG) + the current top-20 and see where the known-good targets actually land. Calibrate the band to the seeds (overfit-on-seeds is Andrew-sanctioned early). The hunch is a hypothesis to confirm, not a hardcoded filter.
- **Where it slots:** a new enrichment in S6 (`advisor_headcount` + `headcount_source`) feeding a new ranking term `headcount_band_score`. Open question for Andrew on resume: should headcount be a RANK axis (peaks in-band) or a hard FILTER (drop outside ~20–500)? Lean: rank axis (soft), since it preserves recall and we're still calibrating the band.
- **Cost note:** FINRA rep-count is free and may carry most of the signal — pull that FIRST (it's already in S6), THEN decide whether Lusha credits are justified for the total-employee + org-chart depth. Do NOT burn Lusha credits at 315-firm volume without a band-calibration probe on a small subset first (credit discipline, same family as the serp_opal-zone lesson).

**Andrew directive: capture only — do not pursue tonight.** This is queued as a P3 axis (after P1 qualification + P2 age-composite), pending Andrew's resume + the rank-vs-filter call + a seed-calibration probe.

---

## 6. Open questions for Andrew on resume
1. Headcount: rank axis (soft, band-centered) vs hard filter? + confirm the ~100–200 center after a seed-calibration probe.
2. Build order within P1: S2 registry-cleanup first (my lean) vs S6 FINRA+AUM first (faster license/AUM data on the current list).
3. Noise tolerance: a handful of misfits slipped the filter (e.g. vrtabenefits.org, americanseniorsbenefit.com, novacu.com) — tighten the producing-firm filter, or leave soft for recall?
4. Whether to re-run after S2 purges the wrong-zone candidates (counts will shift slightly).

— end comprehensive log; DS_MI signing off pending Andrew resume.
