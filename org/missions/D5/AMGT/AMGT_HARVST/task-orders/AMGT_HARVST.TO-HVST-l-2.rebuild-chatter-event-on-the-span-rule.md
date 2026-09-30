# AMGT_HARVST task order -- `HVST-l-2` -- ROUND 22 chain 2 of 2: REBUILD `chatter_event` ON THE SPAN RULE. This MOVES SERVED OUTPUT under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-l-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~52</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the gold write path; no scheduled producer writes the chatter_event prefix; this cell deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on silver and the three gold prefixes; ONE PUT on amgt/harvest/gold/chatter_event. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a rebuild whose moved events exceed the pair, or a put the pre-put read did not see coming (another act moving the newest parts or the reader in the same window, round 18 row Z-S41). AC1 is that test; the dry step re-reads the reader's CodeSha256 and the three newest ETags.
</preflight>

## 0. BEGIN ONLY WHEN IT HOLDS

BOTH never-widen halves are COMMITTED and named to you by the issuer:
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round22/NEVER_WIDEN_HALF_COO_L2.md` and
`1.0.0_SA_CTO~Z`'s half. **Read both and act only inside them.** Where they and this face differ, the halves win.

## 1. THE STANDING CLAUSES

1. **NO S3 DELETE of any kind.** ONE PUT, on `chatter_event` only; no mention or daily put. On a failed read-back
   (`HarvestStoreError`), report it verbatim and STOP. The distrusted object stays.
2. **NO VENDOR CALL. NO CODE CHANGE.** The rule is the one merged at `88dbe4af64` (`k-1`: the span rule plus the roundup
   guard at 4).
3. **THIS TABLE IS SERVED TO USERS:** the deployed scoped API serves the newest `chatter_event` part as the `/timeline`
   `events`. The put changes what users see.
4. **AC1 is write-once.** Make the pre-put arm a SEPARATE dry step that you run FIRST.
   - It accepts no arguments, so it cannot be re-run silently (row `Z-W45-S4`).
   - It records to an `l2_*` file the three newest keys and ETags and the scoped API's CodeSha256, each beside the
     halves' value.
   - It prints STOP on any difference.

   Never pipe the act's output through `head`. Post-act verification is a separate read-only script.
5. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~52/scripts/`; outputs named `l2_*`
   -- **never `.scratch/`.** Never run another cell's script in place (round 21's `k1_ac2_dry_rebuild.py` writes into
   its own committed folder); import or copy it.
6. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~52/AMGT_HARVST.TO-HVST-l-2.rebuild-chatter-event-on-the-span-rule.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-l-2.rebuild-chatter-event-on-the-span-rule`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~52/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE ACT

Run `python -m lib.research.harvest.publication_gold build-event` ONCE, with `--as-of <today UTC>` and the securities file
the halves name. `write_gold` makes ONE conditional put (`IfNoneMatch="*"`) at
`amgt/harvest/gold/chatter_event/date=<as-of>/part-<run_stamp>.parquet`.
- **At the cut:** the newest part is `date=2026-09-29/part-20260929T192706Z.parquet` (8 events).
- Every prior part stays.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-l-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~52/scripts/l2_ac1_post_act_verify.py</invocation><expect>THE REBUILD LANDED INSIDE THE PAIR ON THE SERVED PLANE, read after the act from S3: (a) the newest chatter_event part is the one this cell wrote, with its ETag and row count, and the BEFORE state recorded by the dry step equal to the halves; the newest mention and daily parts unchanged (key and ETag); (b) every served event mapped to what it became (KEPT / CHANGED / MERGED / GONE) against the pair's expected diff, with ANY event the pair did not name printed as OUTSIDE THE PAIR (a run with one such event FAILS); (c) every event_id unique; (d) every prior event part still exists with its ETag unchanged</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-l-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~52/scripts/l2_ac2_served_equals_rebuildable.py</invocation><expect>C-HV-GOLD-REBUILDABLE ON THE SERVED PLANE: the chatter_event rows built IN MEMORY from the same inputs under the merged rule equal the SERVED newest event part ROW BY ROW, every field, denominator printed, any difference printed in full</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-l-2" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~52/scripts/l2_ac4_changed_events.py`, **read from
S3.** For every CHANGED served event, print:
- security, span and lead;
- every member with publisher, day, tier and guard status.

**Is it ONE story about its own company, and does its lead name that story?** Present; record NO verdict.

## 4. WHAT THIS CELL DOES NOT DO

No delete, no mention or daily put, no code change, no deploy, no route mount, no vendor call, no portal work.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Cut now, independent of `l-1`**, per the CTO's ruling @`3100474cde`: `l-1` is outcome-identical by construction.
2. **The pair is written from the rule at `88dbe4af64` and a signing-time re-run of the `k-1` dry rebuild.**
   - Expected: KEPT 5; CHANGED 3; GONE 0.
     - 992_HK 08-13..08-14.
     - AMZN 09-06..09-07, 5 articles, led by bbg's first report.
     - HD 08-17..08-18, led by barrons' "Home Depot Stock Rises as Earnings Defy Housing Slump". This is a disclosed
       lead change from today's bbg piece (`Z-W50-S1`); its start is a day early (ruling 3, accepted and disclosed).
   - The 3 changed events get new `event_id`s.
3. **Base:** AC1 FAILS at the base by construction (no new part). AC2 FAILS at the base, because the served part is the
   per-day rule.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>22</round>
<slot>~52</slot>
<fabric>site-z</fabric>
