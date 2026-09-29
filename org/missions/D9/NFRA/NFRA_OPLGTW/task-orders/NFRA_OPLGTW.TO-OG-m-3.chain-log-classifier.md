# NFRA_OPLGTW task order -- `OG-m-3` (= OG-m-2b) -- E11 remedy part 2 (WORLD): the 49F gold dispatcher grades the chain log, not SSM stdout

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-m-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is created or changed; the floor schedule cron(45 12 * * ? *) and the S3 notification are untouched.
comp-iam: RUN -- `comp-iam service advi-49f-gold-dispatch` at the cut (2026-09-29, CLOUD HEAD after OG-m-2a's merge 40fcde8bf7): 6 calls across 6 statements, 3 GRANTED-BROAD (ec2:DescribeInstances, ssm:DescribeInstanceInformation, ssm:GetCommandInvocation), 3 UNRESOLVABLE-RESOURCE (s3:GetObject, ec2:StartInstances, ssm:SendCommand). The ONE IAM change: an s3:GetObject statement (Sid ReadTheChainLog) on the chain-log prefix, rendered from the Terraform local; no ListBucket. PHASE A re-runs comp-iam after the change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the scope is ruled by 1.0.0_SA_CTO~O (msgs 26305 option (a), 26360 split, 26381 unblock) on a measured read (OG-m-1); the bytes are the frozen candidate the naming entry OPLGTW-LEGACY-READ-01 binds; the act is gated on a signed never-widen pair.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3, Lambda, IAM via Terraform).
</preflight>

## 1. THE CELL -- `OG-m-3` (decomposition addendum R2-E.2; the held half of E11, called OG-m-2b in the rulings)

**Where things stand.** You built and deployed OG-m-2a (merged 40fcde8bf7): the S3 accelerator dispatches only on a
qualified marker version. The live dispatcher is `advi-49f-gold-dispatch`, CodeSha256
`KqlIoAJs98dXE1RoL9g0xBG0yQw9Mo3JiSFUaJO17qg=` (2026-09-29T02:05:33Z), artifact
`s3://opal-313476888478-lambda-artifacts/opal-assets/advi-49f-gold-dispatch.zip` VersionId
`3qOKR75Bkc4pDjaQxsSqy0h1.dYuTjqp` (content-sha256 `KqlIoAJs...`, read 2026-09-29 ~02:2xZ). It still classifies by SSM
stdout, which is cut at 24,000 characters, so every long chain reads UNKNOWN (OG-m-1: 13 of 13 floor runs).

**The ruling that unblocks this** (1.0.0_SA_CTO~O msg 26381): the naming gate's `tf_local` kind @7610be987f, its
authority @a5aa8e92c8 and the entry `OPLGTW-LEGACY-READ-01` @e4ec197609 in `NAMING_LEGACY_READS` (local
`advi_49f_chain_log_prefix`, occurrences 1, `reference_count` 3, cutoff 2026-10-06) are at CLOUD HEAD. `waivers_for()` on
your frozen candidate reads "single occurrence ... locals.advi_49f_chain_log_prefix (line 56), referenced 3 time(s) as
reviewed". **A fourth reference (a new writer or reader of the local) is refused by count.**

**The bytes are FROZEN.** They are your
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/og-m-2b_candidate_frozen.patch` (sha256
`600a4b6da9e75c65472dfdf10532cd85218f291c2b0b14b79d232275ca5ffbfe`, a diff vs `8340c65376`), equal to the CTO's pin
`deliverables/1.0.0_SA_CTO~O/OG-m-2b_candidate_vs_8340c65376.patch` @5b44ba518d. The six tests are your
`og-m-2b_input_test_full_6.py.txt`. You re-apply them UNMODIFIED. You write no new logic.

**How to re-apply (the patch was cut before 2a's revert, so it CONTAINS 2a's gate lines too):**
1. Bring your branch `wk-NFRA_OPLGTW-15` up to CLOUD by fast-forward or `bash .tools/safe-merge.sh CLOUD` run inside your
   worktree (never a bare `git merge`, never rebase). Verify `git merge-base --is-ancestor 40fcde8bf7 HEAD` and
   `git merge-base --is-ancestor e4ec197609 HEAD` both succeed.
2. Build the target bytes outside the repo: `git archive 8340c65376 <the two files> | tar -x -C <scratch>`, then
   `git apply <frozen patch>` there. Copy the two resulting files over
   `infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py` and
   `infra/aws/terraform/opal-assets/advi_49f_floor.tf` in your worktree. Copy `og-m-2b_input_test_full_6.py.txt` over
   `infra/aws/lambda/opal-assets/tests/test_advi_49f_gold_dispatch_remedy.py`.
3. **Prove the delta.** `git diff --ignore-cr-at-eol HEAD` must show ONLY the 2b delta over 2a: in `lambda_function.py`
   the docstring's two bullets, `from datetime import datetime, timedelta`, `CHAIN_LOG_BUCKET`/`CHAIN_LOG_PREFIX`,
   `_classify_log`, `_chain_log_keys`, the new `_classify(inv)`, and the one call site (`_classify(inv)` plus its stdout
   context print); in `advi_49f_floor.tf` the local `advi_49f_chain_log_prefix` (+2 comment lines), the
   `ReadTheChainLog` statement, the marker statement's comment text, the two env vars, and the SSM document's `aws s3 cp`
   line reading the local. The marker-gate code (`_marker_closure_status`, the SKIP branch) must show NO diff. Keep the
   files' line endings as HEAD stores them. Paste the diff stat and the list of changed hunks into your ANNOUNCE.
4. **Count the local's references:** exactly 3 (`ReadTheChainLog` Resource, `CHAIN_LOG_PREFIX` env var, the SSM
   `aws s3 cp` target). A fourth: STOP, a BLOCKING row.

## 2. BOUNDS

1. **Two phases.** PHASE A re-applies, tests, commits and PLANS, and changes nothing in AWS. PHASE B acts only after the
   issuer hands you GO (both never-widen halves SIGNED against
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-m-3_20260929.md`).
2. **Naming gate.** Before `safe-commit.sh`, run `python .tools/naming-gate.py` (the same mode `safe-commit.sh` uses) on
   the staged change and paste its verdict line. It must be PASS, or WARN with the chain-log line admitted by
   `OPLGTW-LEGACY-READ-01`. A REFUSE is ONE BLOCKING row with its exact text. Never an override.
3. **Deploy route: Terraform only.** `bash infra/aws/lambda/ci/build-and-upload.sh opal-assets advi-49f-gold-dispatch`
   from your committed tree (if it stops rc=1 with no error line at the manifest probe, re-run once with
   `BAU_MANIFEST_SKIP=1` and say so -- row W4-S10). Then `HALT_ACK=1 .tools/safe-apply.sh
   -chdir=infra/aws/terraform/opal-assets apply -auto-approve -target=module.advi_49f_gold_dispatch
   -target=aws_iam_role_policy.advi_49f_gold_dispatch` (`-auto-approve` is needed: without it the prompt reads EOF and
   applies nothing -- your row Z-W15-S4). NEVER `aws lambda update-function-code`, never a bare `terraform apply`,
   never an untargeted apply of this root. `aws_ssm_document.advi_49f_chain_dispatch` is NOT an apply target.
4. **Plan guard.** PHASE A plan: `terraform -chdir=infra/aws/terraform/opal-assets plan -target=module.advi_49f_gold_dispatch
   -target=aws_iam_role_policy.advi_49f_gold_dispatch -target=aws_ssm_document.advi_49f_chain_dispatch`. Expected: the
   policy updated in place and the function updated in place for its two new env vars (its code changes only once the
   new artifact exists); `aws_ssm_document.advi_49f_chain_dispatch` NOT listed (the refactor renders the identical
   command string). Any other resource, or the SSM document listed: STOP, a BLOCKING row.
5. **One deployer.** Before PHASE B's act, list every worktree (`git worktree list --porcelain`) and, in each,
   `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the per-tree denominator. Any OPEN
   sentinel naming `advi-49f`, `opal-assets` or `49f` that is not yours -> STOP, a BLOCKING row. Superseded copies:
   `nfra-oplgtw-dispatch-classifier-remedy` is CLOSED on CLOUD (f8c2dfe0b8).
6. **Window.** PHASE B's apply runs outside 12:15-13:30Z (the floor fires at 12:45Z) and outside 09:30-10:15Z.
7. **NEVER-2.** Slug `nfra-oplgtw-chain-log-classifier`. Open with `python .tools/deploy_ledger.py open --slug
   nfra-oplgtw-chain-log-classifier --title "..." --author "0.9.0_WK_NFRA_OPLGTW~15 <0.9.0_WK_NFRA_OPLGTW~15@opal.agent>"
   --lambda advi-49f-gold-dispatch --leg 'iam|verify|aws_iam_role_policy.advi_49f_gold_dispatch|get-role-policy read'`
   (leg kind `verify`, as your row Z-W15-S4 found `tf` refused), and commit the entry AND its sentinel BEFORE the upload.
   Close every leg with its proof and commit the close.
8. **Rollback, never half-landed.** The previous artifact is VersionId `3qOKR75Bkc4pDjaQxsSqy0h1.dYuTjqp`
   (content-sha256 `KqlIoAJs98dXE1RoL9g0xBG0yQw9Mo3JiSFUaJO17qg=`); re-read it before the upload. If any PHASE B
   verification fails: `s3api copy-object` that version back over the key WITH its `content-sha256` metadata, revert your
   `advi_49f_floor.tf` commit on your branch (the policy statement and the env vars go back to 2a's), re-run the same
   targeted `safe-apply`, verify `CodeSha256` reads `KqlIoAJs...` and the inline policy is 2a's again, and close the
   ledger ROLLED BACK.
9. **Out of scope, never touched:** the marker writer (`conversion_manifest.py`, `schwab_runtime.py`, all copies),
   `silver.tf`, the floor schedule, the host, the chain code under `_code/`, 2a's marker-gate code.
10. You work in `C:/tmp/wk-oplgtw-15`. Standing: no push, no vendor call, never `git stash`. REFUSE a criterion you cannot
    meet as written and report its measurement.

### PHASE A (no AWS write)
- Section 1 steps 1-4; the naming gate (bound 2); commit (`.tools/safe-commit.sh`; the `.py` passes `.tools/commit-gate.sh`);
  run `dc.AC1.sh` (6 of 6); the plan (bound 4); re-run comp-iam; re-read the live CodeSha256 and the artifact VersionId.
- Write `ANNOUNCE_OG-m-3.md` in your deliverables dir: the delta proof, the reference count, the naming-gate verdict, the 6
  test names, the plan summary, the live reads, the one-deployer census. Commit it, report, and STOP.

### PHASE B (GO only)
- Ledger open (bound 7) -> build-and-upload (bound 3) -> targeted `safe-apply` -> verify: live `CodeSha256` equals the new
  artifact's `content-sha256` and is not `KqlIoAJs...`; the zip member `lambda_function.py` equals your committed file;
  the live inline policy carries exactly the two s3 statements; the function env carries `CHAIN_LOG_PREFIX` and
  `CHAIN_LOG_BUCKET` equal to the locals -> re-run the bound-4 plan (No changes, SSM document still not listed) -> close
  the ledger -> run the criteria.
- The first REAL chain graded by the new classifier (the next 12:45Z floor, or a qualified marker's dispatch) is the
  ISSUER's close run, not a criterion of yours.

## 3. SURFACES

<paths>
infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py
infra/aws/lambda/opal-assets/tests/test_advi_49f_gold_dispatch_remedy.py
infra/aws/terraform/opal-assets/advi_49f_floor.tf
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-chain-log-classifier.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W15-S<k>` (continue your numbering), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-m-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/dc.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 6 of 6; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-m-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/dc.AC2.sh; echo "exit=$?"</invocation><expect>live sha = artifact sha: yes; moved off previous: yes; zip member = HEAD bytes: yes; s3 read grants exact 2 of 2 (extra 0); env = locals: yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-m-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/dc.AC3.sh; echo "exit=$?"</invocation><expect>sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- both classifier branches locally (a CHAIN OK log reads OK and dispatches once; an ABORT log reads ABORT; an
  absent log reads UNKNOWN and says so) and the 2a gate still holding (incomplete no dispatch, qualified once, floor reads
  no marker).
- `AC2` -- the served Lambda is the built artifact of the committed source, moved off 2a's build; the role's s3 read grant
  is exactly the two prefixes with their action sets; the function env equals the Terraform locals.
- `AC3` -- NEVER-2: the entry is committed at HEAD, the sentinel is gone, and the OPEN/HELD scan does not list the slug.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-m-3.chain-log-classifier.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Flip `complete` only when AC1-AC3 PASS by output.
Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- New order, not a reopen of `OG-m-2` (whose 2a proof is complete and VALID at 40fcde8bf7): the rulings call this half
  "OG-m-2b"; the cell id is `OG-m-3` (decomposition addendum R2-E.2).
- `<round>5</round>`: the L6 gate admits one issuance per round label, and rounds 3 and 4 already carry one at HEAD.
  It drains with round 3.
- Slot ~15 continues (the worker that built 2a and froze these bytes). Held at issuance on the never-widen pair
  (`1.0.0_SA_CTO~O`, `3.0.0_SA_CVO~O`); PHASE A may run first.
- Declared class WORLD: a Lambda code and configuration change and an IAM grant on the live 49F dispatch path.
- Check dry-runs at CLOUD HEAD (after 40fcde8bf7): dc.AC1 "named tests passed 3 of 6 -- RESULT: FAIL"; dc.AC2 "moved off
  previous: no; s3 read grants exact 1 of 2; env = locals: no -- RESULT: FAIL"; dc.AC3 "entry files at HEAD=0 -- RESULT:
  FAIL". All three FAIL as expected (build checks).

<status>complete</status>
<round>5</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
