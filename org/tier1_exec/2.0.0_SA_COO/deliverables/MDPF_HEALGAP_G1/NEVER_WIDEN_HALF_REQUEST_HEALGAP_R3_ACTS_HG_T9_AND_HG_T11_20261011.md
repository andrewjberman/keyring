# Never-widen half: MDPF_HEALGAP round 3, drain acts 1 and 3 -- apply HG-t-9 (satellites producer, 13:15Z stamp-gated fire) and HG-t-11 (asset-dim re-attempt and SSM guard)

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-11 ~04:3xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Status:** COO half SIGNED for both acts; CTO half owed. Acting seat: `2.0.0_SA_COO~G1` on dell1 (R2 act 1's pattern), each act
under its own change-management entry opened before the first write and closed after the reads.
**Branch state:** the four round-3 orders are merged and LOCAL on `box/dell1` (HG-t-9 `85fe77beb7`, HG-t-11 `8e130c8c55`,
checks hardened `6be561ee23`); round-close-check round 3 reads MAY-CLOSE. HG-t-5's apply and HG-t-10's induced exercise are NOT
in this half (each takes its own pair, below).

---

## ACT 1 -- apply HG-t-9

### The act
1. `bash infra/aws/lambda/ci/build-and-upload.sh cot-pipeline cot-satellites-registry-producer` from the merged tree. A
   `BUILD_ONLY=1` build reads the sha256 first; the live and the built hashes are both printed.
2. `.tools/safe-apply.sh -chdir=infra/aws/terraform/cot-pipeline apply` with `-target` on exactly: `module.cot_satellites_registry_producer`
   (code hash, in place), `aws_iam_role_policy.cot_satellites_registry_producer_s3` (in place), `module.stamp_gated_rule_name`,
   `aws_cloudwatch_event_rule.cot_satellites_registry_producer_stamp_gated`, `aws_cloudwatch_event_target.cot_satellites_registry_producer_stamp_gated`
   and `aws_lambda_permission.events_cot_satellites_registry_producer_stamp_gated`.
   - **Condition:** the plan reads exactly: the function's code hash and the one inline policy changed in place, and three
     resources added (rule, target, permission). Any other line refuses the act.

### What changes, read from the handler's own rule (`lambda_function.py`, diff `5828c0da8b~1..85fe77beb7`)
- **Event `{}` (the 07:00Z rule, unchanged):** no S3 call; `producer.main` runs once, exactly as before. Served delta 0.
- **Event `{"require_stamp": true}` (the NEW 13:15Z rule only):** HEAD `blackdiamond/cottonwood/meta/<UTC date>-complete.json` in
  `opal-data-assets` (bucket and prefix read from the producer's own constants).
  - **Present:** `producer.main` runs once. This REWRITES `registry.json` and `holdings.json` from today's bronze: the same keys
    the 07:00Z fire writes. On a normal day the bytes are identical to 07:00Z's (same bronze, same classification table).
  - **404 / NoSuchKey / NotFound:** one log line `STAMP-ABSENT`, nothing rebuilt, nothing served.
  - **Any other error (a 403 = a missing grant):** the invoke raises. Loud, nothing rebuilt.

**Writers counted (the named property: the two served keys `platinum/satellites/registry.json` and `holdings.json` in `opal-data-cot`).**
- By GRANT: N = 1 identity holds `s3:PutObject` on each key, the role `cot-satellites-registry-producer-role` (statements
  `WriteSatellitesRegistry`, `WriteSatellitesHoldings`, read live 04:2xZ: four statements, no others).
- By TRIGGER: today 1 rule (`cot-satellites-registry-producer-daily`, `cron(0 7 * * ? *)`, input null); after the act 2 rules.
  The same function, the same code, the same two keys.
- By first-party SOURCE (`comp-find`, band SURFACED, denominator 245 hits across 80099 files, 12 first-party files): the producer
  wrapper (writer) and the readers (the POSN fetchers, `hg_r2_act1_l4.py`, the portal Positioning page). No second writer found.
  The census reads literal text only; an operator `producer.main` run with another principal is outside it and unread.

**Triggers on the keys:** none added. The new rule is a wall-clock schedule; nothing is chained to the runner's success.

### Blast radius
- **Code:** one function's code. **IAM:** one inline policy, two statements ADDED: `s3:GetObject` on
  `arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/meta/*-complete.json` and `s3:ListBucket` on
  `arn:aws:s3:::opal-data-assets` with `s3:prefix` = `blackdiamond/cottonwood/meta/` only. This is a WIDENING; it cannot list or read
  bronze or any other meta key (the check `hg_r3_rules.py --t9-iam` reads the Resource and the prefix exactly, mutants fire).
- **Keys:** the same two served keys, one extra rewrite per day. **Schedules:** one added rule.
- **Untouched:** the 07:00Z rule and its input, the runner, silver, every other role and bucket policy.

### Rollback
| what | state today (read live 2026-10-11 04:2xZ) |
|---|---|
| Lambda CodeSha256 | `eFToEJ0FNu1sMO7cJ1WNdRoGSVuNuHSM9ToBzHGkF1I=`, LastModified 2026-09-14T19:50:02Z, `Successful` |
| artifact `cot-pipeline/cot-satellites-registry-producer.zip` | version `mgzFeamx2_MIO_R.lBF6IYGUNM5aXcir`, 2026-09-14T19:15:56Z, 105484 B (versioning on) |
| inline policy `s3-read-cot-bronze-write-cot-platinum` | statements `ReadCottonwoodRebalancerBronze`, `WriteSatellitesRegistry`, `WriteSatellitesHoldings`, `ReadEtfClassifications` |
| rules on the function | one: `cot-satellites-registry-producer-daily` ENABLED |

To roll back: `terraform apply` of the same targets from `5828c0da8b~1` (removes the rule, target, permission and the two
statements) after restoring the artifact object version above; read back CodeSha256 and the rule list. A rewrite already done by the
13:15Z fire is inert (same bytes as 07:00Z on a normal day).

### Acceptance
1. Live `CodeSha256` equals the build's sha256, read from the build input. `LastUpdateStatus` `Successful`.
2. `list-rules` shows two rules on the function; the new one `cron(15 13 * * ? *)` ENABLED with input `{"require_stamp":true}`.
3. The policy reads the two new statements and no others changed (statement `Sid` list, Resource and prefix read back).
4. **The first 13:15Z fire after the apply:** one invocation, `registry.json` as_of today, LastModified at or after 13:15Z OR the
   log line `STAMP-ABSENT` on a day with no stamp. The negative arm (a day the runner lands after 07:00Z) is read on the first
   such day, or on an induced late landing under HG-t-5's pair.

---

## ACT 3 -- apply HG-t-11

### The act (ORDER MATTERS: the guard lands before the re-attempt exists)
1. **The document.** Publish `infra/aws/ssm/opal-bd-asset-dim-download.json` (merged, `8e130c8c55`) as a new version of the SSM
   document `opal-bd-asset-dim-download` and set it DEFAULT, from the repo file byte-equal to the merged blob (the NFRA_MCPINDEX
   MX-s-12 pattern). **If the acting principal is denied `ssm:UpdateDocument`, the act STOPS here with nothing changed** and the
   rule is not applied (the grant is UNREAD: `ssm:ListDocumentVersions` read AccessDenied for `cloudops-dell1-agent-user` at 04:2xZ).
2. **The rule.** `.tools/safe-apply.sh -chdir=infra/aws/terraform/bd-pipeline apply` with `-target` on exactly:
   `module.asset_dim_reattempt_rule_name`, `aws_cloudwatch_event_rule.bd_asset_dim_reattempt`,
   `aws_cloudwatch_event_target.bd_asset_dim_reattempt_target`, `aws_lambda_permission.eventbridge_asset_dim_reattempt`.
   - **Condition:** the plan reads 3 added resources and nothing else; any other line (the file has pre-existing formatting
     drift on two NFRA_MCPINDEX rules, unrelated) refuses the act.

### What changes
- The document's shell gains a guard BEFORE the as-of resolution and the pull: a staged `hg_guard.py` HEADs today's UTC bronze
  partition `<key_prefix>/<date>/<object>` in the pin's bucket, as `ec2-user`. Exit 0 -> logs `SKIP-COMPLETE`, uploads the log,
  ARMS the shutdown, `exit 0` (the pull is not started). Any non-zero exit (a missing key, a 403, an import error) -> the
  document continues unchanged into the pull. The 22:10Z fire, on a day whose bronze did not land, behaves as before.
- A second weekday fire at 22:40Z on the SAME trigger. After the 22:10Z fire's success the re-attempt starts the instance, the guard
  skips, the instance shuts down in 2 minutes. After a 22:10Z failure on a lapsed session (the mint is 22:20Z) the 22:40Z fire
  re-runs the pull on the fresh session: this is FWD-6's recovery.
- **The guard's key is today's bronze partition, not `silver/assets/<D>.parquet`** (ruling 3411 named the Playwright-era
  artifact; the REST path does not write it). Accepted residual: bronze present with a failed dim rebuild reads "complete" until
  the next day's run.

**Writers counted.** Bronze `assets_dim_rest/<date>/assets_dim_rest.parquet`: N = 1 writer, `pull_bd_asset_dim_rest.py` run by this
document (the one document; the trigger Lambda is its only caller). The guard writes nothing. Silver `bd_assets_dim.parquet`:
unchanged (the same builder, only when the pull ran).
**Vendor / firm-bucket events:** the 22:40Z re-attempt on a failed day makes one REST pull (a vendor read) and writes the firm
bucket exactly as the 22:10Z fire does. No send is made by this act or by the worker. CloudOps msg-1814 conditions apply
verbatim; the laptop is told FIRST of any send that writes a firm data bucket; 49 Financial data never enters another firm's tree.

### Blast radius
- **Document:** one SSM document, one new version set DEFAULT. **Schedules:** one added weekday rule. **Compute:** one more
  instance start and stop per weekday (a cost, no new vendor act on a complete day).
- **Untouched:** the trigger Lambda, the shared `bd_daily_trigger` role (no grant added), every other rule and document.

### Rollback
| what | state today (read live 2026-10-11 04:2xZ) |
|---|---|
| SSM `opal-bd-asset-dim-download` | DefaultVersion 5, LatestVersion 5, Hash `d3a38c7b1a92b3d92030c241ab6502245c5a25d3b40930dcef67548943d3f407`, created 2026-10-01T02:14:59-04:00, Active |
| rules on `bd-asset-dim-trigger` | one: `bd-asset-dim-pipeline-trigger` `cron(10 22 ? * MON-FRI *)` ENABLED |

To roll back: `update-document-default-version` to 5 (version 5 is never deleted by publishing 6), then `terraform apply` of the
same four targets from the pre-merge commit (or `destroy -target` of the three resources). Read back DefaultVersion and the rule list.

### Acceptance
1. `describe-document` DefaultVersion = the new version; its content equals the repo file as parsed JSON and carries `hg_guard.py`.
2. `list-rules` on the trigger shows two rules; the new one `cron(40 22 ? * MON-FRI *)` ENABLED.
3. **The first weekday fire pair (Monday 22:10Z and 22:40Z):** the 22:10Z fire runs as before and the day's bronze lands; the 22:40Z
   fire logs `SKIP-COMPLETE` in `logs/asset-dim-download-<date>.log`, starts no pull, and the instance reaches `stopped`.
   Negative arm: the first day the 22:10Z fire fails on a lapsed session, the 22:40Z fire runs the pull and the bronze lands.

---

## What this half does NOT carry
- HG-t-5's apply (the runner's fire time to `cron(45 12 * * ? *)`): its own pair, after ACT 1 and one 13:15Z fire is read.
- HG-t-10 (the induced FWD-3 exercise): its own pair, with the D1-S12 condition (a restore actor on a different device).
