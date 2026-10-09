# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v5 (site Z) -- THE ROUND-5 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-09 ~15:0xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 5 is terminal: 4 of 4 orders complete with VALID proofs (packet `ledger/COMPLETION_REPORT.round5.json` @8edf605068).

**L9:** AC4 graded at `ADJUDICATION_v1.md`:
- C-S22: TO-IAM-v-1 PASS.
- C-S23: **TO-IAM-v-2 FAIL**.
- C-S24: TO-IAM-v-3 PASS.
- C-S25: TO-IAM-v-4 PASS.

**L8:** C-S26 dispositions the 5 open rows: 2 dismissed and 3 graduated, below.

**For the CTO's round-5 analysis.**
- **FWD-5 is EXERCISED and graded.** The DescribeSecret narrowing on smartx-assets-pull-role was predicted first, read
  in its window and matched the prediction. DescribeSecret is absent from the live policy today.
- **FWD-4's adoption path is not cuttable for four accepted roles (v-2 FAIL).**
  - Rows 3 and 16 belong to no family in ADOPTION_PLAN_TEN.md.
  - Row 6's custody home is left an open question.
  - Family D proposes no home.
  - Name those homes, or rule those roles retire or deferred, before the round that cuts adoption cells.
- **Two production defects found in passing**: smartx daily pull, 30 of 30 runs failing; etfs-canon-fanin writing to a
  deleted table. Each needs an owner beyond this project. They are routed here, not fixed.

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-W13-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "smartx-assets-daily-pull raises DirtyRunError (feed9 reconciliation, PARTIAL identity table) on every daily run, so the bronze delta never reaches its OnSuccess silver converter.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_IAMROLES202609-Z-W13-S1: 30 of 30 log streams 2026-09-09..2026-10-08, one DirtyRunError each at lambda_function.py:265, after the auth path ran.",
      "Z-S20: outside this project; carried into v-4 only as the baseline its outcome was read against."
    ],
    "remedy": "Route to the smartx-assets pipeline's owner: the feed9/feed5 identity reconciliation. Not an IAM fix.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v5",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~ZI", "round": "v5"},
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~ZI", "at": null},
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W13-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "DynamoDB table opal-etfs-ownership-daily was deleted 2026-08-07; its only writer, the ENABLED daily Lambda etfs-canon-fanin, fails BatchWriteItem every run, while etfs-canon/fanin-lambda.tf still declares the table, the grant and the schedule.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_IAMROLES202609-Z-W13-S2: describe-table ResourceNotFoundException; CloudTrail DeleteTable 2026-08-07T17:58:10Z by a console user; 7 ResourceNotFoundException errors in 3 days."
    ],
    "remedy": "Route to the ETFS_CANON owner: either retire the schedule and declaration, or restore the table. The delete was a console act, so which was intended is the owner's question, not this project's.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v5",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~ZI", "round": "v5"},
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~ZI", "at": null},
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W13-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "preflight-blast-radius.py's [2a] negative control reads UNKNOWN on a role with a conditioned statement (missing context), and its PREDICTION block counts every allowed resource as a WOULD BREAK caller path without joining section [3]'s usage plane.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_IAMROLES202609-Z-W13-S3: on smartx-assets-pull-role, iam:CreateUser read UNKNOWN (missing s3:prefix), and 'WOULD BREAK 5' printed for an action Access Advisor reads never-used with 0 DescribeSecret."
    ],
    "remedy": "Supply or neutralise the condition context keys for the negative control, and join section [3]'s usage before printing WOULD BREAK.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~Z", "round": "v5"},
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
