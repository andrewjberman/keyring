# IRPT_DASHBD rounds 2-4 compile -- PREPARED, not on the channel (3.0.0_SA_CVO, 2026-10-02 ~20:0xZ)

The row gate refuses new remediation rows while 2 of 11 IRPT_DASHBD orders are not terminal (TO-DB-b-11, TO-DB-b-12, round 5, issued). This file holds the two documents byte for byte as they will land: `adjudications/ADJUDICATION_v2.md` and `remediations/REMEDIATION_v2.md`, copied into the channel when the gate reads 0 open orders. No override was used.

---

## adjudications/ADJUDICATION_v2.md

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
        "deliverables/0.9.0_WK_IRPT_DASHBD~1/BD_LIKEDAY_PULL_R4.json read by this seat: vendor_calls 3, session_token_mints 1, transport_retries 0; requests 0027265115, 0076459710, 0084073310 all HTTP 200; unmapped 0035940058, 0091939812",
        "infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py:144-152 get_clientview_token (the row's read): the POST needs the bearer minted by GET /session/token"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Within the word: one pull of the performance endpoint over one session, the token mint being that session's authentication. This is this seat's reading of the word; Andrew did not name the mint. The next per-use ask (P-5's population pull, CTO batch 178 item 3) should name it, which is the issuer's to write."
  }
]
```

---

## remediations/REMEDIATION_v2.md

# IRPT_DASHBD -- rounds 2 to 4 (workstream B) remediations

<sweep_watermark>2026-10-02T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02 ~19:5xZ. Graduated at ADJUDICATION_v2.md: 11 rows. Closed here on this seat's reads: S13, S16, S21, W1-S10. OPEN: W1-S7 in round-5 cell DB-b-11 and S22 in round-6 cell DB-b-13 (S22 is this seat's own L9 row and stays open until the re-measured pair is read); S12, S15, S18, S19 and S20 are in no round-5 or round-6 cell and come back to 1.0.0_SA_CTO for placement. Round label v5 (round 5, the round after the compiled round 4, as v1 labelled its rows v2), except S22, labelled v6 for its cell. Carried from v1 and not moved here: S8 (OPEN at v2).

```json
[
  {
    "id": "IRPT_DASHBD-S12",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The X10 register's validator admits only csv/json/pdf and one family per table, so the served platinum series.json.gz (the file the page reads) has no retention family; only SERVED_MANIFEST is registered.",
    "evidence": [
      "investigation row IRPT_DASHBD-S12 (CTO round-1 analysis E2: a registry question to the registry's owner)",
      "infra/logic/registry/reporting_policies.json at HEAD (last change 11bf813387, 2026-10-01): policy irpt-dashbd-served-reporting, revision irpt-dashbd-x10-v1, state PENDING_ENFORCEMENT, ONE family SERVED_MANIFEST (platinum, reporting, json); 'json.gz' 0 occurrences, 'series' 0",
      "lib/opal_naming.py:1822-1823 at HEAD: an extension not in {'csv', 'json', 'pdf'} raises 'reporting content format is not admitted'",
      "s3api list-objects-v2 opal-data-49financial irpt/49financial/platinum/reporting/ (this seat ~19:3xZ): 12 keys, 6 of them series.json.gz, all written 2026-10-02T13:56:29-30Z"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the register owner admits a gzip JSON format or a second reporting table so the series takes its own family (a register edit plus the validator's admitted set). Round 5's DB-b-12 adds a per-client summary file that will need a family the same way. Placement is 1.0.0_SA_CTO's at the next analysis.",
    "owner": "4.0.0_SA_CRO",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S13",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Nothing ran account_return_daily.py on a clock, so the reporting gold froze at date=2026-09-28 and the 08:15 ET publisher would have republished that series every weekday.",
    "evidence": [
      "investigation row IRPT_DASHBD-S13; CTO round-2 analysis E1; round-3 cell DB-b-7 (@ff4b28b3e3, proof @ceb03a4137); ledger org/critical_paths/change_management/20261002T0801Z_irpt-dashbd-reporting-gold-apply-20261002_deploy_completion.md",
      "aws scheduler list-schedules --name-prefix irpt-49f-reporting (this seat ~19:3xZ): irpt-49f-reporting-gold-daily ENABLED",
      "logs filter-log-events /aws/lambda/irpt-49f-reporting-gold-lambda, pattern START (this seat): one invocation since the apply, START 2026-10-02T11:41:47Z, the schedule's 07:41 ET minute",
      "s3api list-objects-v2 and list-object-versions, opal-data-49financial irpt/49financial/gold/account_return_daily/ (this seat): 562 date= partitions (559 at the row), newest date=2026-10-01, the T-1 trading day for Friday 2026-10-02; date=2026-09-29, 09-30 and 10-01 each one version at 11:42:08Z; date=2026-10-01/manifest.json: asof 2026-10-01, rows 6, day_quality_census MEASURED 6, return_basis_census TWR 6"
    ],
    "remedy": "Done: the adapter runs on its own schedule, and its first scheduled fire carried the gold from 2026-09-28 to the T-1 date 2026-10-01 in one invocation at the schedule's minute.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S15",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The reporting read route lives in its own root under the existing portal authorizer and is absent from docs/contracts/investor-reporting/v1/routes.json, which routetable.py calls the one carrier of the route table, so the unguarded-route census does not see it.",
    "evidence": [
      "investigation row IRPT_DASHBD-S15",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_IRPT_DASHBD_READ_ROUTE_20261002.md:21-24: 'IRPT_DASHBD-S15 ... ACCEPTED. One writer per route KEY holds ... Naming the route in the contract without the api root generating it (a duplicate key would fail that root's apply) is hygiene for the issuer at round 3, not a condition here.'; CTO round-2 analysis section 2 hygiene line: 'At the drain or the next change to entry.py; not cells.'",
      "docs/contracts/investor-reporting/v1/routes.json at HEAD (last change 31999d12d4, 2026-10-02T12:29Z): 19 routes; 'investor-reporting/reporting' 0 occurrences",
      "infra/aws/terraform/investor-reporting/reporting-read/api.tf:11 at HEAD: 'The route is NOT in the published routes.json: row IRPT_DASHBD-S15 names what that leaves to the issuer.'"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the issuer names the route in routes.json without the api root generating it, as hygiene at a drain. Not done at the round-3 or round-4 drain.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S16",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seating check read assignees through to-check.py's resolver, whose SERIAL_RE admitted no underscore in the name and only one capital letter as a lane, so every IRPT worker slot collapsed to 0.9.0_WK_IRPT; once enforced, it would refuse a correct issuance.",
    "evidence": [
      "investigation rows IRPT_DASHBD-S16 and S17 (S17 measured that @453c6430ec did not fix it)",
      "CTO RULINGS batch 124 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md:5076-5092), fixed in .tools/to-check.py @0b8f897e7d",
      "this seat's run ~19:3xZ: .tools/to-check.py SERIAL_RE at :154; _assignees_from_field('0.9.0_WK_IRPT_DASHBD~1') -> ['0.9.0_WK_IRPT_DASHBD~1']; '0.9.0_WK_IRPT_BCKEND~3' and '2.0.0_SA_COO~MI' returned whole; negative control: the pre-fix pattern on '0.9.0_WK_IRPT_DASHBD~1' -> '0.9.0_WK_IRPT'"
    ],
    "remedy": "Done by 1.0.0_SA_CTO in .tools/to-check.py (batch 124). Not re-run here: the seating lint over a live issuance; the resolver it reads was exercised directly.",
    "owner": "1.0.0_SA_CTO",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S18",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The PRD's C-NAMES prints a function that was never made (irpt-49f-reporting-adapter-lambda) and none of the reporting-gold resources DB-b-7 made, so a reader of the PRD cannot find the deployed resources (CLAUDE.md rule 30).",
    "evidence": [
      "investigation row IRPT_DASHBD-S18",
      "prd/IRPT_DASHBD_PRD.md at HEAD, prd_version v0.6, last change aabc054e89 (2026-10-02T01:32Z, before DB-b-7's apply): irpt-49f-reporting-adapter-lambda 1 occurrence; irpt-49f-reporting-gold-lambda, irpt-49f-reporting-gold-role, irpt-49f-reporting-gold-policy, irpt-49f-reporting-gold-daily and irpt-reporting-gold-lambda 0 each; irpt-49f-reporting-read-lambda 0 (the read root's function is absent too); irpt-49f-reporting-publish-lambda 3",
      "decompositions/IRPT_DASHBD_DECOMP.md section 3 prints the builder output for the reporting-gold names"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the PRD's author prints the builder output for the reporting-gold and reporting-read names and strikes the adapter name.",
    "owner": "1.0.0_SA_CTO",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S19",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DB-7-AC1 requires at least 10 measured landings per input and counts them before the exclusions it then applies: for holdings_performance_daily, which sets the 07:41 ET fire, 9 of 12 are excluded and 3 kept (2 organic 07:30 fires).",
    "evidence": [
      "investigation rows IRPT_DASHBD-S19 and W1-S8; deliverables/0.9.0_WK_IRPT_DASHBD~1/REPORTING_GOLD_FIRE_TIME_R3.json (excluded list, 11 entries)",
      "first scheduled fire (this seat ~19:3xZ): holdings_performance_daily date=2026-10-01 landed 11:30:18Z; reporting-gold START 11:41:47Z; account_return_daily date=2026-10-01 carries 0 GUARD_NOT_REACHED. One organic day on which the fire followed its input; date=2026-09-29, written by the same fire, carries 1 GUARD_NOT_REACHED and 1 NOT_MEASURABLE (cause not read)"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the issuer amends DB-7-AC1 to count kept landings (or states the kept floor it accepts) and reads the organic landings as they accrue. Open until the criterion grades what the schedule rests on.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S20",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The account picker's suffix dates 'data through' from manifest.as_of and the page body from series.as_of, and the read never checks that the two agree, so a manifest and a series of different vintages would show one account two dates.",
    "evidence": [
      "investigation row IRPT_DASHBD-S20",
      "portal origin/DEV f2d69887 (this seat ~19:3xZ; the three files last changed 06bc6f85, 2026-10-02T09:43Z): src/pages/InvestorReporting/tabs/reporting/pickerSuffix.ts dashboardYtdSuffix builds 'data through' from answer.manifest.as_of; src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx:241 prints series.as_of; src/pages/InvestorReporting/dashboard/reportingRead.ts holds 0 'as_of'/'asOf' occurrences (no comparison)",
      "served today: 6 of 6 platinum manifests read as_of 2026-10-01, written in the same run as their series (13:56:29-30Z), so the split is not observed on served data"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: read one date for both, or refuse the pair when manifest.as_of and series.as_of differ (portal).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S21",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The publisher heads the series object after its two puts, and its role had PutObject but no GetObject on platinum/reporting, so HeadObject answered 403 and the run aborted after the first account.",
    "evidence": [
      "investigation row IRPT_DASHBD-S21; CTO RULINGS batch 172 (RULINGS.md:5763-5769): 'SIGNED: amendment 1 to DB-b-8 (packet blob 2baec1651d). s3:GetObject on exactly platinum/reporting/*, the prefix the role already writes, plan 0/1/0. Then Q1 runs again.'",
      "infra/aws/terraform/investor-reporting/reporting-publish/iam.tf:74-82 at HEAD: statement ReadBackThePlatinumReportingPrefixOnly, s3:GetObject on local.irpt_rp_platinum_write_arns (the write set, nothing wider)",
      "logs /aws/lambda/irpt-49f-reporting-publish-lambda since 13:30Z (this seat): invocation a4019573 ended '[ERROR] ClientError ... (403) ... HeadObject'; the next, a8df95ef, REPORT 14,479 ms with no ERROR line",
      "s3api list-objects-v2 platinum/reporting/ (this seat ~19:3xZ): 12 of 12 keys LastModified 2026-10-02T13:56:29-30Z; all 6 manifest.json read as_of 2026-10-01"
    ],
    "remedy": "Done: the read-back grant on the written prefix only, then the Q1 re-run published 6 of 6 accounts as of 2026-10-01. Not yet read: Monday 2026-10-05 08:15 ET's scheduled fire (A1 of ledger irpt-dashbd-reporting-publish-apply-20261002, still open), which is FWD-1's acceptance, not this row's.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W1-S7",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The scheduled handler takes the newest landed partition's account set (six accounts) as its population and omits the producer's emit_method_row (a write outside its role); the order was silent on both.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S7",
      "account_return_daily date=2026-10-01/manifest.json, written by the first scheduled fire (this seat): rows 6, first_data_date keys 6",
      "CTO RULINGS batch 178 item 2 (RULINGS.md:5849-5852): '(2) widen the precomputed path to every 49 Financial account, then per firm, with PATH A retired in the same window'",
      "task-orders/IRPT_DASHBD.TO-DB-b-11.every-49f-account-measured.md (round 5, status issued):27 'The gold's account set is the newest partition's (handler.py:18-19' and :46 'In reporting-gold/handler.py, the account set comes from the declared population'",
      "task-orders/IRPT_DASHBD.TO-DB-b-13.fwd8-three-pairs-and-tolerance.md (round 6, status issued):44: emit_method_row writes tieout_tolerance, and the method row's served write is the issuer's packet, not the scheduled handler"
    ],
    "remedy": "IN ROUND-5 CELL DB-b-11: the population limb is cut (the declared 49 Financial population replaces the newest-partition default). The method-row limb stands as built: the handler does not write dim_return_method.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W1-S10",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The CRO's code table is generated by a first-match builder in which wd-generic preceded foreign-tax, so FTP/FC/WD and FTR/FC/WD read EXTERNAL; a hand edit of the JSON alone would revert on the next build.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S10",
      "git log: 3cb9f9b6d5 (4.0.0_SA_CRO, 2026-10-02T09:36Z) 'FTP/FC/WD and FTR/FC/WD move EXTERNAL -> INTERNAL (foreign tax) -- builder rule order fixed, table re-applied, 2 rows moved'",
      "org/tier1_exec/4.0.0_SA_CRO/scripts/build_schwab_txn_classification.py at HEAD: 'foreign-tax' at :59 precedes 'wd-generic' at :71",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json at HEAD, 187 rows: FTP/FC/WD (2,449 rows) and FTR/FC/WD (4 rows) rule foreign-tax, partition INTERNAL; FTP/FC/FC and FTR/FC/FC unchanged, INTERNAL"
    ],
    "remedy": "Done: both files edited together by the table's owner, so the builder regenerates what the table holds.",
    "owner": "4.0.0_SA_CRO",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S22",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-4 tie-out's largest disagreement (0027265115, 2026-06-25..07-06, 1.21 points over 7 like days) carried no stated reason, and its cause is findable: Opal books income +0.4627% on 06-25 where Black Diamond nets income -2,470.31 on an account about 47 pct short, consistent with Opal counting dividends received but not dividends paid on shorts (inferred).",
    "evidence": [
      "investigation row IRPT_DASHBD-S22; this seat's L9 grade @7a062defc3, org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_FWD8_L9_GRADE_20261002.md: FWD-8 NOT REALIZED",
      "CTO RULINGS batch 181 (RULINGS.md:5887-5905): tieout_tolerance 0.35 percentage points per like-day window; 'A reason that is an Opal defect is a defect row: it is fixed and the pair re-measured ... That is row IRPT_DASHBD-S22, 2.0.0_SA_COO~P's.'; batch 182 item 1 (:5907-5916): 11 of 14 pairs within, 3 beyond (0027265115 06-25 1.2130, 0084073310 08-21 0.7078, 0027265115 04-09 0.4555)",
      "decompositions/IRPT_DASHBD_DECOMP.md section 6 (round 6, @c94a1de98b) and task-orders/IRPT_DASHBD.TO-DB-b-13.fwd8-three-pairs-and-tolerance.md (status issued):20 'Row IRPT_DASHBD-S22 | Decomp cell: DB-b-13 ... outcome_ref: FWD-8'"
    ],
    "remedy": "IN ROUND-6 CELL DB-b-13: the producer books a short's paid dividend as negative income, the pair is re-measured from the stored responses with 0 vendor calls, and the other two pairs beyond 0.35 pp carry stated reasons; then the issuer's packet re-pins the reporting gold and rewrites the affected account-days. FWD-8 returns to 3.0.0_SA_CVO. This is the L9 seat's own row: it is never dismissed and stays OPEN until the re-measured pair is read.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v6"
    },
    "closed": false
  }
]
```
