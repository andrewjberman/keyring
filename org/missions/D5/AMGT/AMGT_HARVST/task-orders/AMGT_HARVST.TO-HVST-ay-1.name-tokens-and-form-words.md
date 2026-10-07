# AMGT_HARVST task order -- `HVST-ay-1` -- ROUND 52 (round-49 analysis ADDENDUM 3 item 1; CTO @c6a7f4eff8; row Z-S92): A COMPANY'S FORM WORDS ARE NOT REQUIRED IN THE SLUG, AND ITS NAME WORDS MATCH AS WHOLE TOKENS IN ANY ORDER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ay-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~102</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, plants, and an OFFLINE replay over files already on disk. NO publisher host is contacted, no collector or backfill_driver is run, no S3 call. `.runtime` is READ ONLY at the paths named in section 0; never write there and never open a browser profile.
comp-adversary: RUN at L5 -- the adversary is a rule that brings the substring test back to reach the bar (`sap` inside `whatsapp`), a form list declared in two places, a rule that explodes a common-word name (Bank of America, AT&T), or a replay that fetches.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/discovery.py` `_matches(url, query)` decides which sitemap items the wsj and bbg legs fetch. Round 51
(`HVST-ax-1`) replaced a substring test with: the query's words, JOINED, must equal a run of consecutive whole slug tokens
(or that + `s`). `query` is `slug_query(company)` (`lib/opal_data_harvest/publishers.py:258`), which drops TRAILING words
found in `_LEGAL_SUFFIX` (`publishers.py:254`).

Measured after the merge (row AMGT_HARVST-Z-S92), over every finished job with an accepted article:
- **bbg:** 3,282 accepted article URLs, all admitted by the old substring rule; the round-51 rule keeps 3,249 and loses 33.
  - `Amazon.com Inc` -> query `Amazon com` -> joined `amazoncom`: 17 of 17 lost. `com` is a form word no slug carries.
  - `ICICI Bank`, `Universal Music`: the slug carries both words, not adjacent (`hdfc-bank-...-rival-icici`).
- **wsj:** 566 of 566 kept.

The design measured at the cut (issuer, offline): add `com` to the form list, and let a slug match when the joined-adjacent
rule matches OR every query word is a whole slug token (or the word + `s`), in any order. Result: bbg keeps 3,276 of 3,282,
wsj 566 of 566; in the 26,907 stored wsj URLs, AT&T has 11 candidates, SSE 0, Bank of America 9, Amazon 94.
The 6 bbg URLs it still loses are of two classes:
- **substring accident (4):** the name is only INSIDE a longer token -- `sap` in `whatsapp`, `ubs` in `hubs`, `nokia` in
  `nokian`, `monster` in `monsterverse`. No whole-token rule keeps these, and none should.
- **alias (2):** `Eli Lilly`, slug `lilly-to-buy-...` -- the slug carries part of the name. That belongs to a later cell.

Read-only inputs on disk (absolute; NOT in your worktree):
- run records `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-bbg/runs/*.json` and
  `.../.runtime/opal-data-harvest-wsj/runs/*.json` (per job: `publisher`, `security_key`, `ticker`, `accepted[]`, each
  accepted entry carrying `path` to its stored publication JSON, whose `url` is the article URL);
- the company per security: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/harvest-backfill/securities/<security_key>.json`, field `company`;
- stored wsj sitemaps: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-wsj/harvest_listing/*.xml`
  (read every `<loc>`);
- the issuer's own replay, for the shape only: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round51/ax-1.matcher_rules_eval.py`.

## 1. THE BUILD (LOCAL)

1. **One declared form list.** `publishers.py` `_LEGAL_SUFFIX` gains `com`. It stays the ONE list: `discovery.py` declares
   none of its own. `slug_query` is otherwise unchanged (`Amazon.com Inc` -> `Amazon`; `Boeing Co` -> `Boeing`; a name is
   never emptied).
2. **The matcher** (`discovery.py`, `_matches`). Keep the round-51 joined-adjacent rule. ADD: the slug also matches when
   EVERY query word is a whole slug token, or the word + `s` is, in any order. A word never matches inside a longer token.
   An empty query matches nothing. Name `HVST-ay-1` in a comment.
3. **Plants** in `lib/opal_data_harvest/test_ay1_name_tokens.py` (no network):
   - (i) `slug_query("Amazon.com Inc") == "Amazon"`, and `_matches` admits
     `amazon-ramps-up-india-fast-commerce-push-to-take-on-local-rivals` for it;
   - (ii) any order: `ICICI Bank` admits `hdfc-bank-is-at-risk-of-losing-its-top-nifty-spot-to-rival-icici`; `Universal
     Music` admits `suno-stares-down-universal-and-sony-to-reshape-the-future-of-music`;
   - (iii) still refused: `SAP` against `venezuelan-oil-industry-is-running-on-whatsapp-after-cyberattack`; `UBS` against
     `iran-war-prompts-rethink-of-saudi-uae-qatar-finance-hubs-stability-premium`; `SSE` against
     `ithaca-energy-to-buy-offshore-canada-oil-assets-from-suncor-x1`; `AT T` against
     `oil-little-changed-as-traders-weigh-mideast-crude-export-data-6785f907`;
   - (iv) round 51's hits still hold: `at t` / `at-t-to-buy-spectrum-licenses-9f3c`; `mcdonald s` /
     `mcdonalds-sales-rise-on-value-meals-5e2a`; `boeing` / `boeings-new-chief-faces-a-test-77de`;
   - (v) the mutant: a rule that tests `word in slug` makes (iii) fail.
4. **Existing tests.** `lib/opal_data_harvest/test_ax1_slug_phrase_and_bound.py` asserts that `eli lilly` does NOT match
   `eli-manning-and-lilly-pulitzer-22bb`; under the any-order rule it DOES (both words are whole tokens; the body check
   rejects it later). Change that one assertion and say so in your report. Change any other existing assertion only if this
   cell's rule is the reason, and list each.
5. **The offline replay** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~102/ay-1.replay.py`, importing
   the REAL `_matches` and `slug_query` from your worktree and defining the OLD substring rule inline:
   - recall: for bbg and for wsj, over every finished job with an accepted article, count the accepted URLs the OLD rule
     admits (with the round-51 `slug_query`, i.e. `com` kept) and how many the NEW rule + NEW `slug_query` keep. Print
     `<pub>: kept <k> of <n>`. Print every lost URL as `LOST <class> <query> <slug>`, where class is `substring_accident`
     when the old rule matched only because a query word sits inside a longer slug token, else `alias`;
   - selectivity over the stored wsj `<loc>` URLs: print `<company>: old <n> new <m>` for `AT&T Inc`, `SSE PLC`,
     `Bank of America Corp`, `Amazon.com Inc`, `Meta Platforms Inc`;
   - print `REPLAY OK` only if ALL hold: wsj kept == n; bbg lost <= 6 and every lost URL is class `substring_accident` or
     its query is `Eli Lilly`; AT&T new <= 100; SSE new <= 100; Bank of America new <= 100. Otherwise `REPLAY FAIL` and the
     failing line.
   - Write its output beside it as `ay-1.replay.out`.
   - If the bar is missed, do NOT loosen the rule toward substring matching: report the count and the lost lines.
6. The harvest suite stays green: `python -m pytest lib/opal_data_harvest -q -p no:cacheprovider`. Report the count.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/discovery.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/test_ay1_name_tokens.py
lib/opal_data_harvest/test_ax1_slug_phrase_and_bound.py
lib/opal_data_harvest/test_af4_discovery_hookup.py
lib/opal_data_harvest/test_af4_sitemap_listing.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~102/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ay-1"><invocation>python -m pytest lib/opal_data_harvest/test_ay1_name_tokens.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ay-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~102/ay-1.replay.out</invocation><expect>REPLAY OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ay-1"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W102-S<k>`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~102/AMGT_HARVST.TO-HVST-ay-1.name-tokens-and-form-words.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ay-1.name-tokens-and-form-words`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Round-49 analysis ADDENDUM 3 item 1 @c6a7f4eff8; decomposition section 65; row AMGT_HARVST-Z-S92 @24a2d1cf45.
- **The bar, amended by the issuer at the cut, and why:** ADDENDUM 3 sets 3,282 of 3,282 bbg. Measured offline before the
  cut, the design ADDENDUM 3 names (form words not required, names tokenized on punctuation) reaches 3,276: 4 of the 6
  residual URLs were admitted by the old rule ONLY as substring accidents (`sap` in `whatsapp`, `ubs` in `hubs`, `nokia` in
  `nokian`, `monster` in `monsterverse`), which no whole-token rule can keep, and 2 are Eli Lilly slugs carrying `lilly`
  alone, which is ADDENDUM 3 item 2's alias case. AC2's bar is therefore bbg lost <= 6 with each lost URL in one of those two
  classes; wsj 566 of 566 and the T, SSE bounds are as written. No gate limb graded this amendment.
- ADDENDUM 3 item 2 (the alias set per name) is NOT in this issuance: it is separate and non-gating by the ruling, and its
  input (the research-folder name per security) is unread. It is section 66's cell, cut in its own round.
- The close run is the issuer's: bbg resumes after Andrew's hand-solve of its bot check (`--clear-stop bbg`); the OMAB pair,
  concluded on the round-51 rule, is re-run with `--names`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>52</round>
<slot>~102</slot>
<fabric>site-z</fabric>
