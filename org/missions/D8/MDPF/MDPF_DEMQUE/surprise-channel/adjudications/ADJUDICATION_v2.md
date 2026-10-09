# MDPF_DEMQUE -- round 2 L8/L9 adjudication

<sweep_watermark>2026-10-09T03:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T03:20:00Z. No L8 packet reached this seat for round 2; compiled from the channel, the issuer's real run
`deliverables/2.0.0_SA_COO~Q1/FWD1_REAL_RUN_R2.md` and the CTO's round-2 analysis (msg 1520). 3 new rows swept: W7-S1 and W7-S2 dismissed
(their order superseded), D1-S1 graduated INERT to `remediations/REMEDIATION_v2.md`.

**L9 -- FWD-1 agreement clause (judgment, CTO msgs 1373/1520): MET on AMLP** (row C-S3). **FWD-1: NOT REALIZED** -- hop 7, the values on
acct#8039e07b's served page, is still owed by dell2's ADVI_COTBKF. The no-hand-pull clause is EXERCISED (scheduled fire 2026-10-09T02:30:01Z).

```json
[
  {
    "id": "MDPF_DEMQUE-C-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:20:00Z",
    "one_line": "FWD-1 'those prices agree with the prices the client actually traded at' is MET on AMLP: 3 of 4 of acct#8039e07b's fills within 2% (median 0.92%), and the 2020-03-12 miss (4.19%) is an intraday fill inside that day's move; across all accounts 100 of 108 trade dates agree (92.6%), which clears the CTO's 90 pct lock floor. FWD-1 stays NOT REALIZED until hop 7 (the served page).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "FWD-1 'those prices agree with the prices the client actually traded at' is MET on AMLP: 3 of 4 of acct#8039e07b's fills within 2% (median 0.92%), and the 2020-03-12 miss (4.19%) is an intraday fill inside that day's move; across all accounts 100 of 108 trade dates agree (92.6%), which clears the CTO's 90 pct lock floor. FWD-1 stays NOT REALIZED until hop 7 (the served page).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "dell2 2.0.0_SA_COO~C2 @14d4fc7049 AMLP_CONSUMER_READ_MDPF_DEMQUE_20261009.md: fills 2017-05-18 1.54%, 2019-07-03 0.20%, 2020-02-03 0.29%, 2020-03-12 4.19%",
        "3.0.0_SA_CVO read of s3://opal-data-assets/yahoo/global/silver/price_history/cusip=00162Q866/prices.parquet (3,323 rows; columns date, close_served, as_traded_close): as_traded_close 2020-03-11 4.65, 2020-03-12 3.84 (-17.4% on the day). The fill at 4.0010 lies between the prior close and the close, so it is a price the day actually traded through; the store holds closes only, so a close-vs-fill gap on that day is the measuring instrument, not the price",
        "FWD1_REAL_RUN_R2.md hop 2: AMLP LOCKED measured, 100 of 108 Commonwealth trade dates within band; CTO round-2 analysis msg 1520 ruling (2): lock only at >= 90 pct of trade dates within 2 pct",
        "Judgment of the 2 pct bar: for an exchange-traded fund the close-vs-fill gap on an ordinary day is a few tenths of a percent (3 of 3 ordinary-day fills here are 0.20-1.54%); 2 pct catches a wrong-security or wrong-split mapping, which moves prices by multiples, so it is a sound bar for 'agree' on the identity question FWD-1 asks"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 judgment record, not a hazard: FWD-1's agreement clause graded MET on AMLP; FWD-1 itself not yet realized (hop 7 open)."
  },
  {
    "id": "MDPF_DEMQUE-C-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:20:00Z",
    "one_line": "W7-S2 (BLOCKING/INERT) dismissed: its order DQ-t-8 closed SUPERSEDED (CTO msg 1368/1369 retired cot's canonical_prices build as DEMQUE's store), so the refused commit never needs to land; the split-literal refusal was the right one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W7-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "DQ-t-8 is SUPERSEDED; the worktree edits are carried as an input patch to ADVI_FIRMBKTS (deliverables/2.0.0_SA_COO~Q1/ADVI_FIRMBKTS_INPUT_S00_TOLERANT_LOAD.patch), not an order. Note for the record: round 2 was round-closed (590c35ee97) while this BLOCKING row was still UNDER_INVESTIGATION; spine L10 requires it dispositioned first.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log 091ccbafa2: supersede(MDPF_DEMQUE.TO-DQ-t8) S_00 closed SUPERSEDED per 1.0.0_SA_CTO~DELL1 msg 1368",
        "1.0.0_SA_CTO~DELL1 msg 1369: 'close DQ-t-8 SUPERSEDED ... The refused split-literal workaround was the right refusal'",
        "investigation row MDPF_DEMQUE-D1-W7-S2 (0.9.0_WK_MDPF_DEMQUE~7)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by supersession of its order; nothing of it lands in this project."
  },
  {
    "id": "MDPF_DEMQUE-C-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:20:00Z",
    "one_line": "W7-S1 (OBSERVATION/INERT) dismissed: it describes the S_00 step's flag form in the superseded order DQ-t-8; it travels with the ADVI_FIRMBKTS input patch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W7-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "build_canonical_prices_v2.py takes only --dry-run; the fact is ADVI_FIRMBKTS's if it schedules S_00.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log 091ccbafa2 (DQ-t-8 SUPERSEDED)",
        "investigation row MDPF_DEMQUE-D1-W7-S1 (0.9.0_WK_MDPF_DEMQUE~7)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Its order is superseded; the fact belongs to ADVI_FIRMBKTS's input, not this project."
  }
]
```
