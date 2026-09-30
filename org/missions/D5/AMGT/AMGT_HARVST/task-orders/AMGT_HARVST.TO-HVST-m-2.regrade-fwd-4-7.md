# AMGT_HARVST task order -- `HVST-m-2` -- ROUND 23 chain 2 of 3: RE-GRADE FWD-4 / FWD-7 FROM THE SERVED STORE (read-only)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-m-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~54</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the harvest prefixes; this cell writes nothing to S3.
comp-iam: RUN at L5 -- S3 GET/LIST only on s3://opal-data-harvest/ (silver, the newest gold parts); Lambda GetFunctionConfiguration and a read-only Invoke of the served chatter/rank route where one exists. NO PUT, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a strength grade "re-derived" by calling the very function that produced it (a tautology), or a rank compared against itself. AC1 re-derives the grade from the stored TEXT with the rule stated in the script; AC2 compares the page source's served rank to a rank recomputed independently from the graded daily table.
</preflight>

## 0. THE STANDING CLAUSES

1. **READ-ONLY. NO S3 WRITE OR DELETE, NO VENDOR CALL, NO CODE CHANGE, NO DEPLOY.** This cell MEASURES; it grades
   nothing. The CTO grades at L10.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~54/scripts/`; outputs named `m2_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~54/AMGT_HARVST.TO-HVST-m-2.regrade-fwd-4-7.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-m-2.regrade-fwd-4-7`.
4. **Whatever this machine cannot see is printed as NOT MEASURABLE HERE, with the reason.** It is never estimated.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~54/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE TARGETS, VERBATIM (`org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md`)

- **FWD-4** -- For any article and company, we can say how strongly the article is about that company. DONE WHEN
  EXERCISED -- every (article, company) pair carries whether the company is in the headline, in the opening, how often it
  is named, how much of the article names it, which other covered companies it names, and a strength grade; the grade is
  re-derived from the stored text and matches.
- **FWD-7** -- The ranking of companies by chatter uses how strongly they were written about, not how many times they
  were named. DONE WHEN EXERCISED -- the chatter ranks on the page are computed from the graded daily table, and a company
  named once in passing in many articles no longer outranks one that was the subject of a few.

**Where things live:**
- The graded pair table is gold `article_security_mention`; the daily table is gold `chatter_daily`. Both are newest
  parts under `amgt/harvest/gold/`, read through `lib/research/harvest/publication_gold._latest_gold_snapshot_rows`.
- The page's chatter rank is served by the scoped API (`opal-amgt-scoped-api`) and/or `amgt-resapp-chatter-axis`. Find
  the route the page reads in `lib/research/api/scoped_amgt.py` and `lib/research/metrics/chatter_axis.py`, and state
  which you read and why.
- `CHATTER_AXIS_SOURCE` on `amgt-resapp-chatter-axis` was `legacy` at the last read. Report its value at your run.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-m-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~54/scripts/m2_ac1_fwd4_carriers.py</invocation><expect>FWD-4 MEASURED over the newest served article_security_mention part: per (article, company) pair, the presence of each carrier -- in headline, in opening, count, share (how much of the article names it), co-mentioned companies, strength grade -- as 6 present-counts over the pair denominator; and the grade RE-DERIVED from the stored silver text by the rule stated in the script's header (the producer's rule, re-implemented or re-read from stored text, never by calling the producer on its own output), with the matched / mismatched count and every mismatch listed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-m-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~54/scripts/m2_ac2_fwd7_rank.py</invocation><expect>FWD-7 MEASURED: the page's chatter rank as SERVED (the route and function named, CHATTER_AXIS_SOURCE printed), the input it is computed from (graded daily table or raw counts), and a rank recomputed independently from the served graded chatter_daily part over the same window; the two rankings printed side by side with their rank correlation; and the passing-mention test: the companies whose raw mention count rank is above their graded rank by 5 or more places, listed</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No grade, no fix, no write of any kind, no vendor call, no change to `CHATTER_AXIS_SOURCE`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):** from `ROUND_ANALYSIS.round22.md` @`9d7bd0e4f9` s.4 item 2. Round 10's last reading had FWD-4's
carrier clause unmeasured and FWD-7's rank unexercised. Risk is LOCAL: it reads served state and writes deliverables only.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>23</round>
<slot>~54</slot>
<fabric>site-z</fabric>
