# 0.6.2_AE_PartnerETL -- OPAL_ASSETS C3(c): Andrew's "daily REST pattern for both 0833 and 0824" made live infrastructure

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE, COORDINATE
**Date:** 2026-07-14 | **Window:** ~03:19Z -> 04:11Z (since log eacf54ceb) | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Andrew asked directly whether we had a daily ETL pattern on the 0833 account on the Schwab box. Grounded the
answer on live state (**no** -- 0833 was a one-time backfill; the box's only live schedule was the dead
0824-GUI channel), flagged the silent-freeze risk, and offered to stand it up. Andrew: **"Yes we definitely
need to proceed through ETL" / "DO it"** and then, via COO, the scope: **"We need daily rest pattern for both
0833 and 0824 on that box, yes."**

Built and shipped it to LIVE INFRASTRUCTURE in ~25 minutes end to end: both daily REST schedules are applied,
ENABLED, and staggered; the puller retargets to the monolith; a box-wide SDD **session lock** (CTO design
requirement) makes the shared-session contention safe by construction; and a silent manifest-write failure
was caught and fixed before this new producer ever ran.

## Work done

### 1. Grounded the "is there a daily pattern?" question (no assumption)
Live checks: the SI2 daily schedule's SSM command is hardcoded to the **0824** delivery folder and drives the
dead GUI task; no EventBridge Scheduler rule names 0833; 0833 freshness (07-10) is a snapshot of the backfill,
not a feeder. Answer: no daily ETL on 0833, and it silently freezes on the next posted trading day until
C3(c) exists. Offered the reorder; did NOT self-authorize it off the sovereign lift (two-step inference).

### 2. C3(b) puller retarget + the SDD session lock (7f31489d2)
`sdd-daily-pull.ps1`: added `-Target monolith|staging` (monolith default; staging kept as an explicit escape
hatch for the in-flight 0824 wide pull -- you do not repoint a running producer). Added the **session lock**:
the SDD credential is a single-point-of-freshness shared across both masters, so the puller acquires a
box-wide atomic lockfile before touching the session and **REFUSES to start (loud, pages, exit 7) if a live
sibling holds it**; stale-safe (dead-pid or >2h reclaims). CTO ruled this a design requirement, not a flag --
"the guard has to be right BEFORE the failure." Also rc-checked the manifest cp (was `--only-show-errors` +
no check = silent AccessDeny, the exact dead-channel shape) -> WARNs loudly, does not fail the pull.

### 3. C3(c) CREATE-NEW schedules, both masters (7f31489d2 -> 0d8607926)
New EventBridge schedules (CTO ruled CREATE-NEW 030017Z; no repoint -- the dead GUI schedule stays untouched).
for_each over both masters + a shared events-ssm role; each fires SSM RunPowerShellScript on the SI2 box ->
pulls the puller from S3 _ops (Rule 12) -> runs `-Master <m> -Target monolith`. Staggered 30 min (0833 cron
45 9,21; 0824 cron 15 10,22 UTC); the lock, not the stagger, is the guarantee. SendCommand IAM scoped to the
one document + one instance.

### 4. The _ops grant + the gate discipline
Caught tracing the box role vs what the puller writes: the manifest lands under schwab/{master}/_ops/ but
MonolithSchwabWrite only covered bronze/* -> AccessDeny. Added `MonolithSchwabOpsWrite` (PutObject on
schwab/{master}/_ops/*, masters enumerated). CTO GO'd the 0833-only 4/1/0 plan; my both-masters 6/1/0 update
crossed it in flight -> I HELD (a gate GO on plan A does not stretch to plan B) and confirmed lineage while
COO routed a re-gate. Re-gate GO -> applied.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `terraform validate`/`plan` | schedule + _ops IAM, plan-only then apply | PASS -- 6 add/1 change/0 destroy; 0-diff after apply |
| `.tools/safe-apply.sh` | apply the schedules (HALTGT) | PASS -- 6 added, both rules ENABLED |
| `aws iam simulate-principal-policy` | 22a exercise of the new _ops grant | PASS -- enumerated masters allowed, 99999999 implicitDeny (enumeration holds) |
| `aws events describe-rule` | confirm both rules live + ENABLED | PASS -- 0833 cron(45 9,21), 0824 cron(15 10,22) |
| `.tools/commit-gate.sh` | Rule 14 on the .py | PASS |
| PowerShell parser | puller after lock + manifest + retarget edits | PASS -- 441 lines clean |
| `aws s3 cp`/`head-object` | re-upload puller to S3 _ops, byte-verify | PASS -- FIRST attempt AccessDenied on the missing --sse header (the opal-data-schwab forced-SSE footgun, caught by the byte-count check); --sse AES256 fixed it; final 27,198 bytes byte-identical |
| `comp-glob`/`grep` | search for the Schwab FAM/SLM record layout (DS's W4 ask) | PASS -- NONE in-repo; routed as a clean Andrew ask |

**What worked:** the byte-count upload verify caught a silent-looking AccessDenied; the 22a negative control
proved the _ops enumeration did not leak.
**What failed:** first S3 upload AccessDenied (missing --sse AES256 on the forced-SSE bucket -- my own
documented footgun, bitten and caught).
**Gap found:** the Schwab SDD FAM/SLM record layout is not in-repo -- clean Andrew ask (DS needs it to name
the Group-A advisor-role columns; guessing is the confidently-wrong-label trap).

## Deployment Sequence + Verification (AE)

```
CODE     sdd-daily-pull.ps1 (retarget + session lock + manifest rc-check) -> S3 _ops, byte-verified 27,198=27,198
IAM      monolith-iam.tf +MonolithSchwabOpsWrite -> part of the apply
SCHEDULE monolith-daily-schedule.tf (for_each both masters, shared role) -> safe-apply 6 add/1 change/0 destroy
VERIFY   0-diff "No changes"; both rules ENABLED (live describe-rule); _ops grant exercised (allow/allow/implicitDeny)
TAG      schwab-si2-iam-v1.3.0 (pushed --follow-tags)
```
**LIVE (ground truth):** `canonical-schwab-si2-08335338-daily-pull` + `canonical-schwab-si2-08242234-daily-pull`
both ENABLED. First fire 09:45 UTC (0833) -- 5h clock margin over the 0824 wide-pull ETA (~06:00 UTC), so no
first-fire collision by arithmetic.

## Blockers

**Not blocked. Two items GATED on ONE external event -- the 0824 wide pull terminating** (4,230/5,966 at
04:11Z, ETA ~06:00 UTC): (a) the LIVE per-master EXERCISE (manual proof each master pulls + lands, held off
the shared SDD session -- CTO ruled the conservative concurrency call the ruling); (b) the 0824 bronze remap
(13b -- waits for terminal denominator). Monitor `bxjwadcpt` (0824 progress/terminal) + the thaw monitor are
armed. The schedules themselves fire on their own regardless.

## Current State (handoff -- zero prior context assumed)

- **BOTH DAILY REST SCHEDULES LIVE + ENABLED.** `canonical-schwab-si2-{08335338,08242234}-daily-pull` ->
  SSM RunPowerShellScript on i-0f3d57a97f14727af -> `sdd-daily-pull.ps1 -Master <m> -Target monolith`.
  Failure -> opal-critical-surface-alerts (subs CONFIRMED: SQS-to-COO + SMS). Tag schwab-si2-iam-v1.3.0.
- **THE PULLER** (`infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, in S3 at
  `s3://opal-data-schwab/_ops/canonical-schwab-si2/sdd-daily-pull.ps1`, 27,198 bytes): monolith-default,
  session-lock-guarded (`C:\schwab-sdd\.sdd-session.lock`), manifest write WARNs-not-silent.
- **0833** fully in monolith (6,932, 3-tier verified, prior log). **0824** wide pull STILL RUNNING against
  `opal-data-schwab/08242234/bronze/` (~4,230/5,966); its monolith remap runs on terminal via
  `remap-bronze-to-monolith.py --master 08242234 --execute`.
- **257 Glacier** thawing (Bulk, 14-day window), background, monitor armed.
- **Commits this window:** 7f31489d2, 0d8607926. Tag schwab-si2-iam-v1.3.0. All origin/CLOUD.

## Next Steps

- **[0.6.2 self]** On 0824-terminal (monitor): run the per-master live exercise (SSM one-shot each) ->
  report 13c three-tier + partition list per master + both first scheduled fires; then the 0824 remap; MCP
  the terminal 0824 count to DS. On Glacier-thaw-complete: 01raw copy+verify -> grant removal + implicitDeny
  evidence (AC5).
- **[0.4.0_DS_ClientPlatform]** W4 column half done (5a0977da4); open external deps = the FAM/SLM spec
  (Andrew, routed) + the 0824 terminal count (me, on pull-landing).
- **[Andrew]** the Schwab SDD FAM/SLM record layout (via COO).

## MCP traffic

~18 messages. Significant: **Andrew-direct x2** ("proceed through ETL / DO it"; "daily rest pattern for both
0833 and 0824") -- recorded verbatim + broadcast same-turn, TO amended 7c0db1569. CTO: concurrency read
confirmed (conservative call = the ruling), session-lock design requirement, C3(c) gate GO -> re-gate GO on
the 6/1/0. COO: relays + RAVC-4 close (both-masters daily REST accepted as live). DS: W4 column half + the
FAM/SLM spec ask + the crs_reader T1 reconcile.
