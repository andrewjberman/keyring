# TO-IB-yr-671 -- irpt-ycharts-generate RELEASE 2 (E6: X-1 with the E5 on-behalf guard), run as signed

<to_id>IRPT_BCKEND.TO-IB-yr-671</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~158</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>cancelled -- issuer ruling 2.0.0_SA_COO~Y2 2026-10-08 ~21:0xZ: branch B ran as designed (applied 20:37:56Z, rolled back 20:44:41Z to ZspX0qD2.., issuer re-read); Y67-1-AC2 PASS at the issuer on the laptop leg-2 result (4 of 4 admit keys NOT_FOUND, test row NOT FOUND), Y67-1-AC3 PASS, Y67-1-AC1 FAIL by design; the release is re-scoped by CTO msgs 1593/1597/1612 (row D2-W158-S1)</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>67</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-671` (`decompositions/IRPT_BCKEND_DECOMP_R67_Y.md`)
| **Ordered by:** `1.0.0_SA_CTO~DELL2` ADDENDA 3/7/8; CTO half @2df0aa0c99 (msg 1444).

---

## WORKER FACE

### What this is

`irpt-ycharts-generate` is live at release 1, CodeSha256 `ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI=`. Release 2 ships four changed
files at pin `1b94d50b8c`, built `Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY=`.

What it enables: an OPAL_GLOBAL filer (home `opal-capital`) whose profile `allowedFirmIds` lists a partner firm can create an Analysis
upload ON BEHALF of a verified advisor of that firm. The request names the advisor in the query parameter `advisor_email`. The stored
record's owner is that advisor, and `acting_principal_id` is the filer.

The laptop has already applied the IAM grant the advisor lookup needs (read-only `GetItem` on `opal-partner-49financial`,
`-cottonwood` and `-inflection`, at 20:25:33Z).

Read both halves first; they win over this text where they differ:
- Pair (COO half): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release2_ycg/NEVER_WIDEN_PAIR_RELEASE2_E6.md` (blob 369629b0c9)
- CTO half: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_YCG_RELEASE2_E6_CTO_HALF.md`

Your deliverables folder: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~158/`. Use opaque ids only in every
file: no real person's name or email. A real advisor appears as `adv-<first 12 hex of sha256(email)>`.

### Steps, in this order

0. **Pre-checks. STOP on any miss.**
   - `git merge-base --is-ancestor 1b94d50b8c HEAD` rc 0.
   - `python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD` prints `changed_members=4`, naming exactly
     `generate_installed.py`, `interactive_access.py`, `served.py` and `uploads.py`.
   - Live CodeSha256 re-read (`.tools/aws lambda get-function-configuration --function-name irpt-ycharts-generate`) is `ZspX0qD2...`.
   - Grant read-back: `.tools/aws iam get-role-policy --role-name irpt-ycharts-generate-role --policy-name irpt-ycharts-generate`
     holds Sid `ReadPartnerProfileRowForOnBehalfAdvisor` with GetItem on exactly the three tables. That is after-read 0.
   - Record the S3 object version the function uses now: the rollback source.
1. **Ledger.** `python .tools/deploy_ledger.py open --slug irpt-ycg-release2-e6-20261008 --author 0.9.0_WK_IRPT_BCKEND~158 ...` with
   these legs:
   - L1 verify: the pre-checks;
   - L2 s3-prefix: the upload;
   - L3 activation: the apply;
   - L4 verify: after-reads 1-7 and the cleanup handover.

   Commit the sentinel and the entry before any write. Model: `org/critical_paths/change_management/20261008T1732Z_irpt-ycg-release2-20261008_deploy_completion.md`.
2. **Upload.** `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` (no BUILD_ONLY). The SHA256
   must be `Un0wVZqj...`, or STOP. Print the new S3 versionId.
3. **Plan, commit the plan, apply.**
   - Terraform runs from the SHARED tree's initialized root `/c/dev/ajb_workspace/infra/aws/terraform/investor-reporting/ycharts`,
     with `/c/dev/ajb_workspace/.tools/terraform.exe` and `/c/dev/ajb_workspace/.tools/safe-apply.sh`. Your worktree has no
     initialized `.terraform`, and downloads are forbidden. Before planning, `git -C /c/dev/ajb_workspace diff HEAD --stat -- infra/aws/terraform/investor-reporting/ycharts`
     must be empty. Put the planfile in a temp path outside the repo.
   - The plan is targeted: `-target module.irpt_ycharts_generate.aws_lambda_function.this`, reading `0 to add, 1 to change, 0 to destroy`
     (`s3_object_version` and `source_code_hash` only).
   - Write the plan text to `Y67-1_plan.txt` and COMMIT it, then apply with `safe-apply.sh`. Never `aws lambda update-function-code`.
4. **After-read 1 (equality)** first: live == `Un0wVZqj...`, and a re-plan reads 0 changes. **After-read 2:** a direct invoke of
   `{"irpt_import_census": true}` returns `failed: {}`.
5. **Pick the real advisor and the test firm (read-only).**
   - Choose ONE firm F among `49financial`, `cottonwood` and `inflection`.
   - Choose ONE advisor A with an `opal-users-v2` PROFILE row that has `firmId` = F and `status` = `active`, and a row in
     `opal-partner-F` keyed by the same email. Read with projections only; print no values.
   - Choose ONE email U that has an active `opal-users-v2` row at a DIFFERENT firm and NO row in `opal-partner-F` (the unlisted-firm
     advisor).
   - Record A and U only as opaque ids.
6. **Test filer (after-read 3).** Write `TEST_FILER_ITEM.json` first, then ONE `put-item` into `opal-users-v2`:
   - `SK = PROFILE`, with a synthetic `@opal.invalid` email;
   - the fields that make it OPAL_GLOBAL with home `opal-capital` (copy the model from the round-65 `TEST_FILER_ITEM.json` in
     `deliverables/0.9.0_WK_IRPT_BCKEND~156/`);
   - `status` = `active`;
   - `allowedFirmIds` = `[F]`.

   No login identity (no Cognito or other IdP user).
7. **After-reads 4-7 by direct IAM invoke** of `irpt-ycharts-generate`. The event is an API Gateway v2 event for
   `POST /api/scoped/investor-reporting/analysis/inputs` carrying the edge's trusted headers for the test filer (`x-origin-verify: cloudfront`,
   `x-user-email`, `x-firm-id: opal-capital`, `x-user-type`, and so on, per `_scope/resolve.py` `TRUSTED_HEADERS`). The selected tenant
   is F, and `queryStringParameters` carries `advisor_email`. Shape the body from `_authz/tests/test_served_on_behalf_create.py`.
   1. **(4) Real on-behalf ADMIT:** `advisor_email` = A. Admitted. Record the response's upload id and EVERY key the admit wrote in
      `admit_keys`: the `irpt-requests` row as `{"kind":"ddb","table":"irpt-requests","tenant":...,"request_revision":...}` and the
      S3 object as `{"kind":"s3","bucket":"opal-data-ycharts","key":...}`. Take them from the response and from `intake/uploads.py`
      `create` and the ports `reports/generate_installed.py` composes. Do NOT try to read `irpt-requests` yourself: this seat cannot
      decrypt it. The laptop reads it back.
   2. **(5) Unlisted-firm advisor refusal:** the same filer, `advisor_email` = U. Refused, and nothing stored.
   3. **(6) Unlisted firm refusal:** the same filer, tenant = a registry firm NOT equal to F, `advisor_email` = any advisor of that firm.
      Refused with its existing code.
   4. **(7) No regression:** an ordinary subject filing for its own firm with no `advisor_email` (header-only synthetic subject; write
      no row for it). It answers as before. If it stores a record, its keys join `admit_keys`.
8. **Cleanup handover, every branch.**
   - `delete-item` the test row and read it back NOT FOUND (`get-item`, consistent).
   - Write `Y67-1_admit_keys.json` (the `admit_keys` list, opaque) and COMMIT it. The issuer relays it to the laptop, which deletes
     those keys and returns `Y67-1_laptop_cleanup_result.json`. You do not wait for that result.
9. **Branch B.** If any of after-reads 0-7 fails:
   - roll back THE SAME SESSION: re-promote the step-0 S3 version (one `s3api copy-object`, as round 65 did), targeted apply, and
     verify live == `ZspX0qD2...`;
   - then do step 8;
   - file a BLOCKING row, and set `rolled_back: true`.
10. **Record and close.**
    - Write `Y67-1_release2_after_reads.json` with these keys: `pin`, `census_changed_members`, `built_sha`, `live_before`,
      `rollback_source_version`, `replan_changes`, `reads` (`"0"`..`"7"` -> `"PASS"` or `"FAIL: <why>"`), `test_filer_key`
      (`{"pk":...}`), `firm`, `advisor` (opaque), `unlisted_advisor` (opaque), `admit_keys`, `rolled_back`, `ledger_closed`, `limits`.
    - Branch A only: run `infra/aws/lambda/ci/record-terraform-deploy.sh`.
    - Close L4 and the ledger, then commit.
    - Run AC1 and AC3. AC2 stays FAIL until the laptop's result lands; the issuer grades it.

### ACCEPTANCE (run from your worktree root, after your last commit)

<criterion id="Y67-1-AC1" cell_refs="IB-yr-671"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r67/y67_cells.py . Y67-1-AC1</invocation><expect>Y67-1-AC1 PASS</expect></criterion>

<criterion id="Y67-1-AC2" cell_refs="IB-yr-671"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r67/y67_cells.py . Y67-1-AC2</invocation><expect>Y67-1-AC2 PASS</expect></criterion>

<criterion id="Y67-1-AC3" cell_refs="IB-yr-671"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r67/y67_cells.py . Y67-1-AC3</invocation><expect>Y67-1-AC3 PASS</expect></criterion>

<expected_criteria>Y67-1-AC1,Y67-1-AC2,Y67-1-AC3</expected_criteria>

AC2 needs the laptop's cleanup result, so you report its last line as it stands. Write the proof instance with AC2 marked `PENDING-ISSUER`.
Do NOT flip the order to complete; the issuer flips it after AC2.

## BOUNDS

- **Grant.** The `<paths>` block. Live writes are exactly:
  - the artifact upload and the one targeted apply (in branch B, also the rollback copy-object and apply);
  - ONE test row put + delete in `opal-users-v2`;
  - the records after-reads 4 and 7 create, which the laptop deletes.

  No IAM, route, authorizer, table, bucket or Cognito change; no other function. A real person's row is read by projection, never
  printed and never written.
- **NEVER-2.** Open and commit the ledger before any write; close it after.
- **No vendor call, no egress off Opal infrastructure, no downloads or installs, no monitor/alarm/SNS/SES, no SendCommand.**
- **Refusal clause.** STOP, file a row and apply nothing if:
  - the census is not exactly the four files;
  - the live hash at start is not `ZspX0qD2...`;
  - the grant is absent;
  - the built hash is not `Un0wVZqj...`;
  - the plan touches anything else.

  Never weaken a check.
- **Rows** are `IRPT_BCKEND-D2-W158-S<k>` in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`.
  Re-read the channel, then append only your own block. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~158" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~158@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~158 <0.9.0_WK_IRPT_BCKEND~158@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool. Don't pre-`git add`. Edit byte-preserving.
- **Search** with native Grep/Glob/Read. **ASCII only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-671.release2-e6-run-as-signed.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~158/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/CHANGELOG.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R67_Y.md</decomp_doc> round 67, workstream ~Y, cell `IB-yr-671`.
<owned_cells>IB-yr-671</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y67-1-AC1, Y67-1-AC2, Y67-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~158/IRPT_BCKEND.TO-IB-yr-671.release2-e6-run-as-signed.proof_of_spec.json`.
Shape: `deliverables/0.9.0_WK_IRPT_BCKEND~156/IRPT_BCKEND.TO-IB-yr-651.release2-x1-run-as-signed.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):**
- each criterion's last lines;
- the built and live CodeSha256;
- the S3 versionIds;
- the apply line;
- the ledger slug and close;
- the opaque ids for F, A and U;
- the `admit_keys` count;
- the commit hashes;
- the row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at HEAD (= pin 1b94d50b8c members): 4 changed of 100, one function; both halves sign this set; the grant is already applied by the laptop.
comp-iam: RUN (live read) -- irpt-ycharts-generate-role inline policy holds ReadPartnerProfileRowForOnBehalfAdvisor (GetItem, 3 tables), read ~20:27Z; this order adds no permission.
comp-routes: DECLARED-NOT-APPLICABLE -- no route, authorizer or CloudFront behaviour changes; reads go by direct IAM invoke.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- Y67-1-AC1/AC2/AC3 dry-run at base ~20:3xZ: FAIL as expected (no file); AC2 needs the laptop's NOT_FOUND per admit key, so a skipped cleanup cannot pass; AC3 refuses a failed read without a rollback.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
