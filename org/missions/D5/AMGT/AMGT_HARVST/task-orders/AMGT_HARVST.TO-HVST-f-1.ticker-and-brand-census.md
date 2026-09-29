# AMGT_HARVST task order -- `HVST-f-1` -- ROUND 17 cell 1 of 2: THE TICKER AND BRAND CENSUS -- what each candidate name form would add, before any rule changes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-f-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~43</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates; this cell reads and counts, writes no gold, changes no code and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the pool universe and the silver article parts. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a census that reports an added count without the hits behind it (so a common-word ticker reads as recall), or a brand form taken from an unnamed source. AC1 prints the denominator per form; AC2 prints every sample hit with its words around it.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO CODE CHANGE, NO S3 WRITE OR DELETE, NO VENDOR CALL.** The alias rule is decided at the round-17 analysis on
   what this census prints (`ROUND_ANALYSIS.round16.md` @`f424435829`, s.2.1: "No served move this round").
2. **Inputs:** securities `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/securities.universe.json`
   (READ ONLY: 191 securities, the served alias sets); silver articles through `publication_gold._iter_latest_articles()`
   (120 at the cut). Match with the SERVED matcher: `publication_gold._match_counts` (one span, one count, word-bounded).
3. **A brand form needs a named source.** Take brand or short-name forms only from an artifact in the estate that holds
   them (name it: path, field, how many securities it covers). If no such source exists, print that, and count only the
   forms derivable from the universe's own fields.
4. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~43/scripts/` -- **never `.scratch/`,
   never another worker's folder.**
5. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~43/AMGT_HARVST.TO-HVST-f-1.ticker-and-brand-census.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-f-1.ticker-and-brand-census`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~43/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round16.md` @`f424435829`, s.2.1; read it at the bytes)

The CVO found under-counts where a company is named by its ticker or brand ("UPS freighter" reads 1 where the text says
2; "Google" x2 is missed for Alphabet). Adding tickers and brands blindly is unsafe: short tickers ("V", "MA", "ALL",
"UPS") are common words, and brand-to-parent mapping needs a source. **RULED: measure the class first** -- for every
security in the 191, the mentions its ticker forms and its brand or short-name forms would ADD over today's silver, and
per form a printed sample whose hits a text read can grade. Every figure carries its denominator.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-f-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~43/scripts/ac1_form_census.py</invocation><expect>THE CENSUS, per candidate FORM CLASS (ticker root; ticker with exchange stripped; brand or short name, with its named source or the line "no brand source in the estate"): the forms generated (denominator: 191 securities), and per form the ADDED spans over the 120 silver articles -- matches the form makes that the served alias set does not already cover -- as added (article, security) pairs, added mention_count, and pairs whose title or lead flag would flip; every form class totalled; every form of 3 characters or fewer and every form that is an English dictionary word flagged. Final line: "forms with added hits: N of M generated"</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-f-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~43/scripts/ac2_sample_hits.py</invocation><expect>THE SAMPLE FOR THE TEXT READ: for every form with added hits, up to 10 added hits (all if 10 or fewer; otherwise 10 drawn with a printed seed), each with the article key, headline, block, offset and the words around the match; per form the sample size beside its added-hit total</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-f-1" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~43/scripts/ac4_true_hit_read.py`, which presents
AC2's sample grouped by form. **The question the CVO grades: per form, how many sampled hits are the company?** Present;
record NO verdict.

## 3. WHAT THIS CELL DOES NOT DO

No alias change, no code change, no gold write, no vendor call. It recommends no rule; the analysis rules.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **The true-hit read is L9's, not the worker's:** the analysis asks for "how many of those hits a text read shows to be
   the company"; that read is a judgment, so the worker lays out the sample (AC2) and the CVO grades it (AC4). A worker
   self-grading true hits would be a self-graded judgment.
2. **Base:** 191 securities, 120 silver articles, the served matcher one-span (CLOUD `5f25e64267` onward). AC1/AC2 FAIL at
   the base by construction (no scripts).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>17</round>
<slot>~43</slot>
<fabric>site-z</fabric>
