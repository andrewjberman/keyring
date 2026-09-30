# AMGT_HARVST task order -- `HVST-j-2` -- ROUND 20 chain 2 of 2: THE STORY-SPAN CENSUS (row `Z-W41-S1`) -- measurement only, no rule change

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-j-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~48</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the harvest gold prefixes; this cell writes nothing served.
comp-iam: RUN at L5 -- no new boto3 call; S3 GET/LIST only (silver headlines, the newest mention and event parts) through the producer's own reader. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a census whose baseline is not the served truth (a rebuild that already differs before the candidate rule is applied), or a merge count with no members named. AC1 (a) requires the current-rule rebuild to equal the served event part row by row; AC1 (d) names every merge's members.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO CODE CHANGE, NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.** The candidate rule lives ONLY in this cell's
   script. `lib/` is not touched. The CTO rules the rule on this census at round 20's analysis.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~48/scripts/`; outputs named `j2_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~48/AMGT_HARVST.TO-HVST-j-2.story-span-census.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-j-2.story-span-census`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~48/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL (`ledger/ROUND_ANALYSIS.round19.md` @`a251f02116`, s.2 ruling 3 and s.4 item 2; row `Z-W41-S1`)

**Row `Z-W41-S1`:** the AMZN plane-crash coverage forms ONE event of 3 articles on 2026-09-07 only, led by barrons
"Scene of Fatal Amazon Plane Crash". It is not the 6-article 2026-09-06..09-10 burst. bbg's 09-06 first report and its
09-10 NTSB piece fall outside it.

**The question** the census answers, and does not rule: under a CANDIDATE span rule, "the same story across consecutive
days joins one event", what changes?
- State the candidate precisely in the script's header: what "same story" is, and what "consecutive" is.
- Reuse the served rule's own story test from `publication_gold.event_rows` (its linking of articles into a story);
  only the span joining is the candidate.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). ONE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-j-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~48/scripts/j2_ac1_story_span_census.py</invocation><expect>A DRY CENSUS OVER TODAY'S INPUTS (the newest served mention part, silver headlines), printing: (a) BASELINE -- event_rows under the CURRENT rule equals the SERVED newest chatter_event part row by row (8 of 8 at the cut; any difference printed and the census marked INVALID); (b) the candidate rule stated verbatim; (c) the AMZN fixture -- its event(s) under the current rule and under the candidate, each with span, article count, lead headline and every member headline with publisher and day; (d) the served-event delta under the candidate, per served event KEPT / MERGED / CHANGED / GONE (denominator 8), and every NEW or MERGED event with its members' headlines, days and publishers; (e) every event_id unique under the candidate. PASS only if (a) holds and (b)-(e) all print</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No change to `publication_gold.py` or any `lib/` file, no gold write, no deploy, no vendor call. It records NO verdict on
whether the candidate is right; that is the CTO's at L10.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Independent of `j-1`** (disjoint write surfaces; `j-2` changes no code). The two run in parallel, `~47` and `~48`.
2. **Base:** served newest event part `part-20260929T192706Z` (8 events; ETag `c146a325...`, byte-identical to the
   part before it). AC1 is a census: it has no FAIL-at-base arm, except that (a) FAILS if the baseline does not
   reproduce the served part.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>20</round>
<slot>~48</slot>
<fabric>site-z</fabric>
