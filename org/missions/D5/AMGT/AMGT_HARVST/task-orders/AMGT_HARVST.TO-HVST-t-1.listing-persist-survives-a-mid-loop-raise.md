# AMGT_HARVST task order -- `HVST-t-1` -- ROUND 3, FIRST: the harvest listing persist must survive a MID-LOOP RAISE, so a 502 on article 7 cannot discard the listing pages already captured; CODE AND TESTS ONLY, OFFLINE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~16</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing, deploys nothing and writes no S3 object.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every store touch is a stub.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~16`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, `integrations/` and every path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~16;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER OR AWS. NEVER RUN THE HARVESTER's `run` OR `upload-*`.**

## 1. THE CELL, inlined in full -- `HVST-t-1` (manifest row H1, outcome FWD-1)

**THIS IS ROUND 3'S FIRST ACT AND THE ANALYSIS SAYS WHY.** `FWD-1`'s listing half has THREE possible causes, not
two. Round 2 eliminated the first: `HVST-r-5` proved listing capture is **WIRED 5 of 5**. The second is sessions,
which is Andrew's hold. **The third is ours, it is code, and row `AMGT_HARVST-Z-W15-S1` measured it:**

> `worker.py`'s harvest-mode listing persist (`_write_harvest_listings`) sits **AFTER the whole per-article loop**
> over `client.articles(...)`, so a job that raises mid-loop **discards every listing page already captured in
> memory for that job.**

**THE LIVE INSTANCE, from round 1's own run report:** seeking-alpha fetched MULTIPLE listing pages successfully and
then took an **HTTP 502 on a later article fetch**. Its listing pages existed in memory and never reached bronze.

**WHY IT IS FIRST.** `1.0.0_SA_CTO~Z`'s round-2 analysis: *"a fourth vendor act would NOT reliably produce listing
pages for any publisher whose job raises after page 1 ... FIX THE PERSIST PLACEMENT FIRST."* A vendor act spends a
scarce grant; this cell costs nothing and makes the grant worth spending.

**RULED -- what you build:**
1. **The persist must survive an exception raised anywhere inside the per-article loop.** Either persist each
   listing page AS IT IS CAPTURED, or checkpoint such that an exception cannot discard pages already captured.
   **Choose on the code's own shape and say in one line why**, in your report. Do not restructure the loop beyond
   what this requires.
2. **The proof is a DRIVEN MID-LOOP RAISE, not a reasoned argument.** A test must: drive a job whose client yields
   several articles, capture at least two listing pages, then RAISE from inside the loop on a later article, and
   assert the earlier pages **DID land** through the bronze listing writer.
3. **A NEGATIVE CONTROL, and it is the load-bearing arm.** An arm that proves the test can FAIL: with the persist
   restored to its old post-loop position (or the checkpoint disabled), the same driven raise must show the pages
   LOST. **A test that cannot show the bad case proves nothing** -- round 2 taught this project that three times.
4. **THE POISON, NAMED.** A no-network PASS with no poison proven is an ABSENCE. Poison `PacedSession.get`,
   `SessionManager.refresh` and `subprocess.run` so any real call RAISES, print a POSITIVE CONTROL showing each
   raises when tripped, and print `vendor_calls 0` **from a counter, never as a literal.** The package `conftest.py`
   that `HVST-r-4` built already poisons two of these; read it first and do not duplicate what it covers.
5. **NOTHING ELSE CHANGES.** The legacy (non-harvest) path is untouched. No S3 object is written. No existing
   test's outcome changes.

**What this cell does NOT do:**
- it does not re-fetch or recover the listing pages round 1 already discarded -- **they are lost and your report
  says so;**
- it does not touch sessions, credentials or any publisher;
- it does not change the bronze key grammar.

## 2. WHERE THIS CAME FROM
Round 3, decomposition v1.2 @04329b6a4c section 12a, cell 1 of 2, ranked FIRST by the round-2 analysis
@`2539343348` and confirmed by its settling ruling (msg 24591). Independent of `HVST-t-2`.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_listing_persist_durability.py
lib/opal_data_harvest/test_worker.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~16/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-t-1.listing-persist-survives-a-mid-loop-raise.md
</paths>

**READ-ONLY REFERENCES -- read these; they are deliberately NOT in the write grant:**
- `lib/opal_data_harvest/harvest_grammar.py` -- the bronze listing writer.
- `lib/opal_data_harvest/publishers.py` -- where listings are recorded during discovery.
- `lib/opal_data_harvest/conftest.py` -- `HVST-r-4`'s package poison, so you do not duplicate it.
- `lib/opal_data_harvest/census_listing_capture.py` -- `HVST-r-5`'s stub-driving pattern, already proven.
- `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/RUN_REPORT.md` -- the live 502.

- **Only `worker.py` and the two test files may CHANGE**, and `test_worker.py` only if an existing arm genuinely
  needs updating for the new placement. AC3 fails if any other production module changes.
- Scratch goes in `<your worktree>/.scratch/t1/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~16 <0.9.0_WK_AMGT_HARVST~16@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with a non-shell writer.

## 4. BOUNDS
- **OFFLINE ONLY. CODE AND TESTS ONLY. Pure ASCII, LF only.**
- **BASELINES, AND THE CHECKOUT THEY WERE MEASURED IN.** All counts below were measured by the issuer in the
  **FULL SHARED WORKTREE** at the round-2 drain, NOT in a sparse cone: `test_retrieval_provenance` 18 passed,
  `test_bronze_capture` 12, `test_silver_from_bronze` 16, `test_legacy_upload` 6, `test_harvest_grammar` 7,
  `test_worker` 2 failed and 18 passed, `test_catalog` 5, `test_verification` 1 failed and 3 passed,
  `test_poison_control` 3, `test_check_as_received` 16, `test_listing_capture_census` 18.
  **The two pre-existing failures in `test_worker` and `test_verification` are NOT yours to fix and must not GROW.**
  **IF A COUNT DIVERGES IN YOUR WORKTREE, THAT IS AN ENVIRONMENT FINDING AND YOU FILE A ROW** -- it is not a
  repository defect and it is not yours to work around. Last round a worker recorded exactly such a divergence as a
  pre-existing failure and it was the issuer's sparse cone (row `Z-S4`).
- **Surprise rows:** `AMGT_HARVST-Z-W16-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_retrieval_provenance test_bronze_capture test_silver_from_bronze test_legacy_upload test_harvest_grammar test_worker test_catalog test_verification test_poison_control test_check_as_received test_listing_capture_census; do echo "$t :: $(python -m pytest lib/opal_data_harvest/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit, eleven baseline lines recorded; each should equal the section-4 count measured in the full shared tree, and ANY divergence is recorded as an environment finding with a row rather than treated as a repository failure</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_listing_persist_durability.py -v --color=no -p no:cacheprovider 2>&1 | tail -16</invocation><expect>every arm passes and no "failed" -- including the DRIVEN MID-LOOP RAISE arm asserting the earlier listing pages DID land, and the NEGATIVE CONTROL arm proving that with the persist at its old post-loop position the same driven raise LOSES them</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_retrieval_provenance test_bronze_capture test_silver_from_bronze test_legacy_upload test_harvest_grammar test_worker test_catalog test_verification test_poison_control test_check_as_received test_listing_capture_census; do echo "$t :: $(python -m pytest lib/opal_data_harvest/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line's passed and failed counts EQUAL its AC0 line: the placement change altered no existing test's outcome and neither pre-existing failure grew</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/t1/ac3.py</invocation><expect>"outside_allowed []" -- only worker.py and the two named test files changed, nothing else under lib; each changed file prints "compiles True crlf 0 non_ascii 0"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-t-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/t1/ac4.py</invocation><expect>"vendor_calls 0" read from a counter, and a POSITIVE CONTROL showing each of PacedSession.get, SessionManager.refresh and subprocess.run RAISES when deliberately tripped; the script states which of the three the package conftest already covers rather than duplicating it</expect></criterion>
</proof_of_spec>

Write `.scratch/t1/ac3.py` (diff from `git merge-base HEAD SITEZ` over `lib`, an allowed set, and a compile, CRLF and
non-ASCII print per changed file) and `.scratch/t1/ac4.py` (the poison counter and its positive control).

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~16/AMGT_HARVST.TO-HVST-t-1.listing-persist-survives-a-mid-loop-raise.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4`, which must return rc 0.
3. Flip to `complete` only if every criterion passes.
4. Commit with `--only`.
5. Report once, quoting the mid-loop-raise arm's assertion, the negative control's result, and the one line saying
   why you chose per-page persist or a checkpoint. **Say plainly that the pages round 1 discarded are not
   recovered.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **AC1's negative control is the whole cell.** Without it, "the pages landed" is consistent with a test that
   never raised where it claimed to. Round 2 produced three instances of that shape.
2. **The baselines name their checkout on purpose**, and the order tells the worker that a divergence is an
   environment finding. That instruction exists because row `Z-S4` is the issuer's own defect from last round.
3. **The cone for this worktree includes `org/missions` WHOLE and `integrations`**, so neither the missions hook
   nor the seekingalpha import can produce a false finding this time.

<status>pending</status>
<round>3</round>
<slot>~16</slot>
<fabric>site-z</fabric>
