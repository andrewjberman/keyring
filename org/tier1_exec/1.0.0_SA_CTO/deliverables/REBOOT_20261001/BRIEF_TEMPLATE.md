# Reboot brief -- <FULL SERIAL> -- 2026-10-01

Write this in YOUR OWN deliverables folder as `REBOOT_BRIEF_20261001_<serial with ~ written as _>.md`, commit it with
`safe-commit`, and send its path and commit to `1.0.0_SA_CTO` in one message. Order:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md`.
The brief is what your successor reads FIRST, so write it for a session that remembers nothing. Plain sentences, absolute
or repo paths, commit hashes, UTC times. Keep it under about 80 lines.

## 1. Identity
- Serial, base folder, the project(s) this seat holds, its FAST lease(s) and their surfaces.

## 2. Where the work stands (one line per project)
- The outcome being driven, the last thing that landed (commit hash), the next act, and who or what it waits on.

## 3. Open acts that must survive the reboot
- Every ledger entry this seat holds open in `org/critical_paths/` (path, legs closed and open). For each: why it is SAFE to
  hold across a reboot, or the act you complete or roll back BEFORE you stop. Nothing is left half-landed.
- Every worktree this seat owns (path, branch, head) and whether it holds uncommitted work. Commit or stash it now.
- Clocks this seat must read after the reboot (scheduled runs, with UTC times).

## 4. Owed
- What this seat owes another seat or Andrew, with the asking message id. What others owe this seat, with message ids.
- Signed halves outstanding: packets waiting on another signature.

## 5. Relaunch
- RESPAWN: yes or no, with one line why (a seat with nothing open may stay down).
- The first three things the successor does, in order.
- The `--say` hint, which names only what to READ (this brief's path, its inbox), never what it owns.

## 6. Not done and not known
- Anything you started and did not finish, and anything you believe but did not measure.
