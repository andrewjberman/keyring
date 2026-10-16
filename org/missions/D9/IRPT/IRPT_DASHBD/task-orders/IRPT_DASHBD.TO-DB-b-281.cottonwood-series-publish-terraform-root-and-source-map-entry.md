# TO IRPT_DASHBD.TO-DB-b-281 -- the COTTONWOOD SERIES PUBLISH TERRAFORM ROOT and its source-map entry (round 147): the new root `reporting-publish-iso` with a firm-isolated function, its `*-cot-*` execution role, NO schedule, the native pyarrow layer, and the pinned bundle of DB-b-280's handler

<to_id>IRPT_DASHBD.TO-DB-b-281</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~226</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>147</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F + contract, round 147 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md ADDENDUM v0.16 item 4 and the CTO boundary ruling msg 8803 ("~D2 owns handler.py, publisher.py, the publish tf root and the sources entry. The first Cottonwood series publish is ~D2's cell, under its own pair and in one drain with the contract field.") | **Decomp cell:** `DB-b-281` (decomposition section 145).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order writes Terraform files and one source-map entry and runs no Terraform command, no AWS write and no upload. NOTHING is planned, applied or deployed; the applier's plan must read 4 add / 0 change / 0 destroy.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~02:5xZ, on worker row IRPT_DASHBD-D2-W226-S2; gate limb: an existing order modified, placeholders NONE unchanged, no criterion id, cell or path change):** Your branch CONTAINS the series contract 0.3.0 (merge commit 6e56bb47d3 of `wk-IRPT_DASHBD-225` into your branch); the bundle's `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` member is that 0.3.0 file, pinned to the commit that last changed it on your branch. You edit no contract file.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-226` (branch `wk-IRPT_DASHBD-226`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~226/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** `DB-b-280`'s handler (now on your branch) needs its own function in its own Terraform root, for the same reason the report-build function has one: the Cottonwood bucket's fence admits only a `-cot-` role, and no second firm may sit inside the 49 Financial function. **The report-build root next door (`infra/aws/terraform/investor-reporting/reporting-gold-iso/`) is the BLUEPRINT**: it passed the real naming gate and was applied. Copy its structure file by file and change what is below. This root has NO schedule: the function is invoked by hand, under a never-widen pair, by the applier.

**The cell (`DB-b-281`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p149_pubroot.py` (your three criteria; the exact statement ids, the bundle (`CLOSURE`), the entry and the record's form are in it); `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p148_cothandler.py` (its behaviour check runs on your UNPACKED package); the five files of `reporting-gold-iso` and its source-map entry `irpt-cot-reporting-gold-lambda`; the handler `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py`.
2. **The root, FOUR files in `infra/aws/terraform/investor-reporting/reporting-publish-iso/`** (`main.tf`, `locals.tf`, `lambda.tf`, `iam.tf`; no `schedule.tf`), no resource type other than `aws_iam_role` (one) and `aws_iam_role_policy` (one) besides the yang-lambda module, every name from the `opal_name` module (THREE calls: `system = "irpt"`, `scope = local.<firm>`, `function = "reporting-publish"`, kinds `lambda`; `role` with qualifier `execution`; `policy` with qualifier `execution`), the firm and the gold bucket DERIVED in `locals.tf` exactly as `reporting-gold-iso/locals.tf` derives them (never typed), the gold root `irpt/<firm>/gold/` and a NEW local for the platinum reporting root `irpt/<firm>/platinum/reporting/` (the address builder's segments written inline, as the blueprint does), the artifact key read from the source map by the function's builder name. State key `investor-reporting/reporting-publish-iso/tfstate`. The yang-lambda module is named `irpt_reporting_publish_iso`: `handler = "handler.lambda_handler"`, `runtime = "python3.12"`, `timeout = 900`, `memory_size = 1024` (a comment states the basis: the 49 Financial publish function's sizing, one list of the gold table, a thread pool of twelve over about sixty-five small partitions and one small document per account; the Lambda's own first run is the reading), NO `reserved_concurrent_executions`, no environment variable, `layers = [data.aws_lambda_layer_version.irpt_performance_native.arn]` with the read-only data source exactly as the blueprint has it. No served-object local, no scheduler role, no schedule, no alarm, no topic, no mail.
   - **The execution policy, exactly these five statement ids** (explicit actions, no wildcard, no all-resources grant, no delete, no lambda action), in `data "aws_iam_policy_document"`: `ListGoldReturnsAndPlatinumReportingOnly` (`s3:ListBucket` on the gold bucket under an `s3:prefix` StringLike condition for `<gold root>account_return_daily/*` and `<platinum reporting root>*`); `ReadGoldReturnsOnly` (`s3:GetObject` on the `account_return_daily` prefix ONLY: no `account_dim`, no other gold table, no `dim_return_method`); `WriteThePlatinumReportingPrefixOnly` (`s3:PutObject` on the platinum reporting prefix: the ONLY PutObject statement); `ReadBackThePlatinumReportingPrefixOnly` (`s3:GetObject` on the platinum reporting prefix: `head_object` needs it); `OwnLogStreamOnly` (`logs:CreateLogStream`, `logs:PutLogEvents` on the function's own log group). The assume-role document carries the statement id `ExecutionRoleAssumedByLambdaService`.
3. **The source-map entry** `irpt-cot-reporting-publish-lambda` in `infra/aws/lambda/ci/lambda-source-map.json`, NEW (copy the shape of `irpt-cot-reporting-gold-lambda`): `pipeline` "investor-reporting"; `source_dir` "infra/aws/lambda/investor-reporting/reporting-publish-cot"; `files` = ["handler.py"] followed by the checker's `CLOSURE` list in its order; `staged_from` = one member per `CLOSURE` path, in order, each with `packaged_as` equal to its `repo_path`, a full 40-hex `pin` (the most recent commit that changed that file: `git log -1 --format=%H -- <path>`; the publisher's pin is a commit ON YOUR BRANCH, an ancestor of HEAD) and its hex `sha256` at that commit (which must equal the file at HEAD); `artifact_s3_key` "investor-reporting/irpt-cot-reporting-publish-lambda.zip"; `tf_file` "infra/aws/terraform/investor-reporting/reporting-publish-iso/lambda.tf"; `tf_resource` "module.irpt_reporting_publish_iso.aws_lambda_function.this"; `iam_role` the builder name of the execution role. Keep every other entry, key and line of the file byte for byte. Commit the entry BEFORE running the build (it reads committed source).
4. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p149_pubroot.py" . DB147-3-AC1`, then AC2 (this runs the real naming gate in plan mode on the three named resources, reads the layer, builds the package with `BUILD_ONLY=1` and runs `DB147-2-AC1`'s behaviour check on the UNPACKED handler; it takes a few minutes), then AC3.
5. **Record** `RD_COT_PUBLISH_ROOT_FACTS_R147.json` in your folder with EXACTLY these fields: `root` ("infra/aws/terraform/investor-reporting/reporting-publish-iso/"); `names` (the three builder names, in the order function, execution role, execution policy); `resources` (the four addresses the plan will add: `module.irpt_reporting_publish_iso.aws_lambda_function.this`, `module.irpt_reporting_publish_iso.aws_cloudwatch_log_group.lambda`, `aws_iam_role.irpt_reporting_publish_iso_execution`, `aws_iam_role_policy.irpt_reporting_publish_iso_execution`); `expected_plan` ({"add": 4, "change": 0, "destroy": 0, "claim": "inferred"}); `memory` ({"memory_mb": 1024, "basis": <the basis in words>, "claim": "inferred"}); `words` (one paragraph, 80 to 1800 characters: what the root declares, what the three checks proved, what is NOT proven: no plan, no apply, no invoke, the Lambda runtime's memory and time).

<criterion id="DB147-3-AC1" cell_refs="DB-b-281"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p149_pubroot.py" . DB147-3-AC1</invocation><expect>DB147-3-AC1 PASS</expect></criterion>
`DB147-3-AC1` -- the root's HCL: two resource blocks of the two types and one yang-lambda module named `irpt_reporting_publish_iso` (handler, timeout 900, memory 1024, the native layer through the read-only data source, NO reserved concurrency, no environment variable, the artifact key read from the source map), exactly three `opal_name` module calls, no schedule or event rule or topic or mail resource, exactly the six statement ids above with explicit actions and no all-resources grant, one PutObject on the platinum reporting prefix, the read statements naming `account_return_daily` only, no typed builder name, the state key above.
<criterion id="DB147-3-AC2" cell_refs="DB-b-281"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p149_pubroot.py" . DB147-3-AC2</invocation><expect>DB147-3-AC2 PASS</expect></criterion>
`DB147-3-AC2` -- the checker builds the three names from the root's own module arguments with `lib/opal_naming.py` and runs the REAL `.tools/naming-apply-gate.py` in plan mode on a synthetic plan holding them: three CONFORMANT lines, no REFUSE; the bundle's third-party imports are pyarrow plus the runtime's and the layer holds it; the `BUILD_ONLY` package of the entry holds exactly the entry's `files`, every member's bytes equal its source, and the handler UNPACKED from it passes the behaviour check on a fake S3.
<criterion id="DB147-3-AC3" cell_refs="DB-b-281"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p149_pubroot.py" . DB147-3-AC3</invocation><expect>DB147-3-AC3 PASS</expect></criterion>
`DB147-3-AC3` -- the source map gains exactly the one NEW entry above: every other function entry and top-level key unchanged, `files` and `staged_from` equal to the checker's list in order, each member's pin an ancestor commit of HEAD with a sha256 equal to `git show <pin>:<path>` and to the file at HEAD, the three Terraform fields as above, the `iam_role` equal to the builder's execution role name; and the record has exactly the form of step 5 with its names equal to the checker's recount.

<expected_criteria>DB147-3-AC1,DB147-3-AC2,DB147-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the report-build root, the landing root, the 49 Financial roots, the handlers, `publisher.py`, every other source-map entry, the registry, the build script, the naming gate, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files, the naming gate, `lib/opal_naming.py`, the layer (`aws lambda list-layer-versions` and `get-layer-version`, GET and LIST only, which the checker also makes). Writes: the repo files of the grant and your private folder. The `BUILD_ONLY` run writes a zip under a temporary directory only. No Terraform command, no AWS write, no upload, no push, no invoke.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the naming gate refuses a name, record its refusal line verbatim, file a BLOCKING row and stop; never type a name to pass it. The commit-time naming gate refuses a firm token in a hand-kept carrier (the blueprint's Amendment 1): the root directory, module, state key and entry carry the neutral token `iso`/`publish-iso`; take no firm word into any hand-kept string.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W226-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/reporting-publish-iso/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-281.cottonwood-series-publish-terraform-root-and-source-map-entry.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 145 (round 147, workstream B-49F + contract), cell `DB-b-281`.
<owned_cells>DB-b-281</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB147-3-AC1, DB147-3-AC2, DB147-3-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/IRPT_DASHBD.TO-DB-b-281.cottonwood-series-publish-terraform-root-and-source-map-entry.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB147-3-AC1,DB147-3-AC2,DB147-3-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the four addresses; the six statement ids; the number of pinned members; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: four Terraform files and one source-map entry in a branch; nothing is planned, applied, uploaded, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the statements are new and explicit (listed in the order); no existing grant changes; the Cottonwood bucket fence admits the new execution role by its `-cot-` token.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its HCL clause was validated by the issuer against a scratch reference root derived from the blueprint (green), its handler-in-package clause against a scratch reference handler, and its pure clauses (statements, imports, gate output, package, entry, facts) by the self-test (green and red arms); its live clauses (the real naming gate, the layer, the build-only package, the pins) are the blueprint's, proven green on round 133.
lane: the <paths> block IS the grant.
</preflight>
