# Session Log — Git Bash PATH Remediation (2026-04-28)

**Author:** 1.0.0_SA_CTO
**Date:** 2026-04-28 (Eastern)
**Scope:** Environment incident — Git for Windows wiped from this machine; bash resolution falls through to WSL stub
**Status:** In progress — System PATH fix handed to Andrew (admin shell)

---

## Summary

Mid-startup Step 1b, `inbox-watch` launches failed with WSL "execvpe(/bin/bash) failed" relay errors. Investigation revealed `C:\Program Files\Git` had been gutted earlier today (folder timestamp 12:28 PM), leaving only the Inno Setup uninstaller stub. PATH still pointed at `C:\Program Files\Git\cmd` (orphaned). Andrew reinstalled Git for Windows 2.54.0 mid-session, restoring `git.exe` and `bash.exe`, but the WSL stub at `C:\Windows\System32\bash.exe` continues to win bare `bash` lookups in fresh PowerShell tool calls because System PATH precedes User PATH and the installer only adds `Git\cmd`, not `Git\bin`. Profile-based override works for current process but does not survive Claude Code's `-NoProfile` PowerShell launches. Final fix is a System-PATH prepend that requires Andrew to run an elevated PowerShell himself.

---

## Timeline

| Time | Event |
|------|-------|
| Session open | CTO Step 0 register + inbox-watch dispatched via PowerShell `bash org/mcp/inbox-watch.sh 1.0.0_SA_CTO` (run_in_background) |
| +30s | Background task `bs5sh0bf6` exited code 1: `<3>WSL (9 - Relay) ERROR: CreateProcessCommon:800: execvpe(/bin/bash) failed: No such file or directory` |
| Triage | `where.exe bash` → only `C:\Windows\System32\bash.exe` + `WindowsApps\bash.exe` (both WSL stubs); no Git Bash |
| Disk probe | `Test-Path "C:\Program Files\Git\bin\bash.exe"` → False; `\cmd\git.exe` → False; `\usr\bin\bash.exe` → False |
| Forensic | `cmd /c dir "C:\Program Files\Git" /a` → folder timestamp 04/28/2026 12:28 PM, only `unins001.dat`/`.exe`/`.msg` (dated 2026-04-03) remain. Inno Setup uninstaller textbook leftover. |
| Conclusion presented | Git for Windows uninstalled today ~12:28 PM — almost certainly an IT/MDM remediation given timing, lack of replacement install, and absence from uninstall registry (only GitHub CLI 2.87.0 listed) |
| Andrew reinstalled | Hit "directory exists" prompt; offered Options A/B (run leftover unins001.exe vs `Remove-Item -Recurse -Force`); reinstalled successfully |
| Verify reinstall | `git.exe` 2.54.0.windows.1, `bash.exe` 5.3.9(1)-release (x86_64-pc-cygwin) — both resolve via explicit path |
| inbox-watch retry | Launched via `& "C:\Program Files\Git\bin\bash.exe" org/mcp/inbox-watch.sh 1.0.0_SA_CTO` — succeeded (task `b2152aptr` then `blec36lqd`); 2 inbox messages already pulled by `check_inbox` |
| Default-bash request | Andrew: "we need git bash as default there is no wsl on this computer" |
| PATH inspection | System PATH starts with `C:\Windows\system32` (WSL bash here). User PATH has `C:\Program Files\Git\cmd` but NOT `\bin` or `\usr\bin`. Windows process PATH is System+User concatenated → System wins → User-PATH prepend cannot override. |
| Profile attempt | Wrote `~\Documents\WindowsPowerShell\profile.ps1` + `~\Documents\PowerShell\profile.ps1` to prepend Git Bash. Worked in current PS process. Fresh Claude Code tool call: `where.exe bash` → System32 first again → Claude Code launches PS with `-NoProfile`, profile never loads. |
| Admin token check | `whoami /groups` → `BUILTIN\Administrators ... Group used for deny only` (UAC limited token); cannot self-elevate from Claude session |
| Handoff to Andrew | Provided elevated-PowerShell script: read Machine PATH from registry, back up to Desktop, prepend `Git\bin` + `Git\usr\bin`, write as `REG_EXPAND_SZ`, broadcast `WM_SETTINGCHANGE`, verify. Restore-from-backup snippet included. Andrew to run himself. |

---

## Root Cause

Two compounding issues:

1. **Git for Windows wiped**, presumably by IT remediation policy fired at 12:28 PM 2026-04-28. Standard Inno Setup uninstaller pattern (uninstaller stub left behind, all other contents gone). No record in HKLM uninstall registry.

2. **Default Git for Windows install only adds `Git\cmd` to PATH**, not `Git\bin` or `Git\usr\bin`. `git.exe` works (lives in `cmd`), but `bash.exe` (lives in `bin`) does not — so any tooling that calls bare `bash` falls through to the next match, which on Windows is `C:\Windows\System32\bash.exe` (the WSL launcher stub). With no WSL distro installed, the stub errors out.

The two issues stack: even after reinstall, `bash` is not on PATH unless we manually prepend the bin directories.

---

## Fix Applied This Session

| Layer | Status | Notes |
|-------|--------|-------|
| Git for Windows reinstall | Done by Andrew | 2.54.0.windows.1 |
| Profile prepend (`~\Documents\WindowsPowerShell\profile.ps1`) | Written | Effective for interactive PS sessions; ignored by Claude Code's `-NoProfile` launches |
| Profile prepend (`~\Documents\PowerShell\profile.ps1`) | Written | PS Core mirror |
| Current-session `$env:PATH` prepend | Done | This Claude Code instance has Git Bash on PATH for the rest of this conversation |
| System PATH edit | **Pending Andrew** | Script handed off; requires admin shell. Final durable fix. |
| WSL feature disable (alternate) | **Not done** | Would also work; deferred — keeps WSL feature flag intact in case a distro is wanted later |

---

## Why Profile Doesn't Cover Claude Code

Claude Code spawns each PowerShell tool invocation with `-NoProfile` (likely for startup performance and reproducibility). Profile scripts at `$PROFILE.CurrentUserAllHosts` and `CurrentUserCurrentHost` are skipped. Confirmed empirically: after writing the profile, a fresh PS tool call still resolved `bash` → `C:\Windows\System32\bash.exe`.

The profile fix is still useful for:
- User-launched PowerShell (Start menu, Win+X, etc.)
- VS Code integrated terminal
- Any non-Claude-Code PowerShell session

But not for Claude Code automation. That's why System PATH is the right durable fix.

---

## Handoff Script (For Andrew, Admin PS)

Paste-ready script provided in conversation. Highlights:
- Uses `Get-ItemProperty` / `Set-ItemProperty` against `HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment` — does NOT use `setx` (which truncates at 1024 chars and expands variables, both unsafe for the System PATH on this machine).
- Writes back as `ExpandString` (REG_EXPAND_SZ) to preserve any `%VAR%` in other entries.
- Backs up current System PATH to `$env:USERPROFILE\Desktop\system_path_backup_<timestamp>.txt` before writing.
- Broadcasts `WM_SETTINGCHANGE` so newly spawned processes pick up the new PATH without a reboot.
- Idempotent — re-running will not duplicate entries.

After Andrew runs the script, **Claude Code must be closed and relaunched** for the parent process to inherit the new PATH (child PowerShell processes get PATH at spawn from the Claude Code parent).

---

## Side Effects / Notes for Future Sessions

- **Reinstall version delta**: previous Git for Windows version unknown (the leftover `unins001.*` files were dated 2026-04-03, so install age ≈ 25 days). Reinstalled version is 2.54.0.windows.1. No known compatibility issues with current `.tools/safe-commit.sh` / comp-* / record-terraform-deploy.sh wrappers.
- **IT remediation risk**: if the same MDM policy that wiped Git fires again, we'll be back at square one. Recommend Andrew flag Git for Windows to IT as an approved tool, otherwise budget periodic re-installs.
- **WSL stub remains harmless once System PATH is fixed**: the stub stays at `C:\Windows\System32\bash.exe` but is no longer first in resolution order. No need to disable the WSL feature.
- **CTO Step 1b protocol**: agents whose startup runs `bash org/mcp/inbox-watch.sh ...` will silently fail on this machine until the System PATH fix is applied. Workaround in the meantime: invoke via explicit `& "C:\Program Files\Git\bin\bash.exe" org/mcp/inbox-watch.sh <serial>`.

---

## Open Items

| Item | Owner | Gate |
|------|-------|------|
| Run System PATH edit script in admin PS | Andrew | Single command, idempotent |
| Relaunch Claude Code post-PATH-edit | Andrew | New process inherits new PATH |
| Verify in fresh PS: `where.exe bash` → Git Bash first | CTO (next session) | Confirms durable fix |
| Flag Git for Windows to IT as approved tool | Andrew | Prevents re-wipe |
| (Deferred) CTO Step 1b ground-truth reconciliation | CTO (next session) | Was the original session intent; tabled by environment outage |

---

## Compiler Tools

N/A — environment incident. No PRD authored, no scripts touched, no codebase changes. Profile files at `~\Documents\WindowsPowerShell\profile.ps1` + `~\Documents\PowerShell\profile.ps1` are user-config-scoped, not repo-tracked.

One entry will be appended to `org/compiler-tools-log.md` post-session: `CTO-ENVIRONMENT-2026-04-28 / git+bash diagnostic + System PATH handoff / 1.0.0_SA_CTO / 2026-04-28 / 0 corrections (env-only)`.

---

1.0.0_SA_CTO
