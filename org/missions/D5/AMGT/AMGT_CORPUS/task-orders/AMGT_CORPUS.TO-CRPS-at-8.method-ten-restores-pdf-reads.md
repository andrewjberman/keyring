# AMGT_CORPUS task order -- `CRPS-at-8` -- ROUND 44: METHOD /10, the /9 method re-written with PDF reads restored (row D1-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-at-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a version literal and its pinning tests; no AWS act.
comp-adversary: RUN by the issuer at the cut on HEAD f60af71c3f -- METHOD_VERSION reads amgt-corpus-dossier/9; the 5 pinning tests pass with fitz loading. Blind spot: the served re-write and its every-section diff are the issuer's act (CRPS-at-9).
EGRESS CLASS, declared: NONE.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 44. Your worktree is the absolute path the issuer gives you.

## 1. THE CELL -- `CRPS-at-8`

The served dossiers at `amgt-corpus-dossier/9` lost the team cases on six PDF names because the write ran where the PDF reader could
not load. The code is right; the objects must be re-written. A re-write only happens at a new method version (an unchanged method
with unchanged inputs writes nothing). This cell makes that version.

**Build:** in `lib/research/corpus/dossier.py` change `METHOD_VERSION = "amgt-corpus-dossier/9"` to `"amgt-corpus-dossier/10"`, and add
one comment line above it: `# /10 (CRPS-at-8, row D1-S2): /9's method re-written with the PDF reader loading; no logic change.` In the
five tests listed in `<paths>`, change ONLY the literal `amgt-corpus-dossier/9` to `amgt-corpus-dossier/10`. Change nothing else.

## 2. BOUNDS

1. Only the files in `<paths>` change. No S3 write, no deploy, no push, no Bloomberg or vendor call.
2. Edit/Write tools only; ASCII only. Rows are `AMGT_CORPUS-D1-W3-S<k>`, `disarm_owner 2.0.0_SA_COO~C1`.
3. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~3 <0.9.0_WK_AMGT_CORPUS~3@opal.agent>" -F <msgfile> -- <paths>`.
   Your proof instance's `to_id` is `AMGT_CORPUS.TO-CRPS-at-8.method-ten-restores-pdf-reads`.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-at-8.method-ten-restores-pdf-reads.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-at-8.method-ten-restores-pdf-reads.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-at-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -c "from lib.research.corpus import dossier; print('method', dossier.METHOD_VERSION)"</invocation><expect>(?m)^method amgt-corpus-dossier/10$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-at-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py lib/research/corpus/tests/test_dossier_heading_only_round40.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed[ ,]</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance (genre BUILD, with a mutant control), run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order
<this order>` after your final commit (rc 0), append a status tag reading complete at the END of this file in the same commit, and
report once: AC1's and AC2's lines and your commit hashes.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling msg 3213 (fix forward with /10, decoupled from team_sheet, which moves to /11). The served half is the issuer's CRPS-at-9: the /10 write with real fitz asserted, under a pair shaped like ar-2, leg v diffing every section of all 95 names against /7 and /9.
<risk>LOCAL</risk>
<status>pending</status>
<round>44</round>
<workstream>D1S2-FIX</workstream>
<slot>~3</slot>
<fabric>dell1</fabric>

<status>complete</status>
