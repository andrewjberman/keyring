# AMGT_HARVST task order -- `HVST-c-1` -- ROUND 14 cell 1 of 1: THE HELD-OUT READ OF THE ONE-STORY RULE, and the burst-shape census

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-c-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~40</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates; this cell reads and counts, writes no gold and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the newest article_security_mention snapshot, the newest chatter_event snapshot and the silver article parts. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a held-out read that reports a PASS because it graded nothing (0 held-out events) or re-cites the in-sample 8 as held-out evidence. AC1 prints the denominator; AC4 lays out the near-misses so a missed burst is visible.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO CODE CHANGE.** This cell reads and counts. Its source is only what the
   harvest already holds (`1.0.0_SA_CTO~Z` ruling, `ledger/ROUND_ANALYSIS.round13.md` s.2.1: "no new vendor leg").
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~40/scripts/` -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~40/AMGT_HARVST.TO-HVST-c-1.held-out-read-and-burst-census.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-c-1.held-out-read-and-burst-census`.
4. **The round-13 pass is IN-SAMPLE and stays so on every surface you write:** the one-story rule
   (`lib/research/harvest/publication_gold.py` at CLOUD `6a91a6efb1` onward, `event_rows`) was tuned in three generations
   on the 8 events of five securities -- **BA_US_Equity, 992_HK_Equity, COST_US_Equity, HD_US_Equity, NVDA_US_Equity** --
   and never re-cite them as held-out evidence.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~40/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING THIS CELL IMPLEMENTS (`ROUND_ANALYSIS.round13.md` s.2.1, read it at the bytes)

The held-out population is articles the rule was never tuned on: securities OTHER than the five above, or captures dated
after the rule froze (the b-2 put, 2026-09-29 06:26Z). Report (a) the held-out denominator and the events the rule forms
on it, each graded at L9 by the b-2 AC4 question; (b) the burst-shape census over the WHOLE harvest: does any burst exceed
3 articles or 1 day? If none, that shape is **UNEXERCISED** and no held-out pass stands for it; (c) if the held-out
denominator is 0, say so -- the round-13 pass is never promoted by default. A planted fixture of the larger shape (5+
articles over 2+ days) MAY be run as a MECHANISM test, labelled a fixture, never a held-out grade.

**Measured by the issuer at the cut (CLOUD `f1de5ca7ce`), your starting point, not your conclusion:** the newest mention
snapshot holds 263 rows over 55 securities; 130 rows over 50 securities are held-out (44 of them tier A or B); the rule
forms **0 events** on the held-out securities; the newest mention is dated 2026-09-15, so no capture postdates the rule;
exactly 1 (security, day) carries more than 3 tier-A/B articles (BA_US_Equity 2026-09-08, 4 -- in-sample); the largest
served event is 3 articles over 1 day. **So the held-out EVENT set is expected to be EMPTY** -- which tests the rule's
precision on nothing. **What a held-out read CAN test here is RECALL:** whether the rule declines a real burst.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-c-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~40/scripts/ac1_held_out_denominator.py</invocation><expect>THE HELD-OUT DENOMINATOR AND WHAT THE RULE FORMS ON IT, from the newest article_security_mention snapshot + silver headlines exactly as build_event reads them: print the held-out population (rows, tier A/B rows, distinct articles, securities, date range) beside the in-sample population; the events event_rows forms on held-out securities, each with security, span, lead, tier-A publishers and every headline; and every held-out STORY with >= 2 tier-A/B articles that did NOT qualify, with the reason (too few articles / too few tier-A publishers). Verdict line: "held-out events: N over M held-out securities" -- and if N is 0, the line says the held-out pass is NOT a precision grade and the round-13 pass stays IN-SAMPLE</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-c-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~40/scripts/ac2_burst_shape_census.py</invocation><expect>THE BURST-SHAPE CENSUS OVER THE WHOLE HARVEST: over every security in the newest mention snapshot, the distribution of tier-A/B articles per (security, day) and per merged run (the qualifying merge, gap <= 1 day), with its denominator; every burst exceeding 3 articles OR 1 day named; and the verdict line "larger burst shape: EXERCISED (n bursts) / UNEXERCISED". IF a planted fixture (5+ tier-A articles over 2+ days, >= 2 publishers, one story) is also run through event_rows, its output is printed under a line reading "FIXTURE -- MECHANISM TEST, NOT A HELD-OUT GRADE"</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-c-1" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~40/scripts/ac4_held_out_for_l9.py`. Two parts:
(1) every held-out EVENT (expected none) with the b-2 AC4 question -- is it ONE story about its own company, and does its
lead name it?; (2) every held-out NEAR-MISS story from AC1 with all its headlines -- **is any of them a real burst of
coverage about its company that the rule declined?** Present; record NO verdict.

## 3. WHAT THIS CELL DOES NOT DO

No rebuild, no served move (so no never-widen pair), no code change, no vendor call. It does not fix a failing event;
a failure it finds is the next round's cell, shipped under a pair.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **The recall arm is the issuer's addition, inside the ruling's spirit:** the CTO asked for held-out EVENTS graded; the
   base measurement shows there will be none (0 events on 50 held-out securities), so a precision-only read would grade
   nothing. The near-miss layout lets L9 see a declined real burst -- the one failure a held-out read here can reveal.
2. **Base expectations (measured at `f1de5ca7ce`):** AC1 at the base prints 0 held-out events over 50 securities
   (a report, not a build check; the script is the build). AC2: 1 (security, day) above 3 articles (in-sample BA 09-08),
   0 merged runs above 1 day among served events. Scripts are worker-written as in every round of this project.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>14</round>
<slot>~40</slot>
<fabric>site-z</fabric>
