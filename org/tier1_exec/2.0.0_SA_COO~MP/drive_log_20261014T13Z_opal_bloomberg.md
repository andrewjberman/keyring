# Drive log -- 2.0.0_SA_COO~MP (sitez) -- 2026-10-14 12Z-13Z -- NFRA_MCPORTAL

## Ticks

| tick | project | limb | TOs | thread | outcome |
|---|---|---|---|---|---|
| 12:3xZ | NFRA_MCPORTAL | EXECUTING; PC round 1 | pc-1..4 drained; pc-5, pc-6 staged | none | EMPTY -> /next-calls --drive: WAIT on the gateway queue (OG-hv-2 first per Andrew's acceleration, commit 45a2ebd20b; then the tier-admission fix; then OG-mg-1). Payload pre-check re-run against live 90967e39ba: r30 changed 0 of the 5 payload files, the 3 worker commits exist. Re-read at the act. |
| 13:3xZ | NFRA_MCPORTAL | same | same | none | WAIT recorded (unblock.py: owner 2.0.0_SA_COO~O live, until 17:00Z), empty count 0. The armed surprise rows Z-W2-S8, Z-W3-S2, Z-C-S8, Z-C-S3 are 19.6 days old and carry later adjudication/remediation versions (v4); not re-ruled this tick. |

## Acts this window

- Startup: watcher armed, `/canonical-drive 60m` cron at :23 per the LIVE_ARMS row for `~MP`.
- Andrew-direct ~12:2xZ recorded (commit 6b22f775c3, LOCAL) and relayed to 2.0.0_SA_COO~MI and 1.0.0_SA_CTO~Z (msgs 34049, 34050).
- GC ask 34084 answered: archive/sitez/rel-nfra-mcportal-c17-v2-e5bc28df26 tagged on origin and mp-n1-rel2 removed by 0.0.0_AB_MSTR~Z (msg 34088, acked).

## Carried state

- MP-pc-5 GO when the queue frees: worker commits 90ad6bfa00, 12d990e43d, 33d0604810; mcportal 17dcbb2. MP-pc-6 spawns with model haiku, effort high.
- Calls at Andrew unchanged: 21d9, def4.
