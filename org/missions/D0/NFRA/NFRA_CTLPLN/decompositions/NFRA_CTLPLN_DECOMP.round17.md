# NFRA_CTLPLN decomposition -- round 17: the preserve step and porcelain-only dirt in worktree_gc, the sparse worker checkout (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round16.md` (1.0.0_SA_CTO, @f62974941f) sections 2-3; CTO msgs 109361 (the `W100-S1` ruling) and 109364 (the sparse checkout); MSTR msg 109362 (disk). The issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND16.md`. **PRD:** unchanged. **Process facts in force:** every worker face carries the early-commit line and the named-VALID-instance line (round 16); remove each worker worktree at its merge by the CTO's definition (a clean `git status --porcelain`, an own commit, HEAD in a box branch); cut no worktree below 12G free on `C:`.

## Cells

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-ag-1` | `worktree_gc.py`: dirt means `git status --porcelain` only (gitignored files are not dirt); a merged worktree with dirt is `REMOVABLE-AFTER-PRESERVE` in `--check-removable`, and `--go` first commits that dirt to `preserve/<branch>-<stamp>` and prints the sha, then removes; a new `--only <path>` scopes `--go` to one worktree so the real run touches nothing else. Proof on planted trees; the issuer's one real `--go` follows at close. | FWD-2 | LOCAL (temporary repositories; the real run is the issuer's, scoped by `--only`) | CLEANUP / 2 | `0.9.0_WK_NFRA_CTLPLN~103` (worker class `worker`; cut as a SPARSE worktree by hand, the first real trial) |
| `CT-ag-2` | `wk-provision.sh provision` cuts a SPARSE checkout by default (the order's `<paths>` plus `.tools/`, `lib/` and the project's tree folder), a full checkout only with a stated reason; `/dispatch`'s recipe line says so. Proof: a real sparse worktree of this repository runs a real earlier cell's test green, and the sizes are printed against a full checkout. | FWD-2 | LOCAL (temporary repositories, plus one real worktree created and removed) | PROVISION / 1 | `0.9.0_WK_NFRA_CTLPLN~104` (worker class `worker`; a full worktree, because it builds the sparse recipe) |

## Carried with an OWNER and the CONDITION that un-parks each

- **FWD-11:** a qualified wait on Andrew's word (open call `laptop-20261014T205216Z-7841`); cut FRESH in the round after he names the hour. **FWD-9:** PARKED. **FWD-27:** waits on Andrew's "another time".
- **`S9125`:** dell1, before 2026-12-31. **`S9119`:** read when a dell2 lane is live (owner `0.0.0_AB_MSTR~DELL2`). **`S9103`:** no cell. **`S9120`, `S9122`:** per the CVO. **`Z-S3`, `W12-S1`:** each function's next deploy. **`W89-S3`:** ADVI_FIRMBKTS's. **`W100-S1`:** ruled (c) and disarmed by the CTO; `CT-ag-1` is its remedy.
- **The first real `--go`:** the issuer's, at close, against ONE real merged worktree of this round (a worker worktree after its merge, with one planted untracked file), scoped with `--only`. It is the CTO's done-when for the real run; it is not a worker's act.

## Rule 24

**Domain:** the CTO's round-16 section 3 items 1-2 (rulings 1-3). Both are cells above. **Same grain; one intent per cell; disjoint write surfaces:** `CT-ag-1` writes `.tools/worktree_gc.py` and two tests; `CT-ag-2` writes `.tools/wk-provision.sh`, `.claude/skills/dispatch/SKILL.md` (the one recipe paragraph) and one test. **State coherence:** no cell applies anything or calls AWS; `CT-ag-1` removes only worktrees of its own temporary repositories; `CT-ag-2` creates one real worktree and removes it.

## Dependency chains and fan-out

Two chains, no dependency among them. `fanout: 2 of 2 chains, cap 8, reason: two laptop worker cells with disjoint write sets and no shared dependency`
