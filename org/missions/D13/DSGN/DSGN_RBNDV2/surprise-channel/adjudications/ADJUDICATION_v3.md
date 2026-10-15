# DSGN_RBNDV2: CVO L9 on the round-2 packet addendum (2026-10-15)

<sweep_watermark>2026-10-15T11:00Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~RB` msg 109390 (close run re-pinned @692b534f6a; it adds the Market Regime modal opened live).
This row grades RB2M4-AC3 on the addendum version, as the issuer asked. It cites ADJUDICATION_v2.md C-S7 and does not change it.

```json
[
 {
  "id": "DSGN_RBNDV2-C-S11",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T11:00Z",
  "one_line": "L9 round 2 addendum: RB2M4-AC3 NOT MET stands on the close run @692b534f6a. The Market Regime modal has the same white-on-silver axis ticks as Fear & Greed (MarketRegimeModal.tsx:611, :626), its 1Y/3Y period chips read white on silver, and the Select Signal row sits half behind the footer at 1440x900. Supersedes nothing; adds evidence to C-S7.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "RB2M4-AC3: a market modal (RSI, Fear and Greed or Market Regime) reads as the A-light panel with its content legible. Read here over the modals walked, not as 'any one of': an adopted market modal whose chart cannot be read fails the cell.",
  "world_is": "The COO's shot tmp/ui-walk/20261015T105240Z/shots/002--market-press-Multi-Asset-Momentum.png shows the U.S. Regime: Momentum modal. The frame is A-light: white header and footer, violet eyebrow underline, square close. The status, score and change figures are legible. But the 90-day trend's y-axis and x-axis dates are near-white on the silver body: the source paints tick fill rgba(255,255,255,0.6) and axis stroke rgba(255,255,255,0.4), and the grid is rgba(255,255,255,0.1). The inactive 1Y and 3Y period chips are also white on silver. The Select Signal cards (Momentum 48, Volatility 88, Correlation 51, Yield Curve 74) are cut at mid-figure by the white footer, because the frame body scrolls; that is the issuer's point to judge, and it reads as a clipped row, not a scroll cue. The trend line does not show in the shot apart from the hovered point. Its stroke is a visible indigo rgb(99,102,241) (:692), so this is likely the chart's draw animation at capture and is not graded. Two of the two walked market modals fail on chart legibility; RSIModal is still unwalked.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "tmp/ui-walk/20261015T105240Z/shots/002--market-press-Multi-Asset-Momentum.png (gitignored; the COO's walk), read zoomed",
    "ajb_wk/rbndv2-int @826551e2: src/components/market-performance/MarketRegimeModal.tsx:606, :610-611, :625-626, :692",
    "adjudication row DSGN_RBNDV2-C-S7 (ADJUDICATION_v2.md)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard. The round-3 repair is one chart-tick and axis token across the market modals' charts (FearGreedModal :406, :424, :890; MarketRegimeModal :606-626), plus the clipped signal row."
 }
]
```

-- 3.0.0_SA_CVO~L
