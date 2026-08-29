# The resolver's two-state collapse — and the same collapse, found inside the battery that tests it — 0.4.0_DT_ClientPlatform~X

**Date:** 2026-08-28
**Task Order:** NFRA_C3MATERIALIZE.TO-WP4-DTX (resolver repair, track A2)
**Status:** COMPLETE. Six criteria PASS; the proof-of-spec instance is VALID.
**Window:** 17:55–18:50Z
**Archetype:** BUILDER-REPAIRING-A-KEYSTONE

## Objective

Repair `nerves_resolve`'s two-state collapse per RULING.md:61 — five resolver states where two
stood — re-point the spine at the ledger's minted serials read-only, and prove it with a battery
whose every rule is independently load-bearing.

## Outcome

**In-repo: 27 of 27 battery arms, exit 0, all six mutations caught by named arms. Self-test 11 of 11
(baseline at the pin: 9 of 10).** From a clean extract: 20 passed, 0 failed, 7 NOT_EXERCISABLE,
exit 3, extract released. Proof-of-spec **VALID** — 6/6 criteria, 28/28 cell refs, 23/23 declared
cells. Six commits, all under the scoped lane row, no author override.

## The defect, stated exactly

Every failure returned `kind=UNADDRESSED / confidence=NONE / node_ids=[]`, **byte-identical**,
whether the trace-graph cache was missing, git had failed, the ref belonged to another fabric, or
the ref genuinely has no address here. One answer for four questions — and three of the four are
*instrument* failures that were being read as findings about the estate.

The arm that proves it is fixed uses the case where the old contract could hide, with **both sides
returning zero candidates**:

```
ref 'zzz_not_a_thing_anywhere_xyz'
  every tier alive   -> GENUINELY_UNADDRESSED
  substrate stripped -> SUBSTRATE_UNAVAILABLE, naming 4 tiers + exception classes
  byte_identical     -> False
```

## The through-line: I kept rebuilding the defect I was removing

Three times, in three different places, and each was caught by an instrument rather than by review.

1. **A false alarm everywhere is the same disease as a collapse everywhere.** Adding the ledger as a
   sixth tier made "any tier unavailable → SUBSTRATE_UNAVAILABLE" fire on everything, because
   `$NERVES_LEDGER` is normally unset. Every genuine miss became a dead-substrate report. Fixed by
   counting only tiers that *could have answered this ref* — a dead ledger cannot make a filename
   unknowable.
2. **Two views of one fact that can disagree.** `substrate_unavailable` listed every dead tier
   regardless of consultation while `state` counted only consulted ones, so a `GENUINELY_UNADDRESSED`
   result also reported dead substrate. A consumer branching on the property got a different answer
   from one branching on the state. The property now agrees with the state by construction.
3. **The battery reported a dead substrate as a finding.** `.comp-graph/graph.json` is *gitignored*,
   so a clean extract has no trace graph, and the graph-dependent arms came back `FAILED` — which
   says "the resolver is broken" when the truth is "this environment cannot exercise this arm". An
   arm now declares the tiers it needs; absent substrate is `NOT_EXERCISABLE`, never a pass and
   never a fail.

**I wrote the arms and the thing they test in the same sitting, and the arms inherited the exact
assumption I was testing for.**

## What the instruments caught that review did not

- **The mutation proof, on its first run:** `consult_all_tiers → NOT CAUGHT`. The rule I had just
  added to kill the false alarm, and *nothing tested it* — because the battery's own fixture sets
  `$NERVES_LEDGER` and therefore makes every tier alive. **A rule that only matters when a tier is
  dead cannot be tested by a fixture in which nothing is dead.** Reverting it would have left 26 of
  26 green while every genuine miss in the estate became a false alarm.
- **The ledger refused two fixtures before accepting one** — `L-04-close-without-event` and
  `L-05-authored-vs-derived`. Both are WP-3 machines I built last wave, declining to let this wave's
  fixture fake a rename. The second was a defect in *my resolver too*: it matched on `status="active"`,
  a word the fold does not use, so it would have matched nothing in production and I would have read
  the empty result as "no binding".
- **The clean clone**, which found what the in-repo run structurally could not.

## Work Completed

| commit | what |
|---|---|
| `8980571384` | AC1 five-state contract + AC3 typed tier capture (3 broad excepts → 0) |
| `ef76516c6e` | AC2 ledger spine read-only + the 26-arm battery + mutation proof |
| `fd173c06bc` | AC2's main clause: the serial beside the node_id; the rename arm made real |
| `b76b1d56f3` | AC5: arms declare their substrate; NOT_EXERCISABLE ≠ failure |
| `a3c34f019f` | AC5: the AMBIGUOUS arm needs the tracked-file index |

## Decisions Made

- **NOT_APPLICABLE honours a qualifier; it does not classify fabrics.** `executed_on_fabric` is a
  free `nonempty` string with no vocabulary — the same shape CTO~X ruled ABSENT for `semantic_layer`
  in WP-3b. Inventing a fabric taxonomy to make the state reachable would be that costume. The
  double-colon separator means no ref that resolves today can become NOT_APPLICABLE by accident:
  compatibility here is a property of the separator choice, not of care.
- **Exclude `candidate_equivalence` by enumerating what canonicalises**, not by listing what does
  not — so a relation_type added to the contract later is non-canonicalising until someone decides
  otherwise, rather than silently joining the fold.
- **Move the precedence chain byte-for-byte into `_resolve_chain()`.** Every rule in it was earned by
  a live failure; rewriting them while changing the result type would make a regression in either
  indistinguishable from a regression in the other.
- **Re-point the stale self-test case, don't weaken it.** `gap1` asserted a tool retired 22 days ago
  still resolves. Re-pointed at a live bash shim so it tests the same property, and the retirement
  became its own case — expressible only under the new contract.

## Findings Filed

| class | substance |
|---|---|
| OBSERVATION | the self-test was already red at the pin (9/10); subject deleted 2026-08-06 `1a962886be` |
| OBSERVATION | the trace-graph cache is 22 days stale — now readable on every result |
| OBSERVATION | `resolve_many()` has ZERO external callers; its surface is the self-test alone |
| OBSERVATION | the c0 consumer census counted a gitignored build copy and a documenter as consumers |
| OBSERVATION | the TO's face cites the excepts at `:77`; measured they are 75/88/132 (count of 3 correct) |

## Blockers

**None.** One AC clause could not be satisfied as written and is a declared exclusion:
`bundle_identity.py --check` reports STALE *both before and after*, because it compares
`derived_at_commit` and friends, which move with HEAD. The substantive invariant holds and is
measured: `contract_bundle_id` byte-identical, 0 members differ.

## Current State

Six criteria PASS, instance VALID. Push state MEASURED: **LOCAL** — push on CLOUD is integrator-only
(LD-0367/LD-0368); MSTR's window carries it.

## The transferable half

WP-3b's lesson was that a control can report on a world it cannot reach. This wave the same shape
arrived from the other side: **I built the fix, then built the test, and the test inherited the
blind spot the fix was for.** The battery's fixture made every tier alive, so the rule about dead
tiers was untestable; the extract had no graph, so the arms needing one called the resolver broken.

The question that caught both is not "does this arm pass?" but ***"what state of the world does this
arm require in order to be able to fail — and does my fixture ever produce it?"*** A fixture that
cannot produce the failing state is not testing the rule; it is confirming the setup. Mutation is
the only mechanical way I have found to ask it: break one rule at a time and read *which* arms turn.
