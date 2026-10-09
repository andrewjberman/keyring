# AMGT_CORPUS task order -- `CRPS-aq-1` -- ROUND 41: a served passage ends at a sentence end, or says it was cut

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check re-composes offline from a frozen fixture.
comp-adversary: RUN by the issuer at the cut on HEAD 14dec5e21b -- aq12_check.py aq1: counts cut 25 of 95, build 0/1 control 1/1. Blind spot: offline re-compose of 29 names only; the served objects are read by the issuer's paired act aq-5.
EGRESS CLASS, declared: NONE. Library code and tests only. No S3, no Bloomberg, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 41. Your worktree is the absolute path the issuer gives you; work and commit only there.

## 1. THE CELL -- `CRPS-aq-1`

The dossier's text fields (`company_description`, `growth_algorithm`, `investment_thesis_summary`, `management`, `negatives`,
`positives`, `risks`, `special_items`, `thesis_summary`, `why_we_own`) are composed from a picked research report by
`lib/research/corpus/dossier.py` (`_recompose_section_fields(pick_a, pick_b)`, about line 1728, and the section-block readers it
calls, from about line 317). In 25 of 95 such values for the affected names the passage STOPS MID-SENTENCE: for example
`8306 JP company_description` ends "...contributed 25%+ of earnings in each of the past five years" and `8766 JP management` ends
"...He was also known for emphasizing corporate culture," -- the report's sentence goes on past a page break or a block boundary the
reader treats as the end.

**Build:**
1. A composed text value ends at a sentence end: one of `. ! ? ; : ) ] " '` (and the curly quote forms). Where the report's sentence
   continues in the next block or across the page break, read on to its end. Where the sentence cannot be completed from the report,
   end the value with an explicit ellipsis (`...`) so the reader sees it was cut. Never invent words.
2. A value that ALREADY ended at a sentence end must stay exactly as it is, character for character.
3. Bump `METHOD_VERSION` (`dossier.py:146`) from `amgt-corpus-dossier/7` to `amgt-corpus-dossier/8`, and update the five tests that
   pin the literal `amgt-corpus-dossier/7` (they are listed in `<paths>`); change only that literal in them.
4. Add `lib/research/corpus/tests/test_dossier_passage_edges_round41.py` with at least: a sentence that continues into the next block
   is read to its end; a sentence that cannot be completed ends with `...`; a value already ending at `.` is unchanged.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's check, fixture or snapshot (`checks/round41/aq12_check.py`,
   `aq12_picks.json`, `aq12_base_values.json`).
2. NO S3, AWS, Bloomberg or vendor call. NO dossier write (`--write`), NO push, NO deploy.
3. Do not touch `continuation.py` or the pillar `terms` shape.
4. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
5. Rows are `AMGT_CORPUS-D1-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~C1`
   and `surfaced_at` from `date -u +%FT%TZ` at filing.
6. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`,
   the message file written with the Write tool.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_passage_edges_round41.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-aq-1.passage-ends-at-a-sentence-end.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aq-1.passage-ends-at-a-sentence-end.md
</paths>

Read-only: the whole repository, in particular the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/aq12_check.py`
(its docstring defines CUT and the control) and the c1 evidence `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/evidence/r41_c1_truncated_values_20261009.txt`.

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/aq12_check.py" aq1</invocation><expect>(?m)^aq1 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_dossier_passage_edges_round41.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
</proof_of_spec>

- AC1: over the 24 affected names, every re-composed text value ends at a sentence end or an explicit ellipsis (CUT 0); every value
  that already ended at a sentence end at the base is unchanged.
- AC2: the new test and the four method-pinning tests that collect on this box pass with no failure (base: 39 passed).
  `test_dossier_heading_only_round40.py` imports `fitz`, whose DLL does not load on this box (39 of its 47 fail at the base on
  `ImportError: DLL load failed`); change its literal anyway and say in your report that it was not run here.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path (genre BUILD), with its mutant control. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
2. Only if AC1 and AC2 pass, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
3. Report ONCE: the change and why, AC1's output lines (including its counts line), AC2's last line, your commit hashes, and any row.
   The issuer then hands you `CRPS-aq-2` in the same worktree.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-40 analysis @`05739a6e4e` s.2 item 1 (msg 2835). Base HEAD 14dec5e21b: aq1 counts cut 25 of 95, build 0/1 control 1/1. Same file as aq-2; slot ~1 takes aq-2 by continuation. The served half is the issuer's aq-5 (never-widen pair to 1.0.0_SA_CTO~DELL1) after aq-2 drains.
<risk>LOCAL</risk>
<status>pending</status>
<round>41</round>
<slot>~1</slot>
<fabric>dell1</fabric>
<status>complete</status>
