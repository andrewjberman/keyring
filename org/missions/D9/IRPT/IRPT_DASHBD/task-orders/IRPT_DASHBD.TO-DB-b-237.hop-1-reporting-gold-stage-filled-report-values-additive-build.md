# TO IRPT_DASHBD.TO-DB-b-237 -- HOP 1 TO THE CLOUD, THE BUILD HALF (round 120, workstream B-49F): the 49 Financial reporting-gold Lambda gains a GUARDED `filled_report_values` stage (it builds the day's rows with the round-118 module from the day's gold tables and writes ONE partition at the firm's gold address, after the stages that produce its inputs, on the EXISTING daily schedule), the bundle gains the module as a source-map member, and a facts record names every file, the IAM cover, the schedule, the expected plan and the names for the never-widen packet; the change is additive, no Terraform file changes, nothing is applied or deployed

<to_id>IRPT_DASHBD.TO-DB-b-237</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~191</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 120 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-120 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_120_20261015.md @5e358b0a8f`: "Hop 1 goes to the cloud now. Contract 0.5.4 landed, so the gate is met. `~D2` cuts the apply order to `0.7.0_AE_CloudOps~DB2`: the 49 Financial `filled_report_values` schedule after its inputs and its first cloud write, under a never-widen pair. It is additive: a new gold prefix, a new schedule and a new function or entry, with builder names. The plan gate names exactly those additions") | **Rows:** IRPT_DASHBD-D2-W191-S<k> | **Decomp cell:** `DB-b-237` (decomposition section 118) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

**Risk class WORLD** is the floor of the paths below (an `infra/` path): this order DEPLOYS NOTHING; the apply is another seat's order under a signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-191` (branch `wk-IRPT_DASHBD-191`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~191/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~191/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.**

**Why.** Round 118 built the module `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` and ran it LOCAL for 49 Financial; contract 0.5.4 (round 119) fixed the members. The 49 Financial reporting-gold Lambda (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, 738 lines, one scheduled fire per trading day at 07:41 America/New_York, `infra/aws/terraform/investor-reporting/reporting-gold/schedule.tf`) already runs, in ONE invocation, the stages that produce every input of the table (the returns, the class table, the activity and lot tables), each stage imported GUARDED (a bundle that lacks a module still writes the earlier tables and logs the stage's skip by name). So hop 1 reaches the cloud as ONE MORE GUARDED STAGE of that invocation, on that schedule: no new function, no new schedule. This cell builds the stage and gathers the facts; the packet, both halves and the apply (a rebuild of the bundle and a Terraform apply of the function's code hash, by `0.7.0_AE_CloudOps~DB2`) are the issuer's and the CTO's next acts.

**The cell (`DB-b-237`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_hop1stage.py` (your criteria and the facts record's exact form are in its docstring and clauses); `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` (every stage: `class_days`, `emit_classes`, `_class_location`, `catch_up_classes`, `lots_days`, `emit_lots`, the guarded imports at about lines 95 to 115, `run`, `lambda_handler`, `local`); its tests directory `infra/aws/lambda/investor-reporting/reporting-gold/tests/` (96 tests today: copy the style of `test_class_table_emission.py`, `test_class_catch_up.py`, `test_activity_lot_emission.py` and `test_handler_passes_src.py`); `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` and `adapters/` (the module: `build_document`, `to_rows`, `COLUMNS`, `main`; it has NO S3 write: the handler writes); `infra/aws/lambda/ci/lambda-source-map.json` (the entry of the function `irpt-reporting-gold-lambda`: its `staged_from` members and how a member is declared); `infra/aws/terraform/investor-reporting/reporting-gold/` (`lambda.tf`, `iam.tf`, `schedule.tf`, `locals.tf`): READ them, you edit none.
2. **The stage** in `handler.py`, ADDITIVE (at most 3 of the existing lines may change, for the import block): import `filled_report_values` GUARDED exactly as `account_class_daily` is (the import error kept and named at the stage); a stage that, for each day the returns stage wrote (and the catch-up logic the earlier stages use for a day owed), reads that day's gold tables of the firm (the same reader helpers the earlier stages use, addresses from `address()`), builds the rows with the module (`build_document` per household and `to_rows`), and writes ONE partition `address("irpt", <firm>, "gold", "filled_report_values", "date=<day>", "data.parquet")` through the handler's own writer for gold tables (the module itself stays free of any S3 write call); the stage runs AFTER the class and lot stages (its inputs), honours `upload` exactly as they do (a `local()` run writes to a local path), returns `(written, failed)` and NEVER raises (a failure is logged by name and the earlier tables stay written); the household set is the firm's population the other stages use. The stage must also be reachable from `local()` and the backfill path only if the earlier stages are (follow them; add nothing else).
3. **The bundle.** In `infra/aws/lambda/ci/lambda-source-map.json` add `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` as a member of that function's entry the way `account_class_daily.py` is a member (`staged_from`; leave the commit and sha256 pin for the applier, who writes it at the apply, as the handler's comments say for the earlier members; say so in the facts). Also list any module the stage newly needs that the bundle lacks (the module imports from `lib/` and the contract file: find out, and name each, adding it as a member if the earlier members' rules require it).
4. **Tests** `infra/aws/lambda/investor-reporting/reporting-gold/tests/test_filled_report_values_stage.py`, at least 6, no network: the guarded import (a bundle without the module logs the skip by name and the earlier stages still write); the stage writes exactly one partition at the builder address for a synthetic day; it never raises (a failing build is returned as failed, the earlier tables written); `upload=False` writes nothing to S3; the stage runs after the class and lot stages; a non-trading day writes nothing (the handler's own day selection); the household set equals the population the other stages use. The whole directory's tests (96 plus yours) must pass.
5. **The facts record** `RD_HOP1_STAGE_FACTS_R120.json` in your folder, counts, hashes, paths and words only, with EXACTLY these fields: `firm` ("49financial"); `stage` {`handler_file`, `functions` (the names of the functions you added, at least 2, each a `def` in the handler), `guarded_import` true, `after_stages` (the stages it follows), `words`}; `files_changed` (a list, at least the handler, the new test file and the source map, each {`file`, `sha256` (of the bytes at your final commit), `kind`}; NO Terraform file); `source_map` {`file`, `entry` (the entry's key), `member_added` ("data/assets/scripts/gold/irpt_reporting/filled_report_values.py"), `pin` (words: left for the applier), `words`}; `iam` {`file` (the IAM file you read), `covers_new_prefix` (boolean: does the function's existing role already allow writing the new table's gold prefix; read the policy, never assume), `statement_ids` (the statement ids you relied on), `words`}; `schedule` {`file`, `cron` (the existing cron as the file states it), `after_inputs` true, `trading_day_frontier` true, `words`}; `expected_plan` {`to_add`, `to_change`, `to_destroy` (0), `resources` (the Terraform addresses that change, for example the function's code hash), `words`: what `terraform plan` will print at the apply, from the Terraform files you read; if the apply also needs an IAM statement, say so here and set `covers_new_prefix` false)}; `write_path` {`table` "filled_report_values", `address_form` (the `address(` call as the stage makes it), `partition` ("date=<business date>"), `existing_prefixes_written` ([])}; `tests` {`file`, `new_tests`, `dir_total`}; `names` {`from_builders` true, `words` (every new name, if any, is builder output; none is typed)}; `words` (one paragraph: what the apply will do and what it will not); `claim`; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `line` or `pin` field.

<criterion id="DB120-1-AC1" cell_refs="DB-b-237"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_hop1stage.py" . DB120-1-AC1</invocation><expect>DB120-1-AC1 PASS</expect></criterion>
`DB120-1-AC1` -- the handler imports `filled_report_values` guarded; the new stage test file has at least 6 tests; the whole handler tests directory passes with at least 102 tests (the checker runs `pytest`). Base: FAIL (no stage test file).
<criterion id="DB120-1-AC2" cell_refs="DB-b-237"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_hop1stage.py" . DB120-1-AC2</invocation><expect>DB120-1-AC2 PASS</expect></criterion>
`DB120-1-AC2` -- `RD_HOP1_STAGE_FACTS_R120.json` has exactly the form of step 5; every file in `files_changed` exists and its sha256 equals the bytes, and no Terraform file is among them; the stage functions exist in the handler; the expected plan has no destroy; the write path touches no existing prefix; the names are builder output; the flags are false. Base: FAIL (no record).
<criterion id="DB120-1-AC3" cell_refs="DB-b-237"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_hop1stage.py" . DB120-1-AC3</invocation><expect>DB120-1-AC3 PASS</expect></criterion>
`DB120-1-AC3` -- the change is ADDITIVE: against the commit that issued this order the handler gains at least 20 lines and loses at most 3, the source map gains at least 1 line and loses at most 2, and no file under `infra/aws/terraform/` changes. Base: FAIL (the handler is unchanged).

<expected_criteria>DB120-1-AC1,DB120-1-AC2,DB120-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every Terraform file, the module `filled_report_values.py` (a change there is a row and a stop), the sibling producers, the contract, `sources.json`, every other adapter and test, `lib/`, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests run with no network and no AWS. Writes: the repo files of the grant and the private folder named above. No deploy, no Terraform act of any kind (plan included), no Lambda update, no S3 put, copy or delete, no schedule, no push, no vendor call, no secret read.
- **Client data.** None is needed or read; if a test fixture needs figures, they are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the stage cannot be added without changing more than 3 existing lines of the handler, or the bundle needs a member the source map cannot declare additively, or the existing IAM does not cover the new prefix (that is a FACT for the facts record, not a stop), file a BLOCKING row naming the exact obstacle and stop on that point. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W191-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/test_filled_report_values_stage.py
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~191/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-237.hop-1-reporting-gold-stage-filled-report-values-additive-build.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 118 (round 120, workstream B-49F), cell `DB-b-237`.
<owned_cells>DB-b-237</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB120-1-AC1, DB120-1-AC2, DB120-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~191/IRPT_DASHBD.TO-DB-b-237.hop-1-reporting-gold-stage-filled-report-values-additive-build.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB120-1-AC1,DB120-1-AC2,DB120-1-AC3` (the three ids as ONE comma-joined argument) BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the stage's functions and where it sits in `run`; the IAM finding (does the existing role cover the new prefix, which statement); the schedule as the file states it; the expected plan (adds, changes, destroys, the addresses); the members you added to the bundle; the test counts; anything the packet must say that you could not settle. Counts, paths and words only: no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a guarded handler stage, its tests, a source-map member and a facts record in a branch; nothing is applied, scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the facts record reads the existing role and says whether it covers the new prefix.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms for each clause); its clauses were dry-run at the base (the handler is unchanged: the stage tests and the facts record are missing).
lane: the <paths> block IS the grant.
</preflight>
