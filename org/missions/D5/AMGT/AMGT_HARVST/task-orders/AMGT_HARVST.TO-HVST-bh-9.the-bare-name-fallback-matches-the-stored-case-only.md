# AMGT_HARVST task order -- `HVST-bh-9` -- ROUND 63 (`1.0.0_SA_CTO~Z` msgs 31542, 31551 and 31554, on `3.0.0_SA_CVO~Z`'s grades @31fbcebb42 and @9e8ca92e4e): THE BARE-NAME FALLBACK MATCHES THE COMPANY NAME IN ITS STORED CASE ONLY -- NOKIA'S PAIRS KEPT, THE VERB `sap` AND `200-bp` GONE, EVERY REMOVED PAIR PRINTED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-9</owned_cells>
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

You are a later order of this slot's queue: `HVST-bh-4`, `bh-5`, `bh-3` and `bh-7` are merged into your base.

`lib/research/harvest/publication_gold.py` `_security_aliases(security)` returns
`list(security.get("aliases") or [security["company"]])`: a security whose alias list is EMPTY is matched on its `company`
string, and name aliases match case-insensitively. A census of the served gold
(`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~111/bh1_fallback_census.out`, script beside it) found 5 such
securities and 277 pairs that rest on that fallback alone: Nokia 262 (every one with a span in the stored case), BP (US) 8
and SAP 7 (none of the 15 with a stored-case span). A reviewer read all 15: 13 are not about the company (the verb "sap",
"a 200-bp margin increase") and 2 are (`sa:4473686`, `sa:4441205`, where BP writes its own name in lower case).

The ruling: **the fallback matches the company name in its STORED CASE only.** The two true BP pairs are lost with the 13,
by name; no context test is built for them.

## 1. THE BUILD (LOCAL)

1. **The matcher** (`publication_gold.py`). When a security has no aliases, its `company` string is matched CASE-SENSITIVELY,
   exactly as written (the way an exact ticker form is matched today), and not case-insensitively. A security with a
   non-empty alias list takes today's code path unchanged, byte for byte in what it returns. `match_forms` still names the
   company string when it won a span. Name `HVST-bh-9` in a comment. Change nothing else in that file.
2. The collector (`lib/opal_data_harvest`) is not changed.
3. **Plants** `lib/research/harvest/tests/test_bh9_fallback_stored_case.py` (no network), on securities with an empty alias
   list:
   - (i) THE NEGATIVE CONTROL, verbatim titles: "Tax Changes Sap Demand" and "Quant Curbs Sap Volatility" give
     `mention_count` 0 for a security whose company is `SAP`;
   - (ii) a block "a 200-bp margin increase" gives 0 for a security whose company is `BP`;
   - (iii) "Nokia said" gives 1 for company `Nokia`; "NOKIA" alone gives 0 through the fallback (and 1 when `NOKIA` is in
     the security's `ticker_aliases`, which is how the real security carries it);
   - (iv) "SAP reported" gives 1 for company `SAP`;
   - (v) a security WITH aliases is unchanged: its lower-case alias hit still counts;
   - (vi) the mutant: with the fallback case-insensitive again, (i) gives 1 each -- assert that.
4. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh9_census.py`, following `bh1_fallback_census.py`'s reading of the
   list file `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json` and of silver. BEFORE = the matcher with the fallback case-insensitive (the
   mutant of plant (vi), stated in the file how); AFTER = as you leave it. Over every latest silver article:
   - `DENOMINATOR: securities <S>, with an empty alias list <E>, silver articles <N>`;
   - per empty-alias security: `<security_key> company=<c>: pairs before <p0> after <p1> removed <r>`;
   - `REMOVED PAIRS: <R>`, then EACH removed pair: security_key, article_key, title, and every span of the company string
     with 120 characters of context each side (these go to a reviewer);
   - `TRUE PAIRS LOST BY NAME: sa:4473686 <removed|still present>, sa:4441205 <removed|still present>`;
   - `SECURITIES WITH ALIASES CHANGED: <c> of <S - E>`;
   - last line `CENSUS OK` only if N > 0, E > 0, no removed pair has a stored-case span, Nokia's removed count is 0, both
     named BP pairs read `removed`, and SECURITIES WITH ALIASES CHANGED is 0; otherwise `CENSUS FAIL` and the failing line.
     Write the output as `bh9_census.out`.
5. If the S3 read is refused or returns 0 articles: BLOCKING row, stop on AC2. Build no gold.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round60/securities.universe.r60.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~111/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-9"><invocation>python -m pytest lib/research/harvest/tests/test_bh9_fallback_stored_case.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-9"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh9_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bh-9"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W110-S6`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/AMGT_HARVST.TO-HVST-bh-9.the-bare-name-fallback-matches-the-stored-case-only.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-9.the-bare-name-fallback-matches-the-stored-case-only`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msgs 31542, 31551 and 31554, on `3.0.0_SA_CVO~Z`'s grades @31fbcebb42 and @9e8ca92e4e. Decomposition section 77.
- msg 31542: "The fallback to a bare company name matches the name in its stored case only." msg 31551: the two true BP pairs
  "are REMOVED and NAMED as lost"; "no context test is built for two pairs"; the next rebuild's rule allows a lost pair only by
  name. Grades: `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND61_FALLBACK_AND_NINE_FORMS_GRADE_20261008.md` @31fbcebb42 and the read of the other 12 @9e8ca92e4e.
- Answered already to `1.0.0_SA_CTO~Z` (msg after 31551): R3's second anchor keeps 0 of the 2 true BP pairs, since a pair in
  the fallback-only class has by construction no stored-case `BP` and no ticker-form span.
- `deliverables/0.9.0_WK_AMGT_HARVST~111/` is in `<paths>` to be READ (the earlier census script); this slot writes its own
  folder only.
- Slot ~110's queue, after `bh-7`. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL
  as expected (no such file); AC3 base PASS as expected (460 passed).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>63</round>
<slot>~110</slot>
<fabric>site-z</fabric>
