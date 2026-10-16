# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 21-22 (2026-10-16 ~12:28Z to 12:57Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| CVO 34988: round 37 v32/v33, 8 of 8 graded, MAY-CLOSE | round-37 analysis updated: ap-14 and mg-1 MET, E1/E2 discharged, E9 added (a missing key answers not-found, not 403) | @9dbe9546bc |
| Z-S176: `round-close-check` grades from the first CVO row, not the grade of record | cross-box to `2.0.0_SA_COO~C` (NFRA_CTLPLN owns the tool) as XB-20261016T121809Z-95c2; MSTR~Z sent it on the bus (ac0634a4), not yet acked | @213c43a184 |
| COO~MP (inbox 20261016T122159Z): MP-pf-9, the bundle-only mcportal release, is cut (applier CloudOps~MQ) | departure from CloudOps~Z accepted (seating rule); CTO half signs on ~MQ's ask | -- |
| COO~O 34999: Z-S177, the opalgateway 429. The limiter is 120 requests per 60 s per identity, in memory; every /mcp POST counts, initialize and tools/list included; site Z shares one identity; a 429 writes no audit row | RULED as proposed: measure first. OG-en-10 audits each 429 with the limiter count (one row per identity per 10 s) on the batched release. No raise of RL_MCP_IDENTITY_LIMIT and no identity split until the rows exist. The choice then weighs three arms: raise the limit, separate identities, or exempt initialize/tools/list from the count | msg to COO~O 20261016T124212Z |
| COO~O 34999: E4, E5, E6, E8 and ts-1 merged; OG-en-7 counted 6010 SmartX candidates, 0 cross-firm; E9 is OG-en-9 | noted for the CVO's grading | -- |

## Scope state

7 open on site Z (`open-calls.py list`, 54 rows), all `act`, all only Andrew can do; 0 forks:
- 21c5, f0d2, 8ed7, 21d9: his MC Portal sitting (21d9 bundles the other three; f0d2 is his login);
- def4: postponed on his word (~07:2xZ, relay 34811);
- bd68: Alyssa's downloads, enforce or strike his 10-08 "no downloads needed yet";
- 5b35: the named asset manager's driven harvest call, after the E3 stand-in read.

Waiting (not calls): CloudOps~MQ's MP-pf-9 ask; COO~C's answer on XB-95c2; OG-en-10's first 429 rows.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| open-calls.py list | the box queue | 7 OPEN of 54 |
| send_message / ack_messages | Z-S177 ruling; ack 34999 | DELIVERED; READ |
| inbox-watch.sh (Monitor) | re-armed on WATCHER-EXPIRED 12:42Z | task bhyfhoflp |

- **What failed:** nothing this span. The 429 itself is a live defect on this seat's own gateway connection (opalgateway MCP unavailable), owned by COO~O as Z-S177.
