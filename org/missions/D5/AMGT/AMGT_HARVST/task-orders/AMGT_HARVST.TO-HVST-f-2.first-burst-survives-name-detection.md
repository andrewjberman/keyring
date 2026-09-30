# AMGT_HARVST task order -- `HVST-f-2` -- ROUND 17 cell 2 of 2: A SECURITY'S FIRST BURST SURVIVES NAME DETECTION (`Z-W40-S1`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-f-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~44</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on publication_gold.py's event rule; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention and chatter_event snapshots and the silver article parts. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a fix that forms the fixture's event by loosening the story link (so unrelated headlines chain), or one that moves a served event. AC2 prints the 8 served events; the fixture's variant 2 and a planted two-story control show the link did not loosen.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL.** If your change moves ANY served event, file a BLOCKING row and stop. The
   served move would need a never-widen pair and its own cell; do not tune the rule to keep an event.
2. **THE FIXTURE IS A MECHANISM TEST, never a held-out grade.** Print it under a line reading "FIXTURE -- MECHANISM TEST,
   NOT A HELD-OUT GRADE". Reuse the planted fixture of `HVST-c-1`:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~40/scripts/ac2_burst_shape_census.py` (~:149-200,
   variants 1 and 2; READ ONLY -- copy what you need into your own scripts).
3. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~44/scripts/` -- **never `.scratch/`,
   never another worker's folder.**
4. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~44/AMGT_HARVST.TO-HVST-f-2.first-burst-survives-name-detection.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-f-2.first-burst-survives-name-detection`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~44/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE DEFECT AND THE RULING (`ledger/ROUND_ANALYSIS.round16.md` @`f424435829`, s.2.2; row `AMGT_HARVST-Z-W40-S1`)

`publication_gold._security_name_tokens` (~:917) INFERS a security's name from its titled tier-A headlines: a stem carried
by >= 3/4 of them on >= `_STORY_NAME_MIN_DAYS` (3) distinct days. `_story_terms` (~:938) then strips those stems before
linking headlines into stories. **When a security's only coverage is one multi-day story, the story's own words pass that
test** ("quantum", "battery", "plant"). They are stripped, the paraphrased headlines share no term, and the burst forms
**0 events** (`HVST-c-1` fixture variant 1). Variant 2 (the same story among other coverage) strips only "zorbex" and forms
the event. **RULED: fix name detection so a security's first burst survives.**

**An issuer's pointer, not a constraint:** every mention row already carries `match_forms` -- the aliases that actually hit
the text (one span, one count since round 16). The security's name can be read from the stems of its own matched aliases,
instead of (or bounding) the inference from headline frequency. Choose the mechanism; the criteria below grade the
outcome.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-f-2"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with the new name-detection tests NAMED in the -rA output (a security whose only coverage is one multi-day story keeps that story's words and forms its event; a security's own name is still stripped; two unrelated stories of one security still do not chain); the pass count BEFORE and AFTER printed (base: 172 passed) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-f-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~44/scripts/ac2_served_events_unmoved.py</invocation><expect>THE SERVED ARM: event_rows under the NEW rule over the SERVED newest article_security_mention snapshot (with silver headlines, exactly as build_event reads them) equals the SERVED newest chatter_event snapshot ROW BY ROW -- 8 of 8, every field, any difference printed in full; and per served security the name stems the rule strips, old vs new</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-f-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~44/scripts/ac3_fixture_mechanism.py</invocation><expect>under the line "FIXTURE -- MECHANISM TEST, NOT A HELD-OUT GRADE", OLD rule vs NEW rule on: variant 1 (the story is the security's only coverage; old 0 events, new 1 event spanning its qualifying days); variant 2 (the story among other coverage; the event unchanged between old and new); and a planted CONTROL of two unrelated multi-day stories of one security with no other coverage (new rule: they do NOT merge into one event). Per variant the stripped name stems and the events formed, with span, articles and lead</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No gold write, no alias change, no tier change, no vendor call. It does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Independent of `f-1`** (disjoint write surfaces: `f-1` changes no code). Both run in parallel, `~43` and `~44`.
2. **A served move is out of scope by design:** the ruling says "any served move goes under a pair". The expected outcome
   is 0 events moved; a moved event stops the cell at BLOCKING, and the recut adds a paired rebuild cell.
3. **Base:** suite 172 passed (the `e-1` drain). AC2 PASSES at the base (the served event part equals `event_rows` over the
   served mention part, `e-2` AC2). AC3 FAILS at the base by construction: variant 1 forms 0 events (`c-1` AC2).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>17</round>
<slot>~44</slot>
<fabric>site-z</fabric>
