# AMGT_HARVST task order -- `HVST-a-4` -- ROUND 12 chain 2 of 3, cell 2 of 2: REBUILD `chatter_event` WITH THE PLURALITY LEAD. This MOVES SERVED OUTPUT under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-a-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~36</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the gold write path; this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention and silver article parts, and ONE PUT on amgt/harvest/gold/chatter_event (the same grant HVST-z-1 exercised). A refusal is a BLOCKING row, never a workaround.
comp-adversary: RUN at L5 -- the adversary is a rebuild that moves an event_id or a span while the only intended change is the lead, and a judgment graded on the builder's output instead of the SERVED rows. AC1 and AC4 are those two tests.
</preflight>

## 0. BEGIN ONLY WHEN BOTH HOLD

1. `HVST-a-3` is `complete` and merged on CLOUD (you are the same worker; the issuer continues you with its merge
   commit named).
2. BOTH never-widen halves for this rebuild are COMMITTED and named to you by the issuer:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round12/NEVER_WIDEN_HALF_COO_A4.md` and
   `1.0.0_SA_CTO~Z`'s half. **Read both before you start and act only inside them.** They name the expected diff,
   read from `a-3`'s merged rule; where they and this face differ, the halves win.

## 1. THE STANDING CLAUSES

1. ⛔ **NO S3 DELETE. NOT OF AN OBJECT, A NONCURRENT VERSION, OR A DELETE MARKER. EVER** (decomp `s.14a`). The pair
   authorises exactly ONE PUT. On a failed read-back (`HarvestStoreError`) report it verbatim and STOP; the distrusted
   object stays.
2. **NO VENDOR CALL. NO CODE CHANGE** -- you run the producer; `a-3` changed it. A needed code change is a BLOCKING row.
3. **ONE table.** `chatter_daily` is NOT in the radius.
4. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/` -- **never `.scratch/`.**
5. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~36/AMGT_HARVST.TO-HVST-a-4.rebuild-chatter-event-with-the-plurality-lead.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-a-4.rebuild-chatter-event-with-the-plurality-lead`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~36/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE ACT

Run the existing producer -- `publication_gold`'s `build-event` subcommand (`--securities-json`, `--as-of`) -- exactly
as `HVST-z-1` did in round 11. `write_gold` makes ONE conditional put (`IfNoneMatch="*"`, it cannot overwrite) at
`amgt/harvest/gold/chatter_event/date=<BUILD date>/part-<run_stamp>.parquet`; readers resolve to the NEWEST part by
`(date, key)`, never a union. **At the cut the prefix held 4 parts; the newest,
`date=2026-09-28/part-20260928T210944Z.parquet`, carries 8 events.** Every prior part stays.

**The expected diff, from `a-3`'s rule (the halves restate it at the merged bytes):** the SAME 8 events -- same
`event_id`, span, `article_keys` and counts -- with `lead_article_key` / `lead_headline` moved ONLY on events whose
plurality story is not the first story. `BA_US_Equity` 2026-09-08 is expected to move.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-a-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/ac1_rebuild_and_name_the_lead_moves.py</invocation><expect>THE REBUILD LANDS AND ONLY THE LEADS MOVE, PROVED ON THE SERVED PLANE. Print in order: (a) the BEFORE state from S3 -- part count and the newest key with its event count (expected 4 parts, 8 events at date=2026-09-28/part-20260928T210944Z.parquet; if different, STOP before the put and file a BLOCKING row); (b) the producer's output verbatim with write_gold's receipt (uri, key, rows, content_length); (c) the AFTER state re-read through publication_gold._latest_gold_snapshot_rows -- the newest part is the one just written; (d) per event: event_id, span and article_keys EQUAL to the prior snapshot 8 of 8, and each lead OLD -> NEW with moved yes/no, the moved count printed; (e) every prior part still exists at its own key with its ETag unchanged. A run that moves any event_id, span or membership FAILS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-a-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE ON THE SERVED PLANE: build the event rows IN MEMORY from the same newest mention snapshot and compare ROW BY ROW with the SERVED newest chatter_event snapshot -- equal event_ids and every field value, denominator printed (8 of 8 rows, fields compared counted), any difference printed in full</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-a-4" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9 as the oracle). Script:
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/ac4_does_the_lead_name_the_burst.py`.
**Read from S3, not from the builder.** For EVERY event whose articles form more than one story under `a-3`'s stated
grouping -- not only Boeing's two -- print: security, span, the stories with their tier-A counts and every headline,
and the served lead. The question the CVO grades: **does the lead name what the burst was about?** Also print, for
each multi-story event, whether its stories are about the SAME company event or unrelated ones -- the CTO left
"is a multi-story day one event?" open for exactly this evidence. Present the text; record NO verdict of your own.

## 4. WHAT THIS CELL DOES NOT DO

No delete, no `chatter_daily`, no code change, no vendor call, no portal work, no event split. It does not grade
FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Same worker as `a-3` (slot `~36`), continued, not respawned** -- it keeps what it learned about the grouping.
2. **The pair is written AFTER `a-3` merges**, against the merged rule; the CTO half for `z-1` said a rebuild after
   the route serves "owes a fresh pair" -- and if `a-2` has deployed first, this rebuild moves USER-VISIBLE output,
   which the COO half will state as measured at signing.
3. **AC1 base:** FAILS at the base by construction (no new part, no lead moved); its (e) arm holds at the base.
   **AC2 base:** PASSES (round 11's `z-1` AC2 read 8 of 8, 104 of 104 fields against the same snapshot).
4. **AC4 widens round 11's judgment on purpose** (the analysis: "re-reads EVERY multi-story event, not only
   Boeing's two"), and adds the same-event-or-unrelated print so the open "one event?" question gets its evidence.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>12</round>
<slot>~36</slot>
<fabric>site-z</fabric>
