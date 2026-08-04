# LT/ULT model closure + display typing canon -- Pod2 FE half (Positioning / Attribution / FactorTilts)

**archetype:** IMPLEMENT
**Session:** 2026-08-04 ~20:27Z-21:30Z
**Agent:** 0.2.0_DE_PortfolioAnalytics

## Work orders (no TO -- MCP was the order, per CTO)
- 0.4.0_DE_ClientPlatform 202936Z: ANDREW-ASSIGNED LT/ULT closure recipe for my three pages (FE half).
- 1.0.0_SA_CTO 203229Z: ANDREW-DIRECT (via Yang) display typing canon, Pod2 half -- "Ultra Short-Term /
  Short-Term / Intermediate-Term / Long-Term / Ultra Long-Term", display layer only.
- 0.2.0_DT 203048Z: both items ride DT's next promote; confirm bar = name both explicitly.
- 2.0.0_SA_COO 203331Z: seat split -- FE seams mine; the 3 yang producer lambdas are 0.2.0_DS's
  (morning-sequenced); do not edit producers.

## Delivered
Portal DEV commit **604101df** (7 files), atop 0.4.0_DE's lib commit **02b7f351** (displayModelName --
consumed, not duplicated; coordination: I held the shared file, asked, they took it). NOT pushed (LD-0367).

1. **Display canon**: all Pod2 model-name emission resolves through `displayModelName()` --
   gridConfig PORTFOLIO_NAMES (derived from PORTFOLIO_ORDER), PositioningSummary PORTFOLIO_CONFIG,
   HoldingsTab PORTFOLIOS, Attribution holdings-shared PORTFOLIOS, FactorTilts AVAILABLE_PORTFOLIOS.
2. **Vintage seams**: portal-proxy getHoldingsAttribution + canonicalizeCodeKeys (seam was ABSENT);
   HoldingsTab/SelectionTab AUM codeMap -> getCanonicalModelName-first lookup; FactorTilts
   computeAggregateMetrics hand candidate-list -> canonicalized weight map (one-mapping law).
3. **Live defect fixed**: served aum-metrics.json carries 'Short-Term'/'Long-Term Conservative'/
   'Long-Term Aggressive' -- forms the raw codeMaps did not key, so ST/LT/ULT AUM weights were
   silently dropped in HoldingsTab/SelectionTab TODAY. Canonicalize-first repairs it.

## Verification (all observed, not inferred)
- `bun run typecheck` (tsc -b) clean.
- ui-smoke observed renders (screenshots in session scratchpad): positioning live artifact
  (honest-absent LT/ULT) + synthesized LTC/LTA-keyed AND LT/ULT-keyed fixtures -> all 5 models render
  identically on both vintages, canon headers; factor-tilts live + LTC/LTA-synthesized -> 5 bars, canon
  legend, AGG recomputed through new weight path; attribution live + LTC-synthesized with LT tab
  clicked -> full table through the new seam.
- SEV1 SURFACE_ACK (portal-proxy on model_portfolios.benchmark surface): audited, surfaced to CTO,
  **RATIFIED as used** (CTO 212359Z).

## FINDING (surfaced to COO/DS/CTO, not absorbed)
ALL THREE served artifacts are missing LT/ULT data rows entirely (S3-measured ~21:0xZ):
positioning_data.json portfolios+current_holdings, tier1-snapshot.json summary+factorTiltsByWindow,
holdings_attribution_data.json portfolios -- each UST/ST/INT only. Briefing recorded positioning/
factor-tilts as "legacy-coded"; the LTC/LTA strings there are metadata only. Silent-drop class on all
3 producers -> DS morning wave. FE proven both-vintage-ready: DS's fix lights pages with zero FE work.

Also: startup triaged 3 stale 07-23 DT dispatches (OBE -- PROD moved v2.1.143->148 same day, now 153+).
TO_PORTALREFRESH_FE_01 still reads ACTIVE but was delivered 07-17 per logs -- status is a claim; left
for reconciliation with DT.

## Compiler Tools
| Tool | Result |
|---|---|
| comp-surface-check (pre-commit, portal) | SEV1 BLOCKED on portal-proxy.ts -> read, scoped, audited SURFACE_ACK, CTO-ratified |
| comp-which (A.3 exercise) | forwarder ran (banner) -- PATH 94/94 |
| comp-transform schema-check | NOT run: no data-prop shape changed (display strings + read-seam key canonicalization only); render proof via ui-smoke live+mutant pair per the 70c884ae acceptance standard |
| comp-blast | NOT run: no deletion; edits confined to Pod2 page trees + one additive proxy seam |

## Next
- [me] Live render verify when DS regenerates the three artifacts (offered to DS).
- [0.2.0_DT] Promote carries 02b7f351 + 604101df + 0.4.0_DE's Pod4 sweep.
