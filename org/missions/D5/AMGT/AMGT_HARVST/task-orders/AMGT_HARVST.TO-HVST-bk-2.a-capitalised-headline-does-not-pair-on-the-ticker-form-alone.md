# AMGT_HARVST task order -- `HVST-bk-2` -- ROUND 66 (`1.0.0_SA_CTO~Z` msg 31613, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 3 @f7ad546af4): IN A HEADLINE CAPITALISED THROUGHOUT, THE EXACT-CASE TICKER FORM ALONE DOES NOT PAIR -- IT NEEDS A SECOND ANCHOR; THE COUNT IT MOVES IS PRINTED, NO REBUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bk-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~117</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus a READ-ONLY census (S3 GET of the pool universe and the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a changed output for a security the rule does not name, a test with no negative control, a rule loosened to meet the census, a second list where the cell says one, or a gold build.
</preflight>

## 0. THE CELL

`lib/research/harvest/publication_gold.py` `_security_mentions(article_row, security)` counts a security's name aliases
case-insensitively and its exact-case ticker forms (`ticker_aliases`) case-sensitively, over the title and the blocks. For a
security with NO aliases the company string is matched in its stored case (`HVST-bh-9`). The file also carries the
second-anchor rule (`HVST-bh-3`): a form in `anchor_required_ticker_aliases` counts only when the article also carries a
name alias, another ticker form, an anchor alias or an exact-case anchor symbol. Read all three before you write.

A reviewer found this on BP's page after the last rebuild: "Bond Traders Bet on Fed Delivering 25 BP Rate Increase"
(bbg, 2026-09-16; `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND65_FEED_WALK_GRADE_20261008.md` @96206b0d29; row AMGT_HARVST-Z-S102). `BP` there is basis points. Its only exact-case `BP` is in
the title, and every word of that title is capitalised.

The ruling: **in a headline where every word is capitalised, case carries no information, so the exact-case form ALONE does
not pair there; it needs a second anchor.**

## 1. THE BUILD (LOCAL)

1. **"Capitalised throughout"** (a pure function with a docstring): a title is capitalised throughout when it has at least
   three alphabetic words and EVERY alphabetic word begins with an upper-case letter (words with no letter, such as "25",
   are ignored; an all-upper title qualifies). Sentence-case titles ("Bond traders bet on ...") do not qualify.
2. **The rule** (`_security_mentions`). For EVERY security: a span of an exact-case form (a ticker form, or the stored-case
   company string of an empty-alias security) that sits in a title capitalised throughout does not count UNLESS the article
   has a second anchor: at least one span of a name alias, an anchor alias or anchor symbol, or an exact-case form of that
   security in a BLOCK (body text is not capitalised throughout, so case carries information there). When there is no
   second anchor, those title spans are left out and every returned field comes from the count without them. A title that
   is not capitalised throughout takes today's path unchanged, and so does every name-alias span.
3. Name `HVST-bk-2` in a comment. Change nothing else in that file; do not change the list code or the alias data.
4. **Plants** `lib/research/harvest/tests/test_bk2_capitalised_headline.py` (no network):
   - (i) THE NEGATIVE CONTROL, verbatim title: "Bond Traders Bet on Fed Delivering 25 BP Rate Increase" with a body that
     never says BP gives `mention_count` 0 for a security whose company is `BP`, aliases empty, ticker form `BP`;
   - (ii) the same title with a body block "BP said it would raise output" gives a count that includes the title span;
   - (iii) a sentence-case title "BP raises its dividend" with no body mention gives 1 (not capitalised throughout);
   - (iv) "CAT Shares Jump After Results" with a body naming "Caterpillar" counts the title form (a name alias anchors);
   - (v) "CAT Shares Jump After Results" with no other span gives 0 for a security with ticker form `CAT`;
   - (vi) a two-word title "BP Results" is not "capitalised throughout" (fewer than three alphabetic words) and gives 1;
   - (vii) the mutant: with the rule off, (i) gives 1 -- assert that.
5. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~117/bk2_census.py`: the served list file
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/securities.universe.r64.json`; BEFORE = the matcher with the rule off (stated in the file
   how); AFTER = as you leave it. Over every latest silver article with the real `pg._security_mentions`, progress every
   500 articles:
   - `DENOMINATOR: securities <S>, silver articles <N>, titles capitalised throughout <T>`;
   - `PAIRS REMOVED: <R> over <k> securities`, then per security `<security_key>: pairs before <p0> after <p1> removed <r>`
     for every security with r > 0, largest first;
   - `PAIRS WITH A LOWER COUNT BUT KEPT: <c>`;
   - EVERY removed pair in `BK2_REMOVED_PAIRS.md` and `.json` beside the script: security_key, company, article_key,
     publisher, published date, the title, and the form that matched (these go to a reviewer; no verdict by you);
   - `THE REPORTED PAIR: <article_key of the bbg "25 BP Rate Increase" story> BP_US_Equity <removed|still present>`;
   - `PAIRS ADDED: <a>` (must be 0);
   - last line `CENSUS OK` only if N > 0, T > 0, the reported pair reads `removed`, and PAIRS ADDED is 0; otherwise
     `CENSUS FAIL` and the failing line. Write the output as `bk2_census.out`.
6. The count this rule moves is the deliverable: do NOT tune the definition of "capitalised throughout" to make R smaller
   or larger. If R is large (hundreds), that is the finding; report it as it reads.
7. If the S3 read is refused or returns 0 articles: BLOCKING row, stop on AC2. Build no gold.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/securities.universe.r64.json
org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND65_FEED_WALK_GRADE_20261008.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~117/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bk-2"><invocation>python -m pytest lib/research/harvest/tests/test_bk2_capitalised_headline.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bk-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~117/bk2_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bk-2"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W117-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~117/AMGT_HARVST.TO-HVST-bk-2.a-capitalised-headline-does-not-pair-on-the-ticker-form-alone.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bk-2.a-capitalised-headline-does-not-pair-on-the-ticker-form-alone`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31613, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 3 @f7ad546af4. Decomposition section 80.
- R15: "In a headline where every word is capitalised, case carries no information, so the exact-case form alone does not pair
  there; it needs the second anchor. One cell, with the count of pairs it moves printed before any rebuild." Row Z-S102.
- **Issuer rulings inside the decomposition** (no gate limb graded them): "capitalised throughout" is every alphabetic word of
  a title of three or more such words beginning upper-case; the second anchor is a name alias, an anchor alias or symbol, or
  the exact-case form in a body block; the rule is for every security, not BP alone, which is why the census prints the count
  per security. The removed pairs go to `3.0.0_SA_CVO~Z` before any rebuild's pair names them.
- Chain of one, slot ~117. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as
  expected (no such file); AC3 base PASS as expected (498 passed).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>66</round>
<slot>~117</slot>
<fabric>site-z</fabric>
