# DELL1 self-drive box -- tick 191, 2026-10-20 ~14:18Z (delta: COTBOOKS endpoint v2, autoshutdown confirmed)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec)

## Inbox and open calls
- 0 unread at 14:18Z. Acked since tick 190: 8644, 8646, 8649, 8652.
- open_calls.json: 158 rows, 2 OPEN, both acts only Andrew can do.

## Acts and rulings
- **ADVI_COTBOOKS endpoint v2** @bdbdc59bf7 (`deliverables/ENDPOINT_FORWARD_ADVI_COTBOOKS_20261020.md`).
  - 8 outcomes from the CRO re-brief @fcb2c7cbaf (msg 8646). Black Diamond is read only as the comparison.
  - FWD-3 is a qualified wait on the Schwab master numbers (Andrew's word).
  - Two RECs are carried: the 15% with no custodian feed shows as a sized not-read line; the advisor assignment is seeded once from
    BD and then owned by Opal.
  - Act row ea86 was added for Andrew's confirmation.
  - An F2 correction was sent to CRO~DELL1: the FIDUPL root is applied, not planned.
- **NFRA_FIDUPL autoshutdown.** Andrew confirmed the ruling as written (record @fca03ab0ad, msg 8649). I lifted the apply-timing
  condition so the box stays up while the sign-in is retried. Sent to COO~P1.
- **Estate report (8644):** the base CVO is LIVE on the laptop, so nothing is owed from dell1. CVO~DELL1 was told.
- **FYI 8652:** gateway release window Wed 06:00-06:45Z. No dell1 schedule is in it.

## Scope state
- **NFRA_FIDUPL:** FU-x-1 live; two sign-in attempts stopped before the SMS step (rows W1-S9, W1-S11, COO~P1's lane).
- **ADVI_COTBOOKS:** L2, waiting on Andrew's confirmation.
- **AMGT_HARVST:** stage 6 at 14:00Z.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2, his word).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA session).

## Compiler Tools
- `open-calls.py add`.
