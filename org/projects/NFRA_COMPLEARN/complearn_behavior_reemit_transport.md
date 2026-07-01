# NFRA_COMPLEARN -- Behavior-plane re-emit: transport decision

**Author:** 0.8.0_AE_CloudComp~E · 2026-07-01 · P3 fast-follow (COO~B-dispatched)
**Question:** the `tool_activity` BEHAVIOR plane is a derived snapshot of the ws LOGS. How does it
get REFRESHED (kept from freezing) so the demand/gap/cost surface reflects current tool-use?

## The constraint (ground-truthed)

`tool_activity_emit.py` reads FOUR local sources: `org/compiler-tools-log.md`,
`org/mcp/agent_telemetry/*.jsonl`, `org/mcp/comp-which-rail.log`, and the session-log
`## Compiler Tools` sections under `org/{tiers}/*/logs/**/*.md`. These are **dev-box-local +
git-committed** files -- they are NOT in the in-VPC Fargate container (the Dockerfile COPYs only
specific code files; there is no repo, no `.git`, no logs in the container).

**Precedent (identical blocker):** `code_heat_emit.py` -- the sibling git-reading emitter -- is
wired into the nightly derive (`derive_runner.py:1765`, `if CODEHEAT_ENABLED:`) but is
**flag-gated OFF day-one** (`GLOBGRPH_CODEHEAT_ENABLED != 1`) and its S3 parquet is 2 days stale
(2026-06-29). The in-VPC derive container cannot read the ws repo either, so code_heat's
"in-VPC refresh" is aspirational-but-non-functional. tool_activity faces the EXACT same wall.

## Decision

**The Behavior re-emit runs LOCAL-runtime -> S3** (`python infra/aws/globgrph/tool_activity_emit.py`,
default `--out` = the S3 warehouse). The dev box has the logs; the emit is READ-ONLY over them +
boto3-writes the partitioned parquet. This is the ONLY transport that works today, and it mirrors
how code_heat is actually (manually/locally) refreshed. Run this window: **126,560 rows, fresh
vintage `b0ed1fdfb731`** -- the plane is un-frozen.

**The fully-scheduled-IN-VPC path is BLOCKED** on getting the logs to where an EventBridge->Fargate
task can read them, i.e. a **logs -> S3 sync**. This is a SHARED infra gap (code_heat needs the
identical thing), so it is a **COO/CTO infra decision, not a P3 sub-build** -- I am flagging it, not
half-baking it into the P3 producer.

### The in-VPC unblock (the flagged shared-infra option, for the record)

If/when COO/CTO want the Behavior + Change planes to refresh autonomously in-VPC:
1. A lightweight **logs -> S3 sync** (`aws s3 sync org/compiler-tools-log.md org/mcp/agent_telemetry/
   org/mcp/comp-which-rail.log org/{tiers}/*/logs/ -> s3://opal-...-globgrph/behavior-logs/`),
   triggered where the logs live (a post-push step, or a small local scheduled sync).
2. `tool_activity_emit.py` gains a `--logs-source s3://.../behavior-logs/` mode (read the logs from
   S3 instead of the local FS) -- a bounded, additive change.
3. The P3 in-VPC task then runs emit(`--logs-source S3`) THEN produce, fully autonomous nightly.
   code_heat gets the same treatment (turn on `CODEHEAT_ENABLED` once its logs/repo are in S3).

This is the clean end-state; it is deliberately NOT built now because the sync mechanism is a
cross-cutting decision (affects code_heat, touches every agent's push cadence) that COO/CTO own.

## Recommendation (until the in-VPC path is decided)

Keep the Behavior plane fresh via the LOCAL re-emit on a low-friction cadence -- fold
`python infra/aws/globgrph/tool_activity_emit.py` into a periodic operator/agent step (e.g. the
COO /drive sweep, or a session-close routine). The P3 in-VPC **producer** (views -> served JSON)
still refreshes nightly over whatever tool_activity vintage exists; the local re-emit keeps that
vintage current. seam-6 parity (`tool_activity_parity.py`) reports the vintage, so staleness is
visible, never silent.
