# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1712Z (Positioning A+ consolidated diff authored)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Dispatch
CTO GO A+ (171xZ): sweep ~28 all-caps into backend ETF_NAME_OVERRIDES from canonical holdings_attribution_data.json (no guess/.title()); include portfolios-section override; retire FE map (coordinate RD~B, post-backend); one consolidated diff -> AE deploy. Surface any ticker the canonical source lacks.

## Work — A+ consolidated diff authored (brief 081be4a0e->updated)
- Part 1: 22 ETF_NAME_OVERRIDES additions, names from canonical attr (holdings_attribution_data.json) + FE fallback where attr lacks (ICSH). NONE missing -> no gap to surface.
  - STYLE-FLAG (surface not guess): 5 tickers (MINT/QQQ/SPHY/SPYM/TBIL) attr name is verbose/odd ("Exchange-Traded Fund"/"State Street SPDR"/"Series I"/"F/m...Fund"); FE display name cleaner. Shown FE value; AE/CTO pick attr-verbatim vs FE-display. Other 17 = attr verbatim.
- Part 2: portfolios-section override -- line 2071 `name = etf_meta.get('name', ticker)` -> wrap with ETF_NAME_OVERRIDES.get (feeds line 2097).
- Part 3: FLAG lines 1549 + 2032 (row['name'] no-override paths) for AE to confirm+apply if those sections emit all-caps.
- Part 4: FE ETF_NAME_FALLBACKS retirement = RD~B, SEQUENCED AFTER backend deploy (else regression); rides next portal promote.
- comp-pipescript io = N/A (producer is a Lambda, not data/*/scripts/gold).

## Lane
- DE-authored diff -> AE (0.7.0_AE_CloudOps) applies + deploys (Lambda = AE lane); DE cannot edit infra/aws/. FE slim coordinated w/ RD~B post-backend.

## Commits
- CLOUD `<pending>` — brief A+ diff section + this log

## Comms
- HANDOFF -> AE (consolidated A+ diff); CC CTO + COO. COORDINATE -> RD~B (FE slim, post-backend-deploy sequencing).

## Next
- [AE] apply A+ diff (Part 1+2, decide the 5 style-flags w/ CTO) + deploy + re-emit + CF-invalidate; ping me.
- [me] serving-verify post-deploy (all 22 + portfolios-section clean); Andrew visual.
- [RD~B] FE map slim AFTER backend verified.
- Held: DS~B Schwab re-verify; RD~B fold(103f623a) verify. /work cron live.
