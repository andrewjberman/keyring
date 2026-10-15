# NFRA_CTLPLN decomposition -- round 16: the "merged" test for a worktree's removal, the round scope of round-close-check, the placement-refusal batch (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round15.md` (1.0.0_SA_CTO, @0be7eb664c) sections 3-4; CTO msg 109345 (cell 1 also covers `.tools/worktree_gc.py`); the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND15.md` and `ROUND15_INPUTS_FOR_ROUND_ANALYSIS.md`. **PRD:** unchanged. **Process facts adopted (analysis ruling 2):** every worker face carries two lines: commit a work-in-progress commit as soon as a file exists; copy a proof instance's field names from a named VALID instance.

## Cells

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-af-1` | The drain-cleanup "merged" test (ruling 1, msg 109345): `.tools/worktree_gc.py` counts a worktree as merged only when its branch carries at least one commit of its own and HEAD is in the trunk or a box branch; a worktree with no own commit (UNSTARTED) is never removed; a new verb `--check-removable <path>` is the drain's mechanical test (own commit, in trunk, clean status). Negative control: a branch at its issuance commit. | FWD-2 | LOCAL (temporary repositories only) | CLEANUP / 1 | `0.9.0_WK_NFRA_CTLPLN~100` (worker class `worker`) |
| `CT-af-2` | `round-close-check.py` scopes an order to a round by the decomposition document its `<decomp_ref>` names (`...DECOMP.round<N>.md`), falling back to its `<round>` tag only when it names none (ruling 4). | FWD-2 | LOCAL | ROUNDCLOSE / 1 | `0.9.0_WK_NFRA_CTLPLN~101` (worker class `worker-light`) |
| `CT-af-3` | ONE batch of one: `W99-S1`, the placement-refusal branch of the naming stage in `.tools/safe-commit.sh` unstages every path this call staged, the twin of `W93-S1`. | FWD-2 | LOCAL | BATCH / 4 | `0.9.0_WK_NFRA_CTLPLN~102` (worker class `worker-light`) |

## Carried with an OWNER and the CONDITION that un-parks each

- **FWD-11:** a qualified wait on Andrew's word (open call `laptop-20261014T205216Z-7841`); the restart is cut FRESH in the round after he names the hour. **FWD-9:** PARKED. **FWD-27:** waits on Andrew's "another time".
- **`S9125`:** dell1 (ADVI_FIRMBKTS / the INF pipelines), before 2026-12-31. **`S9119`:** read when a dell2 lane is live (owner `0.0.0_AB_MSTR~DELL2`). **`S9103`:** the kit provider mirror, no cell. **`S9120`, `S9122`:** per the CVO. **`Z-S3`, `W12-S1`:** ride each function's next deploy. **`W89-S3`:** ADVI_FIRMBKTS's.
- **The `kill-maint` interim dry-first rule:** `0.0.0_AB_MSTR`'s to lift (analysis ruling 5); no cell.

## An ambiguity the issuer states rather than resolves

Ruling 1 says "a worktree with a dirty `git status --porcelain` is never removed", and also that Andrew's standing word ("Force-removing merged worktrees is mandatory", 2026-10-08 ~23:0xZ) is unchanged. `worktree_gc.py --go` today force-removes a MERGED worktree that is dirty and idle 24 hours. `CT-af-1` therefore applies the dirty-status test to the new drain verb `--check-removable` only, and changes `--go` in one respect only (no own commit means never removed, clean or dirty). The MERGED force path of `--go` for a worktree WITH an own commit is left as it is. If the CTO meant `--go` to stop force-removing dirty merged worktrees, that is a one-line follow-up cell; the cell files a surprise row stating the choice.

## Rule 24

**Domain:** the CTO's round-15 section 4 items 1-3 and msg 109345. Every item is a cell above or a carried line with an owner and a condition. **Same grain; one intent per cell; disjoint write surfaces:** `CT-af-1` writes `.tools/worktree_gc.py` and one new test; `CT-af-2` writes `.tools/round-close-check.py` and one new test; `CT-af-3` writes `.tools/safe-commit.sh` and one new test. **State coherence:** no cell applies anything, makes an AWS call, or removes a real worktree; the removal arms run on temporary repositories.

## Dependency chains and fan-out

Three chains, no dependency among them. `fanout: 3 of 3 chains, cap 8, reason: three laptop worker cells with disjoint write sets and no shared dependency`
