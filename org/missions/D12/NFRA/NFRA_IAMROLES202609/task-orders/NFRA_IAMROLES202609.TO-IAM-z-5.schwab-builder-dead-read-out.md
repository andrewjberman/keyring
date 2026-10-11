# NFRA_IAMROLES202609.TO-IAM-z-5 -- the canonical Schwab builder stops listing the deleted, claimable opal-data-schwab: latest_rps_date() reads the same monolith bronze axis as dates_to_build() (round-8 analysis E2 act (a))

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R9.md</decomp_doc>
<owned_cells>IAM-z-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~15</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (IAM-z-2 act (a); ROUND_ANALYSIS.round8.md @d14162158d E2)

```
IAM-z-2(a). WHY: s3://opal-data-schwab was deleted and reads 404, so its name is claimable by any AWS account. The canonical
Schwab orchestrator still lists it to choose its build date, and the production runner calls it WITHOUT --date
(infra/aws/ec2/canonical-schwab-runner/run-canonical.sh:61, `build_canonical_daily.py --upload`). A claimant's object names
would choose the date production builds.

THE CODE (file C:/Users/Opal Bloomberg/Desktop/ajb_workspace/data/canonical/schwab/build_canonical_daily.py, in YOUR worktree):
  :48       SRC_BUCKET = "opal-data-schwab"
  :141-145  latest_rps_date() lists Bucket=SRC_BUCKET, Prefix="01_raw/", takes the max CRS date of *.RPS keys
  :228      t1 = _normalize_date(args.date) or latest_rps_date()
  dates_to_build() (~:160-200) was re-pointed @3b01132271 to enumerate partition DIRECTORIES under
  MONOLITH_BUCKET / MONOLITH_FEED_PREFIX (8-digit segments). Read its comment block: it says why the date axis must be read
  from the same place the data is read from.

ACT:
  1. Re-point latest_rps_date() to that same monolith enumeration: the latest 8-digit partition segment under
     MONOLITH_FEED_PREFIX in MONOLITH_BUCKET, returned as YYYY-MM-DD, '' when none. Prefer one shared helper that both
     functions call over a second copy of the enumeration. Keep the function name and return contract.
  2. Remove SRC_BUCKET if nothing else uses it; otherwise leave it with a comment that it is deleted and must not be read.
     Afterwards `grep -c 'Bucket=SRC_BUCKET'` on the file must read 0, and no line may pass "opal-data-schwab" to any S3 call.
  3. Add a regression test beside the existing date-axis suite
     (data/canonical/schwab/tests/test_canonical_daily_date_axis.py; read how it loads the module and stubs S3): with a stub
     paginator, latest_rps_date() returns the max monolith partition, and NEVER asks for Bucket="opal-data-schwab" (assert on
     the buckets requested).
  4. Run `bash .tools/commit-gate.sh` on the changed .py files (py_compile + ds-precommit + ruff py39), and the suite.
  5. Do NOT stage or upload code to S3. The runner pulls s3://opal-data-bd/code/canonical/schwab; that copy is a separate
     act and is not yours.
```

## DEPENDENCIES

None. IAM-z-2(b), the grant narrowing, waits on this order's AC1.

## BOUNDS

```
LOCAL: the repository file and its test only. No S3 write, no AWS write, no run of the builder against real buckets.
Only latest_rps_date() (and a shared helper) change; dates_to_build()'s behaviour stays identical (its tests still pass).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
data/canonical/schwab/build_canonical_daily.py
data/canonical/schwab/tests/test_canonical_daily_date_axis.py
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~15/
</paths>

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-z-2"><invocation>grep -c 'Bucket=SRC_BUCKET' data/canonical/schwab/build_canonical_daily.py</invocation><expect>`0` -- the orchestrator no longer lists the deleted bucket</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-z-2"><invocation>python -m pytest -q data/canonical/schwab/tests/test_canonical_daily_date_axis.py</invocation><expect>all tests pass, including the new one that asserts latest_rps_date() never requests opal-data-schwab</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-z-2" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): does any code path of
  the orchestrator still let a claimant's bucket choose the build date, and is dates_to_build() unchanged in behaviour?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>9</round>
<workstream>SCHWAB_READER</workstream>
<slot>0.9.0_WK_NFRA_IAMROLES202609~15</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-z-5</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 9, workstream SCHWAB_READER) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** `ROUND_ANALYSIS.round8.md` @d14162158d E2 act (a) -> the issuer's ruling: the owner (0.4.0_DS_ClientPlatform) is seated on no box (0.0.0_AB_MSTR~Z msg 33383, process census of laptop, dell1, dell2 and site Z), so act (a) is re-pointed from "the owner via 0.0.0_AB_MSTR~Z" to the issuer's L7 worker (CLAUDE.md rule 27 L7) -> this order.
**Risk LOCAL:** the repository source and its test. The production runner executes the S3-staged copy (run-canonical.sh:45), which this order does not touch; that copy's restage is named in row Z-S44 with its owner.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no deploy; the runner's S3-staged code is not moved.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM resource is read or moved.
comp-adversary: RUN -- denominator of re-derived premises 3 of 3: the dead read is latest_rps_date() :141-145 (bytes printed at the cut); the production runner calls without --date (run-canonical.sh:61); the runner has written 0 run logs under s3://opal-data-bd/canonical/schwab/_runlogs/ (list read 19:2xZ, positive control: gold/ and silver/ listed under the same prefix).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (`1`); AC2 base runs the existing suite (passes) without the new test, so it is graded on the new test's presence at the drain.
