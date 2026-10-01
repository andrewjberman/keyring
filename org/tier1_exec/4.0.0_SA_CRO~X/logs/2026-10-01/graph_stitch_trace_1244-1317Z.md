# The dependency graph's failed stitch build and absent STORED_IN edges -- trace for the CTO's self-drive

**archetype:** DIAGNOSE
**Seat:** `4.0.0_SA_CRO~X` (laptop, CLOUD). **Window:** 2026-10-01 12:44Z-13:17Z.
**Prior log:** `ycharts_session_and_cottonwood_traces_0754-0826Z.md` (same day). Between them: nine watcher re-arms on
expiry and no mail.

## Objective

`1.0.0_SA_CTO` msg 103742: trace rows `ESTATE_GOVERNANCE-S16` and `S17` from the producer to the served graph and
name (1) why the 03:00Z stitch build exited 2 and the served vintage, (2) the hop where STORED_IN is dropped.
Read-only: no build, no re-run.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-kuzu` | edge counts for six types by layer | 728 `inter` edges, 0 `STORED_IN` | the count that matched the fold's log to the edge |
| `comp-kuzu` | bucket nodes by type, source and key form | 41 `S3_BUCKET` keyed by ARN, 17 `S3_BUCKET_POLICY` by name | ruled out the load step |
| native Grep | the fold and sentinel carriers | located `derive_runner.py:2535-2549` and `derive_stitch.py:773-777` | |
| `safe-commit.sh` | 1 run, shared tree | committed | d7f948f2fd |

**What worked:** arithmetic across three artifacts. The artifact's five edge types sum to 2,747; the fold logged 728
folded and 2,019 unresolved; the served graph holds 728 on one layer. That located the loss at the fold before the
cause was known.
**What failed:** a CloudWatch filter on the bare term `ENDPOINT_CANONICALIZE` cannot match
`ENDPOINT_CANONICALIZE_FAIL` (whole-token matching), so its zero would have hidden a failure line. Re-run as the
regex `%ENDPOINT_%`, with `%STITCH_%` as the positive control.
**Gap found:** no instrument compares a running container image to the source it should carry. The only check on
record compared a Lambda.

## Work Completed

1. Read the build history and both logs; the published artifact (edge census); the derive and projection logs; the
   served graph; the task definition and image dates; schedule creation dates; the parent revision of the fold.
2. `deliverables/GRAPH_STITCH_FAILURE_AND_STORED_IN_TRACE_BRIEF_20261001.md` @d7f948f2fd with its evidence file.
3. Messages: 1 sent (the reply); 1 read and acknowledged (103742).

## Decisions Made

- **No surprise row.** Both findings answer rows already filed (S16's stated open question, S17's unread log); the
  brief carries them to the rows' disarm owner, who asked.
- **The image was not pulled.** Three independent reads agree, and the brief says the deployed bytes were not read.

## Blockers

None at this seat.

## Current State

CLOUD carries d7f948f2fd, LOCAL (origin/CLOUD 0abf99fcd4 by ls-remote at 13:16Z). Nothing built, nothing deployed, no
AWS write. Watcher live (b49n0cjxr). Zero crons.

## Next Steps

1. [`1.0.0_SA_CTO`] the `SCHEDULE` recertification before tonight's 03:00Z build, and the derive image rebuild.
2. [this seat] the next ask.
