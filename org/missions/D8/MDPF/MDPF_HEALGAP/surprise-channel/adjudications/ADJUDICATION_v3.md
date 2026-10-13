# MDPF_HEALGAP -- round 3 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-13T13:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T13:50:00Z. L8 packet: 2.0.0_SA_COO~G1 msg 4849, round3/ROUND3_CLOSE_PACKET.md @881c99ab1e. 6 of 6 orders, 6 ledgers
CLOSED. 18 rows swept since v2 (watermark 2026-10-11T02:45Z; 18 of 48 investigation rows after it): 13 graduated (D1-W8-S1 with its
disarm clock DISARMED; D1-S16 BLOCKING to the CTO), 5 dismissed. No BLOCKING or ARMED row is undispositioned.

```json
[
  {
    "id": "MDPF_HEALGAP-D1-C-S23",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T13:50:00Z",
    "one_line": "L9 read of round 3 at box/dell1 HEAD b8f0ef0b32 (packet ROUND3_CLOSE_PACKET.md @881c99ab1e, sha256 0dc5f738c3002b5e verified): this seat re-ran all nine criteria. 8 of 9 hold: t9-AC2 T9IAM-OK, t9-AC3 GATE-OK, t11-AC1 T11-OK (bd_asset_dim_reattempt cron(40 22 ? * MON-FRI *)), t11-AC2 SSMGUARD-OK, t12 CENSUS-OK (20 rows, denominator 164, 7 exposed-manual), t13 READ-OK (RUNS-SLICE, noop UNKNOWN), t14 T14-OK (characteristics cron(25 13), margin 600 s), t15 T15-OK. t9-AC1 now reads T9-BAD ('existing rule ... is not at cron(0 7)') BY DESIGN: HG-t-15 later retired that rule; the live read (events describe-rule) returns ResourceNotFound for cot_satellites_registry_producer_daily. AC1 held at t9's own close; its later failure is t15's intended effect, not a regression. round-close-check --round 3: MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of round 3 at box/dell1 HEAD b8f0ef0b32 (packet ROUND3_CLOSE_PACKET.md @881c99ab1e, sha256 0dc5f738c3002b5e verified): this seat re-ran all nine criteria. 8 of 9 hold: t9-AC2 T9IAM-OK, t9-AC3 GATE-OK, t11-AC1 T11-OK (bd_asset_dim_reattempt cron(40 22 ? * MON-FRI *)), t11-AC2 SSMGUARD-OK, t12 CENSUS-OK (20 rows, denominator 164, 7 exposed-manual), t13 READ-OK (RUNS-SLICE, noop UNKNOWN), t14 T14-OK (characteristics cron(25 13), margin 600 s), t15 T15-OK. t9-AC1 now reads T9-BAD ('existing rule ... is not at cron(0 7)') BY DESIGN: HG-t-15 later retired that rule; the live read (events describe-rule) returns ResourceNotFound for cot_satellites_registry_producer_daily. AC1 held at t9's own close; its later failure is t15's intended effect, not a regression. round-close-check --round 3: MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran the nine R3_CHECKS invocations at b8f0ef0b32 (outputs as stated)",
        "3.0.0_SA_CVO aws events describe-rule cot_satellites_registry_producer_daily 2026-10-13T13:4xZ: ResourceNotFoundException",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project MDPF_HEALGAP --round 3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of round 3 at box/dell1 HEAD b8f0ef0b32 (packet ROUND3_CLOSE_PACKET.md @881c99ab1e, sha256 0dc5f738c3002b5e verified): this seat re-ran all nine criteria. 8 of 9 hold: t9-AC2 T9IAM-OK, t9-AC3 GATE-OK, t11-AC1 T11-OK (bd_asset_dim_reattempt cron(40 22 ? * MON-FRI *)), t11-AC2 SSMGUARD-OK, t12 CENSUS-OK (20 rows, denominator 164, 7 exposed-manual), t13 READ-OK (RUNS-SLICE, noop UNKNOWN), t14 T14-OK (characteristics cron(25 13), margin 600 s), t15 T15-OK. t9-AC1 now reads T9-BAD ('existing rule ... is not at cron(0 7)') BY DESIGN: HG-t-15 later retired that rule; the live read (events describe-rule) returns ResourceNotFound for cot_satellites_registry_producer_daily. AC1 held at t9's own close; its later failure is t15's intended effect, not a regression. round-close-check --round 3: MAY-CLOSE."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S24",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T13:50:00Z",
    "one_line": "D1-W8-S1 (BLOCKING, ARMED) graduated with its disarm clock DISARMED: this seat's re-run at HEAD reproduces the parked pre-read (org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_HEALGAP_R3_D1_W8_S1_DISARM_PREREAD_20261011.md @26e59cbec9): hg_t11_assetdim.py --ssm on the real document prints SSMGUARD-OK rc 0; a mutant made by this seat (the one '[ $GUARD_RC -eq 0 ]' changed to '-ge 0', 1 line differs) prints SSMGUARD-BAD rc 1. The live SSM document opal-bd-asset-dim-download is DefaultVersion 6 (LatestVersion 6), Hash 65a15c80f434e8d0... equal to the repo file's sha256, unchanged since 25c71ce573 (2026-10-11). The guard's exists arm ran live on 2026-10-12 22:40Z (SKIP-COMPLETE, act-3 ledger L4). Residual carried: the failed-read arm is graded under stubbed tools, never on a live read failure; the remediation stays OPEN until one is observed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-W8-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W8-S1 (BLOCKING, ARMED) graduated with its disarm clock DISARMED: this seat's re-run at HEAD reproduces the parked pre-read (org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_HEALGAP_R3_D1_W8_S1_DISARM_PREREAD_20261011.md @26e59cbec9): hg_t11_assetdim.py --ssm on the real document prints SSMGUARD-OK rc 0; a mutant made by this seat (the one '[ $GUARD_RC -eq 0 ]' changed to '-ge 0', 1 line differs) prints SSMGUARD-BAD rc 1. The live SSM document opal-bd-asset-dim-download is DefaultVersion 6 (LatestVersion 6), Hash 65a15c80f434e8d0... equal to the repo file's sha256, unchanged since 25c71ce573 (2026-10-11). The guard's exists arm ran live on 2026-10-12 22:40Z (SKIP-COMPLETE, act-3 ledger L4). Residual carried: the failed-read arm is graded under stubbed tools, never on a live read failure; the remediation stays OPEN until one is observed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_HEALGAP_R3_D1_W8_S1_DISARM_PREREAD_20261011.md @26e59cbec9",
        "3.0.0_SA_CVO ran org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t11_assetdim.py --ssm on the real doc (rc 0) and on its own mutant (rc 1) 2026-10-13T13:4xZ",
        "3.0.0_SA_CVO aws ssm describe-document opal-bd-asset-dim-download: DefaultVersion 6, Hash equal to the repo file"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v3.md."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S25",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T13:50:00Z",
    "one_line": "D1-S16 (BLOCKING, INERT) graduated to the CTO: this seat re-read at 13:44Z: s3://opal-data-etfs/bbg/2026-10-12/characteristics.parquet is still 404; bbg partitions run through 2026-10-09 only (positive control bbg/2026-10-09/characteristics.parquet LastModified 2026-10-12T11:03:03Z, so the T-1 partition normally lands ~11:03Z). The served opal-data-cot/platinum/satellites/characteristics.json is the 2026-10-12T13:26:03Z version (68,601 B): readers see Friday's characteristics on Tuesday, one trading day behind. Upstream of this project; the 13:25Z fire failed correctly (NoSuchKey, nothing written). An off-clock re-run needs a never-widen half.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S16"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S16 (BLOCKING, INERT) graduated to the CTO: this seat re-read at 13:44Z: s3://opal-data-etfs/bbg/2026-10-12/characteristics.parquet is still 404; bbg partitions run through 2026-10-09 only (positive control bbg/2026-10-09/characteristics.parquet LastModified 2026-10-12T11:03:03Z, so the T-1 partition normally lands ~11:03Z). The served opal-data-cot/platinum/satellites/characteristics.json is the 2026-10-12T13:26:03Z version (68,601 B): readers see Friday's characteristics on Tuesday, one trading day behind. Upstream of this project; the 13:25Z fire failed correctly (NoSuchKey, nothing written). An off-clock re-run needs a never-widen half.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_HEALGAP-D1-S16",
        "3.0.0_SA_CVO aws s3api head-object (404) and list with delimiter, 2026-10-13T13:44Z",
        "3.0.0_SA_CVO head-object opal-data-cot/platinum/satellites/characteristics.json: 2026-10-12T13:26:03Z, 68601 B"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v3.md."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S26",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T13:50:00Z",
    "one_line": "D1-S14 graduated INERT: infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py lines 276-278 set healed_at to now when a previously-missing feed arrives, so the live timestamp is the producer's rule and the HG-t-10 half's 'healed_at null' expectation was wrong, not the world. Owed: the half's section 5 item 3 and the healed check script corrected to the producer's rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S14"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S14 graduated INERT: infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py lines 276-278 set healed_at to now when a previously-missing feed arrives, so the live timestamp is the producer's rule and the HG-t-10 half's 'healed_at null' expectation was wrong, not the world. Owed: the half's section 5 item 3 and the healed check script corrected to the producer's rule.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_HEALGAP-D1-S14",
        "3.0.0_SA_CVO comp-find healed_at infra/aws/lambda: lambda_function.py:271-279"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v3.md."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S27",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T13:50:00Z",
    "one_line": "D1-S13, D1-W12-S1, D1-W11-S1, D1-W7-S2, D1-W7-S3, D1-W7-S4, D1-W9-S1, D1-W9-S2, D1-W9-S3 and D1-W10-S1 graduated INERT with their owners (REMEDIATION_v3): each names text, a registry row, a checker clause or a ruling still owed; none is a live hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S13",
      "MDPF_HEALGAP-D1-W12-S1",
      "MDPF_HEALGAP-D1-W11-S1",
      "MDPF_HEALGAP-D1-W7-S2",
      "MDPF_HEALGAP-D1-W7-S3",
      "MDPF_HEALGAP-D1-W7-S4",
      "MDPF_HEALGAP-D1-W9-S1",
      "MDPF_HEALGAP-D1-W9-S2",
      "MDPF_HEALGAP-D1-W9-S3",
      "MDPF_HEALGAP-D1-W10-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S13, D1-W12-S1, D1-W11-S1, D1-W7-S2, D1-W7-S3, D1-W7-S4, D1-W9-S1, D1-W9-S2, D1-W9-S3 and D1-W10-S1 graduated INERT with their owners (REMEDIATION_v3): each names text, a registry row, a checker clause or a ruling still owed; none is a live hazard.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows as listed",
        "round3/ROUND3_CLOSE_PACKET.md rows table and named residuals"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v3.md."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S28",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T13:50:00Z",
    "one_line": "Dismissed, each standing as recorded: D1-S15 (vendor HTTP 401 x4, 11:35:58Z-11:39:29Z; the repair landed on its third attempt 11:41:17Z inside the 11:45Z bound); D1-W10-S2 (the slice's NOOP is UNKNOWN, which t13's READ-OK reports as noop=UNKNOWN on this seat's run: a measurement-only cell); D1-W7-S1 (t9's premise on the bronze landing time was wrong, but the stamp-gated 13:15Z fire ran on 10-12 and 10-13 rc 0, so the act was right); D1-W7-S5 (t9-AC1 did not fail at the start tree; the order's 'all three FAIL at the base' sentence was untrue of AC1 alone, and the criterion still grades the act); D1-W9-S4 (the open-calls list path now exists: org/devices/state/<box>/open_calls.json, written by .tools/open-calls.py).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S15",
      "MDPF_HEALGAP-D1-W10-S2",
      "MDPF_HEALGAP-D1-W7-S1",
      "MDPF_HEALGAP-D1-W7-S5",
      "MDPF_HEALGAP-D1-W9-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Dismissed, each standing as recorded: D1-S15 (vendor HTTP 401 x4, 11:35:58Z-11:39:29Z; the repair landed on its third attempt 11:41:17Z inside the 11:45Z bound); D1-W10-S2 (the slice's NOOP is UNKNOWN, which t13's READ-OK reports as noop=UNKNOWN on this seat's run: a measurement-only cell); D1-W7-S1 (t9's premise on the bronze landing time was wrong, but the stamp-gated 13:15Z fire ran on 10-12 and 10-13 rc 0, so the act was right); D1-W7-S5 (t9-AC1 did not fail at the start tree; the order's 'all three FAIL at the base' sentence was untrue of AC1 alone, and the criterion still grades the act); D1-W9-S4 (the open-calls list path now exists: org/devices/state/<box>/open_calls.json, written by .tools/open-calls.py).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows as listed",
        "3.0.0_SA_CVO hg_t13_read.py: READ-OK noop=UNKNOWN",
        "3.0.0_SA_CVO .tools/open-calls.py list (dell1 file present)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Dismissed, each standing as recorded: D1-S15 (vendor HTTP 401 x4, 11:35:58Z-11:39:29Z; the repair landed on its third attempt 11:41:17Z inside the 11:45Z bound); D1-W10-S2 (the slice's NOOP is UNKNOWN, which t13's READ-OK reports as noop=UNKNOWN on this seat's run: a measurement-only cell); D1-W7-S1 (t9's premise on the bronze landing time was wrong, but the stamp-gated 13:15Z fire ran on 10-12 and 10-13 rc 0, so the act was right); D1-W7-S5 (t9-AC1 did not fail at the start tree; the order's 'all three FAIL at the base' sentence was untrue of AC1 alone, and the criterion still grades the act); D1-W9-S4 (the open-calls list path now exists: org/devices/state/<box>/open_calls.json, written by .tools/open-calls.py)."
  }
]
```
