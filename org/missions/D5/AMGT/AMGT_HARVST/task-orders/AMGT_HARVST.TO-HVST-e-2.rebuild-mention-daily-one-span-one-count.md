# AMGT_HARVST task order -- `HVST-e-2` -- ROUND 16 cell 2 of 2: REBUILD `article_security_mention` and `chatter_daily` WITH ONE SPAN, ONE COUNT. This MOVES SERVED OUTPUT under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-e-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~42</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the gold write path; no scheduled producer writes these prefixes; this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on silver and the three gold prefixes; ONE PUT each on amgt/harvest/gold/{article_security_mention,chatter_daily}. NO put on chatter_event. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a rebuild whose moved rows exceed the pair, or one that silently moves an event the served event part no longer matches. AC1 and AC2 are those two tests.
</preflight>

## 0. BEGIN ONLY WHEN BOTH HOLD

1. `HVST-e-1` is `complete` and merged on CLOUD (you are the same worker; the issuer continues you with its merge named).
2. BOTH never-widen halves are COMMITTED and named to you by the issuer:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round16/NEVER_WIDEN_HALF_COO_E2.md` and
   `1.0.0_SA_CTO~Z`'s half. **Read both and act only inside them.** Where they and this face differ, the halves win.

## 1. THE STANDING CLAUSES

1. **NO S3 DELETE of any kind** (decomp `s.14a`). ONE PUT per table, mention THEN daily (daily reads the newest mention
   part). On a failed read-back (`HarvestStoreError`) report verbatim and STOP; the distrusted object stays and daily is
   not built.
2. **NO VENDOR CALL. NO CODE CHANGE** -- `e-1` changed the matcher. **NO `chatter_event` put:** events are expected not to
   move; AC2 proves the served event part still equals a rebuild from the new mention part.
3. **THESE TABLES ARE SERVED TO USERS:** the deployed scoped API serves the newest `chatter_daily` part as the `/timeline`
   `series`. The puts change what the timeline shows.
4. **Securities input:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/securities.universe.json`
   (READ ONLY).
5. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~42/scripts/`; output files named `e2_*`, never overwriting
   `e-1`'s -- **never `.scratch/`.**
6. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~42/AMGT_HARVST.TO-HVST-e-2.rebuild-mention-daily-one-span-one-count.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-e-2.rebuild-mention-daily-one-span-one-count`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~42/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE ACT

Run `python -m lib.research.harvest.publication_gold` `build-mention`, then `build-daily`, each with `--securities-json
<the file above>` and `--as-of <today UTC>`, once each. `write_gold` makes ONE conditional put (`IfNoneMatch="*"`) per
table at `amgt/harvest/gold/<table>/date=<as-of>/part-<run_stamp>.parquet`. **At the cut (4 / 5 / 7 parts):** mention
newest `date=2026-09-29/part-20260929T092419Z.parquet` (275 rows); daily newest `date=2026-09-29/part-20260929T092435Z.parquet`
(51,952 rows); event newest `date=2026-09-29/part-20260929T092439Z.parquet` (8 events). Every prior part stays.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-e-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~42/scripts/ac1_rebuild_two_tables.py</invocation><expect>THE REBUILD LANDS INSIDE THE PAIR ON THE SERVED PLANE. Print in order: (a) BEFORE from S3 -- per table the part count and newest key with its row count (expected as at the cut in section 2; if different, STOP before the first put and file a BLOCKING row); (b) each producer's output verbatim with write_gold's receipt; (c) AFTER re-read through publication_gold._latest_gold_snapshot_rows -- the newest mention and daily parts are the ones just written and the newest event part is unchanged; (d) per table the moved rows set against the pair's expected diff -- every moved security named, and ANY moved row the pair did not name printed as OUTSIDE THE PAIR (a run with one such row FAILS); (e) every prior part still exists with its ETag unchanged</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-e-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~42/scripts/ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE ON THE SERVED PLANE: the rows built IN MEMORY from the same inputs equal the SERVED newest mention and daily snapshots row by row, AND event_rows over the newly served mention part equals the SERVED newest chatter_event part row by row -- denominator printed per table, any difference printed in full</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-e-2" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~42/scripts/ac4_one_count_per_mention.py`. **Read
from S3 and the silver text.** For the AMZN 09-06 crash report (bbg `TKYJAAVTTCZL00`) and every row whose tier moved, print
the served `mention_count` and `match_forms` beside every matched span in the article text (block, offset, the words
around it). The question the CVO grades: **does each served count equal one per actual mention of that company?** Present;
record NO verdict.

## 4. WHAT THIS CELL DOES NOT DO

No delete, no event put, no code change, no vendor call, no portal work. It does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Same worker as `e-1` (`~42`), continued.** The pair is written after `e-1` merges, against the merged matcher and
   `e-1` AC2's printed moves.
2. **Radius: mention + daily, measured event.** The ruling names mention and daily and says the pair measures events
   (expected 0 moved). A moved event in `e-1` AC2 stops the chain at `e-1` (BLOCKING row), so it never reaches this put.
3. **AC4 widens the ruling's sample** ("the 09-06 crash report and two co-mention articles") to every tier-moved row (8
   today), because tier moves were not in the ruling's premise (record note 1 of `e-1`).
4. **AC1 base:** its arms (b)-(e) FAIL at the base by construction; arm (a) holds. AC2 base: PASSES (round 15 `d-2` AC2).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>16</round>
<slot>~42</slot>
<fabric>site-z</fabric>
