# AMGT_HARVST task order -- `HVST-az-1` -- ROUND 54 (round-49 analysis ADDENDUM 3 item 2 as ruled by ADDENDUM 6 @c1f0c8a429; rows Z-S95, Z-S96): A NAME'S SLUG QUERY IS AN ALIAS SET, AND A BRAND WORD ENTERS IT ONLY FROM THE HAND-WRITTEN LIST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-az-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~104</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, plants, and an OFFLINE replay over files already on disk. NO publisher host is contacted, no collector or backfill_driver is run, no S3 call. `.runtime` is READ ONLY at the paths named in section 0; never write there and never open a browser profile. Three collection legs are LIVE on the shared tree while you work: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a first-word rule that reaches Meta and also admits `bank` for Bank of America; a brand derived from any field instead of read from the list; a slug brand leaking into the gold text matcher; a second sitemap fetch per alias; or a replay that fetches.
</preflight>

## 0. THE CELL

The wsj and bbg legs pick which sitemap items to fetch with `lib/opal_data_harvest/discovery.py` `_matches(url, query)`,
where `query` is `slug_query(security["company"])` (`lib/opal_data_harvest/publishers.py`, three call sites: in
`_sitemap_items`, `_bloomberg_sitemap`, and one further site near line 782). `slug_query` drops trailing form words; the
matcher wants every remaining word as a whole slug token.

That loses a company its headlines call by a brand word:
- `Meta Platforms Inc` -> query `Meta Platforms`: 2 candidates in the 26,907 stored wsj URLs, where 118 slugs carry the
  token `meta`.
- `Eli Lilly & Co` -> query `Eli Lilly`: 2 accepted bbg URLs are lost because their slug carries `lilly` alone
  (`lilly-to-buy-...`).

The ruling (binding on this cell):
1. **Each name's slug query is an ALIAS SET.** A slug is a candidate when `_matches` admits it for ANY ONE alias's
   `slug_query`. Nothing else about `_matches` or `slug_query` changes.
2. **A brand word is NEVER derived.** Not a first word, not a ticker, not a domain label. It enters one security at a time
   from the hand-written list `lib/research/harvest/whole_brand_aliases.json`, key `whole_brands`, and each entry cites the
   census that admitted it.
3. **Each plane has its own census.** The 7 entries in the list today (Dell, TJX, ASML x2, Micron, Uber, Spotify) were
   admitted on ARTICLE-TEXT hits for the gold text matcher (`lib/research/harvest/universe_securities.py`). They are NOT
   slug brands. An entry records which plane admitted it.
4. **The first two slug entries are Meta (`META_US_Equity`, brand `Meta`) and Lilly (`LLY_US_Equity`, brand `Lilly`).**
   Amazon needs none. No other entry is added in this cell.
5. **The carrier is the collector's `aliases` field.** `lib/opal_data_harvest/__main__.py` `universe(config)` builds each
   security with `aliases` from the identity file (today exactly one alias per name, the legal name, 234 names).
6. The wsj unselective bound (`contracts.json` `unselective_after`: 100, `worker._until_unselective`) and the acceptance
   stage's `company_not_mentioned` filter are NOT changed by this cell.

Read-only inputs on disk (absolute; NOT in your worktree):
- run records `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-bbg/runs/*.json` and
  `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-wsj/runs/*.json`;
- the company per job key: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/harvest-backfill/securities/<key>.json`;
- stored wsj sitemaps: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-wsj/harvest_listing/*.xml`;
- the round-52 replay, whose reading of those three inputs you REUSE:
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~102/ay-1.replay.py` and its output
  `ay-1.replay.out` (bbg kept 3,276 of 3,282; wsj 566 of 566; AT&T new 11; Bank of America new 9; Meta Platforms new 2).

## 1. THE BUILD (LOCAL)

1. **The list** (`lib/research/harvest/whole_brand_aliases.json`).
   - Every `whole_brands` entry gains `"plane"`. The 7 existing entries get `"plane": "text"`, otherwise byte-for-byte
     unchanged.
   - Add two entries with `"plane": "slug"`: `META_US_Equity` / `Meta` and `LLY_US_Equity` / `Lilly`. Each `census` string
     cites your replay output by path and gives the slug candidates before and after and the accepted URLs kept before and
     after, as your replay printed them.
   - Extend `about` by one sentence saying what `plane` means. Keep the file ASCII.
2. **The gold text matcher is unchanged in behaviour** (`lib/research/harvest/universe_securities.py`). It reads only
   `plane == "text"` entries. An entry with no `plane`, or a value other than `text` or `slug`, raises with the entry named.
   Its alias output for the pool is the same as before this cell: no `Meta`, no `Lilly`.
3. **The collector's alias set** (`lib/opal_data_harvest/__main__.py` `universe(config)`). After the identity aliases, append
   the brand of each `plane == "slug"` entry whose `security_key` equals the security's `security_key`; no duplicates;
   order kept. The list's path comes from a new `config.json` key `slug_brand_source`
   (`lib/research/harvest/whole_brand_aliases.json`), read as a file: `lib/opal_data_harvest` does NOT import
   `lib.research`. A slug entry whose `security_key` matches no security raises with the key named. Add the same path to
   the release inputs in `lib/opal_data_harvest/build_release.py` beside `symbol_resolution_source`.
4. **The alias-set match.**
   - `publishers.py`: one new function `slug_queries(security)` returning the distinct `slug_query` of the company and of
     each alias, company first. Name `HVST-az-1` in a comment.
   - `discovery.py`: `discover` accepts one query or a list, and yields a hit when `_matches` admits it for ANY query. ONE
     sitemap request per month whatever the number of aliases. `_matches` itself is not edited.
   - `_sitemap_items` passes the set. The listing record name (`"sitemap:" + query`) and every `search_query` provenance
     value keep the COMPANY's query, so nothing already stored is renamed. Read the other two call sites and change one
     only if it selects candidates; say in your report what each does and whether you changed it.
5. **Plants** in `lib/opal_data_harvest/test_az1_alias_set.py` (no network, no `.runtime`):
   - (i) from the real `universe(config)`: `META_US_Equity` aliases contain `Meta`; `LLY_US_Equity` contain `Lilly`;
     `BAC_US_Equity` and `T_US_Equity` each carry exactly their one legal name; the number of securities with more than one
     alias is exactly 2 of 234; none of `Dell`, `TJX`, `ASML`, `Micron`, `Uber`, `Spotify` was added to any security;
   - (ii) Meta's set admits `meta-to-cut-thousands-of-jobs-1a2b`; Lilly's set admits `lilly-to-buy-gene-editing-firm-3c4d`;
     the company's own two-word slugs still match;
   - (iii) controls: Bank of America's set refuses `bank-stocks-fall-as-yields-rise-5e6f`; AT&T's set refuses
     `oil-little-changed-as-traders-weigh-mideast-crude-export-data-6785f907` and admits
     `at-t-to-buy-spectrum-licenses-9f3c`;
   - (iv) a stub session counting requests: `discover` with a two-query list makes the same number of requests as with one;
   - (v) the mutant: a first-word rule (the first word of the company as an alias) makes (iii) fail on the Bank of America
     slug;
   - (vi) the guard: call `lib.research.harvest.universe_securities.brand_refusal` for the two slug entries the way that
     module's own caller does and assert neither is refused (this import is in the TEST only);
   - (vii) a list entry with no `plane` raises in `universe_securities`; a slug entry with an unknown `security_key` raises
     in `universe(config)`.
6. **The offline replay** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~104/az-1.replay.py`, importing
   the REAL `universe`, `slug_queries`, `slug_query` and `_matches` from your worktree. BEFORE = the company's query alone.
   AFTER = the alias set.
   - recall, for bbg and for wsj, over every finished job with an accepted article: print `<pub>: kept <k> of <n>` before
     and after, and every URL still lost after as `LOST <class> <query> <slug>` (classes as in `ay-1.replay.py`);
   - the per-name table over the stored wsj `<loc>` URLs, one line per security of the universe, `<security_key>
     <company>: before <n> after <m>`, then `DENOMINATOR: <names> names, <urls> urls, changed <c>`;
   - print `REPLAY OK` only if ALL hold: wsj kept after == n; bbg kept after >= 3,278 and every URL still lost is class
     `substring_accident`; Meta Platforms after > before; Bank of America after == before; AT&T after == before; `changed`
     is exactly 2 and the two are `META_US_Equity` and `LLY_US_Equity`. Otherwise `REPLAY FAIL` and the failing line.
   - Write its output beside it as `az-1.replay.out`.
   - If the bar is missed, do NOT add an entry, widen a rule or derive a word: report the failing line and the counts.
7. Run `python -m pytest lib/opal_data_harvest -q -p no:cacheprovider` once and report the count (the issuer re-runs it at
   the merge; it is not a criterion here).

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/discovery.py
lib/opal_data_harvest/config.json
lib/opal_data_harvest/build_release.py
lib/opal_data_harvest/test_az1_alias_set.py
lib/opal_data_harvest/test_*.py
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/universe_securities.py
lib/research/harvest/tests/test_alias_rule_round18.py
lib/research/harvest/tests/test_universe_securities.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~104/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-az-1"><invocation>python -m pytest lib/opal_data_harvest/test_az1_alias_set.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-az-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~104/az-1.replay.out</invocation><expect>REPLAY OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-az-1"><invocation>python -m pytest lib/research/harvest/tests/test_alias_rule_round18.py lib/research/harvest/tests/test_universe_securities.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; on this fabric a worker row id reads
  `AMGT_HARVST-Z-W104-S<k>`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~104/AMGT_HARVST.TO-HVST-az-1.alias-set-per-name.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-az-1.alias-set-per-name`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `ledger/ROUND_ANALYSIS.round49.md` ADDENDUM 3 item 2, ADDENDUM 5 @49f385091e, ADDENDUM 6 @c1f0c8a429
  (`1.0.0_SA_CTO~Z` msgs 30738, 30743); research `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_AZ1_BRAND_ALIAS_SOURCES_20261007.md`;
  decomposition section 68; rows AMGT_HARVST-Z-S95 @df63b15a0e and Z-S96 (this commit).
- **Issuer's reading of ADDENDUM 6 item 3 (carrier), stated because it has a consequence:** the brand is appended to the
  security's `aliases` at load, so the collector's acceptance check (`publishers.py` `mentions`, which reads `aliases`)
  also accepts an article whose text carries `Meta` or `Lilly` as a whole word. The gold text matcher is kept apart by the
  `plane` field. This goes to `1.0.0_SA_CTO~Z` in the drain-end message. No gate limb graded this reading.
- **The bar:** bbg kept >= 3,278 of 3,282 (the 2 Eli Lilly slugs recovered; the 4 substring accidents stay lost), wsj
  566 of 566, Meta up, Bank of America and AT&T unchanged, exactly 2 of 234 names changed.
- **Checks dry-run at the base before the cut:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected
  (no such file); AC3 base PASS as expected (40 passed).
- Not in this cell (ADDENDUM 6): the two suffix lists becoming one; the cut or decorated legal names (row Z-S96); any
  further brand entry; a Bloomberg short-name pull.
- The close run is the issuer's: the META and LLY pairs re-run with `--names` on wsj and bbg after the merge.

**COMPLETE 2026-10-07 ~09:5xZ (issuer):**
- **Built:** worker ~104 @3f9bcd5a03 + @bce12586e1; merged @05638ecfd9 (12 paths, index check 0 of 12 differ).
- **AC1 PASS:** 7 of 7. **AC2 PASS:** REPLAY OK -- bbg kept 3,481 of 3,487 before and 3,483 after (4 still lost, all
  `substring_accident`); wsj 640 of 640 before and after; over 26,907 stored wsj URLs Meta Platforms 2 to 118, Eli Lilly 28 to
  33, Bank of America 9 to 9, AT&T 11 to 11; changed 2 of 234 names. The recall denominators are above the face's 3,282 and 566
  because the live legs added run records since round 52; the face's bar (bbg kept >= 3,278) was written against the old
  denominator and is met on the new one with the same 4 lost. **AC3 PASS:** 40 of 40.
- **Issuer drain check on merged CLOUD:** `pytest lib/opal_data_harvest` plus the two research tests: 766 passed, 1 skipped.
- **Call sites:** `_sitemap_items` selects candidates and now passes the alias set; `_bloomberg_sitemap` and
  `_dow_jones_sitemap` only stamp `search_query` and are unchanged.
- **Existing assertions changed** (`lib/research/harvest/tests/test_alias_rule_round18.py`, each because every entry now
  carries a `plane`): the planted KOF, WALMEX and UBS entries gained `plane: text`; the shipped-list test checks the 7 text
  brands among text-plane entries and the 2 slug entries separately; the refusal-count test compares text-plane entries only.
- **Rows:** none from the worker.
- **Close run:** in flight at this close -- the META and LLY pairs re-run on wsj and bbg with `--names` on fresh checkpoints
  `r54_<leg>_az1_checkpoint.json`, each after its leg ends on a stop file, and each leg restarts after. Outputs
  `.runtime/harvest-backfill/r54_<leg>_az1.out`; the read goes into `deliverables/2.0.0_SA_COO_H/round54/`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<status>complete</status>
<round>54</round>
<slot>~104</slot>
<fabric>site-z</fabric>
