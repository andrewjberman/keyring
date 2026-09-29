# AMGT_HARVST task order -- `HVST-d-2` -- ROUND 15 cell 2 of 2: REBUILD `article_security_mention`, `chatter_daily`, `chatter_event` WITH THE COMMON-NAME ALIASES. This MOVES SERVED OUTPUT under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-d-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~41</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the gold write path; no scheduled producer writes these three prefixes (every part so far is a QA or cell build); this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the pool universe, silver article/listing parts and the three gold prefixes; ONE PUT each on amgt/harvest/gold/{article_security_mention,chatter_daily,chatter_event}. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a rebuild whose moved rows exceed the pair (a false-hit alias, input drift the pair did not name), and a judgment graded on the builder's output instead of the SERVED rows. AC1 and AC4 are those two tests.
</preflight>

## 0. BEGIN ONLY WHEN BOTH HOLD

1. `HVST-d-1` is `complete` and merged on CLOUD (you are the same worker; the issuer continues you with its merge named).
2. BOTH never-widen halves are COMMITTED and named to you by the issuer:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round15/NEVER_WIDEN_HALF_COO_D2.md` and
   `1.0.0_SA_CTO~Z`'s half. **Read both and act only inside them.** They name the expected diff per table, read from
   `d-1`'s merged rule and its AC2 output; where they and this face differ, the halves win (a half may drop `chatter_daily`
   from the radius; then you do not build it).

## 1. THE STANDING CLAUSES

1. **NO S3 DELETE of any kind** (decomp `s.14a`). ONE PUT per table, in the order mention -> daily -> event (each reads the
   newest part of the one before). On a failed read-back (`HarvestStoreError`) report verbatim and STOP; the distrusted
   object stays and no later table is built.
2. **NO VENDOR CALL. NO CODE CHANGE** -- `d-1` changed the alias rule.
3. **THESE TABLES ARE SERVED TO USERS:** the deployed scoped API reads the newest `chatter_event` and `chatter_daily` parts
   on every `/timeline` call. The puts change what the timeline shows.
4. **The securities input is** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/securities.universe.json`
   (written by `d-1` with `universe_securities`' own CLI) for all three builds. Not the `~4` file.
5. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~41/scripts/` -- **never `.scratch/`.**
6. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~41/AMGT_HARVST.TO-HVST-d-2.rebuild-mention-daily-event-with-common-names.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-d-2.rebuild-mention-daily-event-with-common-names`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE ACT

Run `python -m lib.research.harvest.publication_gold` `build-mention`, then `build-daily`, then `build-event`, each with
`--securities-json <the file above>` and `--as-of <today UTC>`, once each. `write_gold` makes ONE conditional put
(`IfNoneMatch="*"`) per table at `amgt/harvest/gold/<table>/date=<as-of>/part-<run_stamp>.parquet`; readers take the
NEWEST part by `(date, key)`. **At the cut (3 / 4 / 6 parts):** mention newest `date=2026-09-24/part-20260924T105025Z.parquet` (263 rows, 55
securities); daily newest `date=2026-09-24/part-20260924T105051Z.parquet` (50,997 rows); event newest
`date=2026-09-29/part-20260929T062617Z.parquet` (7 events). Every prior part stays.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-d-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/scripts/ac1_rebuild_three_tables.py</invocation><expect>THE REBUILD LANDS INSIDE THE PAIR ON THE SERVED PLANE. Print in order: (a) BEFORE from S3 -- per table the part count and newest key with its row count (expected as at the cut in section 2; if different, STOP before the first put and file a BLOCKING row); (b) each producer's output verbatim with write_gold's receipt; (c) AFTER re-read through publication_gold._latest_gold_snapshot_rows -- per table the newest part is the one just written; (d) per table the moved rows set against the pair's expected diff -- every moved security named, and ANY moved row the pair did not name printed as OUTSIDE THE PAIR (a run with one such row FAILS); (e) every served event mapped to what it became (kept / moved / gone) and every new event named; (f) every event_id unique; (g) every prior part still exists with its ETag unchanged</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-d-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/scripts/ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE ON THE SERVED PLANE: for each table rebuilt, the rows built IN MEMORY from the same inputs equal the SERVED newest snapshot ROW BY ROW -- equal keys and every field value, denominator printed per table, any difference printed in full</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-d-2" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~41/scripts/ac4_new_matches_and_events.py`.
**Read from S3.** Two parts: (1) a sample of the NEW (article, security) mention matches -- every one if 40 or fewer,
else 40 drawn with a printed seed plus every new match on a tier-A row -- each with its headline and the alias that hit:
**is each a real mention of that company, or a false hit on a common word?** (2) every NEW or MOVED served event with
security, span, lead, tier-A publishers and every headline: **is it ONE story about its own company, and does its lead
name that story?** Present; record NO verdict.

## 4. WHAT THIS CELL DOES NOT DO

No delete, no code change, no vendor call, no portal work, no event-route wiring. It does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Same worker as `d-1` (`~41`), continued.** The pair is written after `d-1` merges, against the merged rule and `d-1`
   AC2's printed ALIAS/DRIFT attribution.
2. **`chatter_daily` is in the radius by the issuer's reading, carded to the CTO** (`d-1` record note 2): `build_daily`
   reads the newest mention snapshot and the deployed `/timeline` range route serves its series. A daily rebuild also
   extends its day range from 267 days (to 2026-09-24) to the new `--as-of` -- a DRIFT move the pair must name. The CTO's
   half may accept or drop it.
3. **Writers (NEVER-1 count):** every part on the three prefixes so far is a cell build or `2.0.0_SA_COO~Y`'s 09-24 QA
   build; no scheduled producer. The pair re-counts at signing.
4. **AC1 base:** its arms (b)-(g) FAIL at the base by construction (no new parts); arm (a) holds at the base. AC2 base:
   PASSES for event (round 13 `b-2` AC2); mention/daily re-derivation at the base carries the silver DRIFT (118 -> 120
   articles), which is why the pair, not the base, sets the expectation.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~41</slot>
<fabric>site-z</fabric>
