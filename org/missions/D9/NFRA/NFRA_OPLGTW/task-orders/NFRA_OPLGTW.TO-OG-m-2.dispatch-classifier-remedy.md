# NFRA_OPLGTW task order -- `OG-m-2` -- ROUND 3 (E11 remedy, WORLD): the 49F gold dispatcher grades the chain log, and the S3 accelerator dispatches only on a qualified marker

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-m-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is created or changed; the floor schedule cron(45 12 * * ? *) and the S3 notification are untouched.
comp-iam: RUN -- `comp-iam service advi-49f-gold-dispatch` at the cut (2026-09-29, HEAD before this commit): 5 calls across 5 statements, 3 GRANTED-BROAD (ec2:DescribeInstances, ssm:DescribeInstanceInformation, ssm:GetCommandInvocation), 2 UNRESOLVABLE-RESOURCE (ec2:StartInstances, ssm:SendCommand), 0 s3 calls. PHASE A re-runs it after the code change. the ONE change is two s3:GetObject statements on the dispatcher's own inline policy (advi-49f-gold-dispatch-role / advi-49f-gold-dispatch-scoped), each on one key prefix, no ListBucket; PHASE A prints the targeted plan so the grant is read before GO.
comp-adversary: DECLARED-NOT-APPLICABLE -- the scope is ruled by 1.0.0_SA_CTO~O (msg 26305, option (a)) on a measured read (OG-m-1, MARKER_STORM_READ.md); the act is gated on a signed never-widen pair.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3, Lambda, IAM via Terraform).
</preflight>

## 1. THE CELL -- `OG-m-2` (decomposition addendum R2-E.1, item E11 remedy)

**What was measured** (OG-m-1, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/MARKER_STORM_READ.md`
and `.json`; rows `NFRA_OPLGTW-Z-W13-S1`, `-Z-W13-S2`), window 2026-09-15T23:45Z..2026-09-28T23:45Z:
- 104 dispatcher invocations: 91 from `aws:s3` (the silver-complete accelerator), 13 from `advi.49f.scheduled-floor`.
  Outcomes: 48 CHAIN REFUSED, 33 CHAIN ABORT, 15 UNKNOWN, 8 running past the poll budget, **0 CHAIN OK**.
- All 13 floor runs read UNKNOWN. The dispatcher classifies SSM `StandardOutputContent`, which is cut at 24,000
  characters; 4 of the 5 sampled chain logs end `CHAIN OK`, and their stdout is exactly 24,000 bytes with no terminal line.
- The marker `schwab/08335338/meta/complete/date=YYYY-MM-DD.json` (bucket `opal-data-assets`) is PUT about 10 times per
  date; on the 3 newest dates 9 of 10 versions carry `closure.status` = `incomplete` and the last `qualified`. Each PUT
  fires the S3 notification, so each dispatched the whole chain.

**The ruling** (1.0.0_SA_CTO~O, msg 26305, option (a)), verbatim: *"The classifier grades the chain log's terminal line,
not SSM stdout cut at 24,000 chars. The S3 accelerator dispatches only on a qualified marker. The writer stays
untouched."*

**The code at the issuance base** -- `infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py` (215 lines;
print it in full before you edit):
- `:90-101` `_classify(stdout)` scans every stdout line for `CHAIN OK` / `CHAIN REFUSED` / `CHAIN ABORT`, else
  `UNKNOWN(first_line=...)`.
- `:104-128` `_trigger_identity(event)`: a scheduler event carries `source`; an S3 event is recognised by
  `Records[0].eventSource == "aws:s3"` and yields `("advi.49f.silver-accelerator", key)`.
- `:131-215` `lambda_handler`: prints `Event:`, ensures the host is running, `ssm.send_command` ONCE (`:160-166`), polls
  `get_command_invocation` for `POLL_BUDGET_S` (300 s), then `_classify(inv["StandardOutputContent"])` (`:203`).
- **The DEPLOYED package is OLDER than this file.** Live `CodeSha256` `fEMCZ4usqXuIC1GhklcClwOn/O6vR+uV+xgbk+oj8lk=`,
  LastModified 2026-08-19T17:32:12Z, its `BUILD_MANIFEST.json` names `built_from_commit` `1abc54fa4c`. The repo file
  adds `_trigger_identity` in `e2be5c2f42` ("BUILD ONLY -- NOT APPLIED", 2026-08-29), which has never shipped. Your
  deploy ships it too; it is named in the never-widen ask and you need it (it yields the marker key).

**The chain log, and how a dispatch finds its own.** The SSM document `advi-49f-chain-dispatch`
(`infra/aws/terraform/opal-assets/advi_49f_floor.tf:272`, `:279`, `:290`) sets `TS=$(date -u +%Y%m%dT%H%M%SZ)`, tees the chain to
`/tmp/advi_49f_chain_${TS}.log`, and uploads it to `s3://opal-data-49financial/gold/advi/_logs/chain_${TS}.log` BEFORE it
exits (the dispatcher passes no `Date`, so the suffix is `TS` alone). OG-m-1 paired 5 of 5 sampled dispatches with
their logs by exactly this rule: the key's `TS` equals the invocation's `ExecutionStartDateTime` to the second
(e.g. command `502de082...`, exec start 2026-09-28T12:45:42.498Z, log `chain_20260928T124542Z.log`).

**Build exactly this (the SSM document, the notification and the writer are NOT touched):**
1. **Classify from the chain log.** When the invocation is terminal within the poll budget, derive the log key from
   `inv["ExecutionStartDateTime"]` (UTC, `%Y%m%dT%H%M%SZ`), `GetObject` it from `opal-data-49financial`, and classify by
   the LAST line of the log that starts with `CHAIN ` (`CHAIN OK` -> OK, `CHAIN REFUSED` -> REFUSED, `CHAIN ABORT` ->
   ABORT). Tolerate host-clock skew by trying TS, TS-1 s and TS+1 s, in that order; the first key that exists wins.
   If no key exists, or the log has no `CHAIN ` terminal line, the signature is
   `UNKNOWN(chain_log=<absent|no terminal line>, key=<first key tried>)` and the log line SAYS SO. SSM stdout is no
   longer the grading input (it may still be printed as context). The "running past the poll budget" branch
   (`:197-201`) is unchanged: it classifies nothing.
2. **Qualified-marker gate for the S3 path only.** When `_trigger_identity` returns a marker key, BEFORE any EC2 or SSM
   call: `GetObject` the marker from the event's bucket at the event's `versionId` (the exact PUT that fired, never the
   latest), parse the JSON and read `closure["status"]`. Anything other than `qualified` (incomplete, absent key, a
   read error, unparseable body) -> print `SKIP: accelerator marker key=<key> version=<v> closure.status=<value or
   error> -- not dispatching (only a qualified closure dispatches; the floor remains the production trigger)` and
   return `{"dispatched": false, "skip_reason": ...}`. No host start, no `send_command`. A qualified marker dispatches
   exactly once, as today. The scheduled-floor path (`source` in the event) is untouched: it reads no marker.
3. **Never re-dispatch.** No branch calls `send_command` more than once per invocation, and none retries on UNKNOWN,
   ABORT or REFUSED (the floor is tomorrow's retry; the module docstring's CHAIN-plane rule stands).
4. **IAM, in `infra/aws/terraform/opal-assets/advi_49f_floor.tf` `aws_iam_role_policy.advi_49f_gold_dispatch` ONLY:** add
   `s3:GetObject` on `arn:aws:s3:::opal-data-49financial/gold/advi/_logs/chain_*` and `s3:GetObject` AND `s3:GetObjectVersion` on
   `arn:aws:s3:::opal-data-assets/schwab/08335338/meta/complete/*` (AMENDMENT A1, row Z-W15-S1: a read at `versionId` needs `s3:GetObjectVersion`). No `ListBucket`, no other action or resource. (Without
   `ListBucket` an absent key reads `AccessDenied`, not `NoSuchKey`: treat both as absent.) Touch no other resource in
   that file or root.
5. **Tests.** New `infra/aws/lambda/opal-assets/tests/test_advi_49f_gold_dispatch_remedy.py` (stdlib `unittest.mock`;
   set `HOST_INSTANCE_ID` and `SSM_DOCUMENT_NAME` in the environment before importing the module from its path; stub
   the module's `ec2`, `ssm` and a new `s3` client; no network, no moto needed). Exactly these 6 tests:
   - `test_chain_log_ok_classifies_ok_once`: SSM stdout is 24,000 characters with no `CHAIN ` line; the chain log ends
     `CHAIN OK`; signature is `OK`; `send_command` called exactly once.
   - `test_chain_log_abort_classifies_abort`: the log's last `CHAIN ` line is `CHAIN ABORT stage=x rc=1`.
   - `test_missing_chain_log_is_unknown_and_says_so`: no key at TS/TS-1/TS+1; signature starts `UNKNOWN(chain_log=absent`
     and the printed line says so; `send_command` called exactly once.
   - `test_incomplete_marker_does_not_dispatch`: an S3 event whose marker version has `closure.status` `incomplete`;
     `send_command` and `start_instances` called 0 times; the SKIP line printed; `dispatched` is false.
   - `test_qualified_marker_dispatches_once`: the same event shape with `qualified`; `send_command` called exactly once.
   - `test_floor_event_reads_no_marker`: a `{"source": "advi.49f.scheduled-floor"}` event makes no marker `GetObject`
     and dispatches once.

## 2. BOUNDS

1. **Two phases.** PHASE A builds, tests, commits and PLANS, and changes nothing in AWS. PHASE B acts only after the
   issuer hands you GO (both never-widen halves SIGNED against
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-m-2_20260929.md`).
2. **Deploy route: Terraform only.** Build and upload the artifact with
   `bash infra/aws/lambda/ci/build-and-upload.sh opal-assets advi-49f-gold-dispatch` from your committed tree (its gate
   refuses uncommitted `infra/aws/lambda/` source). If it stops rc=1 with no error line at the manifest-declaration probe,
   that is row `NFRA_OPLGTW-W4-S10`: re-run once with `BAU_MANIFEST_SKIP=1` and say so in the commit message. Then
   `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.advi_49f_gold_dispatch
   -target=aws_iam_role_policy.advi_49f_gold_dispatch`. NEVER `aws lambda update-function-code`, never a bare
   `terraform apply`, never an untargeted apply of this root (it carries other pipelines).
3. **One deployer.** Before PHASE B's act, list every worktree (`git worktree list --porcelain`) and, in each,
   `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the per-tree denominator. Any OPEN
   sentinel naming `advi-49f`, `opal-assets` or `49f` -> STOP, a BLOCKING row.
4. **Window.** PHASE B's apply runs outside 12:15-13:30Z (the floor fires at 12:45Z) and outside 09:30-10:15Z (the silver
   marker bursts land ~09:46Z).
5. **NEVER-2.** Slug `nfra-oplgtw-dispatch-classifier-remedy`. Open with `python .tools/deploy_ledger.py open --slug
   nfra-oplgtw-dispatch-classifier-remedy --title "..." --author "0.9.0_WK_NFRA_OPLGTW~15 <0.9.0_WK_NFRA_OPLGTW~15@opal.agent>"
   --lambda advi-49f-gold-dispatch --leg 'iam|tf|aws_iam_role_policy.advi_49f_gold_dispatch|get-role-policy read'`,
   and commit the entry AND its sentinel BEFORE the upload. Close every leg with its proof and commit the close.
6. **Rollback, never half-landed.** Before the upload, record the previous artifact version (read at issuance:
   `opal-313476888478-lambda-artifacts` `opal-assets/advi-49f-gold-dispatch.zip` VersionId
   `MLLnDY4WlZCx94GuUkxXyQWlYXR2c5kY`, content-sha256 `fEMCZ4usqXuIC1GhklcClwOn/O6vR+uV+xgbk+oj8lk=`). If any PHASE B
   verification fails: `s3api copy-object` that version back over the key WITH its `content-sha256` metadata, revert
   your `advi_49f_floor.tf` commit on your branch, re-run the same targeted `safe-apply`, verify `CodeSha256` reads
   `fEMCZ4...` again, and close the ledger ROLLED BACK.
7. **Out of scope, never touched:** `conversion_manifest.py` and `schwab_runtime.py` (all copies), `silver.tf` (the
   S3 notification), the SSM document, the floor schedule, the host, the chain code under `_code/`.
8. You work in the worktree named in your identity line. Standing: no push, no vendor call, never `git stash`. REFUSE a
   criterion you cannot meet as written and report its measurement. A cross-firm or naming gate refusal on your commit
   is ONE BLOCKING row, never an override.

### PHASE A (no AWS write)
- Items 1-5; run the 6 tests; commit (`.tools/safe-commit.sh`; the `.py` passes `.tools/commit-gate.sh`).
- `terraform -chdir=infra/aws/terraform/opal-assets plan -target=module.advi_49f_gold_dispatch
  -target=aws_iam_role_policy.advi_49f_gold_dispatch` and print its summary line. Expected shape: the policy updated in
  place; the function unchanged until the new artifact exists (the module reads the artifact's latest S3 version).
- Write `ANNOUNCE_OG-m-2.md` in your deliverables dir: the diff stat, the 6 test names, the plan summary, the live
  `CodeSha256` and artifact VersionId re-read now, and the one-deployer census. Commit it, report, and STOP.

### PHASE B (GO only)
- Ledger open (bound 5) -> build-and-upload (bound 2) -> targeted `safe-apply` -> verify: live `CodeSha256` equals the new
  artifact's `content-sha256` and is not `fEMCZ4...`; the zip member `lambda_function.py` sha256 equals your committed
  file; the live inline policy carries exactly the two new `s3:GetObject` resources -> re-run the targeted plan (No
  changes) -> close the ledger -> run the criteria.
- The first REAL event graded by the new code (tomorrow's 12:45Z floor, or the next marker burst) is the ISSUER's close
  run, not a criterion of yours.

## 3. SURFACES

<paths>
infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py
infra/aws/lambda/opal-assets/tests/test_advi_49f_gold_dispatch_remedy.py
infra/aws/terraform/opal-assets/advi_49f_floor.tf
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-dispatch-classifier-remedy.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-m-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/dr.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 6 of 6; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-m-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/dr.AC2.sh; echo "exit=$?"</invocation><expect>live sha = artifact sha: yes; moved off previous: yes; zip member = HEAD bytes: yes; GetObject resources exact 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-m-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/dr.AC3.sh; echo "exit=$?"</invocation><expect>sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- both CTO branches, locally: a CHAIN OK run classifies OK from its chain log and dispatches once; an absent log
  reads UNKNOWN and says so; an incomplete marker dispatches nothing; a qualified marker dispatches once; the floor
  reads no marker.
- `AC2` -- the served Lambda is the built artifact of the committed source, it moved off the 2026-08-19 build, and the
  role's new read grant is exactly the two prefixes.
- `AC3` -- NEVER-2: the entry is committed at HEAD, the sentinel is gone, and the OPEN/HELD scan does not list the slug.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-m-2.dispatch-classifier-remedy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Flip `complete` only when AC1-AC3 PASS by output.
Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~15, its own queue, so it does not wait on `OG-h-1` (slot ~13). Held at issuance on the never-widen pair:
  `1.0.0_SA_CTO~O` signs the CTO half against the ask file (msg 26305: "not in advance"), `3.0.0_SA_CVO~O` the second.
  PHASE A may run before the signatures; PHASE B only after both.
- The ruling: msg 26305 (option (a)); the read: OG-m-1 @70f45e7675.
- The live package predates `e2be5c2f42`'s `_trigger_identity` (never applied); this deploy ships it. Named in the ask.
- Declared class WORLD: a Lambda code change and an IAM grant on the live 49F dispatch path.

<status>staged</status>
<round>4</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
