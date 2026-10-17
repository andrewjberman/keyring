# TO IRPT_DASHBD.TO-DB-f-2601 -- COMMIT the corrected `function-map/irpt-49f-reporting-gold-lambda.json` (the re-staged state: three fields against the drained file), read BUILD_ONLY through the function-map path and a no-change `terraform plan` of reporting-gold

<to_id>IRPT_DASHBD.TO-DB-f-2601</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>F2PORT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2PORT (the source-map port of F-SHIP, `~F2`) | **Ordered by:** the CTO's msg 10190 (no lane change; one one-file order to the applier, whose lane writes deploy stamps) and msg 10179 (BUILD_ONLY via function-map must equal `JgSV12Tz...`; a difference is a STOP to the CTO); the CTO's acceptance of the round 138 list (msg 10145, item 3) | **Decomp cell:** `DB-f-2601` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** the drain (landed on `box/dell2`), `DB-f-2204` (complete).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying MSTR's drain: `infra/aws/lambda/ci/function-map/` present, `lambda-source-map.json` gone); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded.

**What this order does.** The drain ported the 49 Financial entry into `infra/aws/lambda/ci/function-map/irpt-49f-reporting-gold-lambda.json` from a base taken BEFORE your re-stage (`3ff444434e`): the file holds `artifact_sha256` `SCt7IgN3...` (the first stage) and the older pins of `lib/trading_calendar.py` and `infra/logic/registry/systems.json`. The deployed function runs `JgSV12Tz...`. The issuer holds the corrected bytes, pinned in the repo; you put them in place, prove the build and a no-change plan, and commit them under your lane (the issuer's lane is refused on that path). Nothing is deployed, uploaded or applied by this order: it writes one repo file and records reads.

**Do, in this order:**

1. **Gates, read only.** (a) `sha256` of `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/fm49f_corrected.json` is `51193ac1b91d8b327ae24502eb51db8a80ff50c31a5f23c860b618fc51eb1691` (10,610 bytes) and the sha256 of the file now in `function-map/` is `fa6a4d9ec4419bc51bcb9aa9d2522e2ae9e212f84b1933e2e8d7429c50141d58` (the drained bytes); a different value at the target is a STOP (someone else has edited it; say who, from `git log -3` of the path). (b) Print the worktree denominator (`git worktree list --porcelain` count) and that no `.open_deploys` marker at any live worktree names `function-map/irpt-49f-reporting-gold-lambda.json`; your ledger `irpt-dashbd-49f-transaction-wiring-20261016` stays OPEN and is not touched. (c) No ledger is opened for this order: it deploys nothing. Record `gates` {`corrected_sha256`, `target_sha256_before`, `worktrees_read`, `open_markers_naming_this_file` (0)}.
2. **Put the bytes in place, exactly.** Copy `checks/r138/fm49f_corrected.json` over `infra/aws/lambda/ci/function-map/irpt-49f-reporting-gold-lambda.json` byte for byte (`cp`, never an editor or a JSON re-dump). Print the old and new values of the three fields side by side (`artifact_sha256`; the `pin` and `sha256` of the `lib/trading_calendar.py` and `infra/logic/registry/systems.json` items of `staged_from`): old `SCt7IgN3A+SXxfn8cv0QHVnhjVMmHXePihA6MnPm2nQ=`, `b2b748866020`, `21c672023898`; new `JgSV12TzBm0nHmWKKvtk35PWQvFePk3NHQzGWeACYes=`, `f25618c0b42d`, `fdecf020e721`. `git diff --stat` shows ONE file, 5 insertions and 5 deletions. Record `before_after` and `diff_stat`.
3. **BUILD_ONLY through the function-map path.** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-49f-reporting-gold-lambda`: **its base64 sha256 must equal `JgSV12TzBm0nHmWKKvtk35PWQvFePk3NHQzGWeACYes=` or STOP to the CTO (his word, msg 10179)**; nothing is uploaded. Run it twice; both lines equal. Record `build` {`zip_sha256_b64`, `second_run_equal`}.
4. **Plan, read only.** `.tools/terraform.exe` on `infra/aws/terraform/investor-reporting/reporting-gold/`: `init`, `validate`, then `plan -detailed-exitcode -lock=false` (a read). **It must exit 0 and read `No changes`.** An exit 2 or any addressed change is a STOP: record the addresses, restore the target file (`git checkout -- <file>`), commit nothing. Do NOT apply. Record `plan` {`exit_code` (0), `no_changes` (true), `root`}.
5. **Commit the file alone.** `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~IB2 <0.7.0_AE_CloudOps~IB2@opal.agent>" -F <msgfile> -- infra/aws/lambda/ci/function-map/irpt-49f-reporting-gold-lambda.json` (the message file written by a non-shell writer). The commit touches exactly that one path. Record its hash as `commit`.
6. Write `FM49F_PORT_RECORD.json` in your folder with exactly: `claim` ("measured"); `gates`; `before_after`; `diff_stat`; `build`; `plan` and, at top level, `plan_exit_code` (0) and `plan_no_changes` (true); `commit`; `reads` {`vendor_calls` 0, `secret_reads` 0}; and commit it in a second commit with the proof instance. Counts, hashes and words only.

<criterion id="DBF138-1-AC1" cell_refs="DB-f-2601" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_port.py" . DBF138-1-AC1</invocation><expect>DBF138-1-AC1 PASS</expect></criterion>
`DBF138-1-AC1` -- the file's bytes equal the pinned corrected bytes, and against the drained base exactly three fields differ: `artifact_sha256` and the two `staged_from` pins. Base: FAIL (the drained bytes).
<criterion id="DBF138-1-AC2" cell_refs="DB-f-2601" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_port.py" . DBF138-1-AC2</invocation><expect>DBF138-1-AC2 PASS</expect></criterion>
`DBF138-1-AC2` -- BUILD_ONLY through the function-map path prints the base64 sha256 `JgSV12TzBm0nHmWKKvtk35PWQvFePk3NHQzGWeACYes=` (the deployed bundle). Base: FAIL (it prints `SCt7IgN3...`).
<criterion id="DBF138-1-AC3" cell_refs="DB-f-2601" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_port.py" . DBF138-1-AC3</invocation><expect>DBF138-1-AC3 PASS</expect></criterion>
`DBF138-1-AC3` -- the record names one commit that touched exactly the one function-map file, and the reporting-gold plan read exit 0 / No changes. Base: FAIL (no record).

<expected_criteria>DBF138-1-AC1, DBF138-1-AC2, DBF138-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Nothing wider.** NO upload, NO apply, NO `update-function-code`, NO schedule change, NO deletion of any file or object, NO edit of any other `function-map/` file or of the bundle's pinned members. The plan is a read (`-lock=false`).
- **Refusal clause.** STOP and report, writing nothing further, on any of: the pinned bytes or the target's before-hash differing; BUILD_ONLY not printing `JgSV12Tz...` (to the CTO); a plan exit other than 0; a second path in the commit.
- **Row ids** are `IRPT_DASHBD-D2-IB2-S<k>` (the next free `k`); file a row for anything odd and keep working. ASCII only. **Report once, under 100 words; report each STOP at once.** Landed before Monday's 11:41Z fire.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2601.commit-the-corrected-49f-function-map-file.md
infra/aws/lambda/ci/function-map/irpt-49f-reporting-gold-lambda.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md</decomp_doc> round 138, workstream F2PORT (F-SHIP), cell `DB-f-2601`.
<owned_cells>DB-f-2601</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF138-1-AC1, DBF138-1-AC2, DBF138-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-f-2601.commit-the-corrected-49f-function-map-file.proof_of_spec.json`
(copy the shape of your prior instance). Validate with `python .tools/proof-of-spec-check.py <instance> DBF138-1-AC1,DBF138-1-AC2,DBF138-1-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the BUILD_ONLY line; the plan line; the commit hash. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; one repo file is written, nothing is deployed; the readers of the file (the three `function-map` roots using `fileset`, `lib/opal_lambda_map.py`, the build script) were read by the issuer, and the plan gate in step 4 is the consumer check.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM object is read or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed; Monday's 11:41Z fire is the landing deadline.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF138-1-AC1 to AC3 FAIL at base, and the pinned corrected bytes placed in the file make AC1 and AC2 PASS (positive control run by the issuer; the selftest has 9 arms).
lane: the <paths> block IS the grant; the function-map path is refused to the issuer's lane (owned-paths IRPT_COMPLETION_SOURCE_MAP), which is why the applier commits it (CTO msg 10190).
</preflight>
