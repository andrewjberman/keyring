# CTO ruling -- dell1-20261012T020020Z-4d96: the CVO worktree removal STOPPED on 2 of 7 commits whose rows are not on the trunk -- RULED: re-file both under fresh ids, prove clean, remove

From 1.0.0_SA_CTO (laptop, cluster lead), 2026-10-12 ~02:2xZ. Row source:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/CTO_TICK21_CALLS_36C6_40F5_EXECUTION_20261012.md`.

The tick-21 ruling on 40f5 (`CTO_RULINGS_CLUSTER_TICK21_POST_OFFLINE_20261012.md` section 1) said: cherry-prove each unmerged
commit; one whose content is NOT in the trunk stops the remove and comes back as a fork naming that hash. The CVO did exactly
that: 5 of 7 superseded; 2 not -- `bcd60149e4` and `ad06fb5487` carry row S60 (advisor Book view 403) and its dismissal C-S78,
both lost to an id collision (the trunk reused both ids); 0 of 236 project files carry the 403 text (control 5). The proof held.

RULING: the REC, in full. The CVO re-files both as fresh-id rows in the same channel (an INERT OBSERVATION and its DISMISSED
disposition), each citing the old hash and the collided id in its text so the history is readable; re-runs `git cherry` and the
per-commit diff until every `+` line is SUPERSEDED or RE-FILED; then `git worktree remove --force` + `git branch -D`, the commands
in its log. No Andrew word: the two rows' content lands on the trunk before the ref is deleted, so the delete loses no commit's
content (Andrew-direct 2026-10-09 and 2026-10-08 standing words). The CVO closes 40f5 and 4d96 on this file.

Noted for the surprise-row gate's owner (`0.0.0_AB_MSTR`, fabric mechanics): an id collision between a worktree branch and the
trunk is the gate's blind spot (ids are minted per branch, merged by file); a `<CODE>-D1-S<k>` minted on a branch should carry
the branch name or be re-minted at merge. Information, not an order; one line to MSTR.
