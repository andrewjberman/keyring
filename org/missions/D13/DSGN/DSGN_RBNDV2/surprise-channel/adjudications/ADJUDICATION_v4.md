# DSGN_RBNDV2: CVO L8/L9 at the round-3 close (2026-10-15)

<sweep_watermark>2026-10-15T12:10Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~RB` msg 109400 (record `deliverables/2.0.0_SA_COO~RB/ROUND3_CHART_CHROME_READ_20261015.md` @42f6317957).

**Result: RB3C1-AC3 MET and RB3C2-AC2 MET. W10-S1 meets its disarm condition. W10-S2 GRADUATES ARMED to REMEDIATION_v3 (RSI is read as text only). W11-S1 and
W11-S2 are dismissed. One new finding goes to the CTO's list: the inactive period chips inside the market modals are still white on silver.**

Instrument. This seat's own three walks of `/market` on the feature-branch build at port 5174 (`ajb_wk/rbndv2-int` @cf2bdeaa), each armed, signed in, one press and
disarmed, with the post-disarm login REFUSED each time:
- `--press "Fear & Greed"`, output `tmp/ui-walk/20261015T120922Z`;
- `--press "Multi-Asset Momentum"`, output `tmp/ui-walk/20261015T121023Z`;
- `--press "S&P 500"`, output `tmp/ui-walk/20261015T121134Z`.

All three folders are gitignored. The served `RSIModal.tsx`, and both files on disk, hold 0 `rgba(255,255,255` literals.

```json
[
 {
  "id": "DSGN_RBNDV2-C-S12",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T12:16Z",
  "one_line": "L9 round 3: RB3C1-AC3 MET (the Fear & Greed and Market Regime chart axes read navy-grey, and the Market Regime signal row is fully visible above the footer); RB3C2-AC2 MET (the Index Performance chart axes read navy-grey, and RSI's chrome is token-mapped in source, unreachable by a labelled control). This cures round 2's RB2M4-AC3.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "RB3C1-AC3: the chart axes read as navy-grey on the white surface and the signal row is fully visible. RB3C2-AC2: the chart axes of the two modals (RSI, Index Performance) read as navy-grey on the white surface, read live where reachable.",
  "world_is": "Fear & Greed: the y-axis 0-100 and the date ticks 6/8..10/14 read navy-grey and legible. Market Regime: the axis ticks read navy-grey; the four Select Signal cards (Momentum 48, Volatility 88, Correlation 51, Yield Curve 74, each with its caption) sit wholly above the footer with no clip. Index Performance (S&P 500): the $ axis and date ticks read navy-grey. RSI: no labelled trigger, so not opened; its white literals are gone in the served file. Not graded: in the Market Regime and S&P 500 shots no data line is drawn, though the strokes are a colour (MarketRegimeModal :692 indigo; IndexPerformanceModal :496 trendColor) with Recharts' default draw animation, so this is likely the capture timing. NEW, outside both criteria: the inactive period chips in these modals (Market Regime 1Y/3Y; S&P 500 the chips beside 1Y) read white on silver, because IndexPerformanceModal.tsx:140 still writes 'bg-white/5 text-white/60', an alpha variant the light-scope remap does not reach (the same class as W8-S14). The same idiom is at :131 and :318-339.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "tmp/ui-walk/20261015T120922Z, 20261015T121023Z, 20261015T121134Z, shots/002-* (gitignored; this seat's walks, 2026-10-15 ~12:10-12:12Z)",
    "ajb_wk/rbndv2-int @cf2bdeaa: src/components/market-performance/IndexPerformanceModal.tsx:131, :140, :456-496; MarketRegimeModal.tsx:692",
    "grep -c 'rgba(255, *255, *255' RSIModal.tsx IndexPerformanceModal.tsx -> 0 and 0; the served RSIModal.tsx -> 0"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard. The white period chips are a round-4 candidate: the text-white/NN alpha idiom inside the light scope, on the CTO's list."
 },
 {
  "id": "DSGN_RBNDV2-C-S13",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T12:16Z",
  "one_line": "W10-S1 meets its disarm condition (Index Performance read live: axes navy-grey, 0 white literals). W11-S1 and W11-S2 are dismissed INERT.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W10-S1", "DSGN_RBNDV2-W11-S1", "DSGN_RBNDV2-W11-S2"],
  "spec_asserts": "W10-S1: IndexPerformanceModal takes the RV-c-1 token mapping, read live at the drain.",
  "world_is": "This seat's S&P 500 walk shows the Index Performance chart axes navy-grey, and the file holds 0 white literals. W11-S1 (an alpha-0.3 dot outline mapped to --rb-quiet as the nearest band) is a build note. W11-S2 (a sparse worktree omits org/surprise_channel/schemas/) is a build note for the sparse base set, the same family as NFRA_CTLPLN W105-S2.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "tmp/ui-walk/20261015T121134Z (this seat's walk)",
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md rows W10-S1, W11-S1, W11-S2"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarm condition met as measured, recorded for its owner 2.0.0_SA_COO~RB; two build notes."
 },
 {
  "id": "DSGN_RBNDV2-C-S14",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T12:16Z",
  "one_line": "W10-S2 GRADUATES ARMED to REMEDIATION_v3: RSIModal's chart chrome is mapped in source (0 white literals served) but has never been read in a browser, because its trigger is a chart bar.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W10-S2"],
  "spec_asserts": "A row graduates when its mechanism is attributed and its remedy holder named.",
  "world_is": "Neither the COO's walk nor this seat's opened RSIModal. The source read shows 0 rgba(255,255,255 literals in the served file.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W10-S2",
    "remediations/REMEDIATION_v3.md"
   ]
  },
  "disposition": "GRADUATED"
 }
]
```

-- 3.0.0_SA_CVO~L
