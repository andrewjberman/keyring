# NFRA_CTLPLN decomposition -- round 18: one batch -- the sparse set proven under safe-commit, the absolute-path in-use match, the link kept as a link (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round17.md` (1.0.0_SA_CTO, @8b52525b29) sections 2-3; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND17.md` and `ROUND17_INPUTS_FOR_ROUND_ANALYSIS.md`. **PRD:** unchanged. **Process facts in force:** every worker face carries the early-commit and named-VALID-instance lines; each worker worktree is removed at its merge by the CTO's definition (now by `worktree_gc.py --go --only`, a relative path); the worker's worktree is cut by the NEW `wk-provision.sh` (sparse by default), the first real use of the recipe.

## Cells

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-ah-1` | ONE batch of three: (a) the base sparse set holds `.tools/`, `org/modules/graph/`, `org/devices/` and `infra/logic/registry/` (round 17 put them in; this cell proves it) and `safe-commit.sh` runs green inside a worktree cut by `wk-provision.sh`; (b) `S9126`: `worktree_gc.py` resolves `--only` and `--check-removable` paths before the in-use match and leaves its own process out of it; (c) the preserve step keeps a link as a link (a directory junction is recorded as a link entry, never followed), the symlink test skipped with its reason on WinError 1314. | FWD-2 | LOCAL (temporary repositories, plus one real sparse worktree with one throwaway commit, removed) | BATCH / 5 | `0.9.0_WK_NFRA_CTLPLN~105` (worker class `worker`) |

## Carried with an OWNER and the CONDITION that un-parks each

- **FWD-11:** a qualified wait on Andrew's word (open call `laptop-20261014T205216Z-7841`); cut FRESH in the round after he names the hour. **FWD-9:** PARKED. **FWD-27:** waits on Andrew's "another time".
- **`S9125`:** dell1, before 2026-12-31. **`S9119`:** read when a dell2 lane is live (owner `0.0.0_AB_MSTR~DELL2`). **`S9103`:** no cell. **`S9120`, `S9122`:** per the CVO. **`Z-S3`, `W12-S1`:** each function's next deploy. **`W89-S3`:** ADVI_FIRMBKTS's.
- **The plain `--go` (no `--only`) on the real repository:** not run as a test (CTO ruling 4); it is the drain's ordinary use under the new rules.
- **Close or park (CTO standing note):** before round 19 the CTO reads whether CTLPLN closes or parks its remaining waits and puts that to Andrew if so.

## Rule 24

**Domain:** the CTO's round-17 section 3 item 1 (the three bullets). One cell. **Same grain; one intent; disjoint write surface:** `CT-ah-1` writes `.tools/worktree_gc.py`, `.tools/wk-provision.sh` (only if the proof shows the base set short), and two tests. **State coherence:** no cell applies anything or calls AWS; the one real worktree it creates is removed; its one throwaway commit stays on a throwaway branch and is never merged.

## Dependency chains and fan-out

One chain. `fanout: 1 of 1 chains, cap 8, reason: one laptop worker cell, the CTO's batch`
