# AMGT_RESAPP round 36 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `2c07e79688`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-23 ~07:4xZ, after Andrew's wind-down word -- the compile is an act, not a wait.

**DRAIN-END: 1 of 1 terminal, 0 open. 9 of 9 criteria PASS, rc=0 VALID, 9/9 invocation-alignment,
111 tests pass in the MERGED shared tree** (re-run by this seat, not inherited from the worker).

## 1. BOTH STACKED BLOCKERS CLOSED

| | round 35 state | round 36 result |
|---|---|---|
| **A** -- search returns 0 | `recordCnt=0` under every parameter combination tried | **SOLVED** -- and not by parameters |
| **B** -- adapter cannot win | 5 of 5 return paths `passed` false; seeds written into a list step 4 already read | **CLOSED** -- fetch -> extract -> acceptance inside the adapter |

## 2. BLOCKER A WAS AN ID-SPACE ERROR, NOT A PARAMETER ERROR

⛔ **HKEXnews' `stockId` never accepted the LISTED stock code. It requires HKEXnews' own INTERNAL
predictive-search id** -- the `"i"` field of `activestock_sehk_e.json`. Lenovo, listed code `00992`,
carries internal id **`2325`**.

**Isolated by a SINGLE-VARIABLE SWAP, every other round-35 parameter held byte-identical:**

| `stockId` | recordCnt |
|---|---|
| `"00992"` (round 35's exact shape) | **0** |
| `"2325"` (internal id) | **1117** |

⭐ **So round 35 was never wrong about its parameters -- it was wrong about the ID SPACE.** That is why
EVERY combination it tried returned zero, and ⛔ **why a tuning pass could never have found it: tuning
varies the parameters, and the parameters were correct.** `Z-W128-S1`'s refusal to let this be sized as
query-tuning was the load-bearing call of the last two rounds.

⭐ **AND THE POSITIVE CONTROL IS WHAT MADE THE SWAP INTERPRETABLE.** AC0 first proved the interface
answers at all -- drop `stockId`, `searchType=0`, a date range, **recordCnt 14376** -- *before* any
conclusion about Lenovo was drawn. Without it, `00992 -> 0` and `2325 -> 1117` are two more numbers in a
space of untested guesses. **The order made the control mandatory and refused an unmeasured zero.**

## 3. THE TWO LIMBS WERE GRADED INDEPENDENTLY, WHICH WAS THE POINT

- **LIMB 1, live:** AC0 (control, 14376), AC2 (interface characterised -- `stockId` needs the internal
  id; `documentType` ignored under `searchType=1`; `category` required non-blank; `searchType` not the
  blocker), AC3 (Lenovo -> id 2325 -> 1117, isolating round 35's zero to the ENCODING, not the issuer).
- **LIMB 2, fixture:** AC4 (`passed: True`, winner step 5, family ANNUAL-REPORT), AC5 (**run_battery
  returns RESOLVED** -- the win PROPAGATES), AC6 (test (c) still binds: negative control rejected on
  entity+family, positive control accepts).

⭐ **AC4 and AC5 were deliberately separate and neither implies the other.** An adapter that wins while
the battery still returns UNRESOLVED is the stacked-blocker defect recurring; AC5 exists to catch it.

**Spend:** `http_fetches 11` of 12 permitted, `bloomberg_calls 0`, `s3_deletes 0`, `delete_markers 0`.
**AC8 negative control:** 5 signatures + 6 lambda lines + `STEP_ORDER` byte-identical; diff names exactly
`lib/research/filings/battery.py`.

## 4. ⚠ WHAT THIS DOES **NOT** CLAIM

**The route is now CAPABLE of resolving. That is not the same claim as "Lenovo resolved today."** The
adapter inherits round 35's most-recent-filing selection, so a LIVE win still depends on whether the
newest filing happens to be an annual report on a given day. ⭐ **The worker named this as a limitation
rather than silently widening the cell to fix it** -- limb 2 is fixture-proven for exactly this reason,
and a live win was explicitly a bonus, never the bar.

**So `FWD-3` (Lenovo FILINGS -> Thesis tab) is UNBLOCKED IN MECHANISM, not yet demonstrated end-to-end.**
That is the CVO's judgment to make, and the packet separates the two rather than letting nine PASSes read
as a served outcome.

## 5. ⛔ EVIDENCE THAT COULD NOT BE COMMITTED -- a concrete cost of the `.scratch/**` lane gap

The **ten** `.scratch/r129/` scripts that produced AC0-AC7 were **REFUSED by `owned-paths-check`**,
exactly as this order predicted. They exist **only** in the worktree.

⛔ **`C:/tmp/wk-amgt-36-129` IS DELIBERATELY NOT REMOVED, against `safe-merge`'s own closing advice,**
because removing it discards untracked files silently and these are the live research artifacts behind
the round's finding. ⚠ **Third instance of the `.scratch/**` gap and the FIRST where it costs live
evidence rather than convenience.** `0.0.0_AB_MSTR~Z`: this strengthens that card row.

## 6. What this seat asks of L9/L10

1. **Grade the cell on what it built, and grade `FWD-3` on MECHANISM-vs-DEMONSTRATED** (s.4). Both are
   true and the packet separates them.
2. **`Z-W128-S1` can now be DISARMED** -- its hazard was "do not size this as tuning," and the finding
   vindicates it. Disarm with the reason, do not silently drop it.
3. **`rk-49`'s dependency is materially changed** -- the HK route now works in mechanism. It stays
   `pending` on Andrew's key-rotation word, which is a SEPARATE hold.
4. **The three lane gaps stay on Andrew's card**, with `.scratch/**` now carrying a measured cost.

**Push state: LOCAL on SITEZ @`2c07e79688`.**

-- `2.0.0_SA_COO~Z`
