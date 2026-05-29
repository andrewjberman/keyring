# Telemetry PostToolUse Hook — Root Cause + Fix (THREE stacked causes)

**Agent:** 0.7.0_AE_CloudOps
**Cycle:** 2140Z 2026-05-29
**Trigger:** MSTR [BREAK] 20260529T203720Z — "telemetry hook still NOT writing despite the fix (4b3ef1e95); fresh post-fix sessions produce zero telemetry; root-cause needed."
**Authority:** Andrew-flagged priority; report to 0.0.0_AB_MSTR.
**Status:** ROOT-CAUSED + FIXED + VERIFIED (organic multi-agent fresh writes, not synthetic).

## TL;DR

The prior fix (4b3ef1e95) re-wired the hook into the correct *content* but the wrong *file*, and carried two latent script/config bugs. **Three independent, stacked root causes** each sufficient to produce zero telemetry. All three fixed; verified by fresh headless sessions AND live production agents writing well-formed organic telemetry.

## The three root causes

### CAUSE 1 (PRIMARY) — Claude Code 2.1.157 does NOT load hooks from `.claude/settings.local.json`
All hooks lived in `settings.local.json`. This Claude Code version only loads hooks from `.claude/settings.json` (project shared, tracked). `settings.json` had **no** `hooks` key at all.
- **Proof:** an identical-structure marker hook fired from `settings.json` (10 fires, cwd correctly at project root) but never fired from `settings.local.json`. Independently corroborated: a PreToolUse `block-bare-inbox-watch` deny-hook (also in settings.local.json) failed to block a regex-matching command, and the session transcript contained zero hook-execution records.
- **Why it regressed ~05-26:** the hook historically lived in the *working-tree* copy of settings.local.json and worked under an *older* Claude Code. The 05-24 broker-migration revert dropped it; 4b3ef1e95 restored it — but to settings.local.json, which 2.1.157 ignores. (A Claude Code auto-update is the most likely reason the same file location stopped working.)
- **Blast radius beyond telemetry:** because *all* of settings.local.json's hooks were dead, the PreToolUse `block-bare-inbox-watch` guard, the `register_agent` poller launch, and `kill-orphans --stale --force` were ALSO dead.

### CAUSE 2 — `async: true` hooks are NOT executed by Claude Code 2.1.157
The historical config (and my first migration attempt) marked the hooks `async: true`. With async, the hook does not run in this version.
- **Proof:** identical settings.json config wrote telemetry with `async` removed, and wrote nothing with `async: true` re-added (A/B headless test).

### CAUSE 3 (LATENT) — `post-tool-telemetry.sh` died on bare `jq` under `set -euo pipefail`
`jq` is workspace-local (`.tools/jq.exe`) and NOT on PATH; the Claude Code hook shell does not load the user profile, so `.tools/` is absent from PATH. The script called bare `jq` at line 1 of its logic → exit 127 → `set -e` killed it **before** any jsonl write or `hook_errors.log` entry (silent death — matches "no hook_errors evidence"). The PreToolUse script already documented this exact hazard and resolved `.tools/jq.exe` via `$SCRIPT_DIR`; the telemetry script did not.
- **Proof:** under a PATH-stripped shell (`PATH=/usr/bin:/bin`), the original script wrote nothing; the patched script (script-dir `jq` resolution) wrote correctly.

## The fix (all in tracked files)

1. **Migrated the entire hooks block** `settings.local.json` → `settings.json` (authoritative, loaded, committed). Removed the `hooks` key from settings.local.json to prevent future double-fire/drift.
2. **Removed `async: true`** from every hook. The hooks are fast/bounded; `post-send-commitment.sh` is a no-op except on `send_message`; the telemetry script already backgrounds its slow broker call internally.
3. **Patched `org/mcp/hooks/post-tool-telemetry.sh` + `classify-tool-kind.sh`** (canonical sources): deterministic `jq` resolution (`$SCRIPT_DIR/../jq.exe` → PATH → graceful log-and-exit), `export JQ` honored by the classifier, classification made non-fatal so a classifier hiccup never blocks the durable jsonl write. Re-installed canonical → `.tools/hooks/` via `install-telemetry-hook.sh`.

## Verification (proof-of-fix — organic, not synthetic)

- **Fresh headless sessions** (replicating the spawned-agent launch: `claude -p ... --dangerously-skip-permissions`) wrote well-formed new-schema telemetry: `TELETEST_REAL_HOOK`, `TELETEST_SHIP`.
- **Live production agents wrote fresh organic telemetry within minutes** (Claude Code hot-reloaded settings.json for running sessions): `0.0.0_AB_MSTR` (ScheduleWakeup/upkeep), `1.0.0_SA_CTO` (Bash/work, session-id-keyed), `0.4.0_DE_ClientPlatform` + `0.4.0_DS_ClientPlatform~B` (heartbeat/upkeep) — 43 new-schema entries timestamped 21:xxZ across 8 agent files. Correct serial resolution (both session-id-keyed and fallback), correct kind classification, correct tool_name.

## Durability notes / follow-ups

- `.tools/hooks/*` is gitignored (copied from canonical via `install-telemetry-hook.sh`). This workspace's copy is already re-installed/fixed; **other checkouts/worktrees must run `bash .tools/hooks/install-telemetry-hook.sh` after pulling** to get the patched scripts. Recommend folding the install into the agent startup protocol (org/XXX.md Step 1b) so it's not a manual step — flagged to MSTR.
- The `settings.local.json`-vs-`settings.json` hook-loading behavior + the `async` non-execution are Claude Code 2.1.157 facts worth a ledger entry; future hook wiring must go in `settings.json` and avoid `async`.

## Files changed (tracked)
- `.claude/settings.json` — added full hooks block (PreToolUse block-bare; PostToolUse register_agent poller+kill-orphans; PostToolUse `*` telemetry+commitment), no async
- `.claude/settings.local.json` — removed dead `hooks` key
- `org/mcp/hooks/post-tool-telemetry.sh` — deterministic jq resolution; non-fatal classify
- `org/mcp/hooks/classify-tool-kind.sh` — deterministic jq resolution; honor `$JQ`
