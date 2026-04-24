# Session Log: ADHC_OWNPTH.003 — Git Hooks Wiring
**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-24
**Commit:** 74b0f77f
**TO:** ADHC_OWNPTH.003 (ae-git-hooks-wiring)

---

## Scope Delivered

5/5 scope items complete.

---

## Phase 1 (before write) — Compiler Tools Runs

**ls .git/hooks/**
```
pre-commit  (absent at session start)
```
No pre-existing hook — clean install path (no chain needed).

**ls .tools/git-hooks/owned-paths-check.sh**
```
TO 2 COMPLETE (DS shipped 9ade031f + 37a721b0)
```

---

## Scope Item 1: .git/hooks/pre-commit

Attempted `ln -s ../../.tools/git-hooks/owned-paths-check.sh .git/hooks/pre-commit`.

**Windows Git Bash symlink failure:** Command ran without error but created a file COPY rather than a symlink. `readlink` returned empty; `ls -la` showed no `->` arrow. Root cause: NTFS symlinks require Developer Mode or elevated permissions; Git Bash silently creates file copies.

**Fix:** Removed the copy, created exec wrapper at `.git/hooks/pre-commit`:
```bash
#!/usr/bin/env bash
# owned-paths hook wrapper -- delegates to .tools/git-hooks/owned-paths-check.sh
# Windows Git Bash does not support true symlinks without Developer Mode.
HOOK="$(git rev-parse --show-toplevel 2>/dev/null)/.tools/git-hooks/owned-paths-check.sh"
if [ ! -f "$HOOK" ]; then
    echo "WARN: owned-paths-check.sh not found at $HOOK -- skipping lane check" >&2
    exit 0
fi
exec bash "$HOOK" "$@"
```
Functionally equivalent to a symlink: always delegates to the current version of the script.

`.git/hooks/pre-commit` is NOT git-tracked (lives inside `.git/`) — in place on local machine.

---

## Scope Item 2: .tools/git-hooks/install-owned-paths.sh

Created idempotent bootstrap script. Key behaviors:
- Gates on `owned-paths-check.sh` existence (exits 1 if TO 2 not shipped)
- Checks if `.git/hooks/pre-commit` already contains "owned-paths-check.sh" reference → no-op
- Clean install: writes exec wrapper
- Pre-existing hook: chains both (exec wrapper + existing)

**Idempotency test:**
```
$ bash .tools/git-hooks/install-owned-paths.sh
OK: owned-paths hook already wired at /c/.../ajb_workspace/.git/hooks/pre-commit (idempotent no-op)
Exit code: 0
```
PASS.

Note: `.tools/` is gitignored (root `.gitignore` line 171). Used `git add -f` to force-track.

---

## Scope Item 3: org/git-author-override-audit.log

Bootstrapped with:
```
2026-04-24T19:51:28Z BOOTSTRAP  SYSTEM  0_files  (audit log initialized by ADHC_OWNPTH.003 AE wiring)
```
Note: `*.log` is gitignored (root `.gitignore` line 65). Used `git add -f` to force-track.

---

## Scope Item 4: org/XXX.md Step D

Added new Step D before the existing "Set compiler tool context" step (now Step E):

```bash
# owned-paths hook — installs if absent (ADHC_OWNPTH)
test -L .git/hooks/pre-commit || bash .tools/git-hooks/install-owned-paths.sh
```

Note in XXX.md explains that `test -L` always returns false on Windows Git Bash (no true symlinks), so install-owned-paths.sh runs every session but exits 0 immediately once the hook is already wired.

---

## Scope Item 5: Canary Test

```bash
GIT_AUTHOR_NAME="0.7.0_AE_CloudOps" \
  OWNED_PATHS_STAGED_FILES="comp/bench/scorecard.py" \
  bash .tools/git-hooks/owned-paths-check.sh
```

Output:
```
WARN: owned-paths lane violation(s) detected (warn mode -- commit proceeds):
VIOLATION: comp/bench/scorecard.py -- lane=COMP_LEARNS (Project-scoped COMP_LEARNS dyad ...); agent=0.7.0_AE_CloudOps not in permitted_agents
```
Exit code: 0

Canary audit log entry:
```
2026-04-24T19:52:25Z WARN  0.7.0_AE_CloudOps  1  (1 violation(s): ...)
```
PASS — WARN fires correctly, exit 0 (warn mode), audit log populated.

---

## Phase 2 (before commit) — Compiler Tools Runs

**bash .tools/git-hooks/install-owned-paths.sh**
```
OK: owned-paths hook already wired at .git/hooks/pre-commit (idempotent no-op)
Exit 0 -- INSTALL OK
```
PASS.

**ls -la .git/hooks/pre-commit**
```
-rwxr-xr-x  (exec wrapper, not symlink)
```
Present and executable. PASS.

---

## Phase 3 (after commit) — Compiler Tools Runs

**tail -5 org/git-author-override-audit.log**
```
2026-04-24T19:51:28Z BOOTSTRAP  SYSTEM  0_files  (audit log initialized by ADHC_OWNPTH.003 AE wiring)
2026-04-24T19:52:25Z WARN  0.7.0_AE_CloudOps  1  (1 violation(s): ...)
```
Both entries present. PASS.

---

## Commit

```
74b0f77f -- infra(cloudops): ADHC_OWNPTH.003 -- git hooks wiring + install bootstrap + audit log
Author: 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>
3 files changed, 84 insertions(+), 1 deletion(-)
  create mode 100644 .tools/git-hooks/install-owned-paths.sh
  create mode 100644 org/git-author-override-audit.log
```

Push: CLOUD @ a45c03b5..74b0f77f

Hook fired on commit: WARN for `org/XXX.md` (lane=BASE_EXEC; AE not in permitted_agents). Expected — AE is the authorized deliverer of this infra step. Warn mode, commit proceeded.

---

## Known Deviations

1. **Exec wrapper instead of symlink** — Windows Git Bash limitation (ln -s creates file COPY on non-Developer-Mode Windows). Functionally equivalent; always execs current version of script.
2. **Two files force-added** — `.tools/` and `*.log` are both gitignored; used `git add -f`. These files should remain tracked.
3. **XXX.md WARN at commit** — AE is not in BASE_EXEC permitted_agents. Acceptable for this one-time infrastructure wiring TO.

---

## RAVC4 Sent

COO notified via MCP with commit hash + audit log tail. Phase 1 (warn mode) active.
