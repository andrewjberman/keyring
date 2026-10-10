# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: post-outage restart; MX-r-9 repair GO re-sent to a re-seated applier; AC2/AC3 pre-read PASS; J1 queued -- 2026-10-10 20:5xZ-21:3xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Context

Site Z hit usage limits shortly after 20:0xZ on 2026-10-09 and was down about 25h. Andrew's restart order (laptop,
CTO): `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261010_201xZ_RESTART_COMPILE_STATE_DEPLOYS_THEN_RESIDUE_THEN_INFORM.md`.

## Ticks and events

| time | act |
|---|---|
| 20:51Z | Session start. Registered, watcher armed (pid 27216), inbox empty, 30/30 delivery rows READ |
| 20:59Z | NEVER-2 artifact read of open ledger `nfra-mcpindex-r8-discover-release` (OPEN, 0 of 4 legs). S3 unchanged since 19:42Z 10-09: `-latest` and the rollback key `opal-gateway-1e32562729.tar.gz` both 525795 / ETag 0eed0817 stamped 1e32562729; `opal-gateway-d3c31e972e.tar.gz` 404; base VersionId t6Dv5giTH_t44Ae_FlV3.LcFyQOOVPOh (ETag b96315a5) present |
| 21:0xZ | Cause found: my repair GO 32997 and 33003 were OFFER-EXHAUSTED, never read by `0.7.0_AE_CloudOps~MX`, because the box went down first. ~MX NOT REGISTERED |
| 21:07Z | `/mstr-spawn 0.7.0_AE_CloudOps~MX` (1pt 0 of 13 claude.exe, 1b 0 markers, 1c 0/20, 1d continuity on MX-r-9 only, work measured undone). Repair GO re-sent as msg 33009 |
| 21:08Z | 33009 READ by ~MX (PID 2300) |
| 21:1xZ | 33011 from `2.0.0_SA_COO~MP` answered (33013/33014 to ~MP and ~O): the close condition is CTO~Z 33001's two read-backs |
| 21:1xZ | `/canonical-drive NFRA_MCPINDEX` re-armed, cron 16,46, off the LIVE_ARMS COO-half row (record `ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`, no stop recorded) |
| 21:24Z | Drive tick: ~MX in startup, S3 still unchanged. Not a nudge (heartbeating, 15 min since READ) |
| 21:2xZ | Empty tick, so `/next-calls --drive` ran. r9.AC2 PASS 3/3 (ssm 0592e3b5) and r9.AC3 PASS 9/9 + 3/3 (ssm 9be4e4a8) on the served host, ahead of ~MX's L4. Service is correct; only the labels are wrong |
| 21:27Z | J1 pre-booked with `0.0.0_AB_MSTR~Z` (33019). Queued there and put to Andrew (33020); it fires on my "closed" |

## Next

- On ~MX's two read-backs (rollback ETag b96315a5; host md5 unchanged, /health 200, .env 52): verify both myself,
  send "closed" to `2.0.0_SA_COO~O`, `2.0.0_SA_COO~MP` and `0.0.0_AB_MSTR~Z`, then grade r9.AC1-AC3 and close the TO.
- Then the round-8 L8 packet to the CVO (J1 and J2 at L9), and round 9 per the CTO ruling (after the round-8 drain).
- MX-s-19 stays event-gated on the 2026-10-13 runs.

## Compiler Tools

- `.tools/aws s3api head-object` and `list-object-versions` on the gateway artifact keys: ground truth for the label
  state, twice.
- `get_delivery_state`: found the OFFER-EXHAUSTED GO, the cause of the stall. `check-inbox` cannot see that class.
- `to-check.py --all --assignee`: 0 for ~MI, 1 (MX-r-9) for ~MX.
- `sequence-check.py --project NFRA_MCPINDEX`: no flags.
- `r9.AC2.sh` and `r9.AC3.sh` run verbatim: both PASS.
- `audit-archive-invoker.py`: INTEGRITY and COVERAGE findings on shared audit logs, stale baseline 39.7h; owned by the
  audit-archive owner, not re-filed.
