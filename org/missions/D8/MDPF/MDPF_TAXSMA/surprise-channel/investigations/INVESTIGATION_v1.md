# MDPF_TAXSMA -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~T` at L6, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only.**
Worker rows carry their slot's coordinate, `MDPF_TAXSMA-W<n>-S<k>`; a seat's row carries none.

**Why this file is opened at the issuance.** Two facts found while grounding the round's test criteria change what a
"the suite passes" criterion can honestly say, so every criterion that runs a suite names them instead of inheriting them.

**Denominator at this write: 2 rows** -- `MDPF_TAXSMA-S1`, `MDPF_TAXSMA-S2`, 2.0.0_SA_COO~T at L6.

```json
[
  {
    "id": "MDPF_TAXSMA-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-15T16:52Z",
    "one_line": "The MDPF Gold suite already fails 3 tests at the cut base, all in test_global_fold_flag2.py on the Global fold carry path that TX-a-1 and TX-a-2 edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: Python 3.12.10, 'python -m pytest data/mdpf/scripts/gold/tests -q -p no:cacheprovider' at HEAD bd2fa195c0, 2026-09-15 16:5xZ: 92 collected, '3 failed, 89 passed'.",
        "FAILED: data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_within_window_carries_and_labels (assert 'carried' == 'measured'); ::test_carry_beyond_window_absent_for_real (assert 128.0 == 120.0); ::test_carry_source_is_measured_never_interpolated (assert 'carried' == 'measured').",
        "DECOMP: org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md s.7 and bound 17 record this baseline; TX-p-1 re-measures it at its own HEAD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A cell that edits the Gold aggregation or consolidator would naturally be graded on 'the MDPF Gold suite passes', which assumes the suite is green at the base the workers branch from.",
    "world_is": "The suite is red at the base on 3 tests that predate this project. Every Gold-suite criterion in this issuance therefore reads 'fails only on the 3 pre-existing test_global_fold_flag2.py ids', and a new failure is the defect.",
    "notes": "INERT: it blocks nothing in this round because the criteria name it. OBSERVATION: whether the tests or the fold code is the one to change belongs to the Global fold's owner, not to any MDPF_TAXSMA cell."
  },
  {
    "id": "MDPF_TAXSMA-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-15T16:52Z",
    "one_line": "moto is not installed in this box's Python, so two Gateway test modules fail collection; TAXSMA's Gateway tests must not depend on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: 'python -m pytest infra/aws/ec2/opal-gateway/tests -q --co -p no:cacheprovider' at HEAD bd2fa195c0: '90 tests collected, 2 errors'.",
        "ERRORS: tests/test_access_state.py and tests/test_oauth_durable.py, each 'ModuleNotFoundError: No module named moto'; both modules belong to NFRA_OPLGTW.",
        "PROBE: 'python' and 'py -3.12' both resolve Python 3.12.10 with pandas, pyarrow, boto3, yaml, pytest, fastapi, starlette and httpx importable; moto and msal are not."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A Gateway code cell would naturally be graded on 'the Gateway suite passes', which assumes every module collects on this box.",
    "world_is": "Two modules cannot collect here without an install no order grants. TX-g-1's criterion counts the modules that collected and passed before its edit, names the two moto modules as NOT-EVALUATED on this box, and forbids a new dependency.",
    "notes": "INERT for this project. OBSERVATION: whether moto belongs in the box's Python is NFRA_OPLGTW's and the box owner's question, not this project's."
  },
  {
    "id": "MDPF_TAXSMA-S3",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-15T20:57Z",
    "one_line": "TX-g-1's issued grant omitted tests/test_principal_cutover.py, whose ROUTE_CLASS completeness assertion requires one entry for every served route; amended before spawn.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TEST: infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py:487 defines ROUTE_CLASS; :542 asserts set(ROUTE_CLASS) == set(routes) over every route app.server serves; :35 imports moto (read at HEAD 91b11ff0c9).",
        "MESSAGE: 2.0.0_SA_COO~O 97236 (20:50Z), answering notice N-1: the new route is not in ROUTE_CLASS, so whichever drain lands it goes red without the entry; NFRA_OPLGTW cells take an entries-only grant under 1.0.0_SA_CTO ruling 97203 rule C, scoped to that project.",
        "ORDER: MDPF_TAXSMA.TO-TX-g-1 as issued @955b8c6cbe granted four Gateway paths and not this test file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TX-g-1's <paths> named taxsma_workbook.py, server.py, config.py and test_taxsma_workbook.py as the whole Gateway write surface for adding GET /ms/taxsma-workbook.",
    "world_is": "Adding a served route also requires one ROUTE_CLASS entry in test_principal_cutover.py. The order was amended before its spawn to grant exactly that file for one entry, with no criterion changed; the module needs moto, absent on this box, so it is NOT-EVALUATED here.",
    "notes": "INERT after the amendment. Found by 2.0.0_SA_COO~O's reply to N-1, before any TAXSMA worker spawned; the drain merges TX-g-1's entry after NFRA_OPLGTW's own ROUTE_CLASS lines."
  },
  {
    "id": "MDPF_TAXSMA-W1-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~1",
    "surfaced_at": "2026-09-15T21:37Z",
    "one_line": "TXG1-AC22 names two moto-dependent Gateway test modules as NOT-EVALUATED; at the cut base fd2f1e4b31 four fail collection on moto, and two collected modules already fail or error.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: 'py -3.12 -m pytest infra/aws/ec2/opal-gateway/tests -q -p no:cacheprovider' at HEAD fd2f1e4b31, 2026-09-15T21:20:52Z, Gateway tree untouched: 'Interrupted: 4 errors during collection', each 'ModuleNotFoundError: No module named moto': tests/test_access_state.py, tests/test_browser_oidc.py, tests/test_oauth_durable.py, tests/test_principal_cutover.py.",
        "RUN: the same 14 modules one process each at fd2f1e4b31: tests/test_identity_scope.py '1 failed, 5 passed' (test_scoped_deny_by_default, AssertionError: opal_data_refresh_upload); tests/test_jwt_cve_lock.py '5 passed, 1 error' (test_control_valid_token_accepted, No module named moto at :43); tests/test_schwab_audit.py '1 skipped' (could not import moto); the other 7 modules pass.",
        "ORDER: org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-g-1.workbook-capability.md@50b8910af4 TXG1-AC22, '(the two moto-dependent modules named as NOT-EVALUATED on this box)'; row MDPF_TAXSMA-S2 measured '90 tests collected, 2 errors' at bd2fa195c0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TXG1-AC22 compares the Gateway modules that collected and passed before the edit with after, naming the two moto-dependent modules (row MDPF_TAXSMA-S2: test_access_state.py, test_oauth_durable.py) as NOT-EVALUATED on this box.",
    "world_is": "At fd2f1e4b31 four modules fail collection on moto, because test_principal_cutover.py and test_browser_oidc.py landed with NFRA_OPLGTW after S2's measurement, and all four are named NOT-EVALUATED. The comparison runs per TEST, not per module: test_identity_scope.py carries 1 pre-existing failure and test_jwt_cve_lock.py 1 pre-existing moto fixture error. Both are shown before and after and are not graded, and every test that passed before must still pass.",
    "notes": "INERT: the criterion is graded on the population as measured, with the before arm recorded at fd2f1e4b31 in deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/ac22_before.json before any Gateway edit. OBSERVATION: the identity_scope failure and the missing moto belong to NFRA_OPLGTW and the box owner, not to this cell."
  },
  {
    "id": "MDPF_TAXSMA-W1-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~1",
    "surfaced_at": "2026-09-15T22:02Z",
    "one_line": "Running the Gateway test modules from the Gateway directory, as TXG1-AC22 requires, appends to the TRACKED file infra/aws/ec2/opal-gateway/audit.jsonl, which is outside this order's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: the pre-edit per-module baseline at fd2f1e4b31 (cwd infra/aws/ec2/opal-gateway) left 'M infra/aws/ec2/opal-gateway/audit.jsonl', '3 insertions(+)', 0 deletions: three '_ratelimit_control' alarm records ('per-IP-AUTH', 'per-IP-global' and 'per-identity limiter error ... induced'), written by tests/test_ratelimit.py through the default AUDIT_PATH './audit.jsonl' (app/config.py:279 @fd2f1e4b31).",
        "RESTORE: the file was rewritten with its own HEAD blob's bytes (git show HEAD:<path>): git hash-object = git rev-parse HEAD:<path> = 3c69355bcda895e2e0fbd9fef0d18284534d6dd0, 'git diff --quiet HEAD -- infra/aws/ec2/opal-gateway' rc=0, 0 untracked; porcelain status still reads ' M' from a stale stat entry on this core.autocrlf=true box, so the probe tests content equality instead.",
        "PROBE: deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py now points every pytest it starts at a scratch AUDIT_PATH, so neither AC22 arm writes the tracked file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TX-g-1's write grant is its <paths> block plus its deliverables folder, and TXG1-AC22 runs the Gateway test modules before and after the edit.",
    "world_is": "One of those modules (test_ratelimit.py) writes three records into the tracked Gateway audit.jsonl whenever it runs from the Gateway directory, so running the criterion as written touched a file outside the grant. The worker restored the file's bytes to HEAD (blob 3c69355bcd), commits nothing under that path, and runs its own measurements with AUDIT_PATH redirected to scratch.",
    "notes": "INERT for this cell once the file is back at its HEAD blob and every later run redirects AUDIT_PATH. OBSERVATION: whether test_ratelimit.py should patch AUDIT_PATH, and whether audit.jsonl should be tracked at all, belongs to NFRA_OPLGTW."
  },
  {
    "id": "MDPF_TAXSMA-W1-S3",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~1",
    "surfaced_at": "2026-09-15T22:35Z",
    "one_line": "The TXG1-AC22 before-record at fd2f1e4b31 reads tests/test_schwab_engine.py::test_ogq1_ac02 FAILED in both probe records (bar 0.25 s) though the first shell run passed it, so row W1-S1's 'the other 7 modules pass' holds for 6.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: shell loop, one process per module, finished 2026-09-15T21:36Z at fd2f1e4b31: tests/test_schwab_engine.py '13 passed in 41.02s'.",
        "RUN: probes/tx_g_1.py AC22 --record-before at fd2f1e4b31, Gateway tree content-equal to HEAD: first record (the module beside the others) 'assert 1.005868499991484 < 0.25'; second record (the module alone, first) 'assert 0.48001869998755864 < 0.25', recorded_at 2026-09-15T22:35:23Z in deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/ac22_before.json.",
        "TEST: tests/test_schwab_engine.py:259 @fd2f1e4b31 'assert child_lag < 0.25'; row NFRA_OPLGTW-W3-S12 records that module's lag bar as load-sensitive."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TXG1-AC22 grades that the Gateway tests which passed before the edit still pass after it; row MDPF_TAXSMA-W1-S1 states that at fd2f1e4b31 every module other than the four moto modules, test_identity_scope.py, test_jwt_cve_lock.py and test_schwab_audit.py passes.",
    "world_is": "test_ogq1_ac02's lag bar failed in 2 of 2 probe records and passed in 1 shell run. The committed before arm therefore counts it as failing BEFORE the edit: it is shown before and after and is not graded, and the passed-before population is 12 of that module's 13 tests.",
    "notes": "INERT: AC22's grading is deterministic whichever way the timing lands, because a test failing before is never a regression and a test passing before must still pass. OBSERVATION: the bar's load sensitivity belongs to NFRA_OPLGTW (W3-S12), not to this cell."
  }
]
```
