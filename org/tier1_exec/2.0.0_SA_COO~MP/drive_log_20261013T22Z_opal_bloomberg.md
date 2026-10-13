# Drive log -- 2.0.0_SA_COO~MP (sitez) -- 2026-10-13 19:2xZ-22:2xZ -- NFRA_MCPORTAL

Respawned after the 18:57Z site Z reboot (spawned by 0.0.0_AB_MSTR~Z on 1.0.0_SA_CTO~Z's ask, msg 33701).
`/canonical-drive NFRA_MCPORTAL` armed at 60m (cron at :23) on Andrew's 20:3xZ word, relayed in msg 33744. The LIVE_ARMS row is on CLOUD @81ef5aa2db (msg 33757).

## Closed decision: FWD-20's release (MP-z-5) is LIVE and drained

| act | commit / msg |
|---|---|
| Amendment 2: the GO's worker commits and the measured sparse list (rows Z-S42 and Z-S43 ruled) | @2627c1905f |
| G-REL3 read; gateway slot agreed with 2.0.0_SA_COO~O (OG-bd-2 follows) | msgs 33705/33706 |
| 0.7.0_AE_CloudOps~MQ respawned after the reboot (pre-flight clean: 0 procs, 0 markers, 6/20) | spawn audit 19:3xZ |
| GO: staged -> pending | @81e079ba4b, msg to ~MQ |
| COO never-widen half SIGNED: section 3a accepted; section 6 ruled as a closed list of 7 test ids (row Z-S45) | @0a54b917d9 |
| CTO half SIGNED (same closed set) | @567da88c25 |
| opal-gateway deployed 21:08Z at 64b3e54658060859b81d6bcd48dc7000615f865d | adcb1bf07b, d76cb2401c |
| Amendment 3: the AC2 probe imports app.server (row Z-S48) | @ac44bd46e0 |
| Ledger nfra-mcportal-gw-release CLOSED, 5 of 5 legs; AC1 and AC2 PASS; instance VALID | 4d9261146b, @4cd50e93dd |
| Gateway slot handed back to ~O with the new deployed_commit | msg 21:51Z |
| Ledger entry landed on the trunk (blob-identical); MP-z-5 complete | @485d9eb775 |
| admin_api hookup drained; the 5 payload files on the trunk equal the release, 5 of 5 | @516a2345af |
| EC2_MANIFEST record on the trunk (six fields, 26 other blocks byte-identical) by ~MQ | @9635c128bc |
| MP-z-6 step 2 names `import app.server` before the cell is issued | @d649f04608 |

## What the world shows

With no identity, /control-plane, /open-calls and /gateway answer 401 where they answered 404 before. The breakdown
`_compute` on the host reads channels=8 tools=67 dup_tools=0 channels_held=8 grant_store=read in 1.2 s. The MCP tool
surface difference is empty. The rollback tree is C:/tmp/mp-z5-rb (kept until the round closes).

## Open

- MP-z-6 (FWD-20 close run) is staged on Andrew's read. 1.0.0_SA_CTO~Z is putting the one MC Portal sitting on the open-calls list (msg 33793).
- At that sitting, the page lists the Bloomberg account as an m365 holder. This is the live grant until NFRA_OPLGTW
  releases OG-tg-1, and it agrees with DIRECTION_SITEZ Z7 (COO half, section 6 item 4).
- Row Z-S47 (Andrew: the Claude account and 5h/weekly usage per box on Control Plane) is parked to the GW-round analysis addendum (CTO msg 33782).
- Rows Z-S44, Z-S45, Z-S46 and Z-S48 are ruled by the issuer as above; their L8 adjudication is the CVO's.
- GW-decomposition note for later cells: a release tree's org/ is frozen at the release chain's vintage, so tests reading repo data outside the gateway dir cannot pass there (Z-S45 general note).
