# TO IRPT_DASHBD.TO-DB-f-2606 -- the COTTONWOOD LANDING FUNCTION'S BUNDLE GAINS THE TRANSACTION PRODUCER, ONE cell: `infra/aws/lambda/ci/function-map/irpt-cot-account-return-daily-lambda.json` gains five members (`files`) and their five pins (`staged_from`), appended last, so that the handler of DB-f-2605 imports the producer in the packaged layout; the CTO's XA-20261016T224156Z-3c21 (msg 10002)

<to_id>IRPT_DASHBD.TO-DB-f-2606</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2606</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>F2COTBN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2COTBN (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, XA-20261016T224156Z-3c21 (msg 10002) and the accepted round 138 list (msg 10145, item 1) | **Decomp cell:** `DB-f-2606` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md`, "Cell 6") | **outcome_ref:** FWD-5 | **depends_on:** `DB-f-2605` (merged @92f40e64d9).

**Risk class WORLD** is the floor of the path below (`infra/` path): a repo JSON file in a branch. No AWS call, no build-upload, no Terraform, no push. The build, the upload, the plan and the apply are the applier's later acts (the Cottonwood pair).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2606` (branch `wk-IRPT_DASHBD-2606`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2606/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS: make no AWS call.** No client data. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The handler now imports `account_transaction_cottonwood` (guarded). The producer chain it needs is not in the function's bundle: the entry lists 16 files and 15 pins. The issuer measured that appending the five members below, with the 15 existing pins UNMOVED, makes the attribute closure over the pinned blobs and the packaged-layout import smoke pass.

**The cell (`DB-f-2606`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cotbundle.py` (your three criteria; `NEW`, `entry_problems` and the AC1 to AC3 bodies are the exact spec; it has a `--selftest`), the pinned base composition `checks/r138/cotbundle_base_entry.json`, the entry file `infra/aws/lambda/ci/function-map/irpt-cot-account-return-daily-lambda.json` and the folder's `README.md` (the file's shape), and for the pin shape the sister entry `irpt-49f-reporting-gold-lambda.json` (its `staged_from` items).
2. **The edit: ONE file, the entry above, ASCII, LF, the file's own formatting (two-space JSON indent, key order kept; the diff must show ONLY added lines in `files` and `staged_from`).** Append to `files`, in this order and after the 16 existing paths:
   `data/assets/scripts/gold/irpt_reporting/account_transaction_cottonwood.py`, `data/assets/scripts/gold/irpt_reporting/account_transaction.py`, `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, `data/assets/scripts/gold/irpt_reporting/transaction_words.json`, `data/assets/scripts/lib/stream_parquet.py`.
   Append to `staged_from`, after the 15 existing items and in the same order, five items `{"repo_path": <path>, "pin": <commit>, "packaged_as": <the same path>, "sha256": <sha256 hex of the file now>}` with exactly those four keys. `pin` is a FULL commit hash at which the file's blob hashes to that sha256 and which is an ancestor of HEAD: take `git log -1 --format=%H -- <path>` run in your worktree and VERIFY with `git show <pin>:<path>` hashed. Do NOT change the 15 existing pins, any other key of the entry (including `artifact_sha256`, which the applier stamps), or any other file.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cotbundle.py" . DBF138-6-AC1`, then `AC2`, then `AC3`. Write `RD_COT_BUNDLE_FACTS_R138.json` in your folder: `claim` ("measured"), `members_added` (5), `pins_added` (5), `existing_pins_changed` (0), `diff_added_lines`, `diff_removed_lines` (0).
4. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2606 <0.9.0_WK_IRPT_DASHBD~2606@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): the entry and the facts record in one commit, the proof in a second. **If safe-commit refuses the entry on a LANE (owned-paths) violation, STOP and report it: do not use an override.**

<criterion id="DBF138-6-AC1" cell_refs="DB-f-2606" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cotbundle.py" . DBF138-6-AC1</invocation><expect>DBF138-6-AC1 PASS</expect></criterion>
`DBF138-6-AC1` -- the entry is the base plus the five members and five pins, appended last in order, packaged at their own paths, with every other key unchanged, and each new pin resolves (a full commit, an ancestor of HEAD, the blob hashing to the pinned sha256, which is the file's sha256 now). Base: FAIL (files and pins absent).
<criterion id="DBF138-6-AC2" cell_refs="DB-f-2606" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cotbundle.py" . DBF138-6-AC2</invocation><expect>DBF138-6-AC2 PASS</expect></criterion>
`DBF138-6-AC2` -- the attribute closure: every `module.attr` the handler and the four new Python members read from a bundle member is defined at the top level of that member's PINNED blob. Base: PASS (the unchanged entry); it must stay PASS with the members added.
<criterion id="DBF138-6-AC3" cell_refs="DB-f-2606" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cotbundle.py" . DBF138-6-AC3</invocation><expect>DBF138-6-AC3 PASS</expect></criterion>
`DBF138-6-AC3` -- the bundle smoke: the pinned members laid out at their packaged paths with the handler, run under `python -I` from another directory, import the handler with `ATC_IMPORT_ERROR` None and the producer's `normalize_trn` and `emit_transaction_day` callable. Base: FAIL (the producer is not in the bundle).

<expected_criteria>DBF138-6-AC1, DBF138-6-AC2, DBF138-6-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the handler, the producers, every other function-map file, the build script, the checker.
- **AWS: none; no build-and-upload; no Terraform; no push.**
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a pin of an existing member must move for AC2 or AC3 to pass, STOP and report which, do not move it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2606-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2606/
infra/aws/lambda/ci/function-map/irpt-cot-account-return-daily-lambda.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2606.cottonwood-landing-bundle-gains-the-transaction-producer.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md</decomp_doc> round 138, workstream F2COTBN (F-SHIP), cell `DB-f-2606`.
<owned_cells>DB-f-2606</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF138-6-AC1, DBF138-6-AC2, DBF138-6-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2606/IRPT_DASHBD.TO-DB-f-2606.cottonwood-landing-bundle-gains-the-transaction-producer.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2603/IRPT_DASHBD.TO-DB-f-2603.inf-pipeline-runner-policy-gains-s4-list-on-gold-prefix.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF138-6-AC1,DBF138-6-AC2,DBF138-6-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the facts record; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; one function-map JSON file changes in a branch and nothing is built or deployed; the readers of the file (the three function-map Terraform roots, lib/opal_lambda_map.py, the build script) were read in the source-map port of this round, and the later build's hash is the applier's read.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM object is read or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF138-6-AC1 and AC3 FAIL at base, a reference entry put into the file by the issuer made all three PASS and was restored, and the checker's pure helpers are exercised by its selftest (8 arms).
lane: the <paths> block IS the grant (the function-map folder is lane IRPT_COMPLETION_SOURCE_MAP in .owned-paths.yaml; the issuer's own lane is refused there, a worker's order grant is what the path gate reads; if refused, the worker STOPS).
</preflight>
