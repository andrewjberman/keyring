# Python runtime made clean and clear: 3.14.7 removed, bare `python` is 3.12.10 — 0.3.0_DT_TradingOperations

**Date:** 2026-09-09
**Task Order:** ad-hoc — ELEVATED-SHELL TASK from Andrew, brief authored by `4.0.0_SA_CRO` ~15:4xZ
**Status:** COMPLETE (two follow-on acts are Andrew's, named under Next Steps)

---

## Objective

Andrew's word, record `@fc93ef9dbe`: "We need to make sure we are clean and clear on what python
version we are using." The CRO measured the decision — the estate runs Python 3.12; Python 3.14 has
no consumer. A machine-wide Python 3.14.7 install placed `C:\Program Files\Python314\` ahead of the
3.12 user install on the MACHINE PATH, which Windows resolves before the USER PATH, so bare `python`
became a 3.14 whose site-packages held only pip. That killed `opal-agent-comms` in every Claude
session launched after 12:30Z and refused every Codex seat spawned after it. Only an elevated act
could fix it. This log records that act.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find --name '0.3.0_DT_TradingOperations' --limit 30` | PARTIAL | 106 hits / 156451 files scanned, but 100+ were inbox message filenames carrying my serial; the seat directory I wanted was not on page 1 |
| comp-tool HUD | (gate fired on `find org -type d -path ...`) | PASS | Correctly routed a raw `find` to the rail per Rule 21; the gate did its job |
| comp-tool HUD | (gate fired on `comp-find ... \| head -30`) | PASS | Correctly refused a census piped into a receiver that erases the denominator; `--limit` was the right flag |

**What worked:** the HUD gate caught both off-rail searches at the moment of the call, and its message
named the exact flag to use instead. No time lost.

**What failed:** nothing crashed. `comp-find --name` is basename-matching, so a serial that appears in
thousands of inbox FILENAMES drowns the one directory named for that serial. Correct behavior, wrong
instrument for the question.

**Gap found:** there is no comp-tool verb for "where does seat `<SERIAL>` live in the org tree" — a
directory-shaped question, not a content or basename one. A plain `ls org/tier2_senior/` answered it in
one call. Noting it as a candidate, not filing it as a defect.

---

## Deployment Sequence

Machine act. No repo file was edited, nothing was installed, nothing was pushed.

| Step | Action | Result |
|------|--------|--------|
| 0 | Confirm elevation | `User=AzureAD\AndrewBerman  Elevated=True` |
| 1 | STEP 0 measure-before | 3.14.7 first on PATH; 2 Python314 MACHINE entries; 3 Python312/Launcher USER entries — matches the brief exactly |
| 2 | Census 3.14 site-packages | `pip 26.2.1` and nothing else, denominator 1 of 1 — "no consumer" reproduced at my own seat |
| 3 | Look for option A's artifacts | BOTH ABSENT — no bundle ARP row for 3.14 in HKLM / WOW6432Node / HKCU; no `python*` in `C:\ProgramData\Package Cache` |
| 4 | Pass 1 — 9 component MSIs by product code | 8 exit=0; Standard Library `{4FC6E3AE...}` exit=1603. PATH went clean, `python.exe` gone, STEP 2 passed here |
| 5 | Pass 2 — retry Standard Library with `/l*v` | exit=1603. Cause in log: `Internal Exception during install operation: 0xc00000fd` (STATUS_STACK_OVERFLOW inside msiexec) |
| 6 | Measure after pass 2 | **REGRESSION** — rollback restored `python.exe` AND both MACHINE PATH entries, but the stdlib stayed removed. Bare `python` was a 3.14 that could not boot |
| 7 | Pass 3 — remaining 8 products | 7 exit=0, `python.exe` ABSENT. Add-to-Path `{B591DE94...}` exit=1603, its 2 PATH entries survived |
| 8 | Pass 4 — OPTION B on those 2 entries | Backup written first (`%TEMP%\machine-path-backup-20260909-preB.txt`); removed ONLY the 2 Python314 entries; USER PATH re-measured untouched |
| 9 | STEP 2 re-verify on a registry-rebuilt PATH | ALL GREEN (below) |
| 10 | STEP 3 exercise both harnesses | ALL GREEN (below) |
| 11 | Report to `4.0.0_SA_CRO` + `1.0.0_SA_CTO` | DELIVERED 2/2, msg-ids 94545 / 94546, 10166 bytes each on disk |

---

## Postmortem — the bad window

**Root cause of the regression:** msiexec crashes with `0xc00000fd` while walking the Python 3.14
Standard Library MSI's file table. On that crash the rollback restored more than its own transaction —
it re-landed `python.exe` and re-ran the Add-to-Path component — while the Standard Library itself
stayed uninstalled.

| | Believed after pass 1 | True after pass 2 |
|---|---|---|
| MACHINE PATH | clean | 2 Python314 entries restored |
| `Program Files\Python314\python.exe` | absent | restored |
| Python 3.14 stdlib | removed | still removed |
| bare `python` | 3.12.10, healthy | 3.14.7, **fatal at boot** — `Failed to import encodings module` |

For that window the device was **strictly worse than at STEP 0**. It was found by exercising after
pass 2, not by assuming pass 1 held — the STEP 2 checks had genuinely passed at step 4 and would have
been a true report of a state that no longer existed. **Resolution:** passes 3 and 4, above. This is
in the report to CRO and CTO in full; a report that hid it would have left the next seat to rediscover
it from a device that looks fixed.

---

## Verification

**STEP 2 — measure-after. `$env:Path` rebuilt from the Machine and User registry values rather than
inherited, because this process still carries the stale pre-act PATH.**

```
where.exe python
  C:\Users\AndrewBerman\AppData\Local\Programs\Python\Python312\python.exe
  C:\Users\AndrewBerman\AppData\Local\Microsoft\WindowsApps\python.exe

python -c "import sys, mcp, yaml, websockets; print(sys.version)"
  3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
  no ImportError

py -0p
  -V:3.12 *   C:\Users\AndrewBerman\AppData\Local\Programs\Python\Python312\python.exe

python -c "import sys; sys.path.insert(0,'org/mcp'); import server; print('server.py imports OK')"
  server.py imports OK
```

NEGATIVE CONTROL: the same probe filtered for `Python314` returns none.
POSITIVE CONTROL: the same probe DOES return the Python312 path, so its zero is a real zero.

**STEP 3 — exercised, not import-tested.** Neither seat relaunch is mine to perform, so I exercised
the exact components that were dying, at their real entry points.

```
HARNESS 1 -- the LITERAL .mcp.json command line, spawned as a stdio child, cwd = repo root:
  python org/mcp/server.py
  initialize -> serverInfo {'name': 'opal-agent-comms', 'version': '1.26.0'}
                protocolVersion 2024-11-05
  tools/list -> 16 tools (ack_messages, check_inbox, deregister_agent, ...)

HARNESS 2 -- the Codex launcher's two FAILED COMPONENT casualties, at their real CLIs:
  python org/mcp/codex-inbox-turn-bridge.py --help  -> exit=0   (clears `import websockets` at :35)
  python org/mcp/codex-agent-heartbeat.py --help    -> exit=0   (clears `import mcp`)

Module provenance: websockets 16.0, yaml 6.0.3, boto3 1.42.54; pip list counts 310 packages
(the CRO's 310 figure reproduces on my own instrument).
```

**On this session's own still-dead client:** `opal-agent-comms` here remains CONNECTION_CLOSED, which is
why this whole session ran the broker through the Python 3.12 library fallback. That is a property of an
MCP client spawned BEFORE the act and never re-spawned — it is NOT evidence that a restart is needed.
See the Correction section: a reconnect re-spawns the server and now succeeds.

**Independent corroboration:** `1.0.0_SA_CTO` (msg 94548) re-measured from a live registry read in its
own session — a different instrument from my rebuilt process environment — and reproduced every line
of the verdict and the residue: 12 machine PATH entries with 0 matching Python314, user PATH intact,
`python.exe` absent with the directory remaining, `py -0p` listing 3.12 alone, and exactly one
remaining 3.14 ARP row. Closed at that seat.

---

## Correction — a restart is NOT required; `/mcp` reconnect is sufficient

**Superseded claim (mine, in msg 94545/94546 and in the first version of this log):** "RESTART every
Claude session started today. Do NOT `/mcp`-reconnect", on the reasoning that a reconnect re-spawns
`python org/mcp/server.py` from a process environment still holding the pre-act PATH.

**Why it was wrong:** that reasoning holds for a PATH-edit-alone fix. It does not hold here, because
this act REMOVED `python.exe`. The stale PATH still lists the two Python314 entries, but nothing
resolves at them any more, so lookup falls through to the Python312 entries behind them.
`4.0.0_SA_CRO` caught this in msg 94553 and owns the correction.

**Confirmed at the affected seat.** The CRO measured it at its own seat; this session is the actual
stale-PATH case, since its `opal-agent-comms` is CONNECTION_CLOSED. A Bash child with NO PATH
override, inheriting this process's pre-act environment:

```
PATH still lists, in this order:
  /c/Program Files/Python314/Scripts
  /c/Program Files/Python314
  /c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312/Scripts
  /c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312

which -a python   -> /c/Users/.../Python312/python      (ONE hit; the Python314 entries hit nothing)
python --version  -> Python 3.12.10
python -c "import sys, mcp; ..." -> OK 3.12.10  C:\...\Python312\python.exe
```

**Net effect on the instruction to Andrew:** a `/mcp` reconnect is sufficient for a Claude session
started after 12:30Z; a restart works too but is unnecessary. The Codex item is unchanged —
`1.0.0_SA_CTO~X` still needs a relaunch, because that seat was never provisioned and has no client to
reconnect. Correction sent to both seats as msg 94555 / 94556 after they had closed the item, because
the wrong line instructs a human act and had already been handed onward.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not stop when option A's two named artifacts were both absent | The absence was in the 3.14 install, not in my query — proven by the same census finding 3.12's bundle row. A's INTENT was reachable by product code, was reversible, and stopping would have left every Claude and Codex seat broken for a registry-shaped reason |
| Finished with option B on the one component that would not uninstall | The brief authorizes B when A is refused. A was refused, concretely and twice. Said so in the report rather than presenting a clean A |
| Did NOT retry the Add-to-Path uninstall after pass 4 | PATH is clean now, and pass 2 proved a failed uninstall here can roll back and re-add the very entries just removed. A tidy registry row is not worth re-arming that |
| Did NOT delete `C:\Program Files\Python314\` | Recursive deletion needs Andrew's explicit word per CLAUDE.md Agent Autonomy. The directory is inert — no `python.exe`, no `pythonw.exe`, verified recursively |
| Did NOT touch `C:\Windows\py.exe` | Still the 3.14.7 BUILD of the shared launcher, but it works and resolves 3.12 correctly. The brief said not to touch the Launcher, and removing it would have risked `py` for 3.12 |
| Did NOT run `start-codex-seat.ps1` or the bridge's `--preflight-only` against a real serial | Provisioning `1.0.0_SA_CTO~X` is not my lane, and a half-made seat is worse than none |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| (none in the repo) | This was a machine act — MACHINE PATH and installed products only | n/a |
| `%TEMP%\machine-path-backup-20260909.txt` | Pre-act MACHINE PATH backup | No — machine-local, outside the repo |
| `%TEMP%\machine-path-backup-20260909-preB.txt` | Pre-option-B MACHINE PATH backup | No — machine-local, outside the repo |
| this log | New | Yes — see commit |

---

## Residue, disclosed

1. **`Python 3.14.7 Add to Path (64-bit)` `{B591DE94-FC47-4AA7-BE0A-33DEE9CB8E75}` is still a
   registered product.** Its PATH effect is gone. **HAZARD:** if anything triggers MSI self-repair on
   it, the two Python314 MACHINE PATH entries can return. Falsifier, to run before believing any future
   recurrence is new — empty output means still clean:
   ```
   [Environment]::GetEnvironmentVariable('Path','Machine') -split ';' | Where-Object { $_ -match 'Python314' }
   ```
2. `C:\Program Files\Python314\` still holds directories on disk. Inert. Costs disk, not behavior.
3. `HKLM\SOFTWARE\Python\PythonCore\3.14` residue key remains, carrying no `InstallPath`. The launcher
   already ignores it — `py -0p` lists 3.12 only.
4. `C:\Windows\py.exe` is the 3.14.7 build of the launcher. Works, resolves 3.12.

---

## Blockers

None. The two remaining acts are Andrew's by the brief's own assignment, not blocks on this seat.

---

## Current State

Bare `python` on this device resolves to `C:\Users\AndrewBerman\AppData\Local\Programs\Python\Python312\python.exe`
(3.12.10, 310 packages) in any NEWLY started shell; the MACHINE PATH holds zero Python entries and the
USER PATH keeps its three Python312/Launcher entries untouched. Python 3.14.7 is uninstalled except one
inert Add-to-Path ARP row plus an empty-of-executables directory. Both dying harnesses were exercised
green: `python org/mcp/server.py` completes a real MCP handshake and serves 16 tools, and both Codex
launcher components (`org/mcp/codex-inbox-turn-bridge.py`, `org/mcp/codex-agent-heartbeat.py`) run at
exit 0. `1.0.0_SA_CTO` independently reproduced the verdict from a live registry read and closed it at
its seat (msg 94548), and `4.0.0_SA_CRO` validated and closed it independently (msg 94553); the
measurement is handed to `4.0.0_SA_CRO`, which owns the joint python answer with `1.0.0_SA_CTO~X` on
Andrew's 15:2xZ word. Already-running processes still carry the pre-act PATH, but because the fix removed
`python.exe` rather than only editing PATH, that stale PATH now falls through to 3.12 — so a `/mcp`
reconnect is enough and no restart is required. See Correction, below.

---

## Next Steps

1. **[Andrew] Relaunch `1.0.0_SA_CTO~X` with ajb2 from a NEW shell** — the launcher's "FAILED COMPONENT"
   throw must not fire, and `get_agent_status("1.0.0_SA_CTO~X")` must read LIVE with a heartbeat. This is
   the acceptance the CRO's brief reserved for the Codex harness.
2. **[Andrew] `/mcp` reconnect is SUFFICIENT for any Claude session started after 12:30Z** — a restart also
   works but is unnecessary. See the Correction section below; an earlier version of this line said the
   opposite and was wrong.
3. **[4.0.0_SA_CRO] Fold this measurement into the joint 3.12-vs-3.14 answer with `1.0.0_SA_CTO~X`** —
   delivered as msg 94545; the repo-side load-time guard remains that lane's item, deliberately untouched
   here.
