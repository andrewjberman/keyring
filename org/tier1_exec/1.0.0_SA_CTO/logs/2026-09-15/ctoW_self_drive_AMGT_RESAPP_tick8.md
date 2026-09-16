# /self-drive AMGT_RESAPP -- tick 8 -- 1.0.0_SA_CTO~W -- CARD 17 WITHDRAWN

**State:** ARMED. **Ticks covered:** 8. **Previous log:** tick 7 @`981b8bc234`.

## What happened

Tick 7 ruled `3.0.0_SA_CVO~W` DEAF (card 17) and routed a seat remedy to `0.0.0_AB_MSTR~Z`. **That conclusion was wrong and is
withdrawn** (card 18, `CTO_ADJUDICATION_AMGT_RESAPP_20260915T225xZ.md`; superseding ledger row 16). The routing message was never sent --
`0.0.0_AB_MSTR~Z`'s stop (msg 23276, 22:43:55Z) arrived first -- so no seat acted on it.

**The seat is working.** Measured by this lane at 22:45:56Z:

| instrument | reading |
|---|---|
| `3.0.0_SA_CVO~W`'s own worktree `C:/tmp/cvo-amgt-r11-20260915` (`a35563e197`) | 8 STAGED paths: `prd/stamps/L8.r11.json`, `L9.r11.json`, `L10.r11.json`, `ADJUDICATION_v11.md`, `REMEDIATION_v11.md` (the slug), modified `REMEDIATION_v10.md`, CVO AUDIT and VERIFY json; newest files 22.5 min old |
| MSYS `ps` | pids 5658 (22:23:18Z) and 6077 (22:23:28Z), both `.tools/safe-commit.sh` under `3.0.0_SA_CVO~W <...>` |
| `0.0.0_AB_MSTR~Z` peek (`unstick.ps1 -Peek`, screenshot, no keystrokes), msg 23276 | the seat's TUI: "Working (34m 22s - esc to interrupt)", waiting on that safe-commit |

## Why tick 7 was wrong

Card 17's four arms -- the seat's `read/` cadence, the two untaken messages, the author-anchored commit stop, the nudger's deduplicated
log -- **all observe a turn ENDING.** A seat inside one long turn produces that signature by construction: it does not poll, does not
archive, and cannot commit until its commit returns. Four arms, one plane. That is Rule 22's shared-dependency blindness, and the spread
of instruments read as breadth while being a single view.

⛔ **The aggravation is this lane's own.** The banked memory `a-live-pid-is-not-a-consuming-session-the-deaf-seat-tell` already carries
this exact false positive on a codex CVO seat, and says to check the seat's own tree for fresh work BEFORE a deaf verdict. This lane read
that file at 22:4xZ -- in the same tick -- and still ruled first and checked afterwards. **Reading the lesson is not applying it; the
check belongs before the verdict.** The memory is updated with this instance and with the discriminating instruments.

`2.0.0_SA_COO~W` measured correctly and took no act, routing instead of remedying. That restraint is the only reason there was a window.

## Where the goal stands

The round-11 slug is STAGED in the CVO's worktree and lands when that commit returns. This lane's L10 read starts then; its inputs are
ready (pre-read through the round close, candidates 1-16 with rulings, both CROs' research in). Completion test: NOT DONE, 0 of 1 projects
complete; REACHABLE 1, UNREACHABLE 0.

## Compiler Tools

| tool | used for |
|---|---|
| `git -C C:/tmp/cvo-amgt-r11-20260915 status --porcelain` + mtime walk | the 8 staged paths and their freshness |
| MSYS `ps -ef` on `safe-commit` | the two live commit processes under the CVO's author |
| `0.0.0_AB_MSTR~Z` msg 23276 (peek screenshot + its own ps read) | the seat's TUI state |
