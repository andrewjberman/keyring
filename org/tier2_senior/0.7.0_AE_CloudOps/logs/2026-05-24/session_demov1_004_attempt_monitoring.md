# ADVI_DEMOV1.004 -- attempt-monitoring session (extended)

**Agent:** 0.7.0_AE_CloudOps~C
**Date:** 2026-05-24
**Mode:** Cross-lane monitoring of DS~C's demo_transform.py iterations on the
demo-transform-runner EC2 instance (i-03343a6072834f77d), stood up via
ADVI_DEMOV1.005 (`shared-infra-v1.17.0`) on 2026-05-23.
**Status:** ACTIVE. attempt-13 InProgress at log time (~13 hours into Pass 2).

## Provenance

ADVI_DEMOV1.005 IAM/EC2 grant ratified by COO + MSTR on 2026-05-23 (commit
`f17ee0fb2`; tag `shared-infra-v1.17.0`). DS~C's demo_transform.py is the
next-in-chain consumer of that grant. This log covers the
~24 hours after DEMOV1.005 ratification, during which I monitored DS~C's
13 attempts (attempts 7-13 visible in this session window; attempts 1-6
were the prior session's b1-area collisions on austin_thompson before context
compaction).

## DS~C attempts observed this session (commit-level)

| Attempt | Commit | Failure mode (stderr-summarised) |
|---|---|---|
| 7 | (prior) | austin_thompson surviving-real-identity guard trip |
| 8 | (prior) | austin_thompson exception-swallow → false-positive PII-CLEAN at ~6641/22260 writes |
| 9 | (prior) | (cancelled) |
| 10 | `9e02fc35d` | client_name couple-component guard + real-name pre-seed |
| 11 | `defcab3cb` | sam_owens surviving-real-identity guard trip (different advisor key from austin_thompson — partial progress confirmed) |
| 12 | `c61d4da6e` | diagnostic patch (expose leaking identities in apply-mode HARD ERROR) |
| 13 (active) | builds on `dbf170b32` _embeds_real guard (reject fakes embedding real-name substring) | running; past the austin_thompson + sam_owens abort points; no HARD ERROR observed in stderr to date |

## attempt-13 timeline (SSM cmd `ef7103fd-6776-432c-8732-f800563d28b5`)

| Stamp (UTC) | Event |
|---|---|
| 03:01:04Z | dispatch (DS~C, `--apply --workers 64`) |
| 03:01:04Z .. 04:14Z | empty stdout window (stdout buffering — Python without `PYTHONUNBUFFERED=1` in DS~C's SSM wrapper) |
| 04:16:58Z | AE~C healthcheck-1 (cmd `b79c2b44`): PID 33734, 92.0% CPU, 75 min elapsed; process alive |
| 05:02:14Z | first demo-bucket write observed (post-Pass-1 mapping complete) |
| 05:06:47Z | AE~C healthcheck-2 (cmd `f3c65cab` earlier): PID 33734, 97.7% CPU, 125 min elapsed |
| 05:19:52Z | bucket at 7344 objects (~33% by key count); writes flowing |
| 05:31Z .. 17:38Z | sustained write stream observed at every 10m cycle (37 cycles of latest-LastModified watermark progression) |
| (still in progress at log time) | Pass 2 continues; no HARD ERROR / abort observed |

**Total runtime at log:** ~14 hours wall (started 03:01Z; current ~17:38Z).
**Status:** SSM InProgress, no stderr. No abort, no false-positive completion.

## Infrastructure-side actions this session

1. **EC2 instance i-03343a6072834f77d auto-shutdown protection.** Added to
   `EXCLUDED_INSTANCES` in ec2-auto-shutdown-enforcer (commit `895b4277d`
   prior session); still in effect — no auto-stop during long Pass 2.
2. **boto3 install on AL2023.** Persistent install of `python3-boto3` from
   prior session (`sudo dnf install -y python3-boto3`) — survived all
   attempts.
3. **Healthcheck pattern (non-blocking concurrent SSM).** Demonstrated SSM
   supports concurrent `AWS-RunShellScript` dispatches — sent two `ps`
   probes (`f3c65cab`, `b79c2b44`) while the primary attempt-13 was
   InProgress; both Succeeded in ~8s without disrupting the running cmd.
4. **demo bucket watermark watching.** Adopted max(LastModified) over
   bucket-count as progress proxy (deterministic-key PutObject = UPDATE
   not INSERT; bucket count plateaus while writes flow). Banked as healthy
   doctrine consistent with memory `feedback_dispatch_sh_bang_inverts_exit_code` family.

## Monitoring discipline observations

1. **Heartbeat TTL < 10m loop interval.** Every `/watcher` cycle re-finds
   `NOT REGISTERED` and re-registers. The broker heartbeat TTL is shorter
   than the loop cadence; functionally fine (re-register is idempotent),
   but registration drops show up at every cycle. Worth a note for future
   /watcher skill iteration (consider explicit `heartbeat()` call in the
   loop body to defer the TTL).
2. **Stdout-buffering as silent class.** attempt-13 spent ~1h with zero
   stdout, indistinguishable from a hang via the SSM API alone. The
   healthcheck-via-concurrent-SSM dispatch (steps 1-2 above) is the
   structural test for the hang-vs-buffer disambiguation. Worth a note in
   future DS-runner doc templates: set `PYTHONUNBUFFERED=1` (or
   `python -u`) in the SSM wrapper to surface live progress.
3. **Bucket count vs LastModified.** Memory rule
   `[[feedback_track_inflight_to_by_artifact_not_sla]]` extends cleanly:
   the watermark is `max(LastModified)`, not the count.

## Findings / signals to surface

1. (NEW) **attempt-13 is past the prior abort points** (austin_thompson,
   sam_owens) and into normal Pass 2 grinding — the `dbf170b32`
   `_embeds_real` guard plus the prior commits' couple-component + slug-
   collision fixes appear sufficient. No re-routing needed unless attempt-13
   eventually trips.
2. (NEW) **Pass 2 throughput observation:** ~14h sustained writes at the
   continuous `LastModified` watermark — the runtime is unusual for the
   nominal 22260-object workload. Possible causes: workers reduced from 64
   (PASS 1 logged 64) to a smaller number in Pass 2, S3 throttling, or
   non-trivial per-object compute in transform. Worth a postmortem item
   when attempt-13 completes; not blocking.
3. **DEMOV1.004 RAVC2 gate is downstream of this.** When SSM `ef7103fd`
   transitions Success and Phase D PII-scan exits clean, DS~C delivers
   RAVC2; this AE~C session moves to Task #8 (revert
   EXCLUDED_INSTANCES; author structural-follow-up TO for ephemeral-
   instance Lifecycle tag); instance i-03343a6072834f77d gets terminated.

## Next steps (when attempt-13 lands)

| Recipient | Item |
|-----------|------|
| **DS~C** | Will receive attempt-13 result naturally (SSM completion fires their session). If false-positive class re-emerges, AE~C flags class as before. |
| **2.0.0_SA_COO** | Will receive DS~C's DEMOV1.004 RAVC2 evidence. AE~C does not author this. |
| **~self** | Task #8: terminate i-03343a6072834f77d, revert EXCLUDED_INSTANCES, author structural TO for `Lifecycle=ephemeral-one-shot` tag → enforcer respect. |
| **3.0.0_SA_CVO** | Optional postmortem flag on Pass 2 throughput observation if attempt-13 takes >24h total. |

## Compiler Tools (not used this session)

Monitoring-only session; no compiler-tool invocations were appropriate.
ADVI_DEMOV1.005 grant chain was already RAVC2-accepted in the prior
session; this session was downstream consumer-monitoring not
infrastructure work.

## Standing
attempt-13 still running, ~14h elapsed, Pass 2 writes flowing.
`/watcher` 10m loop continues. Standing by for completion signal.

-- 0.7.0_AE_CloudOps~C, 2026-05-24T17:40Z
