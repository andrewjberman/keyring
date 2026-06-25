# Session 2026-06-25 ~1404-1602Z -- deploy_ledger fix + DC2 harness build (arch-gate cycle) + PEAK BD cross

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, COORDINATE, DIAGNOSE

Continuation of the morning bring-up. Window since last log (894ff6270). Lane: COO-sequenced DATA_PLATFORM-DC2 (+ a GO'd deploy_ledger tooling fix). PEAK BD interrupt arrived mid-window -> routed to 0.6.0, not me.

## Summary

1. **deploy_ledger phantom-leg fix (COO-GO'd, c66b397d1).** Added `--lambda <fn>` flag + a first-class `tf-lambda` leg kind: a single-Lambda TF deploy now opens EXACTLY one real leg (tf_resource resolved from lambda-source-map) instead of the 8-phantom `--pipeline` S3-code expansion (the NEVER-law false-half-landed-blare risk I hit + flagged this morning). Dogfooded my own fix-concept; tested 3 cases (--lambda->1 leg closes clean; --pipeline inf->still 8, no regression); ds-commit-gate clean. COO RAVC2 = ACCEPTED.

2. **DC2-eclipse harness -- full arch-gate cycle + ~80% built.** Drove the Eclipse test#1 (token-expiry discriminator) harness from a falsified premise through unanimous Tier-1 sign-off to a substantially-built, TF-validated state. Remaining = the verify-after script + comp-iam + -target plan + the CTO pre-apply RAVC (deliberate-paced; off-peak run tonight/tomorrow-night).

3. **PEAK BD interrupt (Andrew-direct, ADVI_BDAPIMIG P1) -- routed to 0.6.0, handled the Tier-1 cross.** CVO GO'd me onto the BD interim-cookie build; COO (staffing authority) routed it to 0.6.0_AE_PartnerETL (role-fit) + kept me on DC2. I complied with the sequencer + surfaced the one real risk (cookie-clock vs spawn-ramp) with an (A)+(C) warm-fallback offer -- both Tier-1s confirmed correct; 0.6.0 spun LIVE + already landed (A) keepalive (cookie auto-extends; cross fully closed). Not my lane.

## DC2 harness -- the arch-gate cycle (chronological)

- **Premise falsification (3dede104a):** the CTO had deferred the Eclipse /v1 authed-capture (220218Z) on a "shell-only render => sessionStorage gap" hypothesis. I grounded the PARKED state.json artifact -> auth is in COOKIES (eclipse.access_token) + localStorage (sm.access_token @ api.cloud.orionadvisor.com), NOT sessionStorage -- both storageState-captured. Premise FALSIFIED -> CTO withdrew the deferral, sessionStorage-injector path off the table. CTO credited the grounding discipline (tested-his-premise, didn't supply-a-fitting-fact).
- **CTO re-GO + decision-tree:** run #1 token-expiry FIRST (park->IMMEDIATE crawl: FULL=>expiry confirmed; SHELL=>#2 cross-origin). Single-run discriminator (production delayed-crawl is the known SHELL baseline).
- **Off-peak execution ruling:** I caught that test#1 needs a fresh parker login, which is HARD-constrained OFF-PEAK by the CTO's own isolation ruling 212001Z (eclipse_session_parker.ts:19) -- it was peak. Held the live run (would risk burning the serving session). CTO ruling: (a) autonomous off-peak harness APPROVED, (c) peak-login REJECTED, (b) piggyback REJECTED. 6 LOCKED ROE constraints (e8bdc9bff).
- **Arch-fork on the cross-box build (b7502e0b0 + the 2 arch-rulings):** grounding crawl-instance.tf surfaced 2 constraints I gated to CTO instead of deciding: (1) serving-box IAM widening -> CTO REJECTED, dedicated SSM-Automation orchestrator APPROVED w/ document-scoped SendCommand (the arbitrary-exec control) + ec2:Start/Stop crawl-ARN-ONLY + guaranteed always-stop; (2) crawl-harness full-apply is destructive (191143Z KNOWN-DRIFT) -> -target add-only APPROVED, full apply REJECTED. Self-caught my own draft's AWS-RunShellScript -> swapped to dedicated docs (CTO: "the whole ballgame"). CVO accepted a graduation-gated structural review (build-to-bar: live-applied condition / no shell-passthrough / teardown-executes).
- **Built (committed, TF-VALIDATES):** the Automation orchestration logic (7a91c00a2) + the TF (b7502e0b0: 2 dedicated fixed-command docs + document-scoped scoped IAM + Automation + DISABLED off-peak schedule) + the capture classifier (ee6f2df7a). CTO confirmed he's the pre-apply RAVC gate (no further arch input until then).

## Deployment Sequence + Verification

NO apply this window (the DC2 harness is built but HELD at the CTO pre-apply gate -- comp-iam + -target add-only plan RAVC required BEFORE safe-apply; the off-peak EventBridge schedule ships DISABLED). The deploy_ledger fix (c66b397d1) is a .tools/ change, not an AWS deploy.

`terraform validate` on infra/aws/terraform/crawl-harness (after each TF edit) = **Success! The configuration is valid.** (the only deploy-adjacent verification this window; the apply itself is gated).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| ds-commit-gate | .tools/deploy_ledger.py (the fix) | PASS | py_compile/ruff clean |
| comp-grep / comp-glob | eclipse crawl entrypoint, CrawlReport type, cot-exporter pattern, INF price producer (earlier), state.json probe | mixed | located runEclipseCrawlLive/crawl.ts, CrawlReport (endpointsCataloged); 0-match on lazy-imported helpers (read source directly) |
| terraform validate | crawl-harness (x3, after each .tf edit) | PASS | caught + fixed undeclared-local + the ssm_automation_parameters block before commit |
| comp-freshness (earlier window) | -- | -- | n/a this window |
| comp-iam gaps | PENDING | -- | the CTO pre-apply requirement -- run on the orchestrator role BEFORE the -target apply (not yet, role not built to apply) |

- **What worked:** grounding the parked artifact FALSIFIED the CTO's deferral premise (not a fitting-fact) -- the right Rule-22 discipline; gating the 2 cross-box arch-constraints (serving-box IAM widening + the destructive full-apply) to CTO instead of deciding them; self-catching the AWS-RunShellScript draft -> document-scoped dedicated docs.
- **What failed:** nothing landed-wrong. comp-grep missed lazy-imported TS helpers (loadParkedSessionReadOnly etc.) -- expected (dynamic imports); read source directly.
- **Gap found:** the deploy_ledger `--pipeline` phantom-leg defect (now FIXED, c66b397d1). SSM SendCommand has no `ssm:DocumentName` condition key -> the instance<->doc cross-bind isn't IAM-enforceable (document-scoping IS); flagged inline + for the CTO pre-apply RAVC.

## Blockers

None. DC2 harness is HELD (not blocked) at the CTO pre-apply RAVC gate -- a downstream gate I haven't reached yet (verify-after + comp-iam + -target plan remain before it). BD-P1 is not my lane (0.6.0).

## Current State (handoff)

- **deploy_ledger fix LIVE** (c66b397d1, pushed): `.tools/deploy_ledger.py` -- `--lambda <fn>` opens a single `tf-lambda` leg; `_lambda_leg()` resolves tf_resource from infra/aws/lambda/ci/lambda-source-map.json (keyed under `functions`). Use `--lambda` (not `--pipeline`) for single-Lambda TF deploys. Brief docs/briefs/deploy-ledger-phantom-leg-gap-20260625.md (STATUS: FIXED).
- **DC2 harness ~80% built, TF-VALIDATES, HELD at the CTO pre-apply gate:**
  - infra/aws/terraform/crawl-harness/dc2-test1-offpeak-harness.ssm.yaml (7a91c00a2) -- the Automation 7-step flow: precheck-ABORT -> start crawl-instance -> wait-online -> runParker(dc2-parker-run on inf-exporter i-081ae6aafb394fb1a) -> runCrawlCaptureVerify(dc2-crawl-run on crawl i-010f195f1798b40ad) -> GUARANTEED stopCrawlInstanceAlways (Force, onFailure target of every step). Param-defaults pin the 3 constants.
  - infra/aws/terraform/crawl-harness/dc2-test1-harness.tf (b7502e0b0) -- 2 dedicated fixed-command SSM docs + Automation doc + scoped orchestrator IAM (SendCommand only the 2 docs+2 instances; ec2:Start/Stop crawl-ARN-ONLY, ZERO serving-ARN; Describe crawl-tag-scoped) + DISABLED off-peak EventBridge schedule (cron placeholder -- pin to inf-exporter baseline at finish) + EventBridge-invoke role. Diagnostic-scoped + teardown-trigger documented inline.
  - infra/aws/ec2/crawl-harness/src/dc2-test1-capture.ts (ee6f2df7a) -- observe-only render classifier: parses the tee'd crawl stdout for the CrawlReport (crawl.ts:50, endpointsCataloged) -> FULL(>0)/SHELL(0)/UNKNOWN + crawl_start_ts -> writes s3://opal-crawl-catalog/eclipse/diagnostics/test1-{date}.json (NO token values; no shell-passthrough). park_complete_ts read from the Automation execution log at RAVC.
- **Eclipse parked state**: s3://opal-data-inf/eclipse/browser-profile/state.json (auth in cookies eclipse.access_token + localStorage sm.access_token @ api.cloud.orionadvisor.com -- NOT sessionStorage). Crawl entrypoint runEclipseCrawlLive (crawl.ts:297); minimal read-screens run-eclipse-crawl.ts (double-opt-in liveGateAck + DC04_LIVE_CRAWL_AUTHORIZED=1). Both instances STOPPED.
- **BD-P1 (NOT mine):** 0.6.0_AE_PartnerETL owns ADVI_BDAPIMIG.P1 (TO c7a3e0b2d); landed (A) keepalive (ec11fad19, tag bd-v2.33.0); cookie auto-extends. CVO pulls me as (A)+(C) warm-fallback ONLY if 0.6.0 stalls (it didn't).

## Next Steps

- **[0.7.0_AE_CloudOps]** Finish DC2 harness (deliberate pace): (1) dc2-test1-verify-after.ts -- the 212001Z prove-not-burn check (reuse loadParkedSessionReadOnly crawl.ts:136 + iso.preflight serving-clean gate for a read-only Orion probe; sets serving_intact); (2) `comp-iam gaps` on dc2-test1-orchestrator-role (prove the doc-condition + zero serving-ARN start/stop); (3) comp-blast / `-target` add-only plan (0 destroy/0 replace, instance untouched); (4) RAVC the comp-iam proof + add-only plan to CTO (the pre-apply gate); (5) on GO: enable the schedule, off-peak run, RAVC the render+timing artifact next morning -> picks the #1->#2->#3 branch.
- **[1.0.0_SA_CTO]** pre-apply RAVC gate for DC2 (confirmed ready) -- comp-iam doc-condition proof + -target add-only plan.
- **[3.0.0_SA_CVO]** DC2 graduation-gated structural review IF the harness goes diagnostic->permanent (build-to-bar: live-applied condition / no shell-passthrough / teardown-executes); BD-P1 verify (0.6.0's legs).
- **[2.0.0_SA_COO]** P2-2 still sequence-gated behind NFRA_DEBTSCAN.TO-D3 (the scorer FILL -- register Python tool + CVO AC4); COTETL legs held (BD-adjacent); smartx reconcile held.
