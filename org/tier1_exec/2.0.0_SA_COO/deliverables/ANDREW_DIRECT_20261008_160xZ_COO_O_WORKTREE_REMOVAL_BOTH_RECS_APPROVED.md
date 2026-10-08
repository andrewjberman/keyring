# ANDREW-DIRECT 2026-10-08 ~16:0xZ (2.0.0_SA_COO~O terminal) -- the NFRA_OPLGTW worktree removal, both recs approved

## His words, VERBATIM AND ENTIRE

> "yes recs approved"

Given in answer to `/open-calls at your seta`, which he ran at this seat. The two cards as printed to him at 16:03Z:

**CALL 1 of 2.** "Force-remove the 11 drained NFRA_OPLGTW worktrees? (yes / no)". Context printed: `0.0.0_AB_MSTR~Z` asked
each COO to clear its drained worktrees (msg 31509); git refuses these without `--force` because each holds an untracked
`.scratch/` folder. REC printed: "Yes. Every commit is on CLOUD and on origin; only worker scratch files (2 to 73 per
tree) are lost, for about 19 GB."

**CALL 2 of 2.** "Remove the superseded release, rollback and stand-in trees too? (a) all but og-rb22 and og-rel24
(b) none". Context printed: 24 not-landed trees plus 5 drained trees that contain them, about 65 GB. REC printed: "(a).
Release commits stay on their rel-* branches; rollback trees for r20 to r27 are superseded by r28. Lost: 9 throwaway
stand-in commits and six trees' refused manifest edits. og-rb22 and og-rel24 stay while row Z-S67 is open."

## What it authorizes (his terms, not widened)

- `git worktree remove --force` of the 11 drained trees named in call 1's measurement
  (`C:/tmp/wk-oplgtw-` `r22-28`, `r23-22`, `r24-30`, `r26b-29`, `r24-29`, `r26-29`, `21-r21`, `26-r21`, `22-r21`, `r27-32`,
  `15-r19`).
- The same for call 2's set: the 14 release and rollback trees `C:/tmp/og-rb16` to `og-rb21` and `og-rel16` to `og-rel23`;
  the 9 nested stand-in clones (`x20`, `x23`, `x23b`, `x24`, `x25`, `x26`, `x27`, `x28`, `x28b`); the worker tree
  `wk-oplgtw-r27-31`; and the 5 drained trees that contain nested clones (`wk-oplgtw-15-r20`, `r23-28`, `r23b-28`,
  `r24-28`, `r25-28`).

## What it does NOT cover

- `C:/tmp/og-rb22` and `C:/tmp/og-rel24`: kept, by the REC he approved and by `1.0.0_SA_CTO~Z` msg 31517.
- The four worker trees still in use: `wk-oplgtw-r26-28`, `r28-33`, `r28-34`, `r30-35`. They were not on either card.
- Any branch. A worktree removal keeps its branch; no branch is deleted.
- Any other project's worktrees.

## Acts taken on it, same turn

- This record, then the broadcast to `0.0.0_AB_MSTR~Z` and `1.0.0_SA_CTO~Z`.
- The removals, each tree re-read first (HEAD, tracked changes) and the freed space measured.
