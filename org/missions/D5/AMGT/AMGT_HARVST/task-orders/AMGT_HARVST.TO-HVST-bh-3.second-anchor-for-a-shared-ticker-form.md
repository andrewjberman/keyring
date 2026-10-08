# AMGT_HARVST task order -- `HVST-bh-3` -- ROUND 61 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): A BARE TICKER FORM SHARED WITH A COMPANY OUTSIDE COVERAGE COUNTS ONLY BESIDE A SECOND ANCHOR -- `CSL` IS THE CASE: 39 GOOD PAIRS KEPT, 3 CARLISLE PAIRS DROPPED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-3</owned_cells>
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

You are the third order of this slot's queue: `HVST-bh-4` (so `CSL_AU_Equity` now carries the company name `CSL LTD`) and
`HVST-bh-5` are merged into your base.

`CSL_AU_Equity` is CSL Limited, the Australian biotech. Its exact-case ticker form `CSL` is also the New York ticker of
Carlisle Companies, which is outside coverage. A reviewer read all 42 served pairs that rest on the form: 39 name CSL Limited,
3 are Carlisle in a ticker list ("Carlisle Companies ( NYSE: CSL )"). The 42 pairs with every span in context are in
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round58/GOLD_REBUILD8_CSL_SAMPLE.json` (`all_pairs`; the three
Carlisle rows carry `article_carries_carlisle: true`) and `.../round58/GOLD_REBUILD8_CSL_ALL42.md`.

The rule: **where a security's bare ticker form is shared with a company outside coverage, a pair counts on that form only
when the article also carries a SECOND ANCHOR: the covered company's own name, or a brand of it.** A precedent is already in
the code: `HVST-bd-1`'s `anchored_aliases` (a bare "Lilly" counts only beside "Eli Lilly" or `LLY`) in
`universe_securities.py` and `publication_gold.py` `_security_mentions`. Read it first and build beside it in its style.

## 1. THE BUILD (LOCAL)

1. **The data** (`lib/research/harvest/whole_brand_aliases.json`): a new top-level list `ticker_anchors`, one entry:
   `{"ticker": "CSL", "security_key": "CSL_AU_Equity", "shared_with": "Carlisle Companies (NYSE: CSL)", "anchors": [...],
   "census": "<the grade file and hash, and your census counts>"}`. The grade file is
   `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND58_GOLD_REBUILD8_CSL_FORM_GRADE_20261007.md @f6e370e6cc`.
   `anchors` holds brands or names of CSL Limited ONLY, each one you can show in the text of at least one of the 39 good
   articles (for example a subsidiary's name); never a word that is not the company's own name or brand, and never a word
   chosen because it is absent from the Carlisle rows. Extend `about` by one sentence. Keep the file ASCII.
2. **The list** (`universe_securities.py`): an entry is validated (a known security carrying that exact ticker form, a
   non-empty `census`; else raise with the entry named). The security gains two fields: `anchor_required_ticker_aliases`
   (the forms under the rule) and `ticker_anchor_aliases` (the entry's `anchors`). A security with no entry gains neither
   key, so its dict is byte-equal to today's. The summary gains `ticker_forms_anchored`.
3. **The matcher** (`publication_gold.py`, `_security_mentions`): a form in `anchor_required_ticker_aliases` is counted only
   when the article (title and all blocks) has at least one span of the security's name aliases, of another of its ticker
   forms, or of `ticker_anchor_aliases`. When it has none, the form is left out of the count and every returned field comes
   from the count without it. The anchors themselves count as mentions only as their own spans beside the form, exactly as
   an alias would. A security with neither field takes today's code path unchanged. Name `HVST-bh-3` in a comment.
4. **Plants** `lib/research/harvest/tests/test_bh3_ticker_second_anchor.py` (no network):
   - (i) THE NEGATIVE CONTROL, verbatim: a block "newly promoted Carlisle Companies ( CSL )" gives `mention_count` 0 for the
     CSL security;
   - (ii) "Carlisle Cos. ( NYSE: CSL )" alone gives 0;
   - (iii) a block carrying the company's name and a bare "CSL" in another block counts both;
   - (iv) one of your `anchors` in the title and a bare "CSL" in a block counts the form;
   - (v) lower-case "csl" is not the form and does not anchor;
   - (vi) the mutant: with the entry removed, (i) gives 1 -- assert that, so the control is shown to bite;
   - (vii) a security with no entry is byte-equal in the list and takes the same counts as before;
   - (viii) an entry naming a form the security does not carry, or with no `census`, raises.
5. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh3_census.py`: BEFORE = `build()` with `ticker_anchors` ignored;
   AFTER = as you leave it. Over every latest silver article with the real `pg._security_mentions`:
   - `DENOMINATOR: securities <S>, silver articles <N>, graded pairs 42 (good 39, Carlisle 3)`;
   - `CSL_AU_Equity: pairs before <p0> after <p1>; dropped <d>` and each dropped article key with its `CSL` span in context;
   - `GRADED GOOD PAIRS KEPT: <g> of 39`; `GRADED CARLISLE PAIRS DROPPED: <c> of 3`;
   - `UNGRADED PAIRS DROPPED: <u>` (pairs newer than the 42), each in context, for a reviewer;
   - `OTHER COVERED FORMS UNDER THE RULE: <n>` (entries other than CSL) and `OTHER SECURITIES CHANGED: <c2> of <S>`;
   - last line `CENSUS OK` only if N > 0, g == 39, c == 3 and OTHER SECURITIES CHANGED is 0; otherwise `CENSUS FAIL` and the
     failing line. Write the output as `bh3_census.out`.
6. If the 39 cannot all be kept with anchors that are honestly the company's name or brands: do NOT loosen the rule and do
   NOT add a word that is not one. Print `CENSUS FAIL`, list each good pair that has no anchor with its text in context, and
   report that. That result is a finding the issuer takes back, not a failure of yours.
7. If the S3 read is refused or returns 0 articles: BLOCKING row, stop on AC2. Build no gold.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/universe_securities.py
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
lib/opal_data_harvest/test_az1_alias_set.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round58/GOLD_REBUILD8_CSL_SAMPLE.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round58/GOLD_REBUILD8_CSL_ALL42.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-3"><invocation>python -m pytest lib/research/harvest/tests/test_bh3_ticker_second_anchor.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh3_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bh-3"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W110-S3`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/AMGT_HARVST.TO-HVST-bh-3.second-anchor-for-a-shared-ticker-form.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-3.second-anchor-for-a-shared-ticker-form`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 75.
- R3: "where a security's bare ticker form is shared with a company outside coverage, a pair needs a second anchor in the article
  (the covered company's name or a brand) or it is not counted. CSL is its real case; the cell states how many other covered
  forms it changes, with 0 good pairs lost on the 39."
- **Issuer rulings inside the decomposition** (no gate limb graded them): the rule is DATA (`ticker_anchors`), so it changes a
  form only where an entry names it, and "how many other covered forms" is the entry count; the anchor words are the company's
  own, never chosen by their absence from the wrong rows; a miss on the 39 comes back as a finding, not a looser rule.
- Slot ~110's queue, third. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as
  expected (no such file); AC3 base PASS as expected (419 passed).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>61</round>
<slot>~110</slot>
<fabric>site-z</fabric>
