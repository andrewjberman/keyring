# AMGT_HARVST task order -- `HVST-bd-1` -- ROUND 57 (`1.0.0_SA_CTO~Z` msgs 30873, 30876; CVO grade @8289c4e3ed): `Meta` IS A GOLD BRAND, AND A BARE `Lilly` COUNTS ON GOLD ONLY BESIDE `Eli Lilly` OR THE TICKER -- DATA, MATCHER, CENSUS, NO REBUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~106</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus a READ-ONLY census (S3 GET of the pool universe and the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Three collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is an anchor that any lower-case `lly` or another company's name satisfies, an anchored brand that leaks into the collector or into a security with no anchor entry, a changed output for a security that carries no gold entry, a test with no negative control, or a gold build.
</preflight>

## 0. THE CELL

You built `HVST-bc-1` (merged): `lib/research/harvest/universe_securities.py` now takes each security's legal name from the
collector's identity record, so `META_US_Equity` carries `["Meta Platforms Inc", "Meta Platforms"]` and `LLY_US_Equity`
carries `["Eli Lilly"]`. Your `bc1_census.out` printed, against that list: `Meta` adds 3,626 spans in 642 of 18,634 articles
(171 NEW pairs); `Lilly` adds 294 spans in 94 articles (2 NEW pairs).

`lib/research/harvest/whole_brand_aliases.json` `whole_brands` carries both as `"plane": "slug"` entries (the collector's
slug set) with a `text_census` field (the collector's text check). The gold text matcher takes neither today: it reads
`plane == "text"` entries only.

The graded ruling this cell lands (the grader read 30 added spans per brand):
1. **`Meta` is admitted on the gold plane**, 30 of 30. A bare `Meta` is a mention of `META_US_Equity` in any article.
2. **`Lilly` is admitted on the gold plane WITH AN ANCHOR.** A bare `Lilly` is a mention of `LLY_US_Equity` only in an
   article that ALSO carries one of the security's unanchored aliases (`Eli Lilly`) or its exact-case ticker form (`LLY`),
   anywhere in the title or the blocks.
3. Why: of Lilly's 2 NEW pairs over 18,634 articles, one is a TV review, `wsj:510e7738-752c-4376-889b-7f0d60761963`, block 2:
   "furious that his wife, Lilly (Jane Kaczmarek), has died" -- a character's first name. The other,
   `barrons:WP-BAR-0001937680`, is a link line, "How Lilly just extended its lead in weight-loss drug race." Neither article
   carries `Eli Lilly` or `LLY`. The anchor drops both, and that cost is accepted. The other 292 spans sit in articles the
   legal name already attributes.
4. The collector is NOT changed: `plane` stays `slug` on both entries and `lib/opal_data_harvest` reads the list as before.
5. NO gold is built in this cell.

The gold matcher: `lib/research/harvest/publication_gold.py` `_security_mentions(article_row, security)` counts spans for
the security's `aliases` and exact-case `ticker_aliases` over the title and `text_blocks` (`_match_counts`,
`_span_pattern`: longest first, word-bounded, one span one count).

## 1. THE BUILD (LOCAL)

1. **The data** (`whole_brand_aliases.json`). Each of the two entries gains a `gold` object, nothing else on them changes:
   - Meta: `{"admitted": true, "anchor": "none", "census": "<the grade file path and hash below>: 30 of 30 added spans name
     the company; against the list with legal names the brand adds 3,626 spans in 642 of 18,634 articles, 171 new pairs
     (.../0.9.0_WK_AMGT_HARVST~106/bc1_census.out)"}`;
   - Lilly: `{"admitted": true, "anchor": "own_name_or_ticker", "census": "<the grade file>: 29 of 30; the miss is a first
     name (wsj:510e7738-752c-4376-889b-7f0d60761963); 2 new pairs of 18,634, both dropped by the anchor
     (org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round56/LILLY_GOLD_NEW_PAIRS_READ.md)"}`.
   - The grade file is `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND55_GOLD_PLANE_GRADE_20261007.md @8289c4e3ed`.
   - Extend `about` by one sentence: what `gold` and its `anchor` mean. Keep the file ASCII.
2. **The list** (`universe_securities.py`).
   - A `whole_brands` entry is a gold brand when `plane == "text"` (as today, unanchored) OR it carries
     `gold.admitted == true`. A `gold` object whose `anchor` is not `none` or `own_name_or_ticker`, or with no `census`,
     raises with the entry named.
   - An unanchored gold brand goes through the existing admit path (`brand_refusal`, already-an-alias, appended after every
     other alias). An anchored one goes through the SAME refusal check and, when admitted, lands in a NEW per-security field
     `anchored_aliases` (a list) and NOT in `aliases`.
   - The summary gains `gold_brand_admitted`, `gold_brand_anchored`, `gold_brand_refused` (each a list of
     `{security_key, brand}`), beside the existing whole-brand fields, whose values for the `plane: text` entries do not
     change.
   - A security with no anchored brand carries no `anchored_aliases` key, so every such security's dict is byte-equal to
     what the function returns today.
3. **The matcher** (`publication_gold.py`, `_security_mentions`).
   - Count as today with `aliases` and the exact-case ticker forms. If the security carries `anchored_aliases` AND that
     count over the title and all blocks is at least 1, count again with `aliases + anchored_aliases`; else keep the first
     count. Every returned field comes from the count that was kept. `match_forms` names the anchored form when it won a
     span.
   - A security with no `anchored_aliases` takes the exact code path it takes today.
   - Name `HVST-bd-1` in a comment. Change nothing else in that file.
4. **Plants** in `lib/research/harvest/tests/test_bd1_gold_brands_and_anchor.py` (no network):
   - (i) THE NEGATIVE CONTROL, verbatim text: an article whose block is "Sam Cooper (Mr. Molina), the newest neighbor, is
     furious that his wife, Lilly (Jane Kaczmarek), has died" gives `mention_count` 0 for the Lilly security;
   - (ii) the link line alone ("How Lilly just extended its lead in weight-loss drug race.") gives 0;
   - (iii) an article with "Eli Lilly said" in one block and "Lilly's shares rose" in another gives 2, and `match_forms`
     names both forms;
   - (iv) the ticker anchors: "LLY" in the title and a bare "Lilly" in a block gives 2; lower-case "lly" does not anchor;
   - (v) another company's name does not anchor: an article carrying "Novo Nordisk" and a bare "Lilly" gives 0 for Lilly;
   - (vi) Meta is unanchored: a title carrying a bare "Meta" and no "Meta Platforms" gives 1; "metadata" and "Metaverse"
     give 0;
   - (vii) the mutant: with the anchor removed (the brand placed in `aliases`), (i) gives 1 -- assert that, so the control
     is shown to bite;
   - (viii) from the real list file: `securities_from_universe` on a fixture pool document puts `Meta` in
     `META_US_Equity`'s `aliases`, `Lilly` in `LLY_US_Equity`'s `anchored_aliases` and not in its `aliases`, and leaves a
     security with no gold entry byte-equal with and without the two `gold` objects;
   - (ix) a `gold` object with an unknown `anchor` raises.
5. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/bd1_census.py`, reusing your
   `bc1_census.py` reading. BEFORE = `build()` on the list as merged with the two `gold` objects ignored (a rule copy with
   them removed); AFTER = `build()` as you leave it. Counts come from the REAL `_security_mentions`, over every latest silver
   article:
   - print `DENOMINATOR: securities <S>, silver articles <N>`;
   - per brand: `<security_key> <brand>: pairs before <p0> after <p1> gained <g>; mention_count before <m0> after <m1>;
     title flags gained <t>; lead flags gained <l>`;
   - `LILLY ANCHOR: bare-Lilly articles with no anchor <k>`, and list each by article key with its span in context;
   - `OTHER SECURITIES CHANGED: <c> of <S>` (every security other than the two whose pairs or mention count differ);
   - print `CENSUS OK` as the LAST line only if ALL hold: N > 0; Lilly's pairs gained == 0; Lilly's mention count gained
     > 0; both `wsj:510e7738-752c-4376-889b-7f0d60761963` and `barrons:WP-BAR-0001937680` are in the no-anchor list; Meta's
     pairs gained > 0; OTHER SECURITIES CHANGED is 0. Otherwise `CENSUS FAIL` and the failing line.
   - Write the whole output beside it as `bd1_census.out`. Print a progress line every 500 articles.
6. If the S3 read is refused or returns 0 articles, do not substitute a source: file a BLOCKING row and stop on AC2.
7. If the bar is missed, do not loosen the anchor or edit the list beyond item 1: report the failing line and the counts.

Worktree: the one you hold (the issuer brings it up to the merged CLOUD before handing you this order).

<paths>
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/universe_securities.py
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_bd1_gold_brands_and_anchor.py
lib/research/harvest/tests/test_alias_rule_round18.py
lib/research/harvest/tests/test_universe_securities.py
lib/research/harvest/tests/test_bc1_legal_names.py
lib/opal_data_harvest/test_az1_alias_set.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

## 2. PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bd-1"><invocation>python -m pytest lib/research/harvest/tests/test_bd1_gold_brands_and_anchor.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bd-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/bd1_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bd-1"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W106-S3`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/AMGT_HARVST.TO-HVST-bd-1.gold-brands-and-the-lilly-anchor.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bd-1.gold-brands-and-the-lilly-anchor`. Pin every artifact row to the commit that
  carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 30873 (Meta admitted on gold 30 of 30; Lilly admitted with the anchor; "the entry records
  the anchor as data, with a test whose negative control is that TV review; it rides the one gold rebuild after the Z-S98
  names cell") and msg 30876 (the anchor stands at its measured cost). CVO grade
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND55_GOLD_PLANE_GRADE_20261007.md` @8289c4e3ed. The second-pair
  read @2aba59986e; the committed script re-run returned the same 2 pairs over 18,635 articles. Decomposition section 71.
- **Issuer rulings inside the decomposition** (no gate limb graded them): the anchor is carried as a per-security
  `anchored_aliases` field read by `_security_mentions`, so a security without one takes today's code path unchanged; the
  gold admission is a `gold` object on the entry and `plane` stays `slug`, so one entry serves both planes without the
  collector reading a new value.
- Same chain as `bc-1` (both write `universe_securities.py`), so it goes to worker ~106's queue, continued with its context.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected
  (no such file); AC3 base PASS as expected (380 passed on merged CLOUD @0b35eeba2a).
- The close run is the census (AC2's output, read by the issuer). After it: the request to `1.0.0_SA_CTO~Z` for the ONE gold
  rebuild's never-widen pair, with `bc1_census.out` and `bd1_census.out` as the expected-outcome read.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>57</round>
<slot>~106</slot>
<fabric>site-z</fabric>
