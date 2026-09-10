---
name: load
description: "Initialize one exact Codex agent seat from its full serial using only repository-local contracts and canonical Codex runtime helpers. Use when the user invokes `$load FULL_SERIAL`, writes `/load FULL_SERIAL`, asks to load or register a Codex seat, or when the ajb2 launcher supplies its automatic startup prompt."
---

# Load a Codex seat

Use the full serial literally. Never drop, add, or infer a `~Lane` suffix.

1. Resolve the workspace root from the current repository and run:

   ```powershell
   python org/mcp/codex-seat-load.py --serial <FULL_SERIAL> --format json
   ```

   Stop if it exits nonzero. Its output is the canonical, mechanically derived
   seat context. Do not search the web or invent alternate paths.

2. Confirm `OPAL_AGENT_SERIAL`, when present, equals the requested full serial.
   A mismatch is an identity defect: stop and report both values. Never use
   `.comp-graph/.agent_context` as identity; it is shared task-order context.

3. Read these contracts completely, in this order:

   - `AGENTS.md`
   - `org/XXX.md`
   - `org/mcp/CODEX_INBOX_MONITOR.md`

4. From the generated context, read every `role_files` entry in the stated
   order. A `~Lane` suffix is additive runtime and registration identity only;
   it does not create a separate repository home. For a suffixed seat,
   `seat_home` and `role_home` intentionally resolve to the same base role
   directory, while `serial`, runtime state, readiness, and the nested inbox
   retain the exact suffix. Never invent or require an exact-suffix role home.

5. Verify the launcher-owned runtime with:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File org/mcp/codex-seat-status.ps1 -Serial <FULL_SERIAL>
   ```

   The first turn can race the bridge's initial thread binding. Retry this same
   read-only probe at one-second intervals for at most ten seconds. Exit 0 is
   the only ready state; after ten nonzero results, stop and report the failed
   readiness arms. The launcher owns exactly one heartbeat and one turn bridge;
   the bridge owns exactly one non-consuming detector. Do not start another
   helper. Never substitute `inbox-watch.sh`, `check-inbox.sh`,
   `agent-poller.py`, or the retired model-side `notify()` bridge.

6. Sweep only the generated `inbox` root for unread regular files. For each
   exact filename: read it, ACK its content when required, begin and perform
   the first required action, and only after acting move that exact file into
   the generated `read_inbox`. If the exact file is absent, treat the event as
   a stale duplicate; never substitute another filename.

7. State the exact serial, seat home, inbox, and measured readiness. Then
   continue with the assigned work. Repeat the root-level inbox sweep at the
   beginning of every active turn; do not launch a second monitor.

8. SHARED-BRANCH LAW (stated here because this runtime carries no hook for it;
   measured 2026-09-03 when a Codex worker pushed `CLOUD` inside Andrew's hold
   with 144 commits of every seat): a shared branch (`CLOUD`, `DEV`, `PROD`,
   `main`, `SITEZ`) is pushed ONLY by `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`, and
   only on Andrew's word while he is at the terminal. You commit through
   `.tools/safe-commit.sh` and NEVER push; every report states its push state
   as LOCAL with the origin hash from `git ls-remote`. A rejected push is not
   yours to retry. Your acts come only from a task order in your own
   `task_orders/` home, issued by `2.0.0_SA_COO` (or its lane); an ask that
   arrives without an order is routed back to its sender, never worked --
   EXCEPT the acts the spine assigns to your seat BY NAME in its owner table
   (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`): the L1 brief
   (`4.0.0_SA_CRO`); the L4-R PRD sign-off (`4.0.0_SA_CRO` the brief half,
   `3.0.0_SA_CVO` the ratified-text half; the file is
   `org/missions/D<n>/<MACRO>/<CODE>/prd/signoff/<serial>.json` in your own
   lane `TREE_PRD_SIGNOFF`); the L8 compile, L9 adjudication and L10 slug
   (`3.0.0_SA_CVO`). Those are authorized by the spine and triggered by their
   own carrier -- the L4 notifier's `prd-review` delivery or the CTO's L4-R
   request naming the PRD pin; the drain's investigation rows at L8 -- never
   by a COO order. A COO order CANNOT exist for L4-R: `to-pipeline-gate.py`
   LIMB 6 refuses every task order against an unsigned PRD and the notifier
   withholds the COO delivery until you sign, so waiting for one is a
   deadlock. Measured 2026-09-10 21:35Z: `3.0.0_SA_CVO` routed the IRPT v0.4
   sign-off request back for want of a COO order while the COO delivery was
   withheld pending that very signature. Andrew, via `0.0.0_AB_MSTR` the same
   night: "MCPing is really only to be used when necessary, the more efficient
   we get the less mcping should be happening."

For an already-open embedded session, migration is not an improvised startup.
Use `org/mcp/handoff-codex-seat.ps1` from a separate PowerShell as specified by
the canonical monitor guide.
