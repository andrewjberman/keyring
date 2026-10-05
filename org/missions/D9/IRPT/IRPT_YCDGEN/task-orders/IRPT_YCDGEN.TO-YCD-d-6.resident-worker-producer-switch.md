# IRPT_YCDGEN task order -- `YCD-d-6` -- ROUND 6 (THREAD): THE SERVED WORKER'S PRODUCER SWITCH (C-SWITCH)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md</decomp_doc>
<owned_cells>YCD-d-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-d-6` -- the served worker's producer switch (c-switch) (hops 2 Select; FWD-1)
- `ycharts/generate/resident_worker.py`: R6, in `ResidentAssembly.execute`.
- Tests in `ycharts/generate/tests/test_resident_worker.py` (keep every existing test passing).
- The allow list is one constant, starting with Andrew's sign-in principal id as the issuer states it in the spawn line; the test uses an invented id.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R6 The switch (PRD C-SWITCH).** In `ResidentAssembly.execute` (`ycharts/generate/resident_worker.py`, between `store.claim()` and the `ResidentGenerationWorker(...).run()` build) the producer is chosen on the server from the acting principal `record["owner"]["principal_id"]` against ONE short allow list that starts with Andrew's sign-in only. A principal on the list gets `opal_producer.produce`; every other principal takes the YCharts path unchanged. A client-sent flag never selects. No code path runs both producers on one request. The list is data in one named constant, changed only on Andrew's word; the release that removes the YCharts producer deletes the list and the branch together.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `resident_worker.py` `execute` (480-535), `poll_once` (638), `ycharts/generate/current_authority.py` (`decide`, `allowed_firm_ids`; the existing checks grade the actor's firm access and stay as they are), and `opal_producer.produce` (merged from a-6).
- This file ships through IRPT_BCKEND's release under its own never-widen half: you change code and tests only; the issuer packages the half for the CTO. No deploy.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a principal on the allow list is served by the Opal producer (tests -k allow_listed_principal_opal_producer, >= 1 passed)
- **AC2** -- a principal off the list is served by the YCharts path unchanged (tests -k other_principal_ycharts_path, >= 1 passed)
- **AC3** -- a client-sent flag does not change the producer (tests -k client_flag_never_selects, >= 1 passed)
- **AC4** -- one request never runs both producers (tests -k one_producer_per_request, >= 1 passed)
- **AC5** -- the whole test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-d-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py -q -p no:cacheprovider -k allow_listed_principal_opal_producer</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-d-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py -q -p no:cacheprovider -k other_principal_ycharts_path</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-d-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py -q -p no:cacheprovider -k client_flag_never_selects</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-d-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py -q -p no:cacheprovider -k one_producer_per_request</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-d-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-d-6.resident-worker-producer-switch.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-d-6.resident-worker-producer-switch`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, third order; starts after a-6 is merged. The never-widen half for the resident worker release goes to the CTO at the drain (msg 105387). Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>6</round>
<slot>~1</slot>
<fabric>laptop</fabric>
