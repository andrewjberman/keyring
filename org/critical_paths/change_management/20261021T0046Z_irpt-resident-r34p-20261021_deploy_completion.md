# Deploy Completion Record
**Date opened:** 2026-10-21T00:46:05.994457+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T005509Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34P: resident release 34p (r34o minus the registry change) on the resident host: three S3 objects, pre-read, signed install, after-reads, V2 inside the service environment
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read as root: running root r34o, r34p root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS at 2026-10-21T00:46:57Z (SSM command 79c4e4c8-0683-4f31-8529-4f3fd525e776): running root r34o, restarts 0, r34p root absent, registry member at its r34o value, library and wrapper unmoved, queue 0 0; COO blob b945271a46 and CTO half naming it; three checker arms OK; stage hashes equal; open-deploys 52 worktrees 142 entries, 8 terminal entries name the resident, 0 non-terminal | CLOSED 20261021T004710Z |
| D1 | activation | upload the tar, the sums file and the host script, each read back by VersionId equal | three keys uploaded and read back equal | three keys read 404, uploaded and read back by VersionId equal: tar qXJvdeOXrw7ovNKWAcen3XRT41HIC1rI, sums sMIjjC9lxuWP2MEioN9K1nP10jj1Hz2x, script 5OFrUIMvFyuj.OLIHYa5bMrvl0edKd9E (D1_UPLOAD_OUT.txt) | CLOSED 20261021T004735Z |
| D2 | activation | signed install as root: r34p root installed, unit restarted, polled | install success line and running root r34p | install script rc=0 at 2026-10-21T00:49:50Z (SSM command 75c042f9-a099-4adc-ab75-dcc36a2fde1e, install_r34.sh sha256 4c3f7a94...): running root /opt/irpt-resident/0485393f3a-r34p active restarts 0; registry member MATCH 229eca2d; package sums 0 not OK of 322; queue 0 0; no sign-in | CLOSED 20261021T005313Z |
| V1 | verify | after-reads: sums, census, cure (policy hashes back to r34n), bindings, pool, imports, IRPT_TICKETS_TABLE word | V1 lines | V1 running root r34p active restarts 0; members 1 of 1 MATCH (registry 229eca2d); sums 0 not OK of 322; census package scope 3 changed 0 added 0 removed (SHA256SUMS, reporting_policies.json, resident_bindings.json); cure: anlreq 8edbe84b05765c36 dashbd 301c58e24ff0feda registry equals r34n; bindings pin 919bb891 files_from 47 opal_map pinned packager unchanged, 1 of 18 binding keys differs (provenance); pool pinned pricing estate yfinance ycharts budget 6 per 390 s; IRPT_TICKETS_TABLE unset in the unit and the process (control PATH= read 1); jsonschema yes; queue 0 0; no sign-in | CLOSED 20261021T005346Z |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command 905cc8a9-043a-45ad-b3e0-ef5906757ced, V2 script sha256 7817cf8c..., export V2S_WANT_ROOT=/opt/irpt-resident/0485393f3a-r34p, path conversion off); controls 4 of 4, backoff, door, pricing, budget, tier OK; transient unit rc=0; 2 Yahoo calls, no YCharts call | CLOSED 20261021T005439Z |

## Log

- 20261021T004605Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T004710Z LEG P1 closed: P1 STOP-READ-0 PASS at 2026-10-21T00:46:57Z (SSM command 79c4e4c8-0683-4f31-8529-4f3fd525e776): running root r34o, resta
- 20261021T004735Z LEG D1 closed: three keys read 404, uploaded and read back by VersionId equal: tar qXJvdeOXrw7ovNKWAcen3XRT41HIC1rI, sums sMIjjC9lxuWP2
- 20261021T005313Z LEG D2 closed: install script rc=0 at 2026-10-21T00:49:50Z (SSM command 75c042f9-a099-4adc-ab75-dcc36a2fde1e, install_r34.sh sha256 4c3
- 20261021T005346Z LEG V1 closed: V1 running root r34p active restarts 0; members 1 of 1 MATCH (registry 229eca2d); sums 0 not OK of 322; census package s
- 20261021T005439Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command 905cc8a9-043a-45ad-b3e0-ef5906757ced, V2 script sha256 7817cf8c..., exp
- 20261021T005509Z CLOSED -- all 5 legs proven
