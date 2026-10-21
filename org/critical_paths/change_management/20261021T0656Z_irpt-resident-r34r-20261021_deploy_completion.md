# Deploy Completion Record
**Date opened:** 2026-10-21T06:56:19.614354+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T070042Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34R: resident release 34r (S249 comparison-path fix, lead token, audit projection) on the resident host: three S3 objects, pre-read, signed install, after-reads, V2 inside the service environment
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read as root: running root r34q, r34r root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS at 2026-10-21T06:56:41Z (SSM command 56b806cc-b5ea-4837-baeb-c77886a1f4c1): running root r34q restarts 0, r34r root absent, the four changing members at their r34q value, library and wrapper unmoved, queue 0 0; COO blob fd5b51feaa and CTO half naming it; three checker arms OK; stage hashes equal; started after the 06:00Z to 06:55Z window; open-deploys 50 worktrees 157 entries, 8 terminal name the resident, 0 non-terminal | CLOSED 20261021T065700Z |
| D1 | activation | upload the tar, the sums file and the host script, each read back by VersionId equal | three keys uploaded and read back equal | three keys read 404, uploaded and read back by VersionId equal: tar oxYoJwhCVgkevKgYPtqYLl3eGwweby9F, sums vsQKX50hX5As1OZr_eF2Tyq.i50teSSQ, script Yu_7y1eySBSlr5XhqQDefqTebPZFIiI1 (D1_UPLOAD_OUT.txt) | CLOSED 20261021T065721Z |
| D2 | activation | signed install as root: r34r root installed, unit restarted, polled | install success line and running root r34r | install script rc=0 at 2026-10-21T06:58:23Z (SSM command d0aba62a-18ab-479b-9d37-53f10a4a46f6, install_r34.sh sha256 d124f8e9...): running root /opt/irpt-resident/0485393f3a-r34r active restarts 0; four members MATCH; package sums 0 not OK of 322; queue 0 0; no sign-in | CLOSED 20261021T065902Z |
| V1 | verify | after-reads: sums, census, fix, bindings, pool, imports, IRPT_TICKETS_TABLE word | V1 lines | V1 running root r34r active restarts 0; members 4 of 4 MATCH; sums 0 not OK of 322; census package scope 6 changed 0 added 0 removed; fix: FrozenCompositionWorker.prepare takes upload yes, retained_reason for a RecipeRefused stand-in prints class=RecipeRefused code=- lead=holdings_row_has_no_provider_receipt; policy revisions 8edbe84b05765c36 ACTIVE, 244a20425ba40cde PENDING_ENFORCEMENT, 2b4f91d3feda649b ACTIVE and the registry file b41a3fb5 equal r34q; bindings pin 32bb8d5a files_from 50 tickets_table opal-tickets opal_map pinned packager unchanged, 1 of 19 binding keys differs (provenance); pool pinned pricing estate yfinance ycharts budget 6 per 390 s; IRPT_TICKETS_TABLE unset in unit and process (control PATH= read 1); jsonschema yes; queue 0 0; no sign-in | CLOSED 20261021T065938Z |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command 04e29ef8-0e9b-4c0a-9a20-4eac945464c6, V2 script sha256 7817cf8c..., export V2S_WANT_ROOT=/opt/irpt-resident/0485393f3a-r34r, path conversion off); controls 4 of 4, backoff, door, pricing, budget, tier OK; transient unit rc=0; 2 Yahoo calls, no YCharts call | CLOSED 20261021T070042Z |

## Log

- 20261021T065619Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T065700Z LEG P1 closed: P1 STOP-READ-0 PASS at 2026-10-21T06:56:41Z (SSM command 56b806cc-b5ea-4837-baeb-c77886a1f4c1): running root r34q restar
- 20261021T065721Z LEG D1 closed: three keys read 404, uploaded and read back by VersionId equal: tar oxYoJwhCVgkevKgYPtqYLl3eGwweby9F, sums vsQKX50hX5As1
- 20261021T065902Z LEG D2 closed: install script rc=0 at 2026-10-21T06:58:23Z (SSM command d0aba62a-18ab-479b-9d37-53f10a4a46f6, install_r34.sh sha256 d12
- 20261021T065938Z LEG V1 closed: V1 running root r34r active restarts 0; members 4 of 4 MATCH; sums 0 not OK of 322; census package scope 6 changed 0 add
- 20261021T070042Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM command 04e29ef8-0e9b-4c0a-9a20-4eac945464c6, V2 script sha256 7817cf8c..., exp
- 20261021T070042Z CLOSED -- all 5 legs proven
