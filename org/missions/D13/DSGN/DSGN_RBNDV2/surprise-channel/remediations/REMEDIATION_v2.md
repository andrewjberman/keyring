# DSGN_RBNDV2 -- remediations, v2

<sweep_watermark>2026-10-15T10:50Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-15 ~10:5xZ, at the round-2 close. Graduated in ADJUDICATION_v2.md C-S9. Four rows, all ARMED. REMEDIATION_v1's rows stand as filed.

```json
[
 {
  "id": "DSGN_RBNDV2-W8-S1",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The pre-commit checks passed a portal .tsx commit having checked 0 of 3 files: the risk reflex scanned 0 of 3 with a STALE danger map, and commit-gate reads only .py/.sh/.tf/org/projects JSON. Every portal frontend commit on this branch is ungraded by the commit hooks.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W8-S1",
   "adjudication row DSGN_RBNDV2-C-S9"
  ],
  "remedy": "P2. 1.0.0_SA_CTO routes to the commit-gate and risk-reflex owner. Done when a portal .tsx commit prints a non-zero checked count from the risk reflex, or the hook says it does not grade .tsx.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v2"},
  "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W8-S6",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "ModalFrame's focus-on-open effect runs after React's autoFocus, so the autoFocus inputs of SecurityLookupModal and BulkEditModal likely lose focus to the dialog surface on open. The guard landed, checked by source text only.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W8-S6",
   "adjudication row DSGN_RBNDV2-C-S9"
  ],
  "remedy": "P2. The round-3 walk opens both modals and reads document.activeElement right after open. Done when the autoFocus input holds focus in both.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~RB", "round": "v2"},
  "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~RB", "at": null},
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W8-S9",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "RSIModal and FearGreedModal kept a literal dark content ground that the frame's token remap does not reach. FearGreedModal's ground now renders silver rgb(238,241,246) in the CVO's walk. RSIModal is unwalked, so its labels may still read navy on dark navy.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W8-S9",
   "adjudication rows DSGN_RBNDV2-C-S7, DSGN_RBNDV2-C-S9"
  ],
  "remedy": "P2. The round-3 walk opens RSIModal (its trigger is a chart bar; a --hover or a coordinate press). Done when its content ground reads light and its labels legible in that walk.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~RB", "round": "v2"},
  "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~RB", "at": null},
  "closed": false
 },
 {
  "id": "DSGN_RBNDV2-W8-S11",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "SessionTimeoutWarning hides the frame's Close control with an arbitrary-variant class on the surface, checked as class text only. If the variant does not emit, a dead X shows on a dialog that has no X by design.",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md row W8-S11",
   "adjudication row DSGN_RBNDV2-C-S9"
  ],
  "remedy": "P3. The round-3 walk renders the session warning and confirms there is no X. If one shows, the issuer rules a showClose option. Done when the walk shows no X.",
  "owner": "2.0.0_SA_COO~RB",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~RB", "round": "v2"},
  "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~RB", "at": null},
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
