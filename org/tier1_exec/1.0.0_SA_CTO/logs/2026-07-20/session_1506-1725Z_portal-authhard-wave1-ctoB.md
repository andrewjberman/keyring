# Session Log -- 1.0.0_SA_CTO~B (PORTAL_AUTHHARD lead) -- 2026-07-20 1506-1725Z

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, VALIDATE

Lane note: 1.0.0_SA_CTO~B is an MSTR-spawned CTO tilde-lane (LD-0323), DISTINCT from the base
1.0.0_SA_CTO (Andrew ontology session). Log filed in the base folder per the lane convention, ~B in title.

## Window summary

Stood PORTAL_AUTHHARD up from charter and drove Wave-1 to CLOSED (deployed + exercised + CVO-green) in one
session, with Wave-2 fully decomposed and its first item in active design. Mandate (LD-0323, Andrew-direct):
PRD the MSTR auth-hardening brief (WS-1..8), decompose to TOs, issue to 0.7.0_AE_CloudOps~B, arch-gate every
IAM/WAF/session/Lambda touch, drive to completion, CC MSTR on close.

Sequence: startup (/watcher, LD-0290 serial, register) -> read brief + Andrew's full source proposal + LD-0323
+ project record -> RE-GROUNDED the load-bearing anchors at source myself (Rule 22) -> authored PRD v0.1
(docs/architecture/PORTAL_AUTHHARD_PRD.md) -> decomposed + GO'd Wave-1 to a confirmed-LIVE executor -> surfaced
the alert-suspension tension (Andrew ruled "no alarms", folded) -> design arch-gate -> plan arch-gate (add-only)
-> Wave-1 deployed v1.20.0 -> executor exercise battery + my independent applied-state ground-truth -> CVO
independent verify GREEN -> Wave-1 CLOSED. Wave-2 (WS-2b/6/3) authored; WS-2b GO'd design-first.

## MCP traffic (this window)

~18 messages handled. Significant dispatches:
- OUT: Wave-1 GO (WS1/2a/8) -> executor; design arch-gate GO; plan arch-gate GO (add-only); test-user GO
  (binding lifecycle); Wave-1-GREEN + WS-2b GO -> executor. Alert-suspension SURFACE -> COO~Z. Two MILESTONE
  notes + one close -> MSTR. Verify-request + ACK -> CVO~Z.
- IN: MSTR mandate (LD-0323); executor READY, WS1 design, TF plan, RAVC x2 (deploy + trio-close), WS2a
  correction; COO~Z alert-ruling relay (Andrew "no alarms") + metrics-scope confirm; CVO~Z verify ACK + GREEN verdict.
- Stale residue in the ~B inbox (2026-07-14 CloudOps/DS/PartnerETL msgs from a prior ~B incarnation) -- noted, not actioned (different superseded project).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| Glob | locate auth stack (auth-handler/edge/authorizer/portal-auth tf) | PASS | stack lives in MAIN repo infra tree, not the portal submodule -> comp-tools + safe-commit see it |
| safe-commit.sh | 8 commits (PRD, TOs, records) | PASS | surface-check OK each; risk-reflex clean |
| aws (rail-checked) | independent applied-state ground-truth: dynamodb describe-table, iam simulate-principal-policy (one-arn isolated), wafv2 list/get-web-acl | PASS | table live/ACTIVE; UpdateItem allowed; AuthLoginRateLimit live + RateLimitRule untouched (never-widen on applied state) |

**What worked:** rail-checked raw `aws` for applied-state verification of a just-deployed security change.
**Why raw aws not comp-tools:** Rule 22a mandates the LIVE primitive for a NEW resource -- comp-iam models
(action) not (action,resource) and fails GREEN on a new ARN; no comp-tool covers WAF web-ACL rules or bare
new-resource existence. Marked `# rail-checked` per Rule 21. **Gap:** none new.

## Files modified

See commit messages: bfbb17d9b, b1c01b39c, ed820bfd1, d52b8ee55, 4390a997b, 4aa801533 (all authored
1.0.0_SA_CTO~B). Net: docs/architecture/PORTAL_AUTHHARD_PRD.md (new, + Appendix A arch-decisions);
org/projects/PORTAL_AUTHHARD.json (phase/prds/blocking); 6 TO files
org/projects/task_orders/PORTAL_AUTHHARD.WS{1,2a,8,2b,6,3}.*.md.

## Blockers

None. One shared-worktree merge conflict encountered + RESOLVED cleanly: my push raced the executor's
deliverable+ledger commits; `git stash` correctly gate-blocked (blanket-park hazard); resolved surgically
(unstage + revert file2 to HEAD + move file1 aside to scratchpad + `git pull --no-rebase` + verified merged
== aside copy, byte-identical, nothing lost) -> pushed. Executor authorship preserved.

## Current state (handoff surface)

- **Project:** PORTAL_AUTHHARD (org/projects/PORTAL_AUTHHARD.json), owner 1.0.0_SA_CTO~B, LD-0323. PRD =
  docs/architecture/PORTAL_AUTHHARD_PRD.md v0.1 (+ Appendix A: A.1 MFA=native-TOTP, A.2 confirm-item grounding,
  A.3 no-alarms ruling).
- **WAVE-1 CLOSED, GREEN:** portal-auth-v1.20.0 (deploy record 067da416e, source 70b2560f0, TF a6d4f52ed,
  exercise deliverable @d84ac01d4). WS-1 (per-account DynamoDB throttle table `opal-portal-auth-throttle`
  us-east-1 + WAF rule `AuthLoginRateLimit` Block/pri2/100-per-300s/IP scoped /auth/{login,forgot,reset} on
  web-acl `opal-cloudfront-protection` a09833c0-... + structured login_failed logs + least-priv IAM on
  opalinvest-auth-lambda-role), WS-2a (refresh() status re-check, auth.ts:129, disabled -> 500 + no token),
  WS-8 (validatePassword min 12 + breached set-time-only). ZERO alarms (Andrew ruling A.3). CVO GREEN @0ce2731bf.
- **WAVE-2 in flight:** WS-2b (revocation primitive) GO'd DESIGN-FIRST -> executor 0.7.0_AE_CloudOps~B designing;
  arch tension to resolve = refresh-path vs full-access revocation (my lean: refresh-path, <=15min access bound).
  WS-6 (least-priv role split + secret de-wildcard) + WS-3 (MFA native-TOTP) authored, dispatch_held, queued.
- **Follow-ups (tracked, non-blocking):** WS-8 breached-list = curated top-N head, full top-10k needs an egress
  word or file drop; password-rejection 500-not-400 + WS2a 500->403 (grep-safe UX, deferred, touch error contract).
- **Reachability:** registered LIVE (PID 24560); persistent Monitor bb4exk1ro (survived a broker restart mid-session,
  re-registered). LD-0290 serial file written.

## Next steps

- **[1.0.0_SA_CTO~B]** ARCH-GATE the executor's WS-2b design when it lands (refresh-path-vs-full-revocation
  tradeoff + ver-claim placement at both verifiers + key-rotation cache). Then GO WS-6 (never-widen co-sign
  w/ COO~Z) + WS-3. Author Wave-3 (WS-5 extraction/cost, WS-7 origin-lockdown+pentest) as Wave-2 progresses.
- **[0.7.0_AE_CloudOps~B]** deliver the WS-2b design (design-first, no build before arch-gate).
- **[3.0.0_SA_CVO~Z]** independent verify each Wave-2 WS as it lands (PRD S6 regime); Wave-1 done @0ce2731bf.
- **[2.0.0_SA_COO~Z]** never-widen co-sign on the WS-6 role-split TF plan when it reaches that stage.
- **[0.0.0_AB_MSTR]** CC on project close per LD-0323.
