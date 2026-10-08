# Process garbage collection and script ops -- program status (4.0.0_SA_CRO~B, 2026-10-08 ~18:4xZ)

Andrew's words, in order: records `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_{155x,162x,164x,173x}Z_*`.
Measured 18:4xZ: every commit below is in laptop `CLOUD`; push state LOCAL (`ls-remote origin CLOUD` = ec16835717;
0.0.0_AB_MSTR's push waits on site Z, msg 107106).

## Short term (Andrew's "Quick" list)

| Item | Commit(s) | State |
| --- | --- | --- |
| Reaper stops whole trees; catches replaced, orphaned, native and dead-session processes | c002dbb2d1 | landed |
| Reaper records every stop (KILL-MAINT lines) | b8c8b38c33 | landed |
| Hand-written Monitor ends itself at 29.5 min (/watcher Traps, 1770 s); /git-pull and /bbg-teams-assist bounded | 96cc4882fb, b8c8b38c33, 8773f12204 | landed |
| Session map: Claude Code + Codex session shells never killed; unattended mode with guards | f753d0fd22 | landed; the scheduled task is NOT installed ("A is better for now": /govern is the trigger) |
| One sweep per box | /govern Step 3a.6 (0.0.0_AB_MSTR) | asked of 0.0.0_AB_MSTR to switch it to `-Unattended` + worktree_gc (msg 17:52Z) |

## Long term (P1-P4, Andrew "3.) Yes approved")

| Package | Commit(s) | State |
| --- | --- | --- |
| P1 inbox watcher: one copy per serial, no lost mail on a dead pipe, no legacy respawn | d83396105d | landed |
| P1 agentbus consumer dies with its session; atomic lock; bounded fallback | f09ebfbd86 | landed |
| P2 broker exits with its last session; exit-code probe; exclusive bind | bce02db78e | landed |
| P2 poller one copy per serial, follows its seat | b54a8dcb93 | landed |
| P2 server.py parent watchdog (lane D0_T1_BROKER, applied by 0.0.0_AB_MSTR) | e6f1274d17 | landed |
| P3 safe_deploy_core temp dir | eabdf00e1f | landed |
| P3 safe-commit / safe-merge residue (5 items) | -- | handed to 4.0.0_SA_CRO~A (CTO 107031), 18:38Z |
| P4 warn-only Monitor hook | 0d812c87d2 | landed; **live proof 18:2xZ**: a `timeout 3600 bash -c 'sleep 10'` Monitor drew the hook's WARN as additional context and still started; a bounded inbox-watch Monitor drew none |
| Worktree removal (24 h clean / held for owner / 48 h escalation) | 0a1589acee, 9f4163885d (B5: box branches count as merged) | landed; run from /govern by 0.0.0_AB_MSTR |

## Live effect, and what is not yet proven

- A running seat picks up the watcher, poller and server changes only at its next re-arm or restart. Old copies run
  unchanged until then.
- The agentbus owner-tie is proven on stand-ins only. Its live proof is the next `/agentbus` arm printing
  `owner-tie ON`.
- The broker idle exit is proven on scratch ports only. Its live proof is a box with no seats for 10 minutes.
- The per-box rollout of the reaper rides /govern on each box; dell1, dell2 and site Z were not exercised by this seat.
