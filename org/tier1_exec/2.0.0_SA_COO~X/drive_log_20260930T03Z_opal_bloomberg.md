# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 03Z (host opal_bloomberg)

| time | limb | round | TOs | act |
|---|---|---|---|---|
| 02:58Z-03:14Z | L6 | 20 | 0/2 | DRIVE FORWARD: round-19 analysis `d5d806bc2e` became ONE issuance, `cba74cc4a0` (merged `9c4b54d1f8`); v-1 went to `~1` (worker-light), v-2 to `~2`, and v-3 is dependent. The Andrew-direct worktree record `8c4f79e531` was committed after a peer's AMGT_HARVST merge cleared, and `1.0.0_SA_CTO~Z` was told. |
| 03:20Z | L7 | 20 | 0/2 | NO-OP: both workers in flight; the 02Z log was committed (`e861cfaced`) |
| 03:24Z | L7 | 20 | 1/2 | DRIVE FORWARD: v-1 re-graded and merged (`f1d007b743`); drain hygiene: 139 passed |
| 03:43Z | L8 | 20 | 2/2 | DRIVE FORWARD: v-2 re-graded and merged (`2d5205bf57`); the cause of the page half read by this seat (0 portal files consume `dossier_fields`, controls 3 and 61); the real run; packet `0f953c0312` to `3.0.0_SA_CVO~Z`; `wk-crps20-1/2` removed, branches kept |
| 03:5xZ | -- | 20 | -- | round-20 analysis `609100db54` (msg 26888) and addendum `7708a8506f` (msg 26893) READ-acked; the round-21 cut began (issued 04:0xZ, `ae80fa8457`, merged `71a9e708d7`) |

## Rulings at L5 this hour

- v-1: the census covers the ruling's root AND the defect's own root. The named root alone passes with the named defect in
  place.
- v-2: the pages per outcome were chosen from round 14's measurements. The signed-out control came first.
- w-1: "the files the fold actually read" means the picked A/B reports, not every report row.
- w-3: the AC demands no fact resolve; "never guessed" admits an honest 0 of 9.

## Compiler Tools

- `to-pipeline-gate.py` (via safe-commit): rounds 20 and 21 issuances admitted, no refusal.
- `safe-merge.sh`: 4 merges, each graded on its MERGED index; 0 collisions; v-2 appended one row (`Z-W2-S15`).
- `proof-of-spec-check.py`: v-1 and v-2 VALID on this seat's re-run.
- `git -C portal grep` at DEV: the page-half cause (0 consumers of `dossier_fields`), with non-zero controls on the same read.
- Gap: a Bash call carrying a recursive `grep -rl` was DENIED whole by the comp-tool rail. Re-run with native Grep.
