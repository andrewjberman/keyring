# AMGT_HARVST task order -- `HVST-b-2` -- ROUND 13 cell 2 of 2: REBUILD `chatter_event` ONE STORY PER EVENT. This MOVES SERVED OUTPUT -- now user-visible -- under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-b-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~39</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the gold write path; this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention and silver article parts, and ONE PUT on amgt/harvest/gold/chatter_event (the grant HVST-a-4 exercised). A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a rebuild that loses or splits one of the six one-company events, and a judgment graded on the builder's output instead of the SERVED rows. AC1 and AC4 are those two tests.
</preflight>

## 0. BEGIN ONLY WHEN BOTH HOLD

1. `HVST-b-1` is `complete` and merged on CLOUD (you are the same worker; the issuer continues you with its merge named).
2. BOTH never-widen halves are COMMITTED and named to you by the issuer:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round13/NEVER_WIDEN_HALF_COO_B2.md` and
   `1.0.0_SA_CTO~Z`'s half. **Read both and act only inside them.** They name the expected diff, read from `b-1`'s merged
   rule; where they and this face differ, the halves win.

## 1. THE STANDING CLAUSES

1. **NO S3 DELETE of any kind** (decomp `s.14a`). ONE PUT. On a failed read-back (`HarvestStoreError`) report verbatim
   and STOP; the distrusted object stays.
2. **NO VENDOR CALL. NO CODE CHANGE** -- `b-1` changed the producer. **ONE table**; `chatter_daily` is not in the radius.
3. **THIS TABLE IS NOW SERVED TO USERS:** the deployed scoped API reads the newest `chatter_event` part on every
   `/timeline` call (round 12). The put changes what the timeline shows.
4. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~39/scripts/` -- **never `.scratch/`.**
5. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~39/AMGT_HARVST.TO-HVST-b-2.rebuild-chatter-event-one-story-per-event.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-b-2.rebuild-chatter-event-one-story-per-event`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~39/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE ACT

Run `publication_gold`'s `build-event` subcommand (`--securities-json`, `--as-of`) once. `write_gold` makes ONE
conditional put (`IfNoneMatch="*"`) at `amgt/harvest/gold/chatter_event/date=<BUILD date>/part-<run_stamp>.parquet`;
readers take the NEWEST part by `(date, key)`. **At the cut the prefix held 5 parts; the newest,
`date=2026-09-29/part-20260929T002311Z.parquet`, carries 8 events.** Every prior part stays.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-b-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~39/scripts/ac1_rebuild_one_story.py</invocation><expect>THE REBUILD LANDS AND THE STOP LIMB HOLDS ON THE SERVED PLANE. Print in order: (a) BEFORE from S3 -- part count and newest key with its event count (expected 5 parts, 8 events at date=2026-09-29/part-20260929T002311Z.parquet; if different, STOP before the put and file a BLOCKING row); (b) the producer's output verbatim with write_gold's receipt; (c) AFTER re-read through publication_gold._latest_gold_snapshot_rows -- the newest part is the one just written; (d) every prior served event mapped to what it became (kept / split / gone), and the SIX one-company events (992_HK_Equity 02-12, 05-22, 08-13; COST_US_Equity 09-14; HD_US_Equity 08-18; NVDA_US_Equity 06-01) each EXACTLY ONE served event with the same span and tier-A membership, 6 of 6; (e) every event_id unique; (f) every prior part still exists with its ETag unchanged. A run that loses or splits any of the six FAILS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-b-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~39/scripts/ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE ON THE SERVED PLANE: the event rows built IN MEMORY from the same newest mention snapshot equal the SERVED newest chatter_event snapshot ROW BY ROW -- equal event_ids and every field value, denominator printed, any difference printed in full</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-b-2" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~39/scripts/ac4_is_each_event_one_story.py`.
**Read from S3.** For EVERY served event print security, span, lead, tier-A publishers and every headline; and for every
prior event that split or left, what became of its articles. The question the CVO grades: **is each served event ONE
story about its own company, and does its lead name that story?** Present; record NO verdict.

## 4. WHAT THIS CELL DOES NOT DO

No delete, no `chatter_daily`, no code change, no vendor call, no portal work. It does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Same worker as `b-1` (`~39`), continued.** The pair is written after `b-1` merges, against the merged rule.
2. **User-visible now** (standing clause 3): since round 12 the deployed timeline serves the newest part; the COO half
   names every served event that moves, splits or leaves.
3. **AC1 base:** its arms (b)-(f) are build arms that FAIL at the base by construction (no new part); the STOP-limb arm (d)
   holds at the base (the 6 are one event each today). AC2 base: PASSES (round 12's `a-4` AC2 read 8 of 8).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>13</round>
<slot>~39</slot>
<fabric>site-z</fabric>
