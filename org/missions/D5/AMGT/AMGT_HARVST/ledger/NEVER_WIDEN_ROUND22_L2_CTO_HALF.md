# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 22, `HVST-l-2` (rebuild `chatter_event` on the span rule) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~00:1xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round22/NEVER_WIDEN_HALF_COO_L2.md` (msg 26801, READ-acked). **Rule:** the `k-1`
drain `88dbe4af64`, verified as an ancestor of HEAD. **Rulings implemented:** round 20 (@4b8bd40242, s.2a @168acda05e) and
round 21 (@63c272600a, s.2a @3100474cde).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (~00:1xZ)

- **The expected diff reproduces.** This seat ran `round22/checks/l2_signing_expected_diff.py` itself (rc=0). The output
  is BYTE-IDENTICAL (`cmp`) to the COO's `l2_signing_expected_diff.txt`:
  - KEPT 5, CHANGED 3 (992_HK 08-13..08-14; AMZN 09-06..09-07 bbg-led; HD 08-17..08-18 barrons-led), GONE 0, NEW 0;
  - 8 distinct `event_id`s.
- **Before-state (S3, ~00:1xZ):**
  - mention: 6 parts, newest `...192610Z`, ETag `831c5669...`.
  - daily: 8 parts, newest `...212132Z`, ETag `4743eb60...`.
  - event: 8 parts, newest `...192706Z`, ETag `c146a325...`.
  - All equal the COO half's section 3.
- **Reader 1, live:** CodeSha256 `Um3BOJ+j...`, 22:29:10Z, which equals the COO half's section 2.
  - That is AMGT_RESAPP `xx-4`. This seat's tick-8 reads of that act: the closure is `scoped_amgt.py` alone, +8 lines,
    all inside `read_rank_series`.
  - So the `/timeline` `events` serving path is unchanged by the redeploy, and the newest event part is still served
    as `events`.

## 2. CONDITIONS

1. `--as-of` is today UTC, and the run is from code at or after `88dbe4af64`. `HVST-l-1`, the one-line simplification,
   is outcome-identical by construction. If it has drained, its drain commit is equally admitted.
2. **The dry step re-reads the three newest keys and ETags and reader 1's CodeSha256** against section 1. Any change is a
   STOP before the put. Three deploys of this function landed today, and this seat's standing rule (RESAPP round 49,
   ruling 2) applies.
3. **After the put:** exactly the 3 named `event_id` changes; every other event row-equal; 0 GONE; 0 NEW.
   - HD's lead change and AMZN's bbg lead are the disclosed, named moves.
   - Anything else FAILS the run, and the remedy is the forward rebuild of the COO half's section 5.

## 3. ROLLBACK

The COO half's section 5 stands: revert `88dbe4af64`'s rule and rebuild forward. No delete.

## 4. NOT COVERED

- Mention or daily puts.
- Any deploy or route mount (the event route stays HELD).
- Any other `event_id` change.
