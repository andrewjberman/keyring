# AMGT_CORPUS task order -- `CRPS-ap-6` -- ROUND 40: a section value that is only its own heading is not a passage (row Z-S89)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ap-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check calls the resolver on hand-built documents.
comp-adversary: RUN by the issuer at the cut -- ap6_check.py build 0/2 control 2/2 (both heading-only fixtures serve "Management/Board 80").
EGRESS CLASS, declared: NONE. The re-write of served dossiers is the issuer's paired act, not yours.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 40.

## 1. THE CELL -- `CRPS-ap-6`

`lib/research/corpus/dossier.py` composes each security's research dossier. Its section fields (company description, ownership,
management, special items, why we own, positives, negatives, and the others in `SECTION_FIELD_NAMES`, about lines 148-169) all go
through `_resolve_section_field` (about 384-396), which takes the block from `_section_block_items` (about 315-358). That block
INCLUDES the section's own lead line, and the only refusal is an empty text (`_resolve_section_block_from_picks`, about 361-377).

The defect (row `AMGT_CORPUS-Z-S89`): when a section's heading is followed at once by the next heading, the block is the heading
alone. Two served dossiers (`8306_JP_Equity`, `8316_JP_Equity`) show "Management/Board 80" (a heading and a score) as the team's
management passage. A heading is not a passage.

**Build, in `dossier.py` only (plus tests):**
1. A section block with NO text beyond its own lead line is not served as a value. Decide "beyond the lead line" from the
   document, not from a length guess: the block has no item after the lead, and what the lead line carries after its section name
   is empty or is not prose (use the lead's `inline_remainder`; a bare number or score such as "80" is not prose; a sentence is).
2. Such a field reads `{"value": None, "absent": <reason>}`, where the reason names the section and the report class and says
   the heading carries no text under it. The case path already does this (`_resolve_case_field`, about 749-797, state
   `heading_only`): reuse its wording and shape where they fit. If class A is heading-only and class B carries a real block, class
   B is served (the existing A-then-B order).
3. A lead with an inline passage ("MANAGEMENT: The CEO has run ...") and a heading followed by body paragraphs are served exactly
   as today, byte for byte.
4. This changes what the dossier writes, so bump `METHOD_VERSION` (about line 144, now `amgt-corpus-dossier/5`) by one and
   satisfy `lib/research/corpus/tests/test_dossier_method_bump.py` the way its own text asks.
5. Add `lib/research/corpus/tests/test_dossier_heading_only_round40.py`: the heading-only docx case, the heading-only pdf case
   (lines, not paragraphs), the A-heading-only-then-B-real case, and the two unchanged cases of point 3.
6. Add a read-only census function and CLI flag `--short-passage-census <N>`: over the newest served dossier of every registered
   name it prints, per section field, how many served values are shorter than N characters, the names and values of each, and the
   denominators (dossiers read, fields read). It writes nothing. You do NOT run it (it reads S3); the issuer does.

## 2. BOUNDS

1. Do not change the recommendation, risks, pillar or case paths, and do not change `_PASSAGE_CAP`.
2. Never run `python -m lib.research.corpus.dossier --write`, and never run the new census (it reads S3).
3. NO push of any branch, NO deploy, NO AWS call, NO Bloomberg call, NO vendor call.
4. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
5. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
6. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
lib/research/corpus/tests/test_dossier.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-ap-6.heading-only-section-is-absent.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ap-6.heading-only-section-is-absent.md
</paths>

Read-only: the whole repository, in particular `lib/research/corpus/extract.py`, `lib/research/corpus/continuation.py`, `lib/research/corpus/tests/test_dossier_case_body.py` and the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap6_check.py` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap6_check.py"</invocation><expect>(?m)^ap6 build 2/2 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest lib/research/corpus/tests/test_dossier.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_heading_only_round40.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1 (the REAL `_resolve_section_field` on four hand-built documents): build -- "Management/Board 80" followed by a bold heading,
  and the same lead followed by the next section's lead, each read value None with an absent reason; control -- an inline passage
  is still served and cited, and a heading followed by a body paragraph still serves the body.
- AC2: the dossier tests, the case-body tests, the method-bump test and your new file pass.

## 5. WHEN YOU ARE DONE

1. Run the pytest files named in AC2 once more after your last edit. Every test passes.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit
   as your instance.
4. Report ONCE: what you changed and where, every criterion's output line, the pytest summary line, your commit hashes and any row.

## 6. AMENDMENT 1 (2026-10-07, the issuer's own; row `AMGT_CORPUS-Z-W2-S21`)

The order asked for a `METHOD_VERSION` bump and left out of `<paths>` three test files that pin the old literal. They are added
to `<paths>` above. The build (commit `763e1e9885`) stands as it is.

**Do, and only this:**
1. In each of `lib/research/corpus/tests/test_dossier_case_body.py` (about line 159), `test_dossier_case_unit.py` (about 110) and
   `test_dossier_case_positional.py` (about 189), change the pinned literal `amgt-corpus-dossier/5` to `amgt-corpus-dossier/6`,
   each with an `AMENDMENT (CRPS-ap-6, round 40):` comment. Change nothing else in those files.
2. Re-run AC1 and AC2. Then run `python -m pytest lib/research/corpus/tests/test_dossier_case_unit.py
   lib/research/corpus/tests/test_dossier_case_positional.py -q -p no:cacheprovider --color=no` and report its last line.
3. Update the proof instance (AC2 now by its real output), run the checker after your final commit, and only if AC1 and AC2
   pass append the status tag reading complete at the END of this file in the same commit as the instance.
4. Your row `AMGT_CORPUS-Z-W2-S21` stays as filed; the issuer disarms it at the drain.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 9 + s.4 item 3; row Z-S89. Base: ap6 build 0/2 control 2/2; the three existing files 25 passed. The served census and the dossier re-write are the issuer's CRPS-ap-10.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
