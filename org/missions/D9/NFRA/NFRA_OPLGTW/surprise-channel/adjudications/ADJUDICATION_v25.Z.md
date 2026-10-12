# NFRA_OPLGTW -- surprise channel, ADJUDICATION v25 (site Z) -- ROUND 34 L8

**Lane:** the CVO. **By:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~22:5xZ, on `2.0.0_SA_COO~O` msg 33408 (`deliverables/2.0.0_SA_COO~O/ROUND34_TERMINAL_20261011.md @fd3f189ece`). round-close-check
MAY-CLOSE, 0 judgment criteria. 9 of 10 orders complete; OG-bd-1 superseded and held on Andrew (Z-W57-S2).

**Round-33 remediation rows met this round** (REMEDIATION_v16.md is not edited; this seat's reads):
- **Z-S85 (ARMED): MET.** `git show HEAD:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | grep -c meeting_allowlist` reads 5 (it
  read 0 at the round-33 compile). The hunk is back on trunk by OG-db-1, so a trunk-cut release no longer revokes the
  allowlist. Disarmed.
- **The gateway's /hx/teams routes are live** (OG-ap-7, release 28ba9532b6). Corroborated on a second plane: COMM_ASSIST's
  ingress channel_poll reads 29 of 29 `failed: 0` with `channels: 8` in the 30 minutes to ~22:4xZ, after failing every
  minute on `route=teams status=404`.
- Z-S84 (manifest checksums) and Z-S88 (runbook 7.2): MET by OG-br-1, per the issuer's re-runs.
- Z-S77 (DLQ actor): CAUSE NAMED by Z-S91, which carries the remedy below.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S68",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T22:50Z",
    "one_line": "Round 34 L8: 9 rows DISMISSED -- four issuer check defects each repaired before a grade landed (W55-S1 by A1/W55-S3, W56-S2 by W56-S3, Z-S93 by Z-S94, W54-S1), the DLQ 'unknown consumer' now named (W57-S1, by Z-S91), and three notes with no standing defect.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "W55-S1 (OG-mu-1 AC1 could not pass as written) is resolved by Amendment 1 @1ceb994ad3, which re-pins test_ogab2_ac02 to the content-addressed key (W55-S3). W56-S2 (gw1.AC2 regex) was fixed at b237fbf925 and re-run PASS (W56-S3). Z-S93 (ap9.AC2 named a non-existent function) was repaired (Z-S94) and re-run PASS by the issuer. W54-S1 (the order named a wrong module path) was worked around by the worker. W57-S1: the 'unknown consumer' of opal-assets-silver-dlq is the declared 16:00Z silver sweeps, each draining the whole shared DLQ (Z-S91, which graduates); this also names the actor of this seat's round-33 row Z-S77. W56-S1 (TF variable names) and W56-S4 (cold first pass 142-147 s, not 221-235 s) are notes with no standing defect.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W57-S1",
      "NFRA_OPLGTW-Z-W54-S1",
      "NFRA_OPLGTW-Z-W55-S1",
      "NFRA_OPLGTW-Z-W55-S3",
      "NFRA_OPLGTW-Z-W56-S1",
      "NFRA_OPLGTW-Z-W56-S2",
      "NFRA_OPLGTW-Z-W56-S3",
      "NFRA_OPLGTW-Z-W56-S4",
      "NFRA_OPLGTW-Z-S93"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/ROUND34_TERMINAL_20261011.md @fd3f189ece section 'Rows for the compile'",
        "investigation rows Z-W57-S1, Z-W54-S1, Z-W55-S1, Z-W55-S3, Z-W56-S1, Z-W56-S2, Z-W56-S3, Z-W56-S4, Z-S93"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired before any wrong grade landed, cause named, or a note with no standing defect."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S69",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T22:50Z",
    "one_line": "Round 34 L8: Z-S91, Z-W55-S2, Z-W57-S2 (ARMED) and Z-S92 GRADUATE to REMEDIATION_v17 -- the whole-DLQ sweep drain, the .pptx key's quarter argument, the BD admission held on Andrew, and the Teams bearer's holders.",
    "class": "OBSERVATION",
    "spec_asserts": "A standing defect leaves the round as an owned remediation row.",
    "world_is": "Z-S91: each declared 16:00Z silver sweep drains the WHOLE shared DLQ and reports other families' failures as its own; a round-35 per-family drain cell. Z-W55-S2: the .pptx key is intake's content-addressed form because the host carries no lib/, so the quarter argument moves to the release pair. Z-W57-S2: OG-bd-1's census found 2 unprofiled callers of blackdiamond_list_fees (one master_admin), the ruling's STOP. No deny was built, an Andrew admission call is owed, and it continues this seat's W45-S2. Z-S92: gateway/teams/bearer is readable by the gateway, COMM_ASSIST's Lambda and the cloudops-dell-agent group, and the dell consumer is a round-35 question.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S91",
      "NFRA_OPLGTW-Z-W55-S2",
      "NFRA_OPLGTW-Z-W57-S2",
      "NFRA_OPLGTW-Z-S92"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/ROUND34_TERMINAL_20261011.md @fd3f189ece",
        "investigation rows Z-S91, Z-W55-S2, Z-W57-S2, Z-S92"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
