# AMGT_HARVST task order -- `HVST-bh-2` -- ROUND 61 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): EVERY PAIR THAT RESTS ON ONE OF THE NINE TICKER FORMS NO SAMPLE REACHED -- THE WHOLE POPULATION IN CONTEXT, READ-ONLY, NO GRADE BY YOU

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~112</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL scripts and records, plus a READ-ONLY census (S3 GET of the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a census with no printed denominator, a sample the script grades, a source substituted for a refused read, or a gold build.
</preflight>

## 0. THE CELL

The served gold (rebuild #8) was built from `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json` (242 securities). Each security
carries `ticker_aliases`: exact-case ticker forms the matcher counts case-sensitively. Nine of those forms were never read by
a reviewer. The dry run before the rebuild counted the pairs that rest on each: BNP 5, HEI 3, SNPS 3, DG 2, ED 2, GPN 2, ADBE 1, NKE 1, SHOP 1 (20 pairs). Silver has grown since,
so your counts may be higher.

A pair RESTS ON A FORM when `pg._security_mentions(article, security)` counts at least one mention with the security as it
stands in the list file and none with that one form removed from its `ticker_aliases`. The method is already written for one
form in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round58/csl_pairs_sample.py`: read it and follow it.

## 1. THE BUILD (read-only)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/bh2_nine_forms.py`. For each of the nine forms, find every security in the list
   file that carries it in `ticker_aliases` (print the security keys; a form no security carries is printed as such). Read
   every latest silver article through `pg._iter_latest_articles()` once. Print a progress line every 500 articles.
2. It prints `DENOMINATOR: forms 9, securities carrying one <k>, silver articles <N>`, then per form
   `<FORM> <security_key>: pairs resting on the form <n> (dry run 3: <the count above>)`, then `TOTAL: <T> pairs`.
3. Write `BH2_NINE_FORMS.json` and `BH2_NINE_FORMS.md` beside it: EVERY such pair, no sampling. Per row: row number, form,
   security_key, the security's `company`, article_key, publisher, title, url, and every exact-case span of the form in the
   title and blocks with 120 characters of context each side. The md opens with one paragraph: the population, the method, the
   counts, and the question per row ("does <FORM> here name <company>"). No verdict, no grade.
4. Last line: `CENSUS OK` only if N > 0, all nine forms printed, and T is at least 20. Otherwise `CENSUS FAIL` and the
   failing condition (a T below 20 is a finding: print the form whose count fell).
5. Write the whole output as `bh2_nine_forms.out`. If the S3 read is refused or returns 0 articles: BLOCKING row, stop.
6. Change no product file. Build no gold.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round58/csl_pairs_sample.py
lib/research/harvest/publication_gold.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/bh2_nine_forms.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-2" judgment="true"/>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W112-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/AMGT_HARVST.TO-HVST-bh-2.nine-unreached-ticker-forms.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-2.nine-unreached-ticker-forms`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 75.
- R2: "All 20 pairs are read whole by the CVO; 20 is a census, not a sample. A form with 2 or more wrong pairs goes to
  `ticker_refusals`." AC2 is that read; a refusal that follows is the issuer's data act in the next round's change set.
- Slot ~112's queue: `bh-2`, then `bh-6` (two small read cells on one light worker; the box runs two collection legs).
- **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>61</round>
<slot>~112</slot>
<fabric>site-z</fabric>
