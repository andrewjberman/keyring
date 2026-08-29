# 1.0.0_SA_CTO~D -- Daily Sprint web client (built, live, ledger CLOSED) + raw-grep gate audit -- 17:22-19:23Z
**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE, DIAGNOSE

Andrew-direct seat: "finish startup but do not engage with the other agents ... we have a separate
project to address here." Zero outbound MCP this session; inbound read + ACKed only.

## Summary

1. **Daily Sprint web client, option A, DONE and LIVE.** Andrew (VERBATIM): "a very thin web client
   upon which we publish the /daily-sprint ... intelligent about who is viewing it ... switches between
   desktop view and mobile view ... only be accessible through a custom link on Teams, not public URL."
   Design tabled, "recs approved, build it solo." Built on the existing estate: the renders /daily-sprint
   already produces (both variants), the opal-gateway ALB's Entra `authenticate-oidc` default action
   (alb.tf:161 "the future GUI path"), and S3 `opal-data-portal-v2/daily-reports/`.
   Serving: `https://mcp.opalinvest.dev/sprint` (latest) / `/sprint/<DAY>` / `/sprint/archive`;
   variant = `?v=` > `Sec-CH-UA-Mobile` > UA; one-way narrow-viewport hop. Ledger
   `20260828T1758Z_opal-gateway-sprint-view` CLOSED 5/5. Tag `opal-gateway-v1.7.0`.
2. **Blocker found on first human use, root-caused, routed:** `AADSTS50011`. App 1 "M365-MCP-Login"
   (`53360468-...`) has ONE web redirect URI `.../oauth2/idpresponse%60` -- a pasted trailing backtick.
   The ALB builds the callback itself (fixed path), so only the registration can change; Andrew's
   account: `Insufficient privileges`; app has no owners -> LDT. Recorded as IT_REQUEST.md Incident #3.
   Andrew: "makes way more sense to just get in touch with IT" -- he is calling them; a portal-page
   alternative (opalinvest.dev/sprint under ProtectedRoute requireInternal) was assessed and declined.
3. **Temporary no-login link for tonight (Andrew: "option 1 works here. go"):** publisher `--presign`
   -> `daily-reports/latest/` + chooser + 7-day presigned links; exercised (chooser fetched via its own
   link; both pages 200; unsigned 403). Expires 2026-09-04T19:20:27Z. /daily-sprint step 7 amended.
4. **IT/LDT call list** (gateway x3 + Azure wiring x7 from MSTR 78699, every value re-read live).
5. **Raw-grep gate audit** (Andrew: "narrow it even harder or just block it entirely and replace with a
   comp-grep function ... i am very tired of grep"): 24 command shapes fed to the live hook. `grep -rn
   foo .`, every compound command, and `cd X && aws iam get-role` pass SILENT; Gate-1 fired 4x in 4
   weeks; silent allows are unlogged (no denominator). comp-find is the replacement. Proposal T1 =
   deny per SEGMENT; decision-gated at Andrew. Andrew's rulings so far: comp-find stays repo-only;
   AWS-substrate expansion = a proposal to write, not build.

## Commits (8, all author 1.0.0_SA_CTO~D; on origin through f41fdaa7e7 except the last)

97b8103069 gateway /sprint + daily-reports-iam.tf + tests (lane override CLOUD_OPS_OR_ETL, audited) ·
d19943c4c2 publisher + skill step 7 + README · 1986e6df89 EC2_MANIFEST row (override SHARED_CLOUD_OPS)
· ddd974d390 ledger CLOSED · 8fa5d25c4b IT_REQUEST Incident #3 (override) · 1949ee56af IT call list ·
05ebf8c4fb grep-gate audit · 55c6dc9524 publisher --presign (LOCAL at write; rides window 19).
Per-file detail: see those commit messages.

## Deployment sequence + verification (actual outputs)

- IAM: `safe-apply` (`SAFE_APPLY_TERRAFORM`=winget tf 1.14.5; `.tools/terraform.exe` 1.9.8 cannot init
  this backend) -> `Apply complete! 1 added` ; re-plan `No changes` ; simulate-principal-policy ONE
  resource per call: GetObject exact key `allowed`, sibling prefix `implicitDeny`, ListBucket ctx
  `daily-reports/` `allowed`, ctx `platinum/` `implicitDeny`.
- Code: `safe-ec2-deploy.sh` (needs `.tools` on PATH for jq) rc=0 18:14:20Z; SSM 150f9ad2: on-box md5 ==
  local for sprint_view.py f2195b70 / server.py 9ba5c40f / config.py 8b63cced; systemd active
  18:14:08Z; on-box `/sprint` 401 (no header), `/sprintfoo` 404, `/health` 200; instance role lists
  `daily-reports/2026-08-27/` and heads the Mobile object (ETag == publisher md5).
- Wall: through the ALB, unauth `/sprint` x3 -> `302 login.microsoftonline.com/6810043e-.../authorize?
  client_id=53360468-...`; `/.well-known/oauth-authorization-server` 200 (bypass rule intact).
  ⚠ This proved the redirect FIRES, not that a person can PASS -- the App-1 defect sat one hop
  downstream (memory: feedback_a_302_to_the_idp_proves_the_wall_exists_not_that_anyone_can_pass_it).
- Publish: 2026-08-27 Desktop 39689 B / Mobile 37812 B read-back MATCH; `s3api list` 18:12:42Z.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-which | 2 questions (gateway location; auth-validator-edge) | PARTIAL | no curated rule for the gateway; near-tie for the edge -> fell to comp-find / comp-routes |
| comp-find | ~30 runs (gateway framework/auth/S3 patterns, hook internals, rail-log, corpus probes) | PASS | two BRE-warning runs (escaped `\|`), re-run bare; `--hidden .` census = 168,349 gitignored invisible to default |
| comp-routes behaviors | 2 | PASS | 28 behaviors; `/api/general/*` -> opal-data-portal-v2 origin identified |
| comp-iam gaps | 1 (after iam.tf) | PASS | only pre-existing D_04 items; (action,resource) axis proven by simulate instead |
| commit-gate | 3 runs / 6 files | PASS | |
| deploy_ledger.py | open / close-leg x5 / close | PASS | |
| verify-ec2.sh | 2 | WARN | first run "0 checked" (jq missing = null result); second: 1 drift (expected pre-deploy) |

What worked: comp-find as the search default (Andrew's mid-turn correction "you should be using
comp-find" -- complied for the rest of the session). What failed: comp-which had no vocabulary for
"opal-gateway". Gap found: comp-find cannot search outside the worktree (git rc=128 dressed as zero)
-- Andrew ruled repo-only is fine; the default corpus hides 168k gitignored files (disclosed on every
zero) -- undecided.

## MCP traffic

Inbound 9 (3 stale 08-07 FYIs; MSTR window 17 OPEN/CLOSE, window 18 OPEN/CLOSE, Azure list 78699),
all READ-acked. Outbound 0 (Andrew's instruction). HOLDs honoured; my commits rode windows 17/18.

## Blockers

- **App-1 redirect URI (LDT, Global Admin):** blocks the Entra-walled link until next week (Andrew).
  Evidence: `az ad app show` web.redirectUris = [`.../idpresponse%60`]; `az ad app update` ->
  `Insufficient privileges`. Workaround live (presigned link). Not a fabric blocker.
- **Grep-gate T1:** decision at Andrew (T1 go/no-go; T2 single-file; native Grep/Glob).

## Current State (zero-context handoff)

- Gateway code: `infra/aws/ec2/opal-gateway/app/sprint_view.py` (+ server.py GuardMiddleware branch for
  `/sprint*`, config.py DAILY_REPORTS_* / SPRINT_VIEW_ALLOWED_EMAILS); deployed to i-07dccb1615503ac99
  `/opt/opal-gateway`; IAM `opal-gateway-role` policy `opal-gateway-daily-reports-read`
  (`infra/aws/terraform/opal-gateway/daily-reports-iam.tf`).
- Content: `s3://opal-data-portal-v2/daily-reports/<DAY>/{Desktop,Mobile}_DAILY_REPORT_<DAY>.html` +
  `daily-reports/latest/{Desktop,Mobile}_DAILY_REPORT.html,index.html` (presigned; expiry 09-04 19:20Z).
- Publisher: `daily_reports/scripts/publish_daily_report.py --date <DAY> [--presign]`; /daily-sprint
  SKILL.md step 7 calls it.
- Records: ledger CLOSED; `IT_REQUEST.md` Incident #3; `deliverables/IT_CALL_LIST_20260828_LDT.md`;
  `deliverables/COMPRAIL_GREP_GATE_AUDIT_20260828.md`; memories: 302-vs-round-trip, three wrapper
  toolchain refusals.
- Phase 2 (declined for now): Teams SSO tab app (LDT-gated). Portal-page alternative assessed, declined.

## Next Steps

1. **[Andrew]** tonight: `/daily-sprint` (step 7 publishes + presigns; the same Teams link updates).
   Call LDT: App-1 redirect fix + app ownership + Azure items (IT_CALL_LIST).
2. **[1.0.0_SA_CTO~D successor]** on LDT's fix: `az ad app show ... web.redirectUris` == exact callback,
   then a real sign-in to 200 on `/sprint` (the round trip, not the 302) -> switch the Teams tab to
   `mcp.opalinvest.dev/sprint`, delete `daily-reports/latest/`.
3. **[1.0.0_SA_CTO~D successor]** on Andrew's T1 word: extend `.tools/comprail-gate1-fptest.sh` with the
   24 shapes (red first), per-segment deny in `comp-tool-hud.sh`, ALLOW-SEARCH logging, comp-grep ->
   forwarder, CLAUDE.md Rule 21 text; broadcast needs Andrew's word (seat is off the channel).
4. **[1.0.0_SA_CTO~D successor]** write the `comp-find --corpus aws` proposal (live-inventory substrate,
   own denominator + vintage) -- proposal only.

**state: IDLE at Andrew's decision** · push state of this log: LOCAL (origin/CLOUD @f41fdaa7e7, ls-remote read 19:22Z)
