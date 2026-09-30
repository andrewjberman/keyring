# NFRA_MCPMSP task order -- `MS-c-1` -- ROUND 2, E1: the gateway identity's portal-v2 reader census and the DELTA baseline

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-c-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~1</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN -- this cell reads the live policies on opal-gateway-role (the census's IAM half). Blindness: that one role.
comp-adversary: DECLARED-NOT-APPLICABLE -- the census is the input to MS-dn-1's adversary read.
EGRESS CLASS, declared: none (Opal's own AWS account and host).
</preflight>

## 1. THE CELL -- `MS-c-1` (decomposition v2, R2.2)

PRD v0.3/v0.4 C5: the gateway's own identity must read no firm data. Today it reads `opal-data-portal-v2` for
opal-internal askers. Round 2 builds an Opal-internal reader role and later Denies the gateway identity the firm keys
(MS-dn-1, HELD). This cell measures what that Deny will touch, and records what "unchanged" means.

1. **The reader census** -> `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/r2_c1_census.json`:
   - `call_sites_scanned`: every `boto3.client("s3"...)` and `.get_object(` call site under
     `infra/aws/ec2/opal-gateway/app/**` (the denominator);
   - `readers[]`: each site that can read `opal-data-portal-v2`, as `{file, line, bucket, prefixes, identity}`, where
     `identity` is `gateway-instance-role` for a default client (known at the cut: `app/query_v0.py` `_fetch_capped`;
     `integrations/portal_index/integration.py:273-275`; `integrations/opal_discover/integration.py:228`), `firm-role`
     for `app/firm_role.py`;
   - `iam_statements[]`: every statement on `opal-gateway-role` (inline and attached, read LIVE with the aws CLI) that
     grants `s3:GetObject` on `opal-data-portal-v2`, as `{policy, resources}` (known in Terraform: `queryv0-iam.tf`
     `json/*`, `platinum/*`; `daily-reports-iam.tf` `daily-reports/*`);
   - `firm_segments[]`: the key patterns under which a firm token (`49financial`, `inflection`, `cottonwood`, from
     `graphql_plumbing/catalog_gate.KNOWN_FIRMS`) appears as a path segment in the catalog
     (`app/refs/DATA_CATALOG.yaml` `key`/`primary` fields), e.g. `platinum/mdpf/{firm}/*` -- these become the Deny's keys.
2. **The DELTA baseline** -> `.../0.9.0_WK_NFRA_MCPMSP~1/r2_c1_delta_baseline.json`: `{"keys": [{key, sha256, bytes,
   captured_at}, ...]}` for at least 6 firm-scoped catalog keys covering at least 2 firms (for example the three
   `platinum/mdpf/{inflection,cottonwood}/{aum-metrics,account-distribution,aggregate-aua-timeseries}.json`). Capture
   each on the SERVED HOST through the gateway's own code -- over SSM, `cd /opt/opal-gateway`, load `.env`, run
   `.venv/bin/python` calling `app.query_v0._fetch_capped(key)` and hashing the bytes (instance `i-07dccb1615503ac99`)
   -- never from a local guess. MS-dn-1 re-runs exactly that read after the Deny.

## 2. BOUNDS

1. Read-only everywhere: no Terraform, no apply, no gateway edit, no host write (the SSM command only reads and hashes).
2. No push, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/**`, `infra/aws/terraform/opal-gateway/*.tf`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W1-S<k>` (next free k for W1), `disarm_owner` `2.0.0_SA_COO~MS` (rows need `project`, `fabric`,
`surfaced_at`).

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-c-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/c1.AC1.sh; echo "exit=$?"</invocation><expect>call_sites_scanned=N readers=R (R <= N) iam_statements>=1 known_readers=3/3 shape=True verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-c-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/c1.AC2.sh; echo "exit=$?"</invocation><expect>keys>=6 firms>=2 shape=True live_sha_match=2/2 verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/NFRA_MCPMSP.TO-MS-c-1.portal-reader-census.proof_of_spec.json`.
Report once, with: the reader list with identities; the IAM statements; the firm segment patterns; the baseline key list;
the two check lines; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance on the CTO's round-1 analysis @5e2ff94c28 (E1) and ruling 27414. Checks dry-run at
base: AC1 FAIL as expected (census absent); AC2 FAIL as expected (baseline absent). Slot `~1` continues to MS-ir-1,
then MS-ir-2.

<status>pending</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
