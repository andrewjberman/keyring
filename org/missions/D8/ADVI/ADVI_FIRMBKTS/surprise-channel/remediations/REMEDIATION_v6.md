# ADVI_FIRMBKTS -- round 5 remediations (dell1)

<sweep_watermark>2026-10-13T07:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T07:40:00Z. Graduated at ADJUDICATION_v6: 11 rows. FWD-1 PARTIAL (D1-C-S39); FWD-4 PARTIAL, live half
(D1-S41).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S41",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "no non-admin session in hand for the validator's ownership read: the 17 organic lines on /platinum/accounts/ and /books/relationship/ since the edge leg are all tier=internal (admin bypass), so the validator's canonical ownership read has not been exercised by a non-admin request.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S41",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The CTO rules or places each: FWD-4's live half closes on the first organic non-admin validator line on the accounts or relationship paths (or a non-admin session a seat holds); the put-events cause on a runner-side read or one non-matching test event (a write, the CTO's word); the pricing evidence goes with the CRO brief on S32. Close when: the named read or ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W65-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "No CloudTrail PutEvents call exists in any of 17 enabled regions over 90 days, so the chain-complete put-events WARN never reached the events API: the failure sits upstream of EventBridge.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W65-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The CTO rules or places each: FWD-4's live half closes on the first organic non-admin validator line on the accounts or relationship paths (or a non-admin session a seat holds); the put-events cause on a runner-side read or one non-matching test event (a write, the CTO's word); the pricing evidence goes with the CRO brief on S32. Close when: the named read or ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-14T11:45:00Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W65-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "organizations list-policies (SERVICE_CONTROL_POLICY) is AccessDenied to cloudops-dell1-agent-user, so any SCP that could deny events:PutEvents is unreadable from this identity.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W65-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The CTO rules or places each: FWD-4's live half closes on the first organic non-admin validator line on the accounts or relationship paths (or a non-admin session a seat holds); the put-events cause on a runner-side read or one non-matching test event (a write, the CTO's word); the pricing evidence goes with the CRO brief on S32. Close when: the named read or ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W66-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Served canonical transaction_observed prices do not equal the current file median for 603 of 1,610 comparable rows over the 20 window dates, so a served T-1 value is not the median the code recomputes from the day partition.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W66-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The CTO rules or places each: FWD-4's live half closes on the first organic non-admin validator line on the accounts or relationship paths (or a non-admin session a seat holds); the put-events cause on a runner-side read or one non-matching test event (a write, the CTO's word); the pricing evidence goes with the CRO brief on S32. Close when: the named read or ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W66-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bd-price-update records no INFO step lines: the \"Step 1a\" filter returns zero events since 2026-09-02 while 35 invocations are recorded, so the reader at lambda_function.py:143 cannot be confirmed from its logs.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W66-S5",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The CTO rules or places each: FWD-4's live half closes on the first organic non-admin validator line on the accounts or relationship paths (or a non-admin session a seat holds); the put-events cause on a runner-side read or one non-matching test event (a write, the CTO's word); the pricing evidence goes with the CRO brief on S32. Close when: the named read or ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W66-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "silver/transactions has objects on weekend dates (for example 2026-10-10 and 2026-10-11), and the two most recent weekdays hold zero-row partitions (2026-10-12 and 2026-10-13, 35,269 bytes each), so \"the 20 most recent trading days that have an object\" needed a weekday rule to be defined.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W66-S6",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The CTO rules or places each: FWD-4's live half closes on the first organic non-admin validator line on the accounts or relationship paths (or a non-admin session a seat holds); the put-events cause on a runner-side read or one non-matching test event (a write, the CTO's word); the pricing evidence goes with the CRO brief on S32. Close when: the named read or ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W66-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The 2026-10-09 same-date price tie is non-decisive in the current file set: all 11,108 tied assets select a later-dated row, so the unstable sort does not decide the served 10-09 price. It is decisive only as of the 10-09 run (inferred: 3,906 of 11,108 alternative prices differ).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W66-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The issuer routes and cuts: the B_01 tie-break fix to the gold owner (W66-S2), and a harness mock list that covers the render-key branch (W63-S1). Close when: the routing record or the corrected harness names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v6"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W63-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two of my pre-harness probe runs reached the render-key Secrets Manager secret, outside the order's two-S3-read bound; the mock I used did not bind.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W63-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The issuer routes and cuts: the B_01 tie-break fix to the gold owner (W66-S2), and a harness mock list that covers the render-key branch (W63-S1). Close when: the routing record or the corrected harness names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S43",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "TO-FB-h-8: the cp1252 crash is fixed, but the fence-scoped check cannot read ok=True for four further reasons that are not the two named: the simulator is denied to this identity (31 of 31 arms), the pinned fence file's CRM selector fails over today's registry, two refusal arms no longer match the validator (5 of 7), and unchanged_today and scoped_rendered read stale against the registry's new `grants` field.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S43",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The infrastructure owner routes or fixes: D1-S43 to NFRA_CTLPLN's re-baseline (CTO msg 4674), the client-data list on dell1, the aws shim's worktree resolution. Close when: the owner's fix or routing names the row",
    "owner": "0.0.0_AB_MSTR",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W64-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On this device safe-commit's client-data check did not run: the hashed account-id list is absent, so the spec commit 7c6522bfe4 was not checked for client account ids.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W64-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The infrastructure owner routes or fixes: D1-S43 to NFRA_CTLPLN's re-baseline (CTO msg 4674), the client-data list on dell1, the aws shim's worktree resolution. Close when: the owner's fix or routing names the row",
    "owner": "0.0.0_AB_MSTR",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W66-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Every aws call from this worktree prints \"WARN: aws: no caller-toplevel .tools/aws (git rc=128) -- PREPENDING THE BAKED C:/dev/ajb_workspace/.tools\", so the shim resolves to the base checkout tools, not the worktree tools.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W66-S7",
      "adjudication row ADVI_FIRMBKTS-D1-C-S43"
    ],
    "remedy": "The infrastructure owner routes or fixes: D1-S43 to NFRA_CTLPLN's re-baseline (CTO msg 4674), the client-data list on dell1, the aws shim's worktree resolution. Close when: the owner's fix or routing names the row",
    "owner": "0.0.0_AB_MSTR",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  }
]
```
