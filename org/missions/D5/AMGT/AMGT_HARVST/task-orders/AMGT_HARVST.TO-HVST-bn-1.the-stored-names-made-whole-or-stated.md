# AMGT_HARVST task order -- `HVST-bn-1` -- ROUND 69 (`1.0.0_SA_CTO~Z` msg 31649 (R22)): AIG'S STORED NAME BECOMES ITS FULL LEGAL NAME WITH A QUERY SHOWN TO MATCH, AND THE THREE NAMES LEFT CUT ARE REPAIRED OR EACH SAID WHY NOT -- FROM STORED SOURCES ONLY, NO POINTER MOVE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bn-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~121</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL files and scripts, plus READ-ONLY reads (S3 GET of the pool universe, the crosswalk object and the silver article parts through the served iterator). NO put, NO delete, NO job, NO collector, backfill_driver or emitter run, NO vendor, publisher or Bloomberg call. `lib/opal_data_harvest/config.json` and the two round-47 files are NOT changed: one collection leg is LIVE and reads them. `.runtime` is not read.
comp-adversary: RUN at L5 -- the adversary is a legal name typed from memory, a name completed by guessing, a query "shown to match" by a test that would pass on any string, a collector code change made to get a query, or a job run to see what the query returns.
</preflight>

## 0. THE CELL

Two NEW dated files carry the collector's universe and search identities with 8 added securities and 2 repaired names:
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/rank_universe_20261008.json` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/rank_universe_identity_20261008.json` (242 records), built by
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/bm1_three_universes.py` and then edited by `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/bm2_truncated_names.py`. They are NOT pointed at:
`lib/opal_data_harvest/config.json` still names the two round-47 files, and that pointer does not move in this cell.

Two things are wrong with the new identity file and are repaired before anyone is asked for a run:

1. **AIG.** The stored name was "American International Group I" (cut at 30 characters). `bm-2` dropped the fragment, so the
   record reads "American International Group", and the query the collector derives from it
   (`lib/opal_data_harvest/publishers.py` `slug_query`, `slug_queries`) is "American International": WORSE than before,
   because it can return other companies. The ruling: the stored name becomes the FULL LEGAL NAME, and the query the
   collector derives is shown to match.
2. **Three names left cut:** `ICT_US_Equity` "International Container Termin", and `OMAB_US_Equity` and `OMAB_MM_Equity`
   "Grupo Aeroportuario del Centro". The ruling: repair them, or state why each cannot be.

Also open (row AMGT_HARVST-Z-W120-S3): re-running `bm1_three_universes.py` rebuilds the identity file and silently reverts
`bm-2`'s repairs. This cell ends that: ONE script yields the final files.

## 1. THE BUILD (LOCAL; nothing fetched from a publisher or vendor)

1. **Where a full name may come from, in this order, each named in the record's evidence:** the pool record's name for that
   exact key; `lib/research/identity/registrations.json` `identity.name`; the crosswalk record
   (`lib/research/identity/crosswalk.py`); the collector's own older identity file `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/rank_universe_identity_20260916.json`;
   and, LAST, the company's own name as written in held article text (silver, through
   `lib/research/harvest/publication_gold.py` `_iter_latest_articles()`): a span that begins with the cut value and runs
   on to a corporate suffix or the end of the name, the SAME completion in at least three distinct articles, with the
   three article keys in the evidence and the words `evidenced by article spans only`. A registry name that is itself cut
   shorter than the stored value is not a source. Nothing is typed from memory.
2. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~121/bn1_names_made_whole.py` prints, for AIG and for each of the three cut names: every source tried, what it holds
   for that key (or `ABSENT`), the completions found in article text with their counts, and ONE verdict line:
   `<security_key>: REPAIRED to "<name>" -- source <...>` or `<security_key>: NOT REPAIRED -- <why: no stored source carries
   it; completions found <list with counts> do not agree | none found>`. For `ICT_US_Equity` also state what is already
   ruled: whether it and `ICT_PM_Equity` are one issuer is not shown by any field and is not inferred, so a name read for
   the Manila listing is not a source for the US key.
3. **The query shown to match.** For each repaired name print what `publishers.slug_query` and `slug_queries` return for the
   new stored string (called locally), and `QUERY MATCHES: <n> of <m> held article titles that carry the full name contain
   every query word` beside `OTHER COMPANIES' TITLES CONTAINING EVERY QUERY WORD: <k>` over the silver titles, with five
   examples of each. If the query the collector derives from the full legal name is STILL not specific (k is large, or the
   query drops the word that makes it the company's), do NOT change `lib/opal_data_harvest` code: say so in the output,
   and state which stored field of the record, if any, lets the record carry a better search form under the builder's own
   rules (the identity file's `rules` field). A collector code change is a different cell.
4. **One script, final files.** Your script (or a small driver it calls) builds `rank_universe_20261008.json` and
   `rank_universe_identity_20261008.json` in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/` from the round-47 files in ONE run: the 8 added records, `bm-2`'s
   KCDMY repair, and this cell's repairs. Running it twice gives byte-identical files. `bm1_three_universes.py` and
   `bm2_truncated_names.py` are left as the record of how the files were first made; each gains a first line of comment
   saying the final files are built by your script. Print `RECORDS CHANGED AGAINST ROUND 47: <c>` with each key, and
   `RECORDS ADDED: 8`.
5. **Plants** `lib/opal_data_harvest/test_bn1_names_made_whole.py` (no network): (i) the new file's `AIG_US_Equity` company is
   the full legal name you found and is longer than 30 characters or ends in a whole corporate suffix; (ii) the query
   derived from it contains the word that the query "American International" lacked, OR the test asserts the stated
   limit of item 3 with the exact strings; (iii) THE NEGATIVE CONTROL: the round-47 file still holds the 30-character cut
   string and config.json still names the round-47 files; (iv) each of the three cut names is either changed with a
   non-empty evidence source, or unchanged and listed in the output's NOT REPAIRED lines (read the output file);
   (v) running the builder twice gives equal bytes; (vi) every record other than those printed as changed equals round
   47's. Update `test_bm1_identity_records.py` and `test_bm2_truncated_names.py` only where this cell's rule is the reason.
6. Last line: `NAMES OK` only if AIG is REPAIRED with a named source, each of the three cut names has a verdict line, the
   two builds are byte-identical, and config.json and the round-47 files are unchanged (compare them with `git show HEAD:`
   of each). Otherwise `NAMES FAIL` and the failing line. Write the output as `bn1_names_made_whole.out`.
7. If no stored source and no three agreeing article spans give AIG's full legal name: do NOT type one. Print `NAMES FAIL`,
   show what was found, and report that. Run no job.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/opal_data_harvest/
lib/research/identity/
lib/research/harvest/publication_gold.py
lib/research/harvest/universe_securities.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~121/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bn-1"><invocation>python -m pytest lib/opal_data_harvest/test_bn1_names_made_whole.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bn-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~121/bn1_names_made_whole.out</invocation><expect>NAMES OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bn-1"><invocation>python -m pytest lib/opal_data_harvest/test_bm1_identity_records.py lib/opal_data_harvest/test_bm2_truncated_names.py lib/opal_data_harvest/test_bf1_job_record.py lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W121-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~121/AMGT_HARVST.TO-HVST-bn-1.the-stored-names-made-whole-or-stated.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bn-1.the-stored-names-made-whole-or-stated`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31649 (R22). Decomposition section 83.
- R22: "The pointer does not move now ... the move rides the same word as the runs. Two repairs before that word is asked, neither
  a fetch. First, AIG: a query of 'American International' is worse than the truncated one, since it can return other
  companies; the stored name becomes the full legal name and the printed query is shown to match. Second, the three names cut
  and not repaired (ICT_US, both OMAB lines): repair them or state why each cannot be. One ask: one cell for both."
- **Issuer rulings inside the decomposition** (no gate limb graded them): a full name comes from a stored source in a fixed
  order, and held article text is the last source, on three agreeing articles, marked "evidenced by article spans only" (the
  form R10 fixed for a symbol anchor); a query that stays unspecific is REPORTED, not fixed by changing collector code that a
  live leg runs; one script yields the final files, which answers row Z-W120-S3; `deliverables/0.9.0_WK_AMGT_HARVST~120/` is
  in `<paths>` to be WRITTEN, because the two final files live there.
- Chain of one, slot ~121. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as
  expected (no such file); AC3 base PASS as expected (count in the issuance commit).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>69</round>
<slot>~121</slot>
<fabric>site-z</fabric>
