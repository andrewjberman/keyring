# TAILDROP RECORD -- intake batch intake-20261016-tabulate (round 25, CT-ao-2)

Written by 0.9.0_WK_NFRA_CTLPLN~128 before the sends. This record names files and hashes only; it holds no file content.
The payload itself travels by Taildrop from the laptop staging folder and is not in git.

- Staging folder (outside every git tree): C:\Users\AndrewBerman\tdrop\out\intake-20261016-tabulate
  (`git -C` on the parent folder fails: not a repository).
- Target: dell1 (tailnet 100.79.95.44). `tailscale status` read at 2026-10-16T03:39:03Z: dell1 listed, not marked offline.
- Receiving: dell1 receives the pack on a SCRATCH target and deletes the scratch. That step is a later issuer call to dell1.
- Command form, one call per file: `tailscale file cp "<file>" dell1:` (trailing colon). No `--name` flag is used.
- A Taildrop has no read receipt. A sent file is proven delivered only by dell1's own `tailscale file get` and
  `intake_receive.py verify` on dell1, which the issuer asks of dell1's CTO next. This record does not claim delivery.
- Each file is sent AT MOST ONCE. A re-run of the test never re-sends.
- The release folder and the pack are the laptop's; no file was moved to dell1 by any other route.

## Files to send (name, bytes, SHA-256 of the bytes to be sent)

| # | name | bytes | sha256 |
|---|---|---|---|
| 1 | MANIFEST.json | 638 | 3735d72d948ae63a65f8d7479df0c708fddacf25c37ea0a0e5da5abccf3c81b5 |
| 2 | tabulate-0.9.0-py3-none-any.whl | 35252 | 024ca478df22e9340661486f85298cff5f6dcdba14f3813e8830015b9ed1948f |
| 3 | tabulate-0.9.0-py3-none-any.whl.check.json | 7477 | 8178cfa9b6148528ebac81d54725ffbd061aca9b3168228dce4a94292b07add4 |
| 4 | tabulate-0.9.0-py3-none-any.whl.delivery.txt | 1666 | bc45f2c1d7df864386aea8bc3bb3d9adcf393d31dc7c24a1c70dfa524edfd7fd |

## Send log

Commands run, in this order, each once. Time is UTC from `date -u` before the call. Exit code is the `tailscale file cp`
exit code. Filled in after each call.

| time (UTC) | command | exit code | outcome |
|---|---|---|---|

Files sent: 0 of 4 (not yet sent). Files failed: 0. Target: dell1.

Delivery status: NOT YET SENT.
