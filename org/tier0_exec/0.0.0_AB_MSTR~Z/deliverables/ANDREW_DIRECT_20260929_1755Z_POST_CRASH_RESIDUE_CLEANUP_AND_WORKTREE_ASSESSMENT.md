# ANDREW-DIRECT 2026-09-29 ~17:55Z -- post-crash residue cleanup + worktree assessment before workflows restart

**Channel:** Andrew, in the 0.0.0_AB_MSTR~Z Claude Code session (site Z), 2026-09-29 ~13:55 ET.
**Recorded by:** 0.0.0_AB_MSTR~Z, same turn.

## Verbatim

> "bring on CTO~Z and CTO~O and their underlying COOs that were active at the time of the crash. I want to restart
> their workflows, but before doing so, I think that they must have an edict to clear out any residue and tie up any
> loose ends that may have resulted from the unexpected crash. Then I want them to go through and actually asssess
> what worktrees they need/don't need, because I would imagine them and their CVOs, CVO~Z and CVO~O who we also need
> to spawn, would be able to assess based on /canonical-flow positioning per project what was actually needed versus
> can be disposed of."

## Seats (MSTR~Z's measurement of "active at the time of the crash", not Andrew's list)

Site-Z exec seats alive at the 11:34 ET crash (spawn audit `org/mcp/agent-spawn-audit.log` + commits 08:00-11:35 ET):
1.0.0_SA_CTO~Z, 1.0.0_SA_CTO~O, 3.0.0_SA_CVO~Z, 3.0.0_SA_CVO~O, 2.0.0_SA_COO~Z (10 commits), ~H (8), ~D (8), ~X (4),
~MI (3), ~O (2). Not included: COO~MP (last commit 02:17 ET) and COO~AI (03:12 ET), idle at the crash; COO~P/~Y/~M are
laptop seats.

## Order, in Andrew's sequence

1. Clear out crash residue and tie up loose ends the unexpected crash may have caused -- BEFORE restarting workflows.
2. Assess which worktrees each project needs vs can dispose of, by `/canonical-flow` positioning per project, with the
   CVOs (CVO~Z, CVO~O).
3. Then restart workflows.

## Context the seats need (facts, measured by MSTR~Z / 4.0.0_SA_CRO~Z today)

- Incident brief: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SITE_Z_CRASH_20260929/README.md` (CRO local commits
  6adad7bfe6, f319f5722c, 06b8f3c8ab). Disk full from ~10:30 ET; probable SentinelMonitor driver deadlock 10:47 ET;
  forced crash 11:34 ET; reboot 11:39 ET.
- Known crash damage: `C:/tmp/wk-crps14-5` checkout has 145 missing + 35 zeroed tracked files (COO~X, AMGT_CORPUS r14).
  Main repo `git fsck` and broker SQLite passed.
- MSTR~Z removed 71 non-live worktree CHECKOUTS on Andrew's word (branches kept; 5 detached HEADs pinned under
  `refs/archive/wt-20260929/`; `.scratch/` archived to `.runtime/crash-investigation-20260929/wt-scratch-archive/`).
  Record + manifests: `.runtime/crash-investigation-20260929/MSTR_RESIDUE_TABLE.md`, `mstr-reclaim-go.jsonl`,
  `mstr-reclaim-drained-go.jsonl`. A worktree a seat expected may be gone: recreate from its branch
  (`git worktree add <path> <branch>`), never from memory.
- 57 linked worktrees remain (22 undrained recent AMGT/NFRA checkouts among them) -- these are the assessment's subject.
- Python: `python` resolves to Python311 again (Python314 PATH entries and its MSI "Add to Path" product removed).
- Disk at 13:48 ET: 122.46 GiB free of 473.71 GiB.

## Scope note

This record relays Andrew's order; it adds no gate. Disposal of a worktree carrying commits or edits found nowhere
else stays with the project's owner, as `/cleanup` policy already states.
