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
    "id": "MDPF_TAXSMA-W5-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~5",
    "surfaced_at": "2026-09-15T21:20Z",
    "one_line": "PRD s.3.4 classifies additional Tax-labelled custodian candidates 'UNCONFIRMED', but no status axis or reason code in the data contract carries that value, so the expected-case manifest cannot name the candidates' status in contract vocabulary.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@671925aecc line 205: 'Discover additional Tax-labeled custodian candidates by the complete dated source population and classify them UNCONFIRMED; no automatic workbook edit or membership promotion follows.'",
        "CONTRACT org/standards/MDPF_TAXSMA_DATA_CONTRACT.json@91b11ff0c9 status_axes (business_status 7, identity_status 7, membership_date_status 3, technical_enrollment 5, value_status 4, freshness 5, run_result 6 members) and reason_codes (36 members): the token UNCONFIRMED occurs only inside REMOVED_UNCONFIRMED (lines 245 and 650), a different state (a removed prior traded row).",
        "TASK ORDER org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-v-1.expected-cases.md@91b11ff0c9 line 22: 'the contract's enumerations are the only vocabulary'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order makes the contract's enumerations the only vocabulary, and PRD s.3.4 names the additional-candidate classification UNCONFIRMED.",
    "world_is": "The contract has no UNCONFIRMED member on any axis. TX-v-1's arm A02-09 therefore states the candidate's observable without a status label: not counted live, not in the dated expected population, listed once in protected candidate evidence, no workbook write. The label that S04 (TX-m-2) emits for a candidate is unfixed by the contract.",
    "notes": "INERT: the manifest's candidate expectation does not depend on the label. OBSERVATION: whether the contract gains a candidate value or the PRD word is dropped belongs to the contract owner (the PRD author), not to any worker cell."
  }
]
```
