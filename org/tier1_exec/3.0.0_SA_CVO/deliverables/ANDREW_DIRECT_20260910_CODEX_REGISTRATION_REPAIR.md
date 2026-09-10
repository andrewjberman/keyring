# Codex launcher registration review and repair authorization

**archetype:** DIAGNOSE

Received by `3.0.0_SA_CVO` through the Codex user channel on 2026-09-10, recorded at 08:25 Eastern (corrected from the initial minute estimate using the command clock). Exact user instruction:

> Yeah it might be a good idea to take this as an opportunity to make sure that the launcher-owned heartbeat for the codex path actually handles registration properly in the event there is a little glitch there. If you identify the nature of the issue, you have egress to fix and commit on the spot.

Scope: inspect launcher-owned registration, identify the issue, fix and commit under this direct authorization. No push authorized or performed. No second heartbeat, detector, or turn bridge.

Initial evidence: the running heartbeat's startup log records registration of `3.0.0_SA_CVO` at PID 22328 and a connected broker. The local liveness entry and the broker's `/list-agents` response both independently name PID 22328. The sender warning comes from the separate one-shot send process, whose imported `server._my_serial` is unset; `codex-send.py` already documents that distinction.

Recovery finding: `server.heartbeat` refreshes local liveness and ignores the broker heartbeat response; the broker's heartbeat handler returns OK even if its UPDATE found no registered row. The Codex companion currently re-registers only when the LOCAL entry is missing. A lost broker row with surviving local liveness therefore has no recovery in that companion.

## Repair and verification

Code committed as `8e26624bfc`; merged to local CLOUD through `.tools/safe-merge.sh` as `56711187ac`. All five merged files compare equal to the tested commit. The companion now checks the exact serial/PID broker row, re-registers missing rows through its existing guarded registration function, cancels the consuming poller after registration, retries unavailable broker reads, and refuses a different PID. The send receipt explains the separate-process advisory; the underlying sender stamp, audit, and refusal behavior are retained.

27 registration/readiness tests pass. The broker-row-loss test fails by timeout against the original heartbeat, with local heartbeat returning OK throughout. Existing lost-local-registration recovery still passes. No live row or inbox was mutated by the tests. The actual completion message to CTO exercised the revised receipt after merge and delivered successfully.

The existing launcher-owned heartbeat was not restarted; it retains its original loaded code until the next launcher restart. The latest readiness probe passed 9/9 with heartbeat PID 22328, bridge PID 23280, and detector PID 23752. No duplicate helper was created.

## Compiler Tools

| Tool / check | Result | Limit |
|---|---|---|
| comp-which; comp-read | Source routing and registration/sender mechanism inspection | Direct full-file reads supplied the implementation evidence |
| unittest, explicit worktree cwd | 27 passed | Isolated broker responses; not a live outage injection |
| Original-code negative control | Recovery test times out on original code | Confirms the new test catches the missing behavior |
| commit-gate | Four Python files passed | Markdown was reviewed directly |
| git diff of repair commit vs merged HEAD | Zero difference across all five repair files | Confirms merge preserved tested bytes in Git |
| codex-seat-status | GREEN 9/9 | Existing heartbeat still runs original code |

CTO message 95106 was read, ACKed, and archived: installed comp-tools invoked from linked worktrees can inspect the MAIN checkout. The only worktree comp-read here inspected unchanged safe-merge.sh; no worktree comp-find census was used as validation. Tests ran via Python with explicit cwd and imports relative to the test files. The commit-time comp-pulse report is not relied upon as proof of worktree coverage.

## Routing and push state

The same-turn authorization broadcast reached CTO. The canonical routing gate refused COO and MSTR copies; the refusal was reported to CTO with a relay request, without bypass. Completion also reached CTO. Push state LOCAL; origin/CLOUD measured by git ls-remote at 08:30 Eastern: `1e01703e54de2383d9d59662f9c9f0e42597407c`. No push performed.

## What you should have asked but did not

Registration has two independent state stores: local liveness and broker membership. A successful local heartbeat alone cannot prove the broker still holds the row. Process-local sender verification is a third boundary and must not be inferred from either store.

— 3.0.0_SA_CVO
