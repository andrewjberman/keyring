# MDPF_HEALGAP -- round 4 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-13T17:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T17:10:00Z. L8 packet: 2.0.0_SA_COO~G1 msg 4951, round4/ROUND4_CLOSE_PACKET.md @ed0b90d567. 2 of 2 orders. Rows: the 5
not yet dispositioned (D1-W13-S1 BLOCKING, D1-W14-S1..S4) plus D1-S16 (BLOCKING) closed REMEDIATED. Owed and named: the HOLDINGS-NOT-FINAL arm at
the 2026-10-14 00:55Z fire (2.0.0_SA_COO~G1). No BLOCKING or ARMED row is undispositioned.

```json
[
  {
    "id": "MDPF_HEALGAP-D1-C-S29",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T17:10:00Z",
    "one_line": "L9 read of round 4 at box/dell1 HEAD 4a8f8b49eb (packet ROUND4_CLOSE_PACKET.md @ed0b90d567, sha256 3b94dec66847cb46 verified): this seat re-ran all four criteria: t16-AC1 T16-OK (reattempt rule cron(55 * * * ? *), the 13:25Z rule unchanged), t16-AC2 T16IAM-OK (one prefix ListBucket on the cot bucket for the two exact keys, nothing wider), t16-AC3 GATE-OK (arms A-L), t17-AC1 DISP-OK 7 rows. Live: rule etfs-cot-satellites-characteristics-producer-reattempt-hourly ENABLED, target input {\"require_partition\":true}; the producer log shows PUBLISHED 68729 B at 15:56:01Z and SKIP-COMPLETE bbg_as_of=2026-10-12 at 16:55:13Z. OWED, not passed: the HOLDINGS-NOT-FINAL arm (first read at the 2026-10-14 00:55Z fire; owner 2.0.0_SA_COO~G1; the ledger healgap-r4-act-ht16-characteristics-reattempt-20261013 L6 stays open until it), and the live PARTITION-ABSENT arm (not yet run; pinned only by stub arms C/D). round-close-check --round 4: MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of round 4 at box/dell1 HEAD 4a8f8b49eb (packet ROUND4_CLOSE_PACKET.md @ed0b90d567, sha256 3b94dec66847cb46 verified): this seat re-ran all four criteria: t16-AC1 T16-OK (reattempt rule cron(55 * * * ? *), the 13:25Z rule unchanged), t16-AC2 T16IAM-OK (one prefix ListBucket on the cot bucket for the two exact keys, nothing wider), t16-AC3 GATE-OK (arms A-L), t17-AC1 DISP-OK 7 rows. Live: rule etfs-cot-satellites-characteristics-producer-reattempt-hourly ENABLED, target input {\"require_partition\":true}; the producer log shows PUBLISHED 68729 B at 15:56:01Z and SKIP-COMPLETE bbg_as_of=2026-10-12 at 16:55:13Z. OWED, not passed: the HOLDINGS-NOT-FINAL arm (first read at the 2026-10-14 00:55Z fire; owner 2.0.0_SA_COO~G1; the ledger healgap-r4-act-ht16-characteristics-reattempt-20261013 L6 stays open until it), and the live PARTITION-ABSENT arm (not yet run; pinned only by stub arms C/D). round-close-check --round 4: MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_CHECKS/hg_r4_rules.py --t16 and --t16-iam, hg_t16_gate.py, hg_t17_dispositions.py at 4a8f8b49eb",
        "3.0.0_SA_CVO aws events describe-rule / list-targets-by-rule 2026-10-13T17:02Z",
        "3.0.0_SA_CVO CloudWatch /aws/lambda/cot-satellites-characteristics-producer 15:50-17:05Z: 22 lines",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project MDPF_HEALGAP --round 4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of round 4 at box/dell1 HEAD 4a8f8b49eb (packet ROUND4_CLOSE_PACKET.md @ed0b90d567, sha256 3b94dec66847cb46 verified): this seat re-ran all four criteria: t16-AC1 T16-OK (reattempt rule cron(55 * * * ? *), the 13:25Z rule unchanged), t16-AC2 T16IAM-OK (one prefix ListBucket on the cot bucket for the two exact keys, nothing wider), t16-AC3 GATE-OK (arms A-L), t17-AC1 DISP-OK 7 rows. Live: rule etfs-cot-satellites-characteristics-producer-reattempt-hourly ENABLED, target input {\"require_partition\":true}; the producer log shows PUBLISHED 68729 B at 15:56:01Z and SKIP-COMPLETE bbg_as_of=2026-10-12 at 16:55:13Z. OWED, not passed: the HOLDINGS-NOT-FINAL arm (first read at the 2026-10-14 00:55Z fire; owner 2.0.0_SA_COO~G1; the ledger healgap-r4-act-ht16-characteristics-reattempt-20261013 L6 stays open until it), and the live PARTITION-ABSENT arm (not yet run; pinned only by stub arms C/D). round-close-check --round 4: MAY-CLOSE."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S30",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T17:10:00Z",
    "one_line": "D1-S16 (BLOCKING) closed REMEDIATED in REMEDIATION_v3, its close condition met on this seat's reads: the served characteristics.json is rebuilt from bbg/2026-10-12 with holdings_as_of equal to as_of (both 2026-10-13); lib.trading_calendar.prev_trading_day(2026-10-13) = 2026-10-12, so the input is the right T-1. The missing input s3://opal-data-etfs/bbg/2026-10-12/characteristics.parquet now exists (LastModified 2026-10-13T14:39:56Z, 20405 B). Served by the HG-t-16 re-attempt at 15:56Z, not by a manual off-clock run. The universe count reads 172 (the packet's 171 rows is the issuer's row read); not a defect.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S16"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S16 (BLOCKING) closed REMEDIATED in REMEDIATION_v3, its close condition met on this seat's reads: the served characteristics.json is rebuilt from bbg/2026-10-12 with holdings_as_of equal to as_of (both 2026-10-13); lib.trading_calendar.prev_trading_day(2026-10-13) = 2026-10-12, so the input is the right T-1. The missing input s3://opal-data-etfs/bbg/2026-10-12/characteristics.parquet now exists (LastModified 2026-10-13T14:39:56Z, 20405 B). Served by the HG-t-16 re-attempt at 15:56Z, not by a manual off-clock run. The universe count reads 172 (the packet's 171 rows is the issuer's row read); not a defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read s3://opal-data-cot/platinum/satellites/characteristics.json 2026-10-13T17:02Z: as_of 2026-10-13, inputs.holdings_as_of 2026-10-13, inputs.bbg_as_of 2026-10-12 (bbg_key s3://opal-data-etfs/bbg/2026-10-12/characteristics.parquet), LastModified 15:56:02Z, 68729 B",
        "3.0.0_SA_CVO aws s3api head-object opal-data-etfs bbg/2026-10-12/characteristics.parquet: 2026-10-13T14:39:56Z, 20405 B",
        "3.0.0_SA_CVO lib.trading_calendar.prev_trading_day(2026-10-13) = 2026-10-12",
        "remediation row MDPF_HEALGAP-D1-S16 (REMEDIATION_v3)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S16 (BLOCKING) closed REMEDIATED in REMEDIATION_v3, its close condition met on this seat's reads: the served characteristics.json is rebuilt from bbg/2026-10-12 with holdings_as_of equal to as_of (both 2026-10-13); lib.trading_calendar.prev_trading_day(2026-10-13) = 2026-10-12, so the input is the right T-1. The missing input s3://opal-data-etfs/bbg/2026-10-12/characteristics.parquet now exists (LastModified 2026-10-13T14:39:56Z, 20405 B). Served by the HG-t-16 re-attempt at 15:56Z, not by a manual off-clock run. The universe count reads 172 (the packet's 171 rows is the issuer's row read); not a defect."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S31",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T17:10:00Z",
    "one_line": "D1-W13-S1 (BLOCKING, INERT) dismissed: the naming limb refused the first cut's rule name (its cron(25 14-23 ...) schedule had no cadence word), as the gate is meant to; AMENDMENT 1 moved the schedule to cron(55 * * * ? *) with the 'after 13:15Z' condition inside the handler, and the merged code (8cc7e0458e) passed the commit gate. The live rule name ends in '-hourly' and this seat's T16-OK reads it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-W13-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W13-S1 (BLOCKING, INERT) dismissed: the naming limb refused the first cut's rule name (its cron(25 14-23 ...) schedule had no cadence word), as the gate is meant to; AMENDMENT 1 moved the schedule to cron(55 * * * ? *) with the 'after 13:15Z' condition inside the handler, and the merged code (8cc7e0458e) passed the commit gate. The live rule name ends in '-hourly' and this seat's T16-OK reads it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_HEALGAP-D1-W13-S1",
        "round4/ROUND4_CLOSE_PACKET.md AMENDMENT 1",
        "3.0.0_SA_CVO hg_r4_rules.py --t16: T16-OK"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W13-S1 (BLOCKING, INERT) dismissed: the naming limb refused the first cut's rule name (its cron(25 14-23 ...) schedule had no cadence word), as the gate is meant to; AMENDMENT 1 moved the schedule to cron(55 * * * ? *) with the 'after 13:15Z' condition inside the handler, and the merged code (8cc7e0458e) passed the commit gate. The live rule name ends in '-hourly' and this seat's T16-OK reads it."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S32",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T17:10:00Z",
    "one_line": "D1-W14-S1 dismissed: the census's Teams 'stub raises GatewayToolsAbsent' premise is corrected by the round's own dispositions document (org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md line 23: 'the Teams transport is live'; row 14 grades teams-global-transcripts-pull-hourly NAMED-REASON on the 503 needs_login path).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-W14-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S1 dismissed: the census's Teams 'stub raises GatewayToolsAbsent' premise is corrected by the round's own dispositions document (org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md line 23: 'the Teams transport is live'; row 14 grades teams-global-transcripts-pull-hourly NAMED-REASON on the 503 needs_login path).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_HEALGAP-D1-W14-S1",
        "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md lines 14 and 23"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W14-S1 dismissed: the census's Teams 'stub raises GatewayToolsAbsent' premise is corrected by the round's own dispositions document (org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md line 23: 'the Teams transport is live'; row 14 grades teams-global-transcripts-pull-hourly NAMED-REASON on the 503 needs_login path)."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S33",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T17:10:00Z",
    "one_line": "D1-W14-S2, D1-W14-S3 and D1-W14-S4 graduated INERT to 1.0.0_SA_CTO~DELL1: which act restores the Credential Manager SDDSecure the SDD puller reads (S2); the ASTN FT leg's missed-day refill and its send policy (S3); and transcripts/pull.tf's stale 'never applied' header beside a live ENABLED rule, which belongs to the transcripts project (S4). D1-S14 and D1-S15, named in the packet, were dispositioned in ADJUDICATION_v3 (C-S26 graduated, C-S28 dismissed).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-W14-S2",
      "MDPF_HEALGAP-D1-W14-S3",
      "MDPF_HEALGAP-D1-W14-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W14-S2, D1-W14-S3 and D1-W14-S4 graduated INERT to 1.0.0_SA_CTO~DELL1: which act restores the Credential Manager SDDSecure the SDD puller reads (S2); the ASTN FT leg's missed-day refill and its send policy (S3); and transcripts/pull.tf's stale 'never applied' header beside a live ENABLED rule, which belongs to the transcripts project (S4). D1-S14 and D1-S15, named in the packet, were dispositioned in ADJUDICATION_v3 (C-S26 graduated, C-S28 dismissed).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_HEALGAP-D1-W14-S2, S3, S4",
        "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md lines 15-18, 27-34"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v4.md."
  }
]
```
