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
  },
  {
    "id": "NFRA_OPLGTW-W3-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T10:42Z",
    "one_line": "Neither OG-d-1's order, OG-i-1's order nor the contract names the access-state table's key attribute names, whether it has a sort key, or its TTL attribute; the adapter chose pk (HASH) + sk (RANGE) and expires_at as both logical expiry and TTL attribute while OG-i-1 designs the table in parallel.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-d-1.access-state-adapter.md:22-35 @2fdc84e250 -- names record types, namespaces, consistency and the TTL policy; names no attribute, key schema or TTL attribute.",
        "TO: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md:65 @2fdc84e250 -- OGI1-AC4 grades 'the TTL attribute set and the designed key schema' without naming either.",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json state_store @2fdc84e250 -- fields service, table, region, account, record_types, consistency, ttl, key_namespaces, runtime_policy_access; no attribute-name or key-schema field.",
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:193 @2fdc84e250 -- 'The DynamoDB partition key separates POLICY#<tid>#<oid> records (profile, grant, approval, operator audit)': several records under one partition key, which implies a sort key without naming it.",
        "ADAPTER: infra/aws/ec2/opal-gateway/app/access_state.py on branch wk-nfra_oplgtw-1-3 -- PK='pk', SK='sk', RECORD_TYPE='record_type', EXPIRES_AT='expires_at', module constants in one place."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order specifies the adapter's namespaces, record types, strong reads, conditional writes and logical expiry against the table OG-i-1 builds in parallel, but states no attribute names, no key schema and no TTL attribute.",
    "world_is": "The adapter had to choose them: a composite key pk (HASH, S) + sk (RANGE, S), record_type on every item, and expires_at (integer epoch seconds) as both the logical expiry and the TTL attribute. If OG-i-1's table uses other names, every adapter call against the live table fails with a ValidationException, which the adapter maps to DEPENDENCY_UNAVAILABLE: closed, but the feature never works. A different TTL attribute would leave expired RUNTIME records uncollected (cleanup only; authorization unaffected).",
    "notes": "ARMED: left alone, the two cells' drains can land a table and an adapter that disagree, and no offline test sees it because moto builds whatever key schema the test declares. OG-i-1's live arm or the first on-host call is the first instrument that can see it. Reconciling is one edit of the constants on either side."
  },
  {
    "id": "NFRA_OPLGTW-W3-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T10:50Z",
    "one_line": "Running the Gateway suite the way row NFRA_OPLGTW-S1 records it appends three lines to the tracked infra/aws/ec2/opal-gateway/audit.jsonl, a path outside every Gateway code cell's write grant, so a worker who runs the suite leaves a tracked file modified that its grant forbids it to restore.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: from infra/aws/ec2/opal-gateway, '.venv-og/Scripts/python -m pytest tests -q -p no:cacheprovider' on branch wk-nfra_oplgtw-1-3 at 2026-09-15 ~10:45Z: '1 failed, 83 passed, 34 subtests passed' (the failure is S1's test_scoped_deny_by_default); afterwards 'git diff --stat -- infra/aws/ec2/opal-gateway/audit.jsonl' reads '1 file changed, 3 insertions(+)'.",
        "WRITER: infra/aws/ec2/opal-gateway/app/audit.py:29-33 @2fdc84e250 -- _emit appends every record to _cfg.AUDIT_PATH; the added lines are _ratelimit_control alarm records of the kind test_ratelimit.py induces.",
        "GRANT: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-d-1.access-state-adapter.md:88-93 @2fdc84e250 -- the <paths> block does not name audit.jsonl."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The grant limits a worker's writes to its <paths> block, and the round's suite criteria (row NFRA_OPLGTW-S1) have Gateway code workers run the whole infra/aws/ec2/opal-gateway/tests suite.",
    "world_is": "The suite run writes the tracked audit.jsonl. This worker did not restore it (a restore is a write outside the grant) and did not commit it; it stays modified in the worktree at /c/tmp/wk-oplgtw-1-3 only. Every later worker that runs the suite will do the same.",
    "notes": "INERT: nothing is committed, and the drain merges commits, not worktree changes. OBSERVATION: blocks nothing. Whether the suite should write to a temporary AUDIT_PATH is for the owner of the Gateway test harness to decide."
  },
  {
    "id": "NFRA_OPLGTW-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T11:25Z",
    "one_line": "Disarm of W3-S1 by its named owner: the table OG-i-1 declares uses exactly the adapter's key names (pk HASH, sk RANGE, TTL expires_at), and the COO binds the applied-plane check to OG-i-1's drain.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADAPTER: infra/aws/ec2/opal-gateway/app/access_state.py:48-51 @8d8b221ee6 (merged) -- PK = \"pk\", SK = \"sk\", EXPIRES_AT = \"expires_at\".",
        "TABLE (declared): infra/aws/terraform/opal-gateway/schwab_access_state.tf on branch wk-nfra_oplgtw-1-1 @59b567eed0 -- hash_key = \"pk\" (type S), range_key = \"sk\" (type S), ttl attribute_name = local.access_state_ttl_attr = \"expires_at\"; read at 11:1xZ from the worker's own commit, not from a message.",
        "NOT YET APPLIED: OG-i-1 refused its plan (row W1-S1) and applied nothing, so the agreement is at the DESIRED plane only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W3-S1 names 2.0.0_SA_COO~O as the disarm owner of the risk that the adapter's key names and OG-i-1's table disagree.",
    "world_is": "The two agree name for name in the declared state. The residual is the applied plane: when OG-i-1 re-runs and applies, 2.0.0_SA_COO~O reads its AC4 describe-table readback at the drain and does not merge OG-i-1's branch unless the live key schema is pk/sk and the TTL attribute is expires_at. A mismatch there is a new row and a hold on the merge, not a silent pass.",
    "notes": "Disarms W3-S1 in the declared plane and moves the applied-plane residue to a named act at a named moment (OG-i-1's drain) by the named owner. INERT: no live table exists yet. The adjudication of W3-S1 is 3.0.0_SA_CVO's at L9."
  }
]
```
