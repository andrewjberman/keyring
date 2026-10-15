# TO IRPT_DASHBD.TO-DB-b-259 -- the Cottonwood landing root gains its PYARROW LAYER (round 127, workstream B-49F): a read-only data source for the EXISTING `irpt-performance-native-layer` and one `layers` line on the module call, because the merged function would fail on `import pyarrow`

<to_id>IRPT_DASHBD.TO-DB-b-259</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~212</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>127</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 127 | **Ordered by:** the issuer, repairing its own round-123 order `DB-b-252` under the CTO ROUND-126 ANALYSIS (B-49F) @2cf3e13682 ruling 1 (the Cottonwood landing pair) and the issuer's own finding recorded in decomposition section 125 | **Decomp cell:** `DB-b-259` (decomposition section 125).

**Risk class WORLD** is the floor of the path below (an `infra/` path): this order edits one Terraform file and runs no Terraform command, no AWS write and no upload.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-212` (branch `wk-IRPT_DASHBD-212`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~212/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~212/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The Cottonwood landing function (`irpt-cot-account-return-daily-lambda`, root `infra/aws/terraform/investor-reporting/account-return-daily/`) packages an adapter that runs `import pyarrow` at module level. The root's module call sets NO `layers`, and the python3.12 Lambda runtime does not carry pyarrow, so the function's first invocation would fail on import. The sibling Cottonwood function takes pandas and pyarrow from the EXISTING layer `irpt-performance-native-layer` through a read-only data source (see `infra/aws/terraform/investor-reporting/account-dim/lambda.tf`, lines 3 to 8 and the `layers` line of its module call). This order does the same for the landing root and nothing else. A data source creates nothing, so the expected plan stays 7 add / 0 change / 0 destroy.

**The cell (`DB-b-259`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r127/p127_layer.py` (your three criteria; every clause and the record's exact form are in it); `infra/aws/terraform/investor-reporting/account-dim/lambda.tf` (the form to follow); `infra/aws/terraform/investor-reporting/account-return-daily/lambda.tf` (the file you edit).
2. **The edit, `lambda.tf` only.** Add, above the first `module` block, the read-only data source exactly in the sibling's form: `data "aws_lambda_layer_version" "irpt_performance_native" { layer_name = "irpt-performance-native-layer" }` (spaced as `terraform fmt` would). In the `module "irpt_account_return_daily"` call add the one line `layers = [data.aws_lambda_layer_version.irpt_performance_native.arn]`, aligned with its neighbours' `=` as `terraform fmt` aligns a contiguous attribute group (re-aligning the group is allowed; the checker compares the code with spacing normalised). Add comment lines (comments only elsewhere) saying that pandas and pyarrow come from the EXISTING `irpt-performance-native-layer` through this read-only data source, that this cell publishes no new layer version, and that the memory measurement of round 125 ran with pyarrow loaded. NOTHING else in code changes: `memory_size = 1024`, `timeout = 900`, reserved concurrency 1, the handler, the runtime and every other root file stay byte for byte.
3. **Record** `RD_COT_LAYER_FACTS_R127.json` in your folder with EXACTLY these fields: `layer_name` ("irpt-performance-native-layer"); `layer_version` (the layer's latest version number, read with `aws lambda list-layer-versions --layer-name irpt-performance-native-layer`, a read); `compatible_runtimes` (that version's list); `sibling_function` ("irpt-cot-account-dim-lambda"); `sibling_layer_arn` (the one layer ARN the sibling function reports in `get-function-configuration`); `words` (one paragraph, 80 to 1500 characters: what was missing, what you added, what is NOT proven: no plan, no apply, no invoke, the layer's pyarrow version against the one the adapter was measured with).

<criterion id="DB127-1-AC1" cell_refs="DB-b-259"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r127/p127_layer.py" . DB127-1-AC1</invocation><expect>DB127-1-AC1 PASS</expect></criterion>
`DB127-1-AC1` -- against the order's first commit, `lambda.tf` gains exactly one read-only data source for `irpt-performance-native-layer` and one `layers = [data.aws_lambda_layer_version.irpt_performance_native.arn]` line, no other code line moves (comments excluded, spacing normalised), a comment names pyarrow and the layer, memory 1024 and timeout 900 stay, and every other root file is byte-equal to the base.
<criterion id="DB127-1-AC2" cell_refs="DB-b-259"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r127/p127_layer.py" . DB127-1-AC2</invocation><expect>DB127-1-AC2 PASS</expect></criterion>
`DB127-1-AC2` -- the checker reads the layer and the sibling function live: the layer's latest version lists python3.12, the sibling runs python3.12 on exactly that latest version, and the record has exactly the form of step 3 and equals those reads.
<criterion id="DB127-1-AC3" cell_refs="DB-b-259"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r127/p127_layer.py" . DB127-1-AC3</invocation><expect>DB127-1-AC3 PASS</expect></criterion>
`DB127-1-AC3` -- the third-party imports of the bundle's python files (the source-map entry `irpt-cot-account-return-daily-lambda`, read by the checker) are exactly pyarrow plus the runtime's boto3 and botocore, and the layer's zip (downloaded by the checker) holds `python/pyarrow/__init__.py`.

<expected_criteria>DB127-1-AC1,DB127-1-AC2,DB127-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the other root files, the handler, the adapter, the source map, the sibling root, the registry, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; `aws lambda list-layer-versions`, `get-function-configuration` of the sibling (GET and LIST only). Writes: the repo files of the grant and your private folder. No Terraform command, no AWS write, no upload, no push, no invoke, no layer publish.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the layer lacks python3.12 or the sibling reports a different layer, record it, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W212-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/account-return-daily/lambda.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~212/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-259.cottonwood-landing-root-pyarrow-layer-from-the-existing-native-layer.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 125 (round 127, workstream B-49F), cell `DB-b-259`.
<owned_cells>DB-b-259</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB127-1-AC1, DB127-1-AC2, DB127-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~212/IRPT_DASHBD.TO-DB-b-259.cottonwood-landing-root-pyarrow-layer-from-the-existing-native-layer.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB127-1-AC1,DB127-1-AC2,DB127-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the layer version and runtimes you read; the lines you changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one Terraform file edited in a branch; nothing is planned, applied, uploaded, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS write and no grant changes; a read-only layer data source needs no IAM change on the function's role.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its HCL, import and facts clauses were exercised by its self-test (green and red arms) and its live and layer clauses dry-run at the base (FAIL as expected) and against a scratch reference.
lane: the <paths> block IS the grant.
</preflight>
