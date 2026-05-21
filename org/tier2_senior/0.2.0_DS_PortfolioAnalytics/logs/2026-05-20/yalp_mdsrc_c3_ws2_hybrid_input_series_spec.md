# Session Log — YALP_MDSRC.C3 WS-2 hybrid-surface input-series spec

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics |
| Date | 2026-05-20 |
| Task Order | YALP_MDSRC.C3 (WS-2 hybrid-surface input-series spec — C2 build-input prep) |
| Status | COMPLETE — brief + TSV committed + pushed; RAVC2 to COO CC CTO |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| WS-2 C2 input-series spec | docs/briefs/mdsrc-ws2-c2-input-spec-20260520.md | COO (RAVC2) / CTO / C2 / A3 |
| Machine-readable input table | docs/briefs/mdsrc-ws2-c2-input-spec-20260520.tsv | C2 build-input (78 rows, 12 cols) |

## What was done

Enumerated the exact index/security input series the WS-2 hybrid-surface yang generators
consume — correlation, factor spreads (FT-02/03), Model Portfolios benchmark legs
(MP-01/02/03) — via source-read of yang-generate-correlation / yang-generate-factor-tilts /
yang-model-portfolio-benchmarks, cross-referenced to the dc01d4b8a YCharts ticker crosswalk.
Pre-stages C2's WS-2 input requirements so C2 is not serialized behind a fresh enumeration
when A3's internal-API mapping lands.

## Headline findings

- Correlation: 63 monthly index series (return_monthly); 59 map cleanly to the crosswalk,
  4 flagged — 3 genuine crosswalk gaps (Bloomberg US Treasury / 1-3 Year Treasury / 7-10
  Year Treasury) + Crude Oil variant ambiguity (Brent vs WTI).
- FT-02/03: 6 factor-spread series — PRE-COMPUTED in model.pkl; the generator does not
  expose the constituent index pair behind each spread. C3 CANNOT ticker-enumerate FT-02/03
  from the generator alone — flagged as needing a Yang-source factor-construction consult.
- MP-01/02/03: 9 distinct public input series (3 constituent indices crosswalk-mapped,
  3 constituent ETFs direct-lookup, 3 RFR Treasury tenors = WS-1 YIELD domain) + the
  re-blend weights are in the generator source. The cleanest C2 target in the WS-2 set.

## Coordination

- 0.4.0_DS / COO: ACK sent on GO (MCP 20260521T015940Z).
- 0.1.0_DS (A3): C3<->A3 surface-ID + join-key coordination (MCP 20260521T015940Z) — input
  rows keyed on portal_name + carry bbg_ticker; A3 fills ycharts_symbol.

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdsrc-ws2-c2-input-spec-20260520.md | New — C3 input-series spec brief |
| docs/briefs/mdsrc-ws2-c2-input-spec-20260520.tsv | New — 78-row machine-readable input table |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/YALP_MDSRC.C3.ds-ws2-hybrid-surface-input-series-spec.md | status pending -> complete |

No code / Terraform / Lambda / portal change — audit/spec only.

## Compiler Tools

| Tool | Command | Result | vs expect |
|------|---------|--------|-----------|
| comp-pipescript io | `comp-pipescript io yang-generate-correlation / yang-generate-factor-tilts / yang-model-portfolio-benchmarks` | All 3 = "Unknown script" — not comp-graph nodes (yang generators off the comp-pipescript graph, per PRD §5) | `<if_mismatch>` fallback — direct source read of all 3 generators, documented in brief §2/§3 |
| Phase 2 | none (spec doc, no code) | No .py authored | MATCH — documented-none |
| Phase 3 | none (per-surface table = self-validation) | brief §3/§4 + TSV checked vs AC1-AC3 | MATCH — documented-none |

comp-pipescript runs auto-logged to org/compiler-tools-log.md via .comp-graph/.agent_context.

## Next Steps

- [COO] RAVC2 — YALP_MDSRC.C3 complete. Route a Yang-source consult for the 6 factor-spread
  constituent definitions (brief §6, finding 2).
- [C2 / 0.1.0_DS + 0.2.0_DS] consume the spec + TSV as the WS-2 build-input; MP-01/02/03
  build-ready, correlation 59/63 ready, FT-02/03 blocked on the Yang-source consult.
- [A3 / 0.1.0_DS] fill ycharts_symbol per portal_name; resolve the 3 correlation Treasury
  crosswalk gaps + the Crude Oil variant.
