# AMGT_RESAPP task order -- `AMGT-af-2` -- THE SERVED T-1 FALLBACK, BREAKOUT READS BREAKOUT, PERCENT BY NAME (FWD-33, FWD-34)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-af-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~198</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; read-path code.
comp-iam: DECLARED-NOT-APPLICABLE -- no new table, bucket or prefix is read; the same DynamoDB pointer and generation reads.
comp-adversary: RUN by the issuer at the cut -- AC2 and AC3 FAIL at the base (overlay price axes ABSENT on 10-01; breakout score a fraction); both PASS on a simulated post-state built from the live responses and the raw DynamoDB items.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r56-198` (branch `wk-AMGT_RESAPP-198`, cut from the issuance commit). Work and commit only there.

## 1. THE ACT -- `AMGT-af-2` (round 56, decomposition s.64)

All edits in `lib/research/api/scoped_amgt.py` READ functions and serializers. Do NOT edit `handler()` (a sibling cell, af-1, adds a
dispatch branch there in parallel).

1. **T-1 fallback on the per-name read (FWD-33).** `read_point_record` (`:821` at the cut) asks for today's UTC date and has no
   fallback, so on any day before the 07:00 ET producer run the overlay's price axes read ABSENT. When the requested date has no
   pointer, serve the latest COMPLETE generation on or before it, using the same walk `read_rankings` uses (`_find_latest_served_pointer`).
   The record then carries `as_of_date` = the trading day SERVED, `requested_as_of`, `dated: true`, and `stale_trading_days` (int).
   The overlay's `axis_reads` entries carry `as_of_date` and `stale_trading_days` from the record.
2. **Staleness on rankings too.** `read_rankings` already walks back; add `stale_trading_days` to its payload.
   `stale_trading_days` = the number of trading days from the served date up to `lib.trading_calendar.prev_trading_day(now)`
   (0 when the served date IS that day). Use `lib/trading_calendar.py` only; never a weekday heuristic.
3. **Breakout reads breakout (FWD-33).** `read_security_overlay` gains `"breakout_price"` = the BREAKOUT/PRICE row
   (`by_axis[movement_gate.crossed_axis("BREAKOUT", "PRICE")]`). `"price"` stays the TRENDING/PRICE row.
4. **Percent by name (FWD-34), at SERVE time, never in the store.** On every PRICE row the API serves (rankings, overlay axis reads,
   `breakout_price`, `price`, and the rank-series points):
   - BREAKOUT/PRICE: `score` is served as stored x 100, `score_pct` = that value, `pct_jump_pct` = stored `pct_jump` x 100, and the
     unsuffixed `pct_jump` key is NOT served.
   - TRENDING/PRICE (already percent): `score` unchanged, `score_pct` = `score`, and `return_30d_pct` = `score` when `window_days` is 30.
   - No field named `*_unit` may read anything but `percent`. CHATTER rows are untouched.
   Existing tests that assert the breakout fraction are updated to percent; name each in your report.
5. **The overlay axis reads name their absence and their move (CONTRACT s.4; DSGN round 15 builds against these names).** Each
   `axis_reads` entry whose `point_status` is not SERVED carries `absent_reason`: plain words a person can read (for example "no
   ranking was produced for this name on or before 2026-10-01"), never a status token such as ABSENT, REFUSED or NOT_SERVED. A
   SERVED entry carries `places_moved` when the ranking row join (`_join_places_moved`) has it for that axis and day.
6. **Test** `lib/research/api/tests/test_t1_fallback_and_pct.py`: stubbed pointers prove the walk-back, `stale_trading_days` across
   a weekend and a market holiday, the breakout field, the percent fields on both axes, and a plain-words `absent_reason`.

**Measured at the cut (10-01 ~05:0xZ):** BREAKOUT/PRICE and TRENDING/PRICE latest served = 2026-09-29; `prev_trading_day` = 09-30;
ASML NA breakout stored score 0.0921396, pct_jump 0.09214; 992 HK trending stored score 18.109; overlay ASML_NA_Equity price axes ABSENT.

## 2. BOUNDS

1. Write only the paths below. No producer change, no store write, no deploy (af-5 deploys), no handler edit, no vendor call.
2. Standing: no S3 delete, no push of shared branches, no portal change.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~198/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-af-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, test_t1_fallback_and_pct.py included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-af-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round56/checks/af_2_serve.py --what fwd33; echo "exit=$?"</invocation><expect>every clause PASS; THE PER-NAME READ SERVES THE LATEST TRADING DAY AND BREAKOUT READS BREAKOUT: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-af-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round56/checks/af_2_serve.py --what fwd34; echo "exit=$?"</invocation><expect>C1-C8 PASS; EVERY SERVED PRICE MOVEMENT IS PERCENT BY NAME: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~198 <0.9.0_WK_AMGT_RESAPP~198@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~198/AMGT_RESAPP.TO-AMGT-af-2.served-t1-fallback-breakout-and-percent.proof_of_spec.json`.
Report once: the commit hash, the three criteria's output lines, every existing test you changed and why, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~Z, before spawn, 05:3xZ):** act item 5 added -- `absent_reason` in plain words and `places_moved` on the overlay axis reads (CONTRACT s.4; COO~D msg 27542 asked for the names). No criterion changed; graded by AC1's test and by DSGN's page read. Gate limb: none graded this modification (not a newly-added order; no `<placeholders>`).

**ISSUER NOTES:** addendum D FWD-33 + FWD-34 (v0.32: the unit rides the `_pct` suffix; the T-1 fallback covers ranking reads). Served
only after af-5. The FWD-33 negative arm is the base itself: the overlay's price axes read ABSENT on 10-01. Positive arm: PASS on the live
responses transformed to the specified shape.

<status>pending</status>
<round>56</round>
<slot>0.9.0_WK_AMGT_RESAPP~198</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-01 ~06:2xZ):** AC2 YES and AC3 YES (worker ~198, a88531512b/0d3a9d939d; re-run on the merged tree, both YES); AC1 graded by the issuer on the full tree (CLOUD 78167bb8fc): 342 passed, exit=0 -- row Z-S327 resolves W198-S1. Drained 78167bb8fc. Served only after round 57's redeploy.

<status>complete</status>
