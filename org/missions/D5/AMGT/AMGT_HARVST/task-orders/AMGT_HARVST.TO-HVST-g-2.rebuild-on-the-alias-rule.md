# AMGT_HARVST task order -- `HVST-g-2` -- ROUND 18 cell 2 of 2: REBUILD `article_security_mention`, `chatter_daily`, `chatter_event` ON THE NEW ALIAS RULE. This MOVES SERVED OUTPUT under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-g-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~45</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the gold write path; no scheduled producer writes these prefixes; this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the pool universe, silver and the three gold prefixes; ONE PUT each on amgt/harvest/gold/{article_security_mention,chatter_daily,chatter_event}. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a rebuild whose moved rows exceed the pair, and a judgment graded on the builder's output instead of the SERVED rows. AC1 and AC4 are those two tests.
</preflight>

## 0. BEGIN ONLY WHEN BOTH HOLD

1. `HVST-g-1` is `complete` and merged on CLOUD (you are the same worker; the issuer continues you with its merge named).
2. BOTH never-widen halves are COMMITTED and named to you by the issuer:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round18/NEVER_WIDEN_HALF_COO_G2.md` and
   `1.0.0_SA_CTO~Z`'s half. **Read both and act only inside them.** Where they and this face differ, the halves win.

## 1. THE STANDING CLAUSES

1. **NO S3 DELETE of any kind** (decomp `s.14a`). ONE PUT per table, in the order mention -> daily -> event (each reads the
   newest part of the one before). On a failed read-back (`HarvestStoreError`) report verbatim and STOP; the distrusted
   object stays and no later table is built.
2. **NO VENDOR CALL. NO CODE CHANGE** -- `g-1` changed the rule.
3. **THESE TABLES ARE SERVED TO USERS:** the deployed scoped API serves the newest `chatter_event` part as `/timeline`
   `events` and the newest `chatter_daily` part as its `series`. The puts change what the timeline shows.
4. **Securities input:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/securities.universe.json`
   (written by `g-1`) for all three builds.
5. **AC1 is write-once:** make the pre-put arm (a) a separate dry step you run FIRST, and never pipe the act's output
   through `head` (round 16 row `Z-W42-S1`). Post-act verification is a separate read-only script.
6. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/`; output files named `g2_*` -- **never `.scratch/`.**
7. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~45/AMGT_HARVST.TO-HVST-g-2.rebuild-on-the-alias-rule.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-g-2.rebuild-on-the-alias-rule`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE ACT

Run `python -m lib.research.harvest.publication_gold` `build-mention`, then `build-daily`, then `build-event`, each with
`--securities-json <the file above>` and `--as-of <today UTC>`, once each. `write_gold` makes ONE conditional put
(`IfNoneMatch="*"`) per table at `amgt/harvest/gold/<table>/date=<as-of>/part-<run_stamp>.parquet`. **At the cut (5 / 6 / 7
parts):** mention newest `date=2026-09-29/part-20260929T112204Z.parquet` (275 rows); daily newest
`date=2026-09-29/part-20260929T112222Z.parquet` (51,952 rows); event newest `date=2026-09-29/part-20260929T092439Z.parquet`
(8 events). Every prior part stays.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-g-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/ac1_post_act_verify.py</invocation><expect>THE REBUILD LANDED INSIDE THE PAIR ON THE SERVED PLANE, read after the act from S3: (a) per table the newest part is the one this cell wrote, with its ETag and row count, and the BEFORE state (recorded by the dry step before the first put) equal to section 2; (b) per table the moved rows set against the pair's expected diff -- every moved security named, and ANY moved row the pair did not name printed as OUTSIDE THE PAIR (a run with one such row FAILS); (c) every served event mapped to what it became (kept / moved / gone) and every new event named; (d) every event_id unique; (e) every prior part still exists with its ETag unchanged</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-g-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE ON THE SERVED PLANE: for each of the three tables, the rows built IN MEMORY from the same inputs equal the SERVED newest snapshot ROW BY ROW -- equal keys and every field value, denominator printed per table, any difference printed in full</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-g-2" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/ac4_new_and_moved_events.py`. **Read from
S3.** Every NEW or MOVED served event, with security, span, lead, tier-A publishers and every headline. **Is it ONE story
about its own company, and does its lead name that story?** Present; record NO verdict.

## 4. WHAT THIS CELL DOES NOT DO

No delete, no code change, no vendor call, no portal work. It does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Same worker as `g-1` (`~45`), continued.** The pair is written after `g-1` merges, from the merged rule and `g-1`'s AC2.
2. **AC1 is shaped as a post-act read** on round 16's lesson (`Z-W42-S1`, `Z-W42-S2`): a write-once invocation cannot be
   re-run by a grader, so the graded criterion is the read, and the act plus its dry pre-check are standing clauses.
3. **Base:** AC1 FAILS at the base by construction (no new parts). AC2 PASSES at the base (round 16 `e-2` AC2 read 3 of 3
   tables equal).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>18</round>
<slot>~45</slot>
<fabric>site-z</fabric>
