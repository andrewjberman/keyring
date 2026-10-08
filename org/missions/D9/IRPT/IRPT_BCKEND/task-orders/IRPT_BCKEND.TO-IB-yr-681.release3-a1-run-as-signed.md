# TO-IB-yr-681 -- irpt-ycharts-generate RELEASE 3: the E6 build, proven on the TEMPLATE lane (file_base64), no new grant

<to_id>IRPT_BCKEND.TO-IB-yr-681</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~159</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-681` (`decompositions/IRPT_BCKEND_DECOMP_R68_Y.md`)
| **Ordered by:** `1.0.0_SA_CTO~DELL2` GO msg 1643, on Andrew-direct "You have egress to ycharts, do not delay" (record @5c9df0ead7).
The CTO half `NEVER_WIDEN_YCG_RELEASE3_A1_CTO_HALF.md` stands with its AMENDMENT 1: the CSV-lane grant is WITHDRAWN.

---

## WORKER FACE

### What this is

`irpt-ycharts-generate` is live at release 1, `ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI=`. Release 3 deploys the E6 build: pin
`1b94d50b8c`, built `Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY=`, four changed members. It adds NO grant. The opal-partner GetItem
grant is already live.

**What it enables:** an OPAL_GLOBAL filer (home `opal-capital`) whose profile `allowedFirmIds` lists a partner firm can create an Analysis
upload ON BEHALF of a verified advisor of that firm. The request carries query parameter `advisor_email`.

**The lane:** the TEMPLATE body (`file_base64` + `file_type`), the one the portal sends. The CSV-body lane (`csv_base64`) is being retired;
do not use it. On a template upload the function does this, in order:
1. retains the original under `opal-data-irpt/irpt/<firm>/state/original_holdings/` (already granted);
2. publishes the UPLOAD# row (owner = the advisor, `acting_principal_id` = the filer);
3. publishes the NORMALIZATION# row in RESOLVING;
4. sends ONE `resolve_upload` message to `irpt-generation`;
5. answers RESOLVING.

The resident then resolves the symbols with one batched YCharts `securities_info` call. **That vendor call is authorized** (Andrew-direct
above). A re-POST of the SAME upload token reads the row's state (RESOLVING, then NORMALIZED or NEEDS_CORRECTION) and never sends a
second message. Source: `intake/uploads.py:311-312, 370-389`; `intake/upload_resolution.py:1-48`.

Read the pair and both CTO halves first:
- `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release2_ycg/NEVER_WIDEN_PAIR_RELEASE3_A1.md` (sections 1, 3-5; IGNORE
  section 2, the grant, which is withdrawn);
- `.../deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_YCG_RELEASE3_A1_CTO_HALF.md`;
- `.../deliverables/2.0.0_SA_COO~Y2/release2_ycg/NEVER_WIDEN_PAIR_RELEASE2_E6.md` for the after-read shapes.

Your deliverables folder: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~159/`. Opaque ids only for real people:
`adv-<first 12 hex of sha256(email)>`. Do not copy any real email, name or advisor_id into a file. Round 68's model files are in
`deliverables/0.9.0_WK_IRPT_BCKEND~158/` (round 67: TEST_FILER_ITEM.json, the after-reads file, the admit keys file).

### Steps, in this order

0. **Pre-checks. STOP on any miss.**
   - `git merge-base --is-ancestor 1b94d50b8c HEAD` rc 0.
   - `release-census.py irpt-ycharts-generate --pin HEAD` reads `changed_members=4`: generate_installed, interactive_access, served, uploads.
   - Live CodeSha256 re-read is `ZspX0qD2...` (CTO condition).
   - After-read 0: `iam get-role-policy --role-name irpt-ycharts-generate-role --policy-name irpt-ycharts-generate` holds
     `ReadPartnerProfileRowForOnBehalfAdvisor` (GetItem, 3 opal-partner tables) and `RetainOriginalHoldingsUploadsOnly`, and does NOT
     hold `RetainOriginalCsvUploadsOnly` (withdrawn).
   - Record the function's current S3 object version: that is the rollback source.
1. **Ledger** `irpt-ycg-release3-20261008`, legs L1 verify / L2 s3-prefix / L3 activation / L4 verify. Open and commit it before any
   write. Model: `org/critical_paths/change_management/` entry `irpt-ycg-release2-e6-20261008`.
2. **Upload.** `build-and-upload.sh investor-reporting irpt-ycharts-generate`, no BUILD_ONLY. SHA256 must be `Un0wVZqj...`, or STOP.
3. **Plan, commit the plan, apply.**
   - Run terraform from the SHARED tree's initialized root `/c/dev/ajb_workspace/infra/aws/terraform/investor-reporting/ycharts`, with
     `/c/dev/ajb_workspace/.tools/terraform.exe` and `.../safe-apply.sh`.
   - `git -C /c/dev/ajb_workspace diff HEAD --stat -- infra/aws/terraform/investor-reporting/ycharts` must be empty.
   - Targeted plan `-target module.irpt_ycharts_generate.aws_lambda_function.this`, reading 0/1/0 (s3_object_version and source_code_hash only).
   - Write the planfile to temp outside the repo and the plan text to `Y68-1_plan.txt`, committed BEFORE the apply.
   - Never run `update-function-code`.
4. **After-read 1:** live == `Un0wVZqj...`, and a re-plan reads 0. **After-read 2:** import census `failed: {}`.
5. **Pick F, A, U (read-only, projections, no values printed).**
   - F: one of `49financial`, `cottonwood`, `inflection`.
   - A: an `opal-users-v2` PROFILE row with `firmId` = F, `status` = `active`, and a row in `opal-partner-F` with the same email.
   - U: an active `opal-users-v2` row at a DIFFERENT firm, with NO row in `opal-partner-F`.
6. **After-read 3:** write `TEST_FILER_ITEM.json`, then ONE `put-item` (synthetic `@opal.invalid` email, OPAL_GLOBAL home opal-capital as
   in round 67's item, `status` active, `allowedFirmIds` = [F]). Do NOT create a login identity.
7. **After-reads 4-7: direct IAM invoke**, an API Gateway v2 event for `POST /api/scoped/investor-reporting/analysis/inputs`.
   - Headers: the edge's trusted headers for the test filer (per `_scope/resolve.py` `TRUSTED_HEADERS`).
   - Tenant F; query `advisor_email`.
   - Body: the TEMPLATE shape, `file_base64` + `file_type` (`csv`), plus the fields `intake/upload_entry.py` requires. Use a SMALL
     synthetic holdings template of 2-3 well-known listed tickers. Take the template's column shape from `intake/template_reader.py` and its
     tests.

   1. **(4) Real on-behalf ADMIT**, `advisor_email` = A.
      - The answer is RESOLVING with an `upload_id`.
      - Then re-POST the SAME token every 30 s for up to 15 minutes until the state is NORMALIZED or NEEDS_CORRECTION. Either terminal
        state counts; RESOLVING at 15 minutes also counts, recorded as `RESOLVING-TIMEOUT`.
      - Record `reads["4"]` = `"STORED-NEXT-STATE"` and `admit_final_state` = the last state. Read 4 FAILS only if the first answer is a
        refusal or has no upload_id.
      - Record in `admit_keys` EVERY key this upload may have written, derived from the code: retention, artifact, UPLOAD#,
        NORMALIZATION# rows; the S3 original under `state/original_holdings/`; and, if NORMALIZED, the INPUT# row and the
        NORMALIZED_PORTFOLIO object under `state/normalized_portfolios/`.
      - Also record `admit_tenant` = F and `upload_id`, so the laptop can sweep that tenant's rows for this upload id.
   2. **(5)** Same filer, `advisor_email` = U: refused, nothing stored.
   3. **(6)** Same filer, tenant = a registry firm other than F: refused, existing code.
   4. **(7)** Ordinary own-firm upload, no `advisor_email`, header-only synthetic subject: refused, no new admit and no write. Expected
      public code NOT_AUTHORIZED (row D2-W158-S2). Record PASS if it is refused with no write, whatever the code, and note the code.
8. **Cleanup handover, every branch.**
   - `delete-item` the test row; a consistent `get-item` reads NOT FOUND.
   - Write `Y68-1_admit_keys.json` with `admit_keys`, `admit_tenant`, `upload_id`, and a `note` asking the laptop to:
     - first read back the stored original (sha256 vs the body you sent: give `body_sha256`) and the UPLOAD# row (owner = A, as
       `adv-` id plus firm; `acting_principal_id` = the test filer);
     - then delete every key plus any other `irpt-requests` row in tenant F whose sort key contains the upload id or its artifact ids;
     - then re-read NOT_FOUND;
     - return `admit_readback` {body_sha256_match, owner_is_advisor, acting_principal_is_filer} and `results` [{key, before,
       after_delete}] with opaque ids only.
   - COMMIT that file.
9. **Branch B.** If any of 0-3 or 5-7 fails, or read 4 is refused:
   - roll back the same session (re-promote the step-0 S3 version, targeted apply, live == `ZspX0qD2...`);
   - then step 8;
   - BLOCKING row; `rolled_back: true`.
10. **Record and close.**
    - Write `Y68-1_release3_after_reads.json` with keys: `pin`, `census_changed_members`, `built_sha`, `live_before`,
      `rollback_source_version`, `replan_changes`, `reads` ("0".."7"), `admit_final_state`, `test_filer_key` {"pk"}, `firm`, `advisor`,
      `unlisted_advisor`, `upload_id`, `body_sha256`, `admit_keys`, `rolled_back`, `ledger_closed`, `limits`.
    - In branch A only, run `record-terraform-deploy.sh`.
    - Close L4 and the ledger, commit, and run the criteria. AC2 stays FAIL until the laptop result lands; the issuer grades it. Do NOT
      flip the status.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="Y68-1-AC1" cell_refs="IB-yr-681"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r68/y68_cells.py . Y68-1-AC1</invocation><expect>Y68-1-AC1 PASS</expect></criterion>

<criterion id="Y68-1-AC2" cell_refs="IB-yr-681"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r68/y68_cells.py . Y68-1-AC2</invocation><expect>Y68-1-AC2 PASS</expect></criterion>

<criterion id="Y68-1-AC3" cell_refs="IB-yr-681"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r68/y68_cells.py . Y68-1-AC3</invocation><expect>Y68-1-AC3 PASS</expect></criterion>

<expected_criteria>Y68-1-AC1,Y68-1-AC2,Y68-1-AC3</expected_criteria>

AC2 needs the laptop's result, so report it as it stands. In the proof instance, mark AC2 FAIL with the reason "PENDING-ISSUER".

## BOUNDS

- **Grant.** The `<paths>` block.
- **Live writes are exactly:**
  - the artifact upload and the one targeted apply; in branch B, the rollback copy-object and apply;
  - ONE test row put + delete in `opal-users-v2`;
  - the records after-reads 4 and 7 create, plus the ONE `resolve_upload` message read 4 sends;
  - what the resident writes for that upload.
- **Authorized vendor egress:** only the resident's own `securities_info` resolution for that one upload (Andrew-direct). No other
  vendor call, no second message, no other egress.
- No IAM, route, table, bucket, Cognito or SendCommand change. Real rows are read by projection, never printed, never written.
- **NEVER-2:** ledger first, closed after. No downloads or installs, no monitor/alarm/SNS/SES.
- **Refusal clause.** STOP, file a row and apply nothing if:
  - the census is not exactly the four files;
  - live is not `ZspX0qD2...` at start;
  - the opal-partner grant is absent, or the withdrawn CSV grant is present;
  - the built hash is not `Un0wVZqj...`;
  - the plan touches anything else.

  Never weaken a check.
- **Rows** are `IRPT_BCKEND-D2-W159-S<k>`, appended only after re-reading the channel; gate with `surprise-row-gate.py`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~159" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~159@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~159 <0.9.0_WK_IRPT_BCKEND~159@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool; no pre-`git add`; byte-preserving edits; ASCII only; native Grep/Glob/Read.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-681.release3-a1-run-as-signed.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~159/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/CHANGELOG.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R68_Y.md</decomp_doc> round 68, workstream ~Y, cell `IB-yr-681`.
<owned_cells>IB-yr-681</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y68-1-AC1, Y68-1-AC2, Y68-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~159/IRPT_BCKEND.TO-IB-yr-681.release3-a1-run-as-signed.proof_of_spec.json`.
Shape: `deliverables/0.9.0_WK_IRPT_BCKEND~158/IRPT_BCKEND.TO-IB-yr-671.release2-e6-run-as-signed.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's last lines;
- the built and live CodeSha256;
- the S3 versionIds;
- the apply line;
- the ledger slug;
- the opaque F, A and U;
- `upload_id` and `admit_final_state`;
- the `admit_keys` count;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at HEAD = the pin's 4 members of 100, one function; no grant in this cell (the CSV grant is withdrawn by CTO msg 1643).
comp-iam: RUN (live read) -- 16 statements in inline policy irpt-ycharts-generate of irpt-ycharts-generate-role read ~20:27Z (holds ReadPartnerProfileRowForOnBehalfAdvisor, RetainOriginalHoldingsUploadsOnly); BLIND to its 2 other inline policies (-directory-read, -ownership-map-read) and to attached managed policies; this order adds no permission.
comp-routes: DECLARED-NOT-APPLICABLE -- no route, authorizer or CloudFront behaviour changes; reads go by direct IAM invoke.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger changes; the one resolve_upload message is the template lane's own dispatch.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- Y68-1-AC1/AC2/AC3 dry-run at base: FAIL as expected (no file); AC2 needs the laptop's admit read-back (body sha, owner, actor) and NOT_FOUND per key, so neither a skipped cleanup nor an unproven admit can pass.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
