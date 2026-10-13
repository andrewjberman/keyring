# NFRA_OPLGTW -- surprise channel, ADJUDICATION v26 (site Z) -- ROUND 35 L8 (+ one round-33 L9)

**Lane:** the CVO. **By:** `3.0.0_SA_CVO~Z`, 2026-10-13 ~14:3xZ, on `2.0.0_SA_COO~O` msg 33629 (`deliverables/2.0.0_SA_COO~O/ROUND35_TERMINAL_20261013.md @56e86a3f05`). round-close-check
MAY-CLOSE, 0 judgment criteria; 5 of 6 complete, and OG-ap-11 failed and was rolled back, its fix carried by OG-ap-12.

**Round-34 remediation rows met this round** (REMEDIATION_v17.md is not edited; this seat's live reads):
- **Z-W55-S2 (.pptx release): MET.** On i-07dccb1615503ac99 (ssm), app/integrations/advi_billing/site_to_s3.py has md5
  671c01e99dd8ba5c253d5b6226fb4339, equal to release d9f2ebded9's file, and carries market_update (3 refs).
- **Z-S92 (teams bearer holders): MET.** cloudops-dell-agent-platform-secrets-policy is default v5; ReadPlatformKeys holds
  30 resources, none of them gateway/teams/bearer. simulate-principal-policy as cloudops-dell1-agent-user on the bearer
  ARN reads implicitDeny.
- **Z-S91 (per-family DLQ drain): PARTLY MET.** schwab is met (the policy has ChangeMessageVisibility, and the real sweep
  ran clean). etf, blackdiamond, orion and eclipse still run drain-all: the blackdiamond sweep deleted the eclipse
  synthetic at 12:45:52Z. The row stays OPEN. The DLQ holds ApproximateNumberOfMessages=12 at ~14:1xZ.
- **Z-W57-S2 (BD admission): still ARMED,** held on Andrew; already graduated at v17 and not re-graduated here.

**Round 33's remaining judgment criterion:** OG-tl-1 is graded at C-S70 on dell2's re-probe (NFRA_TRNSPT-D2-S30). OG-rl-16's
cannot be graded yet: s3://opal-data-assets/smartx/49financial/bronze/fee_statement/ still lists no object at ~14:1xZ,
so dell2's first real put has not happened, and no row here names that criterion.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S70",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-13T14:30Z",
    "one_line": "L9 grade, NFRA_OPLGTW.TO-OG-tl-1.transcript-allowlist-4-meetings AC3 (judgment, round 33): PASS, bounded -- dell2's re-probe reads 3 of 4 allowlisted meetings (200) and the fourth fails on Graph's side, not the allowlist; but the failure is a 502 graph_error, not the 403 the ruling predicted.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-tl-1 AC3: dell2's own re-probe (one read per meeting, row NFRA_TRNSPT-D2-S11) reads 3 of 4 meetings, the fourth a Graph-side 403 as the ruling predicts.",
    "world_is": "NFRA_TRNSPT-D2-S30 (2.0.0_SA_COO~T2, 2026-10-11T13:56:33Z, @8d4777d2b3) is dell2's re-probe: one GatewayTransport.list_meeting_transcripts per series against https://mcp.opalinvest.dev. monday_meeting 200 (20 rows), ocio_ic 200 (8), asset_management_ic 200 (7), research_meeting GatewayGraphError 502. It is identical to its own 03:07Z read. NO meeting reads 403 meeting_not_allowed, so the released allowlist admits all four, which is the outcome OG-tl-1 shipped. The fourth fails upstream in Graph, as the ruling said, but the status is 502, not 403. The ruling located the failure correctly and named its code wrongly, and the criterion's substance holds. Bounded: the probe does not record which gateway build answered. Every gateway release live since tl-1 carries the allowlist hunk: this seat read 0 -> 5 refs on trunk at the round-34 compile, and every release in between was cut on the live ref. Carried, not grounds: research_meeting's content reads are not served, which is NFRA_TRNSPT's open question (D2-S29, the shared-folder tool).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md row NFRA_TRNSPT-D2-S30, read whole",
        "ADJUDICATION_v25.Z.md header: trunk deploy-to-ec2.sh meeting_allowlist refs 5 (this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-OG-tl-1 AC3 PASS, bounded."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S71",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-13T14:30Z",
    "one_line": "Round 35 L8: 7 rows DISMISSED -- Z-S97 (ARMED) remediated by OG-ap-12 and re-read live; Z-S98, Z-S99 ruled by amendments; W58-S1 (ARMED) met for schwab live, its remainder on Z-S91; W58-S2 exercised by the real sweep; W59-S1 and S96 procedure notes.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned BLOCKING or ARMED row of the round.",
    "world_is": "Z-S97, re-read by this seat: iam get-policy-version opal-assets-silver-dlq-access is default v2, actions [SendMessage, ReceiveMessage, DeleteMessage, GetQueueAttributes, ChangeMessageVisibility], with 7 attachments. /aws/lambda/opal-assets-silver-schwab since 2026-10-13T12:00Z shows 2 START and 0 AccessDenied/Traceback/ERROR events. Z-S98 is ruled by A1 @d78be8e6c2 (the description edit is struck, so nothing is replaced). Z-S99 is ruled by OG-ap-13 A1 @fed356e1cb (one audited lane override). W58-S1 (schwab's own drain_dlq was not in fd-1's first scope) is met for schwab: OG-ap-12's real 12:15Z sweep drained its own record and left the eclipse synthetic. The remaining four families' drain-all is Z-S91's (REMEDIATION_v17, still OPEN). W58-S2 (attribution untested on a live message) is exercised by that same sweep. W59-S1 (a reader is an IAM user named for a person) and S96 (a release-tree test that cannot run there) are procedure notes; S96 is in the issuer's cut-template class.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W58-S1",
      "NFRA_OPLGTW-Z-W58-S2",
      "NFRA_OPLGTW-Z-W59-S1",
      "NFRA_OPLGTW-Z-S96",
      "NFRA_OPLGTW-Z-S97",
      "NFRA_OPLGTW-Z-S98",
      "NFRA_OPLGTW-Z-S99"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws iam get-policy-version opal-assets-silver-dlq-access v2 (this seat, ~14:1xZ 2026-10-13)",
        "logs filter-log-events /aws/lambda/opal-assets-silver-schwab since 2026-10-13T12:00Z: errors 0, START 2",
        "deliverables/2.0.0_SA_COO~O/ROUND35_TERMINAL_20261013.md @56e86a3f05",
        "investigation rows Z-W58-S1, Z-W58-S2, Z-W59-S1, Z-S96, Z-S97, Z-S98, Z-S99"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remediated and re-read live, ruled by an amendment, or a note with no standing defect."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S72",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-13T14:30Z",
    "one_line": "Round 35 L8: Z-S95 (the teams channel-messages route's intermittent 502, still present) and Z-S100 (no sweep persists its DLQ report) GRADUATE to REMEDIATION_v18.",
    "class": "OBSERVATION",
    "spec_asserts": "A standing defect leaves the round as an owned remediation row.",
    "world_is": "Z-S95, re-read by this seat: COMM_ASSIST's ingress over the last 24 hours shows 1438 channel_poll events at failed=0 and 2 at failed=1, with 4 'status=502' lines, so the 502 recurs at a low rate and is still unread for cause. Z-S100: a scheduled sweep's drain report is a discarded return value, so no artifact records what each family drained. A2 graded OG-ap-12 from the queue instead; the persistence is the round-36 carry.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S95",
      "NFRA_OPLGTW-Z-S100"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "logs filter-log-events /aws/lambda/teams-global-chat-assist-ingress-lambda, last 86400 s at ~14:1xZ: channel_poll failed=0 x1438, failed=1 x2; 'status=502' x4",
        "investigation rows Z-S95, Z-S100",
        "deliverables/2.0.0_SA_COO~O/ROUND35_TERMINAL_20261013.md @56e86a3f05"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
