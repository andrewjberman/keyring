# NFRA_OPLGTW -- surprise channel, ADJUDICATION v23 (site Z) -- ROUND 32 L9

**Lane:** the CVO. **By:** `3.0.0_SA_CVO~Z`, standing in for `3.0.0_SA_CVO~O`, 2026-10-09 ~16:2xZ, on `2.0.0_SA_COO~O` msg 32865
(packet `deliverables/2.0.0_SA_COO~O/ROUND32_TERMINAL_20261009.md` @5be974003f). This file grades the round's two judgment
criteria. The round's channel compile is separate.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S59",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T16:20Z",
    "one_line": "L9 grade, TO-OG-bf-1 AC3 (judgment): PASS -- what the 13-month backfill caused downstream matches the signed ask: the one consumer, the 49F gold dispatcher, received 256 records and skipped all 256 as historical, dispatching nothing and erroring never.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-bf-1 AC3: what the backfill caused downstream (the 49F accelerator and any other consumer) matches the signed ask's statement, read from the consumers' own logs.",
    "world_is": "The signed ask (NEVER_WIDEN_ASK_OG-bf-1.md section 3) enumerates every ObjectCreated consumer: none for 08242234 (complete and conversions) or for 08335338 conversions; exactly one for 08335338 meta/complete, the silver-complete accelerator -> advi-49f-gold-dispatch, gated by OG-ap-2's dispatcher date gate. This seat re-read the dispatcher's own log, /aws/lambda/advi-49f-gold-dispatch 2026-10-09T05:48:03Z..06:40:00Z, auto-paginated: 1537 events, START 256, SKIP 'not the production T-1' 256, 'dispatched doc=' 0, ERROR/Traceback 0. That equals the worker's read exactly. No other consumer exists for the backfilled keys to have fired.",
    "grounding": {"status": "GROUNDED", "evidence": [
      "deliverables/0.9.0_WK_NFRA_OPLGTW~41/NEVER_WIDEN_ASK_OG-bf-1.md :10-11, :107-131 (consumer table)",
      "aws logs filter-log-events /aws/lambda/advi-49f-gold-dispatch 05:48:03Z..06:40:00Z, re-read by this seat ~16:1xZ: 1537 / START 256 / SKIP 256 / dispatched 0 / ERROR 0"
    ]},
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-OG-bf-1 AC3 PASS."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S60",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T16:20Z",
    "one_line": "L9 grade, TO-OG-da-1 AC3 (judgment): PASS, bounded -- every listed caller's recorded context is admitted by the deployed rule, and the one arm the change touched (empty userType, tier internal) read ADMITTED live; 5 of the 6 have not yet called since the deploy.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-da-1 AC3: each caller named in da1_callers.json reads ADMITTED in the function's own log on its first real call after the deploy (2026-10-09 07:59:39Z).",
    "world_is": "This seat read /aws/lambda/opal-data-refresh-api from 07:59:39Z to ~16:1xZ: 17 events. Callers were joined by sha256(lowercased address)[:8], with no address printed. 1 of 6 has called: 686bd73c (empty userType, tier internal) at 13:24:23Z reads 'admitted as Opal-internal'. 0 of 6 refused. 5 of 6 have not called since the deploy. da1_callers.json records every one of the six with tier internal, and four with userType Dev. The deployed rule (lambda_function.py:161-165, :209-216) admits Dev, or tier == 'internal', or firmId == 'opal-capital', so each listed caller is admitted by construction. The only class the change could have locked out (empty userType) has been exercised live and admitted; 894ae007 is the other member of that class. Also read: an UNLISTED principal (userType test-filer, tier advisor) was admitted as Opal-internal at 15:41:40Z. By the code it can only have entered through the firmId == 'opal-capital' arm, which the ask implemented and the COO half ratified (NEVER_WIDEN_HALF_COO_OG-da-1 :26). firmId is not logged, so that path is inferred from the code, not read.",
    "grounding": {"status": "GROUNDED", "evidence": [
      "aws logs filter-log-events /aws/lambda/opal-data-refresh-api from 2026-10-09T07:59:39Z, read ~16:1xZ: 17 events, 2 admitted lines, 0 REFUSED",
      "deliverables/0.7.0_AE_CloudOps~Z/da1_callers.json callers[] tier_observed / userType_observed",
      "infra/aws/lambda/data_refresh/lambda_function.py:158-165, :209-219"
    ]},
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-OG-da-1 AC3 PASS, bounded as stated. The literal reading (each of 6 first calls observed) completes as the other 5 call. The COO's next drive reads them and appends here only on a REFUSED line."
  }
]
```

-- 3.0.0_SA_CVO~Z

## C-S61 / C-S62 -- ROUND 32 L8 compile: 26 dismissed, 15 graduated; 12 round-33 rows left OPEN (none BLOCKING or ARMED)

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S61",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T17:00Z",
    "one_line": "Round 32 L8: 26 rows DISMISSED -- each was resolved by a later row, an amendment or a landed act (r29, OG-ap-1/2/3), or records a fact.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "W39-S3: retried and succeeded; the box was cleaned (commands 22e138b8, 5ca67e2b). W39-S4: resolved by W39-S7: source 47c3c75f11 (in HEAD) and the repin 7af0b6bc3d; deployed 02:33Z per W41-S3. W39-S6: a recorded fact: safe-apply gates applies only. W39-S7: the resolution row for W39-S4. W39-S8: option (c) built; A3 supersedes the name; OG-ap-1 complete. S68: resolved by option (c) (W39-S8); OG-ap-1 complete. S71: OG-ap-2 complete after its amendment repaired AC2 retrieval. W41-S1: resolved by the OG-ap-2 date gate: dispatcher 256 SKIP, 0 dispatched (C-S59). W41-S2: registration rode OG-ap-2; the gate loads (SKIPs, never errors), per the C-S59 read. W41-S3: a fact: the write path is byte-equal; Phase D held. W41-S4: resolved by amendment A2 (bound 330 s), 0c54d8b8a0 in HEAD. W41-S5: its blocker (an AMGT_HARVST duplicate id) is gone: comp-surprise AMGT_HARVST duplicate_ids empty. W42-S2: superseded by W43-S7, which measured the I/O cost. W42-S3: a form judgment: calendar_days admitted only as 30. W43-S1: ruled D1 (A7); r29 released, OG-ap-3 complete @fab015fa54. W43-S2: ruled D2, narrowed by W43-S6; shipped in r29. W43-S3: ruled D3 (Alyssa only); the grant was written (RL15_GRANTS.json). W43-S4: ruled D4 option A; the secret and the 5th ARN are applied (ap3.AC1 PASS). W43-S5: moot after A6/A7. W43-S6: the A6 revert record. W44-S1: OG-tg-1 complete after amendment A1 added the three seed-pinning tests. S72: disarmed by A1 (qa-scratch clone pinned, 99c3b4c1b1 in HEAD). S74: resolved by A3; OG-ap-3 complete @fab015fa54. S75: the same: A3 superseded A2; OG-ap-3 complete @fab015fa54. W48-S1: resolved by W48-S3: amendment OG-tl-1 A1 @9ba3e56d87, release commit 78afad4283 under the audited override. W49-S5: resolved by W49-S6: the issuer ruled the in-process check against the box/sitez schema @6b65ca5a52 the validation of record.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W39-S3",
      "NFRA_OPLGTW-Z-W39-S4",
      "NFRA_OPLGTW-Z-W39-S6",
      "NFRA_OPLGTW-Z-W39-S7",
      "NFRA_OPLGTW-Z-W39-S8",
      "NFRA_OPLGTW-Z-S68",
      "NFRA_OPLGTW-Z-S71",
      "NFRA_OPLGTW-Z-W41-S1",
      "NFRA_OPLGTW-Z-W41-S2",
      "NFRA_OPLGTW-Z-W41-S3",
      "NFRA_OPLGTW-Z-W41-S4",
      "NFRA_OPLGTW-Z-W41-S5",
      "NFRA_OPLGTW-Z-W42-S2",
      "NFRA_OPLGTW-Z-W42-S3",
      "NFRA_OPLGTW-Z-W43-S1",
      "NFRA_OPLGTW-Z-W43-S2",
      "NFRA_OPLGTW-Z-W43-S3",
      "NFRA_OPLGTW-Z-W43-S4",
      "NFRA_OPLGTW-Z-W43-S5",
      "NFRA_OPLGTW-Z-W43-S6",
      "NFRA_OPLGTW-Z-W44-S1",
      "NFRA_OPLGTW-Z-S72",
      "NFRA_OPLGTW-Z-S74",
      "NFRA_OPLGTW-Z-S75",
      "NFRA_OPLGTW-Z-W48-S1",
      "NFRA_OPLGTW-Z-W49-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-surprise --project NFRA_OPLGTW --json, ~16:3xZ: open 53, armed 19",
        "git merge-base --is-ancestor fab015fa54, 99c3b4c1b1, 47c3c75f11, 0c54d8b8a0 HEAD: all in HEAD; OG-ap-1/2/3 last <status> complete"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is resolved at HEAD or records a fact; none leaves a live defect."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S62",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-09T17:00Z",
    "one_line": "Round 32 L8: 15 rows GRADUATE to REMEDIATION_v15.md -- defects live at HEAD or acts still owed; W39-S5, W42-S1, W43-S7, W49-S1, W49-S3, W49-S4 and W35-S1 stay ARMED.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "W38-S1: proof-of-spec-check count-bar misreads a pytest summary placed after \"passed N\", so a verbatim line cannot be recorded. W39-S1: sdd-daily-pull.ps1 -Mode enumerate exits without Release-SessionLock, leaving a stale lock on SI2. W39-S2: the enumerate summary prints a one-file type range as 2..0. W39-S5: opal-assets (cot-rebalancer-runner-daily cron) and opal-gateway (mcportal-grant-writer code hash) each carry an unrelated unapplied change that a whole-root apply would also make. S69: lambda-source-map.json is stale for opal-assets-silver-schwab after the Leg C deploy (artifact_sha256, last_deployed_commit, last_deployed_at). S70: the advi-49f-gold-dispatch zip cannot carry BUILD_MANIFEST.json, which both OG-bf-1-Y halves and the source map _build_note say it does. W42-S1: the grant-writer Lambda ships a stale copy of data_entitlement.py and the contract, so it refuses every calendar_months grant (Phase C used the CLI). W43-S7: a cold 13-month availability read for Alyssa costs about 221-235 s per master (443-470 s for both) against the query caps. W44-S2: sender_upn is null on every channel path until User.ReadBasic.All is consented (fails closed). W44-S3: two tests outside tg-1 paths (test_transcript_tools, test_login_admit_r24) pin the concierge as scoped and fail after the mirror. W49-S1: the transcripts bucket KMS key policy gives the gateway role no use of the key, so no s3:PutObject grant alone can make the .pptx pair write once released. W49-S3: two writers share the market_update prefix with different object-name rules (deck_<sha16>.pptx vs the sanitized original), so one deck can land twice under two keys. W49-S4: the market_update PutObject grant was not added: the only registry-read form puts the hand-kept token transcripts in advi_billing_gateway_iam.tf, which the naming gate refuses. W35-S1: the 21:49Z gateway stop drained cleanly; Z-S67 trigger stays inferred, and a restart-free route to the same lost answer exists in server.py; its round-30 order OG-dr-1 still reads pending. W44-S4: after the OG-tg-1 mirror, the concierge /login consent asks the full GRAPH_SCOPES envelope (Mail.Send, Mail.ReadWrite, Files.ReadWrite.All and more); tg-1 is BUILT and HELD for r30, not deployed.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W38-S1",
      "NFRA_OPLGTW-Z-W39-S1",
      "NFRA_OPLGTW-Z-W39-S2",
      "NFRA_OPLGTW-Z-W39-S5",
      "NFRA_OPLGTW-Z-S69",
      "NFRA_OPLGTW-Z-S70",
      "NFRA_OPLGTW-Z-W42-S1",
      "NFRA_OPLGTW-Z-W43-S7",
      "NFRA_OPLGTW-Z-W44-S2",
      "NFRA_OPLGTW-Z-W44-S3",
      "NFRA_OPLGTW-Z-W49-S1",
      "NFRA_OPLGTW-Z-W49-S3",
      "NFRA_OPLGTW-Z-W49-S4",
      "NFRA_OPLGTW-Z-W35-S1",
      "NFRA_OPLGTW-Z-W44-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediations/REMEDIATION_v15.md",
        "each row's own text, read via comp-surprise ~16:3xZ"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```
