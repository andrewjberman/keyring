# AMGT_HARVST task order -- `HVST-bp-1` -- ROUND 71 (`1.0.0_SA_CTO~Z` msg 31679, condition C2 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_HARVST_BO1_QUERY_OVERRIDE_MERGE_20261008.md` @d6ea0eff2f): A MALFORMED QUERY OVERRIDE: WHICH JOBS IT STOPS, SHOWN -- AND THE STORED LISTING LABEL OF AN OVERRIDDEN NAME READS THE QUERY THAT WAS SEARCHED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~123</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants only. NO S3 call, NO job, NO collector, backfill_driver or emitter run, NO vendor, publisher or Bloomberg call. `lib/opal_data_harvest/config.json` and the two round-47 files are NOT changed. A collection leg is LIVE on the shared tree and runs this package: touch nothing outside your worktree; your branch is NOT merged while that leg runs.
comp-adversary: RUN at L5 -- the adversary is a malformed override that is silently skipped, a failure contained by catching every exception, a label fix that changes what is SEARCHED, a query that moves for a security with no override, or a job run to see what happens.
</preflight>

## 0. THE CELL

Your branch is cut from `wk-AMGT_HARVST-122-r70` @419dc9b1fc, which is NOT on CLOUD yet: it carries cell `HVST-bo-1`. Read
what it did before you write: `lib/opal_data_harvest/publishers.py` (`_query_override`, `slug_queries`),
`lib/opal_data_harvest/__main__.py` (`universe()` copies `query_override` from an identity record onto the security),
`lib/opal_data_harvest/test_bo1_query_override.py`, and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~122/bo1_query_table.py` with its output. One record of the new,
unpointed identity file `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/rank_universe_identity_20261008.json` carries the field: `AIG_US_Equity`, an object
`{"value": ["American International Group"], "reason": ..., "source": ...}`.

Two things are owed before the collector is ever pointed at that file:

1. **A malformed override: does it stop one job or the whole run?** `_query_override` raises `ValueError` naming the
   security. Nobody has shown where that exception goes: whether the one security's job ends with a named error and the
   driver carries on to the next security, or the whole process dies, or (worst) `universe()` fails at start and no
   security is collected. Read the path: `__main__.py` `universe()`, the worker's job loop (`lib/opal_data_harvest/worker.py`
   `run_job` and how a job's exception becomes its status), and `lib/opal_data_harvest/backfill_driver.py`.
2. **Row AMGT_HARVST-Z-W122-S1.** In `publishers.py`, `_sitemap_items`, `_bloomberg_sitemap` and `_dow_jones_sitemap` build
   `query = slug_query(security["company"])` and use it as the listing's stored name and provenance (`"sitemap:" + query`,
   `search_query`). For a security with an override the SEARCH uses the override, but the stored label would read the
   derived string ("AMERICAN INTERNATIONAL"), which is not what was searched.

## 1. THE BUILD (LOCAL; on your branch, which is not merged while the live leg runs)

1. **Show it first, by test, on the code as you find it** (`lib/opal_data_harvest/test_bp1_malformed_override.py`, no
   network, using the fixtures and fakes the package's existing tests use): a universe of three securities where the
   SECOND carries a malformed `query_override`. Print and assert what happens today: at which call the `ValueError`
   surfaces, what the first and third securities' jobs do, and what the second's recorded status is. Write the finding as
   one plain paragraph in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~123/BP1_MALFORMED_OVERRIDE.md`: "today a malformed override stops <one job | the run at
   start | the run at that job>", with the function names.
2. **Then make it stop exactly one job.** If today's behaviour is anything other than "the one security's job ends with a
   status that names the cause, and every other security is collected as before", change the smallest place so that it
   is: the malformed security's job is recorded with a status that says its query override is malformed and carries the
   validator's message; no query is derived as a fallback (a malformed override never silently becomes the derived
   query); the other securities' jobs are untouched. Do NOT wrap a broad `except Exception`: catch the validator's own
   error where the override is first read. If today's behaviour is already that, change nothing and say so.
3. **The label.** One small helper returns the string a security's listing is named by: for a security with an override,
   its override queries joined in a fixed, stated way; otherwise `slug_query(security["company"])`, byte-for-byte what is
   stored today. The three helpers use it for the label and provenance ONLY. What is searched does not change:
   `slug_queries` stays the one writer of the queries.
4. **Plants** in the same test file: (i) the malformed case of item 1 after your change: jobs 1 and 3 run, job 2 carries
   the named status; (ii) THE NEGATIVE CONTROL: with a well-formed override on job 2, all three run and job 2 searches the
   override; (iii) a security with no override gets the label `slug_query(company)` exactly, for every record of the
   round-47 identity file (assert over all 234); (iv) `AIG_US_Equity` from the new identity file gets a label containing
   "American International Group" and not equal to "AMERICAN INTERNATIONAL"; (v) the mutant: with your containment
   removed, (i) fails the way item 1 recorded.
5. **The table re-read.** Run `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~122/bo1_query_table.py` unchanged and confirm its last line is still `TABLE OK` with
   `CHANGED 1`, `IDENTICAL 241` and `ROUND-47 FILE: CHANGED 0 of 234`; copy its output to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~123/bp1_query_table_rerun.out`. (It reads frozen titles beside itself; it makes no S3 call.)
6. Do not change `_LEGAL_SUFFIX`, `slug_query`, `discovery._matches`, `config.json`, the round-47 files, or the identity
   files. Run no job.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/opal_data_harvest/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~122/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_identity_20261005.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~123/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bp-1"><invocation>python -m pytest lib/opal_data_harvest/test_bp1_malformed_override.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bp-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~123/bp1_query_table_rerun.out</invocation><expect>TABLE OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bp-1"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W123-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~123/AMGT_HARVST.TO-HVST-bp-1.a-malformed-override-and-the-stored-label.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bp-1.a-malformed-override-and-the-stored-label`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31679, condition C2 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_HARVST_BO1_QUERY_OVERRIDE_MERGE_20261008.md` @d6ea0eff2f. Decomposition section 85.
- CTO half C2: "before the pointer ever moves: show whether a malformed override stops one job or the whole run; repair row
  Z-W122-S1; and the first worded run's AIG result is read by hand." The third item is an act after Andrew's word, not a cell.
- **Issuer rulings inside the decomposition** (no gate limb graded them): a malformed override stops exactly one job and never
  falls back to the derived query; the label helper changes what is STORED as the listing's name for an overridden security
  and nothing that is searched.
- **Stacked on `bo-1`'s unmerged branch.** The signed pair for `bo-1`'s merge names branch head 419dc9b1fc. This cell's commits
  sit on top and are NOT covered by that pair: either `bo-1` is merged at 419dc9b1fc and this branch follows under its own
  pair, or one new pair covers both. `1.0.0_SA_CTO~Z` is asked which when this cell reports.
- <risk> SERVED. Chain of one, slot ~123, worktree cut from `wk-AMGT_HARVST-122-r70`. **Checks dry-run at the base (that
  branch):** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected (no such file); AC3 base PASS as
  expected (778 passed, 3 skipped, the bo-1 worker's run on that head).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>71</round>
<slot>~123</slot>
<fabric>site-z</fabric>
