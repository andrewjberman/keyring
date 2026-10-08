# AMGT_HARVST task order -- `HVST-bj-1` -- ROUND 65 (`1.0.0_SA_CTO~Z` msg 31575, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 2 @e93cccc7be, enrichment item 3): THE FIRST WALK OF THE SECURITY ANALYSIS FEED ON REBUILT GOLD -- TWELVE SECURITIES THROUGH THE PAGE'S OWN FEED READER, IN CONTEXT, NO GRADE BY YOU

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~115</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL script and records, plus READ-ONLY reads the page's own feed reader makes (S3 GET of the newest gold part, and whatever read its identity resolution makes). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector. `.runtime` is not read. One collection leg is LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a walk that reads the gold table directly and calls it the feed, a feed read that failed printed as an empty feed, a packet the script grades, or a served part other than the newest.
</preflight>

## 0. THE CELL

The served gold was rebuilt on 2026-10-08 (rebuild #9; record `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/gold_rebuild9.act_20261008T052038Z.json`): the newest
parts are `amgt/harvest/gold/article_security_mention/date=2026-10-08/part-20261008T055319Z.parquet` (48,358 rows) and
`amgt/harvest/gold/chatter_daily/date=2026-10-08/part-20261008T061255Z.parquet`. Its rule held and its counts were read.
Nobody has yet looked at what a reader of the Security Analysis page is shown.

The page's header feed is `lib/research/api/scoped_amgt.py` `read_feed(security_key, identity=None, as_of_date=None)`: the
newest harvested articles that name the security, read from gold `article_security_mention` through the page's own seam.
Read its docstring and the two tests `lib/research/api/tests/test_feed_and_names_an3.py` and `test_feed_url.py` first, to
see how it is called and what `coverage_status` values it returns.

Twenty-one pairs were removed by name in the rebuild; their keys are in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/REBUILD9_NAMED_REMOVALS.json` (`rows`).

## 1. THE BUILD (read-only)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~115/bj1_feed_walk.py` calls the REAL `scoped_amgt.read_feed(<key>)` (no fixture, no patch, `as_of_date` left to today)
   for these twelve securities, in this order: `CAT_US_Equity`, `CSL_AU_Equity`, `HEI_US_Equity`, `BP_US_Equity`,
   `SAP_GY_Equity`, `ASML_US_Equity`, `AIG_US_Equity`, `NOKIA_FH_Equity`, `GSK_LN_Equity`, `ICT_US_Equity`, `META_US_Equity`,
   `LLY_US_Equity`.
2. It prints `SERVED PART READ: <the article_security_mention part key the seam read, or how you established it>` and
   `DENOMINATOR: securities 12`, then per security ONE line:
   `<security_key>: coverage_status <s>, items <n>, window <start> to <end>, identity <status>` and, when the status is not
   a successful read, the `reason` in full.
3. It joins each feed item to its gold mention row (the same snapshot) for `match_forms` and `mention_count`.
4. It writes `BJ1_FEED_WALK.md` and `.json` beside it: per security, the header line, then the NEWEST 15 items (all when
   fewer): published date, publisher, title, url or `url_reason`, `match_forms`, `mention_count`. The md opens with one
   paragraph: what was called, which served part it read, and that the question per security is "does this feed read as
   coverage of this company". It carries NO verdict and NO grade: a reviewer grades it.
5. It prints `NAMED REMOVALS STILL IN A WALKED FEED: <k> of <m>` where m counts the named removals whose security is one of
   the twelve (BP, SAP, CSL, HEI), over ALL items of those feeds and not only the newest 15, with each key still present.
6. Last line: `WALK OK` only if all twelve were read with a status that is not a failed read (a security whose identity is
   unresolved is printed and counts as NOT read), the part read is the 2026-10-08 part above, and NAMED REMOVALS STILL IN A
   WALKED FEED is 0. Otherwise `WALK FAIL` and the failing condition. Write the whole output as `bj1_feed_walk.out`.
7. A failed or refused read is a FINDING: print it whole, file a row, and do not substitute a direct read of the gold
   table for the feed. Change no product file. Call no vendor.

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_feed_and_names_an3.py
lib/research/api/tests/test_feed_url.py
lib/research/harvest/publication_gold.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/REBUILD9_NAMED_REMOVALS.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/gold_rebuild9.act_20261008T052038Z.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~115/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bj-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~115/bj1_feed_walk.out</invocation><expect>WALK OK</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bj-1" judgment="true"/>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W115-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~115/AMGT_HARVST.TO-HVST-bj-1.first-walk-of-the-feed-on-rebuilt-gold.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bj-1.first-walk-of-the-feed-on-rebuilt-gold`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31575, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 2 @e93cccc7be, enrichment item 3. Decomposition section 79.
- ADDENDUM 2, enrichment list: "then the first walk of the Security Analysis feed on rebuilt gold". The round-60 analysis,
  section 2 item 4: "How the page reads with 14,400 more pairs. No walk of the Security Analysis feed has been made on the
  rebuilt gold." AC2 is `3.0.0_SA_CVO~Z`'s read of the packet.
- **Issuer rulings inside the decomposition** (no gate limb graded them): the walk goes through the page's own feed reader,
  not the gold table; the twelve are the securities rebuilds #8 and #9 moved most (names from the registry, the second
  anchor, the fallback, the fragment cut, issuer grouping, the two gold brands) plus ICT's 0-pair security.
- The page is AMGT_RESAPP's; this cell reads through its reader and changes nothing of it. What the walk finds about the
  page itself goes to `2.0.0_SA_COO~Z` as a row on that project's channel, by the issuer.
- Chain of one, slot ~115. **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

**COMPLETE 2026-10-08 ~07:1xZ (issuer):**
- **Built:** worker-light ~115 @ce34c1022d; merged @1b6fb24119 (5 paths, index check 0 of 5 differ). No product file changed.
- **AC1 PASS:** WALK OK. 12 of 12 securities read through `scoped_amgt.read_feed` on the 2026-10-08 part (48,358 rows), window
  2026-09-09 to 2026-10-08. SERVED 8: Meta 135 items, BP (US) 17, Lilly 15, ASML (US) 12, GSK (LN) 9, Nokia 7, HEI 2, SAP 2.
  NONE_IN_WINDOW 3: CAT, CSL, AIG. NEVER_HELD 1: `ICT_US_Equity`. Named removals still in a walked feed: 0 of 21.
- **The three empty feeds, read by the issuer from the served part:** the security has pairs but none published inside the
  30-day window -- CAT 85 pairs, newest 2026-09-08 (one day outside); CSL 39, newest 2026-07-17; AIG 16, newest 2026-08-02.
  Not a failed read. Whether a page should say so differently is AMGT_RESAPP's.
- **AC2 (judgment) OWED by `3.0.0_SA_CVO~Z`:** `deliverables/0.9.0_WK_AMGT_HARVST~115/BJ1_FEED_WALK.md`.
- **Rows:** none.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<status>complete</status>
<round>65</round>
<slot>~115</slot>
<fabric>site-z</fabric>
