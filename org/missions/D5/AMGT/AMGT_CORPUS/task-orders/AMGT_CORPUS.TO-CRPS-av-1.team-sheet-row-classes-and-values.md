# AMGT_CORPUS task order -- `CRPS-av-1` -- ROUND 46: the team-sheet reader classes every row and carries the team's own period values (FWD-12 / FWD-20, lib half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-av-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the reader's S3 GETs of stored workbooks are the existing harvest-bucket reads; no new grant, and this order writes nothing.
comp-adversary: RUN by the issuer at the cut on HEAD b67da60663 -- av1_check.py: `av1 build 0/4 control 2/2` at the base, `build 4/4 control 2/2` on a reference implementation (not shipped). Blind spot: the check is a miniature workbook; the 32 real own workbooks are the issuer's /12 write leg.
EGRESS CLASS, declared: NONE beyond Opal's own S3 reads. No Bloomberg, no vendor call, no write to S3.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 46. Your worktree is the absolute path the issuer gives you; work and commit only there.

## 1. THE CELL -- `CRPS-av-1`

Outcome FWD-12 / FWD-20 (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` lines 433-456 and 593-606, read them). The Model tab shows
each name's OWN research-team sheet rows. Measured on the live page, 3210 of 9233 rendered rows are team labels the page cannot show a figure
for, because the reader serves only LABELS. Many are not figure lines at all: the sheet's own header rows ("Year", "Financial Summary") and
control tokens (`BEST_FPERIOD_OVERRIDE`). The ruling: class every row FROM THE SHEET, and carry the team's own period values VERBATIM for
the figure rows, so the page can show them cited as the team's. This cell builds the lib half; a parallel cell (`CRPS-av-2`) renders them.

`lib/research/corpus/team_sheet.py` already reads each name's workbook (bronze, S3 GETs only) and returns
`rows_for(security_key, client=None) -> {"class", "workbook_key", "sheet", "rows", "model_rows_beside", "reason"}`. `dossier.build` calls it ONCE
and stores the result in the gold dossier's `team_sheet` field; the serving API returns that stored field as stored.

**Build, in `lib/research/corpus/team_sheet.py`:**

1. Keep every existing function and its behavior: `sheet_labels(body)`, `rows_for`, `census`, the counting rule (over rows 1-400 and columns
   1-60, a row's LABEL is the first non-empty string in its first 4 cells, and the row COUNTS when it also holds two or more numbers, a bool
   is not a number), the sheet choice, `model_rows_beside`, the newest-workbook rule, `master_absent`. `rows` stays EVERY counted label in sheet
   order, whitespace collapsed.
2. New `sheet_reading(body)` -> `{sheet name: reading}` for each figure-carrying sheet (the same sheets `sheet_labels` returns), where
   `reading` is `{"rows": [label, ...], "row_numbers": [<1-based sheet row>, ...], "row_classes": [...], "periods": [...], "row_values": [...]}`
   all aligned with the counted rows. The rule:
   - **period header:** the first counted row whose numeric cells are ALL integers in 1990..2100, at least 3 of them, strictly increasing by
     column. Its numeric columns are the PERIOD COLUMNS and its numbers the period labels:
     `periods = [{"label": "2016", "column": "E"}, ...]` (label = the integer as text; column = the spreadsheet column letter).
     None found: every counted row is class FIGURE, `periods` is `[]`, every `row_values` entry is None.
   - **a counted row ABOVE the period header** (the info panel): CONTROL when its label is an upper-case identifier with at least one
     underscore (regex `^[A-Z][A-Z0-9]*(_[A-Z0-9]+)+$`), else HEADING.
   - **the period header row itself, and any later row whose numeric cells are all such increasing integer years:** HEADING.
   - **a counted row BELOW the header:** FIGURE when it holds a numeric value in at least one period column; else CONTROL when the label
     has the identifier form, else HEADING. (A numeric cell is an int or float, not a bool. Numbers OUTSIDE the period columns, such as a
     side panel to the right, never make a row FIGURE.)
   - **`row_values[i]`:** None unless row `i` is FIGURE; for a FIGURE row the list of that row's cells in the period columns, in period
     order, VERBATIM as the workbook saved them: a number as the number, a text (for example `#VALUE!`) as that text, a blank as None. A
     date or datetime becomes its ISO text; a non-finite float becomes None. Never rounded, never re-derived.
3. `rows_for` and `census` answers gain, aligned with `rows`, the keys `row_classes`, `row_numbers`, `row_values`, and `periods`, plus
   `row_counts = {"FIGURE": n, "HEADING": n, "CONTROL": n}` (sums to `len(rows)`). A `master_absent` answer carries the same keys empty
   (`[]`, `[]`, `[]`, `[]`, counts 0). The existing keys are untouched.
4. The `--census` CLI keeps its lines and adds, after the class line, `team_sheet row classes FIGURE <f> HEADING <h> CONTROL <c> sum <s> rows <r>`
   over the served names (`s` equals `r`).

**Then, in `lib/research/corpus/dossier.py`:** the stored field is the whole `rows_for` answer, so the new keys flow with no change to `build`.
Bump `METHOD_VERSION` from `amgt-corpus-dossier/11` to `amgt-corpus-dossier/12`, add the comment line `# /12 (CRPS-av-1): team_sheet carries
row classes and the team's own period values.` above it, and update ONLY that literal in the six tests that pin it (listed in `<paths>`).

**Tests** `lib/research/corpus/tests/test_team_sheet_round46.py`: a workbook built in memory with openpyxl covering the period header, each of the
three classes (a panel HEADING, a panel CONTROL, a table CONTROL whose numbers sit only outside the period columns, a repeated year header,
a FIGURE row with a text cell and a blank), `row_values` verbatim, the class counts summing to `rows`, the no-header case, `master_absent`
carrying the keys empty, and `rows` equal to `sheet_labels`.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's checks. No portal file, no `scoped_amgt.py` change (the API serves the stored
   field as stored).
2. NO S3 write, NO deploy, NO push, NO Bloomberg or vendor call. S3 reads for your own testing are allowed.
3. Write code with the Edit/Write tools, never a shell heredoc, sed or `python -c` rewrite. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W1-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`, and
   `surfaced_at` = `date -u +%FT%TZ` at filing.
5. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.
   Your proof instance's `to_id` is this order's FULL id: `AMGT_CORPUS.TO-CRPS-av-1.team-sheet-row-classes-and-values`.

## 3. SURFACES

<paths>
lib/research/corpus/team_sheet.py
lib/research/corpus/tests/test_team_sheet_round46.py
lib/research/corpus/tests/test_team_sheet_round44.py
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-av-1.team-sheet-row-classes-and-values.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-av-1.team-sheet-row-classes-and-values.md
</paths>

Read-only: the whole repository, in particular `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round46/av1_check.py`.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-av-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round46/av1_check.py" 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^av1 build 4/4 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-av-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_team_sheet_round46.py lib/research/corpus/tests/test_team_sheet_round44.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py lib/research/corpus/tests/test_dossier_heading_only_round40.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-av-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c '^METHOD_VERSION = "amgt-corpus-dossier/12"$' lib/research/corpus/dossier.py</invocation><expect>(?m)^1$</expect></criterion>
</proof_of_spec>

- AC1: the three classes, the counts summing to the rows, the values verbatim, the periods, with `rows` and `sheet_labels` unchanged.
- AC2: your tests and the six method-pinning tests pass (every one of them reads `/12`).
- AC3: the method literal is `/12`.

## 5. WHEN YOU ARE DONE

1. Run `python -m lib.research.corpus.team_sheet --census` if the store is reachable and put its two summary lines in your report; if it is
   not reachable, say so.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1-AC3 pass, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
4. Report ONCE: the change, AC1's line, AC2's line, AC3's line, the census lines (or why not), your commit hashes, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-45 analysis item 1 and ADDENDUM 1 (msg 3846): Bloomberg first where the block carries the field; else the team's own cell verbatim, cited, labelled "team model"; else a PM-worded why; NO label-to-field map. The rule is the issuer's reading of round-44 ADDENDUM 1, measured on the 32 own workbooks (3759 rows = FIGURE 3353, HEADING 344, CONTROL 62; period header in 32 of 32). Base at the cut: AC1 FAIL (`build 0/4`), AC2 FAIL (the new test file is absent), AC3 FAIL (the literal reads /11). The /12 dossier write (av-3) and the API redeploy (av-4) are SEPARATE paired acts after this drains.
<risk>LOCAL</risk>
<status>pending</status>
<round>46</round>
<slot>~1</slot>
<fabric>dell1</fabric>
<status>complete</status>
