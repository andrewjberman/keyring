# Andrew-direct 2026-10-09 ~03:1xZ -- every COO runs /canonical-drive, tapped into /keep-driving

Seat: 0.0.0_AB_MSTR~DELL1 terminal.

## Verbatim

> "Make sure that all COOs on your box are running /canonical-drive on their given project, and are tapped into the
> /keep-driving system. We want to see the /next-calls ticks into /unblock sequence somewhere in the cluster and see what
> happens."

> "Issue this message verbatim to MSTR~DELL2 and MSTR~Z"

## Acts (0.0.0_AB_MSTR~DELL1)

- Switch read: `python .tools/open-calls.py mode get` -> `scan=on empty_tick=on overrides=[none]`; dell1 scan=on,
  empty_tick=on. No flip needed.
- `python .tools/unblock.py list` -> 0 cases cluster-wide at 03:1xZ.
- Relayed verbatim over the bus to dell2 (MessageId b6f8ee4d) and sitez (MessageId f3d135ee).
- Sent to all ten dell1 COOs (C1, D1, G1, H1, M1, Q1, R1, S1, V1, W1; msg ids 1538-1547, 10 DELIVERED): arm
  `/canonical-drive` on the project if not armed, reply with project code and cron id. Mechanism cited:
  `.claude/skills/canonical-drive/SKILL.md` :33-37 (empty tick -> `/next-calls <CODE> --drive` -> `unblock.py tick`;
  THIRD-EMPTY-TICK -> `/unblock` to the CRO).
