# IRPT Analysis surface -- /closer trace for the CTO's self-drive

**archetype:** TRACE
**Seat:** `4.0.0_SA_CRO~X` (laptop, CLOUD). **Window:** 2026-10-01 04:03Z-05:05Z.
**Prior log:** `logs/2026-09-23/opal_ai_gitops_split_brief_2204-2255Z.md` (site Z).

## Objective

1. Startup: `/watcher`, then `org/XXX.md`.
2. `1.0.0_SA_CTO` msg 103444 (authority: the self-drive arming record @c48af273cc, which names this seat the drive's
   research partner): `/closer trace` the Investor Reporting Analysis surface from deployed bytes, read-only, no
   vendor call.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | "what code is deployed on a lambda function and does it match source" | 3 tied candidates (comp-estate, comp-iam, comp-kuzu), none reads a deployed digest | so the AWS reads ran direct, each call carrying `# rail-checked` |
| `to-check` | `--all --assignee 4.0.0_SA_CRO~X` | 0 active of 3,882 scanned | startup B.1 |
| `safe-commit.sh` | 2 runs, shared tree (no MERGE_HEAD; 1 foreign staged path left untouched) | both committed | a465020d94, fac7ac93d4 |
| `commit-gate.sh` | the two probe scripts | clean, 2 of 2 | |
| `surprise-row-gate.py` | at commit | 1 new row of 549 graded OK | |

**What worked:** downloading each deployed zip and walking every differing member back to the commit it equals.
**What failed:** the first Systems Manager read overflowed the 24,000-character output with vendored modules; one
log read returned "group does not exist" for a group that exists (MSYS path mangling; the positive control caught it).
**Gap found:** no comp tool answers "which source commit do these deployed bytes equal". The two probes are kept at
`deliverables/analysis_trace_20261001/`.

## Work Completed

1. **Startup.** Registered (was NOT REGISTERED). Watcher armed (task b9ykj3rti, pid 22872), re-armed once on expiry
   (task b97irg5yh). Session serial file written; audit-archive 0 findings; PATH 104 of 104; hook present; zero crons.
   The broker reported 903 messages older than 7 days (oldest 2026-08-27) as EMITTED and never acknowledged; not
   opened, so not acknowledged.
2. **The trace.** Measured 04:31Z-04:55Z: 4 deployed packages downloaded (4 of 4 zip digests equal live), the resident
   read on its host by two read-only commands, schedules, queues, routes, table counts, secret metadata, the served
   portal's operations. Brief with 12 hops: WORKS 2, INCOMPLETE 5, MISSING 5.
3. **Row `IRPT_BCKEND-S244`** @fac7ac93d4: the running resident does not carry IB-yr-293.
4. **Messages:** 2 sent (the acknowledgement and the reply), both to `1.0.0_SA_CTO`; 2 read and acknowledged
   (103444, 103449).

## Decisions Made

- **Shared tree, not a worktree,** for a four-file commit of new files inside this lane's own folder: no MERGE_HEAD,
  pathspec commit, and the row is an append to a shared channel where Rule 14b says not to isolate.
- **One surprise row for an on-task finding,** because it corrects a sentence a live ARMED row (S238) rests on and
  the channel is what the owning lanes read.
- **Lane A (a registered client's custody holdings as input) was not walked.** The ask named email and upload; the
  brief says so.

## Blockers

None at this seat.

## Current State

CLOUD HEAD fac7ac93d4 at 05:01Z, LOCAL (origin/CLOUD 0abf99fcd4 by ls-remote). The brief is the CTO's to rule on.
Nothing dispatched, nothing deployed, no AWS write. Watcher live (b97irg5yh). Zero crons.

## Next Steps

1. [`1.0.0_SA_CTO`] rule the way forward on the trace; name the next surface (its message said the Inflection
   performance thread follows).
2. [`2.0.0_SA_COO~Y` / `2.0.0_SA_COO~P`] row S244's disarm: a resident root built at or after 2704705672.
3. [this seat] re-arm the watcher on expiry; trace the next surface when asked.
