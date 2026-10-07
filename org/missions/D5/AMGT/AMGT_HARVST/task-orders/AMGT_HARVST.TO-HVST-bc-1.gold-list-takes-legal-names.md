# AMGT_HARVST task order -- `HVST-bc-1` -- ROUND 56 (`1.0.0_SA_CTO~Z` msg 30864 item 2; row AMGT_HARVST-Z-S98): THE GOLD SECURITIES LIST TAKES EACH SECURITY'S LEGAL NAME FROM THE COLLECTOR'S IDENTITY RECORD, AND THE CENSUS PRINTS WHAT EACH NAME GAINS -- NO REBUILD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~106</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus a READ-ONLY census (S3 GET of the pool universe and the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Three collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a name DERIVED from the key or the ticker instead of read from the record, a legal name overriding a name the pool already carries, a census that re-implements the matcher, a changed text-plane brand outcome that goes unreported, or a gold build.
</preflight>

## 0. THE CELL

`lib/research/harvest/universe_securities.py` `securities_from_universe(document, sa_symbols, rule)` builds the `securities`
list every gold builder takes: per security a `company` and an alias set the word-bounded matcher counts as mentions. It
reads the company from the pool universe entry's `name`, and when the entry has none it falls back to the security key
(two places: the `forms_by_key` index loop, `entry.get("name") or entry.get("security_key")`, and the main loop,
`raw_name = entry.get("name") or security_key`).

Measured (row AMGT_HARVST-Z-S98): `build()` against the pool `universe/v1/2026-10-06.json` returns 242 securities, and for
138 of them the alias set is exactly `[security_key]` (`AAPL_US_Equity` aliases `["AAPL_US_Equity"]`). Apple, Amazon,
JPMorgan, Meta, Microsoft and Nvidia are among them. Those names are counted in article text only by exact ticker.

The legal name exists on another plane: the collector's identity record,
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_identity_20261005.json` (the path is the
value of `symbol_resolution_source` in `lib/opal_data_harvest/config.json`): 234 records, each `security_key` and
`company.value` (`"Meta Platforms Inc"`, `"Apple Inc"`), `company.status` MEASURED or DERIVED.

Known about that file (row AMGT_HARVST-Z-S96): 9 names carry a slash tail (`Goldman Sachs Group Inc/The`,
`Coca-Cola Co/The`, `Marriott International Inc/MD`), 1 a receipt tail (`... Co Ltd ADR`), and 10 are exactly 30 characters
long, 5 of them visibly cut (`International Container Termin`, `American International Group I`).

The round-55 census you REUSE: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~105/bb1_census.py` and its
output `bb1_census.out` (18,619 silver articles through `publication_gold._iter_latest_articles()`; Meta's baseline alias set
was `["META_US_Equity"]`; `Meta` added 4,398 spans in 935 articles, 672 NEW pairs; `Lilly` 294 in 94, 2 NEW).

## 1. THE BUILD (LOCAL)

1. **The join** (`universe_securities.py`).
   - `securities_from_universe` gains a keyword `legal_names=None`: a `{security_key: company name}` map. In BOTH loops, the
     name is the pool entry's `name` when it has one; else `legal_names[security_key]` when present; else the security key,
     as today. The pool's own name always wins. Nothing is derived from a key or a ticker.
   - **One cleaning step on a name taken from the map, and only there:** a trailing slash tail (`/The`, `/MD`: a `/` followed
     by letters at the very end) is removed before the name is used. Count it. Nothing else about the name is changed: a cut
     name stays cut and a receipt tail goes through the module's existing rules.
   - `legal_names=None` reproduces today's output byte for byte.
   - Summary gains: `company_name_from_pool`, `company_name_from_identity`, `company_name_absent` (count and the keys),
     `legal_name_slash_tail_stripped` (count and the keys), `legal_name_exactly_30_chars` (the keys, not altered).
   - `build()` gains `legal_names_path=None`. When None it reads the path from `lib/opal_data_harvest/config.json`
     `symbol_resolution_source` AS A FILE (this package does not import `lib.opal_data_harvest`); a caller may pass another
     path. The summary carries `legal_name_join`: the path, records read, securities joined, and the join key
     (`security_key`). A missing or unreadable file raises with the path named: no silent return to the key.
   - Name `HVST-bc-1` in a comment. If any other caller of `securities_from_universe` or `build` exists, list it in your
     report and change none.
2. **Plants** in `lib/research/harvest/tests/test_bc1_legal_names.py` (no network):
   - (i) an entry with no `name` and a legal name `Apple Inc` gets company `Apple Inc` and an alias set that carries `Apple`
     and does not carry the security key;
   - (ii) an entry WITH a pool name keeps it when the map names another;
   - (iii) no pool name and no map entry: the key, as today, and it is counted in `company_name_absent`;
   - (iv) `Coca-Cola Co/The` from the map gives company `Coca-Cola Co`, and it is counted in
     `legal_name_slash_tail_stripped`; a pool name containing a slash is NOT altered;
   - (v) the difference control: on one fixture document, `legal_names=None` equals the output of the function as it is at
     your base commit (keep that expected output as a literal in the test), and passing the map changes ONLY the entries the
     map names;
   - (vi) the text-plane brands: on a fixture with a `plane: text` entry, the brand's outcome (admitted, already an alias or
     refused) is asserted with and without the map.
3. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/bc1_census.py`, importing the REAL
   `universe_securities` and `publication_gold` from your worktree and re-implementing no matcher. BEFORE = `build()` with
   the join off; AFTER = `build()` with it on. Over EVERY latest silver article, with the served matcher's own pattern
   builder (as `bb1_census.py` does):
   - print `DENOMINATOR: securities <S>, silver articles <N>, identity records <R>`;
   - print `KEY-ONLY ALIAS SETS: before <b> of <S>, after <a> of <S>` and the keys still key-only after, each with why (no
     pool name and no identity record);
   - print `WHOLE BRANDS: admitted before <list> after <list>; refused before <list> after <list>`;
   - the per-name table, one line per security whose alias set changed, sorted by pairs gained:
     `<security_key> <company before> -> <company after>: pairs before <p0> after <p1> gained <g>; mention_count before <m0>
     after <m1>`, where a pair is an article with at least one mention of the security;
   - print `TOTAL: names changed <c> of <S>; pairs before <P0> after <P1> gained <G>`;
   - list by key every changed name that is in `legal_name_slash_tail_stripped` or `legal_name_exactly_30_chars`, with its
     pairs gained, under a heading `NAME-QUALITY CLASS`;
   - re-run the round-55 brand question against the AFTER list: for `Meta` and `Lilly`, the same line `bb1_census.py` prints
     (articles with added, NEW pairs, added mention count, title flips, lead flips), headed `AGAINST THE LIST WITH LEGAL
     NAMES`;
   - the agreement control: on a seeded sample of 20 articles and 5 changed securities, the script's AFTER count equals what
     the served matcher returns for that security built from the AFTER list. Print `AGREEMENT: <k> of <n>`.
   - Print `CENSUS OK` as the LAST line only if ALL hold: N > 0; after < before; every key still key-only after has neither
     a pool name nor an identity record; AGREEMENT is n of n; no security's pairs went DOWN. Otherwise `CENSUS FAIL` and the
     failing line. A changed whole-brand outcome does not fail the census: it is printed and you report it.
   - Write the whole output beside it as `bc1_census.out`. Print a progress line every 500 articles.
4. If the S3 read is refused or the iterator returns 0 articles, do not substitute a source: file a BLOCKING row with the
   exact error and stop on AC2.
5. You build NO gold and write NOTHING to S3. A gold rebuild is a later, separately authorised act.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/tests/test_bc1_legal_names.py
lib/research/harvest/tests/test_universe_securities.py
lib/research/harvest/tests/test_alias_rule_round18.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You READ, and never write: `lib/opal_data_harvest/config.json`, the identity record named in section 0,
`lib/research/harvest/publication_gold.py`, `lib/research/harvest/whole_brand_aliases.json`, and the round-55 census script.
Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

## 2. PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bc-1"><invocation>python -m pytest lib/research/harvest/tests/test_bc1_legal_names.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bc-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/bc1_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bc-1"><invocation>python -m pytest lib/research/harvest/tests -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W106-S<k>`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~106/AMGT_HARVST.TO-HVST-bc-1.gold-list-takes-legal-names.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bc-1.gold-list-takes-legal-names`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 30864 (2026-10-07 11:53Z) item 2: "Next HARVST issuance, first cell: gold's list takes each
  security's legal name from the collector's identity record, with the census re-run and the pairs gained printed per name."
  Item 3: ONE gold rebuild after this cell, under its own never-widen pair; none before. Rows AMGT_HARVST-Z-S98 @0dd1c04910,
  Z-W105-S1, Z-S96. Decomposition section 70.
- **Issuer rulings inside the decomposition** (no gate limb graded them): (a) the pool's own name wins over the identity
  record; (b) the slash tail is removed from an identity name on the gold plane only, counted, because `Coca-Cola Co/The`
  as written matches no text and the module's suffix rules do not reach past the slash -- this takes 9 of row Z-S96's 20
  names; the cut names and the receipt tail are left as they are and listed; (c) `build()` reads the identity path from the
  collector's config by default, so the gold builders get the names without a caller change.
- The `<risk>` is LOCAL: the cell changes code and prints a census. The rebuild that moves served chatter is not in it.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected
  (no such file); AC3 base PASS as expected (297 passed).
- The close run is the census itself (AC2's output, read by the issuer). The rebuild's never-widen pair is asked of
  `1.0.0_SA_CTO~Z` in the drain-end message, with the census as its expected-outcome read.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>56</round>
<slot>~106</slot>
<fabric>site-z</fabric>
