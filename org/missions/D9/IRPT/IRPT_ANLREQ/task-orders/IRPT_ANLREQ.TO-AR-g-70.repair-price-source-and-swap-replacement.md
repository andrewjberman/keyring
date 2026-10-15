# TO-AR-g-70 -- the round-7 repair cell: close the four gaps the builders of price_source.py and swap_replacement.py observed (bare string symbols, calendar-impossible dates, a classify error, a ticker with two classes)

<to_id>IRPT_ANLREQ.TO-AR-g-70</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~177</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-70` (`decompositions/IRPT_ANLREQ_DECOMP_R9_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** `AR-g-51` (merged `e8f1f82f2b`) and `AR-g-52` (merged `35cdaff302`).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~177`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-177` (branch `wk-IRPT_ANLREQ-177`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~177 <0.9.0_WK_IRPT_ANLREQ~177@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W177-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you edit passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.

### Read first (under `C:/dev/wk-irpt-anlreq-177/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `price_source.py` and `swap_replacement.py` (whole; both are short), and their test files under `tests/`. The module contracts stay exactly as they are except where this cell changes them.

### THE CELL (`AR-g-70`, inlined)

The builders of the two modules filed four observations (rows `IRPT_ANLREQ-D2-W170-S1`, `S2` and `IRPT_ANLREQ-D2-W171-S1` in
`org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`). The issuer rules them as defects to repair now, before a compose cell imports the modules.
Edit the two existing files. Do not rewrite them; do not change any behaviour the round-7 checks already pin (they must still pass).

**`price_source.py`, `resolve_prices`:**
1. `symbols` that is a `str` or `bytes`, or is not iterable (None, a number), raises `ValueError("PRICE_SYMBOLS")` (a bare string was iterated per character). A list, tuple, set or generator is still accepted.
2. A date is valid only if it matches the `YYYY-MM-DD` pattern AND is a real calendar date (`datetime.date.fromisoformat` accepts it). `start`, `end`, `as_of` that are not valid
   raise `ValueError("PRICE_WINDOW")`; so does `start` later than `end`. A reader's row whose date is not a real calendar date (e.g. `2026-02-30`) is dropped like any other bad row.
   (`datetime` may now be imported; the allowed import set becomes `math`, `re`, `datetime`, `collections`, `typing`, `__future__`.)

**`swap_replacement.py`, `choose_replacement`:**
3. An exception raised by `classify(ticker)` is caught: the proposal is dropped with reason `"NOT_CLASSIFIED"`, the exception message is NEVER in the result, and the rest of the run continues.
4. A ticker that appears on two or more `pool_rows` with DIFFERENT classes (after stripping and `casefold()`) is ambiguous: it is never a candidate, and it is listed in `dropped` exactly once with
   reason `"CLASS_AMBIGUOUS"`; a model proposal naming such a ticker is dropped the same way (once). A ticker repeated on pool rows with the SAME class is one candidate, as before.

**Tests.** Add tests for items 1-4 to the two existing test files (`tests/test_price_source.py`, `tests/test_swap_replacement.py`); at least 4 new tests in all.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR70-g-AC1" cell_refs="AR-g-70"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g70_checks.py repair</invocation><expect>^AR-G70-OK</expect></criterion>

<criterion id="AR70-g-AC2" cell_refs="AR-g-70"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g70_checks.py regress</invocation><expect>^AR-G70-REGRESS-OK</expect></criterion>

<expected_criteria>AR70-g-AC1,AR70-g-AC2</expected_criteria>

- AC1 asks the two modules ten cases that pin items 1-4 (the repaired behaviour). At base it FAILs.
- AC2 re-runs the four round-7 checks (`ar_g51_checks.py g51` and `hygiene`, `ar_g52_checks.py g52` and `hygiene`); each must still print its OK line. The `hygiene` arms hold the import set above: if you import `datetime`, the `ar_g51_checks.py` allowed set must admit it, so
  check the allowed set first; it already admits `datetime`. At base it PASSes (it guards that nothing existing breaks).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_source.py
infra/aws/lambda/investor-reporting/ycharts/research/swap_replacement.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_source.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_replacement.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~177/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-70.repair-price-source-and-swap-replacement.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R9_G.md</decomp_doc> round 9, workstream ~G, cell `AR-g-70`.
<owned_cells>AR-g-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR70-g-AC1, AR70-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~177/IRPT_ANLREQ.TO-AR-g-70.repair-price-source-and-swap-replacement.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-70`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR70-g-AC1,AR70-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines changed in each module;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- both modules are merged and imported by nothing yet (the compose cell is a later round), so no deployed edge changes. Nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read the four observations. Traps: a repair that changes a behaviour the round-7 checks pin (the regress arm catches it); an exception message leaking from `classify`; an ambiguous ticker counted once as a candidate and once as dropped; a calendar check that rejects a valid leap day. The checker feeds a green arm (a repaired reference passes all ten cases) and a base arm (the merged modules fail them). NOT seen (blind): real classifications.
</preflight>

- Cut on the three observation rows of round 7. Risk WORLD: the floor of an infrastructure path; source and tests only. Base: `AR70-g-AC1` FAILs as expected; `AR70-g-AC2` PASSes as expected.
