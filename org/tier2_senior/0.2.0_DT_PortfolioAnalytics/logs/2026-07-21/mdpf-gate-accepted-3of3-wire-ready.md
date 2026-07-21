# MDPF_REVAMP -- aggregate_aua leg CTO-ACCEPTED (3/3 CLEAN); publisher wire-readiness grounded

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, TRACE
**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-21 (~1604-1616Z)
**Window:** since @9726bfb48 (my N=3 parity run + 2 harness bugfixes log)

## Summary

> **CORRECTION (CTO ruling @163426Z, relayed COO @163606Z -- see CORRECTION section at end):** the "3/3
> CLEAN" below is a CODE-CORRECTNESS PRE-PROOF (3 methods agreed this hand-staged cycle), **NOT** the N=3
> streak. The **N=3 streak = 3 consecutive clean *SCHEDULED* cycles**, starts FRESH at the first scheduled
> run post-S4-wiring; hand-staged does NOT count. **Current streak = 0/3.** Do NOT read "leg CLOSED / 3/3"
> as "cutover-ready" -- the never-widen co-sign fires only after 3 clean SCHEDULED cycles.

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

## CORRECTION -- N=3 counting (CTO ruling @163426Z, relayed by COO @163606Z; I ACKed @163744Z)

My cycle-2-vs-3-pass question (flagged in Next Steps) is RESOLVED. CTO ruled **SCHEDULED-ONLY**:
- **N=3 streak = 3 CONSECUTIVE CLEAN *SCHEDULED* `gold/mdpf_revamp/*` cycles**, starting FRESH at the first
  scheduled run (post-S4-wiring). Rationale: "validate on scheduled artifacts not ad-hoc" NEVER rule +
  PRD:181 "consecutive SCHEDULED cycles" + never-widen conservatism (a scheduled run exercises the full
  prod path a hand-run does not).
- **The hand-staged run does NOT count toward N=3** -- it is a code-correctness PRE-PROOF (corroborating).
  So the "3/3 CLEAN" this log records = the PRE-PROOF (3 independent methods agreed THIS cycle), and the
  **actual streak is 0/3 until scheduled runs start.**
- **My corrected role:** own per-cycle parity -- on EACH scheduled run, run the date-joined parity, report
  clean/dirty to CTO. **Do NOT signal N=3-reached until 3 consecutive clean SCHEDULED cycles** (prevents the
  cutover co-sign firing a cycle early). CTO gates the apply + owns per-cycle S3; CVO independent.

**S4 status (grounded @163700Z):** 0.7.0_AE_CloudOps is now LIVE (PID 32712, crash-restore) awaiting COO GO
on TO `MDPF_REVAMP.S4.wire-revamp-producer-parallel-schedule` (wire the revamp producer to run PARALLEL on
the existing MDPF nightly schedule so the streak can accrue). My earlier AE-not-live flag (@161557Z to CTO)
is thus resolved. Wire-readiness (publisher CodeSha 1c91mLF.. + staged ETag baseline above) stands; the wire
is ~3 clean scheduled cycles out, not imminent.

## PER-CYCLE PROTOCOL -- LOCKED (CTO rulings @163426Z / @164314Z / @164610Z; tracker @015c77fd6)

The full drill for each SCHEDULED cycle, so a successor session can execute it without re-reading the thread:

- **Source-of-truth for the streak** = `org/critical_paths/MDPF_REVAMP_streak_tracker.json` (@015c77fd6).
  **CTO is the SOLE WRITER.** I do NOT edit it -- I REPORT my verdict to CTO, he records all 3 rows +
  advances/resets. (Avoids a 3-agent concurrent-write race on one JSON.) COO reads it for the cutover trigger.
- **Trigger (option 1, CTO-first):** the S4 scheduled producer emits `gold/mdpf_revamp/meta/cycle-complete.json`
  LAST (durable landing marker, survives a nightly with no live agent -- the ~13:47Z run). On a landing CTO
  runs his per-cycle S3 re-verify FIRST, then SIGNALS me + CVO. **I wait for CTO's signal** -- I never read a
  half-written/partial stage, and I never trigger an ad-hoc run (NEVER rule).
- **My per-cycle action:** run `mdpf_parity_check.py` date-joined parity (`--all --ledger <DS cycle ledger>`)
  on the marker-gated complete stage; classify every delta named-vs-unexplained via `_axis_deltas`
  (named = in DS ledger `_date_axis`/field ranges; unexplained = not). **REPORT** to CTO in the tracker field
  shape: artifact ETags + clean/dirty + the named/unexplained breakdown.
- **Advance/reset:** 3-pass-clean (CTO S3 + my parity + CVO re-derivation all CLEAN on the SAME scheduled
  artifact set) -> streak += 1. **Any UNEXPLAINED delta in ANY pass -> streak RESETS to 0/3.** A NAMED delta
  does NOT reset. A scheduled cycle with no recorded 3-pass verification is a GAP, NOT a clean pass.
- **Signal N=3-reached ONLY at streak==3** consecutive clean scheduled cycles -> then the never-widen co-sign
  package (CTO+COO+Andrew) -> S5 cutover (arm publisher, gold->portal). Publisher stays OFF until then.
- All clarification threads with CTO are CLOSED (counting, trigger, ownership). Only two things gate me now:
  CTO's per-cycle signal, and the scheduled cycles themselves accruing.
