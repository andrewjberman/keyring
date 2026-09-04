# TO NFRA_OPSEC202609.TO-OP-S-5 -- THE WATCHING STARTS WITH A RECORD: WAF logging on both ACLs, CloudFront access logs, ALB access logs -- all OFF today, all ON and retrievable a week later after this cell

<to_id>NFRA_OPSEC202609.TO-OP-S-5</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` v0.4 @43b75ffbd6 (ENDPOINT FWD-5, property 4; s.5 the moratorium exception FWD-5 by the commissioning word; 7.3 the `waf-logs/{scope}/` prefix; 7.6 C-8) - **Decomp cell:** `OP-s-5` (v0.1 @bff1f8d012, s.1a; ROUND 1; "the input for OP-s-6, OP-s-20, OP-s-23 and OP-s-14's subscription filter") - **Lane:** `infra/aws/terraform/portal-auth/waf-cloudfront.tf` + `cloudfront-distribution.tf` (imported; 0-diff bound), the gateway ALB / regional WAF Terraform under `infra/aws/ec2/opal-gateway/**`, and the NEW module OP-s-17 creates (the S3 legs' destination) - **Round:** 1 of NFRA_OPSEC202609, SECOND on this seat after TO-OP-S-3.

---

## THE CELL -- what the brief measured and what this cell changes

Brief F3 :88-111 (APPLIED 2026-09-02): WAF logging on the CloudFront ACL NOT configured (3-hour sampled requests only); CloudFront access logging OFF; ALB `opal-gateway` access logging OFF; CloudTrail multi-region ON is the one durable audit source. So a blocked attacker is invisible after three hours, and nothing downstream of the front door can be measured: the login-abuse alarm (OP-s-6) has no log to filter, the partner-egress ALLOW census (OP-s-20, C-4) has no addresses to count (the auth handler is IP-blind, brief F4), the WATCH month (OP-s-23, C-3) cannot start, and the sentinel's subscription filter (OP-s-14) has no source. **This cell is the input to four others and is exercised by nothing but time: ordinary production traffic writes the records.**

FWD-5 is a named moratorium exception (the commissioning word). **This cell builds LOGGING ONLY: no alarm, no metric filter, no subscription filter, no notification** -- those are OP-s-6's (one alarm pair, one named human) and OP-s-14's (the sentinel), each its own cell with its own authorization.

## DELIVERABLE -- four logging legs, one retention bar, nothing that alerts

1. **WAF logging on BOTH ACLs to CloudWatch Logs:** `opal-cloudfront-protection` (CLOUDFRONT scope) -> log group `aws-waf-logs-opal-cloudfront`; `opal-gateway-waf` (REGIONAL) -> `aws-waf-logs-opal-gateway` (the `aws-waf-logs-` prefix is AWS's requirement). Retention 400 days on both groups (mirrors C-8's `waf-logs/` expiry so the two carriers agree). Redact the `authorization` and `cookie` request-header VALUES in the logging configuration (issuer's decision for round 1: the log is evidence of requests, not a credential store; state it on the Terraform comment). No sampling filter beyond AWS's default (every request the ACL evaluates is logged).
2. **CloudFront standard access logs** for `EVTSA9VEHNZVH` into `opal-data-security` under `waf-logs/cloudfront-access/` (a `{scope}` under 7.3's `waf-logs/{scope}/` grammar; the C-8 lifecycle -- Glacier 90 d, expire 400 d -- applies by prefix). If legacy standard logging requires ACL-enabled object ownership on the bucket (the known S3 gotcha), use CloudFront standard logging v2 (a CloudWatch delivery source/destination to S3) so the bucket's ownership setting is NOT changed -- state which path was taken and why.
3. **ALB access logs** for `opal-gateway` into `opal-data-security` under `waf-logs/alb-opal-gateway/`. The ALB log-delivery service principal is added to the bucket policy's allow-list for `s3:PutObject` on that prefix ONLY (a service principal that exists; OP-s-17's policy comment anticipates extensions).
4. **The retention bar, measured on every destination:** FWD-5 ACCEPT is "a week after something was blocked, someone can still list which addresses were blocked and what they were asking for" -- so retention >= 7 d is the BAR on all four legs; the configured values (400 d) are the settings.
5. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-5.waf-cloudfront-alb-logging.proof_of_spec.json`, VALID before the complete flip.
6. **A deploy-ledger entry** for the apply (`safe-apply`; the distribution is imported -- 0-diff before the change is added, `cloudfront-distribution.tf:5`).

**Sequencing on this seat:** legs 2 and 3 need `opal-data-security` to exist (TO-OP-S-17-16 at `0.7.0_AE_CloudOps~S`). Do leg 1 first; if the bucket is not yet APPLIED when you reach legs 2-3, read the other seat's ledger entry (never a message) and wait on the artifact, not on a report.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the instance

<criterion id="S5-AC1" cell_refs="OP-s-5"/> `S5-AC1` -- WAF LOGGING ON BOTH ACLs AT APPLIED: `aws wafv2 get-logging-configuration --resource-arn <acl>` for BOTH ACLs (denominator 2 of 2) returns the CloudWatch Logs destination and the two redacted header fields; the log groups exist with retention 400 d (`describe-log-groups`).
<criterion id="S5-AC2" cell_refs="OP-s-5"/> `S5-AC2` -- RECORDS ARRIVE WITHOUT A PROBE: within one hour of the apply each group holds >= 1 stream with >= 1 event (`describe-log-streams` + `get-log-events`, one event quoted with its `action` field; production traffic is the writer, no request is sent by this seat) -- for the CloudFront ACL this is near-certain; for the regional ACL state the count read and, if 0 after an hour, say so (an empty gateway hour is a fact, not a failure).
<criterion id="S5-AC3" cell_refs="OP-s-5"/> `S5-AC3` -- CLOUDFRONT ACCESS LOGS ON, OBJECTS PRESENT: `get-distribution-config` (or the v2 delivery source/destination reads) shows logging ON to the stated destination; within the delivery window (up to an hour for standard logs) >= 1 object exists under `waf-logs/cloudfront-access/` (`list-objects-v2` with the count and the newest key). The bucket's object-ownership setting is UNCHANGED from OP-s-17's (read before/after).
<criterion id="S5-AC4" cell_refs="OP-s-5"/> `S5-AC4` -- ALB ACCESS LOGS ON, OBJECTS PRESENT: `describe-load-balancer-attributes` shows `access_logs.s3.enabled=true` with the bucket + prefix; the bucket policy carries the log-delivery principal on that prefix ONLY (`get-bucket-policy` quoted); >= 1 object under `waf-logs/alb-opal-gateway/` within the 5-minute delivery window, or the count read and stated.
<criterion id="S5-AC5" cell_refs="OP-s-5"/> `S5-AC5` -- RETENTION >= 7 DAYS ON EVERY DESTINATION: the two log groups' `retentionInDays` (400) and the bucket's lifecycle rule on `waf-logs/` (Glacier 90 d, expire 400 d, read from `get-bucket-lifecycle-configuration`) -- four destinations, denominator 4 of 4, each >= 7 d.
<criterion id="S5-AC6" cell_refs="OP-s-5"/> `S5-AC6` -- NOTHING ALERTS: the diff creates no `aws_cloudwatch_metric_alarm`, no `aws_cloudwatch_log_metric_filter`, no `aws_cloudwatch_log_subscription_filter`, no SNS/SES resource (a census of the commit's diff for those resource types, count 0 with the denominator of resources added printed). FWD-5's exception is logging; the rest is other cells'.
<criterion id="S5-AC7" cell_refs="OP-s-5"/> `S5-AC7` -- 0-DIFF, LEDGER CLOSED, PUSH STATE MEASURED: the re-plan reads 0-diff on every module touched; the deploy-ledger entry CLOSED with its proof; push state read by ls-remote + is-ancestor (LOCAL expected).

<expected_criteria>S5-AC1, S5-AC2, S5-AC3, S5-AC4, S5-AC5, S5-AC6, S5-AC7</expected_criteria>

## SURFACES (the brief's reads at @32daebf403; RE-GROUND AT YOUR OWN VINTAGE FIRST)

`infra/aws/terraform/portal-auth/waf-cloudfront.tf` (the CloudFront ACL, full IaC since 2026-07-08) - `portal-auth/cloudfront-distribution.tf` (imported; `:5` 0-diff bound; the logging block lands here) - the gateway's ALB + regional ACL Terraform under `infra/aws/ec2/opal-gateway/**` (locate: `comp-find 'opal-gateway-waf|opal-gateway' --files infra/aws/ec2 infra/aws/terraform`) - OP-s-17's new module (the bucket policy you extend) - brief F3 :88-111, WS2 gateway :199-217 (ALB access logs OFF, finding (b)).

## BOUNDS

- **Logging ONLY.** No alarm, filter, subscription, notification, dashboard or GuardDuty/Security Hub/Config enablement (PRD s.5; the standing moratorium; S5-AC6 is the control).
- **The imported distribution: 0-diff first, `safe-apply`, ledger open** (`cloudfront-distribution.tf:5`); the cache-key params untouched (`cloudfront.tf:16`).
- **The bucket's ownership/ACL setting is not changed** to satisfy legacy CloudFront logging -- use the v2 delivery path instead; the bucket policy gains ONE service principal on ONE prefix.
- **Retention values are settings; >= 7 d is the bar.** No shorter retention anywhere.
- **No request is sent to any production surface** by this seat; production traffic is the writer (S5-AC2).
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY; ids `NFRA_OPSEC202609-Z-S<n>`; `project`, `fabric`, `spec_asserts`, `world_is`), then keep working; never a message.
- **One project per instance (Rule 27):** this seat holds NFRA_OPSEC202609 ONLY.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~Z <0.7.0_AE_CloudOps~Z@opal.agent>" -F <msgfile>`; push is the integrator's.

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @bff1f8d012 (v0.1), cell OP-s-5 (s.1a; manifest row S5; ROUND 1).
<owned_cells>OP-s-5</owned_cells>
Read-dependencies, NOT claimed: OP-s-17 (the S3 destination; its TO runs at the other seat), OP-s-6 / OP-s-20 / OP-s-23 / OP-s-14 (the consumers of these logs; their own cells).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 20 gates armed over 5 carriers (C1 21 -> 5, C2 3 -> 3, C3 12 -> 12, C4 20 SEMI-DECIDABLE -> 0, C5 337 NOT-DECIDABLE -> 0); 0 gates name NFRA_OPSEC202609 or WAF logging; G-15 (the alert/monitor moratorium, CLAUDE.md:208) BINDS this cell hardest -- FWD-5 is a named exception for LOGGING, S5-AC6 is the control that nothing beyond it rides; read 2026-09-03 06:5xZ at the issuer's seat.
comp-iam: RUN -- DESIRED plane (401 .tf files, 369 attached / 24 NOT ATTACHED / 2 Deny unparsed); this cell's new grants are two SERVICE principals (WAF logs delivery to CloudWatch Logs via the resource policy AWS attaches, the ALB log-delivery principal on one S3 prefix) -- verified on the live plane by the log group's resource policy read and the bucket policy read, never by comp-iam silence.
comp-adversary: RUN -- rc 0 at read-vintage @e10633f8b7 (2026-09-03T07:33:52Z); 3 commits, 3 repo paths, 1 file:line cites, 8 tool mentions; cited commits 3 attempted / 3 verified / 0 UNVERIFIABLE; cited paths 3 attempted / 2 stable / 1 flagged (the one flagged path is the proof instance this TO CREATES -- GONE at read-vintage, expected).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S5-AC1`..`S5-AC7`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-5.waf-cloudfront-alb-logging.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. S5-AC6's resource census (count 0 with its denominator) and S5-AC5's four-destination retention read are the controls that must be able to FAIL. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">
    <step><run>comp-read infra/aws/terraform/portal-auth/waf-cloudfront.tf --for "whether any aws_wafv2_web_acl_logging_configuration exists, and how the ACL resource is named for the logging resource to reference"</run><expect>0 logging configurations today (the brief's zero re-measured); the ACL's Terraform address located</expect><if_mismatch>STOP; a logging configuration already present is a row before any edit</if_mismatch></step>
    <step><run>comp-find 'access_logs|logging_config|aws_wafv2_web_acl_logging_configuration' --files infra/aws/terraform infra/aws/ec2</run><expect>every existing logging block in the estate listed with the denominator, so this cell follows the estate's idiom rather than inventing one</expect><if_mismatch>surface as a row</if_mismatch></step>
    <step><run>comp-blast opal-cloudfront-protection</run><expect>the ACL's consumers listed (the distribution); no other consumer is touched by adding logging</expect><if_mismatch>surface to the issuer as a row</if_mismatch></step>
  </phase>
  <phase id="2" when="before commit">
    <step><run>.tools/commit-gate.sh on every .tf/.py/.sh touched; terraform plan via the estate wrapper on every module touched</run><expect>the plan adds ONLY: two logging configurations, two log groups (+ retention), the CloudFront logging block or v2 delivery pair, the ALB attribute change, the one bucket-policy statement -- and NOTHING of the alarm/filter/subscription/SNS classes</expect><if_mismatch>STOP; an alarm-class resource in the plan is a moratorium breach, not a plan detail</if_mismatch></step>
  </phase>
  <phase id="3" when="after commit">
    <step><run>the reads named in S5-AC1..AC5; terraform plan re-run</run><expect>logging ON on all four legs with events/objects present or the read count stated; retention >= 7 d on 4 of 4; 0-diff</expect><if_mismatch>ROLL BACK inside the ledger entry and escalate loud (NEVER-2)</if_mismatch></step>
  </phase>
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO~Z` with per-criterion evidence (the reads pasted; the first event and the first objects quoted with their timestamps), the ledger entry id, and push state as MEASURED. GO = this TO + the dispatch message; this TO ACTIVATES when TO-OP-S-3's complete flip is committed by this seat (sequential on one seat; the GO for this face is carried by the same dispatch message and is conditional on that flip).
