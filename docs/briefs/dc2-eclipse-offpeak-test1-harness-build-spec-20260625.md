# DC2-Eclipse test #1 -- autonomous off-peak harness BUILD SPEC (CTO (a)-APPROVED 142152Z)

**2026-06-25, 0.7.0_AE_CloudOps (DC2 lead).** CTO arch-ruling: option (a) autonomous off-peak
harness APPROVED; (c) peak-login REJECTED (isolation 212001Z binds); (b) piggyback REJECTED.
This spec is the build design; the RUN is off-peak only. Diagnostic/decision-tree: brief 3dede104a.

## Test #1 (the discriminator -- single run, no TTL-bracketing)

CTO discriminator: we already KNOW the production (delayed) crawl renders SHELL-only. So a single
PARK -> IMMEDIATE-crawl is the whole test:
- immediate render = FULL data  => TOKEN-EXPIRY CONFIRMED (production park->crawl delay rides
  expired eclipse/sm.access_token). Fix = crawl-within-TTL or pre-crawl refresh. #2/#3 ruled out.
- immediate render = SHELL       => expiry RULED OUT -> proceed to #2 (cross-origin localStorage).

## Existing pieces (orchestrate, don't rebuild)

- PARKER: `infra/aws/ec2/inf-exporter/src/stepwise/eclipse_session_parker.ts` -- runs on inf-exporter
  box i-081ae6aafb394fb1a (login/creds live there; OFF the crawl box). Writes
  s3://opal-data-inf/eclipse/browser-profile/state.json (authed). Evaluate-free.
- CRAWL: `infra/aws/ec2/crawl-harness/src/run-eclipse-crawl.ts` -> `runEclipseCrawlLive` (crawl.ts:297).
  Read screens only [dashboard, portfolios, models, accounts]; double-opt-in liveGateAck:true +
  DC04_LIVE_CRAWL_AUTHORIZED=1; runs on crawl-instance i-010f195f1798b40ad (STOPPED). The CrawlReport
  already carries the FORK-B authed-vs-shell signal (authed /v1 XHR data captured vs shell render).

## Orchestration (the harness = a thin cross-box sequencer; NEW)

A single off-peak orchestration (SSM-driven, no new login surface on the crawl box):
1. PRECHECK: confirm OFF-PEAK + no concurrent Orion crawl (read the nightly-login window marker /
   exporter schedule); ABORT if peak or a serving crawl is active. (constraint 1)
2. PARK: trigger the parker on inf-exporter (its existing off-peak path); record park_complete_ts
   when state.json is freshly written. FAIL-LOUD if OTP/login fails (parker already does).
3. IMMEDIATE CRAWL: start crawl-instance, run run-eclipse-crawl (the existing minimal read-screen
   observe-only crawl) within the tightest feasible delta; record crawl_start_ts. (constraint 2:
   single park->immediate-crawl, match-baseline shape, no probe storm.)
4. CAPTURE (observe-only, constraint 3): derive FULL-vs-SHELL from the CrawlReport (authed /v1 data
   present vs shell render) + write {render_outcome, park_complete_ts, crawl_start_ts, delta_s} to
   an artifact: s3://opal-data-inf/eclipse/diagnostics/test1-{date}.json. NO token VALUES (presence/
   status only).
5. AUTO-STOP (constraint 4): stop crawl-instance after the single run. NO overnight watcher agent --
   the artifact is reviewed NEXT MORNING (banked rule).
6. VERIFY-AFTER (constraint 5): confirm the production Orion serving crawl still rides clean after the
   test park (re-park its state if Orion single-session bumped it -- bounded/recoverable per 212001Z);
   record serving_intact:true/false in the artifact.
7. RE-GATE (constraint 6): the harness does EXACTLY the single observe-only park->immediate-crawl;
   anything more returns to CTO.

## Scheduling

- EventBridge SCHEDULE in the OFF-PEAK window (after the nightly-login window; cron TBD vs the
  exporter baseline -- match it, do not add a distinct cadence). ONE fire. The harness self-aborts if
  precheck (step 1) finds peak/concurrent-crawl.
- Deploy via the normal cycle (code -> S3 -> EC2 pull -> SSM; Rule 12). Crawl-instance stays STOPPED
  except the single scheduled run.

## Open sequencing (drivers' call)
- CTO: build+deploy today so it runs tonight (RAVC artifact next AM) vs a careful build that may slip
  one off-peak window (acceptable -- not an emergency; /v1 capture has been pending since 06-24).
- COO: harness-build-now vs the NFRA_TSGRAPH P2-2 reroute (non-gated). Flagged the cross (CTO ruling
  post-dated the reroute). Awaiting the sequence call; this spec makes the build instant-start.
