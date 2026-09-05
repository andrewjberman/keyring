# 1.0.0_SA_CTO -- 2026-09-03 16:00-16:25Z -- S28: a session id is not a seat

Inputs (READ-acked): 2.0.0_SA_COO /drive tick 4 (93779) and 0.0.0_AB_MSTR's routing (93781) on row NFRA_COMPEFFICACY-S28
(0.8.0_AE_CloudComp~H): Codex children launched from one Claude seat inherit its CLAUDE_CODE_SESSION_ID, so comp-to's
per-session .to_id file was last-writer-wins across the ten round-6 lanes (the COO's own file read T-17, a value it never
set); the .serial identity file untouched (identity comes from OPAL_AGENT_SERIAL first, set per child by the launcher).

## Acts
1. THE KEY (comp-to, comp-which, comp_log_auto): per-session files keyed <sid>.<serial>.to_id / .route when
   OPAL_AGENT_SERIAL is set; comp_log_auto reads that key first, the bare <sid> key second (legacy); one derivation
   (_seat_session_key) shared by the readers. Exercised: two seats under one sid -> two files, each resolving its own
   task order; files cleaned. Fixes every existing lane on its next comp-to call, no relaunch.
2. THE LAUNCHER (start-codex-seat.ps1): a fresh GUID per child as CLAUDE_CODE_SESSION_ID after the orphan-cleanup hook,
   and org/mcp/sessions/<guid>.serial written, so the session-keyed identity tier resolves for Codex seats; parses
   clean; binds the next launch. 06_current_state recompiled (comp-* sources).
3. Two index-lock races with other seats' commits on the shared worktree; the commit landed on the waited retry
   (hash in the repository, not in this seat's stdout).

## Open, with owner
- 2.0.0_SA_COO: its own stale .to_id under the shared sid clears on its next comp-to call.
- 3.0.0_SA_CVO: S28's L9 disposition at the round's stamp.
