# AMGT_HARVST task order -- `HVST-bh-1` -- ROUND 61 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): THE PAIRS THAT REST ON THE BARE-NAME FALLBACK ALONE -- A CENSUS BY SECURITY AND A SAMPLE OF 30, READ-ONLY, NO GRADE BY YOU

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~111</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL scripts and records, plus a READ-ONLY census (S3 GET of the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a census with no printed denominator, a sample the script grades, a source substituted for a refused read, or a gold build.
</preflight>

## 0. THE CELL

The served gold (rebuild #8, 2026-10-07) was built from the list file
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json` (242 securities) by `lib/research/harvest/publication_gold.py`.

Its matcher reads a security's aliases through `_security_aliases(security)`:
`list(security.get("aliases") or [security["company"]])`. So a security whose `aliases` list is EMPTY is matched on its
`company` string, and name aliases match case-insensitively (`_span_pattern`). Nobody has read the pairs this produces. Known
members before this census: GSK, RWE, SAP, BP (US line), Nokia.

A pair (article, security) RESTS ON THE FALLBACK ALONE when `pg._security_mentions(article, security)` counts at least one
mention with the security as it stands in the list file, and counts none with the fallback taken away (a copy of the security
whose `company` is the empty string and whose `aliases` stay empty; its `ticker_aliases` unchanged). Read `_security_mentions`
and `_match_counts` first and use their own returned fields; do not re-implement the matcher.

## 1. THE BUILD (read-only)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~111/bh1_fallback_census.py`. Reads the list file above and every latest silver
   article through `pg._iter_latest_articles()` (S3 GET, no put). Prints a progress line every 500 articles.
2. It prints, in this order:
   - `DENOMINATOR: securities <S>, with an empty alias list <E>, silver articles <N>`;
   - one line per empty-alias security: `<security_key> company=<company> ticker_aliases=<list>: pairs served <p>, resting on
     the fallback alone <f>, of those with no span in the stored case <c>` (a span is in the stored case when its text equals
     `company` character for character);
   - `FALLBACK-ONLY PAIRS: <F> over <E> securities`;
   - `SAMPLE: <n> of <F>, seed 61`.
3. The sample: sort the fallback-only pairs by (security_key, article_key), then `random.Random(61).sample(...)` of 30, or all
   of them when F is below 30. Write `BH1_FALLBACK_SAMPLE.json` and `BH1_FALLBACK_SAMPLE.md` beside the script. Per row: the row
   number, security_key, company, article_key, publisher, title, url, and EVERY span of the company string in the title and
   blocks with 120 characters of context each side, each marked `stored case` or `other case`. The md opens with one paragraph:
   what the population is, how a pair was chosen, the two counts, and that the question per row is "is this article about this
   security". It carries NO verdict and NO grade: a reviewer grades it.
4. Last line: `CENSUS OK` only if N > 0, E > 0, every empty-alias security printed its line, and the sample holds
   min(30, F) rows each with at least one span. Otherwise `CENSUS FAIL` and the failing condition.
5. Write the whole output beside the script as `bh1_fallback_census.out`.
6. If the S3 read is refused or returns 0 articles, do not substitute a source: file a BLOCKING row and stop on AC1.
7. Change no product file. Build no gold.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json
lib/research/harvest/publication_gold.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~111/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~111/bh1_fallback_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-1" judgment="true"/>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W111-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~111/AMGT_HARVST.TO-HVST-bh-1.bare-name-fallback-census.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-1.bare-name-fallback-census`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 75.
- R1 of the analysis: "a census of the pairs that rest on the fallback alone, by security, denominator printed; then a sample of
  30 graded by `3.0.0_SA_CVO~Z`, bar 27 of 30. Below the bar the fallback requires the name in its stored case, or is removed for
  the securities that fail." AC2 is that grade; the remedy below the bar is a later cell, never this worker's.
- Chain of one. **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>61</round>
<slot>~111</slot>
<fabric>site-z</fabric>
