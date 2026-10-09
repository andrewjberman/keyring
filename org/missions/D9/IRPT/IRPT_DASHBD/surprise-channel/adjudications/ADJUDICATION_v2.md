# IRPT_DASHBD -- rounds 2 to 4 (workstream B) L8/L9 adjudication

<sweep_watermark>2026-10-02T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02 ~19:5xZ. L8 input: the issuer's drain-end records deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND2_B_DRAIN_END_20261002.md @fde5518653 and IRPT_DASHBD_ROUND4_B_DRAIN_END_20261002.md @65d7e15b20 (round 3 has no drain-end file; its cells DB-b-7, DB-b-8 and DB-b-9 are read from their orders, ledgers and the served artifacts); the CTO's round-2 analysis @f5fbeaa543 with its correction line; CTO RULINGS batches 124, 133, 172, 178, 181 and 182. Rounds 5 (@aafc9bd3f7) and 6 (@c94a1de98b) are already issued and are read only for placement. 18 of 18 rows surfaced after the previous watermark 2026-10-02T02:50Z (S12 to S22, W1-S5 to W1-S11; W1-S3 and W1-S4 were never filed, S14 and S15 carry them); 31 rows in the channel, 13 compiled at v1. 7 dismissed by the 6 rows below (S14, S17, W1-S5, W1-S6, W1-S8, W1-S9, W1-S11); 11 graduated in remediations/REMEDIATION_v2.md, of which 4 arrive REMEDIATED and closed (S13, S16, S21, W1-S10) and 7 stay OPEN (S12, S15, S18, S19, S20, W1-S7, S22). 0 rows ARMED. Every closure and every dismissal of a remedied subject rests on a read this seat made at ~19:3xZ (code at HEAD, portal origin/DEV, the served S3 objects, the function logs, the schedules). Notes: S22's surfaced_at (18:45Z) is this seat's estimate, later than its commit (18:21:54Z); the watermark follows it. REMEDIATION_v1's header prose still says S6 is OPEN; its row's clocks were advanced in place at a53c130cb6 (evidence in org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_FAST_PIN_GRADES_20261001.md, section 'IRPT_DASHBD E3 leg (a)'). W1-S11's token mint is read as covered by card 4; CTO batch 180 item 4 records the card done with '3 performancePeriod calls plus 1 token mint'.

```json
[
  {
    "id": "IRPT_DASHBD-C-S5",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T19:50:00Z",
    "one_line": "S14 is ruled in scope: the read role's scope-dependency and service-profile reads are statements the read-route packet lists and both never-widen halves signed as the role's blast radius; the code now cites S14, not the never-filed W1-S3.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-S14"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The role reads the platinum reporting prefix, the shared boundary's two scope dependencies (object-scoped) and the opal-users-v2 service profile, and writes nothing; the signed packet enumerates exactly those statements.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_IRPT_DASHBD_READ_ROUTE_20261002.md:11 (SIGNED ~05:4xZ, bound to packet blob f44ee4d312): 'the role is read-only on 49 Financial's platinum reporting prefix plus the boundary's scope reads'",
        "deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_DASHBD_READ_ROUTE_20261002.md:20 lists aws_iam_role_policy.irpt_reporting_read_service_profile (dynamodb:Query on opal-users-v2/index/email-index, dynamodb:GetItem on opal-users-v2, kms:Decrypt via DynamoDB only); :58 'Scope dependencies: object-scoped, the same grants the Holdings function holds (row IRPT_DASHBD-S14). Writes: none'",
        "infra/aws/terraform/investor-reporting/reporting-read/iam.tf:3-7 at HEAD: the order's 'ONLY the platinum prefix' is the PRODUCT read; the two scope dependencies cite row IRPT_DASHBD-S14 (re-pointed from W1-S3, as the row's notes said)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled in scope by the signed halves: the reads beyond the platinum prefix are the shared boundary's own dependencies, enumerated statement by statement in the packet, with no product read beyond platinum and no write."
  },
  {
    "id": "IRPT_DASHBD-C-S6",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T19:50:00Z",
    "one_line": "S17 corrected the round-2 analysis's 'S16 fixed' and is answered by CTO batch 124, which fixed the truncation at its source (to-check.py's assignee resolver); S16 itself is graduated REMEDIATED in REMEDIATION_v2.md.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-S17"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The seating check reads assignees through .tools/to-check.py _assignees_from_field; at HEAD that resolver returns 0.9.0_WK_IRPT_DASHBD~1 whole, where the pre-fix pattern returns 0.9.0_WK_IRPT.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CTO RULINGS batch 124 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md:5076-5092): the seating check reads assignees through to-check.py's _assignees_from_field, whose SERIAL_RE admitted no underscore; fixed in .tools/to-check.py; 'Rows S16 and S17 are answered by this fix; the round-2 analysis carries a correction line.'",
        "CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_2_B_20261002.md:46, CORRECTION: section 3's 'S16 ... fixed @453c6430ec ... Answered' was WRONG; 'The truncation was in to-check.py's resolver ... fixed by RULINGS batch 124.'",
        "this seat's run ~19:3xZ: .tools/to-check.py (last change 0b8f897e7d, batch 124), SERIAL_RE at :154; _assignees_from_field('0.9.0_WK_IRPT_DASHBD~1') -> ['0.9.0_WK_IRPT_DASHBD~1'], '0.9.0_WK_IRPT_BCKEND~3' and '2.0.0_SA_COO~MI' returned whole; negative control: the pre-fix pattern on '0.9.0_WK_IRPT_DASHBD~1' -> '0.9.0_WK_IRPT'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A correction row whose subject is remedied at HEAD; the defect it measured is carried to closure on S16's remediation row (one finding, one row)."
  },
  {
    "id": "IRPT_DASHBD-C-S7",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T19:50:00Z",
    "one_line": "W1-S5 is ruled: the CTO's round-2 analysis accepts the residual as a net of four offsetting classes and rules the margin-interest class no change; the absolute-value residual check it names is not reused in any later round's checks.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W1-S5"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The residual record stands as filed; margin interest stays internal at Opal as a stated methodology difference; the one check that sums is_residual legs by absolute value lives in checks/r2 only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_2_B_20261002.md section 3: 'W1-S5: accepted as the issuer's (a net-aware sum if the check is reused).'; section 2, margin interest: 'RULED, NO CHANGE: Opal is right ... The difference to Black Diamond is a stated methodology difference; the tie-out record names it.'",
        "Grep 'resid_sum|is_residual' over deliverables/2.0.0_SA_COO~P/checks/ (r1 to r6, 40 entries): 1 file, checks/r2/p2_6_ac1_flow_residual_record.py; no r3 to r6 check reuses it"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled by the CTO's round-2 analysis; the condition attached to the ruling (a net-aware sum if the check is reused) has not been triggered."
  },
  {
    "id": "IRPT_DASHBD-C-S8",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T19:50:00Z",
    "one_line": "W1-S6's stopped fire time is ruled by the issuer's amendment 1 to TO-DB-b-7, and W1-S8's extension to the backfill partitions follows clause (a)'s own words; the schedule is live and its first fire ran after its input. The residual both name (the time rests on few organic landings) is S19's, which stays open.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W1-S6",
      "IRPT_DASHBD-W1-S8"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "Schedule irpt-49f-reporting-gold-daily is ENABLED; its one invocation since the apply started 2026-10-02T11:41:47Z; holdings_performance_daily date=2026-10-01 landed 11:30:18Z; the fire wrote account_return_daily date=2026-09-29, 09-30 and 10-01 at 11:42:08Z, and the 10-01 partition reads 6 rows, day_quality MEASURED 6, guard_state GRADED_AGREED 1 and NOT_GRADED_OUTSIDE_DOMAIN 5, 0 GUARD_NOT_REACHED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/IRPT_DASHBD.TO-DB-b-7.reporting-gold-scheduled-fire.md:71-79, ISSUER AMENDMENT 1 (@f90e619529, ruling row W1-S6): '(a) a partition's landing is the FIRST version's LastModified (its scheduled write) ... (b) ONE day is set aside as a known incident ... (c) the handler's no-gap stop makes such a day safe -- it emits nothing and the next fire catches up'",
        "aws scheduler list-schedules --name-prefix irpt-49f-reporting (this seat ~19:3xZ): irpt-49f-reporting-gold-daily ENABLED, irpt-49f-reporting-publish-daily ENABLED",
        "logs filter-log-events /aws/lambda/irpt-49f-reporting-gold-lambda, pattern START (this seat): one START, 2026-10-02T11:41:47Z",
        "s3api list-object-versions, opal-data-49financial irpt/49financial/gold/ (this seat): account_return_daily 562 date= partitions, newest date=2026-10-01 (T-1 for Friday 2026-10-02); date=2026-09-29, 09-30, 10-01 each one version at 11:42:08Z; holdings_performance_daily date=2026-10-01 one version at 11:30:18Z; the 10-01 data.parquet read: 6 rows, MEASURED 6, GRADED_AGREED 1, NOT_GRADED_OUTSIDE_DOMAIN 5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W1-S6 is ruled by the issuer's amendment, and the ruled schedule serves. W1-S8's exclusion of the unscheduled backfill writes follows clause (a) '(its scheduled write)'. The residual both rows name, a fire time resting on 3 kept landings (2 organic), is one finding carried open on S19."
  },
  {
    "id": "IRPT_DASHBD-C-S9",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T19:50:00Z",
    "one_line": "W1-S9 is ruled: CTO batch 133 signs leg (a) (the adapter's override retired, the reporting-gold function re-pinned) and rules leg (b), the 49F engine's vendored copy, NOT PURSUED; the table the reporting-gold function packages is now pinned with its producer and carries FTP/FTR INTERNAL.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W1-S9"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The source map pins the producer and the code table together at 4ad4008907, whose table reads FTP/FC/WD and FTR/FC/WD rule foreign-tax, partition INTERNAL; the 49F engine keeps its vendored copy by ruling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CTO RULINGS batch 133 (RULINGS.md:5224-5234): '1. SIGNED: leg (a) -- the adapter's override retired and the reporting-gold function re-pinned, output-neutral ... 2. RULED: leg (b) is NOT PURSUED. The 49 Financial engine (c02) is not patched ... The engine keeps its vendored table, nothing it serves moves, and the two treatments are a stated methodology difference until c02 retires.'",
        "infra/aws/lambda/ci/lambda-source-map.json entry irpt-reporting-gold-lambda at HEAD: staged_from account_return_daily.py pin 4ad4008907 and SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json pin 4ad4008907 (one pin for both, as the row asked); git show 4ad4008907 of the table: FTP/FC/WD and FTR/FC/WD rule foreign-tax, partition INTERNAL",
        "lambda get-function-configuration irpt-49f-reporting-gold-lambda (this seat): LastModified 2026-10-02T12:17:04Z; ledger org/critical_paths/change_management/20261002T1157Z_irpt-dashbd-foreign-tax-leg-a-20261002_deploy_completion.md; this seat's leg (a) grade @a53c130cb6 (PASS on the artifact)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The 49F half is ruled out of scope by batch 133 item 2; the IRPT half the row asked for (table and producer re-staged together) is at HEAD in the source map and was re-deployed under leg (a)."
  },
  {
    "id": "IRPT_DASHBD-C-S10",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T19:50:00Z",
    "one_line": "W1-S11: Andrew's card-4 word covered the session-token GET. The word allows ONE pull, and the order itself prescribes 'One session' over the estate's client and the session secret; the bearer mint opens that session and is not a second data call. No other endpoint was called and the record discloses the mint.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W1-S11"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "1 GET /session/token and 3 performancePeriod POSTs (all HTTP 200, 0 retries, 0 performanceSeries, no call for the 2 unmapped accounts). The order's BOUNDS line 'NO other call' is narrower than the act the same order prescribes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_132xZ_ALL_RECS_APPROVED_OPEN_CALLS.md:13, card 4: 'YES, ONE pull, scoped to the five round-1 accounts: Black Diamond's return over each of Opal's gap-free segments'; :16 'The vendor word in card 4 is ONE pull ... It is not a standing grant.'",
        "task-orders/IRPT_DASHBD.TO-DB-b-10.black-diamond-like-day-pull.md:46-52 'THE ONE PULL. One session; for each mapped account, at most ONE performancePeriod request ... tenants.py for 49 Financial's route and session, the blackdiamond/49f/session secret'; :89 BOUNDS 'Vendor: the one pull above and NO other call'",
        "deliverables/0.9.0_WK_IRPT_DASHBD~1/BD_LIKEDAY_PULL_R4.json read by this seat: vendor_calls 3, session_token_mints 1, transport_retries 0; requests acct#e7ab8585, acct#37ac6e23, acct#a4af74fa all HTTP 200; unmapped acct#23898664, acct#7e343f56",
        "infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py:144-152 get_clientview_token (the row's read): the POST needs the bearer minted by GET /session/token"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Within the word: one pull of the performance endpoint over one session, the token mint being that session's authentication. This is this seat's reading of the word; Andrew did not name the mint. The next per-use ask (P-5's population pull, CTO batch 178 item 3) should name it, which is the issuer's to write."
  }
]
```
