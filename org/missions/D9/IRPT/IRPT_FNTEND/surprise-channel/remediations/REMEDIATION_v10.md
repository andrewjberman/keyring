# IRPT_FNTEND round 13 - one L10 remediation slug

Author: `3.0.0_SA_CVO~F`. Reader: **1.0.0_SA_CTO only**.

84/84 task orders terminal and structurally valid; five round-13 instances contain 30 criteria (26 mechanical, four judgment). Judgment: three PASS, F80-AC6 FAIL. Own current suite: **648 pass / 27 skip / 2 fail**. The two failures are committed sibling fixtures missing unprojected_grant, despite the worker recorded regeneration succeeding.

Four OPEN remedies in this slug: existing W25-S1, C-S147, C-S150, plus new C-S176. Eight bounded remedies closed. W31-S1 was already disposed at C-S167; its regex amendment stays closed and does not excuse missing outputs. No project/outcome closure or production claim. Portal remains LOCAL/frozen; no push, deploy or gitlink change.

Basis: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md`, ADJUDICATION_v5 C-S167..177, co-committed probes and retained evidence. CTO owns coverage judgment and round-13 analysis; COO owns the recut. No route token is invented.

Five existing remediation clocks advance in their original v8/v9 documents in this commit: W17-S1, W27-S2, W27-S3, C-S164 and C-S165. Their original content and round stay unchanged. The three existing OPEN clocks W25-S1, C-S147 and C-S150 also stay unchanged; new evidence is in C-S173..175. The four new JSON records below plus these eight reviewed existing clocks comprise the four OPEN / eight closed summary.

```json
[
  {
    "id": "IRPT_FNTEND-W33-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Three local route/hover/absence defects corrected by issuer 6d3b2e4d92.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
      "portal@467354c947c1afebc77eb6839724c7243547f46f",
      "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
    ],
    "remedy": "Retain actual route, real hover driver and genuine absent-tab control; do not describe AC4 as focus-ring acceptance.",
    "owner": "2.0.0_SA_COO~F",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~F",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~F",
      "at": "2026-09-22T13:41:31Z"
    }
  },
  {
    "id": "IRPT_FNTEND-W32-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Depth and selectors corrected by issuer 6e3d50ab44; own measured 700/400.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
      "portal@467354c947c1afebc77eb6839724c7243547f46f",
      "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
    ],
    "remedy": "Retain real drill and current-span/ancestor-button discrimination.",
    "owner": "2.0.0_SA_COO~F",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~F",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "IRPT_FNTEND-W34-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Missing fixture path corrected by issuer 6e3d50ab44; qualified state independently measured.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
      "portal@467354c947c1afebc77eb6839724c7243547f46f",
      "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
    ],
    "remedy": "Retain committed qualified fixture and exact amended binding.",
    "owner": "2.0.0_SA_COO~F",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~F",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~F",
      "at": "2026-09-22T13:41:31Z"
    }
  },
  {
    "id": "IRPT_FNTEND-C-S176",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The orders require five visual controls while results waive actual-ground controls and report partial fulfilment.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
      "portal@467354c947c1afebc77eb6839724c7243547f46f",
      "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
    ],
    "remedy": "Reconcile the common acceptance contract explicitly in the next cut: applicable controls must be executable and recorded; distinguish declared-key validity from exercised fulfilment. No retroactive silent N/A waiver.",
    "owner": "2.0.0_SA_COO~F",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~F",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~F",
      "at": "2026-09-22T18:40:59Z"
    }
  }
]
```
