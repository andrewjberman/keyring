# Session close 1720-1755Z -- W6 PROD promote + closeout gates 1-3, Andrew-direct close

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

Continuation of `mdlp_monpub_deploy_wave_w2_w3_w5_w6_w8_1500-1720Z.md` (same session, window
1720Z -> 1755Z). Closed out on Andrew-direct word ("everything looks done here, close out").

## Current State (handoff surface -- zero-context reader)

- **LIVE PROD: `c6f561b6`, tag `portal-v2.1.155` (peel-verified: tag^{commit} == origin/PROD
  head), CI run 30837075543 "Deploy to Production" conclusion:success** (verified gh run view
  --json, never watch). Content: MDLP_MONPUB.W6 client-cache invalidation on rollback success
  (DEV e77e8b6f + type-fix 5ef651b2). Workspace pointer -> 5ef651b2 pushed on origin/CLOUD
  (MSTR window, 19c47a8a73). Portal main tree ON DEV (verified), worktree pruned (physical
  .runtmp/portal-promote-20260803T172* dir persists -- known Windows long-path case, inert).
- **Promote discipline notes:** the /prod-deploy typecheck gate CAUGHT a real TS error in my
  own W6 contract widening (optional newExecutionId vs state-setter closures) BEFORE the
  merge -- fixed as 5ef651b2 (narrowed const), tsc -b clean; my earlier "tsc clean" had run a
  non-canonical check (bun run tsc --noEmit, not the typecheck script) -- banked. LD-0368
  integrator-only pushes: portal DEV + PROD pushes ran under the audited never-override WITH
  MSTR's explicit prior no-objection (172153Z); the CLOUD pointer push stayed with MSTR.
  Freeze window declared to COO at start, released on the landed report; COO accepted the
  artifact table and closed **GATE 1**.
- **GATE 2 (W8 scratch exercise): execution COMPLETE, formal closure pends CVO witness.**
  I provisioned `opal-data-refresh-api-qa-scratch` (TF `infra/aws/terraform/data-refresh/`
  `qa-scratch-instance.tf`, applied 3-add + 0-diff; identical artifact sha E4944Imr...;
  env BUCKET=opal-313476888478-yang-qa-scratch, TABLE_NAME real per DS plan; Sid-dated role
  grant, Rule-22a triad verified in separate invocations: scratch Put allowed / scratch Get
  allowed / live positive control allowed). DS fired all 3 legs PASS: leg 1 end-to-end
  handle_rollback exec-fdf49e30710f (manifest landed LAST with force_publish=true +
  rollback_execution_id in the BODY), leg 2 manifest-arm (:146) bypass ed35ec26 (rollback id
  in the CloudWatch FORCE_PUBLISH line; disclosed event-side manifest.bucket injection --
  the landed manifest carries no bucket field), leg 3 negative control 030ed212
  refused/seed-unchanged. Middle segment recorded SOURCE-GROUNDED-NOT-EXERCISED per CVO
  172718Z (they grounded all 3 hops incl. the LIVE ASL; the SFN Parameters top-level
  whitelist DROPS a top-level force_publish -- manifest-body carriage is load-bearing).
  **OPEN: W8 ledger `20260803T1707Z_mdlp-w8-force-publish-plumbing_deploy_completion.md`
  exercise leg -- closes on [3.0.0_SA_CVO] witness; then [0.2.0_DS_PortfolioAnalytics]
  deletes the flagged DDB fixture record (SK=exec-w8scratch, real table).**
- **GATE 3 (dual-regime auth-header capture): CLOSED by COO 175003Z.** From an authenticated
  session on deployed PROD (frontend-dev harness credential michael@opalinvest.com, the
  fabric's standing smoke account; Playwright): W9 /api/general/* -> 200, x-cache Hit,
  Age=81/82 under 300, cache-control public,max-age=300,s-maxage=300 (Miss-then-Hit both
  observed); W9b advisor-by-firm -> 200, Hit, Age=20 under 60, public,max-age=60,
  must-revalidate. Three side observations routed to [0.7.0_AE_CloudOps~F], not gate
  material: json-tiered behavior emits bare max-age=300 (no public/s-maxage); the AdvI
  page tolerates a 403 on cohort_a_summary.json?firm=bd; direct platinum fetch without
  ?firm= returns 400 (firm-context mandatory at the router).
- **Serve state at close:** benchmarks at data_as_of=2026-07-31 (legitimate, W4 recovery +
  16:23:50Z rebuild). W2 CLOSED-witnessed; W1 complete-as-superseded @1ab18def94; W7 stood
  down (Andrew removed the offending ST portfolio from Bloomberg at source); W3/W5/W8
  deploys accepted. Andrew-direct: hardening work SUSTAINED THROUGH FIX -- all of it is live.
- **PENDING-LIVE-OCCASION (COO holds as ONE bundled event, does not block closeout):** W6
  full page-level exercise + W8 middle-segment traversal + a W9 header re-capture, all on
  the next GENUINE rollback occasion.

## MCP traffic (window)

~20 messages handled; significant: CTO W6-acceptance + promote-sequencing 171852Z; COO
gates-framing 173818Z, Gate-3 close 175003Z; CVO W8 exercise ruling 172718Z (option b +
manifest-arm condition); DS W8 instance ask 173324Z -> my instance-live GO 174218Z -> their
3-legs-PASS 174734Z; MSTR no-objection 172153Z + three push confirmations (pointer,
qa-scratch TF + prior log, final wave fbae04e0e9). Freeze declared + released same window.

## Files Modified

See commit messages: portal 5ef651b2 (type fix, SURFACE_ACK audited), portal-PROD c6f561b6
(merge), workspace pointer commit (-> 5ef651b2), `qa-scratch-instance.tf` commit, this log.
All pushed via MSTR windows through fbae04e0e9.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-grep (creds/auth-state hunt) | PASS after self-caught pattern error | first call used escaped pipes (literal in Python re -- the tool WARNED and I re-ran with bare pipes); found the harness credential the Gate-3 capture used |
| comp-surface-check (portal pre-commit, on 5ef651b2) | SEV1 named, audited SURFACE_ACK | same TO justification as the W6 commit |
| simulate-principal-policy (x3, rail-checked markers) | allowed/allowed/allowed | Rule-22a triad on the new data-refresh scratch grant; separate invocations; comp-iam fails green on new resources so the raw primitive is mandated -- markers audited |
| VALGATE D-1 + push-time tsc + parity gate + /prod-deploy gates | all PASS | the typecheck gate produced the window's one real catch (TS error, fixed pre-merge) |

What worked: the gate stack -- every one of the window's four gate fires (typecheck, LD-0368,
LD-0276 command-shape, comp-rail) was a correct block, and each had a sanctioned path through.
What failed: my first tag-verify and first tsc claim earlier in the session (prior log) --
both re-verified correct this window. Gap found: comp-grep's escaped-pipe warning saved a
false-absence; no tooling gap this window.

## Blockers

None at this seat. The single open thread (W8 ledger exercise leg) has a named owner
[3.0.0_SA_CVO] and a defined close condition (witness on DS's evidence package), explicitly
accepted by COO as the only remaining step before Andrew's personal closeout.

## Next Steps

1. [3.0.0_SA_CVO] W8 witness on DS's package -> I (or successor DT session) flip the W8
   ledger exercise leg to closed in a one-line commit.
2. [0.2.0_DS_PortfolioAnalytics] delete the exec-w8scratch fixture record post-witness.
3. [2.0.0_SA_COO] report closeout readiness to Andrew (their stated next act).
4. [0.2.0_DT -- successor session] the bundled live-occasion legs when a genuine rollback
   occurs; qa-scratch teardown decision (bucket + both instances + grants are all Sid-dated /
   single-file destroys) is CTO's call whether it persists as a standing QA harness.
