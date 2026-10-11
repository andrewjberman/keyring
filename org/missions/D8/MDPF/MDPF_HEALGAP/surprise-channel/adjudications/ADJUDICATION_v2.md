# MDPF_HEALGAP -- round 2 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-11T02:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:45:00Z. L8 packet: 2.0.0_SA_COO~G1 msg 3360, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_DRAIN_END_REPORT_DRAFT.md` @4832293fd4. Risk WORLD. 5 of 5 orders complete. 14 open rows swept (13 in the tree channel, S1 in the legacy flat channel), every grade on this seat's own reads of S3, IAM, EventBridge and CloudWatch.

**L9:** FWD-2 REALIZED (EXERCISED 2026-10-10, read from the run's own result versions). FWD-3 PARTIAL (marked-missing arm MET; the named-in-advance repair act NOT EXERCISED in the world -- ABSENT != EXERCISED). FWD-4 REALIZED (APPLIED; the 10-10 chain ran exactly the predicted 3 attempts). FWD-5 NOT REALIZED (held; pull 06:00Z before the 07:30 ET refresh). FWD-6 NOT REALIZED (4 pulls / 5 schedules unanswered; live denominator 164 vs census 162).
On version-history evidence: the PARTIAL run and the heal happened in production with no seat watching; S3 versions are the run's own durable output, so FWD-2 and the heal are graded EXERCISED on them. What version history cannot supply is an act that never ran: repair.py --execute.
Rows: D1-W3-S1, D1-S9, D1-S10, D1-S8, D1-S6, S11, S12 (ARMED) dismissed. D1-S7 (BLOCKING ARMED, disarmed by the HG-t-5 hold), D1-W6-S1 (ARMED, disarmed by routing), D1-S11, D1-S12, D1-W6-S2, D1-W6-S3, S1 and this seat's D1-C-S12 and D1-C-S15 graduated to `remediations/REMEDIATION_v2.md`.

```json
[
  {
    "id": "MDPF_HEALGAP-D1-C-S11",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "FWD-2 REALIZED (EXERCISED in the world on 2026-10-10, read from the run's own result). meta/2026-10-10-result.json version 8Za6CN4A (06:00:59Z) reads verdict PARTIAL, rebalancer_accounts status missing, models and model_detail arrived; versions 06:02:19Z and 06:04:21Z are the two async retries. meta/2026-10-10-complete.json has ONE version, 11:34:36Z: no stamp existed while the day was PARTIAL, so no run missing a part read as a success. The read is after the fact, but the instrument is the run's own durable output (S3 versioning), not a reconstruction: the PARTIAL run happened in production and its result object says which feed was missing for which day with nothing else consulted. Control: 2026-10-09 result one version, COMPLETE, 3 arrived.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_HEALGAP PRD v0.2 (FWD-2..FWD-6); spine L9: graded by a seat that did none of the work, on served artifacts, never self-graded.",
    "world_is": "FWD-2 REALIZED (EXERCISED in the world on 2026-10-10, read from the run's own result). meta/2026-10-10-result.json version 8Za6CN4A (06:00:59Z) reads verdict PARTIAL, rebalancer_accounts status missing, models and model_detail arrived; versions 06:02:19Z and 06:04:21Z are the two async retries. meta/2026-10-10-complete.json has ONE version, 11:34:36Z: no stamp existed while the day was PARTIAL, so no run missing a part read as a success. The read is after the fact, but the instrument is the run's own durable output (S3 versioning), not a reconstruction: the PARTIAL run happened in production and its result object says which feed was missing for which day with nothing else consulted. Control: 2026-10-09 result one version, COMPLETE, 3 arrived.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-object-versions opal-data-assets blackdiamond/cottonwood/meta/2026-10-10- (3.0.0_SA_CVO, 02:4xZ 10-11)",
        "s3api get-object --version-id 8Za6CN4AD75iciqPSTACxWVo5TOAZH2Y and 25r6whtG... (latest, COMPLETE 11:34:19Z)",
        "control meta/2026-10-09-result.json: 1 version, verdict COMPLETE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-2 REALIZED (EXERCISED in the world on 2026-10-10, read from the run's own result). meta/2026-10-10-result.json version 8Za6CN4A (06:00:59Z) reads verdict PARTIAL, rebalancer_accounts status missing, models and model_detail arrived; versions 06:02:19Z and 06:04:21Z are the two async retries. meta/2026-10-10-complete.json has ONE version, 11:34:36Z: no stamp existed while the day was PARTIAL, so no run missing a part read as a success. The read is after the fact, but the instrument is the run's own durable output (S3 versioning), not a reconstruction: the PARTIAL run happened in production and its result object says which feed was missing for which day with nothing else consulted. Control: 2026-10-09 result one version, COMPLETE, 3 arrived."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S12",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "FWD-3 PARTIAL, not REALIZED. Marked-missing arm MET: 11 objects meta/2026-08-31..09-10-missing.json (written 10-08 16:27:40-42Z), each naming feed rebalancer_model_detail and the reason (vendor serves current state only); model_detail bronze holds 0 keys on each of the 11 days against 83 (08-30), 81 (09-11), 93 (10-09). Repair-act arm NOT EXERCISED: the 10-10 hole was healed by the production 11:34Z re-attempt (FWD-1's mechanism), which announces nothing before it fetches; repair.py --execute was never run in the world (HG-t-6 AC1 stubs the runner, AC2 is a dry run). ABSENT != EXERCISED: the ACCEPT clause 'before it fetches anything, the repair says which days and which kinds of data it will fill' has no world exercise, so it cannot grade REALIZED. Graduated (REMEDIATION_v2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_HEALGAP PRD v0.2 (FWD-2..FWD-6); spine L9: graded by a seat that did none of the work, on served artifacts, never self-graded.",
    "world_is": "FWD-3 PARTIAL, not REALIZED. Marked-missing arm MET: 11 objects meta/2026-08-31..09-10-missing.json (written 10-08 16:27:40-42Z), each naming feed rebalancer_model_detail and the reason (vendor serves current state only); model_detail bronze holds 0 keys on each of the 11 days against 83 (08-30), 81 (09-11), 93 (10-09). Repair-act arm NOT EXERCISED: the 10-10 hole was healed by the production 11:34Z re-attempt (FWD-1's mechanism), which announces nothing before it fetches; repair.py --execute was never run in the world (HG-t-6 AC1 stubs the runner, AC2 is a dry run). ABSENT != EXERCISED: the ACCEPT clause 'before it fetches anything, the repair says which days and which kinds of data it will fill' has no world exercise, so it cannot grade REALIZED. Graduated (REMEDIATION_v2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-objects-v2 meta/ *missing*: 11 keys; get-object 2026-09-03-missing.json",
        "model_detail bronze key counts (client-side): 08-31..09-10 = 0 each; 08-30 83, 09-11 81, 10-09 93",
        "task-orders/MDPF_HEALGAP.TO-HG-t6:28,45-49 (stubbing, no network; AC2 dry-run); python R2_CHECKS/hg_t6_dryrun.py re-run by this seat: DRYRUN-OK",
        "R2_DRAIN_END_REPORT_DRAFT.md EXERCISE: 'The forced repair (repair.py manifest and --execute) was never run'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-3 PARTIAL, not REALIZED. Marked-missing arm MET: 11 objects meta/2026-08-31..09-10-missing.json (written 10-08 16:27:40-42Z), each naming feed rebalancer_model_detail and the reason (vendor serves current state only); model_detail bronze holds 0 keys on each of the 11 days against 83 (08-30), 81 (09-11), 93 (10-09). Repair-act arm NOT EXERCISED: the 10-10 hole was healed by the production 11:34Z re-attempt (FWD-1's mechanism), which announces nothing before it fetches; repair.py --execute was never run in the world (HG-t-6 AC1 stubs the runner, AC2 is a dry run). ABSENT != EXERCISED: the ACCEPT clause 'before it fetches anything, the repair says which days and which kinds of data it will fill' has no world exercise, so it cannot grade REALIZED. Graduated (REMEDIATION_v2)."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S13",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "FWD-4 REALIZED (APPLIED, and the world agrees). Live get-function-event-invoke-config cot-rebalancer-runner: MaximumRetryAttempts 2, MaximumEventAgeInSeconds 900 (LastModified 2026-10-08 16:12Z), matching cot_rebalancer_runner.tf:240-247 and its comment (two retries, ~1 then ~2 minutes, 900 s covers the ~180 s chain). On 2026-10-10 the failed 06:00Z pull ran exactly 3 attempts (result versions 06:00:59Z, 06:02:19Z, 06:04:21Z; CloudWatch 06Z Invocations 3, Errors 3): a settings-only reader predicts it correctly.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_HEALGAP PRD v0.2 (FWD-2..FWD-6); spine L9: graded by a seat that did none of the work, on served artifacts, never self-graded.",
    "world_is": "FWD-4 REALIZED (APPLIED, and the world agrees). Live get-function-event-invoke-config cot-rebalancer-runner: MaximumRetryAttempts 2, MaximumEventAgeInSeconds 900 (LastModified 2026-10-08 16:12Z), matching cot_rebalancer_runner.tf:240-247 and its comment (two retries, ~1 then ~2 minutes, 900 s covers the ~180 s chain). On 2026-10-10 the failed 06:00Z pull ran exactly 3 attempts (result versions 06:00:59Z, 06:02:19Z, 06:04:21Z; CloudWatch 06Z Invocations 3, Errors 3): a settings-only reader predicts it correctly.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws lambda get-function-event-invoke-config --function-name cot-rebalancer-runner (this seat)",
        "cloudwatch Invocations/Errors cot-rebalancer-runner 2026-10-10 05:55-12:00Z: 06:00 bucket 3/3, 11:30 bucket 1/0",
        "infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf:240-247"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-4 REALIZED (APPLIED, and the world agrees). Live get-function-event-invoke-config cot-rebalancer-runner: MaximumRetryAttempts 2, MaximumEventAgeInSeconds 900 (LastModified 2026-10-08 16:12Z), matching cot_rebalancer_runner.tf:240-247 and its comment (two retries, ~1 then ~2 minutes, 900 s covers the ~180 s chain). On 2026-10-10 the failed 06:00Z pull ran exactly 3 attempts (result versions 06:00:59Z, 06:02:19Z, 06:04:21Z; CloudWatch 06Z Invocations 3, Errors 3): a settings-only reader predicts it correctly."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S14",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "FWD-5 NOT REALIZED (DESIRED only). Live cot-rebalancer-runner-daily is cron(0 6 * * ? *) UTC (02:00 ET); the login refresh cot-bd-session-daily-et is cron(30 7 * * ? *) America/New_York (11:30Z summer, 12:30Z winter). The pull is scheduled BEFORE the refresh. HG-t-5 is HELD on D1-S7 and not applied; CTO ruling @6c538a0bfd section D frees it behind a round-3 12:00Z satellites fire.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_HEALGAP PRD v0.2 (FWD-2..FWD-6); spine L9: graded by a seat that did none of the work, on served artifacts, never self-graded.",
    "world_is": "FWD-5 NOT REALIZED (DESIRED only). Live cot-rebalancer-runner-daily is cron(0 6 * * ? *) UTC (02:00 ET); the login refresh cot-bd-session-daily-et is cron(30 7 * * ? *) America/New_York (11:30Z summer, 12:30Z winter). The pull is scheduled BEFORE the refresh. HG-t-5 is HELD on D1-S7 and not applied; CTO ruling @6c538a0bfd section D frees it behind a round-3 12:00Z satellites fire.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws events list-rules --name-prefix cot-: cot-rebalancer-runner-daily cron(0 6 * * ? *) ENABLED",
        "aws scheduler get-schedule cot-bd-session-daily-et: cron(30 7 * * ? *) America/New_York"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-5 NOT REALIZED (DESIRED only). Live cot-rebalancer-runner-daily is cron(0 6 * * ? *) UTC (02:00 ET); the login refresh cot-bd-session-daily-et is cron(30 7 * * ? *) America/New_York (11:30Z summer, 12:30Z winter). The pull is scheduled BEFORE the refresh. HG-t-5 is HELD on D1-S7 and not applied; CTO ruling @6c538a0bfd section D frees it behind a round-3 12:00Z satellites fire."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S15",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "FWD-6 NOT REALIZED. The census answers 23 rows truly, but 4 pulls on 5 schedules are exposed with neither answer (bd-asset-dim-pipeline-trigger, canonical-schwab-si2-08242234 and -08335338, astn-wsjft-3am-run), and ACCEPT says a pull left without an answer fails. The CTO ruling (section E) makes two of them round-3 heal cells and the two Schwab pulls a KNOWN MANUAL EXPOSURE, which is neither of FWD-6's two answers. Population: this seat's live recount reads 131 scheduled EventBridge rules + 33 Scheduler schedules = 164, against the census's 162 (10-08 sweep); the two not in the census are schwab-canonical-si2-08403355-pull-daily cron(45 10,22) (a third Schwab SDD master, SSM AWS-RunPowerShellScript sdd-daily-pull.ps1: the same exposure class as the two unanswered Schwab pulls) and teams-global-transcripts-pull-hourly cron(0 13-22 MON-FRI) (lambda teams-global-transcripts-pull-lambda, unanswered). Graduated (REMEDIATION_v2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_HEALGAP PRD v0.2 (FWD-2..FWD-6); spine L9: graded by a seat that did none of the work, on served artifacts, never self-graded.",
    "world_is": "FWD-6 NOT REALIZED. The census answers 23 rows truly, but 4 pulls on 5 schedules are exposed with neither answer (bd-asset-dim-pipeline-trigger, canonical-schwab-si2-08242234 and -08335338, astn-wsjft-3am-run), and ACCEPT says a pull left without an answer fails. The CTO ruling (section E) makes two of them round-3 heal cells and the two Schwab pulls a KNOWN MANUAL EXPOSURE, which is neither of FWD-6's two answers. Population: this seat's live recount reads 131 scheduled EventBridge rules + 33 Scheduler schedules = 164, against the census's 162 (10-08 sweep); the two not in the census are schwab-canonical-si2-08403355-pull-daily cron(45 10,22) (a third Schwab SDD master, SSM AWS-RunPowerShellScript sdd-daily-pull.ps1: the same exposure class as the two unanswered Schwab pulls) and teams-global-transcripts-pull-hourly cron(0 13-22 MON-FRI) (lambda teams-global-transcripts-pull-lambda, unanswered). Graduated (REMEDIATION_v2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "boto3 events list_rules (all pages): 154 rules, 131 with ScheduleExpression; scheduler list_schedules (all pages): 33; sum 164 (this seat, 02:4xZ 10-11)",
        "names absent from FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md: schwab-canonical-si2-08403355-pull-daily, teams-global-transcripts-pull-hourly",
        "list-targets-by-rule: AWS-RunPowerShellScript s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1; lambda teams-global-transcripts-pull-lambda",
        "python R2_CHECKS/hg_t7_census.py re-run: CENSUS-OK rows=23 denominator=162"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-6 NOT REALIZED. The census answers 23 rows truly, but 4 pulls on 5 schedules are exposed with neither answer (bd-asset-dim-pipeline-trigger, canonical-schwab-si2-08242234 and -08335338, astn-wsjft-3am-run), and ACCEPT says a pull left without an answer fails. The CTO ruling (section E) makes two of them round-3 heal cells and the two Schwab pulls a KNOWN MANUAL EXPOSURE, which is neither of FWD-6's two answers. Population: this seat's live recount reads 131 scheduled EventBridge rules + 33 Scheduler schedules = 164, against the census's 162 (10-08 sweep); the two not in the census are schwab-canonical-si2-08403355-pull-daily cron(45 10,22) (a third Schwab SDD master, SSM AWS-RunPowerShellScript sdd-daily-pull.ps1: the same exposure class as the two unanswered Schwab pulls) and teams-global-transcripts-pull-hourly cron(0 13-22 MON-FRI) (lambda teams-global-transcripts-pull-lambda, unanswered). Graduated (REMEDIATION_v2)."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S16",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "D1-W3-S1 dismissed: resolved by R2-1 / HG-t-8. The live role policy cot-rebalancer-runner-write-cot carries ReadOwnRunResult Allow s3:GetObject on opal-data-assets/blackdiamond/cottonwood/meta/*-result.json, and the 2026-10-10 latest result reads rebalancer_accounts.healed_at 2026-10-10T11:34:19Z (non-null live).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-W3-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-W3-S1 dismissed: resolved by R2-1 / HG-t-8. The live role policy cot-rebalancer-runner-write-cot carries ReadOwnRunResult Allow s3:GetObject on opal-data-assets/blackdiamond/cottonwood/meta/*-result.json, and the 2026-10-10 latest result reads rebalancer_accounts.healed_at 2026-10-10T11:34:19Z (non-null live).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws iam get-role-policy cot-rebalancer-runner-role cot-rebalancer-runner-write-cot: 4 statements incl. ReadOwnRunResult",
        "meta/2026-10-10-result.json latest version: healed_at 2026-10-10T11:34:19Z",
        "investigation row MDPF_HEALGAP-D1-W3-S1 (0.9.0_WK_MDPF_HEALGAP~3)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W3-S1 dismissed: resolved by R2-1 / HG-t-8. The live role policy cot-rebalancer-runner-write-cot carries ReadOwnRunResult Allow s3:GetObject on opal-data-assets/blackdiamond/cottonwood/meta/*-result.json, and the 2026-10-10 latest result reads rebalancer_accounts.healed_at 2026-10-10T11:34:19Z (non-null live)."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S17",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "D1-S9 dismissed: resolved. The statement landed through CTO ruling H (firm read via one(local.monolith_source_scopes.blackdiamond)) and is live (ReadOwnRunResult above); no R20 entry was needed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-S9 dismissed: resolved. The statement landed through CTO ruling H (firm read via one(local.monolith_source_scopes.blackdiamond)) and is live (ReadOwnRunResult above); no R20 entry was needed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws iam get-role-policy (live): ReadOwnRunResult present",
        "R2_DRAIN_END_REPORT_DRAFT.md R2-1: edit ba88934f7b, close 74b0ca41c8",
        "investigation row MDPF_HEALGAP-D1-S9 (0.7.0_AE_CloudOps~DELL1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S9 dismissed: resolved. The statement landed through CTO ruling H (firm read via one(local.monolith_source_scopes.blackdiamond)) and is live (ReadOwnRunResult above); no R20 entry was needed."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S18",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "D1-S10 dismissed: superseded for this order by D1-S11 (amendment A2 split C5; C5a graded from the live policy, the order complete). The standing capability gap (no iam:SimulatePrincipalPolicy on other principals from dell1) is carried by D1-S11's graduation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-S10 dismissed: superseded for this order by D1-S11 (amendment A2 split C5; C5a graded from the live policy, the order complete). The standing capability gap (no iam:SimulatePrincipalPolicy on other principals from dell1) is carried by D1-S11's graduation.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_HEALGAP-D1-S10, -D1-S11",
        "amendment A2 @37ce04cf93"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S10 dismissed: superseded for this order by D1-S11 (amendment A2 split C5; C5a graded from the live policy, the order complete). The standing capability gap (no iam:SimulatePrincipalPolicy on other principals from dell1) is carried by D1-S11's graduation."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S19",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "D1-S8 dismissed: the execution record of D1-S7 ruling (a); its served gap closed 10-08 16:07Z. The structural cause is carried by D1-S7's graduation. This seat's read: platinum/satellites/registry.json as_of 2026-10-10, written 07:00:18Z.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-S8 dismissed: the execution record of D1-S7 ruling (a); its served gap closed 10-08 16:07Z. The structural cause is carried by D1-S7's graduation. This seat's read: platinum/satellites/registry.json as_of 2026-10-10, written 07:00:18Z.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api head-object + get opal-data-cot platinum/satellites/registry.json: 2026-10-10T07:00:18Z as_of 2026-10-10",
        "ledger 20261008T1607Z_healgap-satellites-rerun-20261008 CLOSED"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S8 dismissed: the execution record of D1-S7 ruling (a); its served gap closed 10-08 16:07Z. The structural cause is carried by D1-S7's graduation. This seat's read: platinum/satellites/registry.json as_of 2026-10-10, written 07:00:18Z."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S20",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "D1-S6 dismissed: a routing (disarm) row for D1-W6-S1; the routing is done (the drain-end read names the four, the CTO ruled section E). D1-W6-S1 itself is graduated with FWD-6's residuals.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-D1-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-S6 dismissed: a routing (disarm) row for D1-W6-S1; the routing is done (the drain-end read names the four, the CTO ruled section E). D1-W6-S1 itself is graduated with FWD-6's residuals.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "R2_DRAIN_END_REPORT_DRAFT.md 'FWD-6 residuals -- RULED (section E)'",
        "investigation row MDPF_HEALGAP-D1-S6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S6 dismissed: a routing (disarm) row for D1-W6-S1; the routing is done (the drain-end read names the four, the CTO ruled section E). D1-W6-S1 itself is graduated with FWD-6's residuals."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S21",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "S11 dismissed: answered by practice. Round 2's FWD-1 reader (hg_fwd1_reader.py) reads the served platinum file after its 13:50:5xZ write, not gold at 13:30Z; this seat's head-object reads platinum/mdpf/cottonwood/aggregate-aua-timeseries.json written 2026-10-10T13:50:51Z. FWD-1 ('by the end of the same day') is not reopened.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-S11"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S11 dismissed: answered by practice. Round 2's FWD-1 reader (hg_fwd1_reader.py) reads the served platinum file after its 13:50:5xZ write, not gold at 13:30Z; this seat's head-object reads platinum/mdpf/cottonwood/aggregate-aua-timeseries.json written 2026-10-10T13:50:51Z. FWD-1 ('by the end of the same day') is not reopened.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api head-object opal-data-portal-v2 platinum/mdpf/cottonwood/aggregate-aua-timeseries.json: 2026-10-10T13:50:51Z",
        "R2_DRAIN_END_REPORT_DRAFT.md EXERCISE 13:50Z reader lines",
        "investigation row MDPF_HEALGAP-S11 (0.7.0_AE_CloudOps~F)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S11 dismissed: answered by practice. Round 2's FWD-1 reader (hg_fwd1_reader.py) reads the served platinum file after its 13:50:5xZ write, not gold at 13:30Z; this seat's head-object reads platinum/mdpf/cottonwood/aggregate-aua-timeseries.json written 2026-10-10T13:50:51Z. FWD-1 ('by the end of the same day') is not reopened."
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S22",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:45:00Z",
    "one_line": "S12 (ARMED) dismissed: disarmed on this project. No induce is outstanding on the daily target (live Input {\"mode\":\"pull\"}); the fail-safe task bv5miebw8 acted once (FAILSAFE-WOKE/ACTING 06:08:40Z 10-08) with the correct restore. The class remedy (a seat that arms a restore names every mechanism it armed) is already graduated as D1-S5 (REMEDIATION_v1, owner 2.0.0_SA_COO~G1), and act 3's restore-actor gap is graduated as D1-S12.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_HEALGAP-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S12 (ARMED) dismissed: disarmed on this project. No induce is outstanding on the daily target (live Input {\"mode\":\"pull\"}); the fail-safe task bv5miebw8 acted once (FAILSAFE-WOKE/ACTING 06:08:40Z 10-08) with the correct restore. The class remedy (a seat that arms a restore names every mechanism it armed) is already graduated as D1-S5 (REMEDIATION_v1, owner 2.0.0_SA_COO~G1), and act 3's restore-actor gap is graduated as D1-S12.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws events list-targets-by-rule cot-rebalancer-runner-daily: Input {\"mode\":\"pull\"} (this seat, 02:4xZ 10-11)",
        "REMEDIATION_v1 row MDPF_HEALGAP-D1-S5",
        "investigation row MDPF_HEALGAP-S12 (0.7.0_AE_CloudOps~F)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S12 (ARMED) dismissed: disarmed on this project. No induce is outstanding on the daily target (live Input {\"mode\":\"pull\"}); the fail-safe task bv5miebw8 acted once (FAILSAFE-WOKE/ACTING 06:08:40Z 10-08) with the correct restore. The class remedy (a seat that arms a restore names every mechanism it armed) is already graduated as D1-S5 (REMEDIATION_v1, owner 2.0.0_SA_COO~G1), and act 3's restore-actor gap is graduated as D1-S12."
  }
]
```

-- 3.0.0_SA_CVO
