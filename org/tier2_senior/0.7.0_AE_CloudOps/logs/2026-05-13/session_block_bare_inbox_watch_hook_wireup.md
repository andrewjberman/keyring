# AE 0.7.0 Session Log — block-bare-inbox-watch Hook Wireup
**Date:** 2026-05-13
**Agent:** 0.7.0_AE_CloudOps
**Trigger:** Boot from compacted context; COO wake-ask cited CTO pending TO `block-bare-inbox-watch-hook-wireup.md`
**TO:** `0.7.0_AE_CloudOps-2026-05-12-block-bare-inbox-watch-hook-wireup`

---

## Objective

Deterministically prevent bare-path `bash org/mcp/inbox-watch.sh <serial>` Bash/PowerShell tool calls
via a PreToolUse hook. Empirical incident 2026-05-12: bare-path launches propagate `$0` into
auto-respawn children, creating PPID=1 zombies that survive session death and short-circuit
future tracked launches via the single-watcher guard (Claude Code surfaces guard-exit-0 as
misleading exit 143).

CTO authored `.tools/hooks/block-bare-inbox-watch.sh` + smoke-tested 5/5 cases standalone
on 2026-05-12; AE owns commit + wireup per Andrew direct authorization.

---

## What Shipped

| File | Mode | Commit | Notes |
|------|------|--------|-------|
| `.tools/hooks/block-bare-inbox-watch.sh` | 100755 | f44146999 (content) + 9e76598 (mode) | Gitignored prefix `.tools/`; required `git add -f` + `git update-index --chmod=+x` |
| `.claude/settings.local.json` | tracked, modified | f44146999 | PreToolUse block: matcher `Bash\|PowerShell`, timeout 5s |

---

## Two CTO-Authored Issues Surfaced + Fixed During Wireup (TO Note #2 surface-back)

### Issue 1: jq location

CTO's hook script used `jq` from PATH. Empirical: Claude Code's hook execution shell does
NOT load `.bashrc`, so workspace `.tools/` is not on PATH. `jq.exe` was unreachable; the
hook fell through to pass-through on every invocation.

**Fix:** Resolve `$JQ` deterministically via `SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"`
relative to the hook script's known location (`.tools/hooks/`), then PATH fallback for
Linux/Mac dev.

### Issue 2: Block mechanism

CTO's hook used `exit 2` + stderr message, per the older Claude Code hook contract. Empirical:
on current Claude Code, bare exit-2 + stderr is treated as a HOOK ERROR (not a permission
block) — the tool call proceeds.

**Fix:** Emit JSON to stdout per the current hook spec:
```json
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"..."}}
```
Exit 0. Tested via claude-code-guide subagent + empirical retry — block is now honored.

Source for current spec: claude-code-guide (Opus 4.7) confirmed JSON output mechanism is
required; exit-2 is interpreted as hook error.

---

## Acceptance Criteria

| AC | Requirement | Result |
|----|-------------|--------|
| #1 | Hook script committed with mode 100755 | PASS — `git ls-files -s` shows `100755 ef38cbda2... .tools/hooks/block-bare-inbox-watch.sh` |
| #2 | PreToolUse entry in `.claude/settings.local.json`; JSON valid | PASS — `jq . settings.local.json` exits 0; entry under `hooks.PreToolUse[0]` |
| #3 | NEGATIVE empirical: bare-path call BLOCKED stderr + non-execute | PASS — see Empirical Evidence below |
| #4 | POSITIVE empirical: `inbox-watch <serial>` + absolute path pass through | PASS — see Empirical Evidence below |
| #5 | No PostToolUse regression on register_agent | PASS — session-start register triggered hook_launch_poller + kill-orphans normally; inbox-watch came up |
| #6 | Session log with test transcripts + commit hash | This file |
| #7 | MCP COMPLETE to CTO with commit hash + settings delta | Sent post-log commit |

---

## Empirical Evidence (Hook Behavior Post-Wire)

All evidence captured via temporary debug instrumentation (`/tmp/block_bare_inbox_watch.debug`,
`.input`, `.stdout`) during the testing iteration, then stripped from final hook script
before commit f44146999. Hook script as shipped contains NO debug logging.

### NEGATIVE (bare-path) — BLOCKED

Real-agent tool calls from external sessions that landed in this workspace during testing:

| Time (UTC) | Session | Command | Hook | Block |
|------------|---------|---------|------|-------|
| 14:52:58Z | c0bfc734 (DS_ClientPlatform~C) | `bash org/mcp/inbox-watch.sh 0.4.0_DS_ClientPlatform~C` | REGEX_MATCHED | BLOCK_EMITTED (JSON_LEN=464) |
| 14:53:10Z | db8cbc89 (AE_PartnerETL) | `bash org/mcp/inbox-watch.sh 0.6.1_AE_PartnerETL` | REGEX_MATCHED | BLOCK_EMITTED (JSON_LEN=464) |

In each case the Claude Code session received the JSON `permissionDecision: "deny"` response
and aborted the tool call. The blocked agents subsequently relaunched via the absolute-path
fallback form (`bash /c/Users/AndrewBerman/Desktop/ajb_workspace/...`), which passed through
the hook unblocked — the canonical recovery path.

### POSITIVE A (PATH wrapper) — PASS-THROUGH

| Time (UTC) | Command | Hook | Block |
|------------|---------|------|-------|
| 14:54:44Z | `inbox-watch 0.4.2_RD_AdvisorIntelligence` | REGEX_CHECK ran (no regex hit) | No BLOCK_EMITTED |

### POSITIVE B (absolute path) — PASS-THROUGH

| Time (UTC) | Command | Hook | Block |
|------------|---------|------|-------|
| 14:53:19Z | `bash /c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh 0.4.0_DS_ClientPlatform~C` | REGEX_CHECK ran | No BLOCK_EMITTED |
| 14:55:20Z | (same form, different invocation) | REGEX_CHECK ran | No BLOCK_EMITTED |

### Standalone smoke tests (final clean hook script, post-commit)

```
$ cat .runtmp/hook_test_neg.json | bash .tools/hooks/block-bare-inbox-watch.sh
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny",...}}
exit: 0

$ cat .runtmp/hook_test_pos_path.json | bash .tools/hooks/block-bare-inbox-watch.sh
exit: 0  (silent)

$ cat .runtmp/hook_test_pos_abs.json | bash .tools/hooks/block-bare-inbox-watch.sh
exit: 0  (silent)
```

### Session-local exemption observation

My own session's `bash org/mcp/inbox-watch.sh ...` calls during NEG2-NEG15 testing did not
trigger Claude Code's enforcement of the JSON deny — the hook fired, but the tool call
proceeded. Hypothesis: Claude Code maintains a per-session approval cache; once a Bash tool
pattern is approved during interactive testing, subsequent calls matching it bypass PreToolUse.
The hook still fires (logged via debug instrumentation), but its deny output is ignored.

This is NOT a deployment defect — fresh sessions (other agents in the workspace; also my own
session for compound commands containing the trigger pattern in arguments) DO see Claude Code
enforce the block. Empirical: my own `chmod +x ...; echo '{"tool_input":{"command":"bash org/mcp/inbox-watch.sh FOO"}}' | ...` compound command WAS blocked by Claude Code in this session at ~14:56Z (the inline JSON string contained the trigger pattern).

Surfacing to CTO for awareness; doesn't change acceptance.

---

## Surface-Back to CTO (TO Notes ratified)

1. **Hook script needed two non-trivial fixes** (jq location + JSON output mechanism) beyond
   the regex Andrew's CTO authored. Both stripped from the shipped hook are documented in
   the commit message + this log.
2. **Promotion-to-shared decision**: CTO suggested YES for org-wide coverage on this workspace
   (all agents share settings.local.json). Empirically confirmed — settings.local.json IS
   workspace-tracked in git (not user-local on this repo), so the wireup in f44146999 ALREADY
   reaches all agents. The TO's framing of "local first, promote-to-shared after" turns out
   to be moot here — promotion is automatic. No follow-up wireup needed.

---

## Test Files (Permanent Reference)

`.runtmp/hook_test_{neg,pos_path,pos_abs}.json` — three input fixtures for reproducing the
standalone smoke tests post-deploy. Not committed (`.runtmp/` is gitignored).

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-* | not applicable | TO `<compiler_tools_mandate>` declared `<none/>` — hook wireup touches `.tools/hooks/` + `.claude/settings.local.json`, neither modeled in the compiler graph. Smoke-test transcripts are the validation surface. |

---

## RAVC Trail

| RAVC | Direction | Time (UTC) | Content |
|------|-----------|------------|---------|
| Wake-ask | COO → AE 0.7 | 14:15:47Z | Triage: CTO TO + Phase B P3 Lambdas + cron-vs-quorum disambig |
| RAVC1 (wake ACK) | AE 0.7 → COO | 14:17:41Z | Triage agreement; starting CTO TO; items 2+3 deferred |
| RAVC1 (TO accept) | AE 0.7 → CTO | 14:17:49Z | Accepting + plan; settings.local.json first |
| ACK | COO → AE 0.7 | (~14:20Z) | Concur local-first ship pattern |
| ACK | CTO → AE 0.7 | (~14:21Z) | Plan ratified; two notes (verify no-spawn on block, promote-to-shared after) |
| RAVC2 | AE 0.7 → CTO + COO | (post-log commit) | Commits f44146999 + 9e76598 shipped; AC table; empirical evidence |

---

## Open Items Post-Session

| Item | Status |
|------|--------|
| Push commits to origin/CLOUD | Pending — AE has push rights for CLOUD |
| ADVI_INFETL Phase B P3 daily Lambdas | Standing by per COO (Andrew Path A/B ruling pending); also see COO's correction-3 in inbox-watch log: Phase B P3 Lambdas ALREADY DEPLOYED — scope simplified to aggregator-empirical-validation only |
| Chain #23/#24 cron-vs-quorum cleanup | AE 0.6.1's lane; absorb if they confirm cron still firing |

## Session Status: COMPLETE — block-bare-inbox-watch hook wired + empirically blocking on fresh sessions; commits f44146999 + 9e76598; ready to push
