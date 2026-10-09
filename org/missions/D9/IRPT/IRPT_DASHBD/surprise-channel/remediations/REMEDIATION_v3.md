# IRPT_DASHBD -- rounds 5 to 9 (workstream B) remediations

<sweep_watermark>2026-10-03T01:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-03 ~02:4xZ. 9 rows graduated at ADJUDICATION_v3.md. Closed here on this seat's read: W3-S1. OPEN in the issuer's P-2 packet: W1-S12, W1-S13, W1-S14, W1-S18, W1-S19 with W2-S3, W4-S1, W4-S2. W1-S17 is in no cell and goes to 1.0.0_SA_CTO for placement. Round label v10 (the round after the compiled round 9). Carried and not moved here: S8 (REMEDIATION_v1, OPEN, owner 1.0.0_SA_CTO; the row gate discloses it as stale for 2 or more rounds); S12, S15, S18, S19, S20, W1-S7 and S22 (REMEDIATION_v2, OPEN). S22's diagnosis changed: the cause of its 1.21 pp pair was W1-S18's missing margin balance, not the short-income sign (batch 193); its residual 0.4738 pp is stated RETURN by batch 195. It closes on W1-S18's served read.

```json
[
  {
    "id": "IRPT_DASHBD-W1-S12",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "reporting-publish takes its account set from the newest gold partition, and an account with no positive value that day has no row, so 885 of 7,570 accounts in the 2026-10-01 holdings population (875 NO-PRIOR-HOLDINGS) get no manifest or series; P-1 names every 49 Financial client.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S12",
      "deliverables/0.9.0_WK_IRPT_DASHBD~1/P2_SCALE_R5.json population and producer blocks"
    ],
    "remedy": "P-2 PACKET (issuer): decide whether a closed or unfunded account with earlier history is published (union of accounts across gold partitions) or stated absent on the page; P-1's 'every client' is read against the answer at the P-2 real run.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W1-S13",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "reporting-publish is deployed at 300 s and 1024 MB; the whole-population publish needs ~450 s and 1,582 MB in one invoke, so it shards (8 invokes) and self-invokes once per shard, which needs lambda:InvokeFunction on its own ARN.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S13",
      "infra/aws/terraform/investor-reporting/reporting-publish/iam.tf at HEAD: statement InvokeOwnFunctionForShardFanOut (lambda:InvokeFunction) is TEXT, not applied (this seat's read ~02:3xZ)",
      "infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf:44 timeout = 300"
    ],
    "remedy": "P-2 PACKET (issuer): apply the own-invoke grant with the publish deploy; closed on the first scheduled sharded fire's REPORT lines (8 shards, each under 300 s).",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W1-S14",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The account-set widening adds the population from the next day only; the 562 landed partitions hold 6 accounts, so history for the other ~7,560 accounts is a rewrite of 562 served partitions, a never-widen act.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S14",
      "deliverables/0.9.0_WK_IRPT_DASHBD~1/P2_SCALE_R5.json backfill.plan (23 chunks of <=25 days, in-region, under a ledger, DELTA=0 on the 6 served accounts)"
    ],
    "remedy": "P-2 PACKET (issuer): the backfill under a change-management ledger and a never-widen sign-off (CTO+COO) naming the 562 partitions, with DELTA=0 on the 6 served accounts read back.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W1-S17",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The short-dividend income fix admits debit legs of QDV, NDV and PDV only; 38 DIV debits on short accounts in 2026 (822.51 absolute) stay out of the served per-day income field, because separating them from one long-fund zero-share row needs dividend_interest_share_quantity, which sources.json does not declare.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S17",
      "deliverables/0.9.0_WK_IRPT_DASHBD~1/SHORT_INCOME_INVARIANCE_R6.json",
      "org/standards/IRPT_DASHBD_SERIES_CONTRACT.json at HEAD: income is a served per-day field (source income_received); total_return_daily does not read it"
    ],
    "remedy": "IN NO CELL: declare the share-quantity column and admit a DIV debit only when it is negative; no return moves. Placement is 1.0.0_SA_CTO's at the round analysis.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W1-S18",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "C-VALUE was net_mv_plus_cash, which leaves out the Schwab margin_balance that the custodian's equity and Black Diamond's value include; every margin account's served return is off by the margin share of value. Ruled by batch 193 (equity = net_mv_plus_cash + margin_balance, method_version 2); built and re-measured in DB-b-15; the served gold is still version 1.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S18",
      "1.0.0_SA_CTO RULINGS batch 193 @ff04f71e47: 'W1-S18 is DISARMED by this ruling. This seat is its disarm owner.'",
      "DB-b-15 merged @ce1d4a0530: sources.json account_value_columns [net_mv_plus_cash, margin_balance], METHOD_VERSION 2; drain-end record :53-60 'Nothing is served'",
      "this seat's FWD-8 round-8 grade @a108c6bd93: equity at acct#89d0916a's window endpoints re-read from Schwab silver, BD value minus accrual minus equity 0.00 at both"
    ],
    "remedy": "P-2 PACKET (issuer): producer re-pin at method_version 2, every landed gold day rewritten under version 2 (the publisher refuses mixed versions), the method row written; closed when this seat reads method_version 2 on served gold rows and reproduces one pair. Row S22 (REMEDIATION_v2) closes on the same read.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-02T23:58:17Z"
    }
  },
  {
    "id": "IRPT_DASHBD-W1-S19",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The method row writes tieout_tolerance, tieout_tolerance_ruling (W1-S19), value_basis and value_basis_ruling (W2-S3), four columns the dim_return_method contract 0.2.0 does not declare, so its schema_hash is stale for the next write; a run without --tieout would also null the landed tieout_tolerance_proposed.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S19",
      "investigation row IRPT_DASHBD-W2-S3 (same shape, same remedy)",
      "org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json at HEAD: 18 columns, none of the four"
    ],
    "remedy": "P-2 PACKET (issuer): contract 0.3.0 (four columns, new schema_hash, rule-24 record) in the same commit as the method-row write, run with --tieout 0.037 so the landed proposal is kept.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W2-S3",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "emit_method_row writes value_basis and value_basis_ruling, which the dim_return_method contract does not carry; the publisher refuses a file of mixed method_version (publisher.py:173), so every landed gold day must be rewritten before version 2 is served.",
    "evidence": [
      "investigation row IRPT_DASHBD-W2-S3",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py emit_method_row at HEAD"
    ],
    "remedy": "With W1-S19: one contract bump in the P-2 packet.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W3-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "DB9-1-AC2 could not pass while test_reporting_entry.py asserted len(entry.ROUTES) == 1, a file outside the order's paths.",
    "evidence": [
      "investigation row IRPT_DASHBD-W3-S1",
      "2.0.0_SA_COO~P amendment @f1acd596eb granted the file for its one assertion",
      "infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_entry.py:74 at HEAD asserts the exact two-route set; this seat's run of reporting/tests at HEAD ~02:3xZ: 21 passed"
    ],
    "remedy": "Done: the assertion is the exact two-route map, and the suite passes 21 of 21 on this seat's run.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W4-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The summaries pass needs _ids/ids.py, raw_keys.json, data/custodian_key_seam.json and data/firm_registry.json and the directory bucket at run time; the irpt-reporting-publish-lambda package map lists none of them and lambda.tf sets no IRPT_DIRECTORY_BUCKET_MAP, so the deployed pass refuses by name.",
    "evidence": [
      "investigation row IRPT_DASHBD-W4-S1",
      "infra/aws/lambda/ci/lambda-source-map.json at HEAD: the publish entry names no ids.py, raw_keys or firm_registry (this seat's read ~02:3xZ)",
      "deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND9_B_DRAIN_END_20261003.md Rows: 'it binds the P-2 packet'"
    ],
    "remedy": "P-2 PACKET (issuer): stage the four files as packaged_as paths in the publish entry (ids.py at the zip root, as the read entry does) or set the variable; closed on the first deployed summaries fire writing at least one summary read back through the route.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W4-S2",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The order budgeted 900 s; reporting-publish runs at 300 s, and the summaries projection (~140 s per shard of ~300 clients) rests on laptop latency, an upper bound, not an in-region measurement.",
    "evidence": [
      "investigation row IRPT_DASHBD-W4-S2",
      "deliverables/0.9.0_WK_IRPT_DASHBD~4/READ_COST_R9.json"
    ],
    "remedy": "P-2 PACKET (issuer): the first deployed summaries fire's REPORT lines are the measurement; closed when every shard reports under 300 s.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v10"
    },
    "closed": false
  }
]
```
