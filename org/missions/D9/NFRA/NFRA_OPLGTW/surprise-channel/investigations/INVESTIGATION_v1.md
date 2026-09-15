# NFRA_OPLGTW -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~O` at L6, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only.**
Worker rows carry their slot's coordinate, `NFRA_OPLGTW-W<n>-S<k>`; a seat's row carries none.

**Why this file is opened at the issuance.** The first row was found while grounding the task orders' test criteria: the
Gateway's existing test suite does not pass at the cut base, so every "whole suite passes" criterion of this round has to
name the one known failure instead of silently inheriting it.

**Denominator at this write: 1 row** -- `NFRA_OPLGTW-S1`, 2.0.0_SA_COO~O at L6.

```json
[
  {
    "id": "NFRA_OPLGTW-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T09:10Z",
    "one_line": "The Gateway's own suite fails one test at the cut base: test_scoped_deny_by_default still lists opal_data_refresh_upload as denied to the Bloomberg service identity, while the tracked allowlist overlay grants that identity that tool.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TEST: infra/aws/ec2/opal-gateway/tests/test_identity_scope.py:32-51 @7921d898c0 -- _FRAME_III_DENIED includes 'opal_data_refresh_upload', and test_scoped_deny_by_default asserts identity_scope.check('opalbloomberg@opalinvest.com', tool) is not None for every member.",
        "OVERLAY: infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt:13 @7921d898c0 reads 'opalbloomberg@opalinvest.com opal_data_refresh_upload'; the test module's own AC-D says the overlay widens the named identity, and infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:134 carries the grant's rationale, so the grant reads as deliberate.",
        "RUN: Python 3.12.10, pytest 9.0.2, 'python -m pytest tests -q -p no:cacheprovider' from infra/aws/ec2/opal-gateway at 2026-09-15 09:03Z: '1 failed, 76 passed, 34 subtests passed'; FAILED tests/test_identity_scope.py::test_scoped_deny_by_default -- AssertionError: opal_data_refresh_upload."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round's cut would have said 'the whole infra/aws/ec2/opal-gateway/tests suite passes' as a criterion on every Gateway code cell, which assumes the suite is green at the base the workers branch from.",
    "world_is": "The suite is red at the base on one test that predates this project and belongs to the opal_portal integration's grant, not to any NFRA_OPLGTW cell. Every suite criterion in this issuance therefore deselects exactly that test by name (-k 'not test_scoped_deny_by_default') and cites this row; no worker edits the test or the overlay.",
    "notes": "INERT: the failure does not change the Gateway's runtime behaviour, which follows the overlay. OBSERVATION: it blocks nothing in this round, because the criteria name it. Whether the test or the overlay is the one to change is the owner of the opal_portal integration's grant to decide; it is outside this project's write surface."
  },
  {
    "id": "NFRA_OPLGTW-W5-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-15T10:43:23Z",
    "one_line": "The audit field list names 'master' in the same sentence that excludes raw account IDs, and the contract's masters are 8-digit account-number-shaped codes; OG-o-1 records master as given, bounded to the contract's two keys.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:282 @f0aa50dbc0 -- 'Audit fields: ... master/dataset/date ... Exclude raw account IDs, customer values, prompts, OAuth credentials, cookies, ticket secrets and complete URLs.'",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json:6-9 @1bcc827bda -- masters keyed '08242234' (SmartX) and '08335338' (BlackDiamond), both 8-digit codes.",
        "BUILD: infra/aws/ec2/opal-gateway/app/schwab_audit.py (_MASTERS, build_record) on branch wk-nfra_oplgtw-1-5 -- master is an enum of exactly those two keys; any other value (the AC5 fixture's 87654321) is dropped and named in redacted_fields; test_ogo1_ac05 asserts both halves."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-o-1 quotes the PRD: the Schwab audit record carries master/dataset/date and excludes raw account IDs. It does not say whether a Schwab master number counts as an account ID.",
    "world_is": "The contract's two masters are 8-digit account-number-shaped values, so the two clauses can be read as conflicting. The worker had to choose: master is written as given, restricted to the contract's closed set, and no other account-shaped value can enter the record. If a master number counts as a raw account ID, the field needs a hash or an alias instead, which is the spec owner's call.",
    "notes": "INERT: nothing deploys in this order, and only the two contract masters can appear in the field. OBSERVATION: no criterion is blocked; AC5's fixture uses a non-master account number."
  }
]
```
