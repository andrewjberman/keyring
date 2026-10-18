# AMGT_HARVST task order -- `HVST-ch-1` -- ROUND 93, workstream PICKER-FIX: WITH NO CANDIDATE AT THE CURRENT METHOD VERSION THE STORED-OBJECT PICKER TAKES THE HIGHEST METHOD VERSION, THEN THE LAST WRITTEN, NEVER THE FIRST KEY IN SORT ORDER (row D1-S52; CTO ruling `ledger/CTO_RULING_D1_S52_CONTINUATION_PICK_20261018.md` @162d5a6934; round-92 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ch-1.the-stored-object-fallback-picks-the-highest-method-version-never-by-key-order</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ch-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~165</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in the census step ONLY: list and get under `amgt/harvest/gold/research-continuation/`, `amgt/harvest/silver/research-report/` and the extraction objects the silver rows name, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 1500 requests and 500 MiB in all, counted in the census's last line. NO gold or silver writer is RUN, NO `write_one`, NO deploy, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a fix that picks by the NEWEST method version only when the keys happen to sort that way (test with the keys in the order that breaks it), a picker that ranks `/10` below `/9` because it compares strings (compare the integer), a change that moves the CURRENT-version branch (it must stay byte-for-byte), a census that compares the new pick with the pick of the NEW code twice (the old rule is reimplemented in the census, not read from the changed module), a gateway rule that is read from memory (copy it from the cited line), and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

`lib/research/corpus/continuation.py::_select_stored(candidates, current_method_version)` (line 1087) chooses which stored continuation object a reader gets. `candidates` is `[(key, last_modified, document), ...]`, every one already known to carry the wanted `inputs`. When some candidate carries the current method version (`/5`), it picks the one written last. **When NONE does, it returns `min(candidates, key=lambda c: c[0])`: the lexicographically FIRST KEY.** The key is a content hash, so the pick is arbitrary. `substrate._pick_stored` (`lib/research/corpus/substrate.py:121-159`) and `continuation.read_latest` (line 1106) both go through it. Measured by the CTO and the issuer: `UNH_US_Equity` has four stored continuations with equal inputs, `28404359eb0645c4.json` (method `/3`, 2026-09-29, `fund_of_record` ABSENT), `4d837586380648bd.json` (`/4`, 2026-10-17, PFOE), `98a4883c1b099e6b.json` (`/1`) and `f174f7092a2d358e.json` (`/2`); none is at `/5`; the picker returns `28404359` (/3) while the gateway serves `4d837586` (/4). 77 of the 94 securities are not rebuilt at `/5`, so any of them can land on any version. **The CTO ruled: with no candidate at the current method version the fallback picks the HIGHEST `method_version`, and the last written among those (the same `_later_candidate` tie rule); it never picks by key order; fixed once, in `_select_stored`, the one rule `read_latest` and the substrate share.** This cell changes `_select_stored`, tests it with a difference-controlled test, and runs a read-only census. It writes no object and changes no other file.

## 1. THE BUILD (LOCAL, about 20 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/continuation.py` change ONLY `_select_stored`'s final `return`, and its docstring:
   - the `current_group` branch stays EXACTLY as it is;
   - when `current_group` is empty: compute each candidate's version as the INTEGER after the last `/` of its `document.get("method_version")` (for example `"amgt-corpus-continuation/4"` is 4); a missing or unparsable value counts as -1; keep the candidates whose version equals the maximum; return the one written last among those by `_later_candidate` (iterate as the `current_group` branch does);
   - docstring: replace the sentence about "the first key in sorted order" with `AMENDED round 93 (row D1-S52, CTO ruling @162d5a6934): with no candidate at the current method version, the highest method_version wins, then the last written; never the first key.`
b. New test `lib/research/corpus/tests/test_select_stored_fallback.py`, offline. Arms: (1) **the difference-controlled test:** four candidates shaped like UNH's (keys `28404359eb0645c4.json` method `.../3`, `4d837586380648bd.json` `.../4`, `98a4883c1b099e6b.json` `.../1`, `f174f7092a2d358e.json` `.../2`, with last_modified rising 2026-09-25, 09-26, 09-29, 10-17 in the order /1, /2, /3, /4) and `current_method_version` `.../5`: the new `_select_stored` returns `4d837586380648bd.json`, and a local copy of the OLD rule (`min(candidates, key=lambda c: c[0])`, written in the test) returns `28404359eb0645c4.json`; (2) the same four with the keys reassigned so the highest version has the FIRST key in sort order: still the highest version (so the test does not pass by luck of ordering); (3) two candidates at the same highest version: the later `last_modified` wins; equal `last_modified`: the greater key wins, as `_later_candidate`; (4) `/10` beats `/9` (integer, not string, comparison); (5) a missing or unparsable `method_version` loses to any parsable one; (6) a candidate AT the current version beats a higher-written older one, whatever the last_modified (the current-version branch is unchanged); (7) one candidate is returned; (8) `continuation.read_latest` on a fake client holding the UNH-shaped four returns `4d837586380648bd.json` (copy the fake client from `tests/test_continuation.py`; read it first; change nothing in it); (9) **A MUTANT:** with `_select_stored` monkeypatched to the old rule, arm (1) FAILS (assert that it does).
c. **The census (read-only).** Write `ch1_census.py` in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `ch1_census.out`. For EVERY security that has a continuation partition under `amgt/harvest/gold/research-continuation/`: list the partition, read every object (each document carries `method_version`, `inputs`), compute `wanted = continuation.current_inputs(security_key, client)` and keep the objects whose `inputs` equal `wanted` (these are the substrate's candidates). If some candidate carries `continuation.METHOD_VERSION`, count the security under `with_current` and print nothing for it. Otherwise print one line `PICK <security_key> candidates=<n> old=<first 8 characters of the key>/<method_version integer> new=<...>/<...> gateway=<...>/<...> new_equals_gateway=<yes|no>` where OLD is the rule reimplemented in the census (`min` by key), NEW is the changed `_select_stored`, and GATEWAY is the rule of `infra/aws/ec2/opal-gateway/app/harvest_research.py` line 349 copied into the census (`max` over ALL objects of the partition, ordered by (LastModified as an ISO string, or "" when missing, then the key)); read that line first. Then exactly `CENSUS-PICKER securities=<n with a partition> with_current=<n> no_current=<n> new_equals_gateway=<n> new_differs_from_gateway=<n> old_equals_gateway=<n> old_differs_from_gateway=<n> gets=<requests> bytes=<bytes>`. **Every name where NEW differs from GATEWAY is printed (its line says `new_equals_gateway=no`); file ONE surprise row listing them and why each differs (stale inputs, or a newer object whose inputs differ).** Do not change anything to make a count read 0.
d. Note, do not fix: `substrate._pick_stored` line 158 has a SECOND fallback by key order (`sorted(docs)[-1]`, when NO candidate's inputs match); it is outside the CTO's ruling. File one INERT row naming it and the number of securities in the census whose partition has NO input-matching object (print that number as `no_input_match=<n>` before the final line).
e. Do not touch `substrate.py`, `gold.py`, any gold or silver writer, or any other file. A surprise is a row; keep working.

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ch-1"><invocation>python -m pytest lib/research/corpus/tests/test_select_stored_fallback.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ch-1"><invocation>python -m pytest lib/research/corpus/tests/test_continuation.py lib/research/corpus/tests/test_continuation_pillar_body.py lib/research/corpus/tests/test_continuation_reader_method.py lib/research/corpus/tests/test_continuation_terms.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_substrate.py lib/research/corpus/tests/test_continuation_pdf_recommendation_line.py lib/research/corpus/tests/test_continuation_holding_stance.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^82 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ch-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165/ch1_census.out</invocation><expect>(?m)^CENSUS-PICKER securities=\d+ with_current=\d+ no_current=\d+ new_equals_gateway=\d+ new_differs_from_gateway=\d+ old_equals_gateway=\d+ old_differs_from_gateway=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-ch-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165/ch1_census.out</invocation><expect>(?m)^PICK UNH_US_Equity candidates=4 old=28404359/3 new=4d837586/4 gateway=4d837586/4 new_equals_gateway=yes$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the CTO's named difference test on the live data (UNH: the old rule picks `/3`, the new rule picks `/4`, the gateway serves `/4`); it is separate from AC3 because AC3 is the shape of the census and AC4 is a claim about the world that may not hold. **If the census prints a different UNH line, DO NOT edit the expectation or the code to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~03:5xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`82 passed in 1.08s` over the eight files); AC3 and AC4 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W165-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165/AMGT_HARVST.TO-HVST-ch-1.the-stored-object-fallback-picks-the-highest-method-version-never-by-key-order.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ch-1.the-stored-object-fallback-picks-the-highest-method-version-never-by-key-order` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ch-1.the-stored-object-fallback-picks-the-highest-method-version-never-by-key-order.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-92 analysis (`ledger/ROUND_ANALYSIS.round92.md` @943c856f6e, msg 7867) item 1 and ruling `ledger/CTO_RULING_D1_S52_CONTINUATION_PICK_20261018.md` @162d5a6934. Decomposition section 123.
- **This cell alone lifts nothing:** the standing instruction (no dossier or continuation rebuild for a name with no `/5` continuation) lifts when this cell AND the shared-classifier cell (`HVST-ch-2`) are merged and their censuses read 0 differing (round-92 analysis item 4). The issuer reads the census here; any name where NEW differs from GATEWAY is a row and the CTO's.
- **`HVST-ch-2` (the shared classifier) edits the same file `continuation.py`:** it is held behind this cell (one dependency chain, no shared write set at a time).
- Slot ~165, worktree `C:/dev/wk-harvst-165`, branch `wk-AMGT_HARVST-165`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922` and `infra/aws/ec2/opal-gateway/app` (read-only, for the gateway's pick rule and the tests that read it).
- **AMENDMENT 1 (issuer, 2026-10-18 04:0xZ; worker `~165` row `D1-W165-S1`, BLOCKING, INERT): THE CENSUS BUDGET WAS THE ISSUER'S MISCOUNT.** The face said at most 1500 requests and 500 MiB; the census aborted at request 1501 after 67 of 95 partitions (125,032,896 bytes), about 22 requests per security. **New total budget for the census step: at most 3500 requests and 600 MiB.** The worker also found a defect in its own census (row `-S2`: the `PICK` line printed `key[:8]` of the full S3 key); the amendment requires the object-name prefix. The worker reruns the census once and regrades `AC3` and `AC4`; the earlier `BUDGET-EXCEEDED` reading stays in the proof instance as history. No criterion text changed.
- **SENT:** with the round-93 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>93</round>
<workstream>PICKER-FIX</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
