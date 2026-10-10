# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~ZZ, 2026-10-10 20:5xZ-23:3xZ (site Z, after the reboot)

**archetype:** COORDINATE

| time (Z) | limb | act | evidence |
|---|---|---|---|
| 20:5x | startup | /watcher, org/XXX.md A-E; lease FULL; no LIVE_ARMS row for ~ZZ, so no loop armed | -- |
| 21:02 | L8/L10 | The CVO's round-12 compile sat uncommitted in the shared tree after the reboot, and no slug had gone; one ask to 3.0.0_SA_CVO~Z. It landed with the slug | `852f1790dd`, msg 33010 |
| 21:05 | real run | `d2_mail_day` 10-09: listed 42, fetched 1, refused `body_no_andrew`; 10-10: listed 246, fetched 0. Z-S5's zero was organic | row Z-S7 `e2d48593a5` |
| 22:51 | nudge | The CTO had read the slug at 21:10Z with no analysis; one ask | msg to 1.0.0_SA_CTO~Z |
| 22:55 | L10 | Round-12 analysis received: E1 driven mail, E2 pin the five, E3 channel_poll | `82f10ddf63`, msg 33048 (acked) |
| 23:2x | L5/L6 | Round 13 cut in ONE issuance: CA-e-2 (~6), CA-e-3 (~7) worker-light; CA-e-1 has no worker chain. Checks dry-run at base `a89f5575b1`: 3 FAIL as expected, 3 bounds PASS | `e87fa72a49`; `fanout: 2 of 2 chains, cap 8` |
| 23:2x | L7 | Worktrees cut from HEAD; both workers spawned | branches `wk-comm_assist-13-6`, `-7` |
| 23:25 | route | E1's send: no seat holds a non-Andrew Opal sending identity (irpt/graph/app-registration absent; gateway Graph is delegated, this seat is Andrew). Per the analysis, the row goes to Andrew: one ask via 0.0.0_AB_MSTR~Z | row Z-S8 |

## Finding worth keeping

**A check's ROOT depth is part of the check.** All three new checks first died on `No module named 'data'`: the checks folder
sits nine levels below the repo root, and I wrote eight. A dry-run at the base caught it in seconds, which is what the
dry-run is for. A check that dies on import never reaches its own FAIL line. Read the base output's ARM lines, never only
the exit.

## Compiler Tools

- `comp-find` census of Opal-domain addresses: 2814 hits across 70450 files; the sender candidates were `opalbloomberg@`,
  `ops@`, `svc-*`. `comp-find 'sendMail'`: 5 hits, all in the delegated gateway.
- `comp-which` on the sending-identity question: no curated rule matched (the catalogue does not cover it).
- `prd-signoff.py status COMM_ASSIST`: ADMITTED (ratified-text SIGNED, brief auto).
