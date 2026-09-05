# TO ETFS_GUARDRAIL.TO-EG-s-12 -- Inflection's lineage: the DEPLOYED bytes of inf-etf-ownership-daily diffed against the build input, and the bucket the deployed code actually reads

<to_id>ETFS_GUARDRAIL.TO-EG-s-12</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- proof-of-spec instance `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-12.inflection-deployed-bytes-vs-build-input.proof_of_spec.json` VALID (rc=0, `.tools/proof-of-spec-check.py`, long-stem name per the amended round faces). All 5 criteria S12-AC1..AC4 PASS by output (VERDICT: MISMATCH -- deployed bytes match commit `af4f123e2c` (2026-08-01), predating the committed-not-applied Orion repoint at `001a73530a`); S12-AC5 judgment RECORDED for CVO L9 grading. Rows ETFS_GUARDRAIL-W1-S4 (INERT) and ETFS_GUARDRAIL-W1-S5 (ARMED, disarm 2.0.0_SA_COO~B) filed. Flip made by the assignee per the amended BOUNDS grant (task-orders/ own-file flip, tree convention). Prior: pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S12; s.6 "ONE UNRESOLVED DEPENDENCY, CARRIED NOT BURIED"; brief s.9.2) | **Decomp cell:** `EG-s-12` | **outcome_ref:** none (a RELIES-ON row that binds ladder rung 2, `EG-s-7`) | **verb:** verify | **depends_on:** --

---

## THE CELL

`EG-s-12` (PRD s.7.2 S12): *"Inflection lineage: repo computes one bucket, slices cite another, deploy POSTDATES the last repo change"* -- claim `absent`, *"attributed, re-measured by NOBODY"*. Bound: *"Needs a deployed-bytes diff vs build input, NOT a source read. Binds rung 2."* The three facts that do not fit (brief s.9.2): repo source computes an `opal-data-assets/orion/inflection/silver/fact_positions` path; every slice 07-16 -> 09-01 cites `opal-data-inf/gold/canonical/holdings_`; the deploy (2026-08-11) postdates the last repo change (2026-08-03 @`001a73530a`). CLAUDE.md 22a: *"diff deployed bytes against the BUILD INPUT (source-map/manifest), never by filename."*

The build input: `infra/aws/lambda/ci/lambda-source-map.json` names for `inf-etf-ownership-daily` the source dir `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily` and `files` = `lambda_function.py`, `dedup_core.py`, `trading_calendar.py`; the deploy is the yang-lambda module from the S3 artifact `inf-pipeline/inf-etf-ownership-daily.zip` in `opal-313476888478-lambda-artifacts` (the module reads `CodeSha256` from the object's `content-sha256` metadata). The LIVE function's `CodeSha256` is the served side.

This is a VERIFY cell with LIVE READS and NO CHANGE. You hold no cloud identity of your own; the `.tools/aws` shim runs under the launching seat's credentials -- so every AWS read you make is recorded VERBATIM (the command and its output) in the result document, and the CVO grades what was printed, never your summary.

## DELIVERABLE

`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/inflection-deployed-bytes-vs-build-input.result.md` plus the script `deployed_bytes_diff.py` beside it. The script: (1) reads the live configuration (`FunctionName`, `CodeSha256`, `LastModified`, `Environment.Variables`, `Layers`) with `.tools/aws lambda get-function-configuration --function-name inf-etf-ownership-daily`; (2) downloads the deployed zip from `aws lambda get-function --query Code.Location` (a presigned AWS URL; read only) into `<worktree>/.scratch/`; (3) builds the repo's zip from the source map's `files` with `bash infra/aws/lambda/ci/build-zip.sh inf-etf-ownership-daily infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily <worktree>/.scratch/build lambda_function.py dedup_core.py trading_calendar.py` (or an equivalent deterministic zip of the same files if that script's output dir convention refuses -- say which); (4) compares FILE BY FILE (unzip both, sha256 each member; the zip's own bytes differ by timestamp so a whole-zip hash is not the diff) and prints ONE line `VERDICT: MATCH` or `VERDICT: MISMATCH files=<n> differing=<comma list>`; (5) prints `DEPLOYED_READS: bucket=<...> prefix=<...>` from the DEPLOYED `lambda_function.py`'s constants and env, and `REPO_READS: bucket=<...> prefix=<...>` from the worktree's copy, so rung 2 knows which bucket the producer that RUNS actually reads. The result document carries every command and output verbatim with rc, the three brief facts re-measured (the last repo commit touching the source dir; the live `LastModified`; a recent slice's `source_artifact` field read from `s3://opal-data-etfs/daily/inflection/<newest date>.json`), and the answer.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`; a `judgment="true"` criterion is RECORDED with NO verdict.

<criterion id="S12-AC1" cell_refs="EG-s-12"><invocation>.tools/aws lambda get-function-configuration --function-name inf-etf-ownership-daily --query "[FunctionName,LastModified,CodeSha256]" --output text</invocation><expect>inf-etf-ownership-daily</expect></criterion>
`S12-AC1` -- the live configuration READ (the three values recorded verbatim).

<criterion id="S12-AC2" cell_refs="EG-s-12"><invocation>python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/deployed_bytes_diff.py</invocation><expect>VERDICT:</expect></criterion>
`S12-AC2` -- the deployed-bytes diff RAN and printed its one verdict line (MATCH or MISMATCH with the differing members named; either is a valid answer -- the CELL asks the question, it does not presume the answer).

<criterion id="S12-AC3" cell_refs="EG-s-12"><invocation>git log --format="%h %ad %s" --date=short -1 -- infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/</invocation><expect>2026-</expect></criterion>
`S12-AC3` -- the last repo commit touching the source dir, re-measured (the brief says 2026-08-03 @`001a73530a`; record what git says).

<criterion id="S12-AC4" cell_refs="EG-s-12"><invocation>.tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix daily/inflection/2026-09 --query "Contents[-1].Key" --output text</invocation><expect>daily/inflection/2026-09</expect></criterion>
`S12-AC4` -- the newest September slice key READ (its `source_artifact` field is then fetched and recorded in the result: the bucket the slices CITE).

<criterion id="S12-AC5" cell_refs="EG-s-12" judgment="true"/>
`S12-AC5` -- THE ANSWER, graded by the CVO at L9: do the three brief facts now fit, which bucket and prefix the DEPLOYED code reads, and what rung 2 of the ladder (`EG-s-7`) must check for Inflection. RECORD; NO VERDICT.

<expected_criteria>S12-AC1, S12-AC2, S12-AC3, S12-AC4, S12-AC5</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) No source file changes in this cell. A path you need that it does not name is a BLOCKING row, never an override.
- **READS ONLY on the live plane.** `get-function-configuration`, `get-function` (download), `s3api list-objects-v2` / `get-object` on `opal-data-etfs/daily/inflection/`. No `update-function-code` (NEVER-9), no apply, no invoke, no write to any bucket. If a read is denied, that is a row and the honest output.
- **EVERY invocation is bounded.** `timeout 120`; a timeout is RECORDED AS THE OUTPUT. The zip download is a single presigned GET; if it exceeds the bound, retry once, then record.
- **Scratch:** `<your worktree>/.scratch/` only.
- **The relied-on producer is NOT modified** (PRD S3 bound), not even to add a print.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>` (`W1` = your slot); a MISMATCH verdict is itself worth a row naming the differing members (class OBSERVATION unless it blocks a criterion).
- **NEVER `git push`.** Report push state as MEASURED (`git ls-remote origin refs/heads/CLOUD`).

<paths>
infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/build-zip.sh
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-12`.
<owned_cells>EG-s-12</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or inf-etf-ownership-daily.
comp-iam: DECLARED-NOT-APPLICABLE -- a read-only census of a deployed function; no policy or resource is changed (the worker's own reads run under the launching seat's credentials, stated in the cell).
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`).
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S12-AC1`, `S12-AC2`, `S12-AC3`, `S12-AC4`, `S12-AC5`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-12.inflection-deployed-bytes-vs-build-input.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S12-AC1,S12-AC2,S12-AC3,S12-AC4,S12-AC5` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
