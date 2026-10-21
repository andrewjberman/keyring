# TO-AR-g-183 -- the resident's retained_for_retry line carries a lead token for our own refusal classes (CTO msg 11890 item 2)

<to_id>IRPT_ANLREQ.TO-AR-g-183</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~356</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL6</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-183` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** CTO msg 11890 item 2. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~356`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-356` (branch `wk-IRPT_ANLREQ-356`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~356 <0.9.0_WK_IRPT_ANLREQ~356@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W356-S<k>` (check the channel file for `W356` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_reason_checks.py` (read it; you cannot edit it, and you cannot edit its fixture). It builds its own inputs and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-183`, inlined)

**What this cell is.** The resident's journal line for a failed poll is `IRPT_RESIDENT_POLL retained_for_retry class=<Class> code=<code>`, built by `retained_reason` in `infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py`. It prints the exception's message only when the message is itself a closed code (an upper-case token), so the sentence messages of our own refusal classes print `code=-` and the cause of a stop can only be found by replaying the composition offline (run 7I: `class=RecipeRefused code=-` three times). The CTO asked (msg 11890) that the line carry the refusal's leading constant words in place of nothing. The same function builds the `IRPT_RESIDENT_PACKAGE` line.

**The rule `retained_reason(exc)` must follow (exact; the checker holds it to 14 cases).**
- A message that is a closed code (it fully matches the existing `_CODE` pattern) prints exactly as today: `class=X code=CODE`, nothing else.
- Otherwise it prints `class=X code=-`, and ONLY when the class name ends in `Refused` or `Attention` (our own refusals, raised with developer-written text) it appends one more field ` lead=<token>` when a leading constant token exists:
  - an upper-case code at the very start of the message followed by a colon, a space or the end (regex `([A-Z][A-Z0-9_]{2,63})(?::| |$)`, for example `COMPARISON_NO_VENDOR_MAPPING: ...`) gives that token;
  - otherwise the leading run of WHOLE words, split on single spaces, each word entirely lower-case letters (`[a-z]+`), at most six words, ends at the first word that is not entirely lower-case letters (a quoted id, a number, a capitalised name, an upper-case value or a URL), joined with `_`; it counts only when it holds at least two words.
- Any other class (RuntimeError, ValueError, a vendor or HTTP error) prints `code=-` and never a lead; no message text is printed in any other case (errors can carry signed URLs or customer data; the module comment says so).
Examples: `RecipeRefused("holdings row has no provider receipt")` -> `class=RecipeRefused code=- lead=holdings_row_has_no_provider_receipt`; `RecipeRefused("holdings row 'SPY' has no provider check")` -> `class=RecipeRefused code=- lead=holdings_row`; `RecipeRefused("template T-1 (multicomp) takes 2..5 comparison securities")` -> `class=RecipeRefused code=-`; `RuntimeError("holdings row has no provider receipt")` -> `class=RuntimeError code=-`.

**Do exactly this.**
1. `infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py`: change `retained_reason` (and add one small private helper if you want) to follow the rule; update its docstring to say what the line now carries. Nothing else in the file changes.
2. Tests, which FAIL before your change (run them first and say so): in `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_main.py` add at least two tests: one that a Refused-class sentence message gives the `lead=` field and a value-bearing message gives only the words before the value; one that a non-Refused class and a closed code print exactly as before. Keep every existing test in the four test files the checker runs passing (the `tests` arm).
3. Run the two acceptance invocations; write the proof instance; commit; flip the order to complete only on both PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR183-g-AC1" cell_refs="AR-g-183"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_reason_checks.py reason</invocation><expect>^AR-REASON-reason-OK$</expect></criterion>

<criterion id="AR183-g-AC2" cell_refs="AR-g-183"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_reason_checks.py tests</invocation><expect>^AR-REASON-tests-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR183-g-AC1,AR183-g-AC2</expected_criteria>

- AC1: retained_reason over 14 fixed exceptions: closed codes print as before, a Refused or Attention class with a sentence message gets lead=<words or code>, any other class never does, and no value (quoted id, number, name, URL) is printed. At base it FAILs (6 of 14 differ).
- AC2: the four test files that read the retained line pass (49 at the base) and at least 51 ran. At base it FAILs (49 ran).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_main.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~356/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-183.resident-retained-line-carries-the-leading-constant-words-of-our-own-refusals.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-183`.
<owned_cells>AR-g-183</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR183-g-AC1,AR183-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~356/IRPT_ANLREQ.TO-AR-g-183.resident-retained-line-carries-the-leading-constant-words-of-our-own-refusals.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-183`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR183-g-AC1,AR183-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one lambda-tree source file and one test file edited in the worker's worktree; nothing is deployed, no AWS call; the line reaches the host only through a later resident release under a never-widen pair. The journal line gains an optional field; no message text other than lower-case constant words or an upper-case code is printed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: both criteria FAIL at base; the checker was calibrated by the issuer against a reference implementation in a scratch tree (OK) and five mutants (lead on any class, value words printed, one-word lead, lead on closed codes, eight words), each of which fails. Traps: printing the message for a non-Refused class (signed URLs and customer data), a value (quoted id, name) in the lead, changing the closed-code output, editing the checker. NOT seen (blind): other consumers that parse the line (IB2's receipts grep `class=` and `code=` only; the new field is appended).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 and AC2 FAIL.
