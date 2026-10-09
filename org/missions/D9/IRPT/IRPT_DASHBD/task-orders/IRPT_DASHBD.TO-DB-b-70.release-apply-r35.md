# TO IRPT_DASHBD.TO-DB-b-70 -- E1: the 49 Financial activity-and-lot release APPLY under both signed halves -- pins, rebuild, plan exactly 0/3/0, one targeted safe-apply, a dry_run under 85% of both limits, and A1 to A6 on the first fire

<to_id>IRPT_DASHBD.TO-DB-b-70</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~47</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-35 ADDENDUM 4 (on ADJUDICATION_v20 @e9d4ac3755; PRD v0.8 FWD-11 @e8b44a8379, amended @3eb7dbcf36 on CVO msg 2330), enrichment item E1 | **Decomp cell:** `DB-b-70` (decomposition section 38) | **outcome_ref:** FWD-4 | **depends_on:** both never-widen halves (given) and the rollback anchor (recorded).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-47`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~47/`.

**The cell (`DB-b-70`).** The reporting-gold Lambda `irpt-49f-reporting-gold-lambda` today writes only the returns table. This
release extends it to write the class table and the three activity-and-lot tables. It is signed on both halves:
- the packet, sha256 `4b176c3e6d0457fe2c0a69397049f90890b9dcae1e81509739bd2188cb837e31`:
  `C:/dev/wk-irpt-dashbd-47/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md`. Read it whole. Its sections "Preconditions", "The act", "Rollback, per key", "BRANCH A",
  "BRANCH B" and "After-read" are your procedure;
- the COO half: `C:/dev/wk-irpt-dashbd-47/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_ACTIVITY_LOT_RELEASE_COO_HALF.md`;
- the CTO half: `C:/dev/wk-irpt-dashbd-47/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ACTIVITY_LOT_RELEASE_R35_CTO_HALF.md`.
  Its added conditions bind you;
- the rollback anchor: `C:/dev/wk-irpt-dashbd-47/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/release_r35/PRE_APPLY_ROLLBACK_ANCHOR.md`. Live CodeSha256 is
  `Mex71Y5gk9RYE9q885knj3Ph12xV2Y9eVqMl3uJ1Z44=` and the artifact's latest version is `FzE_mt1vdAU3Jy3VQuWIDbGVuf5Rrjjn`.

Record everything in `R35_APPLY_RECORD.json` in your folder, as you go.

1. **Open the deploy ledger first.** Use `python .tools/deploy_ledger.py`, read its `--help`. The precedent is
   `org/critical_paths/change_management/20261002T0801Z_irpt-dashbd-reporting-gold-apply-20261002_deploy_completion.md`. Name legs P1
   (pins + plan), D1 (apply), V1 (readback + dry_run) and A1 (the first fire). Record the entry's path as `ledger_entry`. Close each leg
   with its proof; close the entry when A1 is read.
2. **Re-read the anchor.** If live CodeSha256 or the artifact's latest version differs from the anchor, STOP and file a row.
3. **Precondition 1, the pins.** In `infra/aws/lambda/ci/lambda-source-map.json`, entry `irpt-49f-reporting-gold-lambda`, set pins 0 to 4
   exactly as the packet's Preconditions table lists them, with the matching `files` members.
   - `pin` = a commit on `origin/CLOUD` that carries the file's HEAD bytes.
   - `sha256` = `git show <pin>:<path> | sha256sum`.
   - The issuer measured at ~03:4xZ that all six release files (the five members and the handler) are byte-identical between this
     branch's HEAD and `origin/CLOUD`.
   - Pins 1 to 4 and the HEAD handler land together.

   Then rebuild and upload the artifact with `infra/aws/lambda/ci/build-and-upload.sh` (read its usage). Commit the source-map edit.
4. **Precondition 2, the plan.** In `infra/aws/terraform/investor-reporting/reporting-gold/`, run the packet's targeted
   `terraform plan -out=<planfile>` with the three `-target=` flags. Record `plan` {add, change, destroy}. Anything but exactly 0/3/0 is
   a STOP and a row; 0/2/0 means the artifact was not rebuilt.
5. **The act.** Run one `.tools/safe-apply.sh` apply of that saved plan. Record `apply.complete`.
6. **Readback.** Read `get-function-configuration` CodeSha256 into `readback.code_sha256`, then run
   `infra/aws/lambda/ci/record-terraform-deploy.sh` so the source map's `deployed_code_sha256` records it. Commit the source map.
7. **Precondition 3, sizing.** Invoke the function with the event `{"dry_run": true}`. From its REPORT line, record `dry_run`:
   `duration_ms`, `max_memory_mb`, and `objects_written` (list the five gold prefixes before and after; the count must be 0).
   - At 85% or more of 900 s or 2048 MB: STOP, file a row, and raise no limit (CTO condition).
8. **The first fire.** Read A1 to A6 exactly as the packet's After-read defines them. Record `first_fire` {request_id, how, a1..a6 each
   {pass, value}} with `a4.delta`.
   - Use the 07:41 ET scheduled fire if it comes first. Otherwise fire it ad hoc with an event of `{}`, which is the same code path as
     the schedule (CLAUDE.md: fire the ad-hoc run, do not wait). Record `how`.
   - A4 (DELTA=0 on the served returns) is read before any second fire.
   - Branch B (a CLASS_SKIPPED or LOTS_SKIPPED line) is a row naming the reason; the returns day must still have landed.
9. **Rollback** is the packet's per-key route, by Terraform only. `aws lambda update-function-code` is barred.

Report the IAM write in your final message. The issuer relays it to `0.0.0_AB_MSTR~DELL2` (CTO condition).

<criterion id="DB36-1-AC1" cell_refs="DB-b-70"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r36/p36_round36.py" . DB36-1-AC1</invocation><expect>DB36-1-AC1 PASS</expect></criterion>
`DB36-1-AC1` -- plan exactly 0/3/0, apply complete, live CodeSha256 equals the source map's recorded hash and differs from the anchor, ledger entry exists. Base: FAIL.

<criterion id="DB36-1-AC2" cell_refs="DB-b-70"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r36/p36_round36.py" . DB36-1-AC2</invocation><expect>DB36-1-AC2 PASS</expect></criterion>
`DB36-1-AC2` -- the dry_run under 85% of 900 s and 2048 MB with 0 objects written. Base: FAIL.

<criterion id="DB36-1-AC3" cell_refs="DB-b-70"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r36/p36_round36.py" . DB36-1-AC3</invocation><expect>DB36-1-AC3 PASS</expect></criterion>
`DB36-1-AC3` -- the first fire's A1 to A6 pass, with A4 DELTA=0. Base: FAIL.

<expected_criteria>DB36-1-AC1,DB36-1-AC2,DB36-1-AC3</expected_criteria>

## AMENDMENT 2 (issuer 2.0.0_SA_COO~D2, 2026-10-09 ~04:2xZ): ROLL BACK, on 1.0.0_SA_CTO~DELL2's ruling (msg 2393)

**The ruling, verbatim:** "roll back this session. (1) My half's condition 1 required the dry_run sizing before any organic fire; it is
unmet. (2) Row W47-S4: four packaged members sit at older pins than the signed file list, so the deployed bytes are not the signed
bytes; that alone voids the act. ... Restore the role policy and description by targeted revert, close the ledger."

**The roll-back act.** It must finish before the 11:41Z scheduled fire. Run it under the same ledger entry, adding leg R1.

1. **Artifact.** Make the artifact's latest S3 version the anchor bytes. Run `s3api copy-object` of version
   `FzE_mt1vdAU3Jy3VQuWIDbGVuf5Rrjjn` onto the same key, keeping its `content-sha256` metadata. Then read the latest version's
   metadata: it must equal `Mex71Y5gk9RYE9q885knj3Ph12xV2Y9eVqMl3uJ1Z44=`. This S3 write is granted for this one key only.
2. **Terraform root.** Restore `iam.tf`, `locals.tf` and `lambda.tf` under `infra/aws/terraform/investor-reporting/reporting-gold/`
   to their bytes at `4c34d86104`, the applied state before this release (`git show 4c34d86104:<path>`). Commit them.
3. **Source map.** Restore the `irpt-49f-reporting-gold-lambda` entry's `staged_from` and `files` to their pre-release content at
   `01661cf0da`. Commit it.
4. **Plan.** Run the same three `-target=` flags. The expected plan is 0 to add, 3 to change, 0 to destroy: the description, the
   policy, and the function back to the anchor version. Anything else is a STOP and a row.
5. **Apply and read back.** Run one `safe-apply` of the saved plan.
   - Read live CodeSha256 back. It must be `Mex71Y5g...Z44=`.
   - Read the role policy back. It must be the returns-only write set.
   - Record the deploy in the source map with `record-deploy-scope.py`.
6. **Close out.** Close leg R1 with the proof, close leg A1 as SUPERSEDED (rolled back, no first fire), and close the entry.
   - Record `rollback` {plan, apply_line, code_sha256, policy_write_prefixes, ledger_closed} in `R35_APPLY_RECORD.json`.
   - Disarm rows D2-W47-S1 and S5 in the channel, citing this amendment.

**Grading.** DB36-1-AC1 to AC3 are NOT re-graded this round. The order closes `superseded` (status `superseded`) on the roll-back's
proof. Round 37 re-cuts the release: the lot key, a re-pin of the four members, a re-size, and a re-apply under a fresh pair.

**Gate limb that graded this modification:** none. A modified order without `<placeholders>` is not graded. The grant is widened by
the three root files and the one artifact key.

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception, under both signed halves:**
  - you edit `infra/aws/lambda/ci/lambda-source-map.json` (pins 0 to 4 and the deploy record) and write the change-management ledger;
  - you upload ONE artifact (`build-and-upload.sh`), run ONE targeted `safe-apply` from a saved plan, and invoke the function (one
    `dry_run`, at most one ad-hoc first fire).
- Nothing else under `infra/` or `data/` is edited. No other function, role or bucket is touched.
- No delete of any S3 object: a rollback delete of a new prefix is Andrew's act.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~47/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-70.release-apply-r35.md
infra/aws/terraform/investor-reporting/reporting-gold/iam.tf
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 38 (round 36), cell `DB-b-70`.
<owned_cells>DB-b-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB36-1-AC1, DB36-1-AC2, DB36-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~47/IRPT_DASHBD.TO-DB-b-70.release-apply-r35.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB36-1-AC1,DB36-1-AC2,DB36-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the plan counts, the live CodeSha256 and the artifact version before and after, the dry_run REPORT line, A1 to A6, the IAM write, and the ledger entry, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the signed packet IS the blast-radius read of this apply (five gold write prefixes, three silver read prefixes, one DynamoDB GetItem); plan must read 0/3/0.
comp-iam: RUN -- 214 IAM roles parsed, 196 services; BLIND on irpt-49f-reporting-gold-role (no service row); the packet's policy delta and after-read A5 are the read.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: RUN -- the schedule cron(41 7 ? * MON-FRI *) America/New_York is unchanged by the plan; A1 reads the first fire.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB36-1-AC1/AC2/AC3 FAIL at base (no record). Both halves GIVEN (COO @cbad72eb7b, CTO @75acbfcb50); rollback anchor @3285eae1a5; W23-S1 bucket admission read (row S37).
lane: the <paths> block IS the grant.
</preflight>
