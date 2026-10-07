# ANDREW-DIRECT 2026-10-07 ~06:45Z-06:55Z -- site-Z disk cleanup: target 100-200 GB; "Go with your recomendations."

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z), in-session. Two messages.

## Verbatim

~06:45Z: "yeah we should be able to clean up 100gb+, id like to see us clean up 200gb if possible. we need to assess how
much we can get rid of on here because that severely hampers this box from proceeding as a workhorse."

~06:55Z, answering the assessment and its four numbered decisions: "Go with your recomendations."

## The recommendations he approved (as put to him, each with its stated recommendation)

1. Row 2 of the proposal: archive, then remove the idle git worktrees under `C:\tmp`. "I recommend yes." Method stated:
   tag any detached checkout so its commits stay reachable; save each worktree's uncommitted changes as a patch in one
   archive folder; leave alone anything written recently.
3. Shrink the page file from 64 GB: "I recommend 16 GB." Needs admin and a reboot, so it is his own act; the command
   is given to him.
4. Timing: "rows 1 and 2 now, before the reboot". Row 1 = remove the 4 fully merged worktrees (8 GB).
-  "One last push so tonight's handoffs are on origin": recommended yes in the two messages before.

## NOT covered (no recommendation was stated, so nothing is done)

2. The folder `Desktop\OPAL_BLOOMBERG_freeze_investigation_2026-07-30` (25 GB, 79 files): put to him as "delete or
   keep?" with no recommendation. It stays.
- Rows 5, 6, 7 (old `opal-pinned` pins, Claude scratch and package caches, `ajb_workspace\infra`): proposed, not put as
  decisions. They stay, and are re-asked with a recommendation each.

## How row 2 is carried out (narrower than proposed, on the safe side)

- Scope: registered worktrees whose path is under `C:\tmp` only.
- Live window 24 hours, not the 6 stated: every tree touched in the last day stays, so tonight's stopped rounds and the
  trees named in the seats' handoffs are untouched. This frees less than the ~110 GB quoted.
- Every removed tree gets a tag `archive/wt-20261007/<dir>` at its HEAD, a patch of its tracked changes and an archive
  of its untracked files, and a manifest row, under `Desktop\worktree-archive-20261007\`.
