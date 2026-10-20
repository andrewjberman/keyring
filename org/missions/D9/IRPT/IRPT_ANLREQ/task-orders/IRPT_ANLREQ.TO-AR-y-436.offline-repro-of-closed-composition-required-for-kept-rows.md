# TO IRPT_ANLREQ.TO-AR-y-436.offline-repro-of-closed-composition-required-for-kept-rows -- READ AND REPRODUCE OFFLINE: which of the five steps of CompositionAdmission.validate refuses a request composition built from a frozen portfolio with kept rows (three KEPT_BY_HISTORY rows, with and without one UNRESOLVED/KEPT_AS_TYPED row); no product file is changed

<to_id>IRPT_ANLREQ.TO-AR-y-436.offline-repro-of-closed-composition-required-for-kept-rows</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~316</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ95</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read and an offline reproduction; the only repository writes are the worker's deliverables) | **Decomp cell:** `AR-y-436` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a staff filing that keeps an unknown ticker reaches a report), C-SWAP | **depends_on:** IB2 receipt irpt_anlreq_commentary_e2e5b/A_E2E5B.txt (run 5B: NORMALIZED after the Keep, then the resident retained the request for retry twice with SubmissionRefused CLOSED_COMPOSITION_REQUIRED, 02:34:11Z and 02:49:12Z, the job row stayed RECEIVED); CTO msgs 11186 and 11112

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~316`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-316` (branch `wk-IRPT_ANLREQ-316`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~316 <0.9.0_WK_IRPT_ANLREQ~316@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W316-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-436`, inlined)

*Context.* Run 5B (a synthetic request: holdings bytes `SPY`, `AGG`, `TIMXX` and the deliberately unknown `ZQXWVK`, the Keep sent) was accepted by the door as NORMALIZED. The ticket and the analysis request were created. The resident then refused the request's submission twice with `SubmissionRefused("CLOSED_COMPOSITION_REQUIRED")` and never produced a job: the job row stayed RECEIVED. That refusal is raised in `infra/aws/lambda/investor-reporting/ycharts/generate/composition_admission.py` `CompositionAdmission.validate`, which wraps ANY of five steps (1 canonical, 2 schema, 3 compose, 4 bindings, 5 portfolio) and prints only `COMPOSITION-REFUSED step=<n> error_class=<Class>` (no request id; the resident journal was not matched to the request). Before this run no synthetic run had ever got past the upload door, so this is the first time a kept row reaches the composition. The question: WHICH step refuses, and why, for (A) a frozen portfolio whose three rows `SPY`, `AGG`, `TIMXX` are KEPT_BY_HISTORY (the door's `TICKER_KEPT_BY_HISTORY` notices, method KEPT_BY_HISTORY, no provider receipt), and (B) the same plus a fourth row for `ZQXWVK` with `resolution` UNRESOLVED and `method` KEPT_AS_TYPED (`infra/aws/lambda/investor-reporting/intake/portfolio.py` `freeze_template_portfolio`, the `unresolved` branch near line 590). The run-5C order (three rows, no unknown) is about to run live; the answer for (A) tells whether that run can pass.

*Where to look (all in the repository, you may read all of it).* `ycharts/generate/composition_admission.py`; `ycharts/generate/prospect_submission.py` and `custody_submission.py` (they build the composition the resident admits; `prospect_submission.py:46` constructs `CompositionAdmission(schema_directory)`); `reports/submission.py` (`compose_frozen_request`, `canonical_bytes`); `reports/request_composition.py` (`validate_bindings`); `intake/portfolio.py` (`freeze_template_portfolio`, `verify_frozen_portfolio`); the schema directory `docs/contracts/investor-reporting/v1/` (`RequestComposition.schema.json` and its siblings); the existing tests that already build a valid composition and break it one step at a time: `ycharts/generate/tests/test_composition_refusal_cause.py` (five cases, one per step), `ycharts/generate/tests/test_ordinary_owner_legacy_row.py`, `ycharts/generate/tests/test_submission.py`; and for building frozen documents with kept and unresolved rows `intake/tests/test_unresolved_keep.py` and `intake/tests/test_kept_holding.py`. Add the folders you need to the sparse checkout with `git sparse-checkout add <folder>` (for example `docs/contracts/investor-reporting`, `lib`).

*What to do.* (1) Read the five steps and write `repro_composition.py` (stdlib plus the repository's own modules, ruff clean, ASCII, offline, no AWS, no network, under 60 s) in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~316/`. It builds, with the repository's own functions and the fixtures the tests above use (do not hand-write what a function builds), a VALID baseline composition (the one `test_composition_refusal_cause.py` starts from), then replaces its frozen portfolio document (and the digest fields that bind it) with (A) the three-KEPT_BY_HISTORY document and (B) the four-row document, each produced by `freeze_template_portfolio` from synthetic inputs, and runs `CompositionAdmission(<schema dir>).validate(...)` on each. It prints exactly three lines: `REPRO-A step=<n|none> class=<ExceptionClass|none>`; `REPRO-B step=<n|none> class=<ExceptionClass|none> detail=<validator>@<json path>` (the jsonschema `validator` keyword and the `/`-joined path of the first error when the failing step is the schema step, or the name of the check that raised for the portfolio or bindings steps, or `-`); and `REPRO-C step=2 class=ValidationError` for the CONTROL: the baseline composition with one required key removed, which must refuse at the schema step (this proves the script can see a refusal). `step=none` means the composition was admitted. (2) Write `REPRO_NOTES.md` in the same folder: for A and B, in at most 25 lines, the step, the exception class and message class, the file and line that raised it, and in one paragraph why a kept row does or does not fit the composition contract; and, only as a proposal, the smallest change that would let the composition admit it (a file, a function, the lines), NOT applied. If A admits and B refuses, say which field of the UNRESOLVED row the contract rejects. (3) Run the script and print its three lines, then commit the script and the notes, then the proof instance, and flip on VALID.

You also write nothing in the product tree (`infra/`, `docs/`, `portal/`): a READ and REPRODUCE cell; any file you would change is named in the notes only.

---

## ACCEPTANCE

<criterion id="AR436-y-AC1" cell_refs="AR-y-436"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~316/repro_composition.py</invocation><expect>^REPRO-A step=(none|[1-5]) class=\S+$</expect></criterion>
<criterion id="AR436-y-AC2" cell_refs="AR-y-436"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~316/repro_composition.py</invocation><expect>^REPRO-B step=(none|[1-5]) class=\S+ detail=\S+$</expect></criterion>
<criterion id="AR436-y-AC3" cell_refs="AR-y-436"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~316/repro_composition.py</invocation><expect>^REPRO-C step=2 class=ValidationError$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~316/IRPT_ANLREQ.TO-AR-y-436.offline-repro-of-closed-composition-required-for-kept-rows.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-436.offline-repro-of-closed-composition-required-for-kept-rows`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR436-y-AC1,AR436-y-AC2,AR436-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-436</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~316/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-436.offline-repro-of-closed-composition-required-for-kept-rows.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read and an offline reproduction; the worker writes a script and notes in its own deliverables folder; no product file, no AWS, no network.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading composition_admission.py and the five-case test against this cell; the lens: a hand-written document that never was a real freeze (use the freeze function), a control that cannot refuse (REPRO-C must refuse at step 2), a printed client value (the inputs are synthetic and only closed words are printed), a product file edited to make a case pass (forbidden). NOT seen (blind): the live resident and its journal; denominator: three criteria.
</preflight>
