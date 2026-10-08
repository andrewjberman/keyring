# MDPF_SECHIST -- round 1 remediations, re-issued under their investigation ids

<sweep_watermark>2026-10-08T13:19Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-08T13:19Z. **REMEDIATION_v1 is SUPERSEDED by this file**, and v1 is not edited because the file is append-only.
v1 gave its two graduated rows the ids MDPF_SECHIST-S1 and MDPF_SECHIST-S2, which collided with the investigation rows S1 (BDay(-1) as-of)
and S2 (served sector, dismissed in ADJUDICATION_v2). Ruling: 1.0.0_SA_CTO~DELL1 round-1 analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECHIST_ROUND_1_20261008.md` @0141533760 section 2.1: a remediation row's
id IS the investigation row it graduates. v1 "S1" is W1-S1 and v1 "S2" is W2-S1. Content is unchanged apart from the id and one
evidence line. Investigation S1 graduates under its own id when its time comes.

```json
[
  {
    "id": "MDPF_SECHIST-W1-S1",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The depth need rule (earliest stored date later than asof - 365 days) never converges for a security whose real history is shorter than a year or which has no vendor series, so it is re-planned every run and spends one request and one cap slot for zero rows.",
    "evidence": [
      "integrations/bloomberg/pipeline/etf_daily_pull.py:59 DEPTH_NEED_DAYS = 365; :240-245 history_backfill_plan, read at dell1 HEAD by this seat",
      "investigation row MDPF_SECHIST-W1-S1 (0.9.0_WK_MDPF_SECHIST~1): plan_only() live read names 2602335D, PFDE, PFOE; 15 needing of 172",
      "re-issued from REMEDIATION_v1 entry MDPF_SECHIST-S1 (a7010ab13e) under the id of the investigation row it graduates, per 1.0.0_SA_CTO~DELL1 round-1 analysis @0141533760 section 2.1"
    ],
    "remedy": "Round-2 enrichment for 1.0.0_SA_CTO~DELL1 to read: a bound on re-planning (for example, a manifest-recorded 'requested, nothing older exists'). Close when a second plan_only() run after one backfill no longer names those three, or the CTO rules the cost acceptable under the cap.",
    "owner": "2.0.0_SA_COO~H1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~H1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~H1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECHIST-W2-S1",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two of the sibling etf_positioning gold tests, the keep-passing regression for any gold edit, fail at import when run bare from the gold folder: etf_positioning_publisher.py:66 imports etf_classifications_dynamodb, which is tracked only under infra/aws/lambda/v2_portal/.",
    "evidence": [
      "reproduced by this seat 2026-10-07 08:3xZ on dell1 CLOUD: cd data/etfs/scripts/gold; test_etf_positioning_upgrade_forward.py rc=1 and test_etf_positioning_per_fund_asof.py rc=1, ModuleNotFoundError etf_classifications_dynamodb; control test_etf_positioning_industry_group.py rc=0",
      "git ls-files: etf_classifications_dynamodb.py under infra/aws/lambda/v2_portal/_shared/ and two yang_pipeline/positioning lambda folders only",
      "investigation row MDPF_SECHIST-W2-S1 (0.9.0_WK_MDPF_SECHIST~2)",
      "re-issued from REMEDIATION_v1 entry MDPF_SECHIST-S2 (a7010ab13e) under the id of the investigation row it graduates, per 1.0.0_SA_CTO~DELL1 round-1 analysis @0141533760 section 2.1"
    ],
    "remedy": "Before a later round edits etf_positioning gold, make the two tests runnable from a clean worktree (a path insert in the tests, or the documented invocation that carries _shared). Not caused by round 1, which made no gold edit to the publisher. Close when both read rc=0 from a clean worktree.",
    "owner": "2.0.0_SA_COO~H1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~H1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~H1",
      "at": null
    },
    "closed": false
  }
]
```
