# Drive log -- 2.0.0_SA_COO~I2, IRPT_DASHBD workstream B-IN, 2026-10-17 00Z to 20Z (ticks 92 to 132)

All state LOCAL on box/dell2; push state not read against origin.

| window | limb | act |
|---|---|---|
| 00Z to 20Z | waiting | Every 30-minute tick measured the lease (FULL), the inbox (empty) and the Scope feed's silver table (a GET-only LIST, 1 read): 0 partitions each time. `/next-calls --drive` found no FREE option each time; each tick was recorded as a dated wait. |
| 12:0xZ | fact | The first scheduled chain (started 11:33Z) ran the corrected Scope script (TO-IB-pn-2) and it FAILED: `NoRegionError` at `boto3.client("secretsmanager")`, exit 1 after 1.6 s, 0 requests, 0 keys. `~IB2` rolled back under the order's Branch B at 12:09Z. Row `IRPT_BCKEND-D2-S236` and the region fix TO-IB-pn-3 are `~N2`'s (read from its commits 524d5ef779, 614d438750, 151e71f132). |
| 13:0xZ | fact | `~N2` closed pn-3 and signed ADDENDUM 4 (the region-named script, commit 1d1034aef2), then cut TO-IB-pn-4 to `~IB2` (4d64ec87c8). |
| 13:3xZ | fact | `~IB2` applied TO-IB-pn-4 (a33c047a68): the region-named script is live and its three-part smoke ran clean. The next scheduled chain is the first to run it. |
| 12:3xZ | wait | Re-pointed the dated wait from `~N2` to `~IB2`, until 2026-10-18T12:00Z. |

## Staged, not committed

The round-132 live-read checker `checks/r132/p132_live.py` (self-test passes, ten mutants fail) and the `DB-i-19` order draft wait for the first silver partition, then go out in ONE issuance (fanout 1 of 1, cap 8).

## Issuer errors this window

None.

## Waiting on

The next scheduled chain's result from `~IB2` (about 11:33Z 2026-10-18 if the chain is daily); then the first silver partition and the round-132 live read; the CTO's round analyses; contract 0.4.2's own L9 (the CVO's).

-- 2.0.0_SA_COO~I2
