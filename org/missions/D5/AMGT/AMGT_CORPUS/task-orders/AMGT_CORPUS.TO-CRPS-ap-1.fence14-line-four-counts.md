# AMGT_CORPUS task order -- `CRPS-ap-1` -- ROUND 40: FWD-14's printed line is four named counts and their sum

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ap-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check calls one print function on hand-built records.
comp-adversary: RUN by the issuer at the cut -- ap1_check.py build 0/1 control 2/2 (the line reads "sum 3 outside-fence 1" against 4 folders).
EGRESS CLASS, declared: NONE.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 40.

## 1. THE CELL -- `CRPS-ap-1`

`lib/research/corpus/backlog.py` prints the FWD-14 census line in `_print_fence14_line` (about lines 458-480). Each research
folder is classified once by `_fence14_classify` (about 437-455) into resolved / ambiguous / empty-or-workbook-only, and any
other folder into a fourth class the code calls `outside-fence` (`FENCE14_OUTSIDE`, about 434). Today the line reads
`fence14 resolved 84 ambiguous 0 empty-or-workbook-only 12 sum 96 outside-fence 1 folders_read 97`: `sum` adds three classes only,
so it is one short of the folder count it sits beside. The PRD (v0.8 ADDENDUM C) names the fourth class
`unresolved-with-reason`. The counts are right; the print is wrong.

**Build, in `backlog.py` only (plus the test):**
1. The line is exactly: `fence14 resolved <a> ambiguous <b> empty-or-workbook-only <c> unresolved-with-reason <d> sum <a+b+c+d>
   folders_read <n>`. `sum` adds all four.
2. `_print_fence14_line` returns True only when that sum equals `folders_read`; both callers (`_run_coverage`,
   `_run_coverage_dry_run`) already exit non-zero on False. Keep that.
3. Each fourth-class folder is still printed on its own line with its folder, state and reason. Rename the line's tag from
   `fence14_outside` to `fence14_unresolved`, and the constant's VALUE to `unresolved-with-reason`. Keep the constant's name and
   the classification precedence unchanged.
4. Update the docstrings of the two functions to say four classes. Add an `AMENDMENT (CRPS-ap-1, round 40):` comment.
5. In `lib/research/corpus/tests/test_backlog_fence14.py`, update the three literal lines (about 83, 121, 144) and the
   `fence14_outside` prefix (about 89) to the new text, each with an `AMENDMENT (CRPS-ap-1, round 40):` comment. Add one test:
   a document whose `folders_read` is one more than its records makes `_print_fence14_line` return False.

## 2. BOUNDS

1. Change no classification rule and no other printed line (`fence ...`, the coverage totals, the never-prose lines).
2. Never run `python -m lib.research.corpus.backlog` without `--coverage-dry-run`; you do not need to run it at all.
3. NO push of any branch, NO deploy, NO AWS call, NO Bloomberg call, NO vendor call.
4. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
5. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
6. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
lib/research/corpus/backlog.py
lib/research/corpus/tests/test_backlog_fence14.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ap-1.fence14-line-four-counts.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ap-1.fence14-line-four-counts.md
</paths>

Read-only: the whole repository, in particular the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap1_check.py` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap1_check.py"</invocation><expect>(?m)^ap1 build 1/1 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest lib/research/corpus/tests/test_backlog_fence14.py lib/research/corpus/tests/test_backlog_fence_names.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1 (the REAL `_print_fence14_line` on four hand-built records): build -- the exact four-count line with sum 4 of 4 folders, and
  True; control -- one folder unaccounted for returns False, and the fourth-class folder is still printed by name.
- AC2: the amended fence14 tests and the untouched fence-names tests pass.

## 5. WHEN YOU ARE DONE

1. Run the pytest files named in AC2 once more after your last edit. Every test passes.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit
   as your instance.
4. Report ONCE: what you changed and where, every criterion's output line, the pytest summary line, your commit hashes and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 1 + s.4 item 1. Base: ap1 build 0/1 control 2/2; AC2 12 passed. The issuer's own `checks/round6/h4_AC1.sh` and `h4_AC2.sh` match the old line and are retired evidence, not re-run.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
