# AMGT_CORPUS task order -- `CRPS-aq-2` -- ROUND 41: a served passage starts at a word, not at a scorecard label

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aq-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check re-composes offline from a frozen fixture.
comp-adversary: RUN by the issuer at the cut on HEAD 14dec5e21b -- aq12_check.py aq2: counts prefix 2 (BABA US, ST SP management), build 0/1 control 1/1. Blind spot: the prefix shape is one regex; a label of another shape is not counted.
EGRESS CLASS, declared: NONE. Library code and tests only. No S3, no Bloomberg, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continuing in the same worktree after `CRPS-aq-1` (your aq-1 commits are your inherited state).

## 1. THE CELL -- `CRPS-aq-2`

Two `management` values open with a scorecard label and score instead of a sentence: `BABA_US_Equity` reads
"Management/Board 80 Eddie Wu ..." and `ST_SP_Equity` likewise. The report's scorecard table cell (a label and a number) is taken as
the start of the passage.

**Build:**
1. A composed text value opens at a word of the passage: a leading scorecard label and score (`<Label> <1-3 digits> ` followed by
   the passage's first capitalised word) is not part of the value. Drop it in `lib/research/corpus/dossier.py` where the section
   text is read; never drop words of the passage itself.
2. A `management` value with no such prefix stays exactly as it is, character for character.
3. Add cases to `lib/research/corpus/tests/test_dossier_passage_edges_round41.py`: a value opening "Management/Board 80 Eddie Wu
   ..." opens at "Eddie Wu ..."; a value opening "Management changed in 2024 ..." is unchanged (a word, not a score).
4. `METHOD_VERSION` stays at `amgt-corpus-dossier/8` (aq-1's bump covers both cells).

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's check, fixture or snapshot.
2. NO S3, AWS, Bloomberg or vendor call. NO dossier write, NO push, NO deploy.
3. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W1-S<k>`, with `disarm_owner 2.0.0_SA_COO~C1`.
5. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_passage_edges_round41.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-aq-2.passage-starts-at-a-word.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aq-2.passage-starts-at-a-word.md
</paths>

Read-only: the whole repository, in particular `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/aq12_check.py`
and `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/evidence/r41_c2_scorecard_prefix_20261009.txt`.

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/aq12_check.py" aq2</invocation><expect>(?m)^aq2 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/aq12_check.py" aq1</invocation><expect>(?m)^aq1 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-aq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_dossier_passage_edges_round41.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
</proof_of_spec>

- AC1: no re-composed value opens with a scorecard label and score (PREFIX 0); management values without a prefix are unchanged.
- AC2: aq-1's result still holds.
- AC3: the tests pass with no failure.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit; rc 0.
2. Only if AC1-AC3 pass, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
3. Report ONCE: the change, AC1's and AC2's output lines, AC3's last line, your commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-40 analysis @`05739a6e4e` s.2 item 2. Base: aq2 counts prefix 2, build 0/1 control 1/1. Queued behind aq-1 on slot ~1 (same file). Then the issuer's aq-5 served re-write.
<risk>LOCAL</risk>
<status>pending</status>
<round>41</round>
<slot>~1</slot>
<fabric>dell1</fabric>
