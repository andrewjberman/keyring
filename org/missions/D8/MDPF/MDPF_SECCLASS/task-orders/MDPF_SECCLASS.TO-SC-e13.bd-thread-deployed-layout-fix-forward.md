# TO MDPF_SECCLASS.TO-SC-e13 -- round 6 SC-e-13: the BD thread imports the one shared client on the runner (fix-forward for row S5), and the BD_THREAD_R3 half

<to_id>MDPF_SECCLASS.TO-SC-e13</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~10</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-13` (`decompositions/MDPF_SECCLASS_DECOMP_R6.md`) |
**outcome_ref:** FWD-1, FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-13`. On 2026-09-30 the five BD thread files were deployed to `s3://opal-data-bd/code/{gold,silver}/` and an
exercise run of the BD gold chain crashed C_06 at import:

```
File "/tmp/gold_layer_scripts/lib/etf_classifier.py", line 19, in <module>
  _SHARED_DIR = Path(__file__).resolve().parents[5] / 'infra' / 'aws' / 'lambda' / 'v2_portal' / '_shared'
IndexError: 5
```

The BD gold runner copies `s3://opal-data-bd/code/gold/` FLAT into `/tmp/gold_layer_scripts/` and runs from there. It
has no `infra/` tree beside it and no copy of the shared client
`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`. The files were rolled back; nothing served moved.
`data/black_diamond/scripts/gold/E_18.detect_new_securities.py:54` has the same kind of hop (`parents[4]`) into
`infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`. Every in-repo test passed because the repo tree
supplies the ancestors the runner lacks. Row: `MDPF_SECCLASS-S5` in
`org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

**Constraints you must respect:**
- The PRD forbids a second copy of the client in the repo (contract C-TABLE). Ship its BYTES as a deploy artifact
  instead, the way `.tools/safe_deploy_core.py` `_IRPT_HOLDINGS_CLOSURE` ships the same client into the IRPT Holdings
  bundle. Read that closure first.
- `.tools/safe_deploy_core.py` today maps only `data/<tree>/scripts/{gold,silver,bronze}[/lib]/*.py` to code prefixes,
  and `AUX_CODE_PREFIXES["bd"]` is `{}`. Only `code/gold/` reaches the gold runner.

**Build (LOCAL build + record: no upload, no deploy, no run on the runner):**
1. **The deploy mapping.** In `.tools/safe_deploy_core.py`, declare that a BD gold deploy also ships the one client's
   bytes -- and, for E_18, `etf_classification_scheduled.py` plus every repo module either imports at load -- into a
   sub-directory of `code/gold/` (for example `code/gold/lib/_shared/`). The mapping is data the tool reads, so the check
   in step 4 can ask the tool what it would upload.
2. **Resolution.** `data/black_diamond/scripts/gold/lib/etf_classifier.py` and `E_18.detect_new_securities.py` resolve
   the shared modules from their OWN deployed directory first and from the repo path second. Remove every module-level
   `parents[N]` hop that can raise; a missing module is a clear logged refusal, never an `IndexError` at import.
3. **The silver layout.** Find how the BD silver runner lays out `code/silver/` and whether `code/gold/` sits beside it
   (`build_bd_assets_dim.py:56` imports `lib.etf_classifier` through `../gold`). Record what you measured, from the
   runner's own sync script or bootstrap, in the check's output. If the silver runner cannot reach the gold `lib/`, make
   `build_bd_assets_dim.py` resolve it the same way, inside your grant.
4. **The deployed-layout check.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_deployed_layout_import.py`.
   It asks `safe_deploy_core` for the exact list of files a BD gold deploy of the thread files would upload and their
   destination keys (read from the tool, never a hand-built list). It copies them into a fresh temp directory at those
   relative paths, flattened the way the runner flattens `code/gold/`. With NO repo path on `sys.path`, it imports
   `C_06.client_mix_timeseries`, `D_03.composition_artifacts`, `D_04.client_portal_summary`,
   `E_18.detect_new_securities` and `lib.etf_classifier`. It prints one line per module (`OK <module> client=<resolved
   path>`) and, when all five import, a final line `DEPLOYED-LAYOUT-IMPORT modules=5 of 5 files=<n>`. It does the same
   for the silver builder from the silver layout you measured, printed on its own line.
5. **Tests** in `data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py`: the library resolves
   the client from its own directory when the repo path is absent; a missing client is a logged refusal, not an
   exception at import; E_18 the same. The existing thread tests
   (`data/black_diamond/scripts/gold/tests/test_etf_classifier_canonical.py`, `test_thread_trace.py`) still pass.
6. **The new half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R3_20260930.md`
   (`## The act`, `## Blast radius`, `Rollback per key`). It covers:
   - the redeploy of the BD thread files plus the shipped shared modules (every destination key named);
   - an ad-hoc QA exercise run of the BD gold chain on the runner as the import proof, with the ordinary scheduled
     fire (23:00Z `bd-gold-nightly-fallback` or 04:00Z `bd-canonical-prices-daily`) as the acceptance;
   - the COO's FWD-1 page read for relationship z08327149 (VXX structured/Hedge, GLD/PHYS commodities/Metals);
   - E_18's moved acceptance: its first scheduled run after the redeploy;
   - the served keys the chain overwrites and their prior VersionIds (read them live), and the rollback per key,
     including the code-object rollback that ran on 2026-09-30 18:16Z as the tested branch.
   Reuse the blast-radius analysis of `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R2_20260930.md` by citation and restate
   only what changed.

### ACCEPTANCE

<criterion id="SC6-e13-AC1" cell_refs="SC-e-13"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py data/black_diamond/scripts/gold/tests/test_etf_classifier_canonical.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC6-e13-AC1` -- the new resolution tests and the existing thread tests pass in the repo tree.

<criterion id="SC6-e13-AC2" cell_refs="SC-e-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_deployed_layout_import.py</invocation><expect>DEPLOYED-LAYOUT-IMPORT modules=5 of 5</expect></criterion>
`SC6-e13-AC2` -- the five modules import from an exact extract of what the deploy tool ships, with no repo on the path
(1.0.0_SA_CTO DECISION 103371).

<criterion id="SC6-e13-AC3" cell_refs="SC-e-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R3_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC6-e13-AC3` -- the new half, for the issuer and the CTO to sign.

<expected_criteria>SC6-e13-AC1,SC6-e13-AC2,SC6-e13-AC3</expected_criteria>

Dry-run at the base 2026-09-30 19:3xZ: AC1 no such test file (FAIL as expected); AC2 no such check (FAIL as expected);
AC3 no such half (FAIL as expected).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No S3 upload, no `safe-deploy`, no Lambda invoke, no run on any runner. Reads of S3 (prior
  VersionIds) and of the runner's sync script in the repo are allowed.
- **No second repo copy of the client.** Its bytes travel only as a deploy artifact.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W10-S<k>`), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/gold/E_18.detect_new_securities.py
data/black_diamond/scripts/silver/build_bd_assets_dim.py
.tools/safe_deploy_core.py
data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_deployed_layout_import.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R3_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/ssm/opal-bd-asset-dim-download.json
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R6.md</decomp_doc> (round 6), cell `SC-e-13`.
<owned_cells>SC-e-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC6-e13-AC1, SC6-e13-AC2, SC6-e13-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~10/MDPF_SECCLASS.TO-SC-e13.bd-thread-deployed-layout-fix-forward.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC6-e13-AC1,SC6-e13-AC2,SC6-e13-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the deploy mapping's diff, the resolution diff, the silver layout you measured (and its source file), every
line the deployed-layout check printed, the test line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the redeploy and the run are the new half's acts.
comp-iam: RUN -- 1 read (bd-exporter-ec2-role carries bd-securities-access with GetItem on etf-classifications, live 14:3xZ and CTO 15:0xZ); BLIND: none new, the cell adds no call.
comp-adversary: RUN -- 1 log read (s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-09-30_20260930_174903.log, C_06 IndexError: 5), 1 code read (safe_deploy_core AUX_CODE_PREFIXES bd {}), 1 ruling read (CTO 103369 + 103371); BLIND: the silver runner's layout is unmeasured (step 3 measures it).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO rounds 4-5 analysis @533bcae124 section 4 item 1; RULING 103369; DECISION 103371; row MDPF_SECCLASS-S5.

## AMENDMENT 1 (2.0.0_SA_COO~M, 2026-09-30 ~22:1xZ) -- the silver runner stages the shared modules too

Ruling on row `MDPF_SECCLASS-W10-S1` (BLOCKING, disarm owner this seat; the issuer rules inside its own decomposition).
The silver bootstrap document `infra/aws/ssm/opal-bd-asset-dim-download.json` copies `code/gold/lib/etf_classifier.py`
but not `code/gold/lib/_shared/*`, and the served silver builder depends on internals the new library drops, so the gold
redeploy cannot land without the silver leg. The document is not Terraform-managed (only `bd-pipeline/iam.tf:97` names
it). It is now in `<paths>`.

- Add the copy lines that stage the three shipped modules (`code/gold/lib/_shared/etf_classifications_dynamodb.py`,
  `etf_classification_scheduled.py`, `etf_classification.py`) into the RUNROOT at the path the library resolves
  (`data/black_diamond/scripts/gold/lib/_shared/`), in the same style as the document's existing copy lines. Derive the
  list from `safe_deploy_core.shipped_artifacts_for()` if the document format allows; otherwise type the three names and
  let the check prove they match the tool.
- The deployed-layout check: its `SILVER-LAYOUT-AS-STAGED-TODAY` line must now read the document from the repo and import
  OK. The check exits non-zero when the silver as-staged import is refused, so AC2 fails on a silver gap from now on.
- Find how this SSM document reaches AWS (a deploy script, a runbook, or `aws ssm update-document` by hand; read the
  estate, and read the live document version with `aws ssm describe-document`, read only). In the BD_THREAD_R3 half, add
  the document update as its own leg BEFORE the silver builder's redeploy: the act, the live version before, and the
  rollback (restore the prior default version). Remove precondition P1 as satisfied by that leg, citing this amendment.
- Re-run the three criteria, re-validate the proof (VALID rc=0), flip `<status>` back to complete, commit.
- Rows W10-S2 (E_18 has no trigger in `gold_dispatch.sh`) and W10-S3 (`.tools/test_safe_deploy.py` fails 7 of 14
  before and after) are NOT in scope here; leave them as filed.

Gate limb: none graded this modification (a modification of an existing order; `.tools/to-pipeline-gate.py` LIMB 6 fires
on new orders only, and this order declares no placeholders).
