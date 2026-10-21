# TO-AR-g-190 -- page 60's allocation rows print each model's own positioning date (CTO msg 11977 enrichment 2)

<to_id>IRPT_ANLREQ.TO-AR-g-190</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~381</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL11</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-190` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** none (disjoint from AR-g-189). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~381`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-381` (branch `wk-IRPT_ANLREQ-381`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~381 <0.9.0_WK_IRPT_ANLREQ~381@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W381-S<k>` (check the channel file for `W381` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich_checks.py` (read it; you cannot edit it). It builds its own inputs and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-190`, inlined)

**What this cell is.** Page 60 (the comparison section's allocation table) prints, for each Opal model, `Model positioning as of <date>`. The date printed is the positioning object's FILE-level `data_as_of` (2026-10-19), but each model has its own date in the same object: `portfolios.<code>.data_as_of` (Short-Term 2026-10-08, Long-Term 2026-08-18 on the live object). A reader takes the printed date as the date of each model's weights. The CTO (msg 11977) ruled that each row prints its own date.

**Do exactly this.**
1. `infra/aws/lambda/investor-reporting/ycharts/research/model_source.py`, `read_allocation`: for each model code read, take the portfolio entry's `data_as_of`. Absent: the file-level `data_as_of`. Present and not a `YYYY-MM-DD` day (use the file's own `_parse_day`): `_refuse(...)` naming the code, like the module's other malformed-field refusals. Return `{"as_of": <file-level, unchanged>, "as_of_by_code": {code: day}, "allocation": ...}`; `as_of` and `allocation` stay exactly as today.
2. `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py`, `_compare_stage`: the model branch takes `as_of` from `alloc_doc["as_of_by_code"][code]` instead of `alloc_doc["as_of"]` (the `weights, as_of = ...` line). `comparables.py` already prints each row's own `as_of`; do not edit it. Nothing else in the file changes.
3. Tests, which FAIL on the old code (run them first and say so): in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_model_source.py` add at least three: per-code dates read from `portfolios.<code>.data_as_of`; a portfolio without it takes the file's date; a malformed per-portfolio date is refused (use the file's own fixtures and refusal helpers). In `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_producer.py` add one: with per-portfolio dates differing from the file's, the allocation rows' `Basis` reads each model's own date (the file's `_model_bytes` builds the positioning object: give it an optional per-portfolio date argument, default unchanged, so the existing tests are unchanged). Keep every existing test passing.
4. Run the two acceptance invocations; write the proof instance; commit; flip the order to complete only on both PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR190-g-AC1" cell_refs="AR-g-190"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich_checks.py asof</invocation><expect>^AR-ENRICH-asof-OK$</expect></criterion>

<criterion id="AR190-g-AC2" cell_refs="AR-g-190"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich_checks.py tests190</invocation><expect>^AR-ENRICH-tests190-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR190-g-AC1,AR190-g-AC2</expected_criteria>

- AC1: read_allocation returns each model's own data_as_of (fallback to the file's date when absent, a malformed one refused) with the file-level as_of unchanged, and the REAL producer's allocation rows print `Model positioning as of <own date>` per model. At base it FAILs.
- AC2: the two owned test files pass (65 at the base) and at least 68 ran. At base it FAILs (65 ran).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/model_source.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_model_source.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_producer.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~381/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-190.page-60-allocation-rows-print-each-models-own-as-of-date.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-190`.
<owned_cells>AR-g-190</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR190-g-AC1,AR190-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~381/IRPT_ANLREQ.TO-AR-g-190.page-60-allocation-rows-print-each-models-own-as-of-date.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-190`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR190-g-AC1,AR190-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two lambda-tree source files and two test files edited in the worker's worktree; nothing is deployed, no AWS call, no network; the change reaches the host only through a later resident release (r34t) under a never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: both criteria FAIL at base; the checker was calibrated by the issuer against the reference fix in a sparse scratch worktree (OK) and mutants: the file date always, no fallback to the file date, the producer ignoring the per-code date, each fails. Traps: refusing instead of falling back when the field is absent (the test fixtures carry none), changing the file-level as_of that other tests pin, editing comparables.py. NOT seen (blind): the live object's field name beyond the 7J read and the gateway view (both show a per-model data_as_of); run 7M reads it.
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 and AC2 FAIL.
