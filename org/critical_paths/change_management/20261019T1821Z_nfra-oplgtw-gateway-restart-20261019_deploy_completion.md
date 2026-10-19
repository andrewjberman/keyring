# Deploy Completion Record
**Date opened:** 2026-10-19T18:21:53.655159+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T183627Z
**Deploy:** Restart hung opal-gateway service on i-07dccb1615503ac99, same release 6d1b5dcb64 (CTO 36059 incident; OG-rs-1 superseded)
**Authored by:** 0.0.0_AB_MSTR~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | systemctl restart opal-gateway on the gateway host, same release 6d1b5dcb64 | /health 200 within 60s of restart, marker still 6d1b5dcb64, one process, NRestarts read | SSM 84b23884: restart 18:24:47Z rc=0 (stop took 90s); /health 200 at 18:26:22Z; read-back 18:34:36-40Z health 200 x3, marker 6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c, 1 uvicorn proc, NRestarts 0, MemoryCurrent 85MB at 60s and 135MB at 8min (was 1283MB); before: SSM f69d432a health 000 in 5s | CLOSED 20261019T183627Z |

## Log

- 20261019T182153Z OPENED by 0.0.0_AB_MSTR~Z with 1 leg(s)
- 20261019T183627Z LEG L1 closed: SSM 84b23884: restart 18:24:47Z rc=0 (stop took 90s); /health 200 at 18:26:22Z; read-back 18:34:36-40Z health 200 x3, ma
- 20261019T183627Z CLOSED -- all 1 legs proven
