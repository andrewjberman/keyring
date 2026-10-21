# TO-AR-g-182 -- the Opal comparison path reads its comparisons without building the vendor upload and from the real catalogue shape (S249)

<to_id>IRPT_ANLREQ.TO-AR-g-182</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~355</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL6</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-182` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** the run 7I replay (CTO msg 11890) and AR-g-175. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~355`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-355` (branch `wk-IRPT_ANLREQ-355`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~355 <0.9.0_WK_IRPT_ANLREQ~355@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W355-S<k>` (check the channel file for `W355` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_prepare_checks.py` (read it; you cannot edit it, and you cannot edit its fixture). It builds its own inputs and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-182`, inlined)

**What this cell is.** Run 7I (a Multi-Comp filing on the live r34q resident) stopped at the first hop with `retained_for_retry class=RecipeRefused`. The issuer replayed the run's retained synthetic composition through the module and read the inner message: `holdings row has no provider receipt`. Two defects, both in the code that AR-g-175 added for the Opal comparison path (`ResidentGenerationWorker._opal_comparables`, `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`):

1. **It builds the vendor upload it never uses.** `_opal_comparables` reads the request's comparisons through `FrozenCompositionWorker.prepare` (`infra/aws/lambda/investor-reporting/ycharts/generate/frozen_worker.py`). `prepare` ends every call by building the VENDOR upload with `prepare_normalized_upload(frozen_input)`, which refuses a holding with no provider receipt. The run's four holdings are public ETFs priced from history (their security checks read reason `YFINANCE_HISTORY` and carry no `provider_receipt`), so the call raised `RecipeRefused`. An Opal job makes no vendor call and needs only the comparisons.
2. **It reads the wrong fields.** It returns `{"key": c.get("key"), "label": c.get("label"), "ticker": c.get("ticker")}` per catalogue entry. The retained catalogue (`resolved["comparison_catalog"]`, a dict keyed by the comparison key) holds, for a MODEL: `{"mapping_evidence", "name", "namespace": "YCHARTS", "security_type": "model_portfolio", "source_id", "vendor_id"}` (no `key`, no `label`, no `ticker`; example key `opal_short_term`, name `Opal Short-Term`); for an ETF: `{"key": "IWM", "vendor_id": "IWM", "name": ..., "security_type": "etf", "namespace": "YCHARTS", "mapping_evidence"}`. The producer (`infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py`, `_compare_stage`) wants per entry `key` (the catalogue key; `model_source.code_for_key(key)` maps a model key to its code), `label` (the display name) and `ticker` (an ETF's symbol, else absent). With the old code every model would have had key None and the comparison would have been silently skipped.

**Do exactly this (the vendor path stays byte-for-byte as it is by default).**
1. `infra/aws/lambda/investor-reporting/ycharts/generate/frozen_worker.py`: give `prepare` one more keyword, `upload=True`. When `upload` is False the call skips `prepare_normalized_upload` and the result's `"upload"` is `None`; every other guard and read in `prepare` runs exactly as before. Add one key to the result dict: `"comparison_keys": list(document["browser"]["comparison_keys"])` (the browser's order). Nothing else in the file changes. (Rename the local variable that holds the upload if it shadows the new parameter.)
2. `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`, `_opal_comparables`: call `self.frozen.prepare(principal, request_id, data_firm=self.store.tenant, upload=False)` and return, in the order of `prepared["comparison_keys"]` zipped with `prepared["comparisons"]`, one `{"key": <the catalogue key>, "label": <the entry's "name">, "ticker": <the entry's "key"> if the entry's "security_type" == "etf" else None}`. Nothing else in the file changes.
3. Tests, each of which FAILS before your code change (run it first and say so in your report): in `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_frozen_worker.py` add one test that `prepare(..., upload=False)` returns `upload` None and `comparison_keys` equal to the browser's list (use the file's own harness), and that the default call still returns the upload; in `infra/aws/lambda/investor-reporting/reports/tests/test_compare_ports.py` change `FakeFrozen` to the REAL catalogue shape described above (a `comparison_keys` list and entries without key/label/ticker for models), assert that `prepare` was called with `upload=False`, and add the ETF case (`{"key": "IWM", ... "security_type": "etf"}` gives ticker `IWM`). Keep every existing test passing.
4. Run the three acceptance invocations; write the proof instance; commit; flip the order to complete only on three PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR182-g-AC1" cell_refs="AR-g-182"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_prepare_checks.py frozen</invocation><expect>^AR-PREP-frozen-OK$</expect></criterion>

<criterion id="AR182-g-AC2" cell_refs="AR-g-182"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_prepare_checks.py worker</invocation><expect>^AR-PREP-worker-OK$</expect></criterion>

<criterion id="AR182-g-AC3" cell_refs="AR-g-182"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_prepare_checks.py tests</invocation><expect>^AR-PREP-tests-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR182-g-AC1,AR182-g-AC2,AR182-g-AC3</expected_criteria>

- AC1: the REAL FrozenCompositionWorker.prepare over stubs that serve run 7I's retained composition: the default call still refuses a holding with no provider receipt, upload=False returns upload None, variant multicomp, comparison_keys in browser order and the two catalogue entries. At base it FAILs (no upload option).
- AC2: the REAL ResidentGenerationWorker._opal_comparables with a recording frozen stand-in: it calls prepare with upload=False and returns one {key, label, ticker} per chosen key, label the entry's name, ticker None for a model and the symbol for an ETF. At base it FAILs.
- AC3: the two owned test files pass (25 at the base) and at least 27 ran. At base it FAILs (25 ran).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/frozen_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_frozen_worker.py
infra/aws/lambda/investor-reporting/reports/tests/test_compare_ports.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~355/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-182.opal-comparison-path-frozen-read-without-vendor-upload-and-with-the-real-catalogue-shape.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-182`.
<owned_cells>AR-g-182</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR182-g-AC1,AR182-g-AC2,AR182-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~355/IRPT_ANLREQ.TO-AR-g-182.opal-comparison-path-frozen-read-without-vendor-upload-and-with-the-real-catalogue-shape.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-182`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR182-g-AC1,AR182-g-AC2,AR182-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two lambda-tree source files and two test files edited in the worker's worktree; nothing is deployed, no AWS call, no network; the change reaches the host only through a later resident release under a never-widen pair. The vendor path's default call is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base; the checker was calibrated by the issuer against a reference fix in a scratch tree (both arms OK) and six mutants (upload ignored, vendor path weakened, comparison_keys missing, worker omits upload=False, label read from the wrong field, ticker set on a model), each of which fails. Traps: weakening the vendor path (the default upload=True must still refuse), reading label from `label`, setting a ticker on a model, editing the checker or its fixture. NOT seen (blind): the live host and the live Opal producer's reads of the two model objects (the next filing reads them).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 all FAIL.
