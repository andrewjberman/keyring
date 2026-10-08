# TO-IB-yr-651 -- irpt-ycharts-generate RELEASE 2 (TCKT_VNEXT X-1), run as signed

<to_id>IRPT_BCKEND.TO-IB-yr-651</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~156</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>cancelled -- issuer ruling 2.0.0_SA_COO~Y2 2026-10-08 ~18:1xZ on rows IRPT_BCKEND-D2-W156-S1 and D2-W156-S2: branch B ran as designed (release 2 applied 17:37:00Z, rolled back 17:44:54Z to ZspX0qD2.., re-read live by the issuer; AC2 and AC3 PASS, AC1 FAIL) and the order cannot pass as written -- the seat cannot decrypt irpt-requests (S1), and the live guard builds the owner from the actor, so uploads.py's on-behalf branch is unreachable (S2, confirmed by the issuer reading served.py:905-922, interactive_access.py:123-137, uploads.py:241-248). Re-release waits on a recut X-1 cell; routed to 1.0.0_SA_CTO~DELL2</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-651` (`decompositions/IRPT_BCKEND_DECOMP_R65_Y.md`)
| **Ordered by:** `1.0.0_SA_CTO~DELL2` round analysis (sweep 17) @0a91529221, item E2.

---

## WORKER FACE

### What this is

`irpt-ycharts-generate` (AWS Lambda) is live at release 1, CodeSha256 `ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI=`. Release 2
ships three changed files at pin `f7a9d0b34f`. One principal class widens: an OPAL_GLOBAL filer (home `opal-capital`) whose
profile `allowedFirmIds` explicitly names a partner firm may now create an Analysis upload FOR that firm. The stored record names
the actor in `acting_principal_id`. Both sign-off halves bound the act. Read them first; they win over this text where they differ:
- Pair (COO half): `C:\dev\ajb_workspace\org\missions\D9\IRPT\IRPT_BCKEND\deliverables\2.0.0_SA_COO~Y2\release2_ycg\NEVER_WIDEN_PAIR_RELEASE2.md` @bf4707adf1
- CTO half: `C:\dev\ajb_workspace\org\missions\D9\IRPT\IRPT_BCKEND\deliverables\1.0.0_SA_CTO~DELL2\NEVER_WIDEN_YCG_RELEASE2_X1_CTO_HALF.md` @6d24511482
(read them in your worktree at the same relative paths).

Your deliverables folder: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~156/`. Opaque ids only in every file:
no real person's name or email. The test address is a dedicated synthetic address you choose (e.g. `irpt-x1-testfiler-<date>@opal.invalid`).

### Steps, in this order

0. **Pre-checks. STOP on any miss.** `git merge-base --is-ancestor f7a9d0b34f HEAD` rc 0. Both halves present.
   `python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD` prints `changed_members=3` naming exactly
   `uploads.py`, `interactive_access.py`, `generate_installed.py`. **Live CodeSha256 re-read** (`.tools/aws lambda get-function-configuration --function-name irpt-ycharts-generate`)
   equals `ZspX0qD2...` (CTO condition 3; anything else: STOP, file a row, apply nothing). Record the S3 object version that live
   tfstate/the function uses: that is the rollback source.
1. **Ledger.** `python .tools/deploy_ledger.py open --slug irpt-ycg-release2-20261008 --author 0.9.0_WK_IRPT_BCKEND~156 --title "..." --leg ...`
   with legs L1 verify (pre-checks above), L2 s3-prefix (upload), L3 activation (apply), L4 verify (after-reads + test-data deletion).
   Commit the sentinel `org/critical_paths/.open_deploys/irpt-ycg-release2-20261008.json` and the entry IMMEDIATELY, before any write.
   Release 1's entry is the model: `org/critical_paths/change_management/20261007T2256Z_irpt-ycg-release1-20261007_deploy_completion.md`.
2. **Upload.** `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` (no BUILD_ONLY). Its
   SHA256 must equal `798Lgqw25X1am7uCjdgYdTSOY90saT2k3n8H01eOBJ0=`; otherwise STOP. Print the new S3 versionId. Close L2.
3. **Plan, commit the plan, apply.** In `infra/aws/terraform/investor-reporting/ycharts`, a targeted plan
   `-target module.irpt_ycharts_generate.aws_lambda_function.this` to a saved planfile. It must read `0 to add, 1 to change, 0 to destroy`,
   changing only `s3_object_version` and `source_code_hash`. Write the plan text to your deliverables folder as `Y65-1_plan.txt` and
   COMMIT it. Then apply the saved plan with `.tools/safe-apply.sh`. If the tag-authz gate refuses on row S334 (the `default_tags`
   fail-closed), re-run that ONE apply with `TAGAUTHZ_OVERRIDE="S334 interim, CTO~DELL2 round analysis sweep 17 E2, release 2 apply"` --
   for this apply only. Never `aws lambda update-function-code`. Close L3 with the apply line and the live CodeSha256.
4. **After-read 7 FIRST (CTO condition 2):** live CodeSha256 == `798Lgqw2...`, and a re-plan reads 0 changes. Then after-read 6:
   one direct invoke of `{"irpt_import_census": true}` returns `failed: {}`.
5. **Test filer.** Write `TEST_FILER_ITEM.json` (the exact DynamoDB item) to your deliverables folder, then ONE `put-item` into
   `opal-users-v2`: `SK` = `PROFILE`, `PK` in the form existing profile rows use (read one existing row's key SHAPE with a
   `scan --max-items 1 --projection-expression PK,SK`, print no attribute values), the test email, the fields that make
   `InteractiveAccess.current()` read OPAL_GLOBAL home opal-capital (read `_scope/interactive_access.py` and `_scope/resolve.py`
   for which), and `allowedFirmIds` = a list of EXACTLY ONE partner firm id. Never "ALL", never `opal-capital`, never two firms.
   **No login identity:** create no Cognito or other identity-provider user (CTO condition 1).
6. **After-reads 1-5 by direct IAM invoke** of `irpt-ycharts-generate` (`.tools/aws lambda invoke`). The event is an API Gateway
   v2 event for route `POST /api/scoped/investor-reporting/analysis/inputs` carrying the edge's trusted headers
   (`x-origin-verify: cloudfront`, `x-user-email`, `x-firm-id`, `x-user-type`, ... per `_scope/resolve.py` `TRUSTED_HEADERS` and
   `_authz/served.py` `verified_internal_subject`). Shape the body from `intake/tests/test_uploads_on_behalf.py` and
   `intake/tests/test_upload_door_reads_allowed_firms.py`.
   1. **Admit:** the test filer, owner = its one listed firm: admitted; read the stored record back: `acting_principal_id` = the test
      filer, `owner.firm_id` = that firm. Record EVERY key the admit wrote (index row and any S3 object, found from `intake/uploads.py`
      `create` and the ports `reports/generate_installed.py` composes) in `upload_keys`.
   2. **Refuse (a):** the same filer, for a firm NOT on its list: refused with its existing code.
   3. **Refuse (b):** an ordinary (non-OPAL_GLOBAL) subject filing for another firm: refused as before. Use a header-only synthetic
      subject; write no row for it.
   4. **Refuse (c):** the test filer naming owner `opal-capital`: refused as before.
   5. **No regression:** an ordinary subject filing for its own firm is admitted as before, and one ordinary Analysis request answers
      as before. Any record (5) writes joins `upload_keys`.
7. **Delete, every branch.** `delete-item` the test row and every `upload_keys` entry; read each back NOT FOUND.
8. **Branch B.** If any of after-reads 1-7 fails: roll back THE SAME SESSION with a targeted apply to the step-0 S3 object version,
   verify live == `ZspX0qD2...`, then still do step 7. File a BLOCKING row. `rolled_back: true`.
9. **Record and close.** Write `Y65-1_release2_after_reads.json` (keys below). Record the source map at the deployed hash with
   `infra/aws/lambda/ci/record-terraform-deploy.sh` (branch A only). Close L4 and the ledger entry (`deploy_ledger.py close-leg` /
   `close`), commit, then run the criteria.

`Y65-1_release2_after_reads.json` keys: `pin`, `census_changed_members` (list), `built_sha`, `live_before`, `rollback_source_version`,
`replan_changes`, `reads` (an object `"1"`..`"7"` -> `"PASS"` or `"FAIL: <why>"`), `test_filer_key` (`{"pk": ...}`), `upload_keys`
(list of `{"kind":"ddb","table","pk","sk"}` or `{"kind":"s3","bucket","key"}`), `deleted_not_found` (bool), `rolled_back`,
`ledger_closed`, `limits`.

### ACCEPTANCE (run from your worktree root, after your last commit)

<criterion id="Y65-1-AC1" cell_refs="IB-yr-651"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r65/y65_cells.py . Y65-1-AC1</invocation><expect>Y65-1-AC1 PASS</expect></criterion>

<criterion id="Y65-1-AC2" cell_refs="IB-yr-651"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r65/y65_cells.py . Y65-1-AC2</invocation><expect>Y65-1-AC2 PASS</expect></criterion>

<criterion id="Y65-1-AC3" cell_refs="IB-yr-651"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r65/y65_cells.py . Y65-1-AC3</invocation><expect>Y65-1-AC3 PASS</expect></criterion>

<expected_criteria>Y65-1-AC1,Y65-1-AC2,Y65-1-AC3</expected_criteria>

AC1: reads 1-7 PASS and live == built. AC2: the test row and every upload key read NOT FOUND. AC3: the branch is coherent (all
PASS -> not rolled back and live == built; any FAIL -> rolled back and live == `ZspX0qD2...`) and the ledger is closed. Base: all
three FAIL (no file). In branch B, AC1 fails BY DESIGN: report it, do not flip the order to complete; the issuer rules.

## BOUNDS

- **Grant.** The `<paths>` block. Live writes are exactly: the artifact upload, the one targeted apply (and, in branch B, the
  rollback apply), ONE test row put + delete in `opal-users-v2`, the records after-reads 1 and 5 create + their deletes. Nothing else:
  no IAM, route, authorizer, table, bucket, Cognito or other function change; no real person's row read for values or written.
- **NEVER-2.** Ledger opened and committed before any write; closed after.
- **No vendor call, no egress off Opal infrastructure, no downloads or installs, no monitor/alarm/SNS/SES.**
- **Refusal clause.** A census other than the three, a live hash other than `ZspX0qD2...` at start, a built hash other than
  `798Lgqw2...`, or a plan touching anything else: STOP, file a row, apply nothing. Never weaken a check.
- **Rows** are `IRPT_BCKEND-W156-S<k>` in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`;
  append only your own `## <ID> -- <one line>` block after re-reading the channel. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~156" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~156@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~156 <0.9.0_WK_IRPT_BCKEND~156@opal.agent>" -F <msgfile> -- <paths>`.
  Message file via the Write tool; no pre-`git add`; on `index.lock` rc=128 wait and retry, never delete the lock.
- **Search:** native Grep/Glob/Read; raw recursive grep/find in Bash is gated. **ASCII only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-651.release2-x1-run-as-signed.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~156/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/CHANGELOG.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R65_Y.md</decomp_doc> round 65, workstream ~Y, cell `IB-yr-651`.
<owned_cells>IB-yr-651</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y65-1-AC1, Y65-1-AC2, Y65-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~156/IRPT_BCKEND.TO-IB-yr-651.release2-x1-run-as-signed.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y65-1-AC1,Y65-1-AC2,Y65-1-AC3` BEFORE the flip to complete. Shape:
`deliverables/0.9.0_WK_IRPT_BCKEND~155/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's last lines; built and live CodeSha256; the S3 versionIds (new and rollback); the
apply line; whether TAGAUTHZ_OVERRIDE was used; the ledger slug and close; `upload_keys` count and NOT FOUND lines; commit hashes;
row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at f7a9d0b34f: 3 changed members of 100, one function (irpt-ycharts-generate); both halves sign this set.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added or changed; the test row is data, not a grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route, authorizer or CloudFront behaviour changes; reads go by direct IAM invoke.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- Y65-1-AC1/AC2/AC3 dry-run at base 2026-10-08 ~17:4xZ: FAIL as expected (no after-reads file); AC3 grades branch B as coherent only with a rollback, so a silent failed read cannot pass.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
