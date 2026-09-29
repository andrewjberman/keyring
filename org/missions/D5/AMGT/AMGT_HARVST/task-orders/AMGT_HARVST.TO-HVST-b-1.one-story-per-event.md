# AMGT_HARVST task order -- `HVST-b-1` -- ROUND 13 cell 1 of 2: AN EVENT IS ONE STORY -- the rule, proved in memory, under a STOP limb

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-b-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~39</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on publication_gold.py; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention snapshot, the newest chatter_event snapshot and the silver article parts. NO PUT. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a per-story rule that DELETES a real event because the grouper under-merges it (NVDA 06-01: one PC story read as three, each 1 tier-A). AC1's STOP limb is that adversary's test.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL.** This cell changes the producer's rule and proves it IN MEMORY. The served
   rebuild is `HVST-b-2`, under its own never-widen pair.
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~39/scripts/` -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~39/AMGT_HARVST.TO-HVST-b-1.one-story-per-event.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-b-1.one-story-per-event`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_publication_gold_event.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~39/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CONTRACT THIS CELL IMPLEMENTS -- `C-HV-EVENT-SPINE`, L10 addendum round 12 (read it at the bytes)

`org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` ~:704-710 (`1.0.0_SA_CTO~Z`, @`094cc1f110`), in substance:
**an event is ONE STORY, not one day.** The qualifying rule (tier A+B articles >= 2 from >= 2 publishers each contributing
a tier-A article, merged across gaps <= 1 day; `EVENT_MIN_ARTICLES = 2`, `EVENT_MIN_PUBLISHERS = 2`,
`EVENT_MAX_GAP_DAYS = 1` at `publication_gold.py:759-761`) applies to EACH STORY the grouper forms, so an unrelated-story
day yields one event per qualifying story, or none. The lead is the story's own earliest tier-A headline. **`event_id`
carries the story, so two events on one day never collide. Calendar words (month and day names) never link two
headlines.** Read the addendum yourself; where this face and the addendum differ, the addendum wins.

**The grouper today** (`_story_tokens` ~:811, `_event_stories` ~:833, `_story_lead`, `event_rows`; `HVST-a-3`): content
tokens of length >= 3, a stopword list, one plural "s" stripped, tokens present in every tier-A headline of the event
dropped, tier-A articles single-linked on >= 1 shared token.

**Its two known defects, measured at round 12's L9 (`ADJUDICATION_v20.md` @`19dfdd2579`):**
1. **UNDER-merge:** `NVDA_US_Equity` 2026-06-01 -- three tier-A articles about ONE Nvidia PC push read as three stories;
   their only shared token ("nvidia") is dropped as ubiquitous, "pc" is below the 3-character floor, and "pcs" is not
   reduced to "pc". **Applied per story, this under-merge would DELETE a real event.**
2. **Calendar link:** `BA_US_Equity` 2026-09-08's deliveries pair linked on the single token "august".

## 2. WHAT TO BUILD

1. **Calendar words never link:** month and day names (and their common abbreviations) join the tokens that cannot say
   which story a headline belongs to.
2. **Fix the under-merge** so a story that is one company event reads as one story -- by a mechanism you choose and
   STATE (with its failure mode), from fields the rows already carry. It must keep `NVDA_US_Equity` 2026-06-01 one story.
3. **Per-story qualification:** `event_rows` forms stories, then applies the qualifying rule to each story; each
   qualifying story is one event with its own span, members, counts and lead.
4. **`event_id` carries the story** and is unique across the output; deterministic from the rows (no clock, no order).
5. Keep `event_rows` PURE and deterministic.
6. Tests: calendar words do not link; an unrelated-story day yields per-story events (or none); two qualifying stories on
   one day get distinct ids; a paraphrased one-story event (the NVDA shape) stays one event. Change no other assertion.

## 3. BOUNDS

1. **Three mechanical criteria. No judgment here** -- the round's judgment is on `HVST-b-2`, on SERVED rows.
2. No schema change beyond what the addendum names; no other table; no threshold change.

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-b-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~39/scripts/ac1_one_story_in_memory.py</invocation><expect>OVER THE LANDED DATA, IN MEMORY: build event rows with the NEW rule from the newest article_security_mention snapshot + silver headlines exactly as build_event does, and set them beside the SERVED newest chatter_event snapshot (8 events). Print every served event and what it becomes (kept / split into N / gone), and every new event with security, span, story headlines, tier-A publishers, lead and event_id. STOP LIMB -- PASS only if ALL of: (a) each of the SIX events the round-12 L9 graded as ONE company event -- 992_HK_Equity 2026-02-12, 2026-05-22, 2026-08-13; COST_US_Equity 2026-09-14; HD_US_Equity 2026-08-18; NVDA_US_Equity 2026-06-01 -- maps to EXACTLY ONE new event with the SAME span and the SAME tier-A membership (6 of 6); (b) every new event_id is unique; (c) no two headlines in any story are linked only by a calendar word. Print the outcome for BA_US_Equity 2026-08-26 and 2026-09-08 (expected to split or leave; named, not required). At the base (c) FAILS on BA 09-08 ("august")</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-b-1"><invocation>python -m pytest lib/research/harvest/tests/test_publication_gold_event.py -rA --tb=line</invocation><expect>the event tests pass with the new tests NAMED in the -rA output (calendar words do not link; per-story events on an unrelated-story day; distinct ids for two stories on one day; the NVDA-shape paraphrase stays one event); the pass count BEFORE and AFTER printed (base: 15 passed) and the collected count not falling except by a replaced assertion, which is named</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-b-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~39/scripts/ac3_rebuildable_twice.py</invocation><expect>C-HV-GOLD-REBUILDABLE HOLDS UNDER THE NEW RULE: two in-memory builds over the same landed input serialise to byte-identical parquet (both sha256 and the row count printed), including a build over the input in reversed row order</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

It writes no gold, changes no threshold, and does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Split from the rebuild for the NEVER-1 reason round 12 used:** the pair reads the expected outcome from the
   producer's own rule at signing, which exists only after this cell merges.
2. **AC1's STOP limb is the CTO's (analysis s.2.1), made mechanical.** The six events are the ones `ADJUDICATION_v20.md`
   graded as one company event; the check compares SPAN and TIER-A MEMBERSHIP, not the id (every id moves by the
   addendum's own "event_id carries the story").
3. **AC1 base:** its arm (c) FAILS at the base (BA 09-08 linked on "august"); arms (a) and (b) hold at the base. AC2
   base: 15 passed (the `a-3` drain). Scripts are worker-written as in every round of this project.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>13</round>
<slot>~39</slot>
<fabric>site-z</fabric>
