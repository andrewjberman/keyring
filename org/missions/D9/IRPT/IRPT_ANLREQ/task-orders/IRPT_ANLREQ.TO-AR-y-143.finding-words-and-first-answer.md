# TO IRPT_ANLREQ.TO-AR-y-143 -- every finding code has words; the door's first answer carries what the POST can decide

<to_id>IRPT_ANLREQ.TO-AR-y-143</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the floor of an `infra/` path). BUILD ONLY: nothing is built into a package, uploaded, applied or invoked.
**Decomp cell:** `AR-y-143` (`decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the upload door); TCKT_VNEXT FWD-3 by CTO msgs 5737 and 5849 | **depends_on:** `AR-y-142` merged (the same slot, the codes it emits)

**NOT SPAWNED AT ISSUANCE.** The issuer spawns this order when `TO-AR-y-142` is terminal and merged into this slot's branch.

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

### THE CELL (`AR-y-143`, inlined) -- BUILD. Nothing is released by this order.

*Every finding code the reader can emit has words; the door's FIRST answer carries what the POST can decide.*

**Inherited state:** cell `AR-y-142` (this slot, already merged into your branch) added finding codes to
`infra/aws/lambda/investor-reporting/intake/template_reader.py`; its report and `r14/CLOSED_LISTS_RULE24.json` name them. Read them from the code, not from memory.

1. **Words (CTO ruling: "words for every finding code the form can show").** `CORRECTION_WORDS` in `infra/aws/lambda/investor-reporting/intake/uploads.py` (about
   line 58) gives words for 4 codes; every other finding reaches the person as a raw code. Make the list complete: EVERY finding
   code `template_reader.py` and `portfolio.py` (the findings built at about line 496) can put in an upload answer has one plain
   sentence that says what is wrong and what to do, in the style of the four that exist. Derive the set of codes from the code
   (every string a finding's `code` can take; say how you enumerated them and print the count), never from a list you remember.
   If the words for a code live in `infra/aws/lambda/investor-reporting/ops/status.py` (read how the upload answer's description is filled), edit them there: that
   file is in your grant for a WORDS-ONLY edit -- change no logic, no key, no code value in it.
2. **The first answer (CTO ruling 4).** Today the POST answers RESOLVING for every sheet and the findings arrive only after the
   resident step, so a person sees a refusal on a second press. A finding that needs NO pricing and NO provider -- the reader's own
   findings: the account column, the repeated header, the totals row, and every finding `read_template` itself raises today -- is
   decided at the POST: when the reader returns any ERROR finding, the door's FIRST answer is the NEEDS_CORRECTION answer with
   those findings and their words, and nothing is handed to the resident for that upload. Read `UploadService.create`
   (`uploads.py` about line 240) and `resolve_deferred` (about line 423) to see where the reader runs today; if it already runs at
   the POST and its findings are simply withheld, return them; if it runs only in the resident, run it at the POST as well and say
   what that costs (the file is read twice?) in your report.
3. **Unchanged:** a sheet with no reader finding still answers RESOLVING first and is priced and ticker-checked later exactly as
   today. Do not move pricing or the ticker check to the POST. Do not change what an ACCEPTED (NORMALIZED) answer is, other than
   the first-sheet line cell `AR-y-142` added.
4. **Tests,** in `infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py` (existing; keep its tests) and, where the door is exercised,
   `tests/test_template_uploads.py`: functions named exactly `test_every_finding_code_the_reader_can_emit_has_words` (it enumerates
   the codes from the code and fails on one with no words), `test_post_decidable_findings_arrive_on_the_first_answer`,
   `test_a_sheet_that_needs_pricing_still_answers_resolving_first` -- all three in `test_correction_words.py`.
5. In your report: the count of finding codes and how enumerated; the words added; whether the reader now runs once or twice per
   upload; every existing test whose expectation changed and why; whether any caller other than the form reads the POST's first
   answer (search `infra/aws/lambda/investor-reporting/` for callers of the create path and say what you found -- the release census reads this).

---

**SPAWN AMENDMENT (AMENDMENT 1, issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~21:5xZ): `TO-AR-y-142` is terminal and merged (@87202fbaed);
what it built, which this cell builds on.** Gate limb that graded this amendment: read from this commit's own output.

- **Four new finding codes** in `infra/aws/lambda/investor-reporting/intake/template_reader.py`, each carrying its words in a NEW
  optional `description` member on the finding itself: `ACCOUNT_COLUMN_SEVERAL_VALUES` (ERROR), `HEADER_ROW_REPEATED` (ERROR),
  `TOTAL_ROW_PRESENT` (ERROR), `SHEETS_NOT_READ` (NOTICE, on an ACCEPTED sheet: it never turns a sheet back).
- **Their words live in `template_reader.WORDS`** (row `IRPT_ANLREQ-D2-W52-S13`), because `CORRECTION_WORDS` was outside that cell's
  grant. **There must be ONE source of words per code.** For these four, `uploads.py` takes the words from the finding's own
  `description` (or from `template_reader.WORDS`) -- do NOT write a second copy of the sentences in `CORRECTION_WORDS`. Say in your
  report which way you wired it, and make `test_every_finding_code_the_reader_can_emit_has_words` pass a code whose words come
  from EITHER source, and FAIL a code with words in neither.
- **Item 2's "any ERROR finding" means severity ERROR.** A NOTICE (`SHEETS_NOT_READ`, the existing `DUPLICATE_SYMBOL_MERGED`) never
  makes the first answer NEEDS_CORRECTION; a sheet with only NOTICE findings goes on to RESOLVING as today.
- A repeated header row ALSO still emits its older `AMOUNT_NOT_A_NUMBER` finding for that row, and a totals row stays in the
  reader's rows: nothing is dropped. Both findings reach the person; do not suppress either.
- One existing test changed in that cell (`test_template_reader.py::test_prefer_named_sheet_other_sheets_and_columns_ignored` now
  expects one `SHEETS_NOT_READ` NOTICE). The intake folder passes 299 at this base (the keep check's floor of 292 still holds).
- **For your report, because the release census reads it:** the reader runs in TWO places -- the `irpt-ycharts-generate` Lambda (the
  POST half) and the resident process on the runner host (cell `AR-y-141`'s record,
  `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/TOTAL_LABEL_PROVIDER_ASK.json`). Say which of the two
  your first-answer change runs in, and whether the resident's later answer for the same upload can now differ from the POST's.

---

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~22:1xZ): the issuer rules on row `IRPT_ANLREQ-D2-W52-S14`. ONE more test file
joins the grant; the stop was right.** The earlier seating's commits (`4215d98f26`, `ce85146d30`, `c2e0a95500`, `d92664d6fc`) are
inherited state: `AR143-y-AC1` passes; `AR143-y-AC2` fails on exactly one test,
`tests/test_deferred_resolution.py::test_refusal_is_written_by_name_and_answered_with_findings`, which posts a sheet the READER
refuses (`AAPL,bad`) and expects the first answer RESOLVING and a resident run afterwards. That expectation is what this cell
changes on purpose (CTO ruling 4): a reader ERROR is now the POST's own answer and nothing goes to the resident.

- **`infra/aws/lambda/investor-reporting/intake/tests/test_deferred_resolution.py` is added to `<paths>`** for this ONE test only.
- **Keep what the test proves, do not delete it.** Its subject is the RESIDENT's path: a refusal the resident makes is written by
  name and answered with findings. So: change the test's sheet to one the reader ACCEPTS and the resident REFUSES (the earlier
  seating named `MISSING,10` -- a symbol the provider stub does not find; confirm it), so the test still walks POST = RESOLVING,
  then the resident, then the refusal written by name with findings. Keep its name and every assertion that still describes that
  path; change only the sheet and what the sheet forces.
- **Add ONE test beside it,** `test_a_reader_refusal_is_answered_at_the_post_and_never_reaches_the_resident`, with the OLD sheet
  (`AAPL,bad`): the POST's first answer is NEEDS_CORRECTION with the reader's finding, and NOTHING is published or handed to the
  resident (assert on the same fakes the file's other tests use for the queue or publisher).
- Change no other test in that file. If another test there fails after your change, STOP and file a row.
- Then both criteria again, verbatim; a fresh proof instance at the same path; flip `<status>` to `complete` on VALID.
- **Read by the issuer, for the record:** `ops/tests/test_status.py` fails 14 of 23 at the BASE too (`ModuleNotFoundError: No module
  named 'submission'`; the issuer's run on the shared tree before your change): not yours, not in this order.
- **Noted for the release census, not for you to change:** your words table made `build_envelope` add a CORRECT action when a
  NEEDS_CORRECTION reason is one of the 24 codes that gained words. That is a change to a SERVED answer that came from a
  words-only edit; the census (cell `AR-y-145`) names every reader of it. Say in your report exactly which envelope member changes
  and for which reasons.
- Gate limb that graded this amendment: read from this commit's own output.

### ACCEPTANCE

<criterion id="AR143-y-AC1" cell_refs="AR-y-143"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y143-words --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y143-WORDS-OK</expect></criterion>
`AR143-y-AC1`: the three named tests are in `test_correction_words.py` and the file passes.

<criterion id="AR143-y-AC2" cell_refs="AR-y-143"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y142-keep --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y142-KEEP-OK</expect></criterion>
`AR143-y-AC2`: the difference control -- the whole intake test folder passes.

<expected_criteria>AR143-y-AC1 AR143-y-AC2</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else. No push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/ops/status.py
infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_uploads.py
infra/aws/lambda/investor-reporting/intake/tests/test_deferred_resolution.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md</decomp_doc>
<owned_cells>AR-y-143</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR143-y-AC1 AR143-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-143.finding-words-and-first-answer.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-143`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR143-y-AC1,AR143-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 record of round 13 (uploads.py:58 CORRECTION_WORDS with 4 codes; :240 create; :423 resolve_deferred; every first answer RESOLVING on 4 of 4 sheets); NOT seen: every caller of the create path other than the form (the worker searches and reports; cell AR-y-145 reads each before any release). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: RUN -- by reading 1 lane resolution: `owned-paths-validate.py --check-path 2.0.0_SA_COO~Y2 .../ops/status.py` prints PERMIT, lane IRPT_COMPLETION_Y; the worker's grant is this order's <paths>. No permission is changed.
comp-adversary: RUN -- by reading 1 ruling (ruling 4) against the face; the lens: pricing or the ticker check dragged to the POST, or a first answer that changes for a GOOD sheet. The face forbids both and a named test holds the second. NOT seen: whether a caller other than the form depends on the first answer always being RESOLVING.
lane: uploads.py, a words-only edit to ops/status.py, two test files, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-14 analysis @1edb90ada7, items 3 and 4 (service half), rulings 3 and 4. `AR143-y-AC1` base: FAIL as
  expected (the three named tests absent). `AR143-y-AC2` base: PASS as expected (292 passed).
- NOT SPAWNED AT ISSUANCE: spawned when `TO-AR-y-142` is terminal and merged (the same slot's queue).
- BUILT, NOT RELEASED.
