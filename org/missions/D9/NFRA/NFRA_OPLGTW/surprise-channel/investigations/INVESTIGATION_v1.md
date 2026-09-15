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
    "id": "NFRA_OPLGTW-W4-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "The task order's marker census (361 hits over 172,084 files) does not reproduce in this worker's worktree: the same comp-find invocation read 128 hits in 53 files over 32,970 files scanned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-c-1.closure-contract.md:39-40 @1bcc827bda -- 'measured at the cut by an unscoped read (comp-find meta/complete --files --all, 361 hits over 172,084 files)'.",
        "RUN: comp-find 'meta/complete' --files --all in /c/tmp/wk-oplgtw-1-4 (branch wk-nfra_oplgtw-1-4, HEAD 1bcc827bda) before 11:11Z 2026-09-15, rc=0: 'DENOMINATOR: 128 hit(s) across 32970 file(s) scanned in scope [corpus=all] | 3 EPHEMERAL-FLOOR ... | 1870 BINARY', 'PAGE 1 of 1 (showing 53 of 53)'.",
        "CONTENT: the four executed readers the order names or implies are in both reads -- infra/aws/terraform/opal-assets/silver.tf, infra/aws/terraform/opal-assets/advi_49f_floor.tf, data/assets/scripts/silver/conversion_manifest.py and its vendored copy under infra/aws/lambda/opal-assets/opal-assets-silver-schwab/."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGC1-AC13 re-runs the cut's unscoped census 'with its own denominator'; the order quotes that census as 361 hits over 172,084 files.",
    "world_is": "The corpus=all denominator is the CHECKOUT's, and a fresh linked worktree carries tracked files only -- none of the shared tree's untracked or gitignored files (the shared tree's git status lists .worktrees/, archive/, .scratch_* and other untracked directories). The same invocation therefore reads 32,970 files, not 172,084. The AC13 census in this worker's deliverables carries its own denominator; it is not the cut's population.",
    "notes": "INERT: every executed reader of the marker is tracked, so the narrower corpus loses no consumer this criterion is about -- the files it cannot see are untracked scratch, archives and worktrees. Recorded so an L9 reader comparing the two denominators does not read the difference as a coverage loss. The worker did not read the shared tree (its write and read surface is its own worktree)."
  },
  {
    "id": "NFRA_OPLGTW-W4-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "Exactly one qualified closure per date rests on S3's conditional PUT (If-None-Match / If-Match), and the Schwab silver Lambda runs python3.11 on the runtime's own boto3 -- no botocore is vendored or pinned, so whether the deployed client can send those conditions is unmeasured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUNTIME: infra/aws/terraform/opal-assets/silver.tf:592 @1bcc827bda -- 'schwab = { memory = 3008, timeout = 600, runtime = \"python3.11\", layers = [data.aws_lambda_layer_version.pandas_pyarrow.arn] }'.",
        "PACKAGE: infra/aws/lambda/opal-assets/opal-assets-silver-schwab/ @1bcc827bda holds 13 files (BUILD_MANIFEST.json, backfill_status.py, conversion_manifest.py, crs_reader.py, cs_reader.py, lambda_function.py, schwab_conversion.py, schwab_projections.py, schwab_runtime.py, schwab_schemas.py, set_identity_guard.py, silver_registry.py, stream_parquet.py) -- no boto3 or botocore.",
        "GRANT: infra/aws/terraform/opal-assets/silver.tf:320-336 @1bcc827bda -- s3:PutObject and s3:GetObject on schwab/{master}/meta/*, which is all the conditional write and its re-read need.",
        "CODE: data/assets/scripts/silver/conversion_manifest.py _client_lacks_conditional_writes / _write_closure_marker at this worker's commit -- a client that refuses the parameters (botocore ParamValidationError) writes the v1 marker unchanged with closure.write_guard = 'unconditional' and status 'incomplete'; exercised in test_ogc1_ac08."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGC1-AC8: 'concurrent completion yields exactly one qualified closure'; this cell is built and tested, not deployed -- the deploy and replay are OG-c-2's.",
    "world_is": "The only S3 primitive that gives exactly-one under concurrency is the conditional PUT, which botocore accepts only in releases that know IfNoneMatch and IfMatch on put_object. The deployed runtime's botocore version is not pinned anywhere in the repo, so the premise the mechanism depends on is unmeasured from here. The code fails closed for the closure and safe for v1: if the client refuses the conditions, the v1 marker still lands unchanged and no date ever qualifies.",
    "notes": "INERT: left alone the failure mode is 'no date qualifies' with UNGUARDED_WRITE named in every record, never a wrong qualified closure and never a changed v1 field. OG-c-2 is the cell that can read the deployed runtime; its replay criterion ('each replayed record validates against OG-c-1's schema') would read UNGUARDED_WRITE rather than pass silently."
  },
  {
    "id": "NFRA_OPLGTW-W4-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "The producer holds no declared per-day expected source set, so the closure's 'expected source partitions' are the bronze objects observed for the date when the closure is composed -- a type that lands after a qualified closure is not expected by it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GUARD: data/assets/scripts/silver/set_identity_guard.py:24-26 @1bcc827bda -- 'Per-master type sets DIFFER BY CONSTRUCTION ... so the expected-table map derives from the BRONZE CENSUS of the lane, never from a fixed cross-master list.'",
        "DECLARED: data/assets/scripts/silver/conversion_manifest.py:242-245 @1bcc827bda -- declared_not_written 'carries fact_rlw on every date until that spec is resolved'; the SPECS-declared list names 17 fact tables and neither master receives all of them.",
        "DAY LAW: data/assets/scripts/silver/schwab_conversion.py:95 @1bcc827bda -- NON_OPTIONAL = ('RLD',), the only day-level requirement the producer states (assert_rld_covered, :214-245).",
        "RECORD: the closure carries expected_source_basis ('OBSERVED ...') and required_types ['rld'] at this worker's commit; test_ogc1_ac04 shows a later landing re-composing the same date to qualified."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.2 C3 @f0aa50dbc0: 'include ... expected source partitions ... Publish qualified closure only after the complete expected set is reconciled.'",
    "world_is": "Nothing in the producer or the vendor feed declares which source types a given master delivers on a given date. The closure therefore reconciles against the bronze observed at composition (plus the RLD law) and states that basis on the record. Every observed partition must reconcile, but a type that has not landed yet is not in the expected set, so a day can qualify and later be superseded when that type lands.",
    "notes": "INERT: a table whose source has not landed is absent from the closure and cannot be served as present, and the superseding closure is written by the next completion. Whether 'expected' should instead be a DECLARED per-master type set is a spec question for the PRD owner, 1.0.0_SA_CTO; this cell does not invent that declaration."
  },
  {
    "id": "NFRA_OPLGTW-W4-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "Exactly-one-qualified-closure means a run whose composition equals the qualified closure already at the key writes nothing, so the accelerator (s3:ObjectCreated on schwab/08335338/meta/complete/) fires once per distinct closure rather than once per clean lane run; no v1 field is removed, renamed or changed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CONSUMER: infra/aws/terraform/opal-assets/silver.tf:756-760 @1bcc827bda -- lambda_function 'advi-49f-silver-complete-accelerator', events ['s3:ObjectCreated:*'], filter_prefix 'schwab/08335338/meta/complete/', filter_suffix '.json'.",
        "TARGET: infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py:124-127 @1bcc827bda -- reads Records[0].s3.object.key and nothing of the marker body.",
        "RECTANGLE: the task order quotes the certified L4 rectangle @c9a44aa896 -- 'Each run can replace the same date-keyed marker.'",
        "CODE: conversion_manifest.py _write_closure_marker's ALREADY_QUALIFIED branch at this worker's commit; test_ogc1_ac08 asserts one marker write for a two-run race."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "'Existing consumers you must not break ... none reads a field this cell removes or renames' (OGC1-AC13), and OGC1-AC8 'concurrent completion yields exactly one qualified closure'.",
    "world_is": "The field set is unchanged, but the write CADENCE the accelerator observes changes. A completion whose closure is identical to the qualified one already published writes no object, so it no longer re-fires the gold dispatcher. A new date, an incomplete record, an incomplete-to-qualified change and a superseding overwrite all still write, and so all still fire.",
    "notes": "INERT: the floor (advi_49f_floor.tf, cron(45 12 * * ? *)) remains the 49F chain's production trigger and is untouched, and a suppressed fire is one whose information the dispatcher already had. Recorded because it is a behaviour change visible to an existing consumer that no field census can see; OG-c-2's G-B never-widen sign-off covers the act's blast radius and can name it."
  }
]
```
