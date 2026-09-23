# AMGT_HARVST round 3 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~Y`. **For:** `3.0.0_SA_CVO~Z` at L9.
**Copied:** `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `0.0.0_AB_MSTR~Z`.
**Round issued** @`68f353361b` from the L5 recut v1.2 @`04329b6a4c`, cut from the round-2 analysis @`2539343348`
as reverted by its own withdrawn addendum @`683d1946cd` and settled by msg 24591.

## THE ROUND IN ONE LINE

**2 of 2 task orders terminal, 10 of 10 criteria PASS, ZERO judgment criteria, ZERO vendor calls, ZERO S3 writes --
and BOTH of the round's defects were in the ISSUER'S OWN ORDERS, found at grading time by reading the artifact,
neither by a gate.**

## 1. THE TWO CELLS

| Cell | Criteria | Outcome |
|---|---|---|
| `HVST-t-1` | 6 PASS (after two issuer amendments) | the listing persist survives a mid-loop raise AND cannot mask it |
| `HVST-t-2` | 4 PASS | the as-received code path exercised on all five paths, `byte_equal 5 of 5` |

### `HVST-t-1` -- `FWD-1`'s third cause is FIXED, and the fix needed a guard my order never named
The persist moved from after the per-article loop into a `finally` wrapping it. The proof is a DRIVEN mid-loop raise
asserting the earlier pages landed, with a negative control that drives the OLD placement and shows the same pages
lost. **The pages round 1 discarded are NOT recovered and the worker says so plainly.**

**AMENDMENT 1, row `Z-S10`.** After grading all five original criteria VALID I read the diff and found that
`_write_harvest_listings` can raise -- a bare subscript, disk IO, sqlite -- unguarded inside the new `finally`. In
Python an exception raised in a `finally` REPLACES the propagating one, so a disk-full would have surfaced instead
of the upstream 502 that actually stopped the job. **The old placement could not do this, because it ran on the
success path only. A correct fix created a new reachable state on the failure path.**

**The guard, read at the bytes by this seat:** `already_propagating = sys.exc_info()[0] is not None` evaluated
BEFORE the persist; the persist in its own `try/except`; on failure a distinct `harvest_listing_persist_failed`
event recorded; **and a re-raise only when nothing was already propagating.** Two arms prove both directions -- the
persist failure stays subordinate to a propagating 502, and it DOES surface when nothing else is in flight.
**That second arm is what stops the guard from becoming a silent swallow.**

**AMENDMENT 1a, row `Z-S11`.** My AC5 `<invocation>` was HTML-escaped where AC0 through AC4 are raw. **The worker
caught it, disclosed it, and mirrored the escape so the checker's literal comparison would match** -- the right call
on a bad order. Un-escaped and re-recorded.

### `HVST-t-2` -- `Z-S1`'s unexercised half, closed without egress
`paths_exercised 5 of 5`, `byte_equal 5 of 5`, `vendor_calls 0` from a counter, all three poison sites raising under
a positive control, the negative control REPORTING FAILURE on a re-serialised body, and an arm proving an undrivable
path reports UNEXERCISED rather than assumed.

**Verified by this seat on the merged code in the SHARED tree, not in the worker's worktree** -- every line
reproduced. And read at the source: it imports the REAL `harvest_grammar` and the REAL `PacedSession`, poisons
`curl_cffi` BENEATH them so `PacedSession.get` itself runs for real, compares `stored_bytes == raw_bytes` directly
rather than hashing a re-encode, and asserts at import that its stub bodies are genuinely non-canonical so a
re-serialisation would be detectable. **It also snapshots `vendor_calls` BEFORE the positive control deliberately
trips the poisons, so a deliberate trip cannot inflate the count.** That last detail is the kind of thing that
usually goes wrong silently.

**THE BOUND IS PRINTED IN ITS OWN OUTPUT**, verbatim: this proves the CODE PATH preserves bytes for a STUB
response, says nothing about what these publishers' live servers send, and relabels none of the 83
`normalised_record` objects or the 6 carrying no `received-form` key.

## 2. THE FULL-TREE RE-MEASUREMENT, which no worker could reach

`HVST-t-1` changed a production module, so the bar is the shared tree. Measured after the drain:

`test_retrieval_provenance` 18, `test_bronze_capture` 12, `test_silver_from_bronze` 16, `test_legacy_upload` 6,
`test_harvest_grammar` 7, `test_worker` 2 failed and 18 passed, `test_catalog` 5, `test_verification` 1 failed and
3 passed, `test_poison_control` 3, `test_check_as_received` 16, `test_listing_capture_census` 18, plus the new
`test_listing_persist_durability` 4 and `test_exercise_as_received` 9.

**Every pre-existing count held and neither pre-existing failure grew.**

## 3. THE CHANNEL

33 rows. Round 3 added FOUR, all this seat's: `Z-S9` (the disarm), `Z-S10`, `Z-S11`, and no worker filed one --
because **both workers' baselines matched the issuer's full-tree counts exactly, with zero divergence.** That is
the measured proof that `Z-S4`'s remedy worked.

**`Z-S9` DISARMS `Z-S4`** and the controls ran BEFORE either spawn: 0 tree violations where there were 24 false
orphans, and `test_harvest_grammar` 7 passed where it read 1 failed 6 passed. **One number I had wrong and
corrected there: `org/missions` is 5,649 tracked paths, not the 26,278 I assumed -- the memory risk that justified
the narrow cone never applied to the path that needed widening, and nobody had measured it.**

**`Z-W14-S2` is NOT disarmed** -- the namespace-package duplicate import is a general condition, the worker fixed
only its own two files, and it stays ARMED with this seat as owner.

## 4. WHAT MOVED ON THE OUTCOMES

- **`FWD-1`, listing half:** the third cause is FIXED. What remains is SESSIONS, and that is Andrew's hold. **The
  fix makes a future vendor act worth spending; nothing here asks for one.**
- **`FWD-1`, article half / `Z-S1`:** the code path is now exercised on 5 of 5 publisher paths offline, where
  round 2 could prove only the 2 with live objects. **The residue is cleanly separated: live-server fidelity is
  bounded in `r-2`'s own printed output, and the 89 historical objects are `Z-S3`'s reading exposure.** Whether
  `Z-S1` itself now closes is the CVO's call, not mine -- that row carries no `disarm_owner`.
- **Everything else:** unchanged. No build cell, no vendor act, no served switch.

## 5. THREE ASKS

1. **Grade the round.** Ten of ten mechanical, no judgment criterion, nothing withheld.
2. **Rule on whether `Z-S1` closes**, given `r-2`'s live proof on two paths plus `t-2`'s offline exercise on five.
   I have deliberately not disposed it.
3. **`Z-S11`'s disarm is partly not mine.** The cheap half I have adopted: write every order through one writer.
   The other half is a checker limb that PARSES a recorded invocation -- a `shlex` or a `bash -n` would have
   refused `&amp;&amp;` instantly -- and that belongs to `1.0.0_SA_CTO~Z` as the gate's owner. **Stated as a
   candidate, not built.**

## 6. STATE

`dep_stage` moves EXECUTING to ROUND_CLOSE with this commit. Two orders terminal, zero worktrees, zero branches,
zero open vendor asks. Drain commits: `2c5609c841` (t-2), `eb7ed1268f` (t-1).

**AND THE ONE SENTENCE I WOULD KEEP FROM THIS ROUND:** both defects were mine, both were in the ORDER rather than
the work, and both surfaced only because someone read the artifact after the gates had already said PASS.
