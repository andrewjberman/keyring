# Deploy Completion Record
**Date opened:** 2026-10-21T01:18:55.535644+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T014052Z
**Deploy:** TCKT_VNEXT TO-R22-DL1 AMENDMENT 6 (GO msg 11702; CTO ruling 11699): the 42 opal-data-irpt synthetic S3 object VERSIONS only, by exact bucket/key/VersionId through 4 throwaway Terraform IAM roles (opal-ticket-residue-delete-0..3-role, s3:DeleteObjectVersion only, 900 s sessions); the FIRST entry is deleted and read ABSENT before any other; roles destroyed by a -target plan of exactly the 8 resources and read ABSENT; pair ff354d5036, CTO half 28135590a9, manifest 2e8786cc42 (42 entries), check 9b192b70ef
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | four blobs measured; irpt bucket policy printed; census; overlap asks | all printed | AMENDMENT 6 (V2 11702; CTO ruling 11699) and release 11717 (CTO condition: IB2 reports run 7f). Blobs measured: pair ff354d5036ec, CTO half 28135590a958, manifest 2e8786cc4219 (42 entries, all opal-data-irpt), check 9b192b70efd6 (selftest OK); built_from_sha 773a895c2c is a commit. irpt bucket policy printed: ONE statement DenyInsecureTransport (Deny s3:* when SecureTransport false), no other Deny. IB2's ledger irpt-commentary-e2e-7f-20261021 read CLOSED 20261021T011844Z (file read); IB2 11712 7F terminal 01:16:32Z, no run/IAM apply/promote in flight or due. Y2 11716 (01:22Z) said 7F in flight: stale, contradicted by the closed ledger. CTO 11709 7F in flight at 01:20Z, then V2 relayed the release 11717. Holds asked of G2/Y2/IB2 (11719-11721): no Multi-Comp, audit-policy or irpt-writing run until my terminal. Watcher fixed. HCL = pair section 2 (blob d8203ad0de) committed b0df95d0e9, naming gate PASS 8 graded | CLOSED 20261021T012653Z |
| P1 | verify | 42 entries PRESENT at version, one version, no marker, no lock/hold/retention; Deny read; plan 8 add only; naming gate | all true | 01:20Z scan (r22_precond_readonly.py): 42/42 PRESENT at version, one version and no delete marker per key, no ObjectLockMode, no legal hold, no retention; irpt has no object-lock configuration. Deny DenyS3DeletesOnProductionData v7 intact (read 01:05Z, re-read before the check). Roles opal-ticket-residue-delete-0..3-role absent before apply (destroyed 01:03Z). Plan with var.residue_manifest_path (manifest blob 2e8786cc42): 8 to add, 0 to change, 0 to destroy (4 roles, 4 policies). PROD head 234cddba2d83 (CI run 39458711957 success 16:37Z), no promote in flight. | CLOSED 20261021T012653Z |
| A1 | activation | safe-apply of 4 roles and 4 policies | apply complete 8 added | safe-apply of the saved plan (8 to add) 01:27:21Z; Apply complete 8 added, 0 changed, 0 destroyed 01:28:27Z; roles opal-ticket-residue-delete-0..3-role CreateDate 01:28:26Z; HCL commit b0df95d0e9 (pair section 2 verbatim, blob d8203ad0de) | CLOSED 20261021T014050Z |
| X1 | activation | first entry deleted and read ABSENT, then the rest; each 204 and ABSENT by 404 only | 42 of 42 | 42 of 42 exact versions deleted 01:29:04Z-01:29:11Z, each s3:DeleteObject with VersionId returned 204, each read ABSENT (head-object --version-id 404 only) and its key listed no version or marker. FIRST entry tested first in role 0 (900 s): 204 and ABSENT before any other. Roles 0..3 assumed 900 s each, used only for their own chunk (12,12,12,6). Credentials never printed or written. Record deliverables/r22_delete/delete_pass_output_amendment6.txt and deleted.json. No cottonwood entry in this pass (4 stay as residue per the CTO ruling 11699). Nothing of Andrew's ticket TCK-20261020-b1d61f80 touched (present at 01:32Z) | CLOSED 20261021T014050Z |
| D1 | verify | targeted destroy of exactly 8 resources; roles ABSENT; Deny intact; control object PRESENT | all printed | plan -destroy with -target of exactly the eight resources: 0 to add, 0 to change, 8 to destroy (8 destroy lines, 0 naming any other resource; the whole-root destroy was not planned this time); safe-apply 01:30:48Z-01:31:54Z; opal-ticket-residue-delete-0..3-role each read ABSENT (NoSuchEntity); Deny DenyS3DeletesOnProductionData in cloudops-dell-agent-deploy-policy default version intact (DeleteObject*); control object PRESENT (a non-manifest 7F residue key in opal-data-irpt); post-destroy plan of the root = 8 to add only (no drift); protected tickets TCK-20261017-da2a1987 and -5af976ff present | CLOSED 20261021T014051Z |
| V1 | verify | r22_residue_delete_check.py with self-test | RUN-OK (residuedelete) | r22_residue_delete_check.py (blob 9b192b70ef): R22-RESIDUEDELETE-SELFTEST-OK beside RUN-OK (residuedelete) 42 exact versions ABSENT with no marker left; the throwaway roles ABSENT; the Deny still in the deploy policy; the control object PRESENT (01:33Z) | CLOSED 20261021T014052Z |

## Log

- 20261021T011855Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261021T012653Z LEG S1 closed: AMENDMENT 6 (V2 11702; CTO ruling 11699) and release 11717 (CTO condition: IB2 reports run 7f). Blobs measured: pair ff3
- 20261021T012653Z LEG P1 closed: 01:20Z scan (r22_precond_readonly.py): 42/42 PRESENT at version, one version and no delete marker per key, no ObjectLock
- 20261021T014050Z LEG A1 closed: safe-apply of the saved plan (8 to add) 01:27:21Z; Apply complete 8 added, 0 changed, 0 destroyed 01:28:27Z; roles opal-
- 20261021T014050Z LEG X1 closed: 42 of 42 exact versions deleted 01:29:04Z-01:29:11Z, each s3:DeleteObject with VersionId returned 204, each read ABSENT 
- 20261021T014051Z LEG D1 closed: plan -destroy with -target of exactly the eight resources: 0 to add, 0 to change, 8 to destroy (8 destroy lines, 0 namin
- 20261021T014052Z LEG V1 closed: r22_residue_delete_check.py (blob 9b192b70ef): R22-RESIDUEDELETE-SELFTEST-OK beside RUN-OK (residuedelete) 42 exact vers
- 20261021T014052Z CLOSED -- all 6 legs proven
