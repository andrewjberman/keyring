# IRPT_BCKEND -- project sweep 8 L8/L9 adjudication (rounds 42-46 ~P; the ~Y FAST interval to Y-5 V1)

<sweep_watermark>2026-10-04T03:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-04 ~20:3xZ (DRAFT). L8 inputs: the issuer's drain-end records under `deliverables/2.0.0_SA_COO~P/` (`IRPT_BCKEND_ROUNDS_42_44_P_DRAIN_END_20261004.md`, `IRPT_BCKEND_ROUND_45_P_DRAIN_END_20261004.md`, `IRPT_BCKEND_ROUND_46_P_DRAIN_END_20261004.md`); `STATUS~Y.md` (02:3xZ); CTO RULINGS batches 226-237; this seat's grades in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_FAST_PIN_GRADES_20261001.md` (rounds 42-44, 45 and 46, with the S299 and S293 closes) and its naming rulings in `CVO_RULING_NAMING_LIMB_SOURCE_MAP_CITATION_NOT_MINT_20261004.md`; and this seat's own reads for this compile (code and git at CLOUD HEAD 96f17cdbe9, portal ls-remote and ancestry, one node test run, and read-only AWS reads: six Lambda configurations, the render host script's S3 version, the PROD export receipt, one irpt-jobs item, and one secret's version metadata, never its value). 18 items compiled: every row surfaced after 2026-10-03T08:52Z (S306-S319, W110-S1, W113-S1, W114-S1, W115-S1), none referenced by any file in adjudications/ or remediations/. 11 are dismissed by the 5 rows below; 7 graduate in remediations/REMEDIATION_v19.md: 6 REMEDIATED and closed, 1 OPEN. ARMED: 6 before (5 BLOCKING, 1 OBSERVATION); 4 arrive DISARMED (S307, S310, S311, S316), S308 is dismissed into S310 (its re-point; S308's own disarm record is S312), and 1 stays ARMED after this compile (S318). Clock owed in place at publish, outside these 18: S288 (REMEDIATION_v18), DISARMED by 2.0.0_SA_COO~Y on rows S306 and S315, and REMEDIATED and closed (C-S283).

```json
[
  {
    "id": "IRPT_BCKEND-C-S283",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "S306 and S315 are 2.0.0_SA_COO~Y's disarm records for S288: the YCharts session restored from Andrew's HAR without a sign-in (16:36Z), then the remediation row's own disarm condition measured (22:45Z).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S306",
      "IRPT_BCKEND-S315"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S306: Andrew's fresh session (his HAR, 16:16Z) seeded a host capture with no sign-in, persisted at fence 25, and one read through the resident's runtime answered 200 LIVE (ledger irpt-signin-har-20261003 CLOSED 4 of 4); option A was not needed. S315 measures what REMEDIATION_v18 named as S288's disarm: fence 25 (above 23) and securities_info resolves answered on the stored session at 20:55:33Z and 22:28:06Z; CTO batch 234 item 3 asked for it. Neither carries a new finding. S288 still reads disarm ARMED and remediation OPEN in REMEDIATION_v18 at CLOUD HEAD; its clock is advanced in place when this compile is published: disarm DISARMED by 2.0.0_SA_COO~Y at 2026-10-03T22:45:00Z (S315, the record of the row's own condition), and REMEDIATED and closed, because the re-capture the remedy asked for was made (by HAR seed, not option A) and Y-3 (17:03:14Z) and Y-5 V1 (02:28:20Z) reached READY on it. The class (one YCharts seat per login; a sign-in elsewhere ends the session) stays S233's, as S306 records.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-S306, IRPT_BCKEND-S315",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/SIGNIN_HAR/H1_LEG_H_OUTPUT_20261003.txt and V1_LEG_P_READ_20261003.txt (S306's grounding); ledger irpt-signin-har-20261003 CLOSED 4/4",
        "CTO RULINGS batch 234 item 3: S288 goes to 2.0.0_SA_COO~Y, its disarm owner, to read the live session and disarm the row or name why not",
        "STATUS~Y.md (02:3xZ): 'Stored YCharts session | LIVE at fence 25 since the HAR seed (S288 disarm row S315; the remediation clock is the CVO's)'",
        "REMEDIATION_v18.md S288 at CLOUD HEAD 96f17cdbe9: disarm ARMED, remediation OPEN, closed false (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
        "secretsmanager list-secret-version-ids ycharts/session/current, metadata only, never the value: AWSCURRENT created 2026-10-04T19:45:16Z, AWSPREVIOUS 2026-10-04T19:45:08Z, both after the 2026-10-03T00:10:45Z version S288 named (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarm records filed by S288's disarm owner; their effect is a clock advance on S288, not a new item."
  },
  {
    "id": "IRPT_BCKEND-C-S284",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "Five disarm or resolution records filed by 2.0.0_SA_COO~P: S309 (S307), S312 (S308), S313 (S310), S314 (S311) and S319 (W115-S1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S309",
      "IRPT_BCKEND-S312",
      "IRPT_BCKEND-S313",
      "IRPT_BCKEND-S314",
      "IRPT_BCKEND-S319"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Each record's effect is carried by the row it names. S307, S310 and S311 graduate in REMEDIATION_v19.md as REMEDIATED and closed with a disarm object, and W115-S1 as REMEDIATED and closed; S308 is dismissed into S310 (C-S285). S312, S313 and S314 cite one served run: the ****0090 49F PATH B export, receipt EXP-e29b5415a06f90f943481c41a1a4821b READY at 22:13:15Z with facts.frozen_as_of 2026-10-01, which this compile re-read on S3 (the rounds 42-44 grade had taken it from the ledgers). S319 cites the CHANGELOG commit 236f660bb6, admitted by this seat's second naming follow-on as implemented by 1.0.0_SA_CTO @df94193739.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-S309, IRPT_BCKEND-S312, IRPT_BCKEND-S313, IRPT_BCKEND-S314, IRPT_BCKEND-S319",
        "CTO RULINGS batch 228 item 1 (the authorizer ledger closes; S307 DISARMED), batch 230 item 2 (R1 READY: leg V closes and S308 disarms) and batch 231 item 4 (R1 READY disarms S308 and S311)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/IRPT_BCKEND_ROUNDS_42_44_P_DRAIN_END_20261004.md, table 'BLOCKING: 4, all disarmed': S307/S309, S308/S312, S310/S313, S311/S314",
        "s3 get-object opal-data-ycharts firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json: job_state READY, facts.frozen_as_of 2026-10-01, page_count 11, validation_status PASSED, LastModified 2026-10-03T22:13:15Z (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
        "IRPT_BCKEND_ROUND_46_P_DRAIN_END_20261004.md (W115-S1 OPEN at the drain) and commit 236f660bb6 (2.0.0_SA_COO~P), an ancestor of CLOUD HEAD 96f17cdbe9: the recorder's CHANGELOG entry committed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Records of disarms and of one resolution; the hazards they end are carried, and closed, on the rows they name."
  },
  {
    "id": "IRPT_BCKEND-C-S285",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "S308 named the served print page as the refusing layer; S310 (CTO batch 229) re-points it to the render host's allow-list, so S310 carries the hazard and its remedy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S308"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CTO batch 229 read render_export.cjs:83: PRINT_QUERY_KEYS held bundle, tenant, revision, kind, selection, start and end, so account and version never reached the print URL. The served PrintEntry was correct: it refuses only when neither a selection nor an account is present. The disarm owner moved from 2.0.0_SA_COO~D to 2.0.0_SA_COO~P, and no portal promote was owed for S308. S308's hazard (no 49F export reaches READY) is the hazard S310 carries, and both disarmed on the one READY run (S312, S313; CTO batch 230 item 2). A remediation row for S308 would carry a mechanism the CTO's read refuted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-S308",
        "CTO RULINGS batch 229 items 1-2 (S308's disarm owner re-pointed to 2.0.0_SA_COO~P; the fix is PRINT_QUERY_KEYS) and batch 230 item 2",
        "investigation row IRPT_BCKEND-S310 (the re-point) and IRPT_BCKEND-S312 (S308's own disarm record, 22:30Z)",
        "infra/aws/ec2/investor-reporting-export/render_export.cjs at CLOUD HEAD 96f17cdbe9: PRINT_QUERY_KEYS = bundle, tenant, revision, kind, selection, start, end, account, version, request (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded by S310, which names the cause and graduates REMEDIATED and closed with its disarm (S313); S308's own disarm record is S312."
  },
  {
    "id": "IRPT_BCKEND-C-S286",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "W110-S1 (the IB-rtq-2 authorizer test asserts exactly three render routes) and S317, the issuer's disposition: that test is a frozen worker deliverable which no suite runs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W110-S1",
      "IRPT_BCKEND-S317"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "test_edge_render_delegate_v2_authorizer.mjs lives under deliverables/0.9.0_WK_IRPT_BCKEND~15/, the record of that worker's run at its own pin, not a product test. The product suite is infra/aws/users/lambda/portal-authorizer/tests/, which holds one file, test_render_reporting_series.mjs; it passes 9 of 9 with the fourth route, including arms that keep the earlier routes' behavior. Editing the deliverable would rewrite a record.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-W110-S1, IRPT_BCKEND-S317",
        "infra/aws/users/lambda/portal-authorizer/tests/ at CLOUD HEAD 96f17cdbe9: one file; node --test tests/test_render_reporting_series.mjs: tests 9, pass 9, fail 0 (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~15/test_edge_render_delegate_v2_authorizer.mjs present beside that order's proof_of_spec.json (this compile's read, 2026-10-04 ~20:0xZ-20:3xZ)",
        "IRPT_BCKEND_ROUNDS_42_44_P_DRAIN_END_20261004.md: 'W110-S1 | ... | carried to drain hygiene'; S317 committed b7c793dad0 (2.0.0_SA_COO~P)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A record of a frozen deliverable's assertion; no suite or gate runs it, and the live suite covers the earlier routes."
  },
  {
    "id": "IRPT_BCKEND-C-S287",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "W113-S1: the recorder's first irpt-ycharts-generate run hit the worker's own `timeout 300` before its commit; the identical re-run committed fb8653e0e3 and absorbed the staged leftover.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W113-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The 300 s bound was the worker's wrapper, not the recorder's. The re-run's commit fb8653e0e3 (2 files) changed exactly one source-map row, and nothing stayed staged. The issuer recorded it at the drain as no defect in the recorder, and IB-pr-310's re-read on CLOUD found the three functions' records equal to live. The cold-start time of the recorder is unmeasured; no order depends on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-W113-S1",
        "commit fb8653e0e3 (0.9.0_WK_IRPT_BCKEND~113, 'ci: record deploy investor-reporting @ 2ba6a4c2'), an ancestor of CLOUD HEAD 96f17cdbe9",
        "IRPT_BCKEND_ROUNDS_42_44_P_DRAIN_END_20261004.md: 'W113-S1 | ... | no defect in the recorder; recorded'; IB-pr-310 drained @8b37555b1b with fix-up @9b917d2aae",
        "IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, rounds 42-44: IB-pr-310 PASS, deployed_code_sha256 equal to live for irpt-ycharts-generate, irpt-holdings and irpt-status at the 00:4xZ read"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A worker's wrapper timeout on one cold run; the recorder's re-run completed it with no residue, and the issuer ruled it no defect."
  }
]
```
