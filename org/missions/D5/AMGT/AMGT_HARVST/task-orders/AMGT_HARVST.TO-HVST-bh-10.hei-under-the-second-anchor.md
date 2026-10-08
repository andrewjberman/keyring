# AMGT_HARVST task order -- `HVST-bh-10` -- ROUND 63 (`1.0.0_SA_CTO~Z` msgs 31542, 31551 and 31554, on `3.0.0_SA_CVO~Z`'s grades @31fbcebb42 and @9e8ca92e4e): `HEI` UNDER THE SECOND-ANCHOR RULE -- HAWAIIAN ELECTRIC'S PAIR DROPPED, AND A MEASURED ANSWER TO WHETHER HEICO'S TICKER-LIST PAIRS CAN BE KEPT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~110</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus a READ-ONLY census (S3 GET of the pool universe and the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a changed output for a security the rule does not name, a test with no negative control, a rule loosened to meet the census, a second list where the cell says one, or a gold build.
</preflight>

## 0. THE CELL

You are a later order of this slot's queue: `HVST-bh-3` (the second-anchor rule, with its symbol anchors) is merged into your
base. Read its work first: `ticker_anchors` in `lib/research/harvest/whole_brand_aliases.json` (the `CSL_AU_Equity` entry,
with `anchors` and `symbol_anchors`), the handling in `universe_securities.py`, the branch in `publication_gold.py`
`_security_mentions`, and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh3_census.py`.

`HEI_US_Equity` is HEICO Corporation. Its exact-case ticker form `HEI` is also how Hawaiian Electric Industries (outside
coverage) is written. A reviewer read the 3 served pairs that rest on the form alone
(`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/BH2_NINE_FORMS.md`, rows 3 to 5; grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND61_FALLBACK_AND_NINE_FORMS_GRADE_20261008.md` @31fbcebb42): 2 are HEICO in aerospace ticker lists ("... , ESL , HEI , WWD , LHX ..."), 1 is Hawaiian Electric
("The utility's dividend to HEI remains suspended"). The ruling: HEI joins the second-anchor rule, on the same terms as CSL.

The terms (already ruled; do not widen them): an anchor is the covered company's own name or brand; a SYMBOL anchor is
another listing of the SAME issuer, matched in exact case, and its data row names where the symbol was read from; a word
that is not one of those is never added, and never because it is absent from the wrong row.

## 1. THE BUILD (LOCAL; data and a census, no matcher change)

1. **Data only** (`whole_brand_aliases.json`): one more `ticker_anchors` entry, for `HEI_US_Equity`, form `HEI`,
   `shared_with` "Hawaiian Electric Industries", with the `anchors` (and `symbol_anchors`, each with `listing` and `source`)
   you can honestly show under the terms above, and a `census` naming the grade file and your counts. If the rule's code
   needs no change, change none; if you find it does, stop and say why in your report before changing it.
2. **Plants** `lib/research/harvest/tests/test_bh10_hei_second_anchor.py` (no network): (i) THE NEGATIVE CONTROL, verbatim:
   "The utility's dividend to HEI remains suspended" gives `mention_count` 0 for the HEI security; (ii) a block naming the
   company and a bare "HEI" in another block counts both; (iii) the mutant: with the entry removed, (i) gives 1; (iv) the
   CSL entry's behaviour is unchanged (one assertion re-using a `bh-3` plant's text).
3. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh10_census.py`: BEFORE = `build()` with the HEI entry ignored;
   AFTER = as you leave it. Over every latest silver article with the real `pg._security_mentions`:
   - `DENOMINATOR: securities <S>, silver articles <N>, graded pairs 3 (HEICO 2, Hawaiian Electric 1)`;
   - `HEI_US_Equity: pairs before <p0> after <p1>; dropped <d>`, and EACH dropped pair with its `HEI` span in context;
   - `GRADED HEICO PAIRS KEPT: <g> of 2`; `GRADED HAWAIIAN ELECTRIC PAIRS DROPPED: <h> of 1`;
   - `UNGRADED PAIRS DROPPED: <u>`, each in context;
   - `OTHER SECURITIES CHANGED: <c> of <S>`;
   - last line `CENSUS OK` only if N > 0, g == 2, h == 1 and OTHER SECURITIES CHANGED is 0; otherwise `CENSUS FAIL` and the
     failing line. Write the output as `bh10_census.out`.
4. **A miss is a finding, not a failure of yours.** A ticker list may carry no name, brand or other symbol of HEICO at all. If
   the 2 HEICO pairs cannot be kept under the terms, do NOT loosen the rule and do NOT add a word that is not HEICO's own:
   print `CENSUS FAIL`, show each lost pair's text, state what in the article (if anything) identifies HEICO, and stop there.
   The issuer takes that result back for a ruling.
5. If the S3 read is refused or returns 0 articles: BLOCKING row, stop on AC2. Build no gold.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

## AMENDMENT 1 (issuer, 2026-10-08 ~02:5xZ, before any spawn; `1.0.0_SA_CTO~Z` msg 31558; no gate limb graded it)

Two additions to section 1, both data in `whole_brand_aliases.json`:
- **The existing `CSL_AU_Equity` entry.** Its `symbol_anchors` row for `CSLLY` has a `source` that names only the eight
  articles it admits. The issuer read three stored sources for the string `CSLLY`: the pool universe
  (`s3://opal-data-harvest/universe/v1/2026-10-06.json`, 302 records) 0 occurrences; `lib/research/identity/registrations.json`
  (72 entries) 0 occurrences; the collector's identity record (234 records) 0 occurrences. Append to that row's `source`,
  word for word: `; evidenced by article spans only -- not in the pool (302 records), the identity registry (72) or the
  collector's identity record (234), read 2026-10-08`. Change nothing else on that entry.
- **From here a symbol anchor needs a STORED source or that sentence.** For any `symbol_anchors` row you add for HEI, check
  the same three sources for the symbol and write either the stored source that carries it or
  `evidenced by article spans only` with the three counts. The validator in `universe_securities.py` is not changed for this.
- One more plant in your test file: the `CSL_AU_Equity` entry's `CSLLY` row carries the words `evidenced by article spans
  only` when read from the real file.

<paths>
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/universe_securities.py
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
lib/opal_data_harvest/test_az1_alias_set.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~112/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-10"><invocation>python -m pytest lib/research/harvest/tests/test_bh10_hei_second_anchor.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-10"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh10_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bh-10"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W110-S6`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/AMGT_HARVST.TO-HVST-bh-10.hei-under-the-second-anchor.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-10.hei-under-the-second-anchor`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msgs 31542, 31551 and 31554, on `3.0.0_SA_CVO~Z`'s grades @31fbcebb42 and @9e8ca92e4e. Decomposition section 77.
- msg 31542: "HEI joins R3: Hawaiian Electric Industries is a second-anchor case like Carlisle." msg 31554: "The same rule decides
  HEI" (the issuer's own listing symbol, exact case, with a stated source).
- **The issuer expects this cell may return CENSUS FAIL and cut it to measure that:** the 2 HEICO pairs are bare ticker lists,
  and a pair that rests on the form alone has by definition no name alias in the article. If so, the choice between dropping 2
  good pairs to remove 1 wrong one, or leaving HEI outside the rule, goes to `1.0.0_SA_CTO~Z` with the census.
- Slot ~110's queue, after `bh-9`. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL
  as expected (no such file); AC3 base PASS as expected (460 passed).

**AMENDMENT 2 + COMPLETE 2026-10-08 ~04:2xZ (issuer; `1.0.0_SA_CTO~Z` ruling A, msg 31568; no gate limb graded the amendment):**
- **Built:** worker ~110 (re-seated) @66873bfe98; merged @38ffb95329 (7 paths, index check 0 of 7 differ).
- **AC2 as cut reads CENSUS FAIL: GRADED HEICO PAIRS KEPT is 0 of 2.** The cell was cut to measure exactly that. The ruling: HEI
  is under the rule; the bar becomes "Hawaiian Electric dropped 1 of 1, the HEICO pairs lost are exactly the two named, other
  securities changed 0 of 242". On that bar the census is whole.
- **Census over 19,137 articles:** 43 articles carry an exact-case `HEI` span; 40 name HEICO and are kept; `HEI_US_Equity` pairs
  44 to 41. Dropped: sa:4412260 (Hawaiian Electric) and the two bare aerospace ticker lists sa:3584086 and sa:3685322, in which
  nine whole-article searches for HEICO's name, class-A symbol or units read 0. **Those two are TRUE PAIRS LOST by name** in
  the next rebuild's pair, beside BP's two (four in all). Pairs kept only by the symbol anchor `HEI.A`: 0.
- **AC1 PASS:** 17 of 17. **AC3 PASS:** 491 on the branch; the issuer's drain check is in this close's commit message.
- **AMENDMENT 1 landed:** the `CSLLY` row's source ends "evidenced by article spans only -- not in the pool (302 records), the
  identity registry (72) or the collector's identity record (234), read 2026-10-08"; `HEI.A` carries the same sentence.
- **Existing assertion changed (1):** `test_bh3_ticker_second_anchor.py::test_viii_the_shipped_entry_is_the_one_csl_entry` now
  expects the two keys. **Row Z-W110-S6:** answered by the ruling. **OWED by `3.0.0_SA_CVO~Z`:** the read of the two lost pairs.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>63</round>
<slot>~110</slot>
<fabric>site-z</fabric>
