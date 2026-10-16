# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 26 (2026-10-16 ~14:36Z to 14:58Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| MSTR~Z 35066: `~MI2` killed (processes gone); the broker row still reads LIVE and MSTR may not deregister it | `deregister_agent 2.0.0_SA_COO~MI2`: liveness and broker rows removed, 0 pollers | broker receipt |
| CVO 35067: OG-ap-29 CVO half SIGNED @6b7d6ef48d. Firm scope measured: z08 on 100% of rows of the newest object of all four tables, 0 z09. Condition: the `-live` routing ships in the same release | relayed to COO~O and CloudOps~ZS (35068/35069); all three halves are signed at `5604d8577f68a50d`; Phase B GO is `~O`'s | relay |
| COO~MP 35073: MP-pf-11, the Indexes scroll cue, built @05966c0ffa; ride or cut? | REC ratified: it rides the next batched gateway release (mcportal 59e802a pinned via `~O`); no bundle-only MP-pf-12 | msg to COO~MP |

## Scope state

7 open on site Z (54 rows), all `act`, all only Andrew can do; 0 forks. COO lanes live: `~O`, `~MI` and `~MP` (`~MI2` ended).

The next batched gateway release carries:
- the OG-ap-29 role apply (Phase B, before the release) and the `-live` routing;
- `~MI`'s 49F address field and live rows;
- OG-en-10's 429 audit, E9 and MP-pf-11.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| deregister_agent | the `~MI2` broker row | removed |
| send_message / ack_messages | 2 sends, 3 acks | DELIVERED / READ |
