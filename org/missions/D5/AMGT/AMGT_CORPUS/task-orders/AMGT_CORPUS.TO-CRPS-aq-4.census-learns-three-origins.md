# AMGT_CORPUS task order -- `CRPS-aq-4` -- ROUND 41: Z-S90's batch repair -- the read-only code census learns its three origins

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aq-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; a static scan of repository source.
comp-adversary: RUN by the issuer at the cut on HEAD 14dec5e21b -- the bound test reads 1 failed; the census reads tristate library 0 unresolved 6 clear 80 write_like_calls 86, both positive controls flagged 1. Blind spot: a static scan; it resolves origins by name, not by running the code.
EGRESS CLASS, declared: NONE. Library code and its test only.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 41. Your worktree is the absolute path the issuer gives you.

## 1. THE CELL -- `CRPS-aq-4`

`python -m lib.research.corpus.readonly_proof --code-census` scans the corpus code for write-like calls and sorts each into library /
clear / unresolved. It exits 1 on six UNRESOLVED sites, so
`lib/research/corpus/tests/test_readonly_proof_bound.py::test_code_census_arm_leaves_no_amgt_corpus_entry` fails. None of the six writes
the library (library_write_calls 0). They come from three origins the census does not know:
- `induction_request.py` about :475 `os.makedirs` / :476 `open` -- the operator's `--write <path>` argument (`_parse_write_path`), a request file;
- `induction_scheduled.py` about :150 `os.makedirs` / :152 `open` -- the fire's own log, `log_path(as_of)` under `%LOCALAPPDATA%\opal\amgt-induction-daily`;
- `tests/test_induction_request_pick_writes_nothing.py` about :73 `mkdir` / :74 `write_bytes` -- a test fixture under `_setup()`'s tmp cwd.

**Build:** teach `lib/research/corpus/readonly_proof.py` these three origins as CLEAR, each by name (the argv write path, the log
path, the test's tmp cwd), the narrowest rule that clears exactly these sites. Both positive controls must still be flagged. If the
bound test needs a line to state the three, add it in the test file; never weaken its assertion.

## 2. BOUNDS

1. Only the files in `<paths>` change. NO S3, AWS, Bloomberg or vendor call. NO push, NO deploy.
2. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
3. Rows are `AMGT_CORPUS-D1-W3-S<k>`, with `disarm_owner 2.0.0_SA_COO~C1`.
4. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~3 <0.9.0_WK_AMGT_CORPUS~3@opal.agent>" -F <msgfile> -- <paths>`.

## 3. SURFACES

<paths>
lib/research/corpus/readonly_proof.py
lib/research/corpus/tests/test_readonly_proof_bound.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-aq-4.census-learns-three-origins.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aq-4.census-learns-three-origins.md
</paths>

Read-only: the whole repository, in particular `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/evidence/r41_c5_zs90_census_sites_20261009.txt`.

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aq-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider "lib/research/corpus/tests/test_readonly_proof_bound.py::test_code_census_arm_leaves_no_amgt_corpus_entry" 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^1 passed in [\d.]+s$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aq-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m lib.research.corpus.readonly_proof --code-census 2&gt;&amp;1</invocation><expect>(?sm)(?=.*^tristate library 0 unresolved 0 )(?=.*^positive_control flagged 1$)(?=.*^positive_control_test_file flagged 1$)</expect></criterion>
</proof_of_spec>

- AC1: the bound test passes.
- AC2: the census reads library 0 and unresolved 0, with both positive controls still flagged.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2 --governing-order <this order>` AFTER your final commit; rc 0.
2. Only if AC1 and AC2 pass, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
3. Report ONCE: the change, AC1's line, AC2's census lines, your commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-40 analysis @`05739a6e4e` s.2 item 4 (row Z-S90, c5). Base: 1 failed; unresolved 6, both controls flagged 1. The round's batch repair cell -> worker-light.
<risk>LOCAL</risk>
<status>complete</status>
<round>41</round>
<slot>~3</slot>
<fabric>dell1</fabric>
