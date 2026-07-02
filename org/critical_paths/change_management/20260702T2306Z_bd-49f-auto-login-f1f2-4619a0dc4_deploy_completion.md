# Deploy Completion Record
**Date opened:** 2026-07-02T23:06:01.664327+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260702T231741Z
**Deploy:** Deploy F1+F2 auth-chain hardening (0.6.0 commit 4619a0dc4) to i-0fa1846f -- F1 kimiVision request-timeout + F2 smPut rc=1-on-persist-fail. Supersedes 5d9cc4649 (guard+F1+F2). Proves on 00:00Z main mint
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | push 4619a0dc4 bd_49f_auto_login.js to ec2/bd-49f-auto-login/ | aws s3 cp done, md5 e215b90f | aws s3 cp bd_49f_auto_login.js (4619a0dc4) -> ec2/bd-49f-auto-login/ complete; deploy artifact md5 e215b90f5cfc9c0b7b186e30ee92d371 | CLOSED 20260702T230752Z |
| L2 | ec2-baked-asset | SSM-pull onto /opt/bd-49f-auto-login + on-box md5 | md5 == e215b90f5cfc9c0b7b186e30ee92d371 | SSM f6b11afe Success; on-box md5 /opt/bd-49f-auto-login/bd_49f_auto_login.js = e215b90f5cfc9c0b7b186e30ee92d371 == deploy artifact | CLOSED 20260702T231305Z |
| L3 | verify | on-box Rule-22a exercise (F2 smPut-throw->rc=1, F1 hung-socket rejects on box node) | f1f2_exercise ALL PASS on box | SSM 89df3690 Success rc=0; on-box node exercise: F2 smPut-throw->rc=1 (old->rc=0 bug reproduced), F1 hung-socket rejected 1013ms, ALL EXERCISE TESTS PASS | CLOSED 20260702T231307Z |
| L4 | activation | EC2_MANIFEST deployed_commit=4619a0dc4 | manifest updated + committed | EC2_MANIFEST deployed_commit=4619a0dc4 + md5 e215b90f + deployed_at 23:07Z committed (e06641544) | CLOSED 20260702T231737Z |

## Log

- 20260702T230601Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20260702T230752Z LEG L1 closed: aws s3 cp bd_49f_auto_login.js (4619a0dc4) -> ec2/bd-49f-auto-login/ complete; deploy artifact md5 e215b90f5cfc9c0b7b186
- 20260702T231305Z LEG L2 closed: SSM f6b11afe Success; on-box md5 /opt/bd-49f-auto-login/bd_49f_auto_login.js = e215b90f5cfc9c0b7b186e30ee92d371 == deplo
- 20260702T231307Z LEG L3 closed: SSM 89df3690 Success rc=0; on-box node exercise: F2 smPut-throw->rc=1 (old->rc=0 bug reproduced), F1 hung-socket rejecte
- 20260702T231737Z LEG L4 closed: EC2_MANIFEST deployed_commit=4619a0dc4 + md5 e215b90f + deployed_at 23:07Z committed (e06641544)
- 20260702T231741Z CLOSED -- all 4 legs proven
