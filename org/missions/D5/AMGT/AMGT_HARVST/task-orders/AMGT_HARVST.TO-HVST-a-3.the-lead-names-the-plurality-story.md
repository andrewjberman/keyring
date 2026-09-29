# AMGT_HARVST task order -- `HVST-a-3` -- ROUND 12 chain 2 of 3, cell 1 of 2: THE LEAD NAMES THE PLURALITY STORY -- the rule, proved in memory over the landed data

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-a-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~36</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on publication_gold.py; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention gold snapshot and the silver article parts (the headline source). NO PUT. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a rule change that also moves an event's SPAN or article set, so the served event_ids change under a cell that was only meant to change which headline leads. AC1 pins the ids.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL.** This cell changes the producer's rule and proves it IN MEMORY. The
   served rebuild is `HVST-a-4`, under its own never-widen pair.
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/` -- **never `.scratch/`.**
3. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~36/AMGT_HARVST.TO-HVST-a-3.the-lead-names-the-plurality-story.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-a-3.the-lead-names-the-plurality-story`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_publication_gold_event.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~36/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING THIS CELL IMPLEMENTS -- `1.0.0_SA_CTO~Z`, round-11 analysis section 2, verbatim

> **The lead is the headline of the story that carries the MOST tier-A articles in the event; ties go to the
> earliest.** The mechanism (how articles are grouped into stories) is the cell's to choose and state, from the
> silver fields already carried; no new vendor field.

**The finding it answers (measured at L9, 8 served events):** `event_rows` (`publication_gold.py:802-882`) sorts the
event's articles by `_event_sort_key` (tier, then `published_utc`, then `article_key`, `:785-794`) and takes the first
as the lead (`:862`). That names the FIRST story, not the dominant one: right on 6 of 8 events (one story each),
wrong on both Boeing days -- `BA_US_Equity` 2026-08-26 carries two unrelated stories, and on 2026-09-08 the lead is
the runway overshoot while the plurality is August deliveries. The tie-break comment cites "section 1" of the
original `h-6` cell text; that is cell text, not contract text, and the CTO ruled the lead rule an implementation
choice under the unchanged `C-HV-EVENT-SPINE`.

**NOT ruled, and NOT this cell's:** whether a multi-story day is ONE event. **Do not split events.** Spans,
`article_keys`, counts and `event_id` stay exactly as the current rule makes them; only `lead_article_key` and
`lead_headline` may move.

## 2. WHAT TO BUILD

1. In `event_rows`, group the event's tier A/B articles into STORIES by a deterministic mechanism you choose from
   fields the mention rows already carry (the `title` join is how `build_event` supplies headlines). **State the
   mechanism in one paragraph in your instance**, with its failure mode (what it would wrongly merge or split).
2. The lead = the first article, by the existing `_event_sort_key`, of the story with the most TIER-A articles;
   ties between stories go to the story whose earliest article is earliest. An event with one story leads exactly
   as today.
3. Keep `event_rows` PURE (no I/O, no clock) and deterministic: the same input yields the same bytes.
4. Update the one unit test that pins the old tie-break (`test_publication_gold_event.py` ~:178-181) to the new rule
   and ADD tests for: a two-story event whose later story has more tier-A articles; a tie; a one-story event unchanged.
   Change no other test's assertion.

## 3. BOUNDS

1. **Three mechanical criteria. No judgment here** -- the round's judgment is on `HVST-a-4`, graded on SERVED rows.
2. No span, membership, count or id change on any event. No schema change. No other table.

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-a-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/ac1_new_leads_in_memory.py</invocation><expect>OVER THE LANDED DATA, IN MEMORY: read the newest article_security_mention snapshot and the silver headlines exactly as build_event does, build event rows with the NEW rule, and compare them to the SERVED newest chatter_event snapshot (read via publication_gold._latest_gold_snapshot_rows). Print, per event (denominator 8): security, span, event_id, the story groups with each group's tier-A count and headlines, the OLD lead headline, the NEW lead headline, and whether it moved. PASS only if (a) the event_id set, spans, article_keys and every count equal the served snapshot 8 of 8 -- only lead_article_key / lead_headline may differ; (b) every new lead belongs to a story with the maximum tier-A count in its event; (c) BA_US_Equity 2026-09-08's lead MOVED. At the base the in-memory build equals the served snapshot and (c) FAILS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-a-3"><invocation>python -m pytest lib/research/harvest/tests/test_publication_gold_event.py -rA --tb=line</invocation><expect>the event tests pass with the updated tie-break test and the three new tests NAMED in the -rA output; the pass count BEFORE and AFTER printed, and the collected count not falling except by the one replaced assertion, which is named</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-a-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/ac3_rebuildable_twice.py</invocation><expect>C-HV-GOLD-REBUILDABLE HOLDS UNDER THE NEW RULE: two in-memory builds over the same landed input serialise to byte-identical parquet (print both sha256 and the row count), so the story grouping introduces no order or clock dependence</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

It writes no gold, splits no event, changes no contract text, and does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Split from the rebuild on purpose.** The never-widen half must read the expected outcome from the producer's
   OWN rule at signing (CLAUDE.md NEVER-1), and that rule does not exist until this cell lands. So `a-4`'s pair is
   written against `a-3`'s merged bytes, not predicted here -- the `y-1` -> `z-1` pattern of rounds 10-11.
2. **AC1 (c) is the build arm** (FAILS at the base: the rule is unchanged, so no lead moves); (a) is the adversary's
   test and PASSES at the base (in-memory build equals served, 8 of 8 -- round 11's AC2 proved it on 104 of 104
   fields). Scripts are worker-written, as in every prior round of this project; the base expectation is stated in
   the criterion so the grader can check it.
3. **AC2 base: PASS as expected, measured by this seat at shared HEAD `a0186c364b`: `12 passed`** (a control; the
   build arms are the new tests, which the worker adds).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>12</round>
<slot>~36</slot>
<fabric>site-z</fabric>
