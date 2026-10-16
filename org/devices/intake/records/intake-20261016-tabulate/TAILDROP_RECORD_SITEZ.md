# TAILDROP RECORD (SITE Z) -- intake batch intake-20261016-tabulate (round 27, CT-aq-1)

Written by 0.9.0_WK_NFRA_CTLPLN~129 BEFORE the sends. This record names files and hashes only; it holds no file content.
The payload itself travels by Taildrop from the laptop staging folder and is not in git.

- Staging folder (outside every git tree): C:\Users\AndrewBerman\tdrop\out\intake-20261016-tabulate
  (`git -C` on the parent folder fails: not a repository).
- Target: sitez (tailnet name sitez, address 100.99.180.19). `tailscale status` and `tailscale file cp --targets` read at
  2026-10-16T04:53:11Z: sitez listed, not marked offline, and listed as a Taildrop target.
- Receiving: site Z receives the pack on a SCRATCH target and deletes the scratch. That step, and the install, are a later
  issuer call to site Z's CTO. Nothing is installed or proven on site Z by this record.
- Command form, one call per file: `tailscale file cp "<file>" sitez:` (trailing colon). No `--name` flag is used.
- A Taildrop has no read receipt. A sent file is proven delivered only by site Z's own `tailscale file get` and
  `intake_receive.py verify` on site Z. This record does not claim delivery.
- Each file is sent AT MOST ONCE. A re-run of the test never re-sends.
- The release folder and the pack are the laptop's; no file was moved to site Z by any other route. The four files are
  the SAME four files sent to dell1 (see TAILDROP_RECORD.md), with the same SHA-256 values.

## Files to send (name, bytes, SHA-256 of the bytes to be sent)

| # | name | bytes | sha256 |
|---|---|---|---|
| 1 | MANIFEST.json | 638 | 3735d72d948ae63a65f8d7479df0c708fddacf25c37ea0a0e5da5abccf3c81b5 |
| 2 | tabulate-0.9.0-py3-none-any.whl | 35252 | 024ca478df22e9340661486f85298cff5f6dcdba14f3813e8830015b9ed1948f |
| 3 | tabulate-0.9.0-py3-none-any.whl.check.json | 7477 | 8178cfa9b6148528ebac81d54725ffbd061aca9b3168228dce4a94292b07add4 |
| 4 | tabulate-0.9.0-py3-none-any.whl.delivery.txt | 1666 | bc45f2c1d7df864386aea8bc3bb3d9adcf393d31dc7c24a1c70dfa524edfd7fd |

## Send log

Commands run, in this order, each once. Time is UTC, taken AFTER each command. Exit code is the `tailscale file cp`
exit code. Printed output is recorded on each row.

| time (UTC) | command | exit code | outcome |
|---|---|---|---|
| 2026-10-16T05:05:26Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261016-tabulate\MANIFEST.json" sitez:` | 0 | sent (row 1, no output) |
| 2026-10-16T05:05:44Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261016-tabulate\tabulate-0.9.0-py3-none-any.whl" sitez:` | 0 | sent (row 2, no output) |
| 2026-10-16T05:06:07Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261016-tabulate\tabulate-0.9.0-py3-none-any.whl.check.json" sitez:` | 0 | sent (row 3, no output) |
| 2026-10-16T05:06:26Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261016-tabulate\tabulate-0.9.0-py3-none-any.whl.delivery.txt" sitez:` | 0 | sent (row 4, no output) |

Files sent: 4 of 4. Files failed: 0. Target: sitez.

Delivery status: NOT YET PROVEN. A zero exit code means each file reached sitez's Taildrop inbox. It does not show that site Z
has read it. The issuer asks site Z's CTO to run `tailscale file get` and `intake_receive.py verify --from <folder>` on site Z
and to report the result back. This record does not claim delivery.
