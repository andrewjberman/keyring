# TO IRPT_BCKEND.TO-IB-pr-517 -- BUILD the Opal model identity into the comparison catalogue: Ultra Short-Term added keyed by Opal's own model identity, canonical order, the YCharts path refuses an entry with no YCharts mapping (CTO msgs 7178 and 7189; Andrew-direct ~18:2xZ vendor-agnostic; rows D2-S148, D2-S149)

<to_id>IRPT_BCKEND.TO-IB-pr-517</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~366</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>183</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-183 addition (msg 7178) and ruling (msg 7189) | **Decomp cell:** `IB-pr-517` (decomposition section 175) | **outcome_ref:** FWD-1 (O1 hop)

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-366`, on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~366 <0.9.0_WK_IRPT_BCKEND~366@opal.agent>" -F <msgfile> -- <paths>` (write the message file with the Write tool). Never push, never deploy, never call a vendor, never invoke a Lambda, never change an IAM, route, schedule or table. **BUILD ONLY.**

**Cell `IB-pr-517` (inlined).** The Investor Reporting comparison catalogue lists the Opal models a person may compare a portfolio against. `infra/aws/lambda/investor-reporting/ycharts/generate/templates.json`, member `comparison_catalog.entries`, holds four entries (`opal_long_term`, `opal_short_term`, `opal_intermediate_term`, `opal_ultra_long_term`), each with a YCharts id (`security_id` like `P:1728413`). The Model Portfolios page lists five models in this order: Ultra-Short Term, Short Term, Intermediate Term, Long Term, Ultra-Long Term (codes UST, ST, INT, LT, ULT: `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` lines 66-78). **Ultra Short-Term is the one that is missing.** Andrew's rule: vendors are data providers only, so an Opal model is keyed by Opal's OWN model identity, and a YCharts id is an OPTIONAL mapping. The new entry therefore has NO YCharts id, and the YCharts generation path must refuse such an entry and say why. The four existing entries keep their YCharts ids and their pins unchanged. You may not invent or look up a vendor id.

**Do all of these, in this order:**

1. **`templates.json`.** (a) Add ONE entry, key `opal_ultra_short_term`, label `Opal Ultra Short-Term`, `live_proven` false, with NO `security_id` and NO top-level `security_type`, and a `candidate` of: `namespace` `OPAL`; `vendor_id` `UST` (Opal's own model code; the pipeline's field is named `vendor_id` and requires a value, and in namespace OPAL it carries Opal's code); `name` `Opal Ultra Short-Term`; `security_type` `model_portfolio`; `mapping_evidence` a one-line string naming the Opal model code `UST` in `yang-model-portfolio-benchmarks/lambda_function.py` (`MODEL_CODES`); `identity_status` `VERIFIED`; `entitlement_status` `GRANTED`; `permitted_firm_ids` `[]`; `permitted_principal_classes` the same list the existing `opal_long_term` candidate carries; and a `verification_ref` with `evidence` the repository-relative path of that Yang file, `evidence_sha256` the sha256 of that file's bytes at the base commit (compute it, do not type it), `retrieved_at` the current UTC time, `read_by` `0.9.0_WK_IRPT_BCKEND~366`, `graded_by` `2.0.0_SA_COO~P2`, `returned_name` `Ultra-Short Term` (the Yang `MODEL_NAMES` value), `permission_ref` and `permission_scope` copied from `opal_long_term`'s `verification_ref`. (b) Reorder `entries` into the canonical order: `opal_ultra_short_term`, `opal_short_term`, `opal_intermediate_term`, `opal_long_term`, `opal_ultra_long_term`. (c) Set `_meta.denominators.comparison_catalog_entries` to 5. Do not change any other member or any existing entry's content.
2. **The pin.** `infra/aws/lambda/investor-reporting/_scope/maintained_sources.py` holds `_COMPARISON_POLICY_SHA256`, one code-pinned digest per key; an entry whose key has no pin is refused. Compute the digest for the new entry exactly as the admission does (`projection_sha256(_comparison_policy(key, candidate))`, both in that file) and add `"opal_ultra_short_term": "<digest>"`. Do not touch the four existing pins.
3. **The YCharts path refuses an unmapped entry.** In `infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py`: add `"COMPARISON_NO_VENDOR_MAPPING"` to the declared tuple `ENVELOPE_REFUSALS` (an `EnvelopeRefused` raised with an undeclared code becomes a plain `RecipeRefused`); add a module-level function `comparison_security_ids(catalog, keys)` that returns the list of each key's `security_id` in order and, for a key whose entry has no non-empty string `security_id`, raises `EnvelopeRefused("COMPARISON_NO_VENDOR_MAPPING", "<key> has no YCharts mapping; the YCharts path cannot price it")`; and replace the line `ids = [catalog[k]["security_id"] for k in keys]` in `validate_envelope` with `ids = comparison_security_ids(catalog, keys)`.
4. **Tests.** In `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_comparison_catalogue.py` move the two pinned counts: `len(payload["entries"]) == 4` becomes 5 and `== 6` becomes 7. Create `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_comparison_opal_model.py` with at least these three tests (names starting `test_`): the served model entries read the five labels in canonical order with no ticker; all five entries are admitted by `_admitted_comparison` while an altered copy of the new entry (its `name` changed) is refused with `MaintainedSourceUnauthorized`; `comparison_security_ids` returns ids for mapped entries and refuses an unmapped one with the code `COMPARISON_NO_VENDOR_MAPPING` naming the key. Run both test files from `infra/aws/lambda/investor-reporting/ycharts/generate` with `python -m pytest -q -p no:cacheprovider tests/test_comparison_catalogue.py tests/test_comparison_opal_model.py`; both must pass.
5. **Then run the three criteria below from your worktree root, record each output and exit code verbatim, and commit.** If a criterion fails, fix YOUR change (never the check) and run again. Report once, under 150 words, in your final message.

**Criteria (run each under `timeout 200` from your worktree root; the check is read-only):**

<criterion id="IB183-1-AC1" cell_refs="IB-pr-517"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r183/p183_cells.py" . IB183-1-AC1</invocation><expect>IB183-1-AC1 PASS</expect></criterion>
<criterion id="IB183-1-AC2" cell_refs="IB-pr-517"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r183/p183_cells.py" . IB183-1-AC2</invocation><expect>IB183-1-AC2 PASS</expect></criterion>
<criterion id="IB183-1-AC3" cell_refs="IB-pr-517"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r183/p183_cells.py" . IB183-1-AC3</invocation><expect>IB183-1-AC3 PASS</expect></criterion>

<expected_criteria>IB183-1-AC1, IB183-1-AC2, IB183-1-AC3</expected_criteria>

What the checks grade: AC1 the served list (five model entries, canonical order, named, no ticker, no vendor member), the entries count 5, the new entry without a `security_id`; AC2 every entry admitted for the three permitted firms and three principal classes, the four old pins unchanged, the new entry OPAL/UST, an altered copy refused; AC3 the unmapped-entry refusal with its code and the two test files passing. Do not edit the checks.

## BOUNDS

- **Write surface:** exactly the `<paths>` below. **Nothing is deployed, applied, uploaded or invoked, and no vendor is called.** The served catalogue changes only when a later, separately signed apply moves the function that packages these files.
- **Refusal clause:** STOP and report if: a file in `<paths>` already differs from what this order describes in a way that changes the design; a test outside the two named files fails after your change (name it, do not edit it); the admission refuses an existing entry. Do not widen the grant; a worker never receives a question back.
- **Row ids** are `IRPT_BCKEND-W366-S<k>` (start at 1); file a row (append-only, `INVESTIGATION_v1.md`) for anything odd and keep working.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/templates.json
infra/aws/lambda/investor-reporting/_scope/maintained_sources.py
infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_comparison_catalogue.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_comparison_opal_model.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~366/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-517.opal-model-in-the-comparison-catalogue.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 175 (round 183, workstream ~P), cell `IB-pr-517`.
<owned_cells>IB-pr-517</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB183-1-AC1, IB183-1-AC2, IB183-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~366/IRPT_BCKEND.TO-IB-pr-517.opal-model-in-the-comparison-catalogue.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served catalogue (`GET /api/scoped/investor-reporting/analysis/comparisons`, `entry.py:150-166`) and its readers: the portal's Analysis request form (`TicketCenter.tsx:287`, `AnalysisRequestParts.tsx:112-121`) and the request composition (`reports/request_composition.py:190-215`); five model entries, 0 new vendor reads; the build changes nothing served until a later signed apply moves the function that packages these files (round 184: its census and never-widen pair).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission, role or grant is changed; the new entry adds no firm and no principal class (the same three classes the existing models carry).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p183_cells.py dry-run at base on dell2 2026-10-13 ~19:4xZ: IB183-1 AC1, AC2, AC3 FAIL (no Ultra Short-Term entry; no pin; no comparison_security_ids). Positive control in a temp tree the run created itself (copies of the investor-reporting tree, lib, infra/logic and docs/contracts; the change applied by hand; the temp tree removed): AC1 PASS, AC2 PASS, AC3 reaches and passes the refusal arm (its pytest arm needs the test edits); the first AC3 control found that an undeclared refusal code degrades to RecipeRefused, which is why step 3 adds the code to ENVELOPE_REFUSALS.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~366` (worktree `C:/dev/wk-IRPT_BCKEND-366`). Class WORLD (the gate infers the floor from the infrastructure path templates.json; the order itself is BUILD ONLY, changes what the catalogue will serve only once a later apply moves it, and applies nothing).
</preflight>
