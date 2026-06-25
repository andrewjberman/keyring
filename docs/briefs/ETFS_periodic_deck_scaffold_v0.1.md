# ETFS — PERIODIC-DECK variant SCAFFOLD v0.1 (the richer recurring artifact)

**Author:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-25 | **archetype:** EXPLORE
**Status:** SCAFFOLD only — droppable spare-cycle pre-stage (COO `184413Z`). NOT staged for build. Convert to a full `*.deck.md` (via `/deck-prompt` → `/deck-gen`) ONLY when Andrew wants a periodic cadence.
**Relation:** the daily Form-B text report (`etf_ownership_dashboard.py`, lightweight push) ships now; this is the CTO-reserved "deck for PERIODIC" (e.g. monthly) — the polished recurring artifact, NOT the daily record.

## 0. Reuse posture (zero new producer)
The periodic deck consumes the SAME `opal-data-etfs/platinum/etf_ownership_dashboard.json` (+ the AVGCAP `monthly/*` already in it) — no new compute. It's a RENDER variant: same data → the deck-generation engine instead of the lightweight text body. Firm-sep posture identical (Opal-internal artifact; never a tenant route). Deck → an internal-only delivery (Desktop drop / internal S3 / Teams file), same internal-recipient pattern.

## 1. Slide outline → dashboard-artifact field map
| # | Slide | Source (etf_ownership_dashboard.json) |
|---|---|---|
| 1 | Title — "Opal ETF Ownership — <month>" + as_of + INTERNAL-ONLY banner | `run_as_of`, `monthly_context.latest_month` |
| 2 | Headline — total Opal-fund AUM + per-partner totals (ranked) | `grand_total_ownership_value`, `rollup_total_by_partner` |
| 3 | By ETF — DIVZ/IDVZ/PFDE/PFOE, partners side-by-side (bar) | `rollup_by_etf` (config-driven universe) |
| 4 | By partner — each partner across the universe | `per_partner[].etfs` |
| 5 | Monthly-avg trend + MoM (AVGCAP) | `monthly_context.per_partner` (monthly_avg_total, mom_delta) |
| 6 | Freshness / methodology footer — daily-granular basis, per-partner cadence (inf/cot continuous; 49F batch ~5-10d), AVGCAP calendar-day carry-forward | `per_partner[].{as_of,freshness}`, AVGCAP `methodology` |

## 2. Engine + brand
- Engine: `/deck-prompt` authors the `*.deck.md`; `/deck-gen` composes via `deck_generation/engine/compose.py` + `DESIGN_BIBLE.md` (brand linter + fidelity QA). House primitives (statcards, bars, lines) cover slides 2-5 directly.
- Cadence: MONTHLY (matches AVGCAP). Trigger: post the monthly AVGCAP run (`monthly/{YYYY-MM}.json` lands) — the deck is the monthly book-end to the daily text record.

## 3. What this scaffold is NOT
Not a built deck, not a `.deck.md`, not a producer change. It's the convert-ready outline so that IF Andrew wants the periodic deck, the build is "author the `.deck.md` from this map → `/deck-gen`" with zero re-derivation. Dropped instantly if a 0.5.0 deploy Q / CVO cert finding on the live daily artifact lands (that is the reactive primary).
