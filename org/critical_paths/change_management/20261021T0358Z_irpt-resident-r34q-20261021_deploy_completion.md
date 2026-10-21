# Deploy Completion Record
**Date opened:** 2026-10-21T03:58:43.094688+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T040649Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34Q: resident release 34q (S245 admission fix, tickets_table binding, audit revision) on the resident host: three S3 objects, pre-read, signed install, after-reads, V2 inside the service environment
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read as root: running root r34p, r34q root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS at 2026-10-21T04:01:51Z (SSM command 956d66b8-44d1-488b-af5e-a4c694cc8e00): running root r34p restarts 0, r34q root absent, five changing members at their r34p value, library and wrapper unmoved, queue 0 0; COO blob a453712369 and CTO half naming it; three checker arms OK; stage hashes equal; open-deploys 50 worktrees 151 entries, 8 terminal name the resident, 0 non-terminal | CLOSED 20261021T040227Z |
| D1 | activation | upload the tar, the sums file and the host script, each read back by VersionId equal | three keys uploaded and read back equal | three keys read 404, uploaded and read back by VersionId equal: tar S0TbRKv._XzsSgUFewhhvajQhLwlMsa0, sums ABSWjAzFahZTE3loSjbIGNt2tBcRzuVy, script ToG0CZGYG8gEUST7spjMEnR.zZJnLTc5 (D1_UPLOAD_OUT.txt) | CLOSED 20261021T040303Z |
| D2 | activation | signed install as root: r34q root installed, unit restarted, polled | install success line and running root r34q | install script rc=0 at 2026-10-21T04:04:17Z (SSM command 906efb0e-b3e3-4180-846a-b2537fd03757, install_r34.sh sha256 49e86cf9...): running root /opt/irpt-resident/0485393f3a-r34q active restarts 0; five members MATCH; package sums 0 not OK of 322; queue 0 0; no sign-in | CLOSED 20261021T040443Z |
| V1 | verify | after-reads: sums, census, cure, bindings, pool, imports, IRPT_TICKETS_TABLE word | V1 lines | V1 running root r34q active restarts 0; members 5 of 5 MATCH; sums 0 not OK of 322; census package scope 7 changed 0 added 0 removed; cure anlreq 8edbe84b05765c36 ACTIVE, dashbd 244a20425ba40cde PENDING_ENFORCEMENT, audit 2b4f91d3feda649b ACTIVE, registry b41a3fb5, submission lists commentary_requested yes; bindings pin 21cb4e85 files_from 49 tickets_table opal-tickets opal_map pinned packager unchanged, 2 of 19 binding keys differ (provenance, tickets_table); pool pinned pricing estate yfinance ycharts budget 6 per 390 s; IRPT_TICKETS_TABLE unset in unit and process (control PATH= read 1); jsonschema yes; queue 0 0; no sign-in | CLOSED 20261021T040526Z |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command a8b8f8ce-6ddc-4f6b-95ea-6db0f1e8eb1b, V2 script sha256 7817cf8c..., export V2S_WANT_ROOT=/opt/irpt-resident/0485393f3a-r34q, path conversion off); controls 4 of 4, backoff, door, pricing, budget, tier OK; transient unit rc=0; 2 Yahoo calls, no YCharts call | CLOSED 20261021T040647Z |

## Log

- 20261021T035843Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T040227Z LEG P1 closed: P1 STOP-READ-0 PASS at 2026-10-21T04:01:51Z (SSM command 956d66b8-44d1-488b-af5e-a4c694cc8e00): running root r34p restar
- 20261021T040303Z LEG D1 closed: three keys read 404, uploaded and read back by VersionId equal: tar S0TbRKv._XzsSgUFewhhvajQhLwlMsa0, sums ABSWjAzFahZTE
- 20261021T040443Z LEG D2 closed: install script rc=0 at 2026-10-21T04:04:17Z (SSM command 906efb0e-b3e3-4180-846a-b2537fd03757, install_r34.sh sha256 49e
- 20261021T040526Z LEG V1 closed: V1 running root r34q active restarts 0; members 5 of 5 MATCH; sums 0 not OK of 322; census package scope 7 changed 0 add
- 20261021T040647Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command a8b8f8ce-6ddc-4f6b-95ea-6db0f1e8eb1b, V2 script sha256 7817cf8c..., exp
- 20261021T040649Z CLOSED -- all 5 legs proven
