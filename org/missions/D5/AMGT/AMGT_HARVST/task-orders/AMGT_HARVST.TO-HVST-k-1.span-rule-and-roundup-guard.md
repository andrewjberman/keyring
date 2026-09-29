# AMGT_HARVST task order -- `HVST-k-1` -- ROUND 21 chain 1 of 2: THE SPAN RULE PLUS THE ROUNDUP GUARD, in code, dry-rebuilt

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-k-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~49</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on publication_gold.py or the harvest gold prefixes; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 -- no new boto3 call; AC2 reads S3 (silver headlines, the newest mention and event parts) with GET/LIST only through the producer's own reader. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a span rule that silently moves the 5 events the ruling keeps, or a guard keyed on the stored `is_roundup` flag alone (it is False on the very HD article that must not extend the span). AC2 requires 5 of 8 served events row-equal and HD's span to end 2026-08-18 with the roundup still a member.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.** The served `chatter_event` rebuild is round 22, under its own
   never-widen pair, after the CTO rules the lead question. This cell changes the rule and proves it in memory.
2. **Inputs:** the newest served mention part and silver headlines, as landed today, read through
   `publication_gold._latest_gold_snapshot_rows`. The round-20 census outputs are READ ONLY:
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~48/j2_ac1_output.txt` and `j2_census_result.json`.
3. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~49/scripts/`; outputs named `k1_*`
   -- **never `.scratch/`.**
4. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~49/AMGT_HARVST.TO-HVST-k-1.span-rule-and-roundup-guard.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-k-1.span-rule-and-roundup-guard`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~49/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round20.md` @`4b8bd40242`, s.2 rulings 1, 2 and 4)

1. **The span rule, ADOPTED.** The same story on consecutive days, with at most ONE empty day between them
   (`EVENT_MAX_GAP_DAYS`, 1), joins ONE event.
   - The served story test (`publication_gold._security_stories`, ~:992) is unchanged. The event thresholds (at least 2
     tier A/B articles from at least 2 distinct tier-A publishers) apply to the whole run.
   - `event_rows` (~:1086) today tests each day separately. This is the change.
   - The round-20 census (`j-2`) implemented exactly this candidate in its script; its header states it. Bring it into
     the rule.
2. **The ROUNDUP GUARD.** A member with `is_roundup True` **or** `co_mention_count >= 4` (AMENDMENT 1: RULED 4, was 3) is a MEMBER of the event, but it
   NEVER EXTENDS the span and NEVER LEADS.
   - The span is set by the non-roundup members.
   - The lead is chosen among the non-roundup members, by the served lead rule.
   - The stored `is_roundup` flag is NOT sufficient on its own. HD's 2026-08-20 "6 Big Takeaways From Retail's Big Week
     of Earnings" is stored `is_roundup False` with `co_mention_count 4`.
3. **The link window is UNCHANGED** (ruling 4). A follow-up after two empty days is its own event.
4. **The lead rule is otherwise UNCHANGED.** The retitled-preview question is ruled later, on `HVST-k-2`'s census.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-k-1"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with new tests NAMED in the -rA output: the same story on consecutive days with one empty day between joins ONE event; two empty days between leave TWO events (link window unchanged); the thresholds apply to the run; a member with is_roundup True is a member that neither extends the span nor leads; a member with is_roundup False but co_mention_count >= 4 is treated the same, and one with co_mention_count 3 is NOT guarded (AMENDMENT 1); the pass count BEFORE and AFTER printed (base 205) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-k-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~49/scripts/k1_ac2_dry_rebuild.py</invocation><expect>THE DRY REBUILD OF chatter_event UNDER THE NEW RULE, IN MEMORY, OVER TODAY'S INPUTS, beside the SERVED newest event part (8 events at the cut): (a) per served event KEPT / CHANGED / MERGED / GONE, and every NEW event, each with first_day, last_day, lead headline and every member headline with publisher, day and roundup-guard status, denominator 8; (b) the 5 events j-2 kept are row-equal to the served rows; (c) 992_HK_Equity's changed event equals j-2's candidate (span, member set, lead); AMZN_US_Equity's changed event has j-2's member set (5) and lead (bbg's 09-06 first report) with span 2026-09-06..2026-09-07, the 09-08 barrons member being a guarded roundup that does not extend it (AMENDMENT 1); (d) HD_US_Equity's event ends 2026-08-18, with the 2026-08-20 "6 Big Takeaways" article a MEMBER flagged by the guard; (e) every event_id unique. PASS only if (b)-(e) all hold</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No gold write, no deploy, no change to the story test's link window, no change to the lead rule beyond the guard, no
change to how `is_roundup` is produced, no vendor call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Base:** suite 205 passed in `lib/research/harvest/tests/` (the `j-1` drain; 221 with the api route file). The
   served event part is `part-20260929T192706Z` (8 events). AC1's named tests FAIL at the base. AC2 (c) and (d) FAIL at
   the base, because the served rule tests each day separately.
2. **The guard's threshold is the CTO's: RULED 4 by AMENDMENT 1 (was 3).** The stored flag is `co_mention_count >= roundup_at`
   (`publication_gold.py:307`); that producer is NOT changed (analysis s.4 NOT-cells).
3. **Round 22 is the served rebuild,** cut after the CTO rules the lead question on `k-2`.


**AMENDMENT 1 (issuer, 2026-09-29 ~23:3xZ) -- the guard threshold is 4.** At the ruled `co_mention_count >= 3` the worker's AC2 FAILED (rows `Z-W49-S1`/`S2`, BLOCKING): NVDA's served event went GONE (all 3 members guarded) and AMZN reverted to 09-07 led by barrons, contradicting ruling 1 (AMZN led by its first report). The issuer re-ran the worker's AC2 read-only at 3, 4, 5 and flag-only: only 4 meets every ruled intent (KEPT 5, CHANGED 3, GONE 0; HD ends 08-18; AMZN 09-06..09-07, 5 articles, led by bbg's first report; at 5 or flag-only HD stretches to 08-20). `1.0.0_SA_CTO~Z` RULED 4 (msg 26783, `ROUND_ANALYSIS.round20.md` s.2a @`168acda05e`); `Z-W49-S1`/`S2` disarm on the constant landing at 4 with the re-run as the test. AC1's guard test and AC2 (c) for AMZN are amended to match; AMZN's `last_day` is 09-07 because its 09-08 barrons member is `is_roundup True` and the guard keeps it from extending the span. The issuer amends its own criteria without a CTO ruling beyond the threshold itself (CLAUDE.md rule 27, L6); the gate limb that graded this modification is recorded in the amendment commit.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>21</round>
<slot>~49</slot>
<fabric>site-z</fabric>
