# NFRA_MCPORTAL task order -- `MP-g-1` -- ROUND 2, E1 capture + E6 read: the gateway records the header's claim keys and serves the whole history

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-g-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build cell; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface is written here (the gateway's read grant is MP-b-2's Terraform).
comp-adversary: DECLARED-NOT-APPLICABLE -- enrichment round of a thread.
EGRESS CLASS, declared: NONE. Tests use stubs; no network.
</preflight>

## 1. THE CELL -- `MP-g-1` (round 2, decomposition section R2.1)

The gateway at `infra/aws/ec2/opal-gateway/` serves Andrew's dashboard behind `app/owner_gate.py`, which verifies the
ALB-signed `x-amzn-oidc-data` header through `app/identity.py`'s `_alb_oidc_identity` and matches the email. Two gaps:
- nothing records WHICH claims that verified header carries, and the grant writer's owner key depends on it (a later
  cell reads it);
- `GET /api/admin/changes` (`app/admin_grants.py:174-199`) answers for one principal only.

Build:
1. **The capture** (`app/owner_gate.py`, `app/admin_api.py`).
   - On a verified OWNER request, print ONE line to stdout (the service journal), once per process:
     `OWNER-HEADER-CLAIMS keys=<sorted comma-separated claim keys> oid=<value|ABSENT> sub=<value|ABSENT> iat=<PRESENT|ABSENT> exp=<PRESENT|ABSENT>`.
   - No other claim VALUE is ever printed: no email, no name.
   - `GET /api/admin/whoami` returns, to the owner only, `{"email", "claim_keys", "oid", "sub"}`.
   - A non-owner or unverified request is refused as today.
2. **The whole history** (`app/admin_grants.py`, `app/config.py`).
   - `GET /api/admin/changes` with NO query parameters reads the grant writer's own table, named by env
     `MCPORTAL_CHANGES_TABLE`, across ALL principals, newest first.
   - With `tid` and `oid` it filters to that principal.
   - It reads only (Query/Scan/GetItem). A table that is unset or unreachable answers 503 with a reason, never a crash.
   - The round-1 per-principal `operator_audit` read may stay as a fallback only when the table is unset; say which.
3. **`tests/test_admin_round2.py`** (new), with stubs for the header verification and the table (never the network),
   naming exactly:
   - `test_whoami_returns_claim_keys_to_owner`
   - `test_claim_keys_logged_once_without_other_values` (a planted name/email value never appears in the line)
   - `test_changes_reads_writer_table_across_principals` (two principals, newest first)
   - `test_changes_table_unreachable_is_503`

## 2. BOUNDS

1. Nothing is deployed by this order. The existing `tests/test_owner_gate.py` and `tests/test_admin_grants.py` stay
   green; `/sprint*`, `/mcp` and every other route are untouched.
2. The gateway writes nothing. No handler may reach a store write API.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/owner_gate.py
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/opal-gateway/app/admin_grants.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/tests/test_admin_round2.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `app/identity.py`, `app/access_state.py`, `tests/conftest.py`, `tests/test_owner_gate.py`,
`tests/test_admin_grants.py` (under `infra/aws/ec2/opal-gateway/`).

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPORTAL-Z-W2-S<k>` (next free k for W2).

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-g-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/g1.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 2 of 2; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-g-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/g1.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 2 of 2; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/NFRA_MCPORTAL.TO-MP-g-1.claims-capture-and-history.proof_of_spec.json`.
Report once:
- what you changed and where, and the commit hash;
- the exact line format as built;
- whether the per-principal fallback stayed;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E1's capture (the measurement is G-HDR plus MP-a-1's read) and E6's read (R-4). Chain B's root; the
slot continues with MP-d-1.

<status>complete</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
