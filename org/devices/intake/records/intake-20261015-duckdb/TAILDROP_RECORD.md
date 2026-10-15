# TAILDROP RECORD -- intake batch intake-20261015-duckdb (round 22, CT-al-4)

Written by 0.9.0_WK_NFRA_CTLPLN~122 (lane 2.0.0_SA_COO~D1 receives on dell1). This record names files and hashes only;
it holds no file content. The payload itself travelled by Taildrop from the laptop staging folder and is not in git.

- Staging folder (outside every git tree): C:\Users\AndrewBerman\tdrop\out\intake-20261015-duckdb
- Target: dell1 (tailnet 100.79.95.44). `tailscale status` read before sending: dell1 listed, not marked offline.
- Command form, one call per file: `tailscale file cp "<file>" dell1:` (trailing colon). No `--name` flag was used.
- A Taildrop has no read receipt. A sent file is proven delivered only by dell1's own `tailscale file get` and
  `intake_receive.py verify`, which the issuer asks of dell1's manager next. This record does not claim delivery.
- Each file is sent AT MOST ONCE. A re-run of the test never re-sends.

## Files sent (name, bytes, SHA-256 of the bytes sent)

| # | name | bytes | sha256 |
|---|---|---|---|
| 1 | MANIFEST.json | 660 | f18d1f6ad402411228467a9487db8f3ba5dee5880a9247e1f907ae0428f12306 |
| 2 | duckdb-1.5.0-cp314-cp314-win_amd64.whl | 13575130 | 11ae50aaeda2145b50294ee0247e4f11fb9448b3cc3d2aea1cfc456637dfb977 |
| 3 | duckdb-1.5.0-cp314-cp314-win_amd64.whl.check.json | 7449 | 1eba2d9343abe75bbdb7af48f064c563f95fe06f05dcdc73f2f1f7995f397113 |
| 4 | duckdb-1.5.0-cp314-cp314-win_amd64.whl.delivery.txt | 1618 | 9e1d06e637be326971f473419f21ffe7aac508a1c2b4d961d311b6e3ebec8073 |

## Send log

Commands run, in this order, each once. Time is UTC from `date -u` before the call. Exit code is the `tailscale file cp`
exit code. Printed output was empty on every call.

| time (UTC) | command | exit code | outcome |
|---|---|---|---|
| 2026-10-15T20:24:27Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261015-duckdb\MANIFEST.json" dell1:` | 0 | sent (row 1) |
| 2026-10-15T20:24:27Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261015-duckdb\duckdb-1.5.0-cp314-cp314-win_amd64.whl" dell1:` | 0 | sent (row 2) |
| 2026-10-15T20:24:28Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261015-duckdb\duckdb-1.5.0-cp314-cp314-win_amd64.whl.check.json" dell1:` | 0 | sent (row 3) |
| 2026-10-15T20:24:28Z | `tailscale file cp "C:\Users\AndrewBerman\tdrop\out\intake-20261015-duckdb\duckdb-1.5.0-cp314-cp314-win_amd64.whl.delivery.txt" dell1:` | 0 | sent (row 4) |

Files sent: 4 of 4. Files failed: 0. Target: dell1.

Delivery status: NOT YET PROVEN. Taildrop gave exit 0 for each send, which means the file reached dell1's Taildrop inbox. It
does not show that dell1 has read it. The issuer asks dell1's manager to run `tailscale file get` and
`intake_receive.py verify --from <folder>` on dell1 and to report the result back.
