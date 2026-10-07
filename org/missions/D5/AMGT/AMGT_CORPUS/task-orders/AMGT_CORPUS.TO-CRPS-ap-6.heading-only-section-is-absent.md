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
  <criterion id="AC1" cell_refs="CRPS-ap-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap6_check.py"</invocation><expect>(?m)^ap6 build 6/6 control 3/3$</expect></criterion>
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

## 7. AMENDMENT 2 (2026-10-07, the issuer's own; the census on the served dossiers and the CTO's ruling)

The build and AMENDMENT 1 are merged and are your INHERITED STATE (they are in your worktree's HEAD): a heading-only section
reads absent, `METHOD_VERSION` is `amgt-corpus-dossier/6`, and `--short-passage-census <N>` exists. NO dossier has been written
at `/6`, so do NOT bump the version again.

The issuer ran the census on the served dossiers (`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/
r40_ap10_short_passage_census_20261007.txt`: 95 dossiers, 950 fields, 49 served values are a bare heading) and read the source
document behind five of them (`.../evidence/r40_ap10_heading_context_20261007.txt`, read both files). In two of the five the
prose IS in the report and `_section_block_items` stops before it: TSM's "Positives" (the heading, a "-" line, then prose) and
AstraZeneca's "MANAGEMENT:" (the heading, "Sir Pascal Soriot CEO", then prose). The block reader ends a block at an unnamed
short or bold heading-like item (docx: a bold paragraph of at most `extract._HEADING_WORD_CAP` words; pdf:
`continuation._pdf_is_standalone_heading` and not lead-only), and here that item is the FIRST item under the section's own lead.
With the build as landed these two would read "heading carries no text under it", which the report contradicts.

**Ruled by `1.0.0_SA_CTO~Z`: the item directly after a section's lead never ends the block.** Do, and only this:
1. In `_section_block_items` (docx and pdf branches): an UNNAMED heading-like item at the position directly after the lead does
   not end the block; the scan goes on from the item after it. A NAMED section lead (an index in `lead_indices`) still ends the
   block wherever it is, including directly after the lead. Every later unnamed heading-like item ends the block as today.
2. The absent reason tells two cases apart (the CTO's term 2). When the extraction shows a TABLE follows the heading and no
   prose does, the reason says so in words (a table follows the heading and no prose does); it does not say the section is
   empty. Use what the stored extraction actually carries to tell (read `lib/research/corpus/extract.py` for how tables and
   empty paragraphs are represented; the Imperial Brands and Mitsubishi UFJ shapes are in the context evidence file). Where the
   extraction cannot tell a table from nothing, the reason says no prose follows the heading in the report's extracted text.
   Never "no text" where the document shows a table.
3. Add a read-only CLI flag `--section-recompose-census`: for every registered name it re-composes the section fields IN MEMORY
   from the stored extractions with the current code and compares each with the SERVED dossier's value. It prints one line per
   (name, field) whose value differs: the name, the field, the first 70 characters of the served value and of the re-composed
   value (or `ABSENT: <reason>`); then the denominators (names read, fields compared, fields changed, and of the served values
   under 40 characters how many gain prose, how many read absent with the table reason, how many with the no-prose reason). It
   writes NOTHING and makes no put. You do NOT run it (it reads S3); the issuer does.
4. Tests in `lib/research/corpus/tests/test_dossier_heading_only_round40.py`: the docx bold-first-item case; the pdf case BUILT
   FROM THE REAL PREDICATE (construct lines that `continuation._pdf_is_standalone_heading` really flags for the first item, and
   assert the flag in the test, so the case cannot pass by not being flagged); a named lead directly after the lead still ends
   the block; a second unnamed heading still ends it; the two reason wordings; the recompose census on stub documents.

**Prove** AC1 (now `ap6 build 4/4 control 2/2`: arm b3 is the docx bold-first-item case, b4 a pdf dash case) and AC2 by their
invocations in section 4. Then section 5 again: the proof instance updated, the checker after your final commit, and the status
tag reading complete appended at the END of this file only if AC1 and AC2 pass.

## 8. AMENDMENT 3 (2026-10-07, the issuer's own; the after-census)

AMENDMENT 2 is merged and is your INHERITED STATE (in your worktree's HEAD): the item directly after a section's lead no longer
ends the block, the two absent reasons exist, and `--section-recompose-census` exists. The issuer ran that census on the served
dossiers (`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/
r40_ap10_section_recompose_census_20261007.txt`, read it whole): 95 names, 950 fields, 51 changed; of the 49 served bare
headings it counts 41 as gaining prose. 17 of those 41 are NOT prose: ten `special_items` read "Special items: 4_30_2026 5
Supporting documentation: Business model" (a page header, a page number and the next unnamed headings), and seven
`comparison_set` read "COMMON STOCK COMPARISON 6/23/2026" or "... P/E" (a table's date or column header). Your row
`AMGT_CORPUS-Z-W2-S23` named this class. The other 24 are real (positives, negatives, two management, one special items).

**The issuer's rule, and only this:**
1. A section block is served as a passage only when its items AFTER the lead line carry prose: at least one item with more than
   `extract._HEADING_WORD_CAP` words, OR 25 or more words in all across those items (so a section of short bullet lines is still
   served). An inline remainder on the lead line that is itself prose (the existing `_is_prose` test) still serves, as today.
   Count words on the item text as extracted; do not strip bullets or punctuation first.
2. A block that fails that test reads absent with the reasons AMENDMENT 2 made (table, or no prose). Class B is still tried after
   a class A that fails it.
3. `--section-recompose-census` also prints, for the served values under 40 characters, the three counts as now, and for every
   changed field that is NOT one of those 49 a line marked `OTHER-CHANGE` (one exists today: CLX company description), so a
   change outside the bare headings cannot hide in the total.
4. Tests in `test_dossier_heading_only_round40.py`: the page-furniture pdf case and the date-only docx case read absent; a
   section of six short bullet lines (none over the cap, 25 or more words in all) is served; the two cases of AMENDMENT 2 still
   pass. `METHOD_VERSION` stays `/6`.

**Prove** AC1 (now `ap6 build 6/6 control 3/3`: b5 the page-furniture case, b6 the date-only case, c3 the bullets control) and AC2
by their invocations in section 4. Then section 5 again: the proof instance updated, the checker after your final commit, and the
status tag reading complete appended at the END of this file only if AC1 and AC2 pass.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 9 + s.4 item 3; row Z-S89. Base: ap6 build 0/2 control 2/2; the three existing files 25 passed. The served census and the dossier re-write are the issuer's CRPS-ap-10.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
<status>in_progress</status>
<status>complete</status>
<status>in_progress</status>
<status>complete</status>
