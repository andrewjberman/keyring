# NFRA_MCPMSP task order -- `MS-ig-1` -- ROUND 2, E1: query_v0 reads through the Opal-internal reader role

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-ig-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~2</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- it assumes a config-supplied ARN; the role is MS-ir-2's.
comp-adversary: DECLARED-NOT-APPLICABLE -- the no-fallback test is this cell's adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-ig-1` (decomposition v2, R2.2)

`infra/aws/ec2/opal-gateway/app/query_v0.py` `_fetch_capped(key)` (`:94-110`) reads `opal-data-portal-v2` with the
gateway instance role's own default client (`_s3_client = boto3.client("s3")`). It serves `/query/v0` AND the
opal-internal asker path (`asker_scope.handle_asker_query` calls it). PRD C5: the gateway identity will be Denied the
firm keys (MS-dn-1, later); opal-internal reads must first move to the Opal-internal reader role
(`gateway-global-internal-reader-role`, applied by another cell this round).

Build:
1. **`app/internal_role.py` (new):** `s3_client()` returns an S3 client built from credentials assumed (`sts:AssumeRole`)
   from env `INTERNAL_READER_ROLE_ARN` (read at call time with `os.environ`, as `asker_scope.max_age_seconds` does -- do
   NOT edit `app/config.py`), cached until shortly before expiry; env UNSET -> returns `None` (the caller keeps today's
   client, so a release before the role exists moves nothing). The same pattern as `app/firm_role.py` (read it).
2. **`app/query_v0.py`:** `_fetch_capped` uses `internal_role.s3_client()` when it returns a client, else today's
   `_s3_client`. With the ARN SET, an AssumeRole failure REFUSES the read (raise; the callers already turn errors into
   refusals) -- never a silent fall back to the gateway identity. The byte cap, `BUCKET` and every other behaviour stay.
3. **`tests/test_mcpmsp_internal_role.py` (new)** with at least: `test_unset_arn_keeps_existing_client`,
   `test_set_arn_reads_via_internal_role`, `test_byte_cap_holds_on_internal_role`,
   `test_assume_failure_refuses_without_fallback` (a planted default client that fails the test if touched), with fake
   STS/S3 in the style of `tests/test_mcpmsp_asker_firm.py`.

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. `asker_scope.py`, `config.py`, `firm_role.py`, every integration and
   every other gateway module are read-only (others own them this round).
2. No push, no vendor call. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/query_v0.py
infra/aws/ec2/opal-gateway/tests/test_mcpmsp_internal_role.py
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~2/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/{firm_role,asker_scope,config}.py`, `infra/aws/ec2/opal-gateway/tests/`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W2-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-ig-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1g.AC1.sh; echo "exit=$?"</invocation><expect>pytest: N passed; test_unset_arn_keeps_existing_client=1 test_set_arn_reads_via_internal_role=1 test_byte_cap_holds_on_internal_role=1 test_assume_failure_refuses_without_fallback=1 (each >=1, 0 failed) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-ig-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1g.AC2.sh; echo "exit=$?"</invocation><expect>asker + adapter + round-1 suites: >=48 passed, 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~2/NFRA_MCPMSP.TO-MS-ig-1.query-v0-internal-route.proof_of_spec.json`.
Report once, with: the two check lines; the commit hash; any row. Then STOP.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (E1). Checks dry-run at base: AC1 FAIL as expected (test file absent); AC2 PASS as
expected (48 passed, the control). No open sibling order writes `query_v0.py` at the cut (measured). Slot `~2` is chain B
alone (MS-rx-1 takes a fresh slot `~8`: the replay is a second seat's).

<status>pending</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
