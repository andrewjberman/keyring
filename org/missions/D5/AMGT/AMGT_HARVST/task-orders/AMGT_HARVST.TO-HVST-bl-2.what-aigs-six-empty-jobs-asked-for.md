# AMGT_HARVST task order -- `HVST-bl-2` -- ROUND 67 (`1.0.0_SA_CTO~Z` msg 31631 (R18), on `3.0.0_SA_CVO~Z`'s grade of `bk-1` @e84dcdce42): WHAT AIG'S SIX EMPTY JOBS ASKED FOR -- THE REQUEST EACH SENT, READ FROM ITS RUN RECORD, BESIDE WHAT NOKIA'S PRODUCTIVE JOBS SENT; NO JOB IS RUN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bl-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~119</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL script and records, plus READ-ONLY reads: S3 GET of the collector's uploaded run records and of the newest gold part, and a read of run-record files under the shared tree's `.runtime`. NO put, NO delete, NO job of any kind, NO collector, backfill_driver or emitter run, NO vendor or publisher host. One collection leg is LIVE and writes under that `.runtime`: open its files read-only, copy nothing back, touch nothing else outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a set printed without both denominators, a zero read from one store taken as a zero in the other, a job run to see what it returns, or a cause asserted where only a request was read.
</preflight>

## 0. THE CELL

You are the second order of this slot's queue: `HVST-bl-1` is built on your branch and its script shows how both run-record
stores are read.

`AIG_US_Equity` was collected six times and nothing came back: `contract_unavailable`, `no_new_articles` (WSJ, Bloomberg),
`upstream_unavailable`, `no_acceptable_new_articles` twice (`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND66_BK1_COLLECTION_GAP_GRADE_20261008.md` @e84dcdce42). Bloomberg and WSJ holding no AIG
article is not believable as the world. One GUESS, not measured: AIG's company name in the collector's identity record is cut
at 30 characters ("American International Group I"), and a job that searches on that cut string would find nothing.
`NOKIA_FH_Equity` is the control: four jobs, three of them `new_articles`.

Read how a job builds its request before you read the records: `lib/opal_data_harvest/publishers.py` (the queries a
publisher is asked: `slug_query`, `slug_queries`, the search terms), `lib/opal_data_harvest/discovery.py`, and the job and
run-record writers in `lib/opal_data_harvest/worker.py`.

## 1. THE BUILD (read-only; NO job, NO collector run)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/bl2_aig_requests.py` reads the run records of every job for `AIG_US_Equity` and for `NOKIA_FH_Equity` from both
   stores (the S3 run records and the shared tree's `.runtime` run-record and per-job files; read-only).
2. Per job, ONE block: run id, job id, source, started and finished, status, `attempt_class` and `signature` if present,
   keys fetched, keys stored, `reached_span`, and THE REQUEST: every search term, slug, symbol or query string the record
   holds for that job, the date window it asked for, and each entry of `request_attempts` (URL or endpoint with the query
   string, HTTP status, outcome), 400 characters at most per entry. Where the record does not hold a field, print
   `NOT IN THE RECORD` for it; do not reconstruct it.
3. Then `THE IDENTITY EACH JOB WAS GIVEN`: for both securities, the collector's identity record entry (the path in
   `lib/opal_data_harvest/config.json` `symbol_resolution_source`): `company.value`, `aliases`, `ticker`, `sa_symbol`, and
   what `publishers.slug_query(company)` (or the function the code uses today) returns for it. Call that function locally on
   the string; it makes no network call. State plainly whether the string AIG's jobs searched on is the cut name.
4. A side-by-side table in `BL2_AIG_REQUESTS.md`: one row per job, AIG's first, then Nokia's: source, status, the search
   term or slug sent, the date window, attempts, stored.
5. One section `WHAT THE RECORDS SHOW, AND WHAT THEY DO NOT`: per AIG job, whether the record shows the request was SENT and
   answered with nothing, was REFUSED, or was never sent; and which of those the record cannot tell apart. No cause is
   asserted beyond what a field shows.
6. Last line: `RECORD OK` only if at least one job was read for each of the two securities and every job printed its
   block. Otherwise `RECORD FAIL` and the failing condition. Write the output as `bl2_aig_requests.out`.
7. Change no product file. Run no job to see what it returns: that is a call on a publisher.

<paths>
lib/opal_data_harvest/
lib/research/harvest/publication_gold.py
lib/research/harvest/store.py
org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND66_BK1_COLLECTION_GAP_GRADE_20261008.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_identity_20261005.json
.runtime/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bl-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/bl2_aig_requests.out</invocation><expect>RECORD OK</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W119-S2`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/AMGT_HARVST.TO-HVST-bl-2.what-aigs-six-empty-jobs-asked-for.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bl-2.what-aigs-six-empty-jobs-asked-for`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31631 (R18), on `3.0.0_SA_CVO~Z`'s grade of `bk-1` @e84dcdce42. Decomposition section 81.
- R18: "Cell two: AIG's six empty jobs, the request each sent (search term, source, date window) read from its run record, with
  what Nokia's three productive jobs sent beside it. Neither cell runs a job. Running a backfill for an uncollected name is a
  call on a publisher; it waits on `4.0.0_SA_CRO~Z`'s answer."
- Slot ~119's queue, second. **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

**WITHDRAWN 2026-10-08 ~09:0xZ (issuer), never spawned:** `1.0.0_SA_CTO~Z` msg 31637 (R20) replaced the two read cells of
msg 31631 with (a) the three universes reconciled and the missing identity records and (b) AIG's truncated stored name
repaired; those are `HVST-bm-1` and `HVST-bm-2` (round 68). `bm-2` item 3 prints the query the collector derives from AIG's
stored name, old and repaired. `HVST-bl-1` was already executing and is left to finish as the read behind (a).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>withdrawn</status>
<round>67</round>
<slot>~119</slot>
<fabric>site-z</fabric>
