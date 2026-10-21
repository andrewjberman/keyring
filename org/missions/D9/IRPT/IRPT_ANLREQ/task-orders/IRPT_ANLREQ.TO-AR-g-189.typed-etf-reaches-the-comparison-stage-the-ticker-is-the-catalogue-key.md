# TO-AR-g-189 -- a typed ETF reaches the Opal comparison stage as a priced comparable: its ticker is the catalogue key (CTO msg 11977 enrichment 1)

<to_id>IRPT_ANLREQ.TO-AR-g-189</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~380</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL11</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-189` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-182 (merged). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~380`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-380` (branch `wk-IRPT_ANLREQ-380`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~380 <0.9.0_WK_IRPT_ANLREQ~380@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W380-S<k>` (check the channel file for `W380` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich_checks.py` (read it; you cannot edit it). It builds its own inputs and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-189`, inlined)

**What this cell is.** The form's "Other ETFs" field puts a typed ticker into the request's `comparison_keys`. The submission door (`infra/aws/lambda/investor-reporting/_scope/maintained_sources.py`, `resolve_comparison_fields`) admits a ticker that is not in the Opal catalogue when the `etf-classifications` table names it, and retains the entry `{"vendor_id": "IWM", "name": "iShares Russell 2000 ETF", "security_type": "etf", "namespace": "YCHARTS", "source_id": "IWM", "mapping_evidence": ...}`. The door drops the `key` field from EVERY retained entry (lines 614 and 627: the key is the dict key of `comparison_catalog`). The issuer measured (record `ETF_TYPED_PATH_MEASUREMENT_20261021.md`, instrument `checks/etf_typed_measure.py`) that `ResidentGenerationWorker._opal_comparables` (`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`, the line that builds `"ticker"`) reads the ticker from `c.get("key")`, which is therefore None for a typed ETF. The producer's `_compare_stage` then treats the comparable as neither a model nor a ticker and shows it as an empty "other" line: no price is read and no row prints. AR-g-182 zipped the browser's `comparison_keys` with the entries to recover the key for models but kept `c.get("key")` for the ETF; its tests handed in an ETF entry that wrongly carried a `key` field (the door never retains one).

**Do exactly this.**
1. `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`, `_opal_comparables`: the ticker of an ETF entry is the zipped catalogue KEY (the loop variable `key`), not `c.get("key")`: `"ticker": key if c.get("security_type") == "etf" else None`. Keep the order, the `label` and the model branch exactly as they are. Update the comment above it to say the ticker is the key. Nothing else in the file changes.
2. `infra/aws/lambda/investor-reporting/reports/tests/test_compare_ports.py`: change the `CATALOGUE["IWM"]` entry to the door's real shape (no `key` field; add `"source_id": "IWM"`), so the existing ETF test now fails on the old code. Add at least two tests: (a) the REAL door, `maintained_sources.resolve_comparison_fields` (the file's own `_bind` already puts `_scope` on the path), called with `comparison_keys=["opal_long_term", "IWM"]`, a catalogue whose `entries` hold the model's admitted candidate OR (simpler, allowed) `comparison_keys=["IWM"]` with an empty catalogue `{"maintainer": "2.0.0_SA_COO~Y", "candidate_version": maintained_sources.COMPARISON_CANDIDATE_VERSION, "entries": []}`, `authorize_input=lambda owner, ref: True`, `read_classifications=lambda: {"IWM": {"name": "iShares Russell 2000 ETF"}}`, after setting `maintained_sources.resolve_prospect_owner` to return `{"firm_id": "F1", "principal_id": "P1", "principal_class": "OPAL_GLOBAL", "advisor_id": None, "home_firm_id": "F1"}` (restore it with monkeypatch); feed its `comparison_catalog` to `_opal_comparables` through the file's own fake frozen reader and require `[{"key": "IWM", "label": "iShares Russell 2000 ETF", "ticker": "IWM"}]`; (b) a model entry still gets ticker None. Keep every existing test passing.
3. Run the two acceptance invocations; write the proof instance; commit; flip the order to complete only on both PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR189-g-AC1" cell_refs="AR-g-189"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich_checks.py etfkey</invocation><expect>^AR-ENRICH-etfkey-OK$</expect></criterion>

<criterion id="AR189-g-AC2" cell_refs="AR-g-189"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_enrich_checks.py tests189</invocation><expect>^AR-ENRICH-tests189-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR189-g-AC1,AR189-g-AC2</expected_criteria>

- AC1: the REAL door admits a typed ETF (IWM, named by the classification table); the REAL _opal_comparables returns ticker IWM for it and None for a model; the REAL producer given those comparables charts the ETF priced from the held readers, reports it at 100 percent in its class and states no gap. At base it FAILs (ticker None).
- AC2: the owned test file passes (5 at the base) and at least 7 ran. At base it FAILs (5 ran).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/reports/tests/test_compare_ports.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~380/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-189.typed-etf-reaches-the-comparison-stage-the-ticker-is-the-catalogue-key.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-189`.
<owned_cells>AR-g-189</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR189-g-AC1,AR189-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~380/IRPT_ANLREQ.TO-AR-g-189.typed-etf-reaches-the-comparison-stage-the-ticker-is-the-catalogue-key.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-189`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR189-g-AC1,AR189-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one lambda-tree source line and one test file edited in the worker's worktree; nothing is deployed, no AWS call, no network; the change reaches the host only through a later resident release (r34t) under a never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: both criteria FAIL at base; the checker was calibrated by the issuer against the reference fix in a sparse scratch worktree (OK) and mutants: ticker never, ticker on every entry (a model gets one) each fail. Traps: assuming the entry has a key field (the door drops it; the old tests wrongly carried one), setting a ticker on a model, editing the checker. NOT seen (blind): whether the live estate or yfinance tier holds the typed ticker's history (run 7M reads it).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 and AC2 FAIL.
