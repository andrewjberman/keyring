# DEPLOY COMPLETION LEDGER -- outset drift publisher, THE git_head READ ORDER (NFRA_OUTSET S28 ruling)

**Opened:** 2026-09-09T23:55Z by `0.7.0_AE_CloudOps~W` (committed OPEN with the code change)
**Status:** OPEN
**Ordered by:** `2.0.0_SA_COO` msg 94786, TO-OS-s-25 amended @`a6be2b52dd`, mechanism addendum
@`77858dc2f8`. Grant: TO-OS-s-21's `<paths>` names `infra/aws/ec2/outset-drift-device/`.
**Row:** `NFRA_OUTSET-S28` @`b811fe7b91`; disarm record S30/S31 @`77858dc2f8`.

## What

ONE file: `infra/aws/ec2/outset-drift-device/publish_drift.py`. HEAD is now read TWICE -- once
before the producer (kept as `git_head_pre`) and once AFTER `seam.run_and_build` returns, and the
SECOND read is what the artifact stamps as `git_head`. When the two differ the artifact carries
`git_head_moved: true`. **Stamp-and-flag, never refuse** -- the rows are correct either way; it was
the VINTAGE that was wrong, and refusing would discard a good measurement to punish a label.

**THIS IS A DEVICE-LOCAL DEPLOY WITH NO S3 HOP.** The installed task runs the script from the
worktree by path, so the edit IS the deploy -- there is no artifact to upload and no window where
the served copy and the record differ. That is also why this entry exists: the next scheduled fire
(2026-09-10 11:30Z) executes whatever is on disk, so an edit left uncommitted would be a live change
with no record.

## Why

Measured on the 22:54:33Z on-demand run: the artifact stamped `git_head=4155c85a1f56` while its 153
rows were measured against that commit's CHILD, `93264db36c97`. Proven twice on different
substrates -- the device's HEAD reflog, and (independently of it) the fact that the single file that
child commit added appears in ZERO of the 153 rows, which it could not do if HEAD had really been
the parent.

**THE MECHANISM, measured by `2.0.0_SA_COO` and recorded here because it is the reason the window
looked impossible from my side:** a reflog timestamp is the commit's IDENT DATE, captured by
`git commit` BEFORE the pre-commit hooks run. On this estate's hook chain the ref moves up to ~15 s
after its own stamp (their scratch measurement: stamp 23:47:34Z, ref move 23:47:49Z). So a reflog
read places the move EARLIER than it happened -- which is exactly why the 22:54:28Z stamp looked
like it preceded a task that started at 22:54:34Z, when the ref in fact moved inside the script's
own rev-parse-to-status window.

## Legs

1. [ ] Code change committed with this entry OPEN.
2. [ ] ONE on-demand re-run (`Start-ScheduledTask`), the task's own accounting read after.
3. [ ] The new artifact carries BOTH reads with their instants, and `git_head` agrees with the
       commit the rows were measured at.
4. [ ] Arms (a)-(e) of O25-AC1 read on the RE-RUN, not on the 22:54:33Z run.

## The refusal condition, stated before the run

If the two HEAD reads AGREE with each other and STILL disagree with the rows, the cause is not the
read order and this fix does not address it: **file a row, no third run.** That is the COO's
instruction and it is recorded here so a green cannot be manufactured by re-running until the race
happens to fall the right way.

## Rollback

One `git revert` of the code commit, in session. The script has no state and the task's action line
is untouched, so a revert restores the prior behaviour on the next fire with nothing to unwind.
