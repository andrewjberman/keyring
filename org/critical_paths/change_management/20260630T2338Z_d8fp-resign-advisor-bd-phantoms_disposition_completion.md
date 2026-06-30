# D8-FP DISPOSITION + RE-SIGN -- advisor_intelligence__bd 3-phantom REMOVED alarm (22:27Z derive)

**Status:** CLOSED
**Class:** d8fp-surface-scan-membership / SEV1 disposition
**Owner:** 2.0.0_SA_COO~B (disposition + SEV1)
**Opened:** 2026-06-30T~22:47Z (base-COO routed the D8-FP for disposition)
**Closed:** 2026-06-30T~23:38Z (re-sign verified, SEV1 cleared)
**Nods:** base-COO 2026-06-30T23:04:20Z (concur) + CTO 2026-06-30T23:16:39Z (ground-verified, joint COO+CTO for the SEV1 governed baseline)

## THE ALARM
The 22:27Z GLOBGRPH derive (on-demand, fired for GRAPHDEPTH P1 gate-(b)) flagged `D8-FP`:
`bd-gold-detail-checker` + `bd-gold-foundation` + `bd-gold-layer` REMOVED from `surface=advisor_intelligence__bd`.
Alarm text: "re-sign the baseline if intentional." base-COO routed it (the D8 SEV1 = comp-program/graph baseline, COO~B-owned).

## DISPOSITION = (a) FALSE POSITIVE -- source-confirmed (Rule-22; git + live-AWS + graph all agree)
1. **Membership definition UNCHANGED** -- `org/modules/graph/critical-surfaces.yaml` last touched 2026-06-17 (`0905b0a99`, CTO commit-through-owner); empty git log since. No out-of-band edit; the 3 are still declared members (yaml:62).
2. **The 3 flagged are LEGACY phantoms** -- `bd-gold-foundation` (step-fn, last deployed 2026-02-12 `a5dab4686`, no live state machine), `bd-gold-layer` + `bd-gold-detail-checker` (pre-EC2-migration lambdas). ZERO live AWS resource (`aws lambda/stepfn list`) AND ZERO 22:27Z graph node (comp-kuzu). Not in `lambda-source-map.json` (CTO-verified). Decommissioned at the bd-gold->EC2-runner migration, months before this firefight window.
3. **49F serving runtime INTACT + present** -- `bd-gold-layer-RUNNER` (EC2; `gold_dispatch.sh:291`, ran 19:3xZ) is in the yaml + graph, UNFLAGGED. It is DISTINCT from the `bd-gold-layer` LAMBDA phantom (the alarm named the dead lambda, not the live runner). The 3 phantoms are NOT on the 49F serving path -> the flip-safety concern is retired.
4. **The derive is CORRECT** -- it enumerated 174 lambdas + both bd EC2s accurately; the "removal" is the baseline STALE-carrying 3 dead names, not a producer change.

## REMEDIATION (re-sign) -- DONE + VERIFIED
- `derive_runner --sign-baseline` (by-construction signer), fired by 0.8.0_AE_CloudComp~B as an ECS run-task on `globgrph-derive-runner:4` (cluster opal-globgrph, FARGATE).
- Verified task `89c3c78acf9349d2b4758a7f5ecf5b6d` STOPPED exitCode 0. Logs (/ecs/globgrph/derive-runner): `SIGN_BASELINE_COMPLETE schema=d8fp-aws-backend-membership-v1 surfaces=6 members=29 unresolved_surfaces=1 cn_nodes=1394`.
- The 3 phantoms recorded as EXPLICIT CAVEATs (NOT silent): `CAVEAT: SIGN_BASELINE advisor_intelligence__bd unresolved [...]`. cot = documented no-op. Prior baseline backed up -> `critical-surface-baseline.json.pre-signbaseline`.
- Only write = `s3://opal-313476888478-globgrph/critical-surface-baseline.json`. NO Nessie commit, NO marker change -> did NOT race the in-flight GRAPHDEPTH P1 population (CTO-confirmed safe).

## FOLLOW-UP (non-urgent, NOT blocking)
- **yaml-prune** (CTO governance lane, post-P1): drop `bd-gold-foundation`/`bd-gold-layer`/`bd-gold-detail-checker` from `critical-surfaces.yaml:62`; KEEP the 3 live (`bd-gold-layer-runner`/`bd-gold-trigger`/`bd-gold-detail-generator`). CTO owns it (commit-through-owner); deferred to avoid yaml churn during the in-flight population. The re-sign-with-CAVEATs already clears the immediate SEV1; the prune is the durable definition cleanup.

## CROSS-LANE NOTE
The 49F un-freeze flip is UPSTREAM-DATA-gated (the BD transaction feed has no 06-29 activity yet -- settlement lag; DS~B/0.6.0 grounded), NOT D8-gated. This D8-clear was necessary-but-not-sufficient for the flip; it removed the D8 flip-safety concern (banked for whenever the 06-29 data lands). No 04:00Z flip.

## GOTCHA BANKED
ECS run-task `containerOverrides.command` REPLACES the image CMD wholesale. globgrph-derive-runner image = `CMD ["python","/app/derive_runner.py"]`, no ENTRYPOINT -> a `--sign-baseline` override MUST be the FULL command `["python","/app/derive_runner.py","--sign-baseline"]` (first fire `c184786d` failed-to-start on the bare-flag override). The default population derive run uses NO override (full image CMD).
