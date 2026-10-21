# Deploy Completion Record
**Date opened:** 2026-10-21T08:58:06.890785+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T090306Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34S: resident release 34s (Multi-Comp portfolio path from the common window start, report presentation fixes) on the resident host: three S3 objects, pre-read, signed install, after-reads, V2 inside the service environment
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read as root: running root r34r, r34s root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS at 2026-10-21T08:58:49Z (SSM command 1c870390-b2c9-4304-bcfc-207954e28554): running root r34r restarts 0, r34s root absent, the three changing members at their r34r value, library and wrapper unmoved, queue 0 0; COO blob c5148a9c27 and CTO half naming it; three checker arms OK; stage hashes equal; start condition met (residue-delete ledger CLOSED); open-deploys 50 worktrees 160 entries, 8 terminal name the resident, 0 non-terminal | CLOSED 20261021T085908Z |
| D1 | activation | upload the tar, the sums file and the host script, each read back by VersionId equal | three keys uploaded and read back equal | three keys read 404, uploaded and read back by VersionId equal: tar xB8aJXSZ9II9dlfHvCSDrZ47qo46LVp2, sums Hyoeru8TET9qy9RVhM1xV5.7R.9vngy2, script 29TcKaa31UlfVbfJwbFwESS0I1o4.C2F (D1_UPLOAD_OUT.txt) | CLOSED 20261021T085944Z |
| D2 | activation | signed install as root: r34s root installed, unit restarted, polled | install success line and running root r34s | install script rc=0 at 2026-10-21T09:00:34Z (SSM command 3a2b2375-05e3-4503-a23c-885a8916ec6f, install_r34.sh sha256 bc002da4...): running root /opt/irpt-resident/0485393f3a-r34s active restarts 0; three members MATCH; package sums 0 not OK of 322; queue 0 0; no sign-in | CLOSED 20261021T090112Z |
| V1 | verify | after-reads: sums, census, fix words, bindings, pool, imports, IRPT_TICKETS_TABLE word | V1 lines | V1 running root r34s active restarts 0; members 3 of 3 MATCH; sums 0 not OK of 322; census package scope 5 changed 0 added 0 removed; fix words on the host: portfolio_series defines buy_and_hold_from yes, opal_producer calls it yes, layout_overview carries the .cmp break-inside rule yes, no COMPARE_EMPTY_LINE yes; policy revisions 8edbe84b05765c36 ACTIVE, 244a20425ba40cde PENDING_ENFORCEMENT, 2b4f91d3feda649b ACTIVE and registry b41a3fb5 equal r34r; bindings pin 5fd1e793 files_from 50 tickets_table opal-tickets opal_map pinned packager unchanged, 1 of 19 binding keys differs (provenance); pool pinned pricing estate yfinance ycharts budget 6 per 390 s; IRPT_TICKETS_TABLE unset in unit and process (control PATH= read 1); jsonschema yes; queue 0 0; no sign-in | CLOSED 20261021T090147Z |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command 8ef9844c-a91a-4197-afb7-dedf4d611815, V2 script sha256 7817cf8c..., export V2S_WANT_ROOT=/opt/irpt-resident/0485393f3a-r34s, path conversion off); controls 4 of 4, backoff, door, pricing, budget, tier OK; transient unit rc=0; 2 Yahoo calls, no YCharts call | CLOSED 20261021T090306Z |

## Log

- 20261021T085806Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T085908Z LEG P1 closed: P1 STOP-READ-0 PASS at 2026-10-21T08:58:49Z (SSM command 1c870390-b2c9-4304-bcfc-207954e28554): running root r34r restar
- 20261021T085944Z LEG D1 closed: three keys read 404, uploaded and read back by VersionId equal: tar xB8aJXSZ9II9dlfHvCSDrZ47qo46LVp2, sums Hyoeru8TET9qy
- 20261021T090112Z LEG D2 closed: install script rc=0 at 2026-10-21T09:00:34Z (SSM command 3a2b2375-05e3-4503-a23c-885a8916ec6f, install_r34.sh sha256 bc0
- 20261021T090147Z LEG V1 closed: V1 running root r34s active restarts 0; members 3 of 3 MATCH; sums 0 not OK of 322; census package scope 5 changed 0 add
- 20261021T090306Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command 8ef9844c-a91a-4197-afb7-dedf4d611815, V2 script sha256 7817cf8c..., exp
- 20261021T090306Z CLOSED -- all 5 legs proven
