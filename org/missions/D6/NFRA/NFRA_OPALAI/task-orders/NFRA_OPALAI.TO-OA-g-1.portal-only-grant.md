# NFRA_OPALAI task order -- `OA-g-1` -- ADDENDUM A2: the existing grant grammar admits a portal-only asker grant

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-g-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~9</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface; tests use injected stores.
comp-adversary: RUN -- the negative controls are AC1's zero-of-both refusal and AC2's other-channel refusal.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-g-1` (decomposition ADDENDUM A2)

**Why (row `NFRA_OPALAI-Z-S23`, CTO ruling (B), msg 25996):** Andrew admitted Alyssa Keith to "portal figures only".
The only grant the operator path can write today is the NFRA_OPLGTW Schwab-data grant:
- `app/data_entitlement.py:202-237` `parse_scope` requires non-empty `masters` (Schwab master ids), `accounts`,
  `datasets` (`dim_position/dim_balance/dim_asset`) and `columns`;
- `app/asker_scope.py` (points c and d of its docstring) honours only the grant's `query` operation, then serves the
  CALLING identity's catalog rows.

So any grant today names Schwab accounts. The CTO's direction: extend the EXISTING grammar (no second store), and
amend the contract (the OPLGTW stop is lifted).

Build, in `infra/aws/ec2/opal-gateway/`:
1. **Grammar** (`app/data_entitlement.py`, and `org/standards/NFRA_OPLGTW_CONTRACT.json` as its source):
   - a new scope dimension `portal_channels`: a list of channel ids of `app/refs/DATA_CATALOG.yaml` (the channels
     `app/graphql_plumbing/catalog_gate.py` indexes);
   - `masters`, `accounts`, `datasets` and `columns` may be EMPTY only when `portal_channels` is non-empty. Empty of
     both is Malformed;
   - a record WITHOUT `portal_channels` parses exactly as today, so every existing POLICY record keeps its meaning;
   - a portal-only grant admits NO Schwab tool (`allowed_tools`).
2. **The asker path** (`app/asker_scope.py`): when the asker's grant carries `portal_channels`, a catalog key is served
   only if its channel is one of them. Otherwise refuse, with the same deny shape. The CALLING identity's catalog_gate
   still applies on top, so the result is never wider than either side. Grants without `portal_channels` behave as
   today.
3. **The operator path** (`ops/schwab_entitlement_admin.py`): `activate` validates a portal-only candidate against the
   amended contract. A `portal_channels` entry the catalog does not hold is rejected (`CandidateRejected`).
4. **Tests** in a NEW file `tests/test_portal_grant.py`, which must NOT import moto (site Z has none). Use injected
   stores and clients. Name exactly:
   - `test_portal_grant_zero_masters_parses`: a portal-only grant parses; empty of both is Malformed; a record with no
     `portal_channels` parses as before;
   - `test_portal_only_grant_admits_no_schwab_tool`;
   - `test_asker_portal_scope_admits_granted_channel`;
   - `test_asker_portal_scope_refuses_other_channel`;
   - `test_admin_accepts_portal_only_candidate`;
   - `test_admin_rejects_unknown_portal_channel`.
   Also keep `tests/test_asker_scope.py` and `tests/test_identity_scope.py` passing.

**AMENDED by the issuer on row NFRA_OPALAI-Z-W9-S1 (no CTO ruling needed):**
5. **The owner's read-back carries the new dimension.** `app/admin_grants.py` `_grant_json` (the dashboard's
   Entitlements read) returns `portal_channels` whenever the grant carries it, so a portal-only grant never reads back
   as empty. Add `test_admin_readback_shows_portal_channels` to `tests/test_portal_grant.py`; it is graded under AC3,
   whose check becomes 3 of 3.

## 2. BOUNDS

1. No deploy (that is `OA-g-2`), no POLICY write (that is `OA-g-3`), no push, no vendor call.
2. No second grant store. `integrations/schwab/` is not edited. Existing grants keep their meaning.
3. Standing rule: REFUSE a criterion you cannot meet as written, and report the refusal with its measurement. Never
   repair, widen or route around a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py
infra/aws/ec2/opal-gateway/app/admin_grants.py
infra/aws/ec2/opal-gateway/tests/test_portal_grant.py
org/standards/NFRA_OPLGTW_CONTRACT.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_OPALAI-Z-W9-S<k>` and disarm_owner `2.0.0_SA_COO~O`. The gateway suite appends to the tracked
`infra/aws/ec2/opal-gateway/audit.jsonl`. Restore it before every commit.

## 4. PROOF OF SPEC (literal; run from your worktree root after your last commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-g-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g1.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 2 of 2; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-g-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g1.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 2 of 2; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-g-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g1.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/NFRA_OPALAI.TO-OA-g-1.portal-only-grant.proof_of_spec.json`.
Report once, with:
- the grammar change, and the contract diff in words;
- the catalog channel ids;
- the commit hashes;
- the results of `test_asker_scope.py` and `test_identity_scope.py`;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on the CTO's ruling (B) (msg 25996), which settles Andrew's call 2
(`ANDREW_DIRECT_20260926_022xZ_CTO_O_OPEN_CALLS_1_TO_6_ANSWERED.md`). Checks were dry-run at base: g1.AC1-3 FAIL
(the test file is absent).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~9</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
