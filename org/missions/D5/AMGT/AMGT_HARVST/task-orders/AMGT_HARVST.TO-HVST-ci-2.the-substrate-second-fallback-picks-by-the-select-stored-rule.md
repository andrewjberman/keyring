# AMGT_HARVST task order -- `HVST-ci-2` -- ROUND 94, workstream PICK2-FIX: THE SUBSTRATE'S SECOND FALLBACK (NO STORED OBJECT'S INPUTS MATCH TODAY'S) PICKS BY THE `_select_stored` RULE, NEVER BY KEY ORDER (row `W165-S3`; CTO round-93 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ci-2.the-substrate-second-fallback-picks-by-the-select-stored-rule</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ci-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~169</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in the census step ONLY: list and get under the four gold tables the substrate reads and whatever each producer's `current_inputs(...)` reads, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 8000 requests and 1 GiB in all, counted in the census's last line. NO gold or silver writer is RUN, NO `write_one`, NO deploy, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a fix that picks the highest method version only when the keys happen to sort that way (test with the keys in the order that breaks it), a picker that ranks `/10` below `/9` because it compares strings (compare the integer; `_select_stored` already does), a change that moves the input-MATCHING branch (it must stay as it is), a change that flags the fallback `current` True (it stays False), a rule re-implemented beside `_select_stored` (call it, do not copy it), a census that grades the changed module against the changed module (the rule is reimplemented in the census, as in `ci1_census.py`), and a test that passes whatever the code does (it has a mutant).
</preflight>

## 0. THE CELL

`lib/research/corpus/substrate.py::_pick_stored` (line 121) picks, among a table partition's stored objects, the one whose `inputs` equal today's through `continuation._select_stored` (the highest-method-version rule `HVST-ch-1` fixed). **When NO object's `inputs` match it still returns `docs[sorted(docs)[-1]]` (line 158), the lexicographically LAST KEY (a content hash, an arbitrary pick), with `current` False.** The CTO's ruling: the fallback takes the SAME rule as `_select_stored` (the highest `method_version`, then the last written), still flagged `current` False, never decided by key order. This cell makes that one change, tests it with a difference-controlled test, and re-runs the census of `HVST-ci-1` after the change. Your earlier order `HVST-ci-1` (same worker queue) wrote `ci1_census.py` and `ci1_census.out` in your deliverables folder: read both first; they print how many partitions fall to the fallback and which would move.

## 1. THE BUILD (LOCAL, about 15 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/substrate.py` change ONLY the fallback at the end of `_pick_stored` and its docstring:
   - the input-matching branch (`candidates` non-empty) stays EXACTLY as it is;
   - the fallback becomes: build `[(key, last_modified, docs[key]) for key, last_modified in listing]` (every stored object of the partition, the same triples the matching branch builds) and call `continuation._select_stored(<that list>, current_method_version)`; return that object's document, its `s3://` uri, and `False`. Call `_select_stored`; do NOT copy its rule;
   - the docstring sentence `Otherwise the lexicographically LAST stored object under that partition (current=False, an arbitrary but deterministic pick among possibly-several stale objects -- gold never overwrites)` becomes `Otherwise (no stored object's inputs match) the stored object chosen by continuation._select_stored over ALL the partition's objects: the highest method_version, then the last written, never key order (current=False; AMENDED round 94, row D1-W165-S3, CTO round-93 analysis item 1).`
   - `(None, None, None)` for an empty partition stays.
b. New test `lib/research/corpus/tests/test_substrate_fallback_pick.py`, offline (read `lib/research/corpus/tests/test_substrate.py` first for its fake S3 client and copy that style; change nothing in it). Arms: (1) **the difference-controlled test:** a partition of four stored objects shaped like UNH's (names `28404359eb0645c4.json` method `.../3`, `4d837586380648bd.json` `.../4`, `98a4883c1b099e6b.json` `.../1`, `f174f7092a2d358e.json` `.../2`, last-modified rising in the order /1, /2, /3, /4), NONE whose `inputs` equal `wanted`: the new `_pick_stored` returns `4d837586380648bd.json` with `current` False, and the OLD rule written in the test (`sorted(docs)[-1]`) returns `f174f7092a2d358e.json`, so they DISAGREE; (2) the same four with the object names reassigned so the highest version has the LAST name in sort order: still the highest version (the test does not pass by luck of ordering); (3) two objects at the same highest version: the later `last_modified` wins; equal `last_modified`: the greater name wins; (4) `/10` beats `/9`; (5) the input-MATCHING branch is unchanged: a partition with one object whose inputs match (method `.../3`) and a newer non-matching object at `.../5` returns the matching one with `current` True; (6) an empty partition returns `(None, None, None)`; one object is returned; (7) **A MUTANT:** with the fallback monkeypatched to `sorted(docs)[-1]`, arm (1) FAILS (assert that it does).
c. **The census after the change (read-only).** Write `ci2_census_after.py` in your deliverables folder (start from your `ci1_census.py`) and run it once in the FOREGROUND with `python -u`, stdout to `ci2_census_after.out` (open the output file with `newline="\n"`). For every partition of the four tables that has NO input-matching object (recompute them as `ci1_census.py` does): call the CHANGED `substrate._pick_stored(table, partition, wanted, <the producer's METHOD_VERSION>, client)` and print `AFTER <table> <partition> module=<first 8 characters of the object name>/<method_version integer> rule=<...>/<...> old=<...>/<...> module_equals_rule=<yes|no> moved_from_old=<yes|no>` where RULE and OLD are the reimplemented rules of `ci1_census.py`, not the changed module. Then `CONTROL-DIFFERENCE module_pick=rule_pick old_pick_differs=yes`, printed only when the UNH-shaped four of step b (1), run through the real changed `_pick_stored` with a fake client, return the RULE object and differ from the OLD object. Then exactly `CENSUS-FALLBACK-AFTER fallback_partitions=<n> module_equals_rule=<n> moved_from_old=<n> gets=<requests> bytes=<bytes>`. **Every partition where the pick moves from OLD is printed (its line says `moved_from_old=yes`); a served move goes under its own pair, so file ONE surprise row listing the moved partitions (or saying none) with the reason you can read.** Do not change anything to make a count read 0.
d. Do not touch `continuation.py`, `gold.py`, any gold or silver writer, or any other file. A surprise is a row; keep working.

<paths>
lib/research/corpus/substrate.py
lib/research/corpus/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ci-2"><invocation>python -m pytest lib/research/corpus/tests/test_substrate_fallback_pick.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ci-2"><invocation>python -m pytest lib/research/corpus/tests/test_continuation.py lib/research/corpus/tests/test_continuation_pillar_body.py lib/research/corpus/tests/test_continuation_reader_method.py lib/research/corpus/tests/test_continuation_terms.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_substrate.py lib/research/corpus/tests/test_continuation_pdf_recommendation_line.py lib/research/corpus/tests/test_continuation_holding_stance.py lib/research/corpus/tests/test_select_stored_fallback.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^96 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ci-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/ci2_census_after.out</invocation><expect>(?ms)^CONTROL-DIFFERENCE module_pick=rule_pick old_pick_differs=yes$.*^CENSUS-FALLBACK-AFTER fallback_partitions=(\d+) module_equals_rule=\1 moved_from_old=\d+ gets=\d+ bytes=\d+$</expect></criterion>
</proof_of_spec>

- AC2 is the unchanged-behaviour check: the nine existing test files (96 tests at the base, issuer dry run 2026-10-18 ~05:4xZ) must still pass; do not change any of them. AC3's `\1` makes the census grade itself: the changed module's pick equals the rule's for EVERY fallback partition, whatever their number (zero is possible), and the control line shows the change differs from the key-order rule.
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`96 passed in 1.09s`); AC3 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id follows your last (`AMGT_HARVST-D1-W169-S<n+1>`). The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/AMGT_HARVST.TO-HVST-ci-2.the-substrate-second-fallback-picks-by-the-select-stored-rule.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ci-2.the-substrate-second-fallback-picks-by-the-select-stored-rule` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ci-2.the-substrate-second-fallback-picks-by-the-select-stored-rule.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-93 analysis (`ledger/ROUND_ANALYSIS.round93.md` @5ef0dd0efd, msg 7921) item 1 (the fallback takes the same rule as `_select_stored`, still flagged `current` False; graded by a difference-controlled test plus the census re-read; a partition whose pick moves is printed and a served move goes under its own pair).
- **Chain A, second order, same worker queue `~169`:** depends on `HVST-ci-1` (its census is the "before" of this cell). I hand it to the SAME worker by continuing it after `ci-1` merges, with this order file on its branch (the order file on the worker's branch is the grant). It writes no object; the code lands in the repo only. **Measured by me (a grep of `lib/research`, `infra/aws/ec2/opal-gateway` and `portal` `.py` files for the word `substrate`: 15 files, none under the gateway folder):** the readers of the substrate are the corpus builders (`dossier.py`, `report_input.py`) and tests, so the change moves only what a FUTURE dossier or report-input build would read, never a served value by itself; whether a name's pick moves is what the census prints, and a move is the CTO's to see. I did not read `report_input.py`'s use.
- Slot ~169, worktree `C:/dev/wk-harvst-169` (the same as `ci-1`), branch `wk-AMGT_HARVST-169`.
- **SENT:** with the round-94 issuance (the order is cut now; the worker starts it after `ci-1`).

**COMPLETE 2026-10-18T06:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~169`, fix `9ebf5ef8c7`, proof `da024d88f7`; merged `6837f7c754`. The diff I read: `substrate._pick_stored`'s input-matching branch unchanged; the fallback builds `[(key, last_modified, docs[key]) ...]` over ALL the partition's objects and calls `continuation._select_stored` (not a copy of its rule), returns `current` False; the docstring amended as ordered; `1 file changed, 8 insertions(+), 6 deletions(-)` in `substrate.py`; one new test file (244 lines, 10 tests).
- **AC1 PASS:** `10 passed in 0.40s` (re-run here `0.40s`; includes the mutant arm). **AC2 PASS:** `96 passed in 1.03s` (the nine existing files, unchanged; re-run here). **AC3 PASS:** `CONTROL-DIFFERENCE module_pick=rule_pick old_pick_differs=yes` and `CENSUS-FALLBACK-AFTER fallback_partitions=0 module_equals_rule=0 moved_from_old=0 gets=4655 bytes=384039907`; the control detail reads `module=4d837586/4 rule=4d837586 old=f174f709 current=False`; **I re-ran `ci2_census_after.py` myself: identical to the worker's.** Proof instance VALID rc 0 (re-run here).
- **No partition moves** (fallback_partitions=0, as `ci-1` read), so nothing served or buildable moves from this change today; the change proves itself on the synthetic UNH-shaped four through the real function (it returns the highest method version, where the old rule returned the last key).
- **A difference between the face I sent the worker (in my resume message) and the order file on its branch, mine:** the message added "(your census read 0 of 109 today; ...)" to section 0 and "(there may be none)" to step c; no criterion text differs. The worker disclosed its first census run crashed in its control helper before any line printed (a `utc()` argument bug), fixed and re-run once; row `D1-W169-S2` (OBSERVATION, INERT: no partition moved) read and accepted.
- **What this does NOT prove:** the behaviour for a partition that really falls to the fallback beyond the synthetic arms (none exists today).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>94</round>
<workstream>PICK2-FIX</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
