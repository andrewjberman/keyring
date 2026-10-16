# NFRA_MCPORTAL task order -- `MP-pd-7` -- WORKSTREAM PC ROUND 2: the F2 release -- the grant-writer code and the gateway release that make per-person control live

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-7</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-7</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a release; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change: the writer already holds the POLICY# write the operator path uses and the gateway already holds the one invoke grant (MP-t-3); AC2 reads the served result.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's no-header invoke and its served read are the adversary.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane through safe-apply (one Lambda's code) and S3 artifact upload + SSM pull and restart of opal-gateway on i-07dccb1615503ac99 by safe-ec2-deploy; one Lambda invocation that must be refused.
</preflight>

## 1. THE CELL -- `MP-pd-7` (workstream PC round 2, decomposition sections PD.1, PD.2, PD.3 and PD.6)

**Do not start before the issuer's GO message.** The GO file is `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/GO_MP-pd-7.md`.
It carries the line `LIVE_BASE=<sha>` (the gateway release live at the GO), the gateway commits to ship, the mcportal commit, and the
Lambda source commit. It comes when G-REL7 holds: MP-pd-2, MP-pd-3 and MP-pd-4 drained; NFRA_OPLGTW OG-cp-1 RELEASED, so the live
gateway's `app/access_state.py` knows `person_access` (the Lambda's `build_package.py` stages its closure from that release); the gateway
queue free (one release in flight at a time); the never-widen pair signed against YOUR release ASK (step 2).

This is the mechanic of `MP-pc-5` (read `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pc-5.pc-gateway-release.md`
whole, and its ASK `deliverables/0.7.0_AE_CloudOps~MQ/NEVER_WIDEN_ASK_MP-pc-5.md`, which was signed and executed at `bacec95ccd`) with TWO
acts instead of one, in this order, and these differences:

**Act A -- the grant-writer Lambda code (inert until the gateway route exists).**
- Source: the Lambda directory at the GO's Lambda commit (`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`, adding the action
  `set_person_access`). Build the package with the Lambda's own `build_package.py` per `infra/aws/lambda/ci/lambda-source-map.json` and
  `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`; it stages the closure from the LIVE gateway release
  (`EC2_MANIFEST.json` `services.opal-gateway.deployed_commit`), which must already know `person_access`. A zero-diff apply with no new
  artifact is a failed leg.
- Apply ONLY through `safe-apply` (never a bare `terraform apply`; read its interface). The plan must show EXACTLY one resource
  changing in place (the function's code hash), with 0 to add and 0 to destroy; anything else: STOP, a BLOCKING row.
- Blast radius: the one function's code. It may never touch the function's role, environment, the owner key variable, the changes table,
  or any other resource. Rollback: `safe-apply` of the previous package (rebuild from the previous Lambda commit and the previous live
  release), proven before the act by a rebuild compared by md5 per member against the deployed package, with a negative control.
- Before and after the apply, invoke the function ONCE with no owner header on each of `narrow` and `set_person_access`: both must answer
  REFUSED NO-OWNER-HEADER (the four existing actions' header check is unchanged).

**Act B -- the gateway release.** On the LIVE ref (read `deployed_commit` at the act, never assume it), cherry-pick the GO's gateway worker commits
in the GO's order (MP-pd-3: `app/admin_people_access.py`, `app/admin_people.py`, their two test files), your step-0 hookup commit in
`app/admin_api.py` (the import `from . import admin_people_access` beside the other `admin_*` imports, and the line `*admin_people_access.routes,`
beside `*admin_refusals.routes,`), and the dashboard bundle at the GO's mcportal commit (MP-pd-4). Census, tests, the `EC2_MANIFEST.json`
record (`deployed_commit`, `previous_deployed_commit` corrected, `mcportal_commit`, `release_note`), the bun cache pre-check, the sparse
checkout list, the 90-second `/health` rule with an AT-ONCE rollback, and the before/after MCP tool-name lists (difference EMPTY) are
exactly MP-pc-5's steps 0 to 4, with these changes: the release census names ONLY `app/admin_api.py`, `app/admin_people.py`,
`app/admin_people_access.py`, `tests/test_admin_people.py` and `tests/test_admin_people_access.py`; any other file under
`infra/aws/ec2/opal-gateway` STOPS the act.

In order:
1. **Step 0: the hookup** (above), tested with `tests/test_admin*.py tests/test_owner_gate.py` on `box/sitez` HEAD with the payload: 0 failed.
2. **The ASK and the pair.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_MP-pd-7.md` with the blast
   radius of BOTH acts (Act A's one function; Act B's five files, the two new routes, the bundle swap, the manifest record, one restart,
   two S3 keys), what it may never touch (the MCP tool surface, any IAM, any other resource or service, the deploy scripts), the census, the
   tests, both rollbacks proven, the read-backs (AC1, AC2), and the failure branches in WORDS BOTH HALVES REPEAT, as MP-pc-5's ASK section 7 did:
   roll back AT ONCE if `/health` is not 200 within 90 seconds, or the tool-name difference is non-empty, or the existing gitstate or people
   route stops answering 401/403 to no identity, or the no-header invoke of any action stops answering REFUSED NO-OWNER-HEADER; otherwise
   a miss in AC2's served read alone is graded FAIL as measured, a row is opened, and the issuer decides. Name the semantic change:
   `GET /api/admin/people` rows gain `principal`; the access routes answer `record_kind` "not live" until the store knows the type.
   Commit it, then send ONE message to BOTH `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~MP` naming the ASK path and commit, asking each for its half.
   WAIT for both halves at HEAD of `box/sitez` (`deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-pd-7_<date>.md`,
   `deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-pd-7_<date>.md`). A refused half STOPS the act.
3. **Rollback, proven before the act**, for both acts, and the rollback TIME measured as MP-pc-5 did (record which and the seconds).
4. **NEVER-2 ledger, on your branch, in this order.** `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-pd-release`; legs:
   Lambda package build and apply, bundle build, gateway release build and upload, SSM pull and restart, manifest record. Put the census, tests,
   rollbacks and this order's path in `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/MP-pd-7_PRE_ACT_RECORD.md`, one pointer
   line in the entry; commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-pd-release.json`. ACT A, then ACT B from
   the release tree with ITS scripts (`bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`; its
   stale-base guard must read the live ref unchanged at both reads). Close every leg with its proof and commit the close BEFORE the AC reads.
5. **Close report** `deliverables/0.7.0_AE_CloudOps~NFRA1/MP-pd-7_CLOSE_REPORT.md`, which MUST contain the line `GW_LAMBDA_SHA256=<the
   function's CodeSha256 after Act A>` on a line of its own (AC2 reads it), the new `deployed_commit`, the tool counts, the rollback time and how
   it was measured.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No IAM, no Terraform logic change (you may let tooling record a build hash), no store write
   (no `person_access` record is written by this act), no change to the four existing writer actions.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report. Never leave a deploy half-landed.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/lambda/mcportal/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcportal-pd-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

(`infra/aws/lambda/mcportal/`, the source map and the `.tf` are granted so the build and apply tooling can record a hash or a variable file. Change no
logic in them; a needed logic change is a BLOCKING row.)
Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, every gateway file the GO names, and
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-7"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd7.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; closed=yes; sentinel=no; listed OPEN/HELD=0; descends=yes; outside the F2 set=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pd-7"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd7.AC2.sh; echo "exit=$?"</invocation><expect>ssm status=Success with routes, rows and the principal key read; lambda sha equals the close report's; no-header invoke REFUSED NO-OWNER-HEADER -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_MCPORTAL.TO-MP-pd-7.person-access-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with: the census; both acts' before and after (function code hash; tool counts); the two check outputs; both
rollbacks and their measured time; the new `deployed_commit`; and any row. Tell `2.0.0_SA_COO~O` the new `deployed_commit` when the ledger closes.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the PC round-2 issuance (decomposition v10). Gate G-REL7 (PD.6). The Lambda is applied BEFORE the gateway release
because the new action is unreachable until the gateway route exists, so Act A is inert on its own. If OG-cp-1 is not released when the other
three cells drain, this order waits: a Lambda built from a release that does not know `person_access` answers RECORD-KIND-NOT-LIVE to every
write (the safe state, tested by MP-pd-2). The write half of FWD-21 is Andrew-only (C2). Checks dry-run at base: AC1 FAIL (no entry), AC2 FAIL
(close report absent). Executed once as MP-pc-5 (this seat), so the mechanics are its own.

**AMENDMENT A1 (the issuer's, 2026-10-16 ~16:0xZ; CTO msgs 35104/35110/35114, CLAUDE.md rule 34):** the order was staged to `0.7.0_AE_CloudOps~MQ`; CloudOps is now seated one lane per macro per box, so every new NFRA CloudOps order goes to `0.7.0_AE_CloudOps~NFRA1` (seated by MSTR~Z at the first such need) and ~MQ retires. `<issued_to>` and every path of this order's own deliverables folder (the ASK, the pre-act record, the close report, the proof instance, the grant) now name `~NFRA1`; the one citation of `~MQ`'s MP-pc-5 ASK (a real, executed file) is left as it is. The order stays STAGED and the CTO's hold on PD (OG-cp-1 and Andrew's sitting) is unchanged; at the GO the issuer sends MSTR~Z one line naming this order so the lane is seated before the order is sent.

<status>staged</status>
<round>2</round>
<workstream>PC</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
