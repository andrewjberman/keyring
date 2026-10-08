# Deploy Completion Record
**Date opened:** 2026-10-08T18:13:20.373801+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN F1 svc principal: resident st24 -> st25 (allow list adds svc-irpt-analysis), one seat-driven F1 run, then the removal release st25 -> st24
**Authored by:** 2.0.0_SA_COO~G2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | verify | st25 tar + install script staged in S3, read back by version | sha256 equal | tar irpt-resident-3cf5d52a7b-st25.tar.gz v Hwc58HnvsK34Ik4nWiLfUTPk4wj_blNO sha256 57e70cc96970f6c8...; install script v lrMO.Fq4usTTy.vsB67UKPvE4MU.Tlos sha256 86fe9deee41cbf88...; both keys 404 before, read back by version equal (staged ~18:1xZ before the ledger opened, as st24 did); gate PASS G1 267/267 G2 265/265 + added 1/1 G3 111/111 G4 0 unserved G5 vs st24 changed 2 (resident_worker.py, resident_bindings.json) identical 265 | CLOSED 20261008T181334Z |
| P1 | verify | host pre-read (root st24, allow list, queue 0/0) | recorded | SSM fbce151c 20:53:54Z rc 0: active root 409e3066d1-st24 restarts 0; allow list andrew only; worker sha256 9317219a (st24); st24 root present, st25 absent; library 857d90b8 + wrapper 55ddb8f7 equal the st25 pins; pydeps pyarrow + drop-in present; queue 0/0; journal 60s polls 3 tracebacks 0 (f1_svc_release/P1_PRE_READ_20261008.txt) | CLOSED 20261008T205410Z |
| D2 | activation | install_st25.sh via SSM | root 3cf5d52a7b-st25 active, rc=0 | SSM 959fadc3 20:55:02-20:55:46Z rc 0 (attempt 1 SSM 56fe806f refused at fetch, exit 30, nothing moved: host role lacks s3:GetObjectVersion; wrapper re-pointed to fetch by key, sha256 86fe9dee binds the bytes): script sha verified on host; SHA256SUMS 267 OK; factory OK enrolled 1276035; queue 0/0; install rc 0; active, NRestarts 0, MainPID 746083, root 3cf5d52a7b-st25, polls 2/30s tracebacks 0 | CLOSED 20261008T205606Z |
| V1 | verify | running allow list carries svc; producer_for svc=OPAL; queue 0/0; no traceback | read from the running root | same SSM 959fadc3: running root 3cf5d52a7b-st25; allow list (andrew, svc-irpt-analysis); worker sha256 c0bbea55 = built; pyarrow + drop-in present; producer_for svc=OPAL andrew=OPAL other=YCHARTS; proof exit 0; queue 0/0; journal 60s polls 3 tracebacks 0 (f1_svc_release/D2_V1_INSTALL_20261008.txt). Window: D2 start 20:55:02Z | CLOSED 20261008T205606Z |
| F1 | verify | one seat-driven F1 run as svc-irpt-analysis through the portal route (ruling d54e0b7515) | run record, zero YCharts calls measured | RAN 21:10:18-21:10:32Z as svc through CloudFront (F1_RUN_RECORD_20261008.json): login 200, upload NORMALIZED, submit QUEUED REQ-8966d24ffefa1c28269ef26c; resident took it 21:10:31Z on the OPAL path and refused: retained_for_retry class=LayoutRefused (brand asset absent on host) -> FINDING row IRPT_YCDGEN-D2-S3, FWD-1 NOT realized; YCharts markers in window 0 of 40 journal lines; first secret read reported (MSTR) | CLOSED 20261008T212529Z |
| X1 | activation | remove_st25_to_st24.sh via SSM (the removal release) | root 409e3066d1-st24 active, rc=0 |  | OPEN |
| V2 | verify | running allow list is andrew only; queue 0/0; no traceback | read from the running root |  | OPEN |

## Log

- 20261008T181320Z OPENED by 2.0.0_SA_COO~G2 with 7 leg(s)
- 20261008T181334Z LEG U2 closed: tar irpt-resident-3cf5d52a7b-st25.tar.gz v Hwc58HnvsK34Ik4nWiLfUTPk4wj_blNO sha256 57e70cc96970f6c8...; install script v
- 20261008T205410Z LEG P1 closed: SSM fbce151c 20:53:54Z rc 0: active root 409e3066d1-st24 restarts 0; allow list andrew only; worker sha256 9317219a (st2
- 20261008T205606Z LEG D2 closed: SSM 959fadc3 20:55:02-20:55:46Z rc 0 (attempt 1 SSM 56fe806f refused at fetch, exit 30, nothing moved: host role lacks s
- 20261008T205606Z LEG V1 closed: same SSM 959fadc3: running root 3cf5d52a7b-st25; allow list (andrew, svc-irpt-analysis); worker sha256 c0bbea55 = built;
- 20261008T212529Z LEG F1 closed: RAN 21:10:18-21:10:32Z as svc through CloudFront (F1_RUN_RECORD_20261008.json): login 200, upload NORMALIZED, submit QUE
- 20261008T2130Z NOTE secret window: retry ADD put 21:04:07Z (laptop 107315, set-compare rule 107308); one read by dell2 at ~21:10:18Z inside f1_svc_run.py (reported to MSTR, rule 2); REMOVE put 21:27:47Z, verified by simulation: dell2 explicitDeny, dell1 explicitDeny, Andrew_Berman allowed (laptop 107345, MSTR 1678). Condition (1) met before X1 closes.
