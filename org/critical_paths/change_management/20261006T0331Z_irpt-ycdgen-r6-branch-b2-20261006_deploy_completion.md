# Deploy Completion Record
**Date opened:** 2026-10-06T03:31:09.409523+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T135020Z
**Deploy:** IRPT_YCDGEN round 6 branch B2: resident package 409e3066d1-st24 (st22 plus the 11 named files, the Overview map, the classifier client member and the pinned pyarrow), Andrew's sign-in on the Opal allow list; CTO half pending, COO half in the packet
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | irpt-resident-409e3066d1-st24.tar.gz, resident_host_install_409e3066d1-st24.sh and the pinned pyarrow tar staged in S3 | read back by version, sha256 equal | all three keys 404 before (the B2 tar and script) and absent (the pyarrow tar under resident/deps/); B2 tar irpt-resident-409e3066d1-st24.tar.gz version nmBP0Y17T7x.kglMG7.y9gW_ZBZX7GZ2 (871424 bytes) sha256 91d23ab3367bed1cc3dbb7f5cba0ac51dfec0816f6a2a6679341ed5596b51a04; install script resident_host_install_409e3066d1-st24.sh version UT9UcMwONgu2fQhH.SSD3fpGfzupizJ_ (8717 bytes) sha256 c9ad01d7f1a15108e7b59424b30cc845651af55269f4aa78153bf21b3782e9b0; pyarrow tar deps/pyarrow-18.1.0-cp312-awssdkpandas16.tar.gz version 4oc.2naPXytcEzYL7K5zyMB5ShhhJaCr (17751495 bytes) sha256 dad8a09e088722e1fc4b506b921583a3d62b7097a7eacf0907bce6f284393506, built from the estate's own AWSSDKPandas-Python312:16 layer (zip sha256 4ea9482ddb6d...); staged BEFORE the ledger was opened (S3 only; no host change); gate G1 267/267, G2 265/265 + added 1/1, G5 added 11 removed 0 changed 3 | CLOSED 20261006T033109Z |
| R1 | verify | retention module of the B2 tar vs the running st22 module over the live v1 rows, read-only | 0 differences | 721 of 721 rows, 0 verdict differences, 0 refusals; org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/ (re-recorded by 2.0.0_SA_COO~G2 from the ledger at HEAD; originally closed 20261006T034427Z by 2.0.0_SA_COO~Y, commit e2fec30ce2; the .open_deploys JSON on dell2 never carried that close) | CLOSED 20261007T102038Z |
| P1 | verify | pre-install step-2 answers | recorded | pre-install answers recorded; equal to branch B pre; org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6 (re-recorded by 2.0.0_SA_COO~G2 from the ledger at HEAD; originally closed 20261006T034427Z by 2.0.0_SA_COO~Y, commit e2fec30ce2; the .open_deploys JSON on dell2 never carried that close) | CLOSED 20261007T102038Z |
| D2 | activation | install_branch_b2.sh via SSM | root 409e3066d1-st24 active; pyarrow in the root; members equal | root 409e3066d1-st24 active, rc=0, 14 members OK, pyarrow in root, MainPID 622977 NRestarts 0; org/missions/D9/IRPT/IRPT (re-recorded by 2.0.0_SA_COO~G2 from the ledger at HEAD; originally closed 20261006T034427Z by 2.0.0_SA_COO~Y, commit e2fec30ce2; the .open_deploys JSON on dell2 never carried that close) | CLOSED 20261007T102039Z |
| V1 | verify | post-install step-2 equal; real classifier and characteristics reads from the running root, exit code 0 | equal or rolled back | step-2 answers equal pre (only root name differs); real classifier SPY and characteristics 3 of 3 from running root, exi (re-recorded by 2.0.0_SA_COO~G2 from the ledger at HEAD; originally closed 20261006T034428Z by 2.0.0_SA_COO~Y, commit e2fec30ce2; the .open_deploys JSON on dell2 never carried that close) | CLOSED 20261007T102039Z |
| F1 | verify | Andrew's first real Overview | opened by Andrew | SUPERSEDED per 1.0.0_SA_CTO~DELL2 ruling msg 1260 (NEVER-2 measure, no re-execute): the deploy is world-done -- D2 and V1 closed; host root 409e3066d1-st24 last measured by laptop SSM 4119ed28 (DELL2_READS_SECOND_BATCH_20261007.md @8b83fd1d6f); no resident install since (2.0.0_SA_COO~G2 is the host's one writer; 390 s release ad4ae786d9 never applied); trunk constant equal (M1, diff 0). Andrew's first real Overview is the OUTCOME FWD-1, graded by round 6 on the run card F1_RUN_CARD_20261007.md (retry opened msg 1278), not by this deploy entry. | CLOSED 20261008T135017Z |
| M1 | git | the allow-list constant lands on CLOUD after F1 | commit | commit 035443efaa (cherry-pick of 409e3066d1), drained to CLOUD @73e23d9f5e; git diff 409e3066d1 HEAD -- ycharts/generate/resident_worker.py = 0 lines (trunk constant == running root, OPAL_PRODUCER_PRINCIPALS = andrew@opalinvest.com); host root 409e3066d1-st24 read SSM 4119ed28 (DELL2_READS_SECOND_BATCH_20261007.md @8b83fd1d6f); CTO~DELL2 msg 306; code only, no deploy | CLOSED 20261007T101933Z |

## Log

- 20261006T033109Z OPENED by 2.0.0_SA_COO~Y with 7 leg(s)
- 20261006T033109Z LEG U2 closed: all three keys 404 before (the B2 tar and script) and absent (the pyarrow tar under resident/deps/); B2 tar irpt-residen
- 20261006T034427Z LEG R1 closed: 721 of 721 rows, 0 verdict differences, 0 refusals; org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/
- 20261006T034427Z LEG P1 closed: pre-install answers recorded; equal to branch B pre; org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6
- 20261006T034427Z LEG D2 closed: root 409e3066d1-st24 active, rc=0, 14 members OK, pyarrow in root, MainPID 622977 NRestarts 0; org/missions/D9/IRPT/IRPT
- 20261006T034428Z LEG V1 closed: step-2 answers equal pre (only root name differs); real classifier SPY and characteristics 3 of 3 from running root, exi
- 20261007T101933Z LEG M1 closed: commit 035443efaa (cherry-pick of 409e3066d1), drained to CLOUD @73e23d9f5e; git diff 409e3066d1 HEAD -- ycharts/generat
- 20261007T102038Z LEG R1 closed: 721 of 721 rows, 0 verdict differences, 0 refusals; org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/
- 20261007T102038Z LEG P1 closed: pre-install answers recorded; equal to branch B pre; org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6
- 20261007T102039Z LEG D2 closed: root 409e3066d1-st24 active, rc=0, 14 members OK, pyarrow in root, MainPID 622977 NRestarts 0; org/missions/D9/IRPT/IRPT
- 20261007T102039Z LEG V1 closed: step-2 answers equal pre (only root name differs); real classifier SPY and characteristics 3 of 3 from running root, exi
- 20261008T135017Z LEG F1 closed: SUPERSEDED per 1.0.0_SA_CTO~DELL2 ruling msg 1260 (NEVER-2 measure, no re-execute): the deploy is world-done -- D2 and V
- 20261008T135020Z CLOSED -- all 7 legs proven
