# TO IRPT_DASHBD.TO-DB-b-243 -- the THREE GRANTS of hop 1 as a Terraform EDIT (round 121, workstream B-49F): the reporting-gold role gains PutObject on the one `filled_report_values` gold prefix, GetObject on the one served model-series object, and GetObject plus a prefix-conditioned ListBucket on the one household crosswalk prefix, each explicit and derived from the files that name it; written in `iam.tf` and `locals.tf` only, nothing planned, applied or deployed

<to_id>IRPT_DASHBD.TO-DB-b-243</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~197</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>121</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 121 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-121 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_121_20261015.md @9d4bd6adf3`: "YES: hop 1's apply pair includes the three grants, as an explicit Terraform edit of the reporting-gold root, applied with the code hash by `0.7.0_AE_CloudOps~DB2` under ONE never-widen pair (expected plan 0 add / 2 change / 0 destroy; anything else STOPS). Write: PutObject on the one `filled_report_values` gold prefix only. Read: GetObject on the one served model-series object. Read and list on the household crosswalk prefix only. No wildcard") | **Rows:** IRPT_DASHBD-D2-W197-S<k> | **Decomp cell:** `DB-b-243` (decomposition section 119) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

**Risk class WORLD** is the floor of the paths below (an `infra/` path): this order edits two Terraform files and runs no Terraform command; the plan and the apply are another seat's act under a signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-197` (branch `wk-IRPT_DASHBD-197`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~197/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~197/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The reporting-gold function's role (`infra/aws/terraform/investor-reporting/reporting-gold/iam.tf`) cannot write the `filled_report_values` prefix and cannot read two surfaces the round-120 stage reads (the facts record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~191/RD_HOP1_STAGE_FACTS_R120.json`, section `iam`, and rows `W191-S1` and `W191-S2`). Without the three grants the deployed stage is refused on every fire. The CTO ruled they ride hop 1's pair. This cell writes them in the Terraform files, additively, with every bucket, prefix and key DERIVED (rule 30), so that the applier's plan reads exactly: 0 add, 2 change (`aws_iam_role_policy.irpt_reporting_gold` and `module.irpt_reporting_gold.aws_lambda_function.this`), 0 destroy.

**The cell (`DB-b-243`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_grants.py` (your three criteria; its docstring, the HCL clauses and the facts record's exact form; it recomputes every ARN from `lib/opal_naming.py address()` and the module's constants); `iam.tf` and `locals.tf` of `infra/aws/terraform/investor-reporting/reporting-gold/` (the existing statements, the `irpt_rg_gold_*` locals, how the firm and the gold bucket are derived from `sources.json` and `infra/logic/registry/scopes.json`, and the comment that cites the producers' constants because Terraform cannot call `address()`); `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` (`TABLE`, `FirmAdapter.crosswalk_address` and `crosswalk_prefix`) and `data/assets/scripts/gold/irpt_reporting/adapters/model_series_windows.py` (`SERVED_BUCKET`, `SERVED_KEY`). You edit ONLY `iam.tf` and `locals.tf`.
2. **`locals.tf`** (additive; at most 4 existing lines may change): (a) `irpt_rg_gold_table_filled = "filled_report_values"`, mirrored from the module's `TABLE` and cited like the other tables (path and constant name in a comment); (b) `irpt_rg_gold_filled_prefix = "irpt/${local.irpt_rg_firm}/gold/${local.irpt_rg_gold_table_filled}/"`, and a sixth element in `irpt_rg_gold_write_arns` for it; (c) the served model series: read the adapter file with `file(...)` and take the bucket and the key from its `SERVED_BUCKET` and `SERVED_KEY` constants with `regex(...)` (the file is the one place they live: NEVER type the bucket name or the key in Terraform), and a local holding the one object ARN `arn:aws:s3:::<bucket>/<key>`; (d) the household crosswalk: the prefix `advi/${local.irpt_rg_firm}/gold/household_crosswalk/` mirrored from `FirmAdapter.crosswalk_address` (cite it in a comment; `advi` and `household_crosswalk` are that method's own segments), its object ARN pattern `<prefix>*` in the firm's gold bucket, its list pattern, and a check that the crosswalk lives in the SAME bucket as the irpt gold tables (the checker's recount of `address()` says it does; if you find otherwise, stop and file a BLOCKING row).
3. **`iam.tf`** (additive; at most 4 existing lines may change): the single `s3:PutObject` statement keeps its resource list `local.irpt_rg_gold_write_arns` (now six prefixes; you may rename its sid to `WriteTheSixGoldPrefixesOnly` and fix its comment and the output description; there must remain EXACTLY ONE PutObject statement); a NEW statement `ReadTheServedModelSeriesObjectOnly` (`s3:GetObject`, the one object ARN); the crosswalk: `s3:GetObject` on its object ARN pattern and `s3:ListBucket` on the bucket ARN with a `StringLike` condition on `s3:prefix` for its list pattern, either as new statements or by adding the crosswalk prefix to the existing gold read and list locals (choose the smaller edit; the existing gold read locals are named for six tables, so a new pair of statements is the clearer one). Every `actions` list is explicit: NO `*` anywhere, nothing but `s3:GetObject`, `s3:ListBucket` and `s3:PutObject` in new text, and no all-resources grant.
4. **The facts record** `RD_GRANTS_FACTS_R121.json` in your folder with EXACTLY these fields: `firm` ("49financial"); `files_changed` (a list of exactly two, IN THIS ORDER: iam.tf then locals.tf, each {`file`, `sha256` (of the bytes at your final commit), `kind` ("terraform")}); `grants` (a list of exactly three, in this order, each {`id` ("write_filled", "read_model_series", "read_crosswalk"), `actions` (the explicit actions), `arns` (the RESOLVED ARN strings, as the plan will print them: the write prefix pattern `arn:aws:s3:::<bucket>/<prefix>*`; the one object ARN; for the crosswalk BOTH the object pattern and the bucket ARN), `statement_ids` (the sids of the statements that carry it), `words`} and, on the crosswalk only, `list_prefix_pattern` (the `s3:prefix` value)); `expected_plan` {`to_add` 0, `to_change` 2, `to_destroy` 0, `resources` (exactly `aws_iam_role_policy.irpt_reporting_gold` and `module.irpt_reporting_gold.aws_lambda_function.this`), `words` (why the function changes: its code hash follows the new bundle, and who builds it)}; `validated` {`ran` (boolean), `words` (the box has no `terraform`: say what you could check, for example brace balance and the checker, and that `terraform fmt` and `validate` are the applier's)}; `derivations` {`served_series`, `crosswalk`, `filled_prefix`} (one sentence each: where each value comes from); `words`; `claim` ("inferred": nothing was planned); `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. The ARNs may contain long digit runs only in the `arns`, `list_prefix_pattern`, `resources`, `file`, `path`, `sha256` and `key` fields.

<criterion id="DB121-2-AC1" cell_refs="DB-b-243"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_grants.py" . DB121-2-AC1</invocation><expect>DB121-2-AC1 PASS</expect></criterion>
`DB121-2-AC1` -- `iam.tf` gains at least one new statement; every statement has an explicit actions list with no `*`; the actions of the new statements are only `s3:GetObject` and `s3:ListBucket`; exactly one `s3:PutObject` statement remains and it uses `irpt_rg_gold_write_arns`; `locals.tf` defines `irpt_rg_gold_table_filled` equal to the module's `TABLE` and the write list carries the filled prefix; the served series is read from `model_series_windows.py` and neither the served bucket name nor its key is typed; the crosswalk grant names `household_crosswalk`; no all-resources grant. Base: FAIL (nothing changed).
<criterion id="DB121-2-AC2" cell_refs="DB-b-243"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_grants.py" . DB121-2-AC2</invocation><expect>DB121-2-AC2 PASS</expect></criterion>
`DB121-2-AC2` -- the change is ADDITIVE against the commit that issued this order: `iam.tf` gains at least 12 lines and loses at most 4, `locals.tf` gains at least 6 and loses at most 4, and no other file under `infra/aws/terraform/` changes. Base: FAIL (no change).
<criterion id="DB121-2-AC3" cell_refs="DB-b-243"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_grants.py" . DB121-2-AC3</invocation><expect>DB121-2-AC3 PASS</expect></criterion>
`DB121-2-AC3` -- `RD_GRANTS_FACTS_R121.json` has exactly the form of step 4; its two files hash as recorded; each grant's actions and resolved ARNs EQUAL the checker's recount from `lib/opal_naming.py address()` (the filled prefix and the crosswalk prefix, bucket included) and the adapter's `SERVED_BUCKET` and `SERVED_KEY`; the crosswalk's list prefix pattern equals the recount; the expected plan is 0 / 2 / 0 on the two named resources; flags false; no long digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB121-2-AC1,DB121-2-AC2,DB121-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other Terraform file, the handler, the module, the adapters, the source map, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files and `lib/opal_naming.py` run locally. No AWS call of any kind, no Terraform command (`init`, `plan`, `validate` and `fmt` included; the box has none), no S3, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the crosswalk does not live in the irpt gold bucket, or the checker's recount of an ARN differs from what the files derive, file a BLOCKING row with both values and stop on that point. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W197-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/reporting-gold/iam.tf
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~197/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-243.hop-1-grants-in-the-reporting-gold-terraform.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 119 (round 121, workstream B-49F), cell `DB-b-243`.
<owned_cells>DB-b-243</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB121-2-AC1, DB121-2-AC2, DB121-2-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~197/IRPT_DASHBD.TO-DB-b-243.hop-1-grants-in-the-reporting-gold-terraform.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB121-2-AC1,DB121-2-AC2,DB121-2-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the new and changed statements by sid; the three resolved grants (actions and ARNs); the existing lines you changed; the expected plan; what you could not check without Terraform. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: two Terraform files and a facts record in a branch; nothing is planned, applied, scheduled or deployed, and the apply is another seat's act under a signed never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the files add three explicit grants to the reporting-gold role; they take effect only at the applier's apply, under the pair.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (nothing changed) and exercised by its self-test (seven HCL arms and seven record arms).
lane: the <paths> block IS the grant.
</preflight>
