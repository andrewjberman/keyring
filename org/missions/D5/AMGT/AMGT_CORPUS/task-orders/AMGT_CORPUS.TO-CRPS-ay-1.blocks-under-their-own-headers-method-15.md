# AMGT_CORPUS task order -- `CRPS-ay-1` -- ROUND 49: every value is served under the header of its own block -- period grids, case tables, an unread block with a why (FWD-20, lib half; method /15)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ay-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy, role or credential changes; tests use an in-memory workbook only. AC2 reads four stored workbooks (S3 GET) through the existing reader.
comp-adversary: RUN by the issuer at the cut -- ay1_check.py: `ay1 build 0/4 control 2/2` at the base (every build arm fails, both controls pass), `build 4/4 control 2/2` on the issuer's reference reader (the file named below); the live seam line reads `block_names 0/4` at the base and the pinned line on the reference. Blind spot: fixtures are miniature workbooks and four real names; the 95 stored dossiers are the issuer's /15 write leg.
EGRESS CLASS, declared: NONE. No S3 write, no Bloomberg or vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 49. Your worktree is the absolute path the issuer gives you; work and commit only there.
It is cut from the branch after round 48 closed: `lib/research/corpus/team_sheet.py` is blob `3ba68a99a22f` and `lib/research/corpus/dossier.py` is blob `6c4529c51a13`
(`git rev-parse HEAD:<path>`; if either differs, STOP and file a BLOCKING row), and `METHOD_VERSION` is `/14`.

## 1. THE CELL -- `CRPS-ay-1`

Outcome FWD-20 (a figure on every row, in words). The Model tab's team rows are the sheet's rows aligned to the sheet's ONE period header. A team sheet is not one grid: below the main grid
it carries other tables that have their OWN header rows (a second table headed by years 2026..2030; three scenario tables side by side headed `Upside Case | Base Case | Downside Case`
with years under each; a lone `Average` row with no header). Read under the main header they print a value under a year that is not its year (ROG SW prints "Price $660.45" under 2016).
The issuer's read of the stored workbooks (nothing written): this sits on all 32 own sheets and all 63 master templates, 3,103 rows, and outside those rows no label, number or value moves.

**The CTO's principle (round-48 analysis ADDENDUM 1, msg 4165):** every value renders under the header row of ITS OWN BLOCK, as the sheet wrote it. A block whose header names
periods (any years, quarters or `E` forms) is a PERIOD grid aligned to THAT block's periods and is never made a "case table", even when its years differ from the main grid's. A block whose
header names non-period words is a CASE table under those words. A block whose header the reader cannot read stays out of both, with a why (kind UNREAD).

**What you build is already written.** The issuer's reference implementation is the file
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay1_reference_team_sheet.py.txt`: it is the base `team_sheet.py` with the change applied
(221 insertions, 10 deletions). It adds `ROW_BLOCK = "BLOCK"`, the period-label parser (`_period_key`, `_header_runs`), `_block_rows` (which counted rows are BLOCK rows),
`_blocks` (the block bands, kinds and cells), reads every raw row beside the counted rows (`_raw_rows`, `_figure_sheets_raw`), and carries `blocks` and the BLOCK count into the
answer. **The served shape is exactly decomposition v49.1 section 1** (read it: `org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md`): a BLOCK row has
`row_classes[i] == "BLOCK"` and null `row_values[i]` and `row_formats[i]`; `row_counts` gains `"BLOCK"` only when there is one; `blocks` is present only when there is a BLOCK row and
each block carries `first_row`, `last_row`, `kind` (`period` | `case` | `unread`), `why`, `withheld`, `columns`, `rows`. A name with no BLOCK row serves its answer unchanged, key for key.

**Build:**

1. `lib/research/corpus/team_sheet.py`: copy the reference file over it (`cp`), then `git diff --stat` must show this one file with about 221 insertions and 10 deletions. Read the diff.
   Change no behaviour. (Comments may be improved; the reading rules for FIGURE, HEADING, CONTROL, the labels and the formats stay byte-for-byte what they were.)
2. The same file's module docstring: add a paragraph `THE BLOCKS (AMGT_CORPUS round 49, CRPS-ay-1, FWD-20, CTO round-48 ADDENDUM 1):` after the `THE LABELS AND FORMATS` paragraph
   stating, in your own words and in at most 16 lines: what a BLOCK row is (the two tests), the three kinds, that the served `blocks` list carries the sheet's own header rows and
   cells verbatim, that an UNREAD block carries no cell and a why, and that a master answer carries no figure.
3. The census CLI (`_main`): when at least one entry has a BLOCK row, the `team_sheet row classes` line reads
   `team_sheet row classes FIGURE %d HEADING %d CONTROL %d BLOCK %d sum %d rows %d` (BLOCK before `sum`; the total over `entry["row_counts"].get("BLOCK", 0)`; `sum` includes it), and a further
   line `team_sheet blocks period %d case %d unread %d withheld %d` follows it (BLOCK rows per block kind, and the withheld cells, over every entry). When no entry has a BLOCK row the
   output is byte-for-byte what it is today (two existing tests pin it).
4. `lib/research/corpus/dossier.py`: the literal becomes `METHOD_VERSION = "amgt-corpus-dossier/15"`; replace `amgt-corpus-dossier/14` with `amgt-corpus-dossier/15` in the six test
   files in `<paths>` that pin it (`test_dossier_method_bump.py` has three occurrences).
5. New tests in `lib/research/corpus/tests/test_team_sheet_round49.py`, with in-memory openpyxl workbooks (the issuer's check `checks/round49/ay1_check.py` builds four fixture workbooks
   you may read and reuse in shape; do not import from it): (i) a row whose values sit under a second year header is a BLOCK row; (ii) a row with a letter-text cell in a period column is a
   BLOCK row; (iii) a row holding only `NA`, `#N/A` and a range string stays FIGURE and makes no block; (iv) a block with two title cells and a year row is `case`, a block with only a year row
   (integer years, or `1Q26`..`4Q26`) is `period`, a header-less one-row block is `unread` with `columns == []`; (v) a numeric cell under no header of its block is null and counted in `withheld`;
   (vi) a `master` answer keeps the BLOCK class and blocks and carries no numeric cell outside a header run; (vii) a sheet with no block has no `blocks` key and `row_counts` has exactly the
   three round-46 keys.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's checks, snapshot or reference. No portal file, no `scoped_amgt.py`.
2. NO S3 write, NO deploy, NO push, NO Bloomberg or vendor call.
3. Write code with the Edit/Write tools (`cp` for step 1 only), never a shell heredoc, sed or `python -c` rewrite. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W1-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`, and `surfaced_at` = `date -u +%FT%TZ` at filing.
5. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`; the commit gate runs `ruff` (py39) on the
   `.py` files. Your proof instance's `to_id` is this order's FULL id: `AMGT_CORPUS.TO-CRPS-ay-1.blocks-under-their-own-headers-method-15`.

## 3. SURFACES

<paths>
lib/research/corpus/team_sheet.py
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_team_sheet_round49.py
lib/research/corpus/tests/test_team_sheet_round44.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ay-1.blocks-under-their-own-headers-method-15.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ay-1.blocks-under-their-own-headers-method-15.md
</paths>

Read-only: the whole repository, in particular the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay1_check.py` and its
`ay1_base_snapshot.json`, and the reference `ay1_reference_team_sheet.py.txt` beside them.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ay-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay1_check.py" 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^ay1 build 4/4 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ay-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay1_check.py" --live ROG_SW_Equity BABA_US_Equity AZN_LN_Equity TSM_US_Equity 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^ay1 live block_names 4/4 block_rows 108 split period 15 case 91 unread 2 split_ok true text_separator_rows_left 0 headerless_values 0$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ay-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_team_sheet_round49.py lib/research/corpus/tests/test_template_round47.py lib/research/corpus/tests/test_team_sheet_round47.py lib/research/corpus/tests/test_team_sheet_round46.py lib/research/corpus/tests/test_team_sheet_round44.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py lib/research/corpus/tests/test_dossier_heading_only_round40.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-ay-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c '^METHOD_VERSION = "amgt-corpus-dossier/15"$' lib/research/corpus/dossier.py</invocation><expect>(?m)^1$</expect></criterion>
</proof_of_spec>

- AC1: the fixtures: a row under a second header and a row with a label cell are BLOCK rows; `NA`, `#N/A` and a range stay FIGURE; case / period (integer years, and `1Q26`..`4Q26`) / unread
  kinds; a value under no header of its block is withheld; a master answer carries no figure; a sheet with no block is unchanged key for key and the non-BLOCK rows of a sheet with blocks
  equal the base's.
- AC2: four real stored workbooks (ROG SW own_model, BABA and AZN LN own_new, TSM US master): every one has BLOCK rows and blocks; the split is 15 period + 91 case + 2 unread = 108;
  no FIGURE row still carries a text separator; no value sits under a header that is not its block's own.
- AC3: your tests, round 47's, 46's and 44's, and the method-pinning tests pass (every one of them reads `/15`).
- AC4: the method literal is `/15` (a fourth criterion: the stored-object version is its own outcome).

## 5. WHEN YOU ARE DONE

1. Run `python -m lib.research.corpus.team_sheet --census` (read only; if the store is not reachable, say so) and put its `row classes`, `blocks` and `labels` lines in your report.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>`
   AFTER your final commit; rc 0. WITHHOLD the order's complete tag: the issuer flips it after re-running the criteria.
3. Report ONCE: the change, AC1's to AC4's lines, the census lines, your commit hashes, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-48 analysis (msg 4158) and ADDENDUM 1 (msg 4165): full width confirmed, three kinds, "the 3,103 split three ways with the denominator" (this cell's
`blocks` carry it; the issuer's census prints it: `evidence/r49_block_split_census_20261011.txt`: period 401, case 2,690, unread 12 over 12,264 rows; own 86 / 611 / 12, master 315 / 2,079 / 0;
357 blocks; 35 withheld cells; 0 headerless values; 0 names with any other change). The /15 write (its own pair, `CRPS-ay-3`) and the redeploy carrying /15 or /14 follow. Reference reader
dry-run: AC1 `build 4/4 control 2/2`, AC2 the pinned line, AC3 145 passed with the pins bumped (a throwaway worktree), ruff clean. Base at the cut: AC1 FAIL (`build 0/4`), AC2 FAIL (`block_names 0/4`),
AC3 FAIL (the new test file does not exist yet), AC4 FAIL (the literal reads /14).
<risk>LOCAL</risk>
<status>pending</status>
<round>49</round>
<slot>~1</slot>
<fabric>dell1</fabric>
