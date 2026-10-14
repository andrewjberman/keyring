# NFRA_MCPORTAL task order -- `MP-n-4` -- WORKSTREAM C17 ROUND 2: the gateway release -- the pointer reader goes live

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-n-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-n-4</to_id>
<issued_to>0.7.0_AE_CloudOps~MQ</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a release; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the pointer sits under the gateway's existing read prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's no-identity arm is the adversary.
EGRESS CLASS, declared: S3 artifact upload + SSM pull and restart of opal-gateway on i-07dccb1615503ac99, by safe-ec2-deploy.
</preflight>

## 1. THE CELL -- `MP-n-4` (workstream C17 round 2, decomposition sections C17R2.1, C17R2.3 and C17R2.4)

**Do not start before the issuer's GO message.** That GO names the gateway commit to ship. It comes when G-REL4 holds:
MP-n-2 is drained; the gateway queue is free (NFRA_MCPORTAL's own MP-z-5 GW release has landed, and no NFRA_OPLGTW
release held by `2.0.0_SA_COO~O` is in flight); the never-widen pair is signed against YOUR release ASK (step 2).

Work in a linked worktree you cut from `box/sitez` HEAD, using a NO-CONE pattern list if sparse (rows NFRA_MCPORTAL-Z-W5-S2,
Z-S43).

The gateway runs `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` (MP-z-5's release by the time
this order starts). Read it at the act; never assume it. Build the release on THAT live base with ONLY the GO's gateway
commit: `app/admin_fabric_gitstate.py` and `tests/test_admin_fabric_gitstate.py` (MP-n-2). There is no route change and no
bundle change; keep `mcportal_commit` as the live manifest records it.

In order:
1. **The release tree.** `git worktree add -b rel-nfra-mcportal-c17r2 <path> <live deployed_commit>`; cherry-pick the GO's
   commit. **Census:** `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY those two files; anything
   else STOPS with a BLOCKING row. Run `tests/test_admin_fabric_gitstate.py tests/test_admin_fabric.py` on `box/sitez`
   HEAD with the payload: 0 failed. Then run the same two files on the release tree. There, a test may fail ONLY if its
   failure is `FileNotFoundError` on a repo path outside `infra/aws/ec2/opal-gateway/` whose `git ls-tree` reads 0 at the
   live base AND 1 at `box/sitez` HEAD, and that same test passes at HEAD. A release tree's `org/` is frozen at the
   release chain's vintage (row Z-S45; at 64b3e54658, `cp2/fixtures/` lists 0 files). List each such test id with its
   path and both ls-tree counts in the ASK. Any other failure STOPS with a BLOCKING row.
2. **The ASK and the pair.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NEVER_WIDEN_ASK_MP-n-4.md`:
   the blast radius (the one module and its test; the refusal field's basis changes and boxes with no pointer read "not
   recorded"); what it may never touch (the MCP tool surface, any IAM, any store write, the producer); the census; the
   rollback (step 3); the read-backs (AC1, AC2). Commit it and send ONE message, to BOTH `1.0.0_SA_CTO~Z` and
   `2.0.0_SA_COO~MP`, naming the ASK path and commit, asking each for its half. WAIT for both halves at HEAD of
   `box/sitez` (`deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-n-4_<date>.md`,
   `deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-n-4_<date>.md`), each citing your ASK by path. A refused half STOPS
   the act.
3. **Rollback, proven before the act.** Rebuild the live base's artifact from a clean tree WITHOUT uploading, and name the
   command that would re-deploy it. If it cannot be shown: STOP, no deploy, a BLOCKING row.
4. **NEVER-2 ledger, on your branch, in this order.** `python .tools/deploy_ledger.py open ...` with slug
   `nfra-mcportal-c17r2-release`; legs: release build and upload, SSM pull and restart, manifest record. Write the census,
   the test counts and the rollback to `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-n-4_PRE_ACT_RECORD.md`
   with ONE pointer line in the entry. Commit the entry AND its sentinel
   `org/critical_paths/.open_deploys/nfra-mcportal-c17r2-release.json`. ACT from the release tree with ITS scripts:
   `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Poll `/health` after
   the restart; not 200 within 90 s -> the named rollback AT ONCE, close as rolled back, stop. Record the release in
   `EC2_MANIFEST.json` on your branch (`deployed_commit`, `previous_deployed_commit`, `release_note`). Close every leg with
   its proof and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No IAM, no Terraform, no store write, no producer change.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/*nfra-mcportal-c17r2-release*
org/critical_paths/.open_deploys/nfra-mcportal-c17r2-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, the GO's gateway
files, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/`, `.../c17/checks/_n1_probe.py`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`. Append a row as ONE whole fenced ```json block.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-n-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/n4.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel=no; listed OPEN/HELD=0; descends=yes; outside the C17R2 set=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-n-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17r2/checks/n4.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; no-identity gitstate=401 or 403; gitstate_s<=5 with body_fetches printed and recorded>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NFRA_MCPORTAL.TO-MP-n-4.c17r2-gateway-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with: the census; the two check outputs; the cold read's time and fetch count; the
ledger entry path and its CLOSED state; every commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the C17 round-2 issuance (decomposition v8). Checks dry-run at the base: AC1 FAIL (no entry;
the narrow limb alone reads clean because round 1's live span is the same two files -- the slug is the discriminator);
AC2 FAIL (SSM 90c9dbfe: /health 200 control, no-identity 401, gitstate_s=9.7 body_fetches=1336 recorded=4 against the
5 s bar). Gate G-REL4, holder the issuer. Same project as MP-z-4/z-5, so the seating rule admits ~MQ.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~MP, 2026-10-13 ~22:4xZ):** step 1's "0 failed" is graded at box/sitez HEAD. On the release tree, a failure is admitted only by mechanism: a FileNotFoundError on a repo path absent at the live base and present at HEAD, with the test passing at HEAD. This is the MP-z-5 ruling (row Z-S45; both never-widen halves of MP-z-5 used the same closed-set form), applied before the GO and measured at the act, so the issuer does not predict the ids. Gate limb: to-pipeline-gate GATE (viii).

<status>complete -- flipped by the issuer 2.0.0_SA_COO~MP, 2026-10-14 ~01:4xZ. opal-gateway LIVE at b0c75d24f11808d1de4f70fcca5d39216282054a (previous 7eff14b2e6, mcportal 0e02a1f unchanged). AC1 PASS, AC2 PASS: cold gitstate _compute 1.3 s / 136 fetches, recorded=4, against the 5 s bar (base 9.7 s / 1,336). Instance VALID. Ledger nfra-mcportal-c17r2-release CLOSED, 3 of 3 legs, landed on box/sitez by this commit. Condition B-1: 4 of 4 boxes read not recorded before and after. Report: deliverables/0.7.0_AE_CloudOps~MQ/MP-n-4_CLOSE_REPORT.md @7dfa13b601 (msg 33894). The payload on the trunk equals the release, 2 of 2 files. Was: pending.</status>
<round>2</round>
<workstream>C17</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
