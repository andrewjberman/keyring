# IRPT_BCKEND -- project sweep 2 remediations

<sweep_watermark>2026-09-29T09:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-29. Graduated at sweep 2's L9 (ADJUDICATION_v16.md).

```json
[
  {
    "id": "IRPT_BCKEND-S202",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two tracked ec2 .env files (bd-49f-auto-login/secret-ids.env, smartx-exporter/config/production.env) have LF blobs, no eol rule, and CRLF working copies; a deploy that uploads a working copy puts a trailing CR on every sourced value.",
    "evidence": [
      "rows S201, S202",
      "git check-attr eol: bd-49f-auto-login/secret-ids.env unspecified (read 12:1xZ)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP2_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P2: one .gitattributes rule (infra/aws/ec2/**/*.env text eol=lf) plus a renormalize of both working copies, cut by ~M; disarm when both check-attr read lf and both working copies carry 0 CRs.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v23",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v23"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S204",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The 49F holdings switch (adapter hD7G6YT1, 10:14Z) failed every ruled-period read (YTD/QTD/1Y) on ModuleNotFoundError 'parity_period_returns': _holdings_source dropped the runners_49f sys.path insert; since-inception short-circuited, so the cold-start smoke passed.",
    "evidence": [
      "row S204",
      "rollback commit 9e0bde13e3 (2026-09-29T11:06:10Z): the switch rolled back to qfxZ0DzB",
      "TO-IB-pr-201 amendment 2 drained 66469ce943 (build_runtime puts runners_49f on sys.path)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP2_REVIEW_20260929.md (co-committed)"
    ],
    "remedy": "P1: re-switch on the amendment-2 build with (a) a cold-start invoke that requests a RULED period, and (b) the CTO's served-figure census from the adapter (msg 102704): no YTD/1Y/SI at or below -100%, every figure at or above +100% named; then the CRO walk.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v23",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v23"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-09-29T11:06:10Z"
    },
    "closed": false
  }
]
```
