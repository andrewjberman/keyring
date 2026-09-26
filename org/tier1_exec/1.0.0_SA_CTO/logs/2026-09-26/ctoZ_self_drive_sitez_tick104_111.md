# self-drive ticks 104-111, `1.0.0_SA_CTO~Z`, 2026-09-26 ~12:2x-17:0xZ

**Arming record:** `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md` @`f3b85ff6a5`,
A1 @`fc26dfeedb`. **state: ARMED.** Prior log ticks 102-103 @`ec0d05f2db`, author time
`2026-09-26T08:20:21-04:00` (read from the COMMIT, not the filename).

## Step 0

```
SCOPE: sitez -> 5 of 15 live directives [D1, D4, D5, D7, D12] -> 18 project(s)   open TOs 24
INBOX: 0 unread at each read; 9 arrived and were READ-acked in-block
COMPLETION TEST: NOT DONE -- 4 of 18 status:complete (+3 closed)
OPEN CALLS IN SCOPE: 0 adjudicable | 1 RESERVED (serp = metered SPEND, Andrew's by his own class exclusion)
```

## The block in one line

**Andrew paused Tier 1, assessed, and resumed -- and the assessment turned into the one measurement that answers
his question: the latency he saw is CONTENTION, and five amendments were needed because I kept prescribing
before the axes were separated.**

## Acts, with hashes

| act | hash |
|---|---|
| `FWD-23`: a POSITIVE CONTROL written INTO the fence (v0.27 -> v0.28) | `496b42d725` |
| HVST-v-2: the audited override **AUTHORIZED** under five conditions | `7d5f8279a8` |
| fabric throughput **DIAGNOSIS** | `fd8e33c712` |
| diagnosis **A1** -- both levers wrong | `7c7a781ee0` |
| diagnosis **A2** -- my census was one word-splitting bug | `57529a8f63` |
| diagnosis **A4** (commit subject misreads "A3", see below) | `45ece7298b` |
| diagnosis **A3 + A5** -- the loaded arm | `0e1d12028e`, `4ca70cd24e` |

## VERDICTS RECEIVED

| what | hash |
|---|---|
| **`AMGT_RESAPP` ratified-text half SIGNED at v0.28** -- covers `FWD-31` AND the `FWD-23` amendment in ONE signature | `e8534d7433` |
| `AMGT_CORPUS` ratified-text signed a THIRD time | `872b4195f6` |
| gitlink gate: SPEC 3 added, my hardcoded-path finding adopted | `a7898627ef` |

**Batching `FWD-31` and `FWD-23` into v0.28 cost one CVO signature instead of two.** The fabric being quiet at
16:0xZ is what made that free.

## THE PAUSE, AND WHAT IT PRODUCED

Andrew paused all Tier-1 seats at ~14:3xZ (*"Issue a note to all tier 1 agents to pause activity"*) and resumed
at ~16:18Z (*"resume tier 1"*). **I treated neither a `/self-drive` invocation nor an automated goal check-in as
the resume** -- MSTR's relay said *"Do not treat a reply from this seat as the resume"*, and reading an adjacent
prompt as authority is the error I had ruled against on the serp card hours earlier.

**His actual question:** the lowest tokens-per-runtime he had ever measured, with CPU, memory and antivirus clean.

### The answer, and it took THREE SEATS and FIVE AMENDMENTS

| arm | timings (ms) | spread | concurrency | files | trees |
|---|---|---|---|---|---|
| PAUSE (`0.0.0_AB_MSTR~Z`) | **393 / 385 / 379** | **14** | quiet | 44,595 | 56 |
| POST-RESUME (this seat) | **774 / 1119 / 1004** | **345** | 10 seats | 44,597 | 56 |
| my original | 822, ONE run | -- | ~10 seats | 44,589 | 56 |

**File count moved 8 files. Trees never moved. Only CONCURRENCY changed.**

> **THE VARIANCE IS THE PROOF, NOT THE MEAN.** A file-count-bound walk is SLOW BUT STABLE. A lock-contended one is
> ERRATIC. **385/385/379 is a device working; 774/1119/1004 is a device waiting.**

**Ruled OUT along the way, each with its instrument:** no commit storm (9-12 commits/hour, flat); nothing hung (0
Windows-visible git); **`gc` gains nothing** (119 loose objects, 0 garbage, prune-packable 0).

## FIVE CORRECTIONS OF MY OWN, IN ONE RECORD

**1. Lever 2 was already closed three hours before I wrote it -- and I had READ the repaired code.** I quoted the
hook's two WARN lines approvingly, then reported the FAIL-OPEN branch as operative when the `$MAIN` candidate two
lines above is what fires. `0.0.0_AB_MSTR~Z` **ran the hook** and read `rc 0` from 56 of 56.

> **When a gate's LIVENESS is the question, RUN THE GATE.** File presence is a proxy for a resolution path, and a
> resolution path can have a fallback. Two seats using proxies disagreed with each other AND with the answer.

**2. My worktree census was ONE BUG.** Unquoted `for wt in $(...)` word-split every path containing a space:
`[1] 'C:/Users/Opal'` `[2] 'Bloomberg/Desktop/ajb_workspace'`. **Predicted before measuring:** 64-56 = 8 extra,
so 8 paths with spaces, 16 bogus fragments. **Measured: exactly 8, and my NEITHER was 16.** Line-safe re-run
reproduces `3.0.0_SA_CVO~Z` digit for digit: `56 | ROOT 2 | MAIN 56 | NEITHER 0`. **This device has a banked
lesson titled "path has a space" and I walked into it.**

**3. Lever 1 failed FIVE times over**: not cheap (53 of 56 carry state), destructive, wouldn't help if free,
tree count held constant while latency tripled, and site Z with 56 trees is FASTER than the laptop with 12.
**I aimed a remedy at the visible term rather than the dominant one.**

**4. A3's "latency tracks FILE COUNT" was over-read** -- my 822 was itself inflated by concurrency, so the
file-count attribution rested on a contaminated sample. A5 replaces it: **file count sets a FLOOR (~385 ms);
concurrency moved what Andrew saw.**

**5. I mis-attributed an instrument.** A3 credited `0.0.0_AB_MSTR~Z` with three laptop samples the LAPTOP seat
ran. Its rule is the keeper: *"an instrument credited to the wrong seat cannot be asked for its method."*

**And a housekeeping disclosure:** commit `45ece7298b` carries section 5d (A4) but I reused the A3 message file,
so its subject reads "A3". **The record is labelled correctly; only `git log` misdescribes it.** Not amending a
shared-branch commit for cosmetics.

## HVST-v-2 -- a guard that had become a trap

Four individually-correct mechanisms composed into a cycle: the gate refuses the order edit while the instance is
invalid *including the edit recording it invalid*; a 342-char `invocation` compared WHOLE against a ~136-char
command; only the worker may edit that path; the worker cannot be resumed.

**AUTHORIZED under five conditions** -- the override is an AUDITED escape (14a), not a NEVER, and refusing would
strand COMPLETE work behind a string mismatch that moves no measured value. **I recorded that `2.0.0_SA_COO~Y`
was RIGHT to decline it itself**: escalating rather than self-authorizing is the behaviour to repeat. **And I did
NOT change the limb** -- editing a gate to admit my own unblocking act is how a bypass gets built.

> **A guard satisfiable only by a party that no longer exists is not a guard, it is a trap.**

## Scope state

| project | where it sits |
|---|---|
| `AMGT_CORPUS` | round 5 = 10 of 19; **round 6 ALL FIVE CELLS DRAINED** (h-1..h-5); ratified-text signed 3x |
| `AMGT_RESAPP` | round 44: rs-1 drained, **rs-2 DEPLOYED** under both halves; **v0.28 half SIGNED** |
| `AMGT_HARVST` | round 6 recut; HVST-v-2 override authorized; AC1a exercisable under the egress word |

## THE NEXT L10 DUTY IS ALREADY DUE

**`AMGT_CORPUS` round 6 has all five cells drained**, and `CRPS-h-4` and `CRPS-h-5` name `FWD-14`'s three
columns and `FWD-18`'s pillar terms -- **the two enrichment items my own round-5 analysis cut.** So the round-6
slug is due, and with it this seat's round-6 analysis. **0.8's warning applies exactly: open TOs will read an
honest zero while the seat owes an artifact.**

## Cards at Andrew -- ONE

1. **The `serp` BUILD** -- metered, so 92 names is SPEND, excluded BY NAME from his egress term.

## Still owed by this seat

- `AMGT_CORPUS` round-6 analysis, on its slug.
- `AMGT_RESAPP` round-44 analysis, when that round closes.
- The rs-2 deploy's expected outcome is **UNVERIFIED**: its evidence proves page/rich PARITY (285 same), which
  cannot establish the currency is PRESENT -- two sides agreeing neither shows it reads identically.

## Compiler Tools

`git log -1 --format=%aI -- <logfile>` for the floor, from the COMMIT never the filename -- explicit `date -u`
windows after a `--since` with a local offset produced a FUTURE window and two vacuous zeros -- per-op wall timing
with `date +%s%N` and **the concurrency recorded beside each sample**, which is what made the loaded arm
interpretable -- a PREDICTED count (8 space-paths) measured afterwards, so the word-splitting explanation is a
prediction rather than a story -- `git count-objects -vH`, which answered the `gc` question in one call and in the
negative.
