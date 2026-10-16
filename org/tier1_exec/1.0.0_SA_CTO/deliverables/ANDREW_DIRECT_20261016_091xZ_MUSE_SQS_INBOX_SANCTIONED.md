# ANDREW-DIRECT 2026-10-16 ~09:1xZ -- give muse the SQS inbox

**Channel:** Andrew at the `1.0.0_SA_CTO~Z` terminal (site Z), ~09:1xZ 2026-10-16, answering open act row `sitez-20261016T083801Z-35b3`.
**Recorded by:** `1.0.0_SA_CTO~Z`, in the same turn.

## Verbatim

> "I'm here, give muse the inbox sqs"

## What it settles

1. ms (muse) gets an inbound bus destination: queue `agentbus-ajbdev-to-ms.fifo` (account 313476888478, us-east-1; FIFO with
   content dedup; MSTR~Z read it read-only per relay msg 34848). This lifts the "sender-only" status in the device register
   that his 2026-10-13 word set for ms. Seats that talk to ms send there. Mail stays the fallback.
2. The register edit (DEVICES.json) and the send path in `.tools/agentbus-sqs.sh` are `0.0.0_AB_MSTR~Z`'s to make, on this record.
3. Row 35b3 closes, ruled by Andrew.
