# RESEARCH: host for the AMGT_HARVST daily dossier refresh (cm-6), from the estate's past pattern

**For:** `1.0.0_SA_CTO~DELL1`, msg 8177 | **By:** `4.0.0_SA_CRO~DELL1` | **Read at:** box/dell1 @bba3e258d5, 2026-10-18 ~17:4xZ

**The job:** `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round98.md` section 4 item 1. A daily trading-day job
that reads model blocks in `s3://opal-data-harvest` and rewrites 95 dossiers: about 5,700 S3 requests and 919 MB, with no
Bloomberg call. It runs on its own clock, one hour after `amgt-induction-daily`'s trigger (14:00Z on the register's 13:00Z
default). The driver is `lib/research/corpus/dossier.py`.

## 1. Recommendation

**(a) A scheduled Lambda on EventBridge Scheduler, declared in the harvest Terraform root (`infra/aws/terraform/harvest/`).**

It follows the two schedules that root already runs:

| Schedule | Target | Lambda | Cron (UTC) | Limits |
|---|---|---|---|---|
| `amgt-resapp-chatter-axis-daily` | Lambda `amgt-resapp-chatter-axis` | `chatter-axis-schedule.tf:178` | `cron(0 10 * * ? *)` | 120 s, 512 MB |
| `amgt-global-freshness-snapshot-daily` | Lambda `opal-amgt-scoped-api` | `freshness-snapshot-schedule.tf:100-110` | `cron(30 12 ? * MON-FRI *)` | -- |

**Suggested shape** (estimates; to be confirmed by the grade run):
- `cron(0 14 ? * MON-FRI *)` UTC, with the trading-day skip inside the handler (`lib/trading_calendar.py`);
- timeout 900 s; memory 1769 MB or more.

**Runner-up: (b) an ECS Fargate task on an EventBridge schedule.** It is the globgrph derive pattern, and it becomes the choice only
if the measured run of the 95-name grade nears Lambda's 15-minute cap.

## 2. The doctrine that binds the choice (quoted from `infra/logic/02_DOCTRINE.md`, line numbers printed from the file)

- **R13, lines 488-495 (compute):** "**R13 — SILVER→GOLD IS PULLED BY LAMBDA; EC2 ONLY WHERE GENUINELY HEAVY.** The threshold for
  'heavy' is **DEFERRED** by Andrew's word until the first genuinely heavy case ... authority: Andrew-direct 2026-08-25 (*'lambda pull
  from silver to gold unless its really obnoxious/heavy and needs ec2'*)." The dossier is a gold-tier rebuild, so Lambda is the
  default unless the job is heavy.
- **R16, lines 536-544 (one code home):** the pipeline's code has one home beside the gold code. Non-application: "**Lambda deployment
  artifacts** (`lambda-source-map.json` `artifact_s3_key`) -- they keep the source-map tie, R16 does not reach them." A Lambda host
  therefore adds no R16 obligation.
- **R6, lines 409-412 (harvest is general tenancy, homed in its own bucket):** "harvest, on Andrew-direct 2026-09-18 ~21:45Z ...
  *'the whole pipeline will exist within opal-data-harvest'*." The producer reads and writes inside `opal-data-harvest`, so no
  cross-bucket or firm-fence grant is needed.
- **R18, lines 556-557:** no shadow path. The scheduled refresh replaces the ad-hoc rebuild; it never runs alongside it.

From `CLAUDE.md`:
- **Line 233:** "**Ad-hoc gold runs are PERMITTED FOR QA; production pipelines MUST be scheduled** -- success-of-upstream as the only
  trigger is a defect." This matches round 98's own-clock ruling. EventBridge Scheduler is the estate's scheduling primitive.
- **Line 235:** "**NEVER write device-specific logic into ajb_workspace/portal -- DERIVE, don't hardcode** ... Legit only when
  device-ness is the code's PURPOSE." Nothing in this job needs a device.
- **Line 195, rule 30:** "**EVERY NEW PIPELINE IS BUILT TO LGIC**." The schedule, role and function names are `lib/opal_naming.py`
  `name()` output, and a builder refusal is a registry row to add.

## 3. Past cases, by host class

**Denominators:**
- `comp-find 'resource "aws_scheduler_schedule"|resource "aws_cloudwatch_event_rule"' infra/aws/terraform --all`:
  **181 hits across 101 files** (888 scanned).
- A file-level regex classification of each target, over 105 files that carry a schedule or rule. This is **inferred** from regex,
  not read target by target:

| Target class | Files |
|---|---|
| Lambda only | **82** |
| EC2/SSM plus Lambda | 10 |
| EC2/SSM only | 4 |
| ECS only | 3 |
| ECS plus Lambda | 1 |
| Other | 4 |
| SNS | 1 |

- Box scheduled tasks are not in Terraform. The census here covers the three installers in `.tools/` plus the two data producers found
  through change-management records. **It is not exhaustive.**

| Class | Case | Trigger | Limits | Why that host (where a record says) |
|---|---|---|---|---|
| **(a) Lambda** | harvest `amgt-resapp-chatter-axis` (S3 to DynamoDB, same bucket) | `cron(0 10 * * ? *)` | 120 s / 512 MB | Same root and bucket as this job. |
| (a) Lambda | harvest `opal-amgt-scoped-api` freshness snapshot | `cron(30 12 ? * MON-FRI *)` | 29 s / 1769 MB (API ceiling) | Same root. |
| (a) Lambda | `mdpf-portal-publisher` (S3 to S3 JSON publisher) | `cron(50 13 * * ? *)` | 120 s / 256 MB | The estate's standard publisher shape. |
| (a) Lambda | `etf-positioning-producer` (S3 to S3 producer) | `cron(0 13 * * ? *)` | 120 s / 512 MB | -- |
| (a) Lambda | `etfs-canon-fanin` | `cron(45 15 * * ? *)` | 120 s / 256 MB | -- |
| **(b) ECS Fargate** | `globgrph-derive-runner` (item2a) | `cron(0 2 * * ? *)` | 1 vCPU / 2 GB | `item2a.tf:343`: "account-wide describe + pyiceberg writes; **Lambda is 15-min capped**". |
| (b) ECS Fargate | `globgrph-cse-producer` | `cron(30 3 * * ? *)` | 1 vCPU / 4 GB | "derive-scale reads" (`cse_producer.tf:127`). |
| (b) ECS Fargate | `globgrph-comp-learns-producer` | `cron(0 4 * * ? *)` | 0.5 vCPU / 1 GB | Trino queries plus one S3 write. |
| **(c) Box task** | dell1 "Opal Data Harvest - Continuous Cycle" (wsj, barrons, sa news scrape) | Windows scheduled task, continuous | Box process | Publisher scraping from a pinned box worktree (cc-5 record `20261016T1536Z_harvst-cc5-runner-order...md`). Device-bound by purpose. |
| (c) Box task | site Z `amgt-induction-daily` (model blocks, Bloomberg) | Windows scheduled task, 13:00Z per the register | Bloomberg box | **Calls Bloomberg** from the terminal box (`20260930T0457Z_amgt-corpus-r22-induction-daily-register...md`, a pinned checkout on the Opal Bloomberg desktop). |
| (c) Box task | `.tools/box-sync-schedule.ps1`, `estate-capture-schedule.ps1`, `open-calls-scan-schedule.ps1` | Box scheduler | -- | Fabric tooling, not data producers. |
| **(d) EC2/SSM runner** | `consolidation-gold-runner` | EventBridge to SSM `AWS-StartEC2Instance` | EC2 | A heavy gold runner. R13 calls these "UNCLASSIFIED", not violations. |
| (d) EC2/SSM runner | `canonical-schwab-ec2` monolith pulls | EventBridge to SSM `AWS-RunPowerShellScript`, staggered daily | SI2 Windows box | Vendor (SDD) pull on Windows: "A pull is minutes". |
| (d) EC2/SSM runner | `advi-49f-publisher` dispatch | `cron(15 13 * * ? *)` to SSM | EC2 | Firm gold dispatch path. |

## 4. Fit

- **Lambda limits:** 15 min, 10 GB memory, up to 10 GB /tmp.
  - **Estimate (inferred):** about 5,700 S3 requests at an in-region latency of about 20-50 ms each is roughly 2-5 min serial, and
    under 2 min with a small thread pool. 919 MB of transfer adds tens of seconds.
  - **Memory:** processing per dossier keeps peak memory far under the cap.
  - **Measured runtime:** none exists. A census of 3,280 AMGT_HARVST files for a logged rebuild duration found 0 hits. The cm-5 grade
    run over all 95 names should print its wall time, and that number settles (a) against (b).
- **Packaging:** `lib/research/corpus/dossier.py` and its imports must build into the Lambda artifact. The harvest root already
  builds two Lambdas (`build-and-upload-*.sh`, `vendor_from_deployed.py`), so that is the existing path.
- **The existing harvest runners:**
  - **The dell1 box task** is a device-bound news scraper. Adding a non-device job to it would break the device rule (`CLAUDE.md`
    line 235) and tie the refresh to one box's uptime.
  - **Site Z's `amgt-induction-daily`** is Bloomberg-bound and on another fabric.
  - Neither is the estate already having it in the build-ladder sense for this job. The harvest root's Lambda-plus-Scheduler pattern
    is.

## 5. Why not the other two hosts

- **(c) A box task:** reserved in the estate for device-bound purposes (Bloomberg, publisher browser sessions) and for fabric
  tooling. This job has no device need, and `CLAUDE.md` line 235 forbids device logic without that purpose.
- **(d) An EC2/SSM runner:** R13 keeps EC2 for genuinely heavy work, and the threshold is deferred. This job is light by the estimate
  above.

## 6. What this research does not claim

- No live AWS state was read. The cases come from Terraform at HEAD and change records, not a live describe of each schedule.
- The class counts come from a file-level regex and are labeled inferred.
- The box census is not exhaustive.
- The runtime is estimated, not measured.
