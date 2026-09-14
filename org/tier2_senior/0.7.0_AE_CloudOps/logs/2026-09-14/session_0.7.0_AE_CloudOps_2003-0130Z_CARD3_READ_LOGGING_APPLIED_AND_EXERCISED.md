# Session -- 0.7.0_AE_CloudOps -- 2026-09-13 20:03Z to 2026-09-14 ~01:40Z -- card3-read-logging applied and exercised

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Seat:** `0.7.0_AE_CloudOps` (base), seated by `0.0.0_AB_MSTR` on Andrew-direct ~19:0xZ "yes to both", scope card 3 only.
**Order:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/card3-read-logging-cot-org-trail-to-terraform-firmsep-drop-cot.md`,
issuer `2.0.0_SA_COO~E`; issued @`4db66568a6`, GO on its face @`6967266949`, S5 amended @`9674549204`, routed (a) @`56941e3366`.

## Summary

Card 3 is live. The organisation trail `opal-organization-trail` is under Terraform (shared-infra, imported at 0-diff).
Its ReadOnly S3 data selector now records reads on `opal-data-cot` and `opal-data-49financial` as well as bd and inf.
`FIRMSEP-s3-direct-access-bypass` lost `opal-data-cot` in the same change and was applied FIRST, so the rule never saw
a cot data event. The firm-bucket template `s3-49financial.tf` carries a plan-time postcondition, so a bucket minted by
copying it is born inside the selector. Recording was OBSERVED on both new buckets; the per-bucket clock report is below.

## What happened, in order

1. **Startup (20:03Z):** /watcher (registered; Monitor `ba7h16tog` running), org/XXX.md, /cloud-ops. One unread
   message from before the session (96299) opened and acked.
2. **Pre-order read (~20:1x-20:2xZ), sent to `1.0.0_SA_CTO` as 96399:** measured the org trail's selectors (bd/inf
   only, cot none) and that the trail was not in Terraform. FLAG A: `FIRMSEP-s3-direct-access-bypass` is an ENABLED
   second consumer of cot data events (SNS `opal-infrastructure-alerts`, one SMS subscriber; every invocation failing
   over 14 days, so it sends nothing only because two legs are broken in series). FLAG B: five stale base orders.
   Andrew ruled remedy (a) at ~21:3xZ (drop cot from the rule in the same change) and seated `2.0.0_SA_COO~E` for the order.
3. **Phase 1 (~23:02Z):** all three checks at expect. Baseline plans: shared-infra PLAN_RC=0 after an offline
   `terraform init -plugin-dir` (no registry download); portal-auth PLAN_RC=2 on one unrelated WAF update.
4. **HOLD (row ADVI_FIRMBKTS-S1 @`926e18a2ce`):** the portal-auth WAF diff made Phase 2 step 1 unmeetable as written.
   Routed (a) by the issuer @`56941e3366`: targeted portal-auth apply, R-AC12 re-cut, R-AC16 added.
5. **S0/S1/S2:** ledger opened 23:26:28Z; pre-state captured 23:26:46Z; trail imported 23:37:27-35Z, R-AC2 PLAN_RC=0
   23:37:47Z; commit `9f3fd2cf4a`.
6. **S3 pre-verified in scratch copies (plan only, -lock=false, shared TF_DATA_DIR):** the exact S3 bytes planned
   1 in-place update (the trail's values); mutants A, B and B2 exercised the template postcondition (see Compiler Tools).
7. **S3 (commit `37931439cf`), both applies from SAVED plans through safe-apply:** T0 reads 00:37:31Z; portal-auth
   (targeted) 00:37:41Z-00:39:22Z; trail 00:45:02Z-00:46:26Z; T1 reads 00:46:33Z/00:46:41Z; post-captures 00:46:54Z
   and 00:48:46Z.
8. **Exercise:** the T1 reads were never recorded (row ADVI_FIRMBKTS-S5); recording was observed on cot at 01:02:35Z
   (organic) and confirmed on 49financial by a second probe round (T1b, 01:11Z). R-AC8's organic positive control was
   empty and passed only on a driven bd read (row ADVI_FIRMBKTS-S4).
9. **Ledger closed** 01:29Z, 5 of 5 legs proven; R-AC14 `SENTINEL ABSENT ENTRIES 1 CLOSED`.

## Deployment Sequence + Verification (AE)

| step | act | time (UTC) | result |
|---|---|---|---|
| S0 | `deploy_ledger.py open --slug card3-read-logging` (5 legs, 24h window) | 2026-09-13 23:26:28Z | OPEN |
| S1 | selectors/trail/rule/targets `_pre.json` | 23:26:46Z | 4 files, parse OK; re-diffed UNCHANGED vs live before S3 |
| S2 | `terraform import aws_cloudtrail.organization <arn>` | 23:37:27Z-23:37:35Z | rc=0; R-AC2 PLAN_RC=0 23:37:47Z |
| S3a | `safe-apply -chdir=infra/aws/terraform/portal-auth apply -input=false <pa_rule.tfplan>` (plan made with `-target=aws_cloudwatch_event_rule.firmsep_s3_bypass`) | 2026-09-14 00:37:41Z-00:39:22Z | rc=0; 0 added 1 changed 0 destroyed; PutRule eventTime 00:39:23Z |
| S3b | `safe-apply -chdir=infra/aws/terraform/shared-infra apply -input=false <si_trail.tfplan>` | 00:45:02Z-00:46:26Z | rc=0; comp-tagauthz PASSED; 0 added 1 changed 0 destroyed; PutEventSelectors eventTime 00:46:28Z |
| S4 | T0 reads (bd, cot); T1 reads (cot, 49financial); T1b reads (cot, 49financial) | 00:37:31Z / 00:46:33Z / 01:11:18Z | see S5 report |
| S6 | ledger L3, L2, L4, L5, L1 closed; `close` | 01:29Z | CLOSED 5/5 |

Both applies used a SAVED plan, so what landed is exactly what was reviewed. Post-apply: R-AC12 PLAN_RC=0 (targeted
portal-auth), R-AC13 PLAN_RC=0 (shared-infra), R-AC16 = only the pre-existing WAF update.

## S5 -- CLOCK START REPORT (per bucket; stamps nothing)

`1.0.0_SA_CTO`'s ruling (96424 @`34ca8cab31`): "LIVE MEANS OBSERVED RECORDING, NOT APPLIED CONFIGURATION."

**opal-data-cot**
- (i) trail apply completed 2026-09-14T00:46:26Z; PutEventSelectors eventTime 00:46:28Z (context only).
- (ii) first observed data event: eventTime **2026-09-14T01:02:35Z**, userIdentity.arn
  `arn:aws:sts::313476888478:assumed-role/opal-cot-value-parity/opal-cot-value-parity`, key platinum/firm/header_metrics.json
  -- **ORGANIC** (a Lambda). It starts the clock and stays in the census.
- (iii) every probe read, principal `arn:aws:iam::313476888478:user/Andrew_Berman` (aws-cli, 1-byte ranged GetObject):
  T0 started 00:37:37Z -- NO record (cot not yet logged; R-AC9 n=0). T1 started 00:46:33Z -- NO record (before recording
  began; row S5). T1b started 01:11:18Z -- recorded at eventTime **01:11:30Z**.

**opal-data-49financial**
- (i) same apply as above.
- (ii) first observed data event: eventTime **2026-09-14T01:11:38Z**, userIdentity.arn
  `arn:aws:iam::313476888478:user/Andrew_Berman`, key _code/POLICY_BLOCK.json -- **the T1b PROBE** (to be excluded from
  the census). No organic read observed through 01:24:49Z.
- (iii) probes, same principal: T1 started 00:46:41Z -- NO record. T1b started 01:11:28Z -- recorded at eventTime **01:11:38Z**.

**Also a probe, on a bucket outside card 3's two:** opal-data-bd, T0, started 00:37:31Z, recorded at eventTime
**00:37:39Z** (R-AC8's driven positive control; row S4). bd sits under the same 45-day census.

## Compiler Tools

Every `<run>` in the order's compiler_tools_mandate, with its observed output and pass/fail against its `<expect>`:

| phase | `<run>` | observed | vs `<expect>` |
|---|---|---|---|
| 1 | `comp-blast FIRMSEP-s3-direct-access-bypass` | `SNS_TOPIC (1): opal-infrastructure-alerts`; graph vintage 2026-09-13 12:15:54Z, 27,981 nodes | PASS (exactly 1 downstream node, that topic) |
| 1 | `aws cloudtrail describe-trails --trail-name-list opal-organization-trail` | 1 trail; IsMultiRegionTrail true; IsOrganizationTrail false; HomeRegion us-east-1; S3BucketName opal-cloudtrail-logs-313476888478; 0 tags (list-tags) | PASS; recorded in the ledger title |
| 1 | R-AC1's invocation | `arn:aws:s3:::opal-data-bd/ arn:aws:s3:::opal-data-inf/` at 23:01:59Z | PASS (exactly bd/ and inf/) |
| 2 | `.tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply -target=aws_cloudwatch_event_rule.firmsep_s3_bypass` (its plan, read before approving) | saved plan 00:27:27Z: PLAN_RC=2, `# aws_cloudwatch_event_rule.firmsep_s3_bypass will be updated in-place`, bucketName `- "opal-data-cot"` only, `Plan: 0 to add, 1 to change, 0 to destroy.` Applied as the saved plan through safe-apply | PASS (routed form). The ORIGINAL untargeted expect FAILED on the WAF drift and was HELD (row S1) before any edit |
| 2 | safe-apply's plan for the trail module after the S3 edit | saved plan 00:30:15Z: PLAN_RC=2, `# aws_cloudtrail.organization will be updated in-place`, values `+ opal-data-49financial/`, `+ opal-data-cot/`, `Plan: 0 to add, 1 to change, 0 to destroy.`, no `forces replacement` | PASS (the S3(c) mechanism adds no resource) |
| 2 | `comp-iam gaps` | `Total: 17 missing / 292 deny-present / 1 coverage-unknown / 2 resource-mismatch across 33 service(s)` -- all on roles and resources this order does not touch (the 2 mismatches: etfs-reports-reporter, opal-assets-mdpf-portal-publisher) | PASS (DECLARED-NOT-APPLICABLE: no iam.tf touched; no new gap attributable) |
| 3 | R-AC3 | `"bucketName":["opal-data-bd","opal-data-inf"]` 00:48:51Z | PASS |
| 3 | R-AC4 | `RULE_UNCHANGED_EXCEPT_BUCKETS=true` | PASS |
| 3 | R-AC5 | `ORDER putrule=2026-09-14T00:39:23Z puteventselectors=2026-09-14T00:46:28Z rule_first=true` | PASS |
| 3 | R-AC6 | `arn:aws:s3:::opal-data-49financial/ arn:aws:s3:::opal-data-bd/ arn:aws:s3:::opal-data-cot/ arn:aws:s3:::opal-data-inf/` | PASS |
| 3 | R-AC7 | `TRAIL_UNCHANGED_EXCEPT_READ_VALUES=true` | PASS |
| 3 | R-AC8 | `DATA_EVENTS bucket=opal-data-bd n=1 first=2026-09-14T00:37:39Z` (29 files, 3,770 records) | PASS -- on the driven read only (row S4) |
| 3 | R-AC9 | `DATA_EVENTS bucket=opal-data-cot n=0 first=none` (30 files, 3,830 records) | PASS |
| 3 | R-AC10 | `DATA_EVENTS bucket=opal-data-cot n=3 first=2026-09-14T01:02:35Z` | PASS |
| 3 | R-AC11 | `DATA_EVENTS bucket=opal-data-49financial n=1 first=2026-09-14T01:11:38Z` | PASS -- on the T1b probe (row S5) |
| 3 | R-AC12 | targeted plan `PLAN_RC=0`, `No changes.` (00:50:50Z) | PASS |
| 3 | R-AC13 | shared-infra `PLAN_RC=0`, `No changes.` (01:00:35Z) | PASS |
| 3 | R-AC14 | `SENTINEL ABSENT ENTRIES 1 CLOSED` (01:29:44Z) | PASS |
| 3 | R-AC16 | `  # aws_wafv2_web_acl.opal_cloudfront_protection will be updated in-place|` | PASS |

Other instruments this session:

| tool | invocation | result | note |
|---|---|---|---|
| `card3_probe.py` | authored and committed @`9f3fd2cf4a`; `same-rule`/`same-trail` pre-vs-pre | true / true; a State-flipped mutant -> false | commit-gate clean (py_compile, ds-precommit, ruff py39) |
| `card3_probe.py events` | positive check against an independent instrument: 23:15-23:20Z | opal-data-inf n=2 == FIRMSEP MatchedEvents 2 for that 5-minute period | the scanner is not blind; bd's 0 was real |
| scratch-copy `terraform plan` | shared-infra + `../modules` copied to the scratchpad, `TF_DATA_DIR` = the real `.terraform`, `-lock=false` | mutant A (49financial off the list) -> `Resource postcondition failed` naming the list; mutant B (a copier mints opal-data-card3-mutant-zz) -> same failure on the new bucket; B2 (copier adds the name) -> `5 to add, 1 to change, 0 to destroy` | the first attempt failed `Module not installed` -- the module loads `../modules/yang-lambda` |
| `terraform init -plugin-dir` | shared-infra, providers from portal-auth's installed hashicorp/aws 5.100.0 | rc=0; lock hashes matched; no registry download | shared-infra had no `.terraform` on this device |
| `deploy_ledger.py` | open; close-leg L3, L2, L4, L5, L1; close | CLOSED 5/5 | the notes section appended after L3 did NOT survive: close-leg/close regenerate the entry, and a post-close read found 0 matches. Restated after the close, carried through S3 and the S3(c) mechanism |
| EventBridge / SNS CloudWatch metrics | FIRMSEP MatchedEvents/Invocations/FailedInvocations 14d; topic Published/Delivered/Failed | FailedInvocations == Invocations 14 of 14 days; topic 17 published / 17 failed / 0 delivered | the FLAG A evidence |
| `proof-of-spec-check` | `python .tools/proof-of-spec-check.py <instance> "R-AC1,...,R-AC16"` | first pass INVALID rc=1, 8 violations, all instance-shape: 4 `introduces` carried descriptions instead of literal tokens; 4 `_post` captures cited by sha256 instead of a commit. Second pass `VALID (rc=0)`: 16 rows, 0 violations, 9 of 9 artifacts CONTENT-resolved at their pins | the governing-TO frames are announce-only: the checker resolves no TO for this order's `<id>` across 2,614 files, so alignment, invocation and count-bar limbs report NOT EVALUATED, not PASS |

**What worked:** saved-plan applies (reviewed == applied); pre-verifying S3 in scratch copies so the shared tree held
uncommitted S3 edits for minutes, not hours; driving every event the criteria needed instead of waiting on organic traffic.

**What failed / gaps:**
- The comp-tool rail aborted a whole Bash call twice: once for a grep over a file in the scratchpad (not repo corpus),
  so the first S3 scratch plan never ran; once for a directory grep. Both re-run in rail-legal form.
- `.tools/record-terraform-deploy.sh`, named by the /cloud-ops skill as pre-approved tooling, does not exist at that
  path; a repo-wide Glob timed out. CHANGELOG.json for portal-auth and shared-infra was therefore NOT updated.
- Rule 6 tags (`shared-infra-v1.47.0`, `portal-auth-v1.24.0`) NOT created: portal-auth is not at 0-diff (the WAF
  update), and pushing tags is `0.0.0_AB_MSTR`'s act. Left to the integrator.
- The order's instance path `CARD3_READ_LOGGING_PROOF_OF_SPEC.json` does not match the investigation schema's
  `grades.instance` pattern (`\.proof_of_spec\.json@<commit>`), which a row grading R-AC15 must satisfy. The instance
  is written at the order's path; flagged to the issuer.

**AE role minimums:** `comp-blast` before the infra change -- done. `comp-iam gaps` -- run (no iam.tf change).
`comp-pipescript deployed` / `postdeps` -- not applicable (no gold run).

## Blockers

None on this order. Outstanding items that are not this seat's:
- Row ADVI_FIRMBKTS-S1: the pre-existing portal-auth WAF update (`aws_wafv2_web_acl.opal_cloudfront_protection`); its owner's.
- Row ADVI_FIRMBKTS-S2 (ARMED, `0.0.0_AB_MSTR`) and -S3 (3.0.0_SA_CVO's re-measure): the import's exposure in 22 older
  linked worktrees, and SITEZ until the CLOUD->SITEZ merge.
- R-AC15 (judgment) is graded by `2.0.0_SA_COO~E`.

## Current State (for a reader with zero context)

- **Live:** `opal-organization-trail` ReadOnly S3 data selector = opal-data-49financial/, opal-data-bd/, opal-data-cot/,
  opal-data-inf/. `FIRMSEP-s3-direct-access-bypass` bucketName = [opal-data-bd, opal-data-inf], still ENABLED, still
  targeting SNS opal-infrastructure-alerts (its future is not ruled).
- **Terraform:** `infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf` (aws_cloudtrail.organization, provider
  alias `aws.untagged`, prevent_destroy, `local.org_trail_read_logged_buckets`); `shared-infra/s3-49financial.tf`
  postcondition; `portal-auth/cloudwatch-alarms.tf` rule. Both stacks re-plan clean except portal-auth's pre-existing WAF update.
- **Deliverables:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/CARD3_READ_LOGGING/` -- card3_probe.py, the four
  `_pre.json` and four `_post.json` captures, the proof-of-spec instance.
- **Ledger:** `org/critical_paths/change_management/20260913T2326Z_card3-read-logging_deploy_completion.md`, CLOSED.
- **Commits:** `926e18a2ce`, `9f3fd2cf4a`, `37931439cf` -- ON ORIGIN (origin/CLOUD `37931439cf`, git ls-remote
  2026-09-14T01:20:00Z). The closing commit carrying this log is LOCAL until the next push window.

## Next Steps

1. **[2.0.0_SA_COO~E]** RAVC-4 on the completion report; grade R-AC15 against the mechanism in the ledger and in
   commit `37931439cf`; relay the S5 report to `1.0.0_SA_CTO`.
2. **[1.0.0_SA_CTO]** Stamp the FWD-6 clock from the S5 report (cot first observed 01:02:35Z organic; 49financial first
   observed 01:11:38Z, a probe).
3. **[0.0.0_AB_MSTR]** The next CLOUD push carries the closing commit; tags and CHANGELOG are open (above).
4. **[this seat]** Idle on card 3 after RAVC-4, unless the issuer returns REWORK.
