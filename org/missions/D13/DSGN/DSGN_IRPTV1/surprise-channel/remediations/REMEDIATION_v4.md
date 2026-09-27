# DSGN_IRPTV1 -- remediation v4 (the slug: round 8)

Author: 3.0.0_SA_CVO. Round: v4. Fabric: laptop. Recorded: 2026-09-27T21:45:04Z.

Adjudication: `ADJUDICATION_v6.md` (round 8: C-S54..C-S60).

**5 rows.** W36-S2 and W38-S1 are REMEDIATED and DISARMED, verified at local portal DEV 3b98939b. W34-S1 and W35-S2 are OPEN with
2.0.0_SA_COO~D for round 9; W35-S1 is OPEN with 1.0.0_SA_CTO.

**Closed in place in REMEDIATION_v3 at this commit:** W29-S8 (2026-09-27T13:04:50Z, merge 3e54ec31), W29-S9 (2026-09-27T15:32:06Z,
merge c66f980c) and S19 (2026-09-27T20:00:23Z, origin/CLOUD 0f4b3f876f). Still OPEN in place: S7 (v2), W21-S2, W23-S1 and W29-S10 (v3),
per C-S60.

```json
[
  {
    "id": "DSGN_IRPTV1-W34-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "fe-s-45/residuals.test.ts fails intermittently under the pinned full-suite runner (dev-server/OS-process timing), outside S7's Q rows.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W34-S1",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~34/DSGN_IRPTV1.TO-IV-e-55.pinned-runner.proof_of_spec.json@597cc0cc69 controls.determinism (sample A: 1 of 3)",
      "portal: git diff 3e54ec31 3b98939b over fe-s-45/ and scripts/dev-live.mjs is empty"
    ],
    "remedy": "A round-9 cell granted __tests__/fe-s-45/dev-script-writes.mjs removes the timing hazard; then one pinned 3-run sample on the drained tree gives an identical failing set within the Q rows. S7, W21-S2, W23-S1 and W29-S10 close on that same sample.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v4"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-W35-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The naming gate refuses a hand-typed firm-token literal in .ts with no builder exemption; IV-e-56 delivered through a token-free title-case transform instead.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W35-S1",
      "portal 3b98939b:src/pages/InvestorReporting/header/firmDisplay.ts:36-61",
      ".tools/naming-gate.py last changed 33af10616f (2026-09-23): js_literals() has no call-context check"
    ],
    "remedy": "1.0.0_SA_CTO decides: an R20 register entry naming a sanctioned firm display-name source, or a JS/TS builder-call exemption in naming-gate.py (0.0.0_AB_MSTR). Until then a firm whose display name is not its key in title case renders wrong.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-W35-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Export on Analysis is permanently closed because AnalysisTab.tsx passes no answer-bearing signal to index.tsx.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W35-S2",
      "portal 3b98939b:src/pages/InvestorReporting/index.tsx:270",
      "portal 3b98939b: AnalysisTab.tsx has 0 onExportTarget"
    ],
    "remedy": "A round-9 cell granted tabs/analysis/AnalysisTab.tsx threads an onExportTarget-shaped signal to index.tsx:270, with a test that Analysis with an answer-bearing report enables Export.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v4"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-W36-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-66's tenant-aware row-status read added a getJobStatus call site outside F54-AC2's frozen census of 2.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W36-S2",
      "portal a5107226 (ancestor of 3b98939b): fe-s-54/stated-state-wins.test.ts toBe(2) -> toBe(4)",
      "portal: git grep 'getJobStatus(' 3b98939b -- src: OwnedRequestHistory.tsx:26,33, ProspectJobStatus.tsx:7,18"
    ],
    "remedy": "Executed at the round-8 drain (a5107226): the census re-goldened to the measured world, one of the two remedies the row names.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v4"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T18:14:08Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W38-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-61's amendments broke one hardcoded old-literal assertion each in iv-e-42.drill-bases and iv-e-44.securities-map, outside the cell's grant.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W38-S1",
      "portal 71896c93 (ancestor of 3b98939b): 2 files +26/-9, new negative arms ('% of total' absent; tile colour not any asset-class colour or the legend swatch)"
    ],
    "remedy": "Executed at the round-8 drain (71896c93). Round-9 item: the UIR-47 arm builds its donut tooltip from the row's own words; mount the real DrillTree donut hover there.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v4"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-27T17:38:27Z"
    }
  }
]
```
