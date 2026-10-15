# Deploy Completion Record
**Date opened:** 2026-10-15T22:03:36.829193+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T221724Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R32R (round 21, AR-g-97): resident r31 -> r32 on the resident host, leg R only: upload 3 keys, SSM pre-read, signed install (self-rollback on failed start), V1 after-reads and census; COO half blob 1c3023a9f1, CTO half msg 8693; tar sha256 3338a5c7...
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | SSM pre-read pre_read_r32.sh: running root r31, members at r31, added ABSENT, queue 0 0 | P1 STOP-READ-0 PASS and the printed table | SSM 4360a8dc-6493-429a-8042-9666e23d2c53 Success rc 0 at 22:04Z: P1 STOP-READ-0 PASS, running root r31 active restarts 0, 13 changed members at r31 values MATCH, 11 added members ABSENT, unit free of IRPT_ANALYSIS_READY_QUEUE_URL, library and wrapper unmoved, r32 root and kept-copy path absent, queue 0 0, journal polls 3 tracebacks 0 | CLOSED 20261015T220543Z |
| D1 | verify | upload tar, sums and host script to three keys (each 404 first), read back equal, record VersionIds | three sha256 equal and three VersionIds | three keys each 404 first, uploaded from the stage folder, each read back by download: tar sha256 3338a5c7... 1087615 bytes VersionId Ogs4iUHgnRiUkZe9VcYubANZLFSwhBiI; sums sha256 8a473acc... 33980 bytes VersionId FyqkZ9kX.XbDD4KJYVfoZ66upuu0XaXZ; host script sha256 5adc8d0b... 10199 bytes VersionId MT1Ldk.RVwuLa.vIIEnqMQ1m6zilX_u6 | CLOSED 20261015T220731Z |
| D2 | ec2-baked-asset | SSM install_r32.sh: running root r32 on the host | SSM output: running root and rc | SSM f90c0cae-3766-4da8-bb22-6044832656d4 Success rc 0 at 22:09Z: host script and sums fetched by key and sha256-verified on the host, queue 0 0 twice, factory OK, install 0485393f3a-r32 rc=0, active polls_30s=2 tracebacks_30s=0, no rollback; running root /opt/irpt-resident/0485393f3a-r32 MainPID 1070733 restarts 0, running worker sha256 7bab7930... | CLOSED 20261015T221724Z |
| V1 | verify | after-reads: 25 members MATCH, sums 309 of 309, census 15 changed 11 added 0 removed, producer list, commentary x10 registered pricing off, queue 0 0 | the printed lines | V1 reads 22:09Z to 22:12Z: member table 24 of 24 MATCH plus bindings c4a810ee read by the census = 25 of 25; sums 0 of 309 not OK; census r31 3773 r32 3784 files, 15 differ, 11 only r32, 0 only r31 (pyc excluded, counted); producer list exactly (andrew@opalinvest.com, fwd1-staff-r41b@opal.invalid); Opal imports exit 0; opal_pricing enabled false; ANALYSIS_COMMENTARY_REVISION irpt-anlreq-x10-v1 passed into the built runtime (source read, factory OK on the host); queue 0 0; no sign-in; r31 root and kept library present | CLOSED 20261015T221724Z |

## Log

- 20261015T220336Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261015T220543Z LEG P1 closed: SSM 4360a8dc-6493-429a-8042-9666e23d2c53 Success rc 0 at 22:04Z: P1 STOP-READ-0 PASS, running root r31 active restarts 0
- 20261015T220731Z LEG D1 closed: three keys each 404 first, uploaded from the stage folder, each read back by download: tar sha256 3338a5c7... 1087615 by
- 20261015T221724Z LEG D2 closed: SSM f90c0cae-3766-4da8-bb22-6044832656d4 Success rc 0 at 22:09Z: host script and sums fetched by key and sha256-verified
- 20261015T221724Z LEG V1 closed: V1 reads 22:09Z to 22:12Z: member table 24 of 24 MATCH plus bindings c4a810ee read by the census = 25 of 25; sums 0 of 3
- 20261015T221724Z CLOSED -- all 4 legs proven
