# TO IRPT_DASHBD.TO-DB-c-14 -- RESUME the Cottonwood apply under the signed ADDENDUM (blob `1a7a8c68bb`): the second shared-zip upload (`scopes.json` re-pinned, the member diff against the live zip is that one member), the registry test on the BUILT zip, the 0-to-add 3-to-change plan, then the 12-date catch-up from date 1, the after-read, the reader check and the schedule ENABLED, continuing the open ledger (CTO half signed @05472e30fc, COO half @bd00e9cd11)

<to_id>IRPT_DASHBD.TO-DB-c-14</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed addendum, packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~406/NEVER_WIDEN_ADDENDUM_DB-c-11_R118.md` (blob `1a7a8c68bb153a1b92fab3c5247301ba1d9aae4e`, sha256 `fe34395f221715fb736cf07a6d66a21c620b192103b94d5ad43353e6c06ee830`), COO half `deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_ADDENDUM_DB-c-11_R118_COO_HALF.md` and CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ADDENDUM_DB-c-11_R118_CTO_HALF.md` (both at that blob); the first pair (blob `ad049d506cdb22d4fd729b85ef206a548aa4a6d2`) stays in force for the catch-up's keys and sequence | **Decomp cell:** `DB-c-14` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 7) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** `TO-DB-c-9` (stopped at step 6; its record `deliverables/0.7.0_AE_CloudOps~DB2/COTTONWOOD_APPLY_RECORD.json`), `DB-c-11` and `DB-c-12` (merged).

---

## WORKER FACE

Your worktree is the linked worktree your seat uses for IRPT_DASHBD, cut from the current `box/dell2` (it must carry `eae8170b22`, which holds the re-pin and the registry test); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`. Never push. **A STOP is reported at once and writes nothing further.** No client data: counts, dates, keys, hashes, addresses and words only. Row ids are `IRPT_DASHBD-D2-S<k>` (the next free `k`), as you used last time.

**The state you start from (verify each, read only).** Your first order stopped at its step 6: the three functions (`irpt-holdings-performance-lambda`, `irpt-inf-holdings-performance-lambda`, `irpt-cot-holdings-performance-lambda`) run the first new zip, S3 version `vrBQAr57i.p3TMhjdSld3c_E5HMqX8iy`, whose `infra/logic/registry/scopes.json` is at the old source-map pin (no `z09` row), so the first catch-up invoke was refused. The Cottonwood schedule `irpt-cot-holdings-performance-daily` exists and is `DISABLED`; 0 Cottonwood gold keys are written. Your ledger `irpt-dashbd-cottonwood-holdings-performance-20261015` is OPEN at legs L5 to L8 and CONTINUES: do not open a new one.

**Read first:** the addendum packet (whole), both halves, your own first record and rows S58/S59, `deliverables/0.9.0_WK_IRPT_DASHBD~406/SCOPES_PIN_READ_R118.json`, `infra/aws/lambda/ci/lambda-source-map.json` (the entries of the three holdings-performance functions; the re-pin is merged), the registry test `infra/aws/lambda/investor-reporting/holdings-performance/tests/test_zip_registry_resolves.py`, and `org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-9.apply-cottonwood-holdings-performance-signed-pair.md` (steps 6 to 8 are repeated here).

**Do, in this order.**

0. **Gates, read only.** (a) `git hash-object` the addendum packet equals `1a7a8c68bb153a1b92fab3c5247301ba1d9aae4e` (`gates.packet_blob`); both halves read SIGNED at it (`gates.coo_half_signed`, `gates.cto_half_signed`); `gates.first_pair_blob` records `ad049d506cdb22d4fd729b85ef206a548aa4a6d2`. (b) `git merge-base --is-ancestor eae8170b22 HEAD` is true. (c) One change at a time: no OTHER open ledger or `.open_deploys` marker at any live worktree names `holdings-performance`, `holdings_performance` or `irpt-cot` (print the denominator); yours is the one. (d) The live zip version is still `vrBQAr57i.p3TMhjdSld3c_E5HMqX8iy` and the three functions share one `CodeSha256` (`build.live_version_before`); anything else is a STOP.
1. **Print the schedules (the CTO's condition).** Before any write read and print into your ledger: the state, expression and next fire of the 49 Financial schedule `irpt-holdings-performance-daily` (`cron(30 7 ? * MON-FRI *)` New York) and the Inflection schedule (find its name from `schedule.tf`; its expression is 14:00 UTC), and the current UTC time. Record `schedules_before_upload` {`<function>`: {`state`, `expression`, `next_fire_utc`}} for both functions. **Window:** do not upload or apply within 30 minutes before a fire or while one is running; if a fire is closer, wait for it to finish and read its result first. Read back the result of each function's last fire (its run's return code) as the baseline.
2. **The source map: the Cottonwood row (the CTO's condition, before the upload).** In `infra/aws/lambda/ci/lambda-source-map.json` add ONE new function entry `irpt-cot-holdings-performance-lambda`, immediately after the `irpt-inf-holdings-performance-lambda` entry, copied from that entry with these changes only: the key; `tf_resource` is `module.irpt_holdings_performance_cot.aws_lambda_function.this`; `iam_role` is `irpt-cot-holdings-performance-role`; `_build_note` says the function shares `investor-reporting/irpt-holdings-performance-lambda.zip` with the 49 Financial row by design and names this order and the first pair; `staged_from` is identical to the 49 Financial entry's (the `scopes.json` entry already at `69679b90e3dc52b670d33fddd96d06be1deaac90`). Change NOTHING else in the file (the re-pin lines are already merged). Commit that edit alone with `.tools/safe-commit.sh` before the build.
3. **Build and compare the second zip.** `BUILD_ONLY=1` first, per the addendum: build with `infra/aws/lambda/ci/build-and-upload.sh` (confirm the pipeline argument the script accepts for this function; the usage text does not list investor-reporting) from this commit. **Run the registry test on the BUILT zip before any upload:** `HP_ZIP_PATH=<the built zip> python -m pytest infra/aws/lambda/investor-reporting/holdings-performance/tests/test_zip_registry_resolves.py -q`; it MUST pass (record `build.registry_test_on_built_zip` {`command`, `rc`}); a failure is a STOP. Download the live version `vrBQAr57i...` and compare member by member by name and content: **`build.upload_member_diff` must be EXACTLY `["infra/logic/registry/scopes.json"]`**, and that member's sha256 (`build.scopes_member_sha256`) must equal `6ce64167c26588521fded21330dc59e0109450e9a01c92e0f6ca9aa90b53cfae`. Any other member, count or hash differing is a STOP before upload.
4. **Upload, plan, apply.** Upload the built zip under the same key (record `build.live_version_before`, `build.landed_version_id`, `build.built_equals_landed`). Then a plan (`.tools/terraform.exe`; the full or the targeted plan of the holdings-performance root) must read **0 to add, 3 to change, 0 to destroy** with the changed addresses exactly `module.irpt_holdings_performance.aws_lambda_function.this`, `module.irpt_holdings_performance_inf.aws_lambda_function.this`, `module.irpt_holdings_performance_cot.aws_lambda_function.this` (record `plan`); any other shape is a STOP. ONE `.tools/safe-apply.sh` from the saved plan. Read back all three `CodeSha256` (one value, equal to the built zip's; record `build.live_codesha256_after`); stamp with `record-deploy-scope.py` as before (the Cottonwood row now exists); a post-apply plan reads `No changes` (`plan.replan_no_changes`).
5. **The 49 Financial and Inflection derivations, read after the apply (the CTO's condition 2).** Run the full-derivation comparison on the staged code now live: extract the NEW zip, run in a fresh `python -I` process the producer's own `firm_scope()`, `resolved_prefix()` and the builders' `address()`/`name()` for `schwab_08335338` and `orion`, and compare with the same run on the previous zip (`vrBQAr57i`): identical in every key. Record `derivations_after` {`identical_to_before`: true, `keys_compared`}. A difference is a STOP and Rollback.
6. **The catch-up, resumed from date 1.** Exactly the first pair's twelve dates (`deliverables/0.9.0_WK_IRPT_DASHBD~403/PACKET_FACTS_R115.json` `catch_up.dates`: the silver trading days 2026-09-28 to 2026-10-13; 2026-06-09 excluded and NOT written; 36 keys read ABSENT first by a fresh LIST). A different set (for example 2026-10-14, if its silver has landed) is NOT written here: the first scheduled fire computes it. The ONLY invokes this order permits are of `irpt-cot-holdings-performance-lambda` with the event `{"date": "<D>", "source": "blackdiamond_z09"}`, one date at a time, OLDEST FIRST, stopping at the first non-zero or errored return (a STOP). Record `apply_started_utc` (the instant just before the first write) and `catch_up` {`dates`, `excluded`, `keys` (the builder's order), `count`}.
7. **The after-read and the reader check.** (a) A fresh LIST: all 36 keys exist; the objects written in the window under both gold prefixes are EXACTLY the 36 keys; the newest gold daily date is 2026-10-13; each new `manifest.json` reads `schema_version` `1.2`. (b) The three readers `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, `infra/aws/lambda/investor-reporting/performance/holdings_gold.py` are each run read only (by calling their reading code on a partition, not by invoking a function) against ONE schema-1.1 partition (a Cottonwood date at or before 2026-09-25) and ONE schema-1.2 partition; each reads both clean. Record `reader_check` {`v11_date`, `v12_date`, `readers` [{`file`, `v11`, `v12`}], `method_words`}. A reader not clean on both is a STOP: the schedule is NOT enabled. (c) The planted listing test: `python -m pytest infra/aws/lambda/investor-reporting/holdings-performance/tests/test_refused_listing_fails_loud.py -q`; record `listing_test` {`command`, `rc`}.
8. **ENABLE, only now.** In `infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf`, in the block `irpt_holdings_performance_cot`, the single line `state = "DISABLED"` becomes `state = "ENABLED"`; nothing else moves; commit it. A plan reads `0 to add, 1 to change, 0 to destroy` (record `enable.plan` and `enable.after_read_before_enable` true); ONE `safe-apply`; read back the schedule: `ENABLED`, `cron(15 8 ? * MON-FRI *)`, `America/New_York`, target the Cottonwood function, input naming `blackdiamond_z09`.
9. **Do NOT close the ledger** (`ledger_closed` false). After the first scheduled fire of the 49 Financial and of the Inflection function on the new zip, read each fire's return code and its one written key back and record both in the ledger (the CTO's condition); a failed fire is a Rollback. The issuer closes the Cottonwood leg after its first scheduled fire.

**Rollback (a write, never a delete).** Restore `vrBQAr57i.p3TMhjdSld3c_E5HMqX8iy` as the current object by a server-side copy over the same key, revert the source-map pin in the same commit, then a plan must read 0 to add, 3 to change, 0 to destroy on the code fields only, and each function's `CodeSha256` is read equal to the `vrBQAr57i` zip's. Any delete is Andrew's, registered as ONE call with the exact key list.

Write `COTTONWOOD_APPLY_RECORD_R2.json` in your folder with exactly: `claim` ("measured"); `gates` {`packet_blob`, `coo_half_signed`, `cto_half_signed`, `first_pair_blob`}; `ledger_entry`; `schedules_before_upload`; `build` {`registry_test_on_built_zip`, `upload_member_diff`, `scopes_member_sha256`, `live_version_before`, `landed_version_id`, `built_equals_landed`, `live_codesha256_after`}; `plan` {`add`, `add_addresses` [], `change`, `change_addresses`, `destroy`, `replan_no_changes`}; `derivations_after`; `apply_started_utc`; `catch_up`; `reader_check`; `listing_test`; `enable` {`plan` {`add`, `change`, `destroy`}, `after_read_before_enable`}; `ledger_closed`; `reads` {`vendor_calls` 0, `secret_reads` 0}.

<criterion id="DBC120-1-AC1" cell_refs="DB-c-14"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r120/p120_bcw.py" . DBC120-1-AC1</invocation><expect>DBC120-1-AC1 PASS</expect></criterion>
`DBC120-1-AC1` -- the addendum blob is the signed one and both halves read SIGNED at it; the 49 Financial and Inflection schedule states and next fires are printed; the registry test passed on the built zip before upload; the member diff against the live zip is `scopes.json` only and equals the blob at the new pin; the source map carries the new Cottonwood row (the right resource and role) and no other function entry changed; the ledger was continued; the plan is 0 to add, 3 to change (the three named functions), 0 to destroy and the post-apply plan read No changes; the 49 Financial and Inflection derivations are read identical after the apply. Base: FAIL (no record).

<criterion id="DBC120-2-AC1" cell_refs="DB-c-14"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r120/p120_bcw.py" . DBC120-2-AC1</invocation><expect>DBC120-2-AC1 PASS</expect></criterion>
`DBC120-2-AC1` -- the catch-up dates are the first pair's twelve; the keys equal the builder's addresses; each exists inside the apply window; the objects written under both gold prefixes in the window are exactly those keys; every new manifest reads schema 1.2; the reader check names the three readers, each clean on one 1.1 and one 1.2 partition, and the partitions carry those schema versions. Base: FAIL (no record).

<criterion id="DBC120-3-AC1" cell_refs="DB-c-14"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r120/p120_bcw.py" . DBC120-3-AC1</invocation><expect>DBC120-3-AC1 PASS</expect></criterion>
`DBC120-3-AC1` -- fresh reads: the three functions share one `CodeSha256` equal to the recorded one; the Cottonwood function's role is `irpt-cot-holdings-performance-role`; the schedule is ENABLED at `cron(15 8 ? * MON-FRI *)` `America/New_York`, targets the Cottonwood function and names `blackdiamond_z09`; the planted listing test passes; the enable step was a 0/1/0 plan after the after-read; the ledger was not closed. Base: FAIL (no record).

<expected_criteria>DBC120-1-AC1, DBC120-2-AC1, DBC120-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **The signed act, and nothing wider.** Writes to AWS: the ONE zip upload (the same artifact key, one new version), the Terraform applies (two `safe-apply` runs: the code updates, then the one-line ENABLE), and the 12 catch-up writes through the Cottonwood function's own invokes (36 keys). **NO other invoke; NO invoke of the 49 Financial or Inflection function; NO SSM command that runs the producer; NO hand-run of the producer against a served prefix; NO write of 2026-06-09 or of any date after 2026-10-13; NO re-pin of any registry member other than `scopes.json`; NO schedule, IAM or permission change beyond the plan; NO deletion of any object or file (deletes are Andrew's); NO change to `account_return_daily`.** Plans and applies run through `.tools/safe-apply.sh` only (never a bare `terraform apply`, never `aws lambda update-function-code`).
- **Refusal clause.** STOP and report, writing nothing further, on any of: the addendum blob differs or a half does not read SIGNED; a second open ledger or marker naming this surface; the live zip version or the three `CodeSha256` not as stated; a fire window closer than 30 minutes; the registry test failing on the built zip; a member other than `scopes.json` differing, or its bytes not the blob at the new pin; a plan other than 0/3/0 with the three named addresses; a derivation difference for the 49 Financial or Inflection channels; a catch-up invoke that errors or returns non-zero; any key outside the 36 moving or already present; a reader not clean on both schemas. After the apply, a STOP is reported with the state left as it is; the schedule stays DISABLED.
- **Commit** with `.tools/safe-commit.sh`; ASCII only. **Report once, under 150 words; report each STOP at once.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-14.resume-cottonwood-apply-second-zip-registry-repin-and-catch-up.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 7, cell `DB-c-14`.
<owned_cells>DB-c-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC120-1-AC1, DBC120-2-AC1, DBC120-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-c-14.resume-cottonwood-apply-second-zip-registry-repin-and-catch-up.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC120-1-AC1 DBC120-2-AC1 DBC120-3-AC1` BEFORE any flip; pin each artifact row to the commit that carried it. Run each criterion under `timeout 120` from the repository root and record the output and exit code verbatim.
</proof_of_spec>

**REPORT:** once, under 150 words: the three criteria's last lines; the ledger slug; the new zip version and the plan's counts; the catch-up dates and whether any STOP occurred; the schedule's state; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: no resource is deleted or rewired; the act is one zip upload (one member differs), a code update on three functions and the catch-up writes. The blast radius is the signed addendum's and the first pair's.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or grant is created or changed by this order; the Cottonwood roles exist since the first apply and the CTO half read their grants against both bucket policies.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; no served page reads a Cottonwood gold prefix today.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the Cottonwood schedule exists DISABLED since the first apply and changes only by the one-line ENABLE after the after-read; the 49 Financial and Inflection schedules are READ and printed, not changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the three criteria FAIL at base (no record) and recount from fresh Lambda, scheduler, S3 and git reads.
</preflight>
