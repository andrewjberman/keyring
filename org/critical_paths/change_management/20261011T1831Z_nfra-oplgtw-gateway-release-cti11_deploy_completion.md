# Deploy Completion Record
**Date opened:** 2026-10-11T18:31:58.905198+00:00
**Status:** OPEN
**Deploy:** OG-ap-7 B2: the NFRA_CTLPLN CT-i-11 /hx/teams/* channel-read release deployed on live c3af8687e4
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the re-cut exists at release_sha with BOTH never-widen halves signed at it | release_sha 28ba9532b648061cecafe426836d3e96af4529cd on rel-nfra-oplgtw-cti11; COO half bd6be1a027, CTO half 4f49f40bd0; laptop consent de13ed0e00 + Addendum 1 4f285abe22 |  | OPEN |
| L2 | activation | safe-ec2-deploy.sh run FROM the release worktree with DEPLOY_BASE_REF=c3af8687e44a1e641259b37f992033ae02cdce3d and no HALT_OVERRIDE | the deploy returns rc=0 and the service restarts |  | OPEN |
| L3 | verify | ap7_verify.py after, run IMMEDIATELY against the before-state read at the act | all PASS: /health 200 and active; shipped md5 = the RELEASE list; tool list UNCHANGED; .env names UNCHANGED; every .env digest unchanged; routes +3 exactly the three named and none removed; dashboard unchanged |  | OPEN |
| L4 | verify | the SERVED grade (ruling term 3): GET /hx/teams/teams answers 200 where it answered 404 | AP7_SERVED.json with status_before, status_after, method and the ssm_command_id or log_ref. COO condition B: a 403 or 409 here is a FINDING and an ARMED row, never a rollback trigger |  | OPEN |
| L5 | git | the record clauses: runbook 7.2 moved to the new live ref, and EC2_MANIFEST deployed_commit plus file_checksums from the RELEASE blobs | the commit carrying both edits |  | OPEN |
| L6 | verify | ap7.AC2 | entries at HEAD, CLOSED=yes, sentinel gone, manifest equal, and the served 200 -- RESULT PASS at rc=0 |  | OPEN |

## Log

- 20261011T183158Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)
