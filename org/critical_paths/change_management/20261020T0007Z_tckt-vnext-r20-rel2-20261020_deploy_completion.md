# Deploy Completion Record
**Date opened:** 2026-10-20T00:07:16.640984+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T002527Z
**Deploy:** TCKT_VNEXT TO-R20-REL2 (AMENDMENT 1, GO msg 11113; CTO half signed msg 11111): opal-ticket-api CODE-ONLY release so the package route admits pdf_ref and commentary_ref null together (IRPT_ANLREQ v0.24 FWD-1); built_from_sha 48551f02ac, source blob 085183c76e; diff vs live exactly 11 added 0 removed; ONE in-place update of the function code; pair 2d758b87a9 / 772c800268, check a98078c896
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | pair blobs, source blob, live CodeSha256 baseline, census of every worktree, fire windows asked (CTO, IB2, Y2), env_before printed | all true and printed | pair 2d758b87a9 / CTO half 772c800268 / check a98078c896 measured EQUAL (hash-object); source blob at 48551f02ac = 085183c76e5d33f40b1b3a42e7d8f9f1718b4765 EQUAL; live CodeSha256 iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= = baseline (Active, Successful, LastModified 2026-10-19T18:23:34Z); env_before saved whole (14 keys) deliverables/r20_rel2/env_before.json; census 46 worktrees read: shared tree holds only this ledger, 9 stale-snapshot hits in other worktrees are all absent at HEAD (closed: prod2, prod3, r18-run-meeting, irpt-ycg-r33, irpt-fwd1-run); no PROD promote in flight (gh run list in_progress empty; newest Deploy to Production run 39317468736 success 20:15:56Z; PROD head facddeb687b8); fire windows: CTO none until 02:30Z (msg 11120); IB2 no reply by 00:18Z (its E2E-4 ledger CLOSED per the CTO); Y2 message 11117 unread (OFFER-EXHAUSTED) at 00:18Z: silence read as none per the convention of the earlier orders, DISCLOSED to the COO; 00:18Z is outside 11:30Z-14:15Z and 06:00Z-06:45Z Tue | CLOSED 20261020T001904Z |
| B1 | verify | zip built from built_from_sha, member list and sha256 printed, diffed against the live member | exactly 11 added and 0 removed lines in three hunks inside package_ticket | built at 48551f02ac in the detached worktree C:/dev/tv2-rel-r1819 with BUILD_ONLY=1 build-and-upload.sh ticket-center opal-ticket-api (import-closure OK, 1 member lambda_function.py 135537 bytes, zip 40638 bytes, sha256 b64 LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0= hex 2ee24edf0143a10f6b84ae255d9a6e6c780d06526a3d5344ad583331078f4c8d); built member git blob 085183c76e5d33f40b1b3a42e7d8f9f1718b4765 equals the pair's source blob; live package iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= 40379 bytes, one member lambda_function.py 134698 bytes; diff of built member vs live member (line endings normalized): 3 hunks, 11 added, 0 removed, equals the pair's section 1 | CLOSED 20261020T001452Z |
| U1 | activation | live package saved (copy named by sha) and the new package uploaded to the artifact object | round trip equal, previous S3 VersionId recorded | live package saved: rollback copy C:/dev/tv2-rel-r20-out/rel2/rollback_live_iRxJZYp6.zip equals the previous S3 version bytes (sha256 iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM=, 40379 bytes), previous S3 VersionId 9Y9nFwn0vtsQw3mIqVHRzHKyoJGWa5bK (record deliverables/r20_rel2/rollback_s3_version.json); new package uploaded 00:19Z as VersionId efzUHPSp1bg2_tqpHPy7xQpsJYTuEHnd, metadata content-sha256 LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0=, 40638 bytes, round trip equal, current version | CLOSED 20261020T002015Z |
| A1 | activation | terraform plan -out shows ONE in-place update (the code), then safe-apply of the planfile | Apply complete 0 add 1 change 0 destroy; Active/Successful | terraform plan -out: 0 add 1 change 0 destroy, only module.opal_ticket_api.aws_lambda_function.this in-place (s3_object_version 9Y9nFwn0... -> efzUHPSp1bg2_tqpHPy7xQpsJYTuEHnd, source_code_hash iRxJZYp6... -> LuJO3wFD..., last_modified computed) = the pair's section 3; safe-apply of the planfile rc=0, Apply complete 0 added 1 changed 0 destroyed, 00:22Z; function Active/Successful LastModified 2026-10-20T00:22:47Z CodeSha256 LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0=; environment equal before and after (14 keys), no other configuration attribute changed; post-apply terraform plan: No changes | CLOSED 20261020T002527Z |
| V1 | verify | r20_rel2_check.py with its self-test printed beside the verdict; post-apply plan No changes | REL2-OK | r20_rel2_check.py (blob a98078c896) -> REL2-OK code_sha256=LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0= null_pair=present fence=present env=unchanged members=1 ; self-test -> R20-REL2-SELFTEST-OK ; post-apply plan No changes | CLOSED 20261020T002527Z |

## Log

- 20261020T000716Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
- 20261020T001452Z LEG B1 closed: built at 48551f02ac in the detached worktree C:/dev/tv2-rel-r1819 with BUILD_ONLY=1 build-and-upload.sh ticket-center op
- 20261020T001904Z LEG S1 closed: pair 2d758b87a9 / CTO half 772c800268 / check a98078c896 measured EQUAL (hash-object); source blob at 48551f02ac = 08518
- 20261020T002015Z LEG U1 closed: live package saved: rollback copy C:/dev/tv2-rel-r20-out/rel2/rollback_live_iRxJZYp6.zip equals the previous S3 version 
- 20261020T002527Z LEG A1 closed: terraform plan -out: 0 add 1 change 0 destroy, only module.opal_ticket_api.aws_lambda_function.this in-place (s3_object_
- 20261020T002527Z LEG V1 closed: r20_rel2_check.py (blob a98078c896) -> REL2-OK code_sha256=LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0= null_pair=presen
- 20261020T002527Z CLOSED -- all 5 legs proven
