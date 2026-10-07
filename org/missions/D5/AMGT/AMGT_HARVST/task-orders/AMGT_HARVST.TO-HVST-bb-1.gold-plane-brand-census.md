# AMGT_HARVST task order -- `HVST-bb-1` -- ROUND 55 (`1.0.0_SA_CTO~Z` msg 30842; round 17's rule applied per plane): WHAT WOULD THE GOLD TEXT MATCHER ADD IF `Meta` AND `Lilly` WERE BRANDS THERE -- A DRY-RUN CENSUS, NO REBUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~105</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- READ ONLY. S3 GET of the silver article parts through the served iterator and of whatever the gold builder reads for its securities; NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Three collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a census that counts mentions the served aliases already count, a census run over collected-for-Meta articles only (the question is every stored article), a matcher re-implemented instead of imported, a product file edited, or a sample drawn from pairs the brand did not add.
</preflight>

## 0. THE CELL

`lib/research/harvest/whole_brand_aliases.json` carries two entries with `"plane": "slug"`: `META_US_Equity` / `Meta` and
`LLY_US_Equity` / `Lilly`. The collector uses them. The GOLD text matcher does not:
`lib/research/harvest/universe_securities.py` takes only `"plane": "text"` entries into a security's alias set, and
`lib/research/harvest/publication_gold.py` counts a security's mentions in EVERY stored article with that alias set
(word-bounded, longest first, one span one count).

So on the gold plane a brand would attribute a mention of `Meta` inside ANY stored article, including articles collected for
other companies. Nobody has measured that. Round 17's rule: a short name enters a plane only on a census of what it ADDS
there, graded. This cell is that census for the two brands. It changes NO product file and builds NO gold.

The precedent to REUSE (read it first; same question, round 18):
- `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~43/scripts/_common.py` -- the ADDED definition:
  `spans(aliases + [form]) minus spans(aliases)`, per title and per block, built with the served matcher's own pattern
  builder (`publication_gold._span_pattern`); articles from `publication_gold._iter_latest_articles()` (read-only S3 GET);
- `.../scripts/ac1_form_census.py` and `.../ac1_output.txt` -- the per-form table (pairs, NEW pairs, added mention count,
  title flips, lead flips);
- `.../scripts/control_served_matcher_agreement.py` -- the control that the script's baseline spans equal what the served
  matcher counts.
Those scripts read a securities file from round 18 (`0.9.0_WK_AMGT_HARVST~41/securities.universe.json`, 191 names). Do NOT
use that file: take the securities list the way the gold builder takes it TODAY (through `universe_securities`), and print
where it came from and its count.

## 1. THE BUILD (LOCAL; every file under your deliverables folder)

Folder: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~105/`.

1. **`bb1_census.py`.** Imports the REAL `publication_gold` and `universe_securities` from your worktree; re-implements no
   matcher. For each of the two brands, over EVERY latest silver article:
   - baseline = the security's alias set as gold has it today (the brand is NOT in it; assert that and print it);
   - ADDED = spans(aliases + [brand]) minus spans(aliases), title and blocks;
   - per brand print one line: `<security_key> <brand>: articles_with_added <a> of <N> articles; NEW pairs <p> (the security
     had 0 mentions in the article under the served aliases); added mention_count <m>; title flips <t>; lead flips <l>`;
   - split `articles_with_added` by the article's publisher and print it;
   - print `DENOMINATOR: securities <S> (source <where>), silver articles <N>`.
2. **The control arm, inside the same script.** For each of the two securities, run ADDED with a form that is ALREADY one of
   its aliases: it must add 0 spans in 0 articles. Print `CONTROL <security_key>: <form> adds <n>`.
3. **The agreement control.** On a seeded sample of 20 articles, the script's baseline span count for each of the two
   securities equals the mention count the served matcher itself returns. Print `AGREEMENT: <k> of <n>`.
4. **The sample for the grader.** Per brand, from the ADDED (article, span) rows only: seeded
   `random.Random(55).sample(rows, 30)`, or all if fewer than 30, rows sorted by (article_key, position) before sampling.
   Write `GOLD_PLANE_CENSUS_SAMPLE.json` (per row: n, brand, security_key, article_key, publisher, title, url if the record
   has one, where = `title` or `block <i>`, the text 200 characters either side of the span, `new_pair` true or false,
   `verdict` null) and `GOLD_PLANE_CENSUS_SAMPLE.md` (one table per brand: n, publisher, title, the span in context, an
   empty verdict column). The question the grader answers per row is: does this `Meta` / `Lilly` name the company? You
   grade nothing.
5. **The verdict line.** Print `CENSUS OK` as the LAST line only if ALL hold: N > 0 and S > 0; the brand is absent from each
   baseline alias set; both CONTROL lines read `adds 0`; AGREEMENT is n of n; both sample files exist and each brand's
   sample size equals min(30, its ADDED rows). Otherwise `CENSUS FAIL` and the failing line.
6. Write the script's whole output beside it as `bb1_census.out`.
7. **`test_bb1_added_spans.py`** (no network): on planted articles, (i) a title carrying `Meta` and no legal name gives 1
   added span and a NEW pair; (ii) an article carrying `Meta Platforms` and no bare `Meta` gives 0 added (the longer alias
   takes the span); (iii) `metadata` and `Metaverse` give 0 (word-bounded); (iv) `Eli Lilly` gives 0 added for `Lilly`, and
   `Lilly said` gives 1; (v) the control: an existing alias as the form adds 0.
8. If the S3 read is refused or the iterator returns 0 articles, do not substitute another source: file a BLOCKING row with
   the exact error and stop on AC1.

Bound your run: print a progress line every 500 articles; the read is one pass.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~105/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You READ, and never write: `lib/research/harvest/publication_gold.py`, `lib/research/harvest/universe_securities.py`,
`lib/research/harvest/whole_brand_aliases.json`, and the round-18 scripts named in section 0.

## 2. PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bb-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~105/bb1_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bb-1"><invocation>python -m pytest org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~105/test_bb1_added_spans.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bb-1" judgment="true"/>
</proof_of_spec>

- AC3 is the grade of the two samples (does the brand word name the company; bar 29 of 30 per brand). It is graded by
  `3.0.0_SA_CVO~Z`, never by you and never by the issuer: record it in the instance under `UNVERIFIABLE-BY-INSTRUMENT` with
  a `status_reason` naming `3.0.0_SA_CVO~Z`.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W105-S<k>`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~105/AMGT_HARVST.TO-HVST-bb-1.gold-plane-brand-census.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bb-1.gold-plane-brand-census`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 30842 (2026-10-07 11:27Z): "gold needs its own census, in the next HARVST issuance: a dry
  run of the gold matcher with the two brands added, the count of mention rows it would ADD per brand, and
  3.0.0_SA_CVO~Z's grade of 30 added rows each, bar 29 of 30. No gold rebuild before that grade." Prior: msgs 30836, 30823;
  CVO grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND54_TEXT_PLANE_GRADE_20261007.md` @cc31b43fbc;
  record @bb02e46a3b. Decomposition section 69.
- No product file changes in this cell; nothing merges but the worker's deliverables folder. A pass on AC3 does not itself
  flip a `plane`: that is the CTO's ruling on the grade, and a gold rebuild after it.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (no such file); AC2 base FAIL as expected (the
  test is absent). AC3 is judgment.
- The close run is the census itself (AC1's output, read by the issuer); the packet to `3.0.0_SA_CVO~Z` is the two sample
  files.

**COMPLETE (mechanical) 2026-10-07 ~11:5xZ (issuer); AC3 OPEN at `3.0.0_SA_CVO~Z`:**
- **Built:** worker ~105 @2cfcff5500 + @9d2be4abef; merged @1b87f2b0e1 (7 paths, index check 0 of 7 differ). No product file changed.
- **AC1 PASS:** CENSUS OK. Denominator: 242 securities (pool `universe/v1/2026-10-06.json` through `universe_securities.build()`),
  18,619 latest silver articles. Meta: added spans in 935 articles, 672 NEW pairs, added mention count 4,398, title flips 346,
  lead flips 391 (barrons 43, bbg 451, ft 30, sa 282, wsj 129). Lilly: 94 articles, 2 NEW pairs, 294 added, title flips 18, lead
  flips 2 (barrons 5, bbg 26, sa 39, wsj 24). Controls add 0; agreement 40 of 40.
- **AC2 PASS:** 5 of 5.
- **AC3 (judgment):** the two samples (`GOLD_PLANE_CENSUS_SAMPLE.md` / `.json`, 30 added rows each; 28 of Meta's and 1 of
  Lilly's are NEW pairs) are with `3.0.0_SA_CVO~Z`. The issuer holds no verdict.
- **Rows:** AMGT_HARVST-Z-W105-S1 (worker) and AMGT_HARVST-Z-S98 (issuer): gold's alias set for `META_US_Equity` is the
  security key itself, and the same holds for 138 of 242 securities, so Meta's ADDED count is measured against a baseline with no
  company name in it. The Meta figure overstates what the brand adds beside a real legal-name alias; Lilly's baseline carries
  `Eli Lilly` and is not affected.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<status>complete</status>
<round>55</round>
<slot>~105</slot>
<fabric>site-z</fabric>
