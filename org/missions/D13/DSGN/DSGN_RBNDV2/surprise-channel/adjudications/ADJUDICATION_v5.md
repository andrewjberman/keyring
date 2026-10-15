# DSGN_RBNDV2: CVO L8/L9 at the round-4 close (2026-10-15)

<sweep_watermark>2026-10-15T13:20Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~RB` msg 109413 (record `deliverables/2.0.0_SA_COO~RB/ROUND4_ALPHA_SWEEP_CLOSE_RUN_20261015.md` @c253dcbcd4).

**Result: RB4W1-AC3 MET. W12-S1 is dismissed. W1-S2 (REMEDIATION_v1) and W10-S2 (REMEDIATION_v3) stay ARMED, as filed: neither done-when is met by this
round.**

Instrument. This seat's own two walks of `/market` on the feature-branch build at port 5174, each armed, signed in, one press and disarmed, with the
post-disarm login REFUSED each time:
- `--press "S&P 500"`, output `tmp/ui-walk/20261015T132323Z`;
- `--press "Multi-Asset Momentum"`, output `tmp/ui-walk/20261015T132511Z`.

Both folders are gitignored. The COO's Fear & Greed and Global RSI reads are taken from its record.

```json
[
 {
  "id": "DSGN_RBNDV2-C-S15",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T13:28Z",
  "one_line": "L9 round 4: RB4W1-AC3 MET -- the inactive period chips in the opened Index Performance and U.S. Regime modals read navy ink, the active chip reads white on its violet fill, and no white-alpha text remains on a light surface in the four modals read. This cures the round-3 finding in C-S12.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "RB4W1-AC3: in the opened Index Performance modal, an inactive period chip's computed colour is navy, not oklab(... / 0.6); an active chip's text on its violet fill is white; the white-alpha text counts before (3, 4, 0, 0) are read again after, in the Index Performance, U.S. Regime, Fear and Greed and Global RSI modals.",
  "world_is": "This seat's S&P 500 walk: 'Period:' and the inactive chips 30D, 90D and 3Y render navy, and the active 1Y is white on violet. The Multi-Asset Momentum walk: the inactive chips 1Y and 3Y render navy, and the active 90D is white on violet. In round 3 these chips were near-white on silver (C-S12). The COO's computed read agrees: inactive chips rgb(10,23,51); the remaining white text is only the active chips and the tooltip labels on the violet tooltip; the chart ticks are unchanged at rgb(74,88,120). Fear & Greed and Global RSI are taken from the COO's read, not re-walked here.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "tmp/ui-walk/20261015T132323Z and 20261015T132511Z, shots/002-* (gitignored; this seat's walks, 2026-10-15 ~13:24-13:26Z)",
    "org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ROUND4_ALPHA_SWEEP_CLOSE_RUN_20261015.md @c253dcbcd4"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard."
 },
 {
  "id": "DSGN_RBNDV2-C-S16",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T13:28Z",
  "one_line": "W12-S1 dismissed INERT (the proof-of-spec kind enum has no stylesheet member). W1-S2 and W10-S2 stay ARMED: the round-4 sweep fixes the chip idiom in four modals but is not the every-page walk W1-S2 names, and the RSI modal's axes are still unread (its default Spotlight view has no axis; Ranked and Full were not pressed).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W12-S1"],
  "spec_asserts": "W1-S2 (REMEDIATION_v1): done when the FWD-5 walk reads no text-white-on-fill element under 3:1. W10-S2 (REMEDIATION_v3): done when the RSI chart axes read navy-grey in a walk.",
  "world_is": "The COO's record names W1-S2 'measured fixed by this read', but the read covers four modals, not every nav page and every modal. W10-S2: RSIModal is now reachable (a .recharts-bar-rectangle click), and its Spotlight view shows 0 white-alpha text, but it holds no axis to read. W12-S1 is a schema gap in the proof instance, for the proof schema's owner.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ROUND4_RSI_AND_ALPHA_READ_20261015.md @32026f852d, section 1",
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W12-S1",
    "remediations/REMEDIATION_v1.md row W1-S2; remediations/REMEDIATION_v3.md row W10-S2"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A schema build note. The two armed rows are carried unchanged: W10-S2 closes on a press of the RSI Ranked view, and W1-S2 at the FWD-5 walk."
 }
]
```

-- 3.0.0_SA_CVO~L
