# AMGT_HARVST task order -- `HVST-r-5` -- ROUND 2: settle the CODE half of "four of five publishers produced no listing page" -- an offline, stub-driven reachability census per publisher, denominator printed, poison named; NO vendor call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-r-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~15</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); this cell writes nothing anywhere and arms nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every store touch is a stub.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~15`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~15;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER OR AWS. NEVER RUN THE HARVESTER's `run` OR `upload-*`.** Every response
  in this cell is a stub you write.

## 1. THE CELL, inlined in full -- `HVST-r-5` (manifest row H1, outcome FWD-1)

**THE FACT THIS CELL ANSWERS HALF OF.** `FWD-1`'s bar is every article **AND the listing page that found it**. The issuer's
census of `{source}/harvest/bronze/news_listing/` after the live act: **wsj 2, seeking-alpha 0, bloomberg 0, ft 0,
barrons 0.** One of five publishers has a listing page at all.

**TWO CAUSES ARE POSSIBLE AND THEY HAVE DIFFERENT OWNERS:**
- **CODE:** the listing capture is not wired on those four paths, so it would never have produced a page even on a healthy
  session.
- **SESSIONS:** those paths never reached a listing call in the one authorised run (the bbg probe took a challenge, bbg's
  job took another, wsj and barrons re-authenticated, sa hit an HTTP 502).

**THIS CELL SETTLES THE CODE HALF ONLY, AND OFFLINE.** Whatever it proves wired, the remaining cause is the sessions,
which is a HOLD owned by Andrew through `1.0.0_SA_CTO~Z` (decomposition section 11) and **NOT a cell**. A fourth vendor act
is **not granted**, and nothing in this cell asks for one.

**RULED -- what you build:**
1. **A census at `lib/opal_data_harvest/census_listing_capture.py`**, offline, which for EACH of the five publisher paths:
   - drives that path's discovery with a STUB response carrying a small, publisher-shaped listing payload;
   - asserts whether a listing record is produced on `Publisher.listings` (the capture `HVST-h-1` built);
   - asserts whether that record would be PUT, by calling the bronze listing writer with a STUB S3 client and reading the
     key it would use;
   - prints, PER PUBLISHER: `publisher <code> listing_captured <bool> would_put <bool> key <shape> reason <text>`;
   - prints the DENOMINATOR: `paths_examined 5 of 5`, and `wired <n> of 5`.
2. **THE POISON, NAMED, because a no-network PASS with no poison proven is an ABSENCE** (`3.0.0_SA_CVO~Z`'s bar, adopted
   by the CTO @`f869aa705c`): poison `PacedSession.get`, `SessionManager.refresh` and `subprocess.run` so any real call
   RAISES, and print a POSITIVE CONTROL showing each raises when deliberately tripped. Print `vendor_calls 0` from a
   counter, never as a literal.
3. **A VERDICT that separates the two causes** and does not blur them:
   `listing_capture_wired <n> of 5` and, for every publisher that is wired but produced nothing live,
   `live_cause SESSIONS (see RUN_REPORT)`; for any publisher NOT wired, `live_cause CODE` with the missing step named.
4. **Arms in `lib/opal_data_harvest/test_listing_capture_census.py`** proving the census itself discriminates: an arm where
   a path IS wired reports True, and a NEGATIVE CONTROL arm where the capture is deliberately removed reports False. **A
   census that cannot report False proves nothing.**

**What this cell does NOT do:** it fixes nothing. If a path is unwired, that is a finding, a row and a round-3 candidate,
not a repair in this cell. It writes no S3 object and makes no vendor call.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v1.1 @04a235adb7 section 10a, cell 5 of 5. Independent of the other four. Its output decides whether
the listing half of `FWD-1` is owned by a session hold or by a code cell in round 3.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/census_listing_capture.py
lib/opal_data_harvest/test_listing_capture_census.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/rehearse_run.py
lib/research/harvest/store.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~15/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-r-5.listing-capture-reachability-census.md
</paths>

- **Only `census_listing_capture.py` and `test_listing_capture_census.py` may CHANGE.** Every other lib file is
  READ-ONLY -- read `publishers.py` for the five discovery paths, `rehearse_run.py` for the poison pattern already proven
  in this project, and `harvest_grammar.py` for the listing writer. AC3 fails if any of them changes.
- `~10`'s deliverables are read for `RUN_REPORT.md`'s per-publisher outcomes.
- Scratch goes in `<your worktree>/.scratch/r5/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~15 <0.9.0_WK_AMGT_HARVST~15@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **OFFLINE ONLY. Pure ASCII.** No S3 write, no vendor call, no fix.
- **A publisher you cannot drive with a stub is reported UNKNOWN with its reason, never assumed wired.**
- **Surprise rows:** `AMGT_HARVST-Z-W15-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-r-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_listing_capture_census.py -v --color=no -p no:cacheprovider 2>&1 | tail -14</invocation><expect>every arm passes and no "failed" -- including the NEGATIVE CONTROL arm where the capture is deliberately removed and the census reports listing_captured False for that path</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-r-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest.census_listing_capture</invocation><expect>five publisher lines each carrying listing_captured, would_put, key and reason; "paths_examined 5 of 5"; "wired n of 5"; "vendor_calls 0" from a counter; a per-publisher live_cause of SESSIONS or CODE; and the poison's POSITIVE CONTROL showing all three sites RAISE when tripped</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-r-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r5/ac3.py</invocation><expect>"outside_allowed []" -- only census_listing_capture.py and test_listing_capture_census.py changed, nothing else under lib; each prints "compiles True crlf 0 non_ascii 0"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-r-5"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_retrieval_provenance test_bronze_capture test_silver_from_bronze; do echo "$t :: $(python -m pytest lib/opal_data_harvest/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>18 passed, 12 passed and 16 passed -- the round-1 suites this cell reads are untouched by it</expect></criterion>
</proof_of_spec>

Write `.scratch/r5/ac3.py`: the allowed-set diff from `git merge-base HEAD SITEZ` over `lib`, plus a compile, CRLF and
non-ASCII print per changed file.

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~15/AMGT_HARVST.TO-HVST-r-5.listing-capture-reachability-census.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4`, which must return rc 0.
3. Flip to `complete` only if every criterion passes. **Any verdict is a pass** -- wired 5 of 5 or wired 1 of 5 are both
   valid outcomes of a census; what fails is a census that cannot tell them apart.
4. Commit with `--only`.
5. Report once, with the five publisher lines quoted and the wired count.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The CTO called the silent publishers "not a code question".** This cell exists to make that statement MEASURED
   rather than assumed, so the fourth-act ask, if it comes, is about sessions alone.
2. **The negative control is the load-bearing arm**, exactly as in `HVST-r-2`. Round 1 taught this project three times
   that an instrument which cannot report the bad case reports nothing.
3. **The poison is required even though nothing here intends a call**, because four instances in round 1 came from tests
   that also did not intend one.

<status>complete</status>
<round>2</round>
<slot>~15</slot>
<fabric>site-z</fabric>
