# TO IRPT_BCKEND.TO-IB-cw-6 -- APPLY the signed Cottonwood retained-key pair: the runner bundle FIRST, then the refresh Lambda zip and the `directory` root apply (the directory wedge fix, the runner's retained-key rule and the Lambda's retained-key rule in ONE release; the QA is the first scheduled Cottonwood fire, read by the issuer) (packet blob 51c382f112; CTO half msg 11103)

<to_id>IRPT_BCKEND.TO-IB-cw-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair: packet `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_COTTONWOOD_RETAINED_KEY_PAIR_PACKET_AND_COO_HALF.md` (blob `51c382f11213b8003b122fea6262f09c7bda0b54`), CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_RETAINED_KEY_CTO_HALF.md` (SIGNED, msg 11103, @1087ec58ec). **READ THE PACKET IN FULL, sections 2, 5, 6 and 7 first.** | **Decomp cell:** `IB-cw-6` (decomposition section 255) | **outcome_ref:** FWD-7 (the directory is READY at all 3 firms) | **Not in this order:** the first scheduled Cottonwood fire's read, the filled-report check under a re-keyed account (the CTO's added condition) and the HMAC list read (all the issuer's).

---

## WORKER FACE

**Cell `IB-cw-6` (inlined).** Paths you post are `file:///` absolute URIs or markdown links to them, with the repo-relative form for another box (CLAUDE.md rule 33). No secret value, key material, account or household identifier, and no per-firm client count appears in any record, log or message; counts are PASS or FAIL. A STOP is reported to the issuer and writes nothing further.

**The act, in one line:** two artifacts move, each to a pinned build: the runner bundle object (carrying `directory_runner.py` at blob `f2d2329d39a11c4f0209e36df429a27390560c6c`) and the `irpt-directory-refresh` Lambda zip (carrying `refresh.py` at blob `304eb35580ee108f0884477894ba7eb2808e09bb`); the Terraform plan is the function's code change only.

**WHEN (the CTO's timing, msg 11103, plus the gateway notice, MSTR msg 11032).** Start only between **00:30Z and 04:30Z on 2026-10-20**; never alongside another IB2 act; never in the 11:30Z to 14:15Z band; never from 06:00Z to 06:45Z (the opal-gateway resize). If you cannot start by 04:30Z, do not start: report to the issuer, and the next window opens at 15:00Z on 2026-10-20 only if no other IB2 act is open. A started act is finished or rolled back the same turn (CLAUDE.md section 5), never left half-landed.

**Do, in this order:**
1. **Gates (READ ONLY).** (a) `git hash-object` of the packet equals `51c382f11213b8003b122fea6262f09c7bda0b54`, and the CTO half file reads SIGNED at it. (b) **Re-hash the two pins at the tree you will deploy from:** `git rev-parse HEAD:infra/aws/lambda/investor-reporting/directory/refresh.py` must read `304eb35580ee108f0884477894ba7eb2808e09bb` and `git rev-parse HEAD:data/assets/scripts/gold/investor_reporting/directory_runner.py` must read `f2d2329d39a11c4f0209e36df429a27390560c6c`; a different blob is a STOP (the half is void at another build). (c) **One change at a time:** read EVERY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), union them, print the denominator; if any open ledger names the `investor-reporting/directory` Terraform root, the function `irpt-directory-refresh` or the runner bundle key, or another seat's window is open on them, STOP. **EXCEPTION, ruled by the CTO (msg 11137, AMENDMENT 1 of this order): the HELD ledger `irpt-bckend-hmac-list-producer-hm5-20261017` does NOT block** (its legs L1 to L5 and L7 are PROVED; only L6, the QA run, is open and can close only after this release's first Cottonwood build; its gate is external, not an Andrew hold). It is exempt BY NAME and by no other rule: any OTHER open ledger or window on the three surfaces is still a STOP. Conditions of the ruling: (i) before the first write, prove that the bundle and the zip you will deploy carry hm5's members at their HEAD bytes (the HMAC list stage members of the runner bundle, and the three HMAC environment key names of the function), so nothing regresses: record `hm5_members_equal_head` true; (ii) hm5 stays OPEN and is not touched by this order; its L6 is graded by the issuer on this release's first Cottonwood fire; (iii) one change at a time, as the pair says. Print the other IB2 acts you hold and confirm none is open. (d) The time is inside the window above. (e) **Name both Branch B versions BEFORE any write:** the bundle's live version (`s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`, must read VersionId `7ywFHFyMHW5JcS7hjeGIIAWsNyyOOVMB`, ETag `643410f68f225bdd0f3a80fd33797c85`; any other version is a STOP: someone moved it) and the zip's prior S3 object version whose content sha256 equals the live function's `CodeSha256` (`I7T8wRYmv11nytYpD7i+4XCwwvy6JUaB3fdsgtHyXmA=` at 2026-10-19 23:5xZ): `s3api list-object-versions` of `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip`, paginated to the end, the count printed; download that version to scratch OUTSIDE the repository and hash it; no match is a STOP. (f) **Print the tests before any write:** `python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_directory_runner_retained_key.py infra/aws/lambda/investor-reporting/directory/tests/test_refresh_retained_key.py infra/aws/lambda/investor-reporting/directory/tests/test_refresh_failed_command_redispatch.py -q --color=no -p no:cacheprovider` must read 22 passed and 0 failed; and `python -m pytest lib/tests/test_trading_calendar.py -q --color=no -p no:cacheprovider` (`trading_calendar.py` rides both artifacts) is printed with its counts. A failing run is a STOP.
2. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`) under `org/critical_paths/change_management/` BEFORE the first write, PINNING the two blobs of gate (b) (a ledger binds the blob, not the path), naming the bundle key, the function, the root, both Branch B versions and this order, one `describe-task-definition` sweep for every task family that pulls the bundle tag if any (print the denominator); commit its `.open_deploys` sentinel at once.
3. **The runner bundle FIRST.** `bash .tools/safe-deploy.sh data/assets/scripts/gold/investor_reporting/directory_runner.py` from the tree of gate (b). Then download the new object, extract it to scratch OUTSIDE the repository, and print for each member whether its bytes equal `git show HEAD:<path>` of the same path: **every member must read equal** (record the member count and the equal count). Record the version before and after.
4. **The refresh Lambda zip.** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-directory-refresh` prints the built digest; **it must equal `3YK/4/pGsXjLNoYWmG2mqrps8y+t2QUiLiPt6osNT5g=` (hex `dd82bfe3fa46b178cb368616986da6aaba6cf32fadd905222e23edea8b0d4f98`); ABORT on any difference: never upload another digest.** Then the same build without `BUILD_ONLY`, verified by `head-object`.
5. **The `directory` root through Terraform.** `terraform validate` and a plan to a planfile that must read **0 to add, 1 to change (`module.irpt_directory_refresh.aws_lambda_function.this`, the new zip version), 0 to destroy**; any other line is a STOP and nothing is applied. Apply the planfile through `bash .tools/safe-apply.sh`, never bare `terraform apply`, never `aws lambda update-function-code`. Re-plan: no changes. Read the function's `CodeSha256` back: it must equal the zip pin of step 4. Read the function's environment KEY NAMES back (names only, no values): they must equal the set before the apply.
6. **No invoke, no fire, no QA.** Nothing is invoked and no SSM command is sent: the QA is the first scheduled Cottonwood fire (09:30 ET), read by the issuer.
7. **Close the ledger entry** only after step 6 is written; then write the record `deliverables/0.7.0_AE_CloudOps~IB2/IBcw6_apply_record.json`:
`{"gates":{"packet_blob":"51c382f11213b8003b122fea6262f09c7bda0b54","both_halves_signed":true,"pins_equal_head":{"refresh_py":"304eb35580ee","directory_runner_py":"f2d2329d39a1"},"one_change_at_a_time":true,"hm5_exempt_by_ruling_msg_11137":true,"hm5_members_equal_head":true,"ledger_opened_before_first_write":true,"outside_the_fire_band":true,"outside_the_gateway_window":true,"not_alongside_another_ib2_act":true,"branch_b_versions_named_before_write":{"bundle":"7ywFHFyMHW5JcS7hjeGIIAWsNyyOOVMB","zip_codesha256":"I7T8wRYmv11nytYpD7i+4XCwwvy6JUaB3fdsgtHyXmA=","zip_prior_s3_version_found":true},"pre_mint_tests":{"passed":22,"failed":0}},"bundle":{"minted_through":"safe-deploy","members":<n>,"members_equal_head":<n>,"version_before":"7ywFHFyMHW5JcS7hjeGIIAWsNyyOOVMB","version_after":"<id>"},"zip":{"built_sha256_b64":"3YK/4/pGsXjLNoYWmG2mqrps8y+t2QUiLiPt6osNT5g=","equals_pin":true,"head_object_verified":true},"terraform":{"plan":{"add":0,"change":1,"destroy":0,"addresses_changed":["module.irpt_directory_refresh.aws_lambda_function.this"]},"applied_through":"safe-apply","replan_no_changes":true,"function_codesha256_after":"3YK/4/pGsXjLNoYWmG2mqrps8y+t2QUiLiPt6osNT5g="},"counters":{"lambda_invokes":0,"fires_started_by_hand":0,"other_iam_changes":0,"keys_written_outside_the_two_artifacts":0,"ssm_commands_sent":0},"rollback":{"bundle_version_to_restore":"7ywFHFyMHW5JcS7hjeGIIAWsNyyOOVMB","zip_s3_version_to_restore":"<the prior zip object version id>","used":false}}`
8. **Branch B (any STOP after the first write, any plan that differs, any member that differs, a CodeSha256 that differs).** Reverse order the same turn: the Terraform root back to the prior zip version (plan 0/1/0, `safe-apply`), then restore the bundle object to version `7ywFHFyMHW5JcS7hjeGIIAWsNyyOOVMB` (a copy of that version as the new current), verify both by read-back, close the ledger SUPERSEDED, report to the issuer and escalate loud.
9. Report under 150 words.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IBCW6-AC1" cell_refs="IB-cw-6"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r262/p262_cells.py" . IBCW6-AC1</invocation><expect>IBCW6-AC1 PASS</expect></criterion>
<criterion id="IBCW6-AC2" cell_refs="IB-cw-6"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r262/p262_cells.py" . IBCW6-AC2</invocation><expect>IBCW6-AC2 PASS</expect></criterion>
<criterion id="IBCW6-AC3" cell_refs="IB-cw-6"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r262/p262_cells.py" . IBCW6-AC3</invocation><expect>IBCW6-AC3 PASS</expect></criterion>

<expected_criteria>IBCW6-AC1, IBCW6-AC2, IBCW6-AC3</expected_criteria>

What the checks grade: AC1 the CTO half signed at the packet blob, the two pins re-hashed at the deploy tree, one change at a time, the ledger first, both Branch B versions named before any write, the time outside the band and the gateway window, the tests printed; AC2 the bundle minted through safe-deploy with every member equal to HEAD, the zip digest equal to the pin, the plan 0/1/0 at the named address, applied through safe-apply, a clean re-plan, the function's CodeSha256 equal to the pin; AC3 no invoke, no fire by hand, no SSM command, nothing written outside the two artifacts, the rollback versions recorded. Do not edit the checks. If the order STOPS, the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the runner bundle object via `safe-deploy`; the one Lambda zip object via `build-and-upload.sh`; the `infra/aws/terraform/investor-reporting/directory` root's apply through `safe-apply` (the planfile of step 5 only); the ledger entry; your record folder; reads: S3 head and list by exact prefix, the function configuration (key names only). **No Lambda invoke at all, no SSM command, no `aws lambda update-function-code`, no IAM, schedule, secret or other Terraform root change, no S3 key written outside the two artifacts, no deletion beyond Branch B.**
- **Refusal clause:** STOP and report, writing nothing further, on any of: a half not signed at its blob; a pin that differs at the deploy tree; an open ledger or window on the bundle, the function or the root; the bundle not at the named live version; no matching zip version; a built digest that differs from the pin; a bundle member that differs from HEAD after the mint; a plan that differs from 0/1/0 at the named address; a CodeSha256 that differs from the pin; the time outside the window. A STOP is reported, not worked around; a grant is never widened.
- **Row ids:** put the row text in your report; the issuer appends it as `IRPT_BCKEND-D2-S<k>`. **Report under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-cw-6.apply-the-cottonwood-retained-key-release-runner-bundle-and-refresh-lambda-zip.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 255 (round 18, workstream ~PM), cell `IB-cw-6`.
<owned_cells>IB-cw-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBCW6-AC1, IBCW6-AC2, IBCW6-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-cw-6.apply-the-cottonwood-retained-key-release-runner-bundle-and-refresh-lambda-zip.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN-BY-THE-PAIR -- the blast radius is the packet's section 5: the Lambda `irpt-directory-refresh` code (three firms share it), the runner bundle object (three firms share it), and the next scheduled build's served directory per firm; the rollback per key is section 5 and step 8. The pair is signed by both halves (CTO half msg 11103).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p262_cells.py IBCW6 dry-run at base on dell2 2026-10-19: AC1, AC2, AC3 FAIL (no record). Positive control (control262.py) over a synthetic repo holding the two half files and a clean record: the three positives PASS; each of 34 record negatives (a wrong packet blob, halves unsigned, a pin that differs for each file, not one change at a time, the ledger not first, inside the fire band, inside the gateway window, alongside another act, each Branch B version not named, the tests failing or too few, the bundle not via safe-deploy, a member that differs, no members, the bundle version unchanged, a wrong zip digest, an unverified zip, a plan that adds or destroys or changes another address, not safe-apply, a dirty re-plan, the function not on the pinned zip, an invoke, a hand fire, an SSM command, another IAM change, a key outside the two artifacts, the rollback versions wrong or missing or used, a long digit run) and 2 half-file negatives (unsigned; signed at another blob) and the missing record each fail their own arm, 0 unexpected. NOT measured by me: the live apply, the Terraform plan (IB2 reads it), the first fire.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2`. Class WORLD (a Lambda zip and a runner bundle served to three firms' directory builds).
</preflight>
