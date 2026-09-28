# AMGT_HARVST task order -- `HVST-z-1` -- ROUND 11 cell 1 of 4: REBUILD `chatter_event` gold. This MOVES SERVED OUTPUT and the never-widen pair is SIGNED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-z-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~32</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the gold write path; this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention and silver headline source, and ONE PUT on amgt/harvest/gold/chatter_event. A refusal is a BLOCKING row, never a workaround.
comp-adversary: RUN at L5 -- the adversary is a rebuild reported as "8 events" while two event_ids are orphaned, and a judgment graded on the BUILDER's output instead of the SERVED rows. AC1 and AC3 are those two adversaries' tests.
</preflight>

## 0. THE STANDING CLAUSES

1. ⛔ **NO S3 DELETE. NOT OF AN OBJECT, A NONCURRENT VERSION, OR A DELETE MARKER. EVER.** This project carries a
   STANDING ABSOLUTE clause (decomp `s.14a`, written after a sibling project deleted 123 objects on its own
   judgment). **The signed never-widen half authorises exactly ONE PUT and NO removal of any kind, including on a
   failed read-back.** If you believe a delete is needed, STOP and file a BLOCKING row.
2. **NO VENDOR CALL.** The rebuild reads landed gold and silver. No publisher request.
3. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~32/scripts/` -- **never `.scratch/`.**
4. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~32/AMGT_HARVST.TO-HVST-z-1.rebuild-chatter-event-under-the-amended-rule.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-z-1.rebuild-chatter-event-under-the-amended-rule`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~32/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

⚠ **NO CODE PATH IS IN YOUR GRANT, and that is deliberate: `HVST-y-1` ALREADY amended `event_rows`.** You run the
producer; you do not change it. If the rebuild needs a code change, that is a BLOCKING row.

## 1. THE ACT, AND WHAT AUTHORISES IT

**Run the existing producer** -- `publication_gold`'s `build-event` subcommand (`--securities-json`, `--as-of`) --
so the served `chatter_event` gold reflects the amended `C-HV-EVENT-SPINE` (publishers counted over tier-A only).

⛔ **THIS MOVES SERVED OUTPUT, so NEVER-1 applies, and the pair IS SIGNED -- read both halves before you start:**
- COO half: `deliverables/2.0.0_SA_COO_Y/NEVER_WIDEN_COO_HALF_chatter_event_rebuild_20260928.md` @`7f9df49098`
- CTO half: `ledger/NEVER_WIDEN_CTO_HALF_chatter_event_rebuild_20260928.md` @`9fddce21db`

**The blast radius they authorise is exactly ONE NEW S3 OBJECT.** `write_gold` does one conditional put with
`IfNoneMatch="*"` -- **it CANNOT overwrite** -- at
`amgt/harvest/gold/chatter_event/date=<BUILD date>/part-<run_stamp>.parquet`. Every prior snapshot, including the
live 12-row one, stays. **Readers resolve to the NEWEST part by `(date, key)`, never a union.**

**The signed rollback is FORWARD-ONLY:** revert the amendment and rebuild, so a third snapshot restores 12 rows
**by addition**. ⛔ **Never by deletion.**

## 2. THE EXPECTED DIFF -- NAMED, and `HVST-y-1` already proved it in memory

**12 events -> 8.** The 4 spurious ones absent: `992_HK`, `COST`, `DELL`, `MSFT`. **AND 2 SPANS NARROW SO THEIR
`event_id` CHANGES** -- `BA` 09-07..08 -> **09-08**, `HD` 08-17..20 -> **08-18**.

⛔ **`_event_id` IS `sha256(security_key|first_day|last_day)`, so a narrowed span is a NEW ROW WITH A NEW ID.** A
result reporting "8 events" without naming both id moves would pass while silently orphaning two ids.

## 3. BOUNDS

1. **Two mechanical criteria + ONE JUDGMENT. No fourth.**
2. **ONE PUT. One table.** `chatter_daily` is NOT in the signed radius -- ⛔ **if you find yourself rebuilding it,
   the pair does not cover you and a NEW one is owed.** STOP and file a row.
3. **If the read-back mismatches**, the producer raises `HarvestStoreError`. **Report it verbatim and STOP.** The
   distrusted object stays (you may not delete it) and is superseded later. That branch is named in both halves.
4. **The judgment criterion is graded on the SERVED rows**, after the put -- not on the builder's return value.

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-z-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~32/scripts/ac1_rebuild_and_name_the_diff.py</invocation><expect>THE REBUILD LANDS AND THE WHOLE NAMED DIFF IS PROVED ON THE SERVED PLANE. Print, in order: (a) the BEFORE state read from S3 -- the newest chatter_event snapshot's key and its event count, expected 12; (b) the producer's own output verbatim, including write_gold's receipt (uri, key, rows, content_length) and rows == 8; (c) the AFTER state re-read from S3 through publication_gold._latest_gold_snapshot_rows, showing the NEWEST snapshot is now the one just written and carries 8 events; (d) the 4 spurious events ABSENT, each named by security_key and span; (e) the TWO event_id MOVES -- for BA and HD print the old span, the new span, the OLD event_id, the NEW event_id, that they differ, and that the new one equals publication_gold._event_id(security_key, new_first_day, new_last_day). ⛔ Also print that the PRIOR snapshot still EXISTS at its own key -- the signed radius is one ADDED object and the rollback depends on the old one surviving. A run reporting 8 without both id moves and without the prior key's survival FAILS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-z-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~32/scripts/ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE HOLDS ON THE SERVED PLANE, not just in memory. Build the event rows IN MEMORY from the same newest article_security_mention snapshot, and compare them ROW BY ROW against what the SERVED newest chatter_event snapshot now carries -- equal sets, equal event_ids, equal per-row field values, with the denominator printed (8 of 8). Print any difference in full. This is the criterion that would catch a put that landed different bytes than the build produced, which write_gold's own read-back checks only by LENGTH</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-z-1" judgment="true"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~32/scripts/ac4_are_the_served_eight_real.py</invocation><expect>JUDGMENT, PRESENTED AND NOT GRADED -- status UNVERIFIABLE-BY-INSTRUMENT with status_reason naming 3.0.0_SA_CVO at L9 as the oracle. ARE THE 8 EVENTS THE SERVED TABLE NOW CARRIES THE REAL COVERAGE BURSTS? Read them from S3, not from the builder. For each print security, span, lead_headline, articles_total, publishers_distinct, tier_a/tier_b, and the headlines of every article in the span; then state per event whether the lead names what the burst was about, and where it does not, what the span actually looks like. Andrew's standard: an event about a DIFFERENT company's product is not this security's burst -- that is the test the 4 removed events failed. Present the text; record NO verdict of your own</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

No delete of any kind. No `chatter_daily`. No code change. No vendor call. No portal work. It does not grade FWD-6
-- that is the CVO's at L9 and the CTO's at L10.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. ⛔ **AC1's "prior snapshot still exists" clause is the never-widen half made checkable.** The signed rollback is
   restore-by-addition, which requires the old object to survive. **A criterion that does not verify the rollback's
   own precondition is not verifying the sign-off.**
2. **AC2 exists because `write_gold`'s read-back compares LENGTH ONLY** (`ContentLength != len(body)`). Equal length
   is not equal bytes. Row-by-row against the in-memory build is the real control.
3. **AC4 reads from S3 deliberately.** Round 10's AC4 read the builder's output; this round the whole point is the
   SERVED plane, and a judgment graded on the builder would prove the same thing twice.
4. **No code path in the grant** -- `y-1` amended `event_rows` and this cell must not re-amend it. That also keeps
   the never-widen radius honest: the signed act is a PUT, not a code change.

<risk>SERVED</risk>
<status>pending</status>
<round>11</round>
<slot>~32</slot>
<fabric>site-z</fabric>
