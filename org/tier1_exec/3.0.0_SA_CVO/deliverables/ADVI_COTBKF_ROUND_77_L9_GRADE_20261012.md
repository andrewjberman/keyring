# ADVI_COTBKF round 77 -- L9 grade of CB77by1-AC2 and CB77by3-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T00:56:37Z. Rows D2-S130 (the grade) and D2-S131 (two latent hazards, this seat's).
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_77_DRAIN_END_20261012.md @dca4f4d16f (msg 6226)`. The round answers the question of this seat's round 76 grade: is a value built from the affected close served?

| criterion | verdict |
|---|---|
| CB77by1-AC2, the census of readers | **MET**, with what it could not see stated |
| CB77by3-AC2, the no-snapshot branch and the level error where served | **MET**, reproduced by this seat |

**The answer, on this evidence: no served figure carries the three-quarters error today.** Three limits stand beside it.

## CB77by3-AC2: MET

47 served holdings partitions (2026-04-22 to 2026-06-07) were built before the first snapshot and do carry the store's close.
On those dates the store's close is the right price. This seat re-derived that with its own script:

| the store's close over the unadjusted close, the 15 failing funds | worker | this seat |
|---|---|---|
| the served window, fund-days | 480 | 480 |
| lowest and highest ratio | 0.9845 and 1.0061 | 0.9845 and 1.0061 |
| median | 1.0000 | 1.0000 |
| below 0.98 | none | 0 |
| per-fund median over the whole history | 0.5647 to 0.9179 | 0.5647 to 0.9179 |

**Why it holds, shown as numbers.** The median ratio by year, all 15 funds: 0.46 in 2020, 0.51, 0.63, 0.74, 0.79, 0.88, and
1.00 in 2026. The error grows going back and is nil at the present. The served partitions sit at the present end.

## CB77by1-AC2: MET

19 readers are classed with 18 denominators; one serves a value. This seat printed that reader's code: with a snapshot present
it prices each holding at the custodian's market value over units, and returns before the price store is loaded. The census's
"does not use the store" is true of that branch only, and the round then read the other branch. That is the criterion met: the
one serving reader was not waved through on its live path.

What the census could not see, in its own words: deployed code as against the repository copy; consumers that fetch the firm's
gold through an API without naming the store; exports. Three readers are not established.

## The three limits

1. **7 of the 15 funds were matched as held** on the one date read; "held on any such date" is between 7 and 15.
2. **46 of the 47 partitions were not opened.** The branch is read from one partition's rows and the rest's last-written times.
3. **The store read is a local copy of 2026-10-08,** not the store as it stood when the partitions were written. This seat's
   re-derivation uses the same local data and shares this limit: it confirms the arithmetic, not the store's past state.

## Two latent hazards, filed as row D2-S131

No row was filed in the round. Two things in it should not live only in a packet:

- **A rebuild of those 47 partitions from a later copy of the store would carry the error.** They are right because they were
  written when the close was current. The same dates read from the store after later distributions will be low. Nothing in the
  tree prevents it (the issuer's statement).
- **This project's own minted table holds 259,357 account-days at a value built from these closes, and has no reader.** The first
  reader built on it serves the error. The funds are a median 23 percent of the account's valued total there (the worker's figure).

Neither is live. Both are one ordinary act away.
