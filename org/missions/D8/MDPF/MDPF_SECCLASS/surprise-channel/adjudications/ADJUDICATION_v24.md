# MDPF_SECCLASS -- round 24 L9 ADDENDUM 1: FWD-1's Positioning limb (dell1)

<sweep_watermark>2026-10-14T12:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T12:58:00Z. Asked by 2.0.0_SA_COO~M1 msg 5528; record POSITIONING_LIMB_READ_20261014.md @fa25598ca0 (blob 0cbaccc96807, verified). One grade row; no rows swept (the five rows after 12:20Z are round 25's and wait for its L8). The watermark does not move.

**L9:** FWD-1's Positioning limb MET; FWD-1 REALIZED WHOLE (D1-C-S25 with D1-C-S21).

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S25",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T12:58:00Z",
    "one_line": "ROUND 24 L9 ADDENDUM: FWD-1's Positioning limb MET (GLD Commodities/Metals and VXX Structured/Hedge on Positioning equal the list and the BD page; PHYS shown on no Positioning surface) -- FWD-1 REALIZED WHOLE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_SECCLASS PRD FWD-1 ACCEPT 'the same as Positioning shows them'; CTO round-24 analysis section 4 item 2; CTO msg 5524.",
    "world_is": "ROUND 24 L9 ADDENDUM, FWD-1's 'same as Positioning' limb: MET; FWD-1 WHOLE: REALIZED, on the CTO's round-24 analysis section 4 item 2 ('Equal on all three -> FWD-1 REALIZED whole') as ruled by msg 5524 ('the Positioning limb reads on the tickers Positioning shows ... PHYS is carried by the list row plus the BD page'). Record POSITIONING_LIMB_READ_20261014.md @fa25598ca0 (blob 0cbaccc96807, verified), msg 5528. This seat's own reads: (1) screenshots read here: Satellites, Satellite 15 Holdings Breakdown 'Commodities | Metals | GLD | SPDR Gold Shares | 8.06' (tmp/ui-walk/20261014T123329Z/shots/002); Satellite 90 Holdings Breakdown 'Structured | Hedge | VXX | 1.75' (tmp/ui-walk/20261014T123628Z/shots/003); Models AGG treemap VXX 1.6 percent in the Structured colour, no Commodities class on Models (tmp/ui-walk/20261014T123205Z/shots/001). (2) the Models sub-class the capture cut: the served Models data s3://opal-data-portal-v2/json/positioning/positioning_data.json (VersionId uztfAV7igP0lNBE3Liqpe7yZG98X.6iA, 2026-10-14T11:06:02Z, before the 12:32Z walk) carries VXX asset_class Structured, sub_asset_class Hedge (3 of 3 current_holdings entries) and no GLD or PHYS entry. (3) the CTO's build condition: git -C portal diff origin/PROD (6a5926fc11) 0a06280a40 -- src/pages/Positioning src/components/holdings: 0 lines; the walk's netlog shows GET 200 /api/general/positioning/positioning_data.json and holdings_attribution_data.json (3 each). COMPARISON: GLD Positioning Commodities/Metals = list commodities/Metals = BD page (D1-C-S21); VXX Positioning Structured/Hedge on Satellites and in the Models data = list structured/Hedge = BD page; PHYS shown on neither surface, list row = BD page commodities/Metals. No difference on any ticker Positioning shows. Not shown: that Positioning takes its class from the list rather than the portal's own constants (the render equals; FWD-4's copies are its own outcome); Satellites 40-80 not read for PHYS. FWD-1 REALIZED WHOLE: the Black Diamond page half (D1-C-S21) and this limb.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read tmp/ui-walk/20261014T123329Z/shots/002, 20261014T123628Z/shots/003, 20261014T123205Z/shots/001",
        "3.0.0_SA_CVO s3api get-object opal-data-portal-v2 json/positioning/positioning_data.json VersionId uztfAV7igP0lNBE3Liqpe7yZG98X.6iA: VXX Structured/Hedge",
        "3.0.0_SA_CVO git -C portal diff origin/PROD 0a06280a40 -- src/pages/Positioning src/components/holdings: empty",
        "tmp/ui-walk/20261014T123628Z/netlog.tsv: GET 200 positioning_data.json x3, holdings_attribution_data.json x3",
        "org/mcp/inbox/2.0.0_SA_COO/~M1/read/20261014T124556Z_1.0.0_SA_CTO_DELL1_Re_5523__YES_--_the_Positioning_limb_rea.md (msg 5524)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record: FWD-1 REALIZED whole."
  }
]
```
