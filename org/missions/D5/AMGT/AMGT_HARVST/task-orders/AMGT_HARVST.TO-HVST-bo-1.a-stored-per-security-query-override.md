# AMGT_HARVST task order -- `HVST-bo-1` -- ROUND 70 (`1.0.0_SA_CTO~Z` msg 31664 (R23)): A STORED PER-SECURITY QUERY OVERRIDE THE COLLECTOR USES WHEN PRESENT -- SET FOR `AIG_US_Equity` ONLY; THE DERIVED QUERY OF ALL 242 NAMES PRINTED BEFORE AND AFTER, 1 CHANGED AND 241 IDENTICAL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bo-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~122</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, data and plants, plus READ-ONLY reads (S3 GET of the silver article parts through the served iterator, for titles). NO put, NO delete, NO job, NO collector, backfill_driver or emitter run, NO vendor, publisher or Bloomberg call. `lib/opal_data_harvest/config.json` and the two round-47 files are NOT changed. A collection leg is LIVE on the shared tree and runs this package: touch nothing outside your worktree; your branch is NOT merged while that leg runs.
comp-adversary: RUN at L5 -- the adversary is `_LEGAL_SUFFIX` changed, a query that moves for any name but the one named, an override that the round-47 files could trigger, a table printed over fewer than 242 names, or a job run to see what the new query returns.
</preflight>

## 0. THE CELL

The collector derives the words it searches a publisher's listing for from a security's stored name:
`lib/opal_data_harvest/publishers.py` `slug_query(company)` drops trailing legal-suffix words (`_LEGAL_SUFFIX`), and
`slug_queries(security)` returns the distinct `slug_query` of the company and of each alias; a listing entry is a candidate
when it matches ANY ONE of them (`lib/opal_data_harvest/discovery.py`). Read both, and how the identity record reaches a
job (`lib/opal_data_harvest/__main__.py`, the loader of `symbol_resolution_source`).

`AIG_US_Equity`'s stored name in the new, unpointed identity file `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/rank_universe_identity_20261008.json` is
"AMERICAN INTERNATIONAL GROUP, INC." (built by `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~121/bn1_names_made_whole.py`; read it: ONE script builds that file).
`slug_query` strips "group" and "inc", so the collector would ask for "AMERICAN INTERNATIONAL", which also matches other
companies' headlines: two held titles are American Airlines stories ("American plans to cut some international flights while
it waits on Dreamliner order"; "American Airlines cuts more international routes on Dreamliner delays - WSJ").

The ruling, and its bounds: **a stored per-security query override the collector uses when present, set for
`AIG_US_Equity` ONLY. `publishers._LEGAL_SUFFIX` is NOT changed:** that rule derives the query of every name, and a change
there moves what already-authorized runs ask for names nobody has looked at.

## 1. THE BUILD (LOCAL; on your branch, which is not merged while the live leg runs)

1. **The override, as data.** An identity record may carry an optional field (name it `query_override`): a non-empty list of
   query strings with a `reason` and a `source`. When a security's record carries it, `slug_queries` returns exactly those
   strings and nothing derived from the company or the aliases. When it is absent, `slug_queries` returns exactly what it
   returns today. An empty or malformed override raises with the security named; it is never silently ignored.
2. **Set for AIG only**, through the ONE builder (`bn1_names_made_whole.py` or a successor you write beside your own
   script, so one run still yields the final files byte-identically): `AIG_US_Equity` gets the override
   `["American International Group"]`, reason and source stated (this ruling; the record's own full legal name). No other
   record gains the field. The round-47 files and `config.json` are not changed, so the live leg's inputs cannot carry it.
3. **Nothing else in the collector changes:** not `_LEGAL_SUFFIX`, not `slug_query`, not `discovery._matches`, not the
   matcher of bodies. If the override cannot reach `slug_queries` without touching one of those, STOP and say why.
4. **The table** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~122/bo1_query_table.py`: for ALL 242 records of the new identity file, the queries BEFORE (the function at
   your base commit, loaded from `git show <base>:lib/opal_data_harvest/publishers.py` or by passing the record with the
   field removed, stated in the file) and AFTER. Print `DENOMINATOR: records 242`, `CHANGED: <c>` with each changed key and
   both query lists, `IDENTICAL: <i>`, and write every row to `BO1_QUERY_TABLE.md` and `.json`. Then the same comparison
   over the 234 records of the round-47 identity file: `ROUND-47 FILE: CHANGED <c47> of 234` (must be 0).
5. **AIG's new query against held titles** (silver, `lib/research/harvest/publication_gold.py` `_iter_latest_articles()`,
   titles only): `TITLES MATCHING THE OLD QUERY "AMERICAN INTERNATIONAL": <n>` with each; `TITLES MATCHING THE NEW QUERY: <m>`
   with each; `THE TWO AMERICAN AIRLINES TITLES: <excluded|still matched>`, matched the way `discovery._matches` matches a
   listing entry (call it; do not re-implement it).
6. **Plants** `lib/opal_data_harvest/test_bo1_query_override.py` (no network): (i) a record with the override returns exactly
   the override strings; (ii) THE NEGATIVE CONTROL: the same record without the field returns today's derived queries;
   (iii) an empty list, a non-list and an empty string each raise naming the security; (iv) the two American Airlines
   titles above do not match AIG's override query and do match the old one (through `discovery._matches`); (v) from the
   real new identity file, exactly one record carries the field and it is `AIG_US_Equity`; (vi) from the real round-47
   identity file, no record carries it; (vii) the mutant: with the override ignored, (iv)'s titles match again.
7. Last line: `TABLE OK` only if the 242-record comparison reads CHANGED 1 (`AIG_US_Equity`) and IDENTICAL 241, the round-47
   comparison reads CHANGED 0, the two titles read `excluded`, and `config.json` and the round-47 files equal `git show HEAD:`
   of each. Otherwise `TABLE FAIL` and the failing line. Write the output as `bo1_query_table.out`.
8. Run no job. Whether the new query finds AIG's articles at a publisher is not measured by this cell and cannot be without
   a run.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/opal_data_harvest/
lib/research/harvest/publication_gold.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~121/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~122/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bo-1"><invocation>python -m pytest lib/opal_data_harvest/test_bo1_query_override.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bo-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~122/bo1_query_table.out</invocation><expect>TABLE OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bo-1"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W122-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~122/AMGT_HARVST.TO-HVST-bo-1.a-stored-per-security-query-override.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bo-1.a-stored-per-security-query-override`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31664 (R23). Decomposition section 84.
- R23: "Cut it now, on a branch. The shape is narrow: a stored per-security query override the collector uses when present, set
  for AIG_US_Equity only. Do not change publishers._LEGAL_SUFFIX ... The proof is a printed table of the derived query for all
  242 names before and after, reading 1 changed and 241 identical, with AIG's new query shown to exclude the two American
  Airlines titles. The merge is held on two things: the live Seeking Alpha leg ending, and a pair, because on this box a merge
  into lib/opal_data_harvest is a deploy to whatever the driver runs next."
- **Issuer ruling inside the decomposition** (no gate limb graded it): the override REPLACES the derived queries for its
  security and does not join them, since the queries are OR-ed and a joined override could only widen.
- **<risk> is SERVED**, and this order does NOT close at the worker's report: the branch is HELD UNMERGED until (1) the live
  Seeking Alpha leg has ended and (2) a never-widen pair is signed for the merge; the issuer brings the COO half with this
  cell's table.
- Chain of one, slot ~122. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as
  expected (no such file); AC3 base PASS as expected (count in the issuance commit).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>70</round>
<slot>~122</slot>
<fabric>site-z</fabric>
