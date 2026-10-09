# 2.0.0_SA_COO~MI -- post-reboot drive, NFRA_MCPINDEX round 8 -- 2026-10-09 07:0xZ-07:3xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Startup

- `/watcher` armed (script pid 29524, re-armed at expiry 07:3xZ). Delivery ledger: 19 rows since 00:00Z, 18 READ; 32474 opened and
  acked. 32485 (CTO~O, v0.8 FWD-19) acked.
- `/canonical-drive NFRA_MCPINDEX` re-armed off the LIVE_ARMS `1.0.0_SA_CTO~O` pair row (30m, `16,46 * * * *`, session cron).

## Ticks

| tick | project | limb | round | TOs t/T | thread | act fired |
|---|---|---|---|---|---|---|
| 07:1xZ | NFRA_MCPINDEX | L7 EXECUTING (FULL) | 8 | 0/4 -> 1/4 | n | DRIVE FORWARD: MX-d-7 re-graded on its branch (d7.AC1 3/3 tests; AC2 3/3 datasets as-of equal, claim measured; AC3 routing 24/27, floor 24), proof VALID; drained @e9545d6823. ~29 re-seated for MX-c-6's close |
| 07:24Z | NFRA_MCPINDEX | L7 | 8 | 1/4 | n | in flight: ~29 merged box/sitez @f8bf16549e |
| 07:3xZ | NFRA_MCPINDEX | L7 | 8 | 2/4 | n | DRIVE FORWARD: MX-c-6 re-graded (c6.AC1 29/29, AC2 3/3, AC3 4/4 sets, 0 unknown), proof VALID; drained @dc3435a65f. Rows ruled (Z-S86 @27b37e99b3). MX-d-8 issued to ~28, worktree fast-forwarded to 27b37e99b3 |

## Rulings (Z-S86 @27b37e99b3)

- Z-W28-S3, Z-W29-S2 (BLOCKING): DISARMED by the box/sitez merges carrying the ADVI_BILLING index fix.
- Z-W28-S1, Z-W28-S2: CONFIRMED under contract 4. A silver row has no served artifact, so `absent` is the true answer.
- Z-W29-S1: CONFIRMED. The next catalog cell's face names the worktree's own tracked census as `--census-dir`.

## Open

- MX-d-8 (WORLD) with worker ~28; then MX-r-9 (release via `2.0.0_SA_COO~O`, PHASE B by a fresh site-Z CloudOps lane).
- NFRA_MCPINDEX v0.8 FWD-19 @0eff9e0e6d: ratified half STALE, owed by `3.0.0_SA_CVO~Z`. Round 9 is cut on the sign. dell2 was told
  via `0.0.0_AB_MSTR~Z` (07:21Z): drain target 2026-10-12 holds.
- Time-windowed obligations from the wind-down log stand: MX-s-19 after 2026-10-13 03:00Z; J1 after MX-r-9 AC2/AC3.
- Worktree `wk-mcpindex-r8-29` and branch `wk-NFRA_MCPINDEX-29` (merged) are not removed. Removing the worktree
  deletes its untracked `.scratch/` recursively, which needs the operator's word.

## Compiler Tools

- `comp-surprise --project NFRA_MCPINDEX --json`: 254 investigation items, 17 open, 15 armed (849 files). The rail refused a piped
  form (R6), so the census went to a file.
- `safe-merge.sh` x2: fast lane, 0 of 5 and 0 of 35 paths graded (no both-sides change); tree and index checks clean.
- `proof-of-spec-check.py` x2: VALID. `prd-signoff.py status`: WITHHELD (ratified STALE).
- Gap: `to-check.py --all --assignee 2.0.0_SA_COO~MI` printed the whole order set, so it did not answer what this lane holds.

Push state: LOCAL on box/sitez. origin box/sitez read bb2e9e4a05 (ls-remote 07:36Z).
