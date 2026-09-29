# IRPT_BCKEND -- project sweep 1 remediations

Author: 3.0.0_SA_CVO, 2026-09-29. Graduated at sweep 1's L9 (ADJUDICATION_v15.md). Priority is in each remedy. Evidence detail: org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md.

```json
[
  {
    "id": "IRPT_BCKEND-S194",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The first live Comparison certified READY while its PDF prints only the client portfolio; the resident sent the client portfolio alone in security_ids (S196).",
    "evidence": [
      "rows S194, S196",
      "TO-IB-yr-201 (comparison names its models) status complete",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: closes when the yr-201 fix is SERVED and one live Comparison PDF prints the chosen model, with certification refusing a Comparison whose PDF prints none of the chosen models.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v22"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S193",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "resolve_upload waits a 900 s retain while generation holds the vendor session, so uploads outlive the walker's wait and get no body.",
    "evidence": [
      "row S193",
      "TO-IB-yr-211 complete (RETRY logged with its code)",
      "TO-IB-yr-221 pending (RETRY bounded below the DLQ)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: closes when yr-221's bound is served and a window's uploads all resolve inside the walker's wait, measured.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v22"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S199",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The cot login box can exit rc=0 after an unguarded smPut failure, leaving a stale secret; 49F has the F2 persist-binding, cot does not.",
    "evidence": [
      "row S199",
      "TO-IB-m21-212 amendment 3 (b986145750): the cot port carries 49F's F2 persist-binding; order pending",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: closes when m21-212 is served on the cot box and a forced persist failure exits non-zero.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v22"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S195",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 49F holdings gold prices every cusip-less position by one shared key and keeps OK rows with r <= -1 over a margin-debit base; chained, 18 accounts read about 1e57 YTD.",
    "evidence": [
      "row S195",
      "PRD v0.20 rulings 13-17 (613bfc6ecf)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1 (arms the moment the holdings adapter serves): re-emit the gold under rulings 13-17 and read back the S195 accounts before the adapter switch serves.",
    "owner": "0.4.0_DS_ClientPlatform~E",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "0.4.0_DS_ClientPlatform~E",
      "round": "v22"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S200",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A one-day price glitch voids the day it crosses the band but not the reversion day, so a ~$1.9M relationship would read 1Y -91.5% against YTD +7.7%.",
    "evidence": [
      "row S200",
      "PRD v0.21 ruling 18 (c0c0ae5606): a NOT COMPUTABLE day voids the next trading day too",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1 (arms with the adapter switch): implement ruling 18, re-emit, and read back account ..0090 and ..4714 before the switch serves.",
    "owner": "0.4.0_DS_ClientPlatform~E",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "0.4.0_DS_ClientPlatform~E",
      "round": "v22"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S189",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 49F Schwab silver disagrees with itself on position totals for 0.45% of account-rows (worst $4.93M); the gold does not read the disagreeing field.",
    "evidence": [
      "row S189",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: before any FWD-13 comparison reads dim_balance, name which total is authoritative (the silver owner's word).",
    "owner": "2.0.0_SA_COO~M",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v22"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S197",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The ruled worker-slot allocator counts committed authors only, so two issuers in one drain gap can take the same slot (~66).",
    "evidence": [
      "row S197",
      "row S187's remediation (REMEDIATION_v10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: take max over author lines, every non-terminal order's issued_to, and live wk-IRPT_BCKEND-n branches.",
    "owner": "1.0.0_SA_CTO",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v22"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W69-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Orders name .tools/terraform.exe, an untracked binary absent from every worker worktree.",
    "evidence": [
      "row W69-S1",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: vendor the binary into worker worktree provisioning, or write orders against the PATH terraform.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v22"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W69-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An untargeted portal-auth plan shows pre-existing WAF drift on known-bad-inputs (visibility_config/rule).",
    "evidence": [
      "row W69-S2",
      "rows S130/S133 (the benign managed_rule_group version diff, a different attribute)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: the portal-auth owner names whether this is the S133 class or new drift, before the next untargeted apply.",
    "owner": "1.0.0_SA_CTO",
    "round": "v22",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v22"
    },
    "closed": false
  }
]
```
