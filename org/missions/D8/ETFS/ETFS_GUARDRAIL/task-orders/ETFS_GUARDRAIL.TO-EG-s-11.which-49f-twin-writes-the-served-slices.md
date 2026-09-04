# TO ETFS_GUARDRAIL.TO-EG-s-11 -- which bd-49f twin WRITES the served slices: the live plane read from both ends, so the port lands in the producer that runs and not the one that merely exists

<to_id>ETFS_GUARDRAIL.TO-EG-s-11</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S11; s.7.4 last paragraph) | **Decomp cell:** `EG-s-11` | **outcome_ref:** none (a RELIES-ON row beneath FWD-1; the WRONG-OBJECT risk under `EG-s-2`) | **verb:** verify | **depends_on:** --

---

## THE CELL

`EG-s-11` (PRD s.7.2 S11): *"`bd-49f-etf-ownership-daily` vs its `-canonical` twin -- which writes the served slices"* -- claim `absent`, *"4 producer dirs; discriminator NOT run"*. Bound: *"WRONG-OBJECT risk under S2; comp-read cannot detect a wrong file (rule 21 limb ii)."* PRD s.7.4: *"S11 is the one most likely to move S2's address out from under this table."*

What the repo says at HEAD (read by the issuer, not to be trusted over the plane): `bd-49f-etf-ownership-daily` -- Terraform `infra/aws/terraform/bd-pipeline/bd-49f-etf-ownership-daily.tf` (module `bd_49f_etf_ownership_daily`, scheduled floor `cron(45 10 * * ? *)`, writes `daily/49financial/{date}.json`, source map entry present); `bd-49f-etf-ownership-daily-canonical` -- a lambda dir whose header says *"NOT YET DEPLOYED: the source is frozen (06-18); going live waits on the silver fire"*, NO Terraform file names it, ABSENT from the source map. The DESIRED plane says the first twin is the writer. **The cell asks the APPLIED plane and the served objects**, because a producer can exist in AWS without a Terraform file (drift) and a slice's writer is a fact about the slice.

## DELIVERABLE

`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/which-49f-twin-writes-the-served-slices.result.md` plus the script `twin_writer_census.py` beside it. The script, READ-ONLY: (1) lists the live functions whose name starts with `bd-49f-etf-ownership` (`.tools/aws lambda list-functions`, paginated, count client-side); (2) for each live one: configuration (`OUTPUT_PREFIX` env, `LastModified`, `CodeSha256`), the EventBridge rules targeting it (`.tools/aws events list-rule-names-by-target --target-arn <fn arn>`), and the newest CloudWatch log events matching `OK: wrote` in `/aws/lambda/<fn>` over the last 3 days (`logs filter-log-events --start-time <epoch ms> --filter-pattern "OK: wrote" --limit 20`); (3) the three newest served slices `s3://opal-data-etfs/daily/49financial/` (`s3api list-objects-v2`, sorted by `LastModified`) with their `LastModified` and, from the object body, `source_artifact` and `source_as_of`; (4) prints ONE line `WRITER=<function-name> EVIDENCE=<n log lines within 5 min of a served slice's LastModified>` (or `WRITER=UNDETERMINED` with the reason) and one line per twin `TWIN=<name> LIVE=<bool> SCHEDULED=<rules> LAST_WROTE=<ts or none>`. The result document carries every command and its output verbatim with rc and denominators, and states the consequence for `EG-s-2` (the next-but-one order in your queue).

## ACCEPTANCE

<criterion id="S11-AC1" cell_refs="EG-s-11"><invocation>.tools/aws lambda get-function-configuration --function-name bd-49f-etf-ownership-daily --query "[FunctionName,LastModified,Environment.Variables.OUTPUT_PREFIX]" --output text</invocation><expect>daily/49financial/</expect></criterion>
`S11-AC1` -- the first twin is LIVE and its configured output prefix is the served prefix.

<criterion id="S11-AC2" cell_refs="EG-s-11"><invocation>.tools/aws lambda get-function-configuration --function-name bd-49f-etf-ownership-daily-canonical --query FunctionName --output text; echo rc=$?</invocation><expect>rc=</expect></criterion>
`S11-AC2` -- the canonical twin's live existence READ either way (a `ResourceNotFoundException` with a non-zero rc is a valid answer: NOT DEPLOYED, as its header says; record which).

<criterion id="S11-AC3" cell_refs="EG-s-11"><invocation>python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/twin_writer_census.py</invocation><expect>WRITER=</expect></criterion>
`S11-AC3` -- the census RAN and printed its determination line (a `WRITER=bd-49f-etf-ownership-daily` confirms `EG-s-2`'s address; `WRITER=bd-49f-etf-ownership-daily-canonical` or `UNDETERMINED` is a BLOCKING row on `EG-s-2`'s premise, filed by you now so the issuer re-addresses before that order is handed).

<criterion id="S11-AC4" cell_refs="EG-s-11"><invocation>.tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix daily/49financial/2026-09 --query "Contents[-1].[Key,LastModified]" --output text</invocation><expect>daily/49financial/2026-09</expect></criterion>
`S11-AC4` -- the newest served September slice READ (its `LastModified` is the timestamp the log census is keyed to).

<criterion id="S11-AC5" cell_refs="EG-s-11" judgment="true"/>
`S11-AC5` -- graded by the CVO at L9: the writer is named on the APPLIED plane with log evidence tied to a served object, both ends (function side, object side) read, the DESIRED plane's answer compared and any drift stated. RECORD; NO VERDICT.

<expected_criteria>S11-AC1, S11-AC2, S11-AC3, S11-AC4, S11-AC5</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) No source change; the two lambda dirs and the TF file are named for READING.
- **READS ONLY on the live plane** (`lambda get-function-configuration`/`list-functions`, `events list-rule-names-by-target`, `logs filter-log-events`, `s3api list-objects-v2`/`get-object` on `opal-data-etfs/daily/49financial/`). No invoke, no write. A denied read is the honest output and a row.
- **NEVER#1:** you read the AGGREGATION bucket's 49financial prefix and the function's configuration; you do NOT read `opal-data-assets/schwab/*` or any firm bucket.
- **EVERY invocation is bounded.** `timeout 120`; `filter-log-events` with `--limit 20` and a 3-day window; paginated lists counted client-side, never `--no-paginate`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W2-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/
infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily-canonical/
infra/aws/terraform/bd-pipeline/bd-49f-etf-ownership-daily.tf
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-11`.
<owned_cells>EG-s-11</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or bd-49f-etf-ownership-daily.
comp-iam: DECLARED-NOT-APPLICABLE -- a read-only census of two functions; no policy or resource is changed (the reads run under the launching seat's credentials, stated in the cell).
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`).
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S11-AC1` .. `S11-AC5`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-11.which-49f-twin-writes-the-served-slices.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S11-AC1,S11-AC2,S11-AC3,S11-AC4,S11-AC5` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
