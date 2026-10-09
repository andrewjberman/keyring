# AMGT_CORPUS task order -- `CRPS-ar-1` -- ROUND 42: `risks` is recomposed, and a bullet line's end is a sentence end

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ar-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check re-composes offline from a frozen fixture.
comp-adversary: RUN by the issuer at the cut on HEAD b0213f2871 -- ar1_check.py: cut 0 ell_false 15 ell_true 0 line_end 2 prefix 0 of 123; risks outside the recomposed sections 23; build 0/1 control 1/1. Blind spot: 29 frozen names only; the served objects are read at the issuer's ar-2 leg v.
EGRESS CLASS, declared: NONE. Library code and tests only. No S3, no Bloomberg, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 42. Your worktree is the absolute path the issuer gives you; work and commit only there.

## 1. THE CELL -- `CRPS-ar-1`

`lib/research/corpus/dossier.py` composes each dossier text field from a picked research report. Round 41 added `_complete_passage`
(about line 601): a section value that does not end at a sentence end is read on in a pdf (`_pdf_continuation_tail`), or else gets an
explicit `...`. Two defects remain:

1. **`risks` is outside that path.** `_resolve_risks_field` (about line 1064) builds the risks value without `_complete_passage`, and
   `_section_field_names_resolved_as_blocks` (about line 1756) leaves `risks` out, so `_recompose_section_fields` (the census path)
   never composes it.
2. **A whole bullet line is marked as cut.** 15 values end in `...` although the report's line is complete (for example TTE FP
   "...partly due to being French-listed..."): the block's next line is a bullet, a blank, bold, a lead, a size change or the
   document's end -- or the value is a docx paragraph -- so nothing was cut. A bullet line's end is a sentence end.

**Build:**
1. `risks` goes through the same ending treatment as every section field, and `_recompose_section_fields` composes it, for every
   name with a risks block. Keep the risks field's existing shape (`value`, `citation`, and its `pre_mortem` attached by `build`).
2. A value that does not end at a sentence-end mark is left UNMARKED when the block does not continue in the same style (the rule:
   the next pdf line is non-blank, the same font size within `_CONTINUE_SIZE_TOLERANCE`, and not a section lead, bold or a bullet --
   otherwise it does not continue; a docx paragraph never continues). `...` is added ONLY when the block continues and the
   sentence could not be completed. Never invent words; never add a period.
3. Bump `METHOD_VERSION` from `amgt-corpus-dossier/8` to `amgt-corpus-dossier/9` and update the five tests pinning the literal
   `amgt-corpus-dossier/8` (listed in `<paths>`); change only that literal in them.
4. Add `lib/research/corpus/tests/test_dossier_risks_and_line_end_round42.py`: a risks value is completed like a section value; a
   value ending at a bullet line's end (next line a bullet) carries no `...`; a value whose next line continues in the same style
   and cannot be completed carries `...`; a docx paragraph without a period carries no `...`.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
2. NO S3, AWS, Bloomberg or vendor call. NO dossier write, NO push, NO deploy.
3. Do not touch `continuation.py` or the pillar `terms` shape.
4. Write code with the Edit/Write tools, never a shell heredoc, sed or `python -c` rewrite. ASCII only.
5. Rows are `AMGT_CORPUS-D1-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~C1`.
6. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.
   In your proof instance, `to_id` is this order's FULL id: `AMGT_CORPUS.TO-CRPS-ar-1.risks-recomposed-and-line-end`.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_risks_and_line_end_round42.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
lib/research/corpus/tests/test_dossier_passage_edges_round41.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ar-1.risks-recomposed-and-line-end.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ar-1.risks-recomposed-and-line-end.md
</paths>

Read-only: the whole repository, in particular the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round42/ar1_check.py`
(its docstring defines every class and the control).

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round42/ar1_check.py"</invocation><expect>(?m)^ar1 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round41/aq12_check.py" aq2</invocation><expect>(?m)^aq2 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_dossier_risks_and_line_end_round42.py lib/research/corpus/tests/test_dossier_passage_edges_round41.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
</proof_of_spec>

- AC1: cut 0, false ellipses 0, prefix 0, risks inside the recomposed sections for every name with a risks block; the control holds.
- AC2: round 41's opening repair still holds.
- AC3: the tests pass with no failure. If a round-41 test asserts a `...` on a whole bullet line, that assertion encodes the defect
  this cell fixes: change that assertion and say so in your report. `test_dossier_heading_only_round40.py` imports `fitz`, whose DLL
  does not load on this box: change its literal and say it was not run.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path (genre BUILD), with its mutant control. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit. It must return rc 0.
2. Only if AC1-AC3 pass, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
3. Report ONCE: the change and why, AC1's output lines (its counts and risks lines), AC2's and AC3's lines, your commit hashes, and any row.

## 6. AMENDMENT 1 (2026-10-09 ~18:5xZ, the issuer's own; your row AMGT_CORPUS-D1-W1-S2)

Your row is right: AC3 runs `test_dossier_passage_edges_round41.py`, which `<paths>` did not grant, and two of its assertions
(`test_sentence_that_cannot_be_completed_ends_with_an_ellipsis`, `test_docx_cut_before_a_heading_ends_with_an_ellipsis_not_a_comma`)
expect a `...` on a block that does not continue -- the defect this cell fixes. Ruling: `<paths>` now grants that file (added above).

**Do, and only this:** take the amendment by merging `box/dell1` into your branch (`git merge --no-edit box/dell1`). In that file,
change those two tests so they assert the round-42 rule (no `...` where the block does not continue; keep the trailing-comma drop
the second one checks), and rename them to say so. Change no other code. Re-run AC1-AC3 by their invocations, update your instance
(AC3 PASS by output, row D1-W1-S2 resolved by this amendment), run the checker after your final commit, and append the status tag
reading complete at the END of this file only if all three pass. Report once.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-41 analysis s.2 item 1 (msg 2982); CTO half ADDENDUM 1 (msg 2968). Base HEAD b0213f2871: ar1 build 0/1 control 1/1 (ell_false 15, risks outside 23). round 41's aq12 aq1 arm is NOT a criterion here: it counts a whole line without a period as CUT, which this cell makes correct. The served half is the issuer's ar-2 at /9.
<risk>LOCAL</risk>
<status>pending</status>
<round>42</round>
<slot>~1</slot>
<fabric>dell1</fabric>
