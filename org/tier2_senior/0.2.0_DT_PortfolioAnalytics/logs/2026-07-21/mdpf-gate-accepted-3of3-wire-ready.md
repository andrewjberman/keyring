# MDPF_REVAMP -- aggregate_aua leg CTO-ACCEPTED (3/3 CLEAN); publisher wire-readiness grounded

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, TRACE
**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-21 (~1604-1616Z)
**Window:** since @9726bfb48 (my N=3 parity run + 2 harness bugfixes log)

## Summary

Post-`/clear` resume of the same crash-recovery session (SID f0c84ef1..., PID 25952 -- context-clear,
NOT a new spawn; existing Monitor `bgh3zh9bm` is mine and streaming). Startup re-run clean. Consumed
CTO's gate verdict: **aggregate_aua N=3 = 3/3 CLEAN, my independent date-joined parity ACCEPTED** vs the
FINAL ledger 6026af46a. Closed both RAVC loops (CTO gate + DS re-pull), grounded the held pre-cutover
publisher + staged-gold ETag baseline so the wire-time router-ARN confirmation is instant, and surfaced
two wire dependencies (AE not live + the co-sign; CVO cycle-2 vs 3-pass question).

## What happened

1. **Startup (crash-recovery resume).** register_agent (PID 25952, idempotent update) -> serial file
   written -> owned-paths hook present -> comp-graph context set -> audit-archive-invoker ran (non-exec:
   benign LIVENESS/STALE-BASELINE finding, snapshot deferred to an exec startup, non-blocking). Watcher:
   NOT re-armed -- Monitor `bgh3zh9bm` from pre-clear is the same session's live watcher (liveness PID ==
   my PID confirms MINE-and-ALIVE; DO-NOT-KILL per XXX.md).
2. **Gate verdict consumed.** CTO 160853Z: my parity ACCEPTED (NAMED_DELTA_PASS all 3, 0 unexplained,
   both harness bugfixes @e17a28141 clean w/ regression self-tests). item-3 (non_model band covers D-2+F2)
   confirmed. A4 455-axis 3rd-pass DECLINED for now (2 passes + spine coverage), held-available for cutover
   co-sign. KEEP aum_timeseries/aum_metrics rows (TO-2 later wave; PUBLISHED_ABSENT != fail).
3. **RAVC closes.** (a) CTO 161557Z -- ACK + wire-readiness + 2 deps surfaced. (b) DS 161604Z -- re-pull
   satisfied: my ACCEPTED run already used FINAL ledger 6026af46a (e3b2c8f6b was only the PRIMED pass).
4. **Wire-readiness grounding** (see Current State).

## Current State (zero-context handoff)

**My aggregate_aua leg: CLOSED + CTO-accepted (3/3 CLEAN).** No open action on me. The gold->portal cutover
is co-sign-gated (Andrew never-widen) + AE-lane; not mine to force.

**Held pre-cutover publisher (= "mdpf-data-router" in the handoff):**
- Function: `opal-assets-mdpf-portal-publisher`
- ARN: `arn:aws:lambda:us-east-1:313476888478:function:opal-assets-mdpf-portal-publisher`
- CodeSha256: `1c91mLFHQxUDhZdG7gUuL3ezW5ZCNcL5OH8yvCdcMsU=`  | LastModified 2026-07-20T21:25:59Z
- Env: `ASSETS_BUCKET=opal-data-assets`, `STAGING_ROOT=gold/mdpf_revamp` (reads the EXACT staged prefix
  I verified; not yet pointed at portal output = confirmed held state).
- **Only `$LATEST` exists; NO numbered published version.** WIRE CONFIRMATION = at the co-signed cutover,
  verify the numbered version AE publish-version's carries this exact CodeSha + STAGING_ROOT.

**Staged-gold ETag baseline (opal-data-assets, my wire baseline -- publisher must publish from these
UNCHANGED, else re-verify parity first):**
| Key (gold/mdpf_revamp/) | ETag | Size | Modified |
|---|---|---|---|
| 49financial/aggregate_aua_timeseries.json | 6e072745ad79f431fc9d9003485e333b | 152815 | 2026-07-21T15:46:02Z |
| inflection/aggregate_aua_timeseries.json  | a9778de44b393940788db56707b52c11 | 126188 | 2026-07-21T15:46:05Z |
| global/aggregate_aua_timeseries.json      | 7d574a2d1662b92daf9b4baea7e53209 | 165549 | 2026-07-21T15:46:07Z |
| global/non_model_assets.json (A4)         | d4802341934a7e68203f6f83d1b80102 | 82101  | 2026-07-21T15:55:48Z |

(The 3 "firms" = 49financial, inflection, global[enterprise aggregate]. account_distribution.json x3 =
CVO-owned leg, clean.) All single-part ETags.

**Other threads:** OPAL_TAXSMA_PT2 WS-2/3/4 PARKED behind MDPF P0 (CTO 07-20 sequence-call); WS-1 closed
@c67398701. A4 3rd-pass held-available.

## Blockers

None (no assumption-BLOCKED). The cutover is gated on external conditions I do not control: (1) Andrew
never-widen co-sign (not yet issued), (2) 0.7.0_AE_CloudOps not currently registered/live (holds the
cutover pkg). Both surfaced to CTO (CC-noted for COO spawn-routing) -- not blocking me now; my leg is done.

## Next Steps

- [0.2.0_DT] AT THE CO-SIGNED CUTOVER: confirm the numbered publisher version ARN carries CodeSha
  1c91mLF.. + STAGING_ROOT=gold/mdpf_revamp, and the staged ETags above are unchanged (else re-verify
  parity on the re-staged set first). Hold A4 455-axis parity available if the co-sign wants extra assurance.
- [1.0.0_SA_CTO] owns the publish trigger + the gate; clarify cutover gate = this-cycle 3/3 + co-sign vs
  a 3-scheduled-run streak (CVO reads "cycle 1 of N=3, holding for cycle 2"). Route AE spawn when co-sign nears.
- [0.7.0_AE_CloudOps] (when live + co-signed): apply router lambda + 9 behaviors + OAC origin + emitter
  source-repoint.
- Else: event-driven, reachable.

## MCP traffic

3 handled. IN: CTO gate verdict (160853Z), DS re-pull ACK. OUT: 2 RAVC closes (CTO 161557Z ACK+deps, DS
161604Z re-pull-closed). Summary updated.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `aws lambda list-functions/get-function-configuration/list-versions-by-function` (`# rail-checked`) | PASS | Found real publisher `opal-assets-mdpf-portal-publisher`; got ARN+CodeSha+env+versions. `mdpf-data-router` name does not exist (as expected -- router is in the held cutover pkg). |
| `aws s3api list-objects-v2` (operational, LISTING = acceptance instrument) | PASS | Staged-gold ETag baseline for gold/mdpf_revamp/ (4 wire-relevant artifacts). |

**What worked:** the live lambda + S3 primitives answered the wire-readiness questions exactly (version
ARN, CodeSha, env target, staged ETags).
**What failed:** nothing.
**Gap found:** none new.
**Why not comp-*:** this window was grounding/coordination only -- no code/script edit, no deploy, no new
boto3 call -- so DT role-minimums (`comp-pipescript io`/`comp-iam service`) do not apply. The two questions
asked (a lambda's published-version ARN/CodeSha; live S3 ETags) are live-primitive questions no comp-tool
maps; both raw `aws` inspections carried inline `# rail-checked:` markers per the COMPRAIL exception.
