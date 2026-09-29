# AMGT_HARVST task order -- `HVST-e-1` -- ROUND 16 cell 1 of 2: ONE TEXT SPAN, ONE COUNT -- the matcher change, proved in memory

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-e-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~42</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on publication_gold.py's matcher; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on silver article/listing parts and the newest gold snapshots (mention, daily, event). NO PUT.
comp-adversary: RUN at L5 -- the adversary is a span count that loses a real mention (a shorter alias at a position the longer one does not cover), or one whose tier change reaches an event. AC2 prints every moved row and every event.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL.** This cell changes the matcher and proves the rebuild IN MEMORY. The served
   rebuild is `HVST-e-2`, under its own never-widen pair.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~42/scripts/` -- **never `.scratch/`,
   and never write into another worker's deliverables folder.**
3. **THE INPUT IS PINNED:** securities `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/securities.universe.json`
   (READ ONLY; the file the served parts were built from); silver as landed today.
4. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~42/AMGT_HARVST.TO-HVST-e-1.one-span-one-count.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-e-1.one-span-one-count`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~42/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round15.md` @`ce26d1244b`, s.2; read it at the bytes)

`publication_gold._match_counts` (~:116) counts "every alias independently, summed", and `_alias_pattern` (~:112) is
word-bounded by `(?<!\w)` / `(?!\w)`, so "Amazon" matches inside "Amazon.com". One span that several aliases cover counts
more than once (AMZN's 09-06 crash report reads `mention_count` 10). **RULED: count each matched text span ONCE, keeping the
LONGEST alias that covers it, with NO overlapping spans.** `match_forms` then names the aliases that won a span.

**Measured by the issuer at the cut (CLOUD `c13ec03ca8`), a starting point and not your conclusion:** a prototype span count
(one alternation, longest alias first, non-overlapping, same word bounds) over today's 120 silver articles moves
`mention_count` on **14 of 275 rows across 6 securities** (AMZN 8, UPS 2, GOOGL 1, GOOG 1, DAL 1, FDX 1), and **moves 8
rows from tier C to tier D** (AMZN 2, UPS 2, GOOGL, GOOG, DAL, FDX 1 each), because tier C is `mention_count >= 2`
(`assign_tier`, ~:101). `mention_in_title`, `mention_in_lead` and `blocks_hit` move on **0** rows, so tiers A and B, and
therefore events, are expected not to move.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-e-1"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with the new span-count tests NAMED in the -rA output (a nested alias counts once: "Amazon.com Inc." with aliases Amazon / Amazon.com / Amazon.com Inc is ONE span credited to "Amazon.com Inc"; two separate mentions still count two; a shorter alias outside any longer span still counts; match_forms names only winning aliases); the pass count BEFORE and AFTER printed (base: 163 passed) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-e-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~42/scripts/ac2_span_rebuild_in_memory.py</invocation><expect>THE REBUILD, IN MEMORY, OVER TODAY'S SILVER with the pinned securities, OLD matcher (CLOUD base) vs NEW matcher, set beside the SERVED newest snapshots, every moved row attributed SPAN (new vs old) or DRIFT (old vs served): (a) article_security_mention -- rows served/old/new, every row whose mention_count, signal_tier, signal_weight or match_forms moves, with security, article, old and new values and headline; per-security counts; (b) chatter_daily -- per security, the (security, day) cells whose any column moves, SPAN vs DRIFT, with the as-of named; (c) chatter_event -- every served event KEPT or MOVED, and any event moved printed as a FINDING; (d) every event_id unique. PASS only if (a)-(d) all print, 0 rows are added or removed by the span change, and title/lead/blocks_hit move on 0 rows</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-e-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~42/scripts/ac3_rebuildable_twice.py</invocation><expect>C-HV-GOLD-REBUILDABLE for the new matcher: two in-memory builds of mention, daily and event from the same inputs are equal row by row, denominator printed per table, any difference printed in full</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No gold write, no alias change, no tier-rule change, no event-rule change, no vendor call. If AC2 (c) prints a moved event,
file a BLOCKING row and stop -- do not tune the rule to keep it.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **The ruling's premise is corrected at the cut:** `ROUND_ANALYSIS.round15.md` s.2 says the double count "does not touch
   tier (title/lead flags)". It does not touch A/B, but tier C is a COUNT threshold, so 8 rows move C -> D today. This
   moves `signal_weight` and the daily `tier_c` / `tier_d` / `mention_score`. It is carded to `1.0.0_SA_CTO~Z` at the
   issuance for the pair; the ruling itself (count one span once) is unchanged.
2. **Base:** AC1 base 163 passed (the `d-1` drain). AC2 and AC3 FAIL at the base by construction (no new matcher). The
   issuer's prototype counts (s.1) are a second implementation: the issuer compares them to AC2's printed moves at the
   drain, and a disagreement is symmetric evidence (either may be wrong).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>16</round>
<slot>~42</slot>
<fabric>site-z</fabric>
