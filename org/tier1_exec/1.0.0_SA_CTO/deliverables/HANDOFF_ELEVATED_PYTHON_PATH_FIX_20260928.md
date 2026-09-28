# HANDOFF -- elevated session: remove the gutted Python 3.14 from the machine PATH (site Z, post-reboot)

Paste the block below as the first message to `1.0.0_SA_CTO~Z` in an ELEVATED (Run as administrator) terminal.

```
You are 1.0.0_SA_CTO~Z, launched ELEVATED on site Z after the reboot, for ONE act on Andrew's standing approval
(REC (a), record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260927_1723Z_OPEN_CALLS_RECS_APPROVED_PYTHON_PATH_AND_SERP_AFTER_IDENTITY.md):
remove C:\Program Files\Python314 from the MACHINE PATH so bare `python` resolves to Python 3.11.
Skip /watcher and the org/XXX.md startup until the act is done and reported. Use PowerShell.

1. CONFIRM ELEVATION -- stop if False:
   ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

2. MEASURE BEFORE (print all three):
   ([Environment]::GetEnvironmentVariable('Path','Machine') -split ';') | ? { $_ -match 'Python' }
   ([Environment]::GetEnvironmentVariable('Path','User')    -split ';') | ? { $_ -match 'Python' }
   Get-ChildItem 'C:\Program Files\Python314\Lib' | Select Name      # expect only site-packages (gutted)
   If the machine PATH holds NO Python314 entry, or Lib\encodings EXISTS (someone repaired it), STOP and report.

3. BACK UP, then REMOVE only the Python314 entries (four were measured: Python314, Python314\, Python314\Scripts, Python314\Scripts\):
   $p=[Environment]::GetEnvironmentVariable('Path','Machine')
   $p | Out-File "$env:USERPROFILE\machine_path_backup_$(Get-Date -Format yyyyMMddTHHmmss).txt"
   [Environment]::SetEnvironmentVariable('Path', (($p -split ';' | ? { $_ -and $_ -notmatch '\\Python314' }) -join ';'), 'Machine')

4. VERIFY IN A FRESH PROCESS (the current shell keeps its old PATH -- read the new one from the registry):
   $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')
   (Get-Command python).Source            # expect ...\Programs\Python\Python311\python.exe
   python -c "import sys, mcp; print(sys.version.split()[0], 'mcp OK')"   # expect 3.11.9 mcp OK
   python -c "import encodings; print('stdlib OK')"
   Also confirm the Machine PATH lost ONLY the Python314 rows: compare entry counts against the backup file
   (before minus 4 == after); any other difference -> restore from the backup file and report.

5. LEAVE IN PLACE (set 2026-09-27, user scope, still useful): PY_PYTHON=3.11 and PY_PYTHON3=3.11 -- py.exe picks
   the newest REGISTERED Python (3.14) from the registry regardless of PATH, and the comp-* .cmd shims run through py.exe.
   Do NOT uninstall Python 3.14 in this session; that is a separate call for Andrew.

6. REPORT to Andrew in this terminal, in plain English: before/after PATH rows, the backup file path, the three
   verification lines. Then say: every Claude session must be (re)started AFTER this act to inherit the new PATH,
   and opal-agent-comms (broker messaging) should connect in those new sessions.

7. RECORD: one line appended to org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_ELEVATED_PYTHON_PATH_FIX_20260928.md
   under "## Outcome" (date, before/after counts, backup path), committed with
   bash .tools/safe-commit.sh --author "1.0.0_SA_CTO~Z <1.0.0_SA_CTO~Z@opal.agent>" -F <msgfile> -- <that file>
   (message file written by the Write tool, not the shell). Push state: LOCAL; MSTR~Z pushes.
   Then close this elevated session -- do not run the fabric from an admin shell.
```

## Outcome

(to be appended by the elevated session)
