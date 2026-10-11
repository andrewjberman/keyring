# NFRA_IAMROLES202609.TO-IAM-z-6 -- fred-data-ingestion retires its raw-series write to the 404 opal-market-update, so the daily yield-curve fold runs and the portal's yield_curve_fred.json (frozen since 2026-08-05) resumes (CTO ruling @3e091a9436)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R9.md</decomp_doc>
<owned_cells>IAM-z-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (CTO_RULING_IAMROLES_FRED_DESTINATION_RETIRE_RAW_WRITE_20261011_Z.md @3e091a9436; your rows Z-S45, Z-S48)

```
IAM-z-6. WHY: fred-data-ingestion has no env keys, so S3_BUCKET defaults to the 404 opal-market-update
(infra/aws/lambda/fred-data-ingestion/lambda_fred_ingestion.py:257). process_frequency() writes the raw series there
(put_object at :130 and :144) and the handler returns 500 BEFORE the daily yield-curve fold (:276-291). The fold is the only
live producer of s3://opal-data-portal-v2/json/macro/yield_curve_fred.json, a SERVED portal artifact last written
2026-08-05T23:02:30Z. A comp-find census found no live reader of the raw series, so the write is RETIRED, not re-pointed.

ACT: the code no longer writes the raw series to S3, and the fold no longer sits behind that write. Choose the form (e.g.
drop process_frequency's put_object calls and the S3_BUCKET default; keep the FRED fetch only if something still uses it) and
NAME it in the survey; the pair signs that form. Weekly and monthly runs must not start failing for a new reason.

PHASE A -- no AWS write:
  1. In YOUR OWN worktree, edit lambda_fred_ingestion.py. Build the zip locally the way
     infra/aws/lambda/ci/build-and-upload.sh fred-pipeline fred-data-ingestion would, WITHOUT uploading; record its
     content-sha256 and the file list. Read the deployed function's code (get-function -> Code.Location) and diff the
     handler against the repo base, to show the deployed bytes ARE the base before your edit.
  2. Read the served key's current version: s3api list-object-versions opal-data-portal-v2
     json/macro/yield_curve_fred.json -> the latest VersionId and LastModified: that is the rollback.
  3. Plan fred-pipeline with -target=aws_lambda_function.fred_data_ingestion against the artifact you WOULD upload (or state
     why the plan can only show the change after upload, and what the plan reads before it).
  4. Write org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/fred/FRED_SURVEY.md with the
     form chosen, the diff, the zip sha, the deployed-vs-base diff, the rollback VersionId, and exactly:
       ROLLBACK-VERSION: opal-data-portal-v2/json/macro/yield_curve_fred.json <VersionId>
     Commit the survey only. STOP. Report to 2.0.0_SA_COO~ZI. The pair is
     ledger/NEVER_WIDEN_ROUND9_Z-6_{COO,CTO}_HALF.md; its blast radius is that one served key plus the function's code, and
     it covers both branches (the fold writes 10 valued tenors / the fold fails and the key stays at its prior version).

PHASE B -- only on the issuer's GO after both halves are SIGNED:
  5. Read .open_deploys/ for fred-pipeline; open a NEVER-2 entry `iamroles-r9-fred-retire`.
  6. Commit the code on your worktree branch; upload with build-and-upload.sh; `safe-apply` -target the function; drain the
     same session. Never update-function-code.
  7. After the NEXT SCHEDULED daily run (cron(0 23 * * ? *)), record in .../round9/fred/POST_APPLY.md, exactly:
       FRED-RUN: statusCode=<n> yield_curve_success=<true|false>
       SERVED-KEY: LastModified=<iso> as_of=<date in the object>
     read from the run's own log line and a head-object. If the fold failed, restore nothing on your own: the key is
     unchanged by a failure; file a row and report. Then close the entry.
```

## DEPENDENCIES

None. Serializes with IAM-z-1..z-3 on `.open_deploys/`. Independent of z-1's narrowing of the opal-market-update grant.

## BOUNDS

```
Only fred-data-ingestion's code changes. No env, no schedule, no IAM, no fred-macro-ingestion change. One served key moves.
Terraform deploy only (NEVER-9: no update-function-code); safe-apply -target; the NEVER-2 entry opens first and closes last.
Never write the served key by hand. G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/lambda/fred-data-ingestion/lambda_fred_ingestion.py
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/fred/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-z-6.fred-retire-dead-raw-write.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-z-6).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-z-6"><invocation>bash -c ".tools/aws s3api head-object --bucket opal-data-portal-v2 --key json/macro/yield_curve_fred.json --query LastModified --output text"</invocation><expect>a timestamp AFTER 2026-10-11T22:59:00 -- the scheduled daily run wrote the served key (the base reads 2026-08-05T23:02:30+00:00)</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-z-6"><invocation>grep -c -E '^FRED-RUN: statusCode=200 yield_curve_success=true$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/fred/POST_APPLY.md</invocation><expect>`1` -- the scheduled run returned 200 with the fold succeeding, as read from the run's own log</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-z-6"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r9-fred-retire') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r9-fred-retire* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=1`</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-z-6" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): does the served
  yield curve carry 10 valued tenors as of the last trading day, and did no other run frequency start failing?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>complete</status>
<round>9</round>
<workstream>FRED_RETIRE</workstream>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-z-6</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 9, Addendum 1, workstream FRED_RETIRE) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** rows Z-S45 (0.7.0_AE_CloudOps~IR) and Z-S48 (issuer) -> issuer [DECISION] msg 33392 -> `1.0.0_SA_CTO~Z` ruling @3e091a9436 (msg 33394) -> DECOMP_R9 section 7 -> this issuance.
**Risk WORLD:** a Lambda code deploy that moves one served portal key; two phases under its own never-widen pair.
<preflight>
comp-schedule: RUN -- fred-pipeline/eventbridge.tf:17 daily cron(0 23 * * ? *); weekly :45 THU 14:00, monthly :73 first FRI 15:00; the grade reads the next daily fire after PHASE B.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM document moves in this cell (z-1 owns the opal-market-update grant).
comp-adversary: RUN -- denominator of re-derived premises 3 of 3: the served key's LastModified 2026-08-05T23:02:30Z (head-object 20:2xZ); the handler order :257 -> :272 process_frequency -> :276 fold (bytes printed at the cut); opal-data-portal-v2 versioning Enabled (rollback by version).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (2026-08-05T23:02:30+00:00); AC2 base FAIL as expected (file absent); AC3 base FAIL as expected (`open=0 closed=0`).
