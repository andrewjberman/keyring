# TO IRPT_ANLREQ.TO-AR-y-319.ordinary-viewer-owner-without-home-firm -- FIX the named cause (row D2-S97 / W128-S3): an ordinary viewer's retained owner and the frozen composition's owner must not carry home_firm_id, so a partner advisor's own-input analysis passes CompositionAdmission; source and tests only, nothing deployed

<to_id>IRPT_ANLREQ.TO-AR-y-319</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~129</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZG</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the infrastructure `<paths>` imply; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `AR-y-319` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop 1, the owned-input analysis of a partner advisor) | **depends_on:** `AR-y-318` (merged `ece60105e1`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~129`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-129` (branch `wk-IRPT_ANLREQ-129`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~129 <0.9.0_WK_IRPT_ANLREQ~129@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W129-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. **No live call of any kind** (no AWS, no network), no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. Scratch outside the product tree. Write no value of a person into any file or message.

### THE CELL (`AR-y-319`, inlined) -- the fix of a named cause. Source and tests only; nothing is deployed.

*The release-29 partner-advisor sitting proved the upload route and refused the OWNED-INPUT ANALYSIS of the advisor's own input (rows D2-S97, W128-S3). Worker 128 named the cause (record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~128/r40/COMPOSITION_CAUSE.json`, read it first, and `session_log.txt` beside it for the offline method): `CompositionAdmission.validate` step 2 (the JSON schema `docs/contracts/investor-reporting/v1/RequestComposition.schema.json`) refuses the frozen composition because `resolved.owner.home_firm_id` is present for a FIRM_ADVISOR; the owner definition (lines 520-605) REQUIRES `home_firm_id` only when `principal_class` is `OPAL_GLOBAL` and FORBIDS it otherwise (the `else` branch, line 599). Where it comes from: `infra/aws/lambda/investor-reporting/_scope/interactive_access.py` `current()` sets `home_firm_id` on EVERY ordinary viewer (line 97, `row["home_firm_id"] = owner["firm_id"]`), and `prospect_owner()` (about line 128-138) builds the retained owner as the actor minus only `ownership_fingerprint` and `allowedFirmIds`, so `home_firm_id` rides into the retained owner and into the composition. An OPAL_GLOBAL owner legitimately carries it. D6 (OPAL_GLOBAL) and the stored accepted composition pass all five steps; D1 (FIRM_ADVISOR) fails at step 2; removing only `home_firm_id` from D1's request owner makes all five pass (the negative control).*

**THE RULE.** The SCHEMA IS THE CONTRACT and is NOT edited (the file is outside your grant). Fix the producer(s) so a non-`OPAL_GLOBAL` owner has no `home_firm_id`:
1. **The writer.** `prospect_owner()` keeps `home_firm_id` in the retained owner ONLY when `principal_class == "OPAL_GLOBAL"`; for every other class it is omitted, and the owner's `ownership_fingerprint` is computed over the owner AS STORED (the existing `_fingerprint(owner)` call after the dict is built; check it is computed after the omission). `current()` and the PRINCIPAL it returns KEEP `home_firm_id` (the ordinary-viewer authorizer `_scope/ordinary_viewer.py` condition 2 compares `principal.home_firm_id` with the firm: do not touch that file or that comparison; its 43 tests must still pass).
2. **The reader of a LEGACY retained row.** Inputs stored BEFORE the fix (the release-29 sitting's D1 input, and any ordinary viewer's input) carry `home_firm_id` in their stored owner. Find where the analysis route turns a retained owner into the frozen composition's `resolved.owner` / request owner (follow the call from `ycharts/generate/submission.py` `compose_frozen_request` and `reports/request_composition.py` `validate_bindings`; and the route that loads the owner for the OWNED_INPUT guard). Make that step produce a schema-conforming owner for a non-`OPAL_GLOBAL` legacy row: omit `home_firm_id` and recompute whatever fingerprint or binding step 4 (`validate_bindings`) verifies over the owner, so steps 1 to 5 all PASS for the legacy row as well. If keeping step 4 passing for a legacy row requires touching a file outside `<paths>`, or cannot be done without weakening a binding check, STOP that half: file a BLOCKING row naming the conflict (file, line, the check) and say in your report that only the writer is fixed.
3. **What must not change:** an `OPAL_GLOBAL` owner (D6 and the stored accepted composition) is byte-identical before and after; `authorize_current` still admits the owner's own input for the owning advisor and refuses another advisor of the same firm and another firm's advisor (the cases of `_scope/tests`); no schema edit; no weakening of any check; the ordinary-viewer authorizer untouched.
4. **The tests (NEW file `infra/aws/lambda/investor-reporting/_scope/tests/test_ordinary_owner_composition.py`, self-contained, run with `python -m pytest`):** (a) `prospect_owner()` for a FIRM_ADVISOR actor has NO `home_firm_id` and its fingerprint equals the product's fingerprint of that stored owner; (b) for an OPAL_GLOBAL actor the owner still carries `home_firm_id` and is unchanged; (c) a FIRM_ADVISOR owner passes the schema's owner definition (validate against the product's `RequestComposition.schema.json` via the same registry `CompositionAdmission` builds; build a minimal composition from the product's fixtures or from the stored accepted composition shape with the owner swapped) and the same owner WITH `home_firm_id` is refused; (d) a LEGACY retained row (a FIRM_ADVISOR owner that still carries `home_firm_id`) is turned into a conforming owner by the reader of item 2 and then passes all five steps of `CompositionAdmission.validate` (use worker 128's method; the test may build the five-step inputs from the product's functions, with the verified-subject and profile lookups stubbed); (e) the owning advisor is admitted and another advisor / another firm refused by `authorize_current` after the change. `before_arm`: run the new tests on the tree WITHOUT your source change: (a), (c-refuse-with-field is the same as today so it passes), (d), and the FIRM_ADVISOR schema-pass case FAIL.
5. **Regression (record the counts both ways, base and with your change):** `infra/aws/lambda/investor-reporting/_scope/tests/` whole folder (the known failing `test_resolve.py` baseline stays identical), `ycharts/generate/tests/test_composition_refusal_cause.py`, `intake/tests/` whole folder, `reports/tests/` whole folder. A new failure outside your files is a BLOCKING row.
6. **Write `r40/OWNER_FIX.json`** in your deliverable folder: `cause_ref` (the AR-y-318 record), `files_changed`, `writer_change`, `reader_change` (or the BLOCKING row id), `tests` {`added`, `passed`, `failed`}, `before_arm`, `regression` {folder, base counts, fixed counts}, `opal_global_unchanged` (the evidence: a byte comparison), `claim`, `not_read`.

### ACCEPTANCE

<criterion id="AR319-y-AC1" cell_refs="AR-y-319"><invocation>python -m pytest C:/dev/wk-irpt-anlreq-129/infra/aws/lambda/investor-reporting/_scope/tests/test_ordinary_owner_composition.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`AR319-y-AC1`: the new tests (a) to (e) of item 4 pass (and fail on the tree without the change).

<criterion id="AR319-y-AC2" cell_refs="AR-y-319"><invocation>python C:/dev/wk-irpt-anlreq-129/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~129/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR319-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `interactive_access.py` to a scratch folder OUTSIDE the product tree with the writer fix undone (`home_firm_id` kept for every class), runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR319-y-AC3" cell_refs="AR-y-319"><invocation>python C:/dev/wk-irpt-anlreq-129/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~129/regress_check.py</invocation><expect>^REGRESSION-OK </expect></criterion>
`AR319-y-AC3` (a third check, with a reason: the cell edits the owner producer that the authorizer and the upload route share): you write `regress_check.py`: it runs `_scope/tests/test_ordinary_viewer.py` and prints `REGRESSION-OK ordinary_viewer 43 passed, ...` only when all 43 pass and the whole `_scope/tests` folder's failing test ids equal the base's (the known baseline, recorded in `OWNER_FIX.json`) with no new one; otherwise `REGRESSION-BAD <why>`, exit 1.

<criterion id="AR319-y-AC4J" cell_refs="AR-y-319" judgment="true"/>
`AR319-y-AC4J` (judgment, graded at L9, never by you): the writer omits `home_firm_id` for every class but OPAL_GLOBAL and fingerprints the stored owner, the legacy-row reader produces a schema-conforming owner without weakening step 4 (or the BLOCKING row says exactly why not), an OPAL_GLOBAL owner is byte-identical, the schema and the authorizer are untouched, and the owning advisor is admitted while another advisor and another firm are refused.

<expected_criteria>AR319-y-AC1 AR319-y-AC2 AR319-y-AC3 AR319-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~129/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else, in particular `docs/contracts/` (the schema: NOT edited), `_scope/ordinary_viewer.py` and `intake/uploads.py`.

<paths>
infra/aws/lambda/investor-reporting/_scope/interactive_access.py
infra/aws/lambda/investor-reporting/_scope/tests/test_ordinary_owner_composition.py
infra/aws/lambda/investor-reporting/ycharts/generate/submission.py
infra/aws/lambda/investor-reporting/reports/request_composition.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ordinary_owner_legacy_row.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-319</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~129/IRPT_ANLREQ.TO-AR-y-319.ordinary-viewer-owner-without-home-firm.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-319`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR319-y-AC1,AR319-y-AC2,AR319-y-AC3,AR319-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and tests in a worker worktree; nothing is deployed, applied or invoked. The members touched are carried by the Lambda irpt-ycharts-generate and the resident (N = 2 each: interactive_access.py, submission.py, request_composition.py); the intake release pair (the issuer's, after this cell) counts them.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; the owned-input analysis of an ordinary viewer is admitted past CompositionAdmission. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading worker 128's record (D1 fails at step 2, D6 and the control pass, the negative control passes) against the cell; the lens: a fix that edits the contract instead of the producer, a fix that drops home_firm_id from the PRINCIPAL and breaks the authorizer's condition 2, a legacy row that still fails after the fix, an OPAL_GLOBAL owner that changes, a fingerprint that no longer matches the stored owner. The cell requires the schema untouched, the principal unchanged, a legacy-row test through all five steps, a byte-identical OPAL_GLOBAL owner and a regression count both ways. NOT seen: the live function, the live profile and partner reads, any real advisor's stored owner.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings msg 7677 (S97: the cause read first, the fix a later cell under the next intake pair) and worker 128's named cause (merged `ece60105e1`). Workstream `ZG` of round 40 (the L6 limb keys one issuance to a round and workstream). Base: `AR319-y-AC1`, `AC2` and `AC3` FAIL as expected (no test file, no checker files).
- It ships with `AR-y-318` (the failing-step log and the typed owner refusal) in the next intake release under a never-widen pair, with the ticket-service pair in the same window if the CTO so rules; the widening named there: an ordinary viewer's owned-input analysis becomes REACHABLE (it is already authorized by release 29's authorizer).
