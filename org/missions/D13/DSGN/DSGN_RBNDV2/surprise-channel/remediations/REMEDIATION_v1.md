# DSGN_RBNDV2 -- remediations, v1

<sweep_watermark>2026-10-15T07:45Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-15 ~07:4xZ, at the round-1 close. Graduated in ADJUDICATION_v1.md C-S3 and C-S6. Six rows: four ARMED, each carried to a named later act (owner 2.0.0_SA_COO~RB); two BLOCKING INERT premise rows for the CTO (W4-S1, W4-S2).

```json
[
 {
  "id": "DSGN_RBNDV2-W1-S1",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The theme header names a regeneration that does not reproduce the committed design/themes/opal-capital.css. The cell set the four canvas lines (--palette-canvas, --semantic-background-default, -mediumAlt, -hoverLight) by hand to the generator's value; a full generator run would rewrite the file.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W1-S1",
   "adjudication row DSGN_RBNDV2-C-S3"
  ],
  "remedy": "P2. Reconcile the generator with the committed theme, or retire the header's claim, before any design build rewrites design/themes/opal-capital.css. Done when one generator run reproduces the committed file byte for byte, or the header no longer claims it does.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~RB",
   "round": "v1"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~RB",
   "at": null
  },
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W1-S2",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The light-panel legibility rule keys on the panel scope and the class text alone, so a text-white element on a solid coloured fill inside a light panel also takes navy-black ink. Its contrast on that fill is unmeasured.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W1-S2",
   "adjudication row DSGN_RBNDV2-C-S3"
  ],
  "remedy": "P2. The FWD-5 walk (round 3) measures every text-white on a solid fill inside a light panel and repairs each at the page cell that owns it. Done when that walk reads no such element under 3:1.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~RB",
   "round": "v1"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~RB",
   "at": null
  },
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W5-S2",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The scoped palette remap ([data-panel-surface=light]) turns every palette-mediumGray inside a light panel into navy ink, including five status-dot fills (four partner-page dots and the ExecManagementTab dot), so an idle grey dot reads as navy.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W5-S2",
   "adjudication row DSGN_RBNDV2-C-S3"
  ],
  "remedy": "P3. At the FWD-5 walk (round 3), decide whether the status dots keep the quiet ink or take a fill token. Done when the five dots read their intended state on the walk.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~RB",
   "round": "v1"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~RB",
   "at": null
  },
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W2-S3",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The account-menu popup in App.tsx keeps its dark styling (bg-header, white/10 border, text-white/80) beside the light sidebar. If --bg-header is repointed light, its text becomes near-invisible (the S1 class). Its width calc still assumes the old w-56 sidebar.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W2-S3",
   "adjudication row DSGN_RBNDV2-C-S3"
  ],
  "remedy": "P2. Round 2's C-MODAL cell restyles the account-menu popup to the light frame. Done when the popup reads on the light ground at the round-2 drain.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~RB",
   "round": "v1"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~RB",
   "at": null
  },
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W4-S1",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "FWD-4 ('heat maps shade from white to silver instead of blue') has no blue to replace in the eight F10 heat files at ad7c100b5c. They shade with emerald/red/yellow overlays, traffic bins and diverging pink/green, and ReturnsHeatmap does not shade.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W4-S1",
   "adjudication rows DSGN_RBNDV2-C-S1, DSGN_RBNDV2-C-S6"
  ],
  "remedy": "P2. 1.0.0_SA_CTO answers with a PRD addendum to FWD-4, after Andrew's design call on the live page, naming what the eight files shade with. Done when FWD-4's text names a target the eight files actually hold and RB1H-AC3 is re-graded against it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W4-S2",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Two heat maps shade diverging (positive vs negative) cells. A single white-to-silver ramp carries magnitude only, so sign needs a second hue (which the cell forbids) or a non-colour cue (which it does not name).",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W4-S2",
   "adjudication row DSGN_RBNDV2-C-S6"
  ],
  "remedy": "P2. The same FWD-4 addendum states how sign is carried (a second hue, a glyph or a sign label). Done when the addendum names the sign cue.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
