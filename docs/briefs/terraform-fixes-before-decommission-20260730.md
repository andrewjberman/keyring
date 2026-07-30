# Terraform fixes owed BEFORE the S3/DynamoDB decommissions — consolidated brief

**Author:** `0.7.0_AE_CloudOps` · **Date:** 2026-07-30 · **Requested by:** Andrew-direct
(*"write a docs/briefs/ document about all the terraform fixes youve identified thus far across our
investigations in the s3 and DDB resources"*).
**Companion tracker (updated as the walk continues):**
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/TF_DEBT_RUNNING_LIST_20260730.md`
**Evidence base:** `KILL_LIST_20260730.md` (@`715bf4d83f`) + `SCHWAB_INGESTION_BEHAVIOR_MAP_20260730.md`
(@`c4169c6312`).

**Nothing in this brief has been applied, destroyed, or patched.** It is the fix-first ordering for
work that is authorized but not yet executed.

## Why this document exists

Every decommission in this program has turned out to be a **two-legged delete** (C-6): kill the
resource, *and* remove or repair the Terraform that declares it. The legs fail in opposite
directions, which is why the order is not cosmetic:

- **Leg 2 skipped → RESURRECTION.** A declared-but-deleted resource is recreated by the next
  `apply` of that stack. Three instances found so far, below.
- **Leg 2 done first, resource still live → OUTAGE.** Removing a declaration under a running
  producer strands it.
- **Resource killed while a writer still runs → a silent no-op becomes a daily failure.**

**The rule that falls out: fix the Terraform and stop the producers FIRST; delete the resource
LAST.** Andrew-direct, 2026-07-30: *"there needs to be a scratchpad list where thats kept on file
over the course of your session so we can strategically fix the terraforms first and then get rid of
the offending resources."*

---

## CLASS A — RESURRECTION HAZARDS (declared in TF, resource already deleted)

**These are live defects right now, independent of any decommission.** Each was verified 404/NotFound
against a separately-run positive control.

| # | Resource | Declaration | Live state |
|---|---|---|---|
| A1 | `opal-analytics-dashboard` | `infra/aws/terraform/shared-infra/s3.tf:89-97+` (bucket + versioning) | **404** |
| A2 | `opal-cloudfront-logs-313476888478` | `infra/aws/terraform/shared-infra/s3.tf:37-57` (bucket + SSE + public-access-block) | **404** |
| A3 | `opal-crawl-catalog` | `infra/aws/terraform/crawl-harness/main.tf:40-66` (bucket + PAB + versioning + SSE) | **404** |
| A4 | `orion-crawl-catalog` (DynamoDB) | already deleted; confirm no surviving declaration when A3's stack is destroyed | **NotFound** |

> 🚨 **TRAP — A1 AND A2 SANDWICH A LIVE RESOURCE.** `opal-cloudtrail-logs-313476888478` is declared at
> `shared-infra/s3.tf:63-83`, **between them**, in a near-identical block shape, and it is **LIVE**.
> A block-shaped `sed`/regex edit takes the wrong one. **Remove by resource address
> (`aws_s3_bucket.analytics_dashboard`, `aws_s3_bucket.cloudfront_logs`) and their named
> sub-resources — never by line range or block pattern.**

Each bucket carries dependent sub-resources referencing it by `.id` (SSE config, public-access-block,
versioning). **A partial removal fails the plan** — remove the whole set per bucket, in one change.

---

## CLASS B — WHOLE STACKS TO DESTROY (authorized, ordering applies)

| # | Stack | Scope | Authorization |
|---|---|---|---|
| B1 | `infra/aws/terraform/crawl-harness/` | **ENTIRE STACK** — see manifest below | **Andrew-direct 2026-07-30, verbatim: *"I dont care about any of these crawl functions, all of it can go."*** Supersedes my Recon-scope caveat; the DC-1/DC-2 TOs it referenced are among the 8 frozen orphans from dead COO seats. |
| B2 | `infra/aws/terraform/seeking-alpha/main.tf` | the Q-15 chain (7 lambdas + triggers) | Andrew ruled the news-av teardown; **Class D1 must precede it** |
| B3 | `infra/aws/terraform/smartx-v2-bucket-lifecycle/main.tf:34` | a lifecycle stack whose **entire subject is `opal-data-smartx-v2`** — it is orphaned the moment the bucket dies | Andrew-direct: delete Q-13 |

**B1 destroy manifest (enumerate before, not after):** `aws_instance.crawl` (stopped) ·
`aws_security_group.crawl` · `aws_iam_role.crawl` + policy + `aws_iam_instance_profile.crawl` + the
SSM managed-policy attachment · **4 SSM documents** (`dc1_crawl_run`, `dc2_parker_run`,
`dc2_crawl_run`, `dc2_test1_orchestrator`) · `aws_iam_role.dc2_orchestrator` + policy ·
`aws_iam_role.dc2_eventbridge_invoke` + policy · `aws_cloudwatch_event_rule.dc2_test1_offpeak`
(**applied, DISABLED, `cron(15 8)`**) + its target · `aws_s3_bucket.catalog` **(already absent —
expect a state-only removal, A3)**. Also delete the **6 stale `tfplan.*` artifacts** sitting
uncommitted in that directory (`tfplan.cat`, `.crawl`, `.ecltrim`, `.fork-c`, `.fork-c-iam`,
`.forkb`).

---

## CLASS C — CODE FIXES THAT MUST LAND BEFORE THE RESOURCE DIES

**Each of these turns silent today into a daily failure the moment its target is deleted.** Lambda
code changes deploy via Terraform only (Rule 1).

| # | Fix | Why it is blocking |
|---|---|---|
| C1 | `infra/aws/lambda/smartx_ingestion_pipeline/compute_account_distribution.py:435-444` — drop the legacy compat write to `opal-data-smartx-v2/views/account_distribution.json` | `smartx-account-distribution-daily` is **ENABLED, `cron(30 11)`**. Delete the bucket first and it fails every day. ⚠ **Do NOT touch `DISABLE_PORTAL_BELL_WRITE` (`:408-421`)** — a live CTO-ruled guard (2026-07-23) preventing this 2-firm producer from reverting the served 3-firm bell. |
| C2 | `infra/aws/lambda/news_layer3_curation/lambda_function.py:52` — `S3_BUCKET = os.environ.get('S3_BUCKET', 'opal-data-news-av')` | An **env-var DEFAULT** pointing at a doomed bucket. Inert today (deployed env = `news-v2`); a future deploy with the var unset silently targets a deleted bucket. |
| C3 | `data/canonical/schwab/build_canonical_daily.py:48, :141-146, :228` — `SRC_BUCKET = "opal-data-schwab"`, `latest_rps_date()` paginating `01_raw/`, called as the no-`--date` fallback | **Already wrong today**: silently resolves "latest" to the frozen **2026-07-15** while monolith bronze is at the T-1 frontier. After decommission it returns `""` and flows downstream. Neither shape is loud. Under the 49F-deprecation ruling this is a **delete-candidate rather than a repair-candidate** — confirm no other caller first. |

---

## CLASS D — PRODUCERS TO STOP FIRST (ordering, not fixes)

| # | Producer | State |
|---|---|---|
| D1 | `seeking-alpha-news-daily` + `seeking-alpha-analysis-daily` | **ENABLED**, driving 7 lambdas that have produced **zero articles since 2026-04-14** |
| D2 | `fred-data-ingestion` ×5 rules (`-daily` `cron(0 23)`, `-weekly`, `-monthly-early/mid/late`) + `fred-macro-ingestion-daily` `cron(30 23)` | **6 ENABLED rules across 2 functions.** The queue said "stop fred-data-ingestion first" — the real scope is six. Three are **monthly**, so this resource is invisible 27 days in 30. |
| D3 | `smartx-account-distribution-daily` `cron(30 11)` | stop **after** C1 lands |
| D4 | `dc2-test1-offpeak-harness` | applied + DISABLED; dies with B1 |

---

## CLASS E — DANGLING IAM GRANTS AFTER DELETION

Bucket deletion leaves grants naming a non-existent ARN. Not an outage, but it is exactly the
least-privilege-cleanup debt CLAUDE.md Rule 22a warns about — and a future engineer reading these
cannot tell a needed grant from a dead one.

- **`opal-data-news-av`** referenced in: `infra/aws/terraform/news-pipeline/iam.tf` ·
  `shared-infra/lambda-execution-role.tf` · `market-overview/least-privilege-secrets.tf` ·
  `opal-assets/router_iam.tf` · `seeking-alpha/main.tf`
- **`opal-data-smartx-v2`** referenced in: `shared-infra/opal-portal-lambda-role.tf` ·
  `shared-infra/iam_legacy.tf` · `opal-assets/router_iam.tf`

**`opal-data-news-av` is NOT declared as an `aws_s3_bucket` anywhere** — it is live-no-declared, so
its deletion has **no bucket TF leg**, only the stack (B2) and these grants.

---

## CLASS F — APPLIED AGAINST ITS OWN HOLD / STALE DECLARATIONS

| # | Item | Problem |
|---|---|---|
| F1 | `infra/aws/terraform/canonical-schwab-ec2/runner-trigger.tf:13-16` | Carries an explicit *"Do NOT apply until the xref bug is fixed + the sentinel emit is wired"* banner — and **is applied and ENABLED**, with **0 invocations in 30 days** and no code anywhere emitting `opal.canonical-xref`. Decide: wire the emitter, or destroy rule + box + start-path IAM together. |
| F2 | `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1:557-561` | Comment says `MonolithSchwabMetaPullsWrite` is *"authored-not-applied until CTO's gate."* **It has applied**; `meta/pulls/` manifests land daily. Stale comment on a live grant (not TF, same declarative-drift class). |

---

## RECOMMENDED EXECUTION ORDER

1. **Class A first, on its own.** Pure repair, no resource dies, immediately removes three
   resurrection hazards. Address-based removal only (mind the cloudtrail neighbour).
2. **Class C code fixes** (C1, C2) through the normal Terraform Lambda deploy cycle.
3. **Class D stops** — disable the rules; confirm by invocation metric, not by config read.
4. **Class B destroys** — `plan -destroy` reviewed against the manifest above, then
   `.tools/safe-apply.sh` (Rule 18; bare `terraform apply`/`destroy` is banned).
5. **Delete the buckets** (`opal-data-news-av`, `opal-data-smartx-v2`) — human-authorized step.
6. **Class E grant cleanup** last, once nothing references the ARNs.

**Deploy-completion discipline (CLAUDE.md):** each destroy leg opens a ledger entry in
`org/critical_paths/change_management/` at deploy-start and closes it at completion. A begun deploy
finishes in-session or rolls back and escalates — a stranded leg is RED-ALERT material.

---

## NAMED TRAPS — read before touching any of this

1. **The cloudtrail neighbour** (A1/A2) — a live bucket declared between two dead ones, same block
   shape. Remove by address, never by pattern.
2. **The `account_distribution` name collision — FOUR artifacts, TWO spellings.**
   `smartx-v2/views/account_distribution.json` (underscore, dead compat write) ·
   `portal-v2/json/portfolios/account-distribution.json` (**hyphen — THE SERVED BELL**) ·
   `portal-v2/json/portfolios/account_distribution.json` (underscore, 5,439 B, 2026-02-19, older) ·
   `gold/mdpf_revamp/{firm}/account_distribution.json` (revamp staging).
   `infra/aws/terraform/mdpf-pipeline/iam.tf:279-282` already warns in its own Sid: *"TWO LITERAL
   KEYS, NEVER A PREFIX … A prefix deny would have caught it and nobody would have noticed."*
   **Match on full bucket+key. Never the basename.**
3. **A name-filtered sweep measures the naming convention, not the estate.** I filtered on `crawl`
   and missed a declared bucket and an applied EventBridge rule in the crawl stack, because its
   resources are named `dc2-*`. **Enumerate from the declaration, then probe each declared resource
   live.** This is the general method for building every remaining second leg.
4. **`comp-iam` cannot settle these** — it models TF (DESIRED) and cannot tell landed from planned.
   Ground each on the live primitive with a separately-run positive control (Rule 22a).

---

## SCOPE OF THIS BRIEF

Covers what **I** have investigated: Q-2, Q-4, Q-7, Q-12, Q-13, Q-15, Q-16, Q-22 plus the Schwab
estate. **NOT covered — CTO's DynamoDB walk owns these:** Q-23 (`opal-sessions` decommission — table
+ `opal-session-analytics` + 4 `/analytics/*` routes + portal ingest calls) and Q-24 (Terraform ALL
globgrph resources, incl. nessie catalog tables + the ECS→DDB derive gap). They belong in the
consolidated picture; I have not measured them and make no claim about them here.

**16 of 24 queue items remain unwalked** — expect this list to grow. The tracker, not this brief, is
the running record.
