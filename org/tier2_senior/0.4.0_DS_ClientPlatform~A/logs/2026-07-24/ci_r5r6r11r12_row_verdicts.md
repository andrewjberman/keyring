# CI-R5R6R11R12 — closure rows 5, 6, 11, 12 (P0)

**archetype:** IMPLEMENT
**Agent:** `0.4.0_DS_ClientPlatform~A` · 2026-07-24 · **TO:** `MDPF_CHANNEL_INDEPENDENCE.CI-R5R6R11R12` @`53efddff35`
**Commits:** `38b4569f0` (row 11, pushed) · `adfd8c327` (rows 5+6) · deliverable/log this pass
**Authorization:** Andrew-direct ~1720Z *"Go now, this is P0."*

## Outcome

| row | verdict | live? |
|---|---|---|
| 5 | TRUE-BUT-NOT-LIVE | ❌ |
| 6 | TRUE-BUT-NOT-LIVE (W-7 half routed to CTO) | ❌ |
| 11 | TRUE-BUT-NOT-LIVE | ❌ |
| 12 | **NOT-YET-TRUE** (gate case — portal promote blocked) | ❌ |

Every verdict rests on an **exercise**, never on a citation of my own prior measurement — the TO's sharpest
constraint was aimed exactly there. Full detail in the deliverable.

## The thing that mattered most

**The mdpf repo→runtime path is unowned and uninstrumented.** Chasing "if a push can't deploy mdpf, what does?"
found the EC2 runner syncing from `s3://opal-data-mdpf/code/scripts/`, whose deployed copy is **51,999 B
@2026-07-21** against a **119,499 B** HEAD with **zero occurrences** of every mechanism these rows touch, on a
runner whose telemetry stops 2026-07-18 (calendar-resolved: five trading days, not a weekend artifact). COO
re-measured independently and added the depth — 20 commits, +67,500 bytes, plus a **fail-open** where a missing
Stage 6 is a non-fatal WARN while a missing feeder is FATAL. Escalated P0.

Consequence I applied to my own work without softening it: **rows 5, 6 and 11 are built, exercised and running
nowhere.** A closure report counting them true would be *true about a file and false about a runtime*.

## Two process findings

1. **`safe-deploy` uploads the WORKING TREE, not the committed blob** (`safe_deploy_core.py:594-595` →
   `deploy_file:193`). The range picks the FILES; the DISK picks the CONTENT — and the ETag check compares
   local disk to S3, so a dirty-tree deploy passes it perfectly. My tree was dirty when COO nearly pushed.
   Real for every bd/inf/cot deploy. Gate candidate: refuse a push unless deploy-scope files are clean vs HEAD.
2. **The author/deployer split opens a window** between "author says green" and "COO pushes" in which the
   author can silently invalidate their own green. I closed mine by freezing edits — *which works because I
   noticed*, and that is not a control.

## My own error, recorded

Removing the dirty-tree hazard, my backup `cp` to the scratchpad **failed and I ran the destructive restore
anyway**, destroying ~an hour of rows 5/6 work. A destructive step executed without verifying the safety step
landed — the exact class I spent the day flagging in others. Nothing shared was affected; rebuilt from scratch.
`git stash` was correctly **blocked by a gate** (it parks every agent's dirty files in a shared worktree).

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| `.tools/commit-gate.sh` | on the producer, twice | **CAUGHT A REAL DEFECT**, then clean | An unused `ad_stamp_as_of` on the inflection leg — meaning that leg's stamp would have stayed silent. Fixed rather than silenced. Best tool outcome of the session. |
| `comp-pipescript io` | `dim_mdpf_aggregate_aua_timeseries.py` | PASS | Re-confirmed the `WRITES: (none detected)` gap. |
| `comp-pipescript deployed` | same script | **NO COVERAGE** | Sweeps `opal-data-bd` only — "No scripts matched filter". The mdpf tree has **no deployed-vs-repo instrument at all**, which is why the 20-commit drift was invisible. Reported, not treated as a pass. |
| `comp-validate` | same script | **NO_CONFIG** | Configs exist for BD + INF only. Per CLAUDE.md, NO_CONFIG = UNVALIDATED; never signalled SAFE on it. |
| `.tools/deploy_ledger.py` | open / close-leg ×3 / close | CLOSED 3/3 | Opened pre-push per NEVER#6; closed honestly once verified no deploy was possible — L1 as **STRUCTURALLY-NOT-APPLICABLE**, not as done. |
| ad-hoc gold dry-run | `--firm 49financial`, `--firm all` | clean; both guards fired | Used to **EXERCISE** per amended NEVER#4 @`7d2b8cf6f`; artifacts explicitly **not** cited as production evidence. |
| `s3api` / `git show <ref>:<path>` | deployed-vs-repo census, PROD render read | PASS | Controls on every retrieval (line counts) so a zero-match is a real absence, not a broken read. |

## Interfaces

Roster consumption contract agreed with `0.7.0_AE_CloudOps~B` **before either side built** (CTO addendum).
They corrected one thing I had wrong — cadence is per **feed**, not per partner — and expose `expected_frontier`
so their row-8 lag and my row-6 as-of are one call site twice. I verified their module and their inflection
correction myself rather than inheriting it. Rows 5/6 as built do not yet consume it; that wiring is the
remaining half.

## Next

Claimed **row 14** (the self-referential import — my GC-W2a/W-2b arc finishing), with the limit stated up
front: it heals **forward**, it does not recover the 20 historical dates (GC-W2b graded those
NOT-DERIVABLE-FROM-RETAINED-SOURCES). W-7's delete-vs-declare is at CTO's gate. Commits await COO's push.
