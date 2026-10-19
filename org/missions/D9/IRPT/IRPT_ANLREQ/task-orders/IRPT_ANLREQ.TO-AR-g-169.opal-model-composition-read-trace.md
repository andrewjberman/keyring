# TO-AR-g-169 -- READ ONLY: where the Opal model compositions live and what reads them (the model-weight read for the comparison side of the price pages) (CTO msg 10778)

<to_id>IRPT_ANLREQ.TO-AR-g-169</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~304</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>58</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-169` (`decompositions/IRPT_ANLREQ_DECOMP_R58_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none. A code read: no AWS call, no run, no deploy, no edit of any product file.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~304`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-304` (branch `wk-IRPT_ANLREQ-304`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~304 <0.9.0_WK_IRPT_ANLREQ~304@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W304-S<k>` (take the next free `<k>`; check the channel file for `W304` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Read with the Grep, Glob and Read tools; the repository search tool `comp-find '<pattern>' [pathspec]` is permitted (a bare recursive `grep -r` or `find` over the repository is refused by the shell hook; run what its message tells you to run). Python 3.9, ASCII only. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-169`, inlined)

An Analysis Request may compare the client's portfolio with up to five entries of the comparison catalogue. Each entry is an Opal MODEL or a single TICKER. For a ticker, the existing price stage already holds the series. For a model, the comparison needs the model's COMPOSITION: its tickers and weights, so the comparison series is the composite of those weights, priced the same way. The catalogue (`infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py` and `templates.json`, key `comparison_catalog.entries`, 5 entries: `vendor_id` UST, ST, INT, LT, ULT) holds NO weights. Your job is to find where the compositions live and what, if anything, already reads them. Build nothing.

Write ONE file, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~304/MODEL_COMPOSITION_TRACE.md`. It must contain exactly six answer lines, each on ONE line that STARTS with its label and a space (`Q1 `, `Q2 `, ... `Q6 `), appearing exactly once, at least 60 characters, carrying one claim word (`MEASURED` = you read it in a file and cite it, `INFERRED` = you concluded it from what you read, `NOT READ` = you did not read it) and at least one `path:line` citation (a repository-relative path, a colon, a line number) for everything you claim to have read, or the words `NOT READ` for what you did not. You may add any other text (headings, a table, evidence lists) so long as no other line starts with `Q1 ` to `Q6 `.

- `Q1` Where are the compositions of the Opal models (model code, ticker, weight) stored? Name the producer, the bucket or table, the address the naming builder (`lib/opal_naming.py`) gives it if the code uses the builder, the columns, and the as-of grain (daily, monthly, per rebalance). Start from `data/mdpf/scripts/bronze/pull_orion_model_composition.py`, `workflows/atom_decomposition/catalog_entries/opal_data_mdpf_feeds_model_composition.yaml` and `.../opal_data_assets_silver_eclipse_inflection_fact_model_composition.yaml`, and `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` (`MODEL_CODES` at line 66).
- `Q2` Whose bucket is it: a firm's private bucket, or a shared Opal one? (CLAUDE.md section 5: a pipeline tree must never reference another firm's bucket or key prefix. State which bucket a reporting-side reader could read without breaking that rule, or that none can.)
- `Q3` Does a reader already exist that returns `{ticker: weight}` for a model code on a date? Name the module and the function signature, or say that you found none.
- `Q4` How fresh is it and on what schedule is it refreshed? (cite the schedule or the pipeline's trigger)
- `Q5` Which IAM role would a reader inside the resident (the `irpt-resident` process, `ycharts/generate/resident_*.py`) run as, and does an existing policy already grant it the read of Q1's location? (read the Terraform and the policy files only; make no AWS call)
- `Q6` How does the catalogue's `vendor_id` (UST, ST, INT, LT, ULT) map to the composition's own model identifier? (cite the mapping, or say it is not written down)

1. Read; write the record; run the three criteria. 2. Commit the record, then the proof and the status flip as separate commits. 3. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR169-g-AC1" cell_refs="AR-g-169"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g169_checks.py build</invocation><expect>^AR-G169-OK</expect></criterion>

<criterion id="AR169-g-AC2" cell_refs="AR-g-169"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g169_checks.py guard</invocation><expect>^AR-G169-OK</expect></criterion>

<criterion id="AR169-g-AC3" cell_refs="AR-g-169"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g169_checks.py regress</invocation><expect>^AR-G169-REGRESS-OK</expect></criterion>

<expected_criteria>AR169-g-AC1,AR169-g-AC2,AR169-g-AC3</expected_criteria>

- AC1: the record exists with exactly the six labelled lines, each of at least 60 characters and each carrying a claim word. At base it FAILs (no record).
- AC2: every answer line cites a `path:line` or says `NOT READ`; the check's own control (a planted uncited line) is refused by the same rule. At base it PASSes (the control runs; the record is absent).
- AC3: the branch changed only the record, your folder, the order and the channel file. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. Every product file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~304/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-169.opal-model-composition-read-trace.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R58_G.md</decomp_doc> round 58, workstream ~G, cell `AR-g-169`.
<owned_cells>AR-g-169</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR169-g-AC1, AR169-g-AC2, AR169-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~304/IRPT_ANLREQ.TO-AR-g-169.opal-model-composition-read-trace.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-169`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR169-g-AC1,AR169-g-AC2,AR169-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~282/IRPT_ANLREQ.TO-AR-g-161.pricing-as-of-calendar-frontier.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a code read; one new record file in the worker's own folder. No deploy, no AWS call, no network, no edit of any product file.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell reads IAM policy files as text and calls no AWS API. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is created; Q4 only reads one.
comp-adversary: RUN -- `ar_g169_checks.py` was dry-run at the base (build FAIL, guard PASS, regress PASS) and against a scratch record with six good lines of which Q4 has no citation: build OK, guard FAIL naming Q4, so the citation rule fires. Traps: the lines must start with the label and a space and appear exactly once (a table row or a bullet `- Q1` does not count); `NOT READ` is an honest answer and is accepted, a citation that does not exist is not (the issuer re-reads two citations at the merge). NOT seen (blind): that a citation says what the line claims (the issuer samples it).
</preflight>

- Cut on the CTO's ruling (msg 10778) by the issuer inside its own decomposition. Risk LOCAL: a read of text files, nothing deployed. Base: AR169-g-AC1 FAILs, AR169-g-AC2 PASSes, AR169-g-AC3 PASSes.
