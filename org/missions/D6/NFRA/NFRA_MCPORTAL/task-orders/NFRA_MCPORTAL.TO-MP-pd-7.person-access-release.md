# NFRA_MCPORTAL task order -- `MP-pd-7` -- WORKSTREAM PC ROUND 2: the grant-writer Lambda deployed from source through Terraform, carrying set_person_access and the WIDENING confirm (Act A only)

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
comp-schedule: DECLARED-NOT-APPLICABLE -- a Lambda code release; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change: the function keeps its role; the two reads below only call get-function and invoke.
comp-adversary: DECLARED-NOT-APPLICABLE -- the no-header invokes (narrow and set_person_access, before and after) and the deployed-bytes read are the adversary.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane through safe-apply (one Lambda's code); AWS READ of the function and the download of its own code zip from the presigned URL get-function returns; two Lambda invocations that must be refused.
</preflight>

## 1. THE CELL -- `MP-pd-7` (workstream PC round 2, decomposition section PD.1, re-scoped by AMENDMENT A2)

**Do not start before the issuer's GO message.** The GO file is `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/GO_MP-pd-7.md`.
It carries the line `LIVE_BASE=<sha>` (the gateway release live at the GO), the line `LAMBDA_COMMIT=<sha>` (the commit of the Lambda
directory to ship) and the act's deadline. This order has ONE act: the gateway release and the dashboard bundle are NOT in it.

This is the Lambda half of the mechanic of `MP-pc-5` (read `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pc-5.pc-gateway-release.md`
whole, and its ASK `deliverables/0.7.0_AE_CloudOps~MQ/NEVER_WIDEN_ASK_MP-pc-5.md`, signed and executed at `bacec95ccd`).

**The act -- the grant-writer Lambda code.**
- Source: the Lambda directory at the GO's `LAMBDA_COMMIT` (`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`). It carries the action
  `set_person_access` and the WIDENING rule (a change that adds an entry to `tools_allow` or `channels_allow` is refused `WIDEN-NO-CONFIRM`
  unless the event carries `widening_confirm` exactly `true`; a confirmed widening writes `widening_signoff`). Build the package with the
  Lambda's own `build_package.py` per `infra/aws/lambda/ci/lambda-source-map.json` and `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`;
  it stages the closure from the LIVE gateway release (`EC2_MANIFEST.json` `services.opal-gateway.deployed_commit`). Read that value at the
  act: if it is not the GO's `LIVE_BASE` at your first read or differs between your two reads, STOP and report (a release is in flight and the
  closure would not be the one the ASK named). A zero-diff apply with no new artifact is a failed leg.
- Apply ONLY through `safe-apply` (never a bare `terraform apply`; read its interface). The plan must show EXACTLY one resource changing in
  place (the function's code hash), with 0 to add and 0 to destroy; anything else: STOP, a BLOCKING row.
- Blast radius: the one function's code. It may never touch the function's role, environment, the owner key variable, the changes table, the
  gateway, or any other resource. Rollback: `safe-apply` of the previous package (rebuilt from the previous Lambda commit and the same live
  release), proven before the act by a rebuild compared by md5 per member against the deployed package, with a negative control.
- Before and after the apply, invoke the function ONCE with no owner header on each of `narrow` and `set_person_access`: record what each
  answers before; both must answer `REFUSED NO-OWNER-HEADER` after (the four existing actions' header check is unchanged).
- After the apply, download the function's code zip (the presigned URL from `aws lambda get-function`, own plane) and show that its
  `lambda_function.py` contains `WIDEN-NO-CONFIRM` and `widening_signoff`, and that the zip's md5 per member equals the package you built.

In order:
1. **The ASK and the pair.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_MP-pd-7.md` with the blast
   radius (the one function's code), what it may never touch (any IAM, the gateway, the tool surface, any other resource), the census, the build
   comparison, the rollback proven, the read-backs (AC1, AC2) and the failure branches in WORDS BOTH HALVES REPEAT, as MP-pc-5's ASK section 7 did:
   roll back AT ONCE if the post-apply no-header invoke of any action stops answering REFUSED NO-OWNER-HEADER, or the plan shows more than the one
   resource; otherwise a miss in the deployed-bytes read alone is graded FAIL as measured, a row is opened, and the issuer decides. Name the
   semantic change: `set_person_access` becomes writable when a route reaches it, and a widening needs the verified owner's `widening_confirm`;
   nothing reaches the action until the gateway mounts its route (not this order). Commit it, then send ONE message to BOTH `1.0.0_SA_CTO~Z` and
   `2.0.0_SA_COO~MP` naming the ASK path and commit, asking each for its half. WAIT for both halves at HEAD of `box/sitez`
   (`deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-pd-7_<date>.md`, `deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-pd-7_<date>.md`).
   A refused half STOPS the act.
2. **Rollback, proven before the act**, and its TIME measured as MP-pc-5 did (record which and the seconds).
3. **NEVER-2 ledger, on your branch, in this order.** `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-pd-release`; legs: package
   build, apply, deployed-bytes read. Put the census, build comparison, rollback and this order's path in
   `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/MP-pd-7_PRE_ACT_RECORD.md`, one pointer line in the entry; commit the entry AND its
   sentinel `org/critical_paths/.open_deploys/nfra-mcportal-pd-release.json`. Then the act. Close every leg with its proof and commit the close BEFORE the AC reads.
4. **Close report** `deliverables/0.7.0_AE_CloudOps~NFRA1/MP-pd-7_CLOSE_REPORT.md`, which MUST contain the line `GW_LAMBDA_SHA256=<the function's CodeSha256
   after the act>` on a line of its own (AC2 reads it), the before and after answers of both invokes, the rollback time and how it was measured.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No IAM, no Terraform logic change (you may let tooling record a build hash), no store write
   (no `person_access` record is written by this act), no change to the existing writer actions, no gateway release.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report. Never leave a deploy half-landed.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
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
Read, never write: `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`, `infra/aws/ec2/EC2_MANIFEST.json`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-7"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd7a.AC1.sh; echo "exit=$?"</invocation><expect>(?s)entry files at HEAD=\d+; closed=yes; sentinel=no; listed OPEN/HELD=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pd-7"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd7a.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sha_got=\S+ sha_want=\S+;.*REFUSED NO-OWNER-HEADER.*tokens: True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_MCPORTAL.TO-MP-pd-7.person-access-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with: the census; the function code hash before and after; the two check outputs; the before and after answers of both
invokes; the rollback and its measured time; and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the PC round-2 issuance (decomposition v10). Gate G-REL7 (PD.6). The write half of FWD-21 is Andrew-only (C2).

**AMENDMENT A1 (the issuer's, 2026-10-16 ~16:0xZ; CTO msgs 35104/35110/35114, CLAUDE.md rule 34):** the order was staged to `0.7.0_AE_CloudOps~MQ`; CloudOps is now seated one lane per macro per box, so every new NFRA CloudOps order goes to `0.7.0_AE_CloudOps~NFRA1` and ~MQ retires.

**AMENDMENT A2 (the issuer's, 2026-10-20 ~19:4xZ; PRD v0.10 FWD-26 and FWD-29, decomposition v20 OGW1.5):** the order is re-scoped to Act A, the Lambda, and rewritten in place (the earlier two-act text is in git history before this commit). Act B, the gateway release, is STRUCK: the mount of `admin_people_access` is `OG-mp-1` in NFRA_OPLGTW's batch17 (`2.0.0_SA_COO~O`), and the people-access routes are not in the live release (`13917ef993` has no `app/admin_people_access.py`; its `app/access_state.py` does know `person_access`, so the writer built from it writes the record kind). The dashboard bundle rides that release with the mcportal pin. The Lambda source is the drained MP-zo-3 (writer code `f3774ac1df8`, drain `55b33623db1`), which adds the WIDENING confirm; AC1 and AC2 are new files (`pd7a.AC1.sh`, `pd7a.AC2.sh`) because the old pd7 checks read the retired `~MQ` folder and the gateway diff, both of which no longer apply. AC2 reads the deployed bytes (rule 22a: the zip's contents, not the filename). Act A is inert on its own: no route reaches `set_person_access` until the mount lands. The CTO's hold on PD named OG-cp-1 (now released) and Andrew's sitting; the Andrew-direct v0.10 text says "the grant-writer Lambda deployed from source through Terraform, carrying set_person_access" is this project's, so the hold's remaining content is the never-widen pair, which the order keeps. Gate limb that graded the modification: none expected (to-pipeline-gate grades a modified order only for `<placeholders>`, which stays NONE).

Checks dry-run at the base (2026-10-20 ~19:4xZ): `pd7a.AC1.sh` FAIL (entry files at HEAD=0), `pd7a.AC2.sh` FAIL (close report absent); the AC2 steps run against the live function with the close-report read bypassed read: sha `894RI63/G4h019yxAGP7E+wQzrpZIfJoMaLhzpTTyck=`, no-header `set_person_access` REFUSED NO-OWNER-HEADER, deployed bytes hold both widening tokens: False. One check defect found and fixed in the dry run: `list-functions --query "...|[0]"` prints one "None" per page (the old pd7 AC2 had it); the name is now picked with grep. GO issued 2026-10-20 ~19:5xZ (`deliverables/2.0.0_SA_COO~MP/pd/GO_MP-pd-7.md`); the lane `0.7.0_AE_CloudOps~NFRA1` has no folder or run yet, so MSTR~Z is asked to seat it before the order is sent.

**AMENDMENT A3 (the issuer's, 2026-10-20 ~20:3xZ), after the lane's report:** the two `<expect>` strings were prose, so proof-of-spec-check marked the lane's instance INVALID; they are now regexes (the lane's suggestion, `(?s)` prefixed) matching the checks' real output. The issuer's defect, not the lane's. The lane regenerates the instance. Gate limb that graded the modification: none expected (to-pipeline-gate grades a modified order only for `<placeholders>`, NONE). The act itself: closed 2026-10-20T20:23:42Z by the lane (plan 0/1/0, apply 237.4 s, CodeSha256 894RI63... -> RUGwtI9t8UKV8VpyCeArffZFwHeuUm4QhOIJU+nAJjg=); the issuer re-ran `pd7a.AC1.sh` and `pd7a.AC2.sh` itself at ~20:3xZ and both read PASS.

<status>pending -- GO issued 2026-10-20; the lane closed the act 20:23:42Z (issuer re-ran AC1 and AC2: PASS); the order flips to complete when the lane's instance reads VALID</status>
<round>2</round>
<workstream>PC</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
