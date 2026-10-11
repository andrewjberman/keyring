# TO IRPT_ANLREQ.TO-AR-y-142 -- the template reader turns back several accounts and a totals row with words; an accepted answer says only the first sheet was read

<to_id>IRPT_ANLREQ.TO-AR-y-142</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the floor of an `infra/` path). BUILD ONLY: nothing is built into a package, uploaded, applied or invoked.
**Decomp cell:** `AR-y-142` (`decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the upload door); TCKT_VNEXT FWD-3 by CTO msgs 5737 and 5849 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you change passes `bash .tools/commit-gate.sh <file>` before its commit.
- **The background for every cell of this round** is one record, read it first:
  `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r13/ONE_ACCOUNT_CHECK_READ.json` (what the upload door does today, run in process on four synthetic sheets), and the CTO's rulings in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_14_20261011.md` section 2. Any sheet you build is SYNTHETIC: made-up tickers (`AAA`, `BBB`), made-up numbers, nothing that looks
  like a real account number or a person. No real uploaded file is ever read.

### THE CELL (`AR-y-142`, inlined) -- BUILD. Nothing is released by this order.

*The template reader turns back a sheet that holds several accounts or a totals row, with words and a row number; and an accepted
answer says only the first sheet was read.*

The lane the form reaches is `infra/aws/lambda/investor-reporting/intake/template_reader.py` (`read_template`; it reads columns A and B of the FIRST sheet), NOT
`parse.py`. Read the reader, its tests (`tests/test_template_reader.py`, `tests/test_template_uploads.py`) and how a finding is
shaped today (code, row, description) before you write anything; match that shape exactly.

**Read first, and report:** the fixture `infra/aws/lambda/investor-reporting/intake/tests/fixtures/holdings/holdings_multi_sheet.xlsx` -- how many sheets, and what
each sheet other than the first holds, by its header cells and row count only.

**The rules (CTO rulings 1, 2 and 5; build exactly these and no other):**
1. **Several accounts, signal one:** a column whose HEADER CELL is on a closed list of account words and which holds TWO OR MORE
   DISTINCT non-empty values. One distinct value (a custodian export repeating one account on every row) is ACCEPTED. The reader
   reads columns A and B today: to see this it must look at the header row's other cells -- look only for that header, keep no
   value of that column in any answer, log, finding or record (a finding names the column letter and that it holds several
   values, never a value). ONE ERROR finding, its own code, with words that say what to do (one account per file).
2. **Several accounts, signal two:** a REPEATED HEADER ROW (the header's own cells appearing again on a later row). ONE ERROR
   finding with the row number of the repeat, its own code, with words.
3. **A totals row:** a row whose label cell (column A) is on a closed list of total words, compared case-insensitively after
   trimming, as a WHOLE cell (never a substring: a fund named "Total Return" is a holding). It is TURNED BACK: an ERROR finding with
   its row number and words that say to remove the row. It is never dropped, summed or compared.
4. **NOT signals (ruled out; a test proves the first):** the same ticker on several rows (tax lots); subtotal-looking rows whose
   label is not on the total list; a label-only line.
5. **A second sheet is not an error.** When the workbook has more than one sheet, the ACCEPTED answer carries one line saying that
   only the first sheet was read and how many others were not. Put it where the reader's answer already carries notes or
   warnings for an accepted sheet (read how; if no such place exists, add ONE member named `sheets_not_read` holding the count,
   and say so in your report). It never turns a sheet back.
6. Findings the reader could already emit keep their codes and shapes. A sheet with BOTH an account finding and a totals finding
   reports both.

**The two closed lists, each with its Rule 24 record** (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r14/CLOSED_LISTS_RULE24.json`):
`{"account_words": {"members": [...], "where_in_code": "<file:line>", "domain": "<what the list is over: header cells, compared how>",
"denominator": "<n> header cells of <m> fixture files", "uncovered_by_subtraction": ["<a header cell found in a fixture that names
an account and is NOT on the list, or empty>"], "deliberately_excluded": [{"word": "...", "why": "..."}]}, "total_words": {same
members}}`. Hunt the uncovered member BY SUBTRACTION: list EVERY distinct header cell (for account words) and EVERY distinct column-A
label that is not a ticker (for total words) across every fixture file under `infra/aws/lambda/investor-reporting/intake/tests/fixtures/` and
`infra/aws/lambda/investor-reporting/ycharts/` test fixtures that hold sheets, print the count, and subtract your list from it; what remains is either excluded
with a reason or added. `Account Type` and `Account Name` are header cells that name no second account by themselves: say how
your list treats them.

**Tests:** one NEW file `infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py`, sheets built in memory the way
`test_template_reader.py` builds them, with functions named exactly:
`test_account_column_with_two_values_is_turned_back_with_words`, `test_account_column_with_one_value_is_accepted`,
`test_repeated_header_row_is_turned_back_with_words`, `test_total_row_is_turned_back_with_its_row_number`,
`test_same_ticker_on_two_rows_is_not_several_accounts`, `test_known_good_sheet_is_accepted`,
`test_accepted_answer_says_only_the_first_sheet_was_read`. Change an existing test only where a rule above forces it, and say which.

In your report: the multi-sheet fixture's read; both lists; the new finding codes and their words; what the reader still cannot
see (stacked tables with no account column and no repeated header; a total with no label) in one sentence each.

### ACCEPTANCE

<criterion id="AR142-y-AC1" cell_refs="AR-y-142"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y142-census --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y142-CENSUS-OK</expect></criterion>
`AR142-y-AC1`: the seven named tests are in the new file and pass, and both closed lists carry their record (members, domain,
denominator, the uncovered members found by subtraction, where in the code).

<criterion id="AR142-y-AC2" cell_refs="AR-y-142"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y142-keep --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y142-KEEP-OK</expect></criterion>
`AR142-y-AC2`: the difference control -- the whole intake test folder passes (292 at the base, plus yours).

<criterion id="AR142-y-AC3J" cell_refs="AR-y-142" judgment="true"/>
`AR142-y-AC3J` (judgment, graded at L9, never by you): the two closed lists are the right ones -- no header or label a one-account
sheet commonly carries is on them, and the words of each finding tell a person what to do.

<expected_criteria>AR142-y-AC1 AR142-y-AC2 AR142-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else. No push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
infra/aws/lambda/investor-reporting/intake/template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_reader.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md</decomp_doc>
<owned_cells>AR-y-142</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR142-y-AC1 AR142-y-AC2 AR142-y-AC3J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-142.template-reader-account-and-totals-findings.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-142`. `AR142-y-AC3J` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with `method`, `invocation`, `denominator` and a `status_reason`
naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR142-y-AC1,AR142-y-AC2,AR142-y-AC3J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 record of round 13 (template_reader.py:71-129 read by its worker; 4 sheets run) and 1 base run of the intake tests (292 passed, 1 skipped); NOT seen by the issuer: the reader's code and the finding shape (the worker reads them first), and which functions package the reader (cell AR-y-145 measures it before any release). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change; nothing is applied.
comp-adversary: RUN -- by reading 5 rulings against the face; the lens: a total word matched as a substring (a fund named Total Return refused), an account column refused on ONE value, or a value of the account column kept in a finding. The face forbids each and a named test covers the first two. NOT seen: a real sheet.
lane: the template reader and two test files, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-14 analysis @1edb90ada7, items 1a and 2, rulings 1, 2 and 5. `AR142-y-AC1` base: FAIL as expected (no test
  file, no record). `AR142-y-AC2` base: PASS as expected (292 passed).
- BUILT, NOT RELEASED: the release is under its own pair (cell `AR-y-145`, then the issuer).
- Seating: slot ~52 is reused; `TO-AR-y-143` queues behind this order in the same slot.
