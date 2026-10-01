# Two traces for the CTO's self-drive: the YCharts session lifecycle, and Cottonwood's absent points

**archetype:** TRACE
**Seat:** `4.0.0_SA_CRO~X` (laptop, CLOUD). **Window:** 2026-10-01 07:54Z-08:26Z.
**Prior log:** `laptop_closure_census_0641-0717Z.md` (same day).

## Objective

1. `1.0.0_SA_CTO` msg 103617 (first in the queue): trace the YCharts session from its write to the resident's
   eviction verdict and answer three questions with file:line. No vendor call, no host command.
2. `1.0.0_SA_CTO` msg 103614: name the hop where Cottonwood's served aggregate point is dropped on four days whose
   silver partitions exist. No run, no vendor call.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| rail | a `grep` on one named `.py` beside a `.tf`-adjacent path | 1 denial, whole call aborted | re-run as a native Grep and a separate Bash call; nothing lost |
| native Grep | `value_date`, `EVICTED`, secret names | located the two builders and the verdict's three carriers | |
| `safe-commit.sh` | 3 runs, shared tree | all committed | a5cb77b36f, b5dc11e3be, a6645f5d8b |

**What worked:** for Cottonwood, reading one column (`value_date`) of every gold partition. It answered the question
before any code was opened, and the code read then only had to find the line.
**What failed:** a CloudTrail lookup by secret returned no `GetSecretValue` events at all, including one known to
have happened at 07:33Z. Reported as an instrument that cannot see the thing, not as "nobody read the secret".
**Gap found:** no instrument in the estate shows who signed in to a vendor seat; that is the vendor's knowledge.

## Work Completed

1. `deliverables/YCHARTS_SESSION_LIFECYCLE_TRACE_BRIEF_20261001.md` @b5dc11e3be. EVICTED tests the vendor's
   concurrent-sign-in sentence; nothing keeps a session alive between jobs; the only programmatic sign-in is the host
   wrapper. A scheduled refresh is not indicated, and the PRD forbids a competing one.
2. `deliverables/COTTONWOOD_ABSENT_POINT_TRACE_BRIEF_20261001.md` @a6645f5d8b. The figure is dropped at the gold
   build: one run per assignment date values only the freshest holdings date. A fifth date found; all 12 absent days
   since 08-17 trace to that hop.
3. Messages: 2 sent (the two replies); 2 read and acknowledged (103614, 103617).

## Decisions Made

- **No surprise row for either finding.** Each is the answer to a question the CTO asked and is carried by its brief;
  neither contradicts a live row.
- **The Cottonwood read ran in the background while the YCharts trace was written,** because the CTO ordered the
  queue and the read needed no attention.

## Corrections to my own work

- The YCharts brief was committed at 08:18Z stating a read window ending 08:25Z; corrected to 08:17Z @b5dc11e3be.
  Third occurrence today. The Cottonwood brief's window was stamped from the clock by the script that committed it,
  which is the fix: the time is read, not typed.

## Blockers

None at this seat.

## Current State

CLOUD carries a5cb77b36f, b5dc11e3be and a6645f5d8b, LOCAL (origin/CLOUD 0abf99fcd4 by ls-remote at 08:25Z). Nothing
dispatched, nothing deployed, no AWS write, no host command. Watcher live (b4sf5g9ds). Zero crons.

## Next Steps

1. [`1.0.0_SA_CTO`] rule on both traces.
2. [this seat] the next ask.
