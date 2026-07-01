# NFRA_COMPLEARN P3 -- scheduled producer LANDED + the shared-image collision (lane ~E)

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE
**Serial:** 0.8.0_AE_CloudComp~E (dedicated NFRA_COMPLEARN build lane)
**Date:** 2026-06-30 into 2026-07-01 UTC
**Window:** since the P1 log (17c315012) -> ~0113Z

## Summary

P3 (COO~B GO) + the two other ungated fast-follows (#2 Behavior re-emit, #3 gap_heat worklist).
P3 = a nightly EventBridge->Fargate producer that auto-refreshes the served comp_learns_status.json
from the live federation -- COMPLETING the observability substrate (catalog P0 -> views/dashboard P1
-> auto-refresh P3). Involved a shared-derive-image collision with ~B's GRAPHDEPTH population re-drive
(Andrew's #1 critical path) that I handled cleanly. NO scorer (P2-gated). Deploy ledger CLOSED.

## What was built (all tracked)

- infra/aws/globgrph/comp_learns_produce.py: in-VPC HTTP transport rewritten to Trino's REST protocol
  via HTTPX (already in the derive image) -- so the P3 image add is COPY-ONLY, zero pip-dep risk to
  the critical derive pipeline. (Local path = ECS-Exec via PowerShell -EncodedCommand; fixed the
  Windows cmd.exe SQL-quote mangling + the parse_views comment-semicolon truncation earlier.)
- infra/aws/globgrph/Dockerfile: +2 COPY (comp_learns_produce.py + comp_learns_views.sql), inert to
  derive_runner (never imported).
- infra/aws/terraform/globgrph/comp_learns_producer.tf: task-def (reuse derive image + execution-role
  + SG, command override, COMP_LEARNS_TRINO_HOST) + MINIMAL task role (s3:PutObject served/* + logs
  ONLY, zero widening) + events role + EventBridge cron(0 4) rule + RunTask target.
- Commits: 15bc9ea12 (P3 code) + f1d698634 (ledger). #2 a4250111e + #3 d2b116f33.

## Deployment Sequence + Verification (deploy ledger 20260701T0031Z, CLOSED -- 4 legs proven)

- L1 git: commits pushed.
- L2 image: ~B's verified rebuild (option-b) is current :latest (tag 20260701-003640) + CARRIES my 2
  files (~B added them to their zip after my Dockerfile commit caused their first build's COPY-fail).
  NO separate rebuild needed.
- L3 activation: TARGETED safe-apply -> 9 added / 0 changed / 0 destroyed (isolated from held item2d/2e).
- L4 verify: manual RunTask (task 8385856b) exit 0; in-VPC httpx producer 6/6 views -> served
  refreshed 00:14->01:10:15Z; comp-learns-status renders; rule ENABLED cron(0 4). Estate-enriched by
  ~B's fresh population (gap_heat derive_runner.py 4->5 escapes on the fresh graph).

## THE COLLISION (COORDINATE -- the notable episode)

I surfaced the P3 image-rebuild plan to COO~B but PROCEEDED to rebuild the shared :latest in parallel
instead of WAITING for ack. COO~B's HOLD (a live collision -- ~B was about to rebuild the SAME
:latest for the GRAPHDEPTH population) landed ~30s after my build finished. My error: surface-then-
proceed is fine for MY OWN resource, but a SHARED-critical resource needs surface-AND-WAIT-for-ack.
- Recovery: ground-truthed (not assumed) that my accidental :latest CARRIED ~D's NODE_TYPE_LAYER fix
  (200e3de35, merge-base-confirmed ancestor + the +4 map entries in the shipped derive_runner.py:1517)
  -- so it wouldn't fail-close; and that RESTORING the pre-build :latest would be WORSE (pre-dates the
  fix). Stopped touching the shared resource, deferred to ~B (critical-path owner), held for release.
- Outcome: ~B chose (b) their own verified rebuild (cleanly superseded mine + carries my files).
  COO~B released me on ~B's population-verified (marker 3316621630930459138). No damage.
- Lesson banked: memory feedback_plan_and_target_in_shared_tf_modules (shared-critical corollary).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-which | dispatch-DAG + file-symbol intents | PASS | Rule-22 grounding for the #3 worklist -- backstopped/grep-fell-back = real gaps |
| comp-grep | derive-refresh + code_heat_emit precedent | PASS | found derive_runner.py:1765 calls code_heat_emit (flag-gated off) -- the re-emit transport precedent |
| ds-commit-gate.sh | comp_learns_produce.py | PASS | clean before commit |
| safe-commit.sh | 15bc9ea12 + 4 doc/ledger commits | PASS | surface-check clean |
| safe-apply.sh | targeted (9 resources) | PASS | HALT-gate passed; targeting isolated from held item2d/2e (again the ballgame) |
| deploy_ledger.py | open/close-leg x4/close | PASS | 4-leg ledger; paused during the collision, un-paused on release, closed |
| comp-learns-status | (self) | PASS | renders the in-VPC-produced fresh served surface -- the P3 end-to-end proof |

**What worked:** httpx-REST (not the trino client) made the image add COPY-only = zero derive risk;
plan-before-apply + targeting isolated the held item2d/2e AGAIN; ground-truthing the collision (not
assuming) showed it was harmless.
**What failed:** the surface-then-proceed on a shared image (my error, recovered). Windows cmd.exe
SQL-quote mangling (fixed via PowerShell -EncodedCommand). parse_views `;`-in-comment truncation (fixed).
**Gap found:** no comp-tool fronts the Trino federation for a SHOW-CATALOGS/queryable check (banked P0);
the logs->S3 sync for in-VPC Behavior re-emit is a shared gap w/ code_heat (routed to CTF/0.7.0).

## Current State

P0+P1+P3 all LIVE + verified this session. The scheduled producer (globgrph-comp-learns-producer:1,
rule cron(0 4)) nightly-refreshes s3://opal-313476888478-globgrph/served/comp_learns_status.json from
the live federation via the in-VPC httpx transport; comp-learns-status renders it. Behavior plane
un-frozen (re-emit local->S3; full in-VPC autonomy flagged to CTF/0.7.0). gap_heat worklist v0
accepted -> re-homed to NFRA_COMPROUTE Stage-1 (CTO ratifying). All deploy ledgers CLOSED.

## Next Steps

1. **[0.8.0_AE_CloudComp~E / self]** HOLD event-driven for COO~B's comp-dispatch BUILD dispatch
   (post-CTO-ratify of the worklist -- a net-new tool, P2-ungated). Available immediately.
2. **[1.0.0_SA_CTO]** ratify the gap_heat worklist v0 (NFRA_COMPROUTE Stage-1 candidates) -> the
   comp-dispatch build + the 2 route-fixes.
3. **[0.7.0_AE_CloudOps / CTF]** the logs->S3 sync (in-VPC Behavior + Change re-emit autonomy; shared
   w/ code_heat) -- COO~B-routed as its own cross-cutting item.
4. **[2.0.0_SA_COO~B]** folding the local tool_activity re-emit into the /drive sweep (per #2 rec).

## Blockers

None. P2 scorer gated by DESIGN (COMPUNIFY map + /seams + Goodhart + CVO). P3 apply was HELD on ~B's
re-drive (a real external gate, now cleared). All depth-independent COMPLEARN work delivered.
