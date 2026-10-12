# TO IRPT_BCKEND.TO-IB-pr-487 -- IB-pr-482's `irpt-performance-adapter` (the claim follows the excluded day's status, C-CHAINCLAIM) applied on lane ~IB2, the one source-map re-pin landed first

<to_id>IRPT_BCKEND.TO-IB-pr-487</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>168</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~337/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-482.md`; COO half `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_482_CLAIM_AND_PARTIAL_RELEASE_READ_AND_COO_HALF.md` (signed 2026-10-12T21:03:15Z, blob 2eef9e6b3e); CTO half `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_482_CLAIM_AND_PARTIAL_RELEASE_CTO_HALF.md` (SIGNED, Branch A, msg 6557); CTO ROUND-168 ANALYSIS section 3 item 1 (msg 6559) | **Decomp cell:** `IB-pr-487` (decomposition section 160) | **outcome_ref:** FWD-3

---

## WORKER FACE

Read the packet and BOTH halves in full first. This order applies ONE function, `irpt-performance-adapter`, under Branch A, with Branch B ready. The artifact was built and checked in round 167; you rebuild it from the candidate map and must print the same digest or abort.

| function | the only bytes that may land (CodeSha256) | expect live before | rollback S3 version |
|---|---|---|---|
| irpt-performance-adapter | `abep4h7RngMS9JomQUdkcOT3EZ+W953OdxeK0HkdzFo=` | `kMB8xCI93/9QLUnzglVIs0EIRY07SSLBiU5ln8iJwUc=` | NOT named in the packet: YOU name it at step 2, before any upload |

The served change: on performance answers the claim on a figure chained over a day that left a return out goes `measured` to `inferred` (accounts whose claim moves: 49F SI 23, YTD 19, QTD 2, 1Y 20; orion SI 750, YTD 76, QTD 7, 1Y 106), and two counts appear beside `days_linked`. **No figure moves.** One member changes, `holdings_gold.py` (1 of 71).

**Steps:**
0. **Open-deploy read (CLAUDE.md NEVER-2), then the ledger.** Read EVERY live worktree's `org/critical_paths/.open_deploys/` (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the per-tree denominator). Run ONE `describe-task-definition` sweep for every task family that pulls this artifact (the function is a Lambda; say so and name the families, which should be none besides the function itself). Open ONE ledger entry with
   `python .tools/deploy_ledger.py open ...` naming the function and the families, and COMMIT the entry and its `.open_deploys` sentinel before any upload.
1. **Source map first (the COO half's limb 3; row W337-S2, disarmed by row S111).** In `infra/aws/lambda/ci/lambda-source-map.json`, replace the `functions` entry of `irpt-performance-adapter` with the same-named entry of `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~337/candidate_source_map_482.json` (its `functions` object only; none of its `_..._` keys). The ONLY difference between the two entries at the cut is the `holdings_gold.py` `staged_from` row (pin moved to `05219b844491b6c3c9309b6b3747e54edb823299`, sha256 `5be3ce00941215c64f96bf03780e9760dee5ff843879e53e4e3b69e49f10580a`):
   print the diff and STOP if any other key differs (another seat moved the entry). ONE commit touching only that file; record its hash as `source_map_commit`.
2. **Precheck, and name the rollback version.** `get-function-configuration irpt-performance-adapter` CodeSha256 must equal `kMB8xCI93/9QLUnzglVIs0EIRY07SSLBiU5ln8iJwUc=` (a moved live version is a STOP and a row). **Then name the rollback S3 version:** list the versions of the artifact key `investor-reporting/irpt-performance-adapter.zip` in the artifact bucket (the packet names it as `s3://opal-313476888478-lambda-artifacts/...`; confirm the bucket from `lambda-source-map.json`/the function), auto-paginate, and choose the version whose content-sha256 (S3 metadata `content-sha256`, or the object's own bytes hashed) equals the live CodeSha256 `kMB8xCI93/...`.
   Record it as `rollback_version`, set `rollback_version_named_before_upload: true` only if you named it BEFORE the upload, and print the denominator (versions listed). **No nameable version: STOP before any upload, file a row, apply nothing.**
3. **Digest control (the COO half's limb 4).** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-performance-adapter` must print the sha256 `abep4h7RngMS9JomQUdkcOT3EZ+W953OdxeK0HkdzFo=`, or ABORT (apply nothing). Then the same WITHOUT `BUILD_ONLY` (the upload), then the module's Terraform path: plan `infra/aws/terraform/investor-reporting/performance` to a planfile (`s3_object_version` + `source_code_hash` only); the plan must read **1 change, 0 to destroy** and no line for another resource; any other line is a STOP. Apply with `bash .tools/safe-apply` on that planfile. **Never `aws lambda update-function-code`.**
4. **After-reads (the COO half's limb 7).** Live CodeSha256 equals `abep4h7R...`; a re-plan reads 0 changes; the function's log group from the promote time on shows 0 `TypeError` lines (state the window start); and the **four direct-invoke arms**, below.
5. **Close the ledger** and write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB168-1_release_after_reads.json`:
   `{ledger:{state:"CLOSED", slug}, source_map_commit, live_before, live_after, rollback_version, rollback_version_named_before_upload, versions_listed, build_only_digest, build_only_digest_matched, plan:{changes:1, destroys:0}, re_plan_changes, rolled_back, log:{window_start, typeerror_lines}, read_operation:"performance-report", persisted_retained_revisions:<int>, direct_invoke_arms:[{arm, exercised, unexercised_reason, figure_sha256_before, figure_sha256_after, claim_before, claim_after, days_without_base_after, days_with_return_left_out_after}], widenings, not_established:[...]}`.
   No account id, balance, figure or client name goes in it: counts, sha256, status codes and reason codes only.

**The four direct-invoke arms (the packet's instrument; read its section "Direct-invoke proof").** A direct `aws lambda invoke` of the DEPLOYED function with an API-shaped event for an Opal principal, using the function's own role (CTO ADDENDUM 3 path 1, as TO-IB-pr-368 used it; read that order's steps 2 and its event shape), no new grant.
**The read operation is `performance-report`, the function's ONE operation (`performance/entry.py` `OPERATION`, kind `read`).** **IT PERSISTS:** on its fresh path the answer is written as a retained report (`retained.py:318`); a persisted record carrying the new claim is a NEW revision (a revision is the sha256 of the whole record) and overwrites nothing. So each invoke is a write the signers see named: at most 8 invokes (each arm read BEFORE the apply and AFTER), at most 8 retained revisions, in the function's own store, by the function's own role.
Count them and record `persisted_retained_revisions` (the number of invokes that persisted; 0 only if none did). Choose the accounts from the served gold with the round-166 driver (`deliverables/0.9.0_WK_IRPT_BCKEND~331/ib166_measure.py`; keep the account ids in YOUR scratch, outside the repo, and delete the scratch at the end):
1. an account whose only excluded days are no-base days (`NO-PRIOR-HOLDINGS`, or `NON-POSITIVE-BASE` with `held_count` 0) and whose claim reads `measured` at base: after, claim `measured`, `days_without_base` > 0, `days_with_return_left_out` 0;
2. an account with an `ALL-HOLDINGS-EXCLUDED` day (and claim `measured` at base): after, claim `inferred`, `days_with_return_left_out` > 0;
3. an account with a `NON-POSITIVE-BASE` day whose prior day held a position row (and claim `measured` at base): after, claim `inferred`;
4. an unnamed status: if the served gold carries no account with one, arm 4 is UNEXERCISED against the served gold (`exercised:false`, `unexercised_reason` stating the census you ran): ABSENT is not EXERCISED-AGAINST, and the offline replay in the packet stands for it.
Each arm: read BEFORE the apply (same event shape) and AFTER with the same window and entry; record the sha256 of the figure (not the figure) before and after: **equal, to the last digit**. If no account fits arm 1, 2 or 3, say which and why; at least arms 1, 2 and 3 must be exercised for the criterion.

**Branch B (restore the live version).** If the after-reads read a 5xx or a `TypeError` in the log group, a failed arm, or any figure that differs from its before-read: re-read that the named rollback version is still present, then redeploy THAT version through the same Terraform path (`s3_object_version` + `source_code_hash`), never a console edit and never `aws lambda update-function-code`; then confirm live CodeSha256 equals `kMB8xCI93/...` and the re-plan reads 0. A function rolled back leaves AC2 FAIL; never weaken a check. Say in the close: rolled back, and why.

<criterion id="IB168-1-AC1" cell_refs="IB-pr-487"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r168/p168_cells.py" . IB168-1-AC1</invocation><expect>IB168-1-AC1 PASS</expect></criterion>
<criterion id="IB168-1-AC2" cell_refs="IB-pr-487"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r168/p168_cells.py" . IB168-1-AC2</invocation><expect>IB168-1-AC2 PASS</expect></criterion>
<criterion id="IB168-1-AC3" cell_refs="IB-pr-487"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r168/p168_cells.py" . IB168-1-AC3</invocation><expect>IB168-1-AC3 PASS</expect></criterion>

<expected_criteria>IB168-1-AC1, IB168-1-AC2, IB168-1-AC3</expected_criteria>

What the checks grade: AC1 the function's entry in the real `lambda-source-map.json` equals the candidate map's entry apart from the keys a deploy record writes, its `artifact_sha256` equals the built digest, and the after-reads file names the `source_map_commit`, which touched only that file; AC2 the LIVE CodeSha256, read from AWS at the check, equals `abep4h7R...` (so it landed and was not rolled back);
AC3 the after-reads record as listed in step 5: ledger CLOSED, the rollback version named before the upload, the BUILD_ONLY digest matched, plan 1 change and 0 destroy, re-plan 0, not rolled back, 0 `TypeError` lines over a stated window, the four arms with equal figure hashes and the claims as stated (arm 4 may be UNEXERCISED with its reason), `persisted_retained_revisions` an integer, `read_operation` `performance-report`, and no long digit run (an account id) in the record.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. One Lambda code package and one source-map file. No IAM, route, schedule, layer, environment or table change; no other function. The `bd_adapter.py` rename is NOT in this release: the candidate map re-pins `holdings_gold.py` only, so `bd_adapter.py` stays at its old pin.
- **No vendor call**, no monitor, alarm, SNS or SES. No write other than the apply and the invokes' retained-report persists named above.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if landed) on any of these: a moved live version; a source-map entry that differs from the candidate in more than the one row; a rollback version that cannot be named; a digest miss; a plan line for another resource or a plan other than 1 change and 0 destroy; a refused upload; a failed read-back; a `TypeError` or a 5xx; a figure that differs from its before-read. Never weaken a check; do not edit `p168_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-S<n>` (the next free number: check the id is free just before you commit); `surfaced_at` is `date -u +%FT%TZ` at filing.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Report to `2.0.0_SA_COO~P2` in one message under 150 words: the digest, the rollback version name (its first 8 characters), each criterion's last line, the retained-revision count.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-487.claim-and-partial-release-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 160 (round 168, workstream ~P), cell `IB-pr-487`.
<owned_cells>IB-pr-487</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB168-1-AC1, IB168-1-AC2, IB168-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-487.claim-and-partial-release-applied.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- `.tools/comp-blast irpt-performance-adapter` on dell2 2026-10-12 ~21:1xZ (served graph, vintage 2026-10-12T15:28:31Z): the function's declared dependents are two DynamoDB tables (irpt-requests, opal-users-v2) and event rules named by the graph; this order changes the function's CODE only (1 of 71 members), no IAM, route, table or schedule. The graph is the estate as of the vintage, not a fresh read.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the direct invokes use the function's own role by direct invoke (CTO ADDENDUM 3 path 1).
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the arms are direct invokes, not API calls.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p168_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~21:1xZ: IB168-1 AC1 FAIL (the real entry differs from the candidate in staged_from only: the re-pin has not landed), AC2 FAIL (live is kMB8xCI93/..., not abep4h7R...), AC3 FAIL (no after-reads file); commit-gate clean. The issuer re-computed the built member's sha256 from the repo blob at the pin (equal to the packet's), read that the live digest equals the source map's artifact_sha256 at line 3543, and read both halves.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2, IRPT_BCKEND only. Class WORLD (a deploy).
</preflight>
