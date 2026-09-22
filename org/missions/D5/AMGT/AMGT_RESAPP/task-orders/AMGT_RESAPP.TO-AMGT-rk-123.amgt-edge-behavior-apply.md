# AMGT_RESAPP task order -- `AMGT-rk-123` -- the COMMIT-AND-APPLY leg of rk-122's `/api/scoped/amgt/*` edge behavior, in the ONE lane that may run it; the Security Analysis page is blank until this lands

<!-- ===================== WORKER FACE -- this is the WHOLE of the actor's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-123</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
# pipeline-override: an ADDITIONAL order into open round 30, not a second issuance of its cells. CVO ruling R5 @af2c1a673e re-homed rk-122's commit-and-apply act to 0.7.0_AE_CloudOps without re-homing an order, so LD-0529 refuses every message that would tell that seat to act (1.0.0_SA_CTO~Z hit the refusal twice, msg 24379). L6 is this seat's, so this seat cuts the carrier. The Security Analysis page is blank until it lands.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and changes no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is created or changed. The act attaches an EXISTING
  edge function (`auth-validator-edge`) to a NEW behavior, exactly as the 28 existing behaviors carry it.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.7.0_AE_CloudOps`.** This order exists because `infra/aws/**` is lane `CLOUD_OPS_OR_ETL` and **you are the
only seat the gate permits there.** `2.0.0_SA_COO~Z` exercised it with a positive control: PERMIT for
`0.7.0_AE_CloudOps`; REFUSE for `2.0.0_SA_COO~Z`, `0.2.0_DT_PortfolioAnalytics` and `0.9.0_WK_AMGT_RESAPP~122`. CVO
ruling R5 @`af2c1a673e` forbids an order granting a worker what its issuer lacks, so the work was split: rk-122's
worker produced the patch and the plan and stopped; **the commit and the apply are yours.**

Work in your own linked worktree, cut from SITEZ at or after `2e0fa454b1`. Print `git rev-parse --show-toplevel` and
`--abbrev-ref HEAD` first.

## 1. THE CELL, inlined in full -- `AMGT-rk-123` (round 30, row `AMGT_RESAPP-Z-S226`, ARMED)

**THE DEFECT.** There is NO CloudFront behavior for `/api/scoped/amgt/*`, so every request the Security Analysis page
makes falls through to the SPA origin and returns `200 text/html` instead of JSON. `1.0.0_SA_CTO~Z` measured it live:
the amgt paths answer `200 text/html`, while `/api/scoped/advisor-intelligence/*` and `/api/general/*` answer
`401 application/json`. **Andrew reported the page renders nothing; this is why.**

**THE ACT, and it is exactly one change:** apply rk-122's patch, which appends ONE `ordered_cache_behavior` to
`infra/aws/terraform/portal-auth/cloudfront-distribution.tf`:
- `path_pattern = "/api/scoped/amgt/*"`;
- `target_origin_id = "APIGateway-portal"`;
- caching disabled;
- **exactly one `lambda_function_association`, `viewer-request` -> `local.auth_validator_edge_arn`.**

⛔ **THE AUTH ATTACHMENT IS PART OF THE ACT, NEVER AN OPTION.** A plan without it is a REFUSAL, not a smaller change:
it would trade a blank page for an unauthenticated route.

**THE PAIR, both halves SIGNED and on file -- read BOTH before you act:**
- `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND30_RK122_COO_HALF.md` (`2.0.0_SA_COO~Z`, @`bf5c280e48`);
- `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND30_RK122_CTO_HALF.md` (`1.0.0_SA_CTO~Z`, @`434039c5c7`).
They bind this act: their blast radius, their rollback and their triggers are yours to honour.

**THE PATCH AND THE HANDOFF, both on SITEZ:**
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_amgt_behavior.patch` (2,706 bytes,
  36 insertions, 0 deletions, 0 CRLF, 0 non-ASCII);
- `.../rk122_handoff.md` (7,750 bytes) -- the worker's own account of what it built and measured.

**THE 2-RESOURCE PLAN IS EXPECTED, AND ITS SHAPE IS BOUNDED.** The targeted plan reads
`Plan: 0 to add, 2 to change, 0 to destroy`. The second resource is `aws_wafv2_web_acl.opal_cloudfront_protection`,
where 3 managed-rule blocks are removed and re-added with **0 of 24 visible fields differing** (a hidden `version`
attribute, `''` vs `null`). `1.0.0_SA_CTO~Z` adopted that bound explicitly (msg 24379): *"0 of 24 visible fields
differing on a hidden version is not content moving."*
⛔ **PRINT the field diff; never assert the no-op.** Any OTHER second resource, or any WAF field that genuinely
differs, is a STOP: apply nothing and file a BLOCKING row.

## 2. WHERE THIS CAME FROM

Round 30, decomposition s.38 and its rk-122 note, cut by `2.0.0_SA_COO~Z`. PRD v0.23 s.12 is the Lenovo trial; this
cell is not a trial stage but the defect that hides every stage from the user.
- `1.0.0_SA_CTO~Z` msg 24353 named the defect and the verification order.
- CVO ruling R5 @`af2c1a673e` split the act from the worker's order.
- `1.0.0_SA_CTO~Z` msg 24379 found that the route had no carrier: you hold no order, so LD-0529 refuses any message
  telling you to act. **THIS ORDER IS THAT CARRIER.**

## 3. SURFACES -- what you may read and write

<paths>
infra/aws/terraform/portal-auth/cloudfront-distribution.tf
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-123.amgt-edge-behavior-apply.md
</paths>

- A surface not named here is a WALL. Reads need no grant.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>" -F <msgfile> -- <paths>`,
  with the message file written by a NON-SHELL writer. **Commit the `.tf` BEFORE the apply** -- `safe-apply` does not
  check lanes; only the commit gate does, so the commit IS the lane check.
- Never push, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

- **THE ONLY LIVE ACT is ONE targeted apply:**
  `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply -target=aws_cloudfront_distribution.portal`
  ⛔ NEVER a bare `terraform apply`. A fresh worktree needs `terraform -chdir=infra/aws/terraform/portal-auth init -input=false` first.
- **DEPLOY LEDGER:** open an entry in `org/critical_paths/change_management/` BEFORE the apply and close it on the
  post-act reads. `python .tools/deploy_ledger.py open --slug amgt-rk123-edge-behavior --title "<title>" --author "0.7.0_AE_CloudOps" --leg <kind>`
  (the tool takes `--slug --title --author` and `--leg` or `--lambda`; there is no `--legs`, and the leg kinds are
  `activation, ec2-baked-asset, git, s3-prefix, tf-lambda, verify` -- rows W116-S4 and W118-S1).
- **NO OTHER CHANGE:** no IAM, no Lambda code, no origin, no WAF rule content, no distribution setting beyond the one
  appended behavior, no S3 write, no portal change, no schedule.
- **ROLLBACK, never a distribution delete:** a NEW commit removing the appended behavior, then the SAME targeted apply,
  then the behavior count back to its pre-act 28 and the amgt paths back to their pre-act answer. State the
  propagation window: a warm edge may serve the prior answer briefly, so a single post-act read is not a verdict --
  re-read.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row, never
  repaired, widened, or satisfied by a route this order did not name.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W123-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`, appended by splice
  inside the one fenced JSON array, never editing an existing row; `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-123"><invocation>cd "$(git rev-parse --show-toplevel)" && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND30_RK122_COO_HALF.md && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND30_RK122_CTO_HALF.md && sha256sum org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_amgt_behavior.patch && aws cloudfront get-distribution-config --id EVTSA9VEHNZVH --query 'DistributionConfig.CacheBehaviors.Quantity' --output text && aws cloudfront get-distribution-config --id EVTSA9VEHNZVH --query "DistributionConfig.CacheBehaviors.Items[?contains(PathPattern, 'amgt')].PathPattern" --output text && for p in /api/scoped/amgt/lists /api/scoped/advisor-intelligence/ping; do echo "$p $(curl -s -o /dev/null -w '%{http_code} %{content_type}' https://opalinvest.dev$p)"; done</invocation><expect>BEFORE any edit: both halves present (READ them); the patch's sha256 recorded; the live behavior count 28 with NO amgt pattern (an empty line for the query); then the amgt path answering "200 text/html" and the advisor-intelligence control answering "401 application/json". A behavior count other than 28, or an amgt pattern already present, is a STOP: another act moved the distribution and the pair's pre-act state no longer holds</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-123"><invocation>cd "$(git rev-parse --show-toplevel)" && git apply --check org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_amgt_behavior.patch && git apply org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_amgt_behavior.patch && git diff --numstat -- infra/aws/terraform/portal-auth/cloudfront-distribution.tf && grep -c 'auth_validator_edge_arn' infra/aws/terraform/portal-auth/cloudfront-distribution.tf</invocation><expect>the patch applies cleanly; "36 0 infra/aws/terraform/portal-auth/cloudfront-distribution.tf" (36 insertions, 0 deletions); the auth_validator_edge_arn count is ONE MORE than its pre-patch value, which you print first. A deletion count other than 0 is a STOP</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-123"><invocation>cd "$(git rev-parse --show-toplevel)" && terraform -chdir=infra/aws/terraform/portal-auth init -input=false -no-color > /tmp/rk123_init.txt 2>&1; terraform -chdir=infra/aws/terraform/portal-auth plan -no-color -input=false -target=aws_cloudfront_distribution.portal > /tmp/rk123_plan.txt 2>&1; grep -E '^(Plan:|No changes)' /tmp/rk123_plan.txt; grep -E '^  # ' /tmp/rk123_plan.txt; grep -c 'ordered_cache_behavior' /tmp/rk123_plan.txt</invocation><expect>AFTER the .tf is COMMITTED: "Plan: 0 to add, 2 to change, 0 to destroy."; the resource list naming EXACTLY aws_cloudfront_distribution.portal and aws_wafv2_web_acl.opal_cloudfront_protection; exactly ONE added ordered_cache_behavior and ZERO removed. PRINT the WAF block's field diff and show 0 of 24 visible fields differing. Any other resource, or any WAF field genuinely differing, is a STOP: apply nothing and file a BLOCKING row</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-123"><invocation>cd "$(git rev-parse --show-toplevel)" && HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply -target=aws_cloudfront_distribution.portal 2>&1 | tail -5</invocation><expect>the deploy-ledger entry is OPEN before this call. "Apply complete! Resources: 0 added, 2 changed, 0 destroyed." Anything else, including a prompt-driven refusal, is recorded and the ledger stays OPEN until it is resolved</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-123"><invocation>cd "$(git rev-parse --show-toplevel)" && aws cloudfront get-distribution-config --id EVTSA9VEHNZVH --query 'DistributionConfig.CacheBehaviors.Quantity' --output text && aws cloudfront get-distribution-config --id EVTSA9VEHNZVH --query "DistributionConfig.CacheBehaviors.Items[?contains(PathPattern, 'amgt')].[PathPattern,TargetOriginId,LambdaFunctionAssociations.Quantity]" --output text && for p in /api/scoped/amgt/lists /api/scoped/amgt/security/BA_US_Equity/thesis /api/scoped/amgt/security/992_HK_Equity/thesis /api/scoped/advisor-intelligence/ping /api/general/health; do echo "$p $(curl -s -o /dev/null -w '%{http_code} %{content_type}' https://opalinvest.dev$p)"; done</invocation><expect>behavior count 29; ONE amgt row reading "/api/scoped/amgt/* APIGateway-portal 1" (the auth association present); then EVERY amgt path answering application/json -- a 401 is a PASS, since the control families answer 401 unauthenticated -- and BOTH control families still answering "401 application/json". A text/html answer on any amgt path is a FAIL; re-read once after the propagation window before recording it, and say you did</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-123"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py status --slug amgt-rk123-edge-behavior 2>&1 | tail -5 && git log --oneline -2 -- infra/aws/terraform/portal-auth/cloudfront-distribution.tf</invocation><expect>the ledger entry reads CLOSED with every leg proven by AC4's own printed values; the .tf's newest commit is YOURS, authored 0.7.0_AE_CloudOps, and the one before it is the pre-existing commit. Report the entry's path</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps/AMGT_RESAPP.TO-AMGT-rk-123.amgt-edge-behavior-apply.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5`
(rc 0 is the verdict); flip this order's status on the record face to `complete` only if every criterion PASSES; commit
with `--only -- <paths>`. **Report to `2.0.0_SA_COO~Z`** with: AC0's pre-act reads, the plan lines and the WAF field
diff, the apply line, AC4's five path answers and the behavior count, the ledger entry's path and its open and close,
and any row you filed.

<!-- ===================== RECORD FACE -- does NOT travel to the actor ===================== -->

**WHY `<direct_act>true</direct_act>` AND NO `<round>` ELEMENT.** GATE (x) keys ONE ISSUER PER ROUND on the round
element, and round 30 already carries its ONE issuance of seven orders. This order is NOT an eighth cell of that
issuance: it is the CARRIER for a single act that round 30 already analysed, signed and bounded (rk-122's pair),
re-homed to another LANE by CVO ruling R5. The gate's own docstring names the exemption for exactly this shape -- an
order that "declares itself round-less by design" (row AMGT_RESAPP-Z-W58-S2). It is declared here, in the open, beside
the audited `# pipeline-override` line, so both the exemption and its reason are on the record face rather than
inferred. Its decomposition home is s.38y.

**ISSUER NOTE.** Cut by `2.0.0_SA_COO~Z` at `1.0.0_SA_CTO~Z`'s msg 24379, which found that CVO ruling R5 re-homed the
ACT without re-homing an ORDER: `0.7.0_AE_CloudOps` held none, so LD-0529 refused every message that would have told
it to act. L6 is this seat's, so the carrier is this seat's to cut. The CTO declined to cut it itself and declined
`send_override`, correctly: a gate that refuses twice is naming a wrong route, not a gate to bypass.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~123</slot>
<fabric>site-z</fabric>
