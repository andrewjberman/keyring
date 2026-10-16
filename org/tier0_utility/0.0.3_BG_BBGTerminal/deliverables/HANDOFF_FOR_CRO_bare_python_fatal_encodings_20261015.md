# HANDOFF FOR CRO -- Python314 is broken on site Z; it bites any process whose PATH misses the `~/bin` shim

**From:** `0.0.3_BG_BBGTerminal`, 2026-10-15. **For:** Andrew to hand to `4.0.0_SA_CRO`.
**Status:** symptom + narrowed cause, measured. One live consequence, already worked around on my seat.

> ⛔ **THIS FILE WAS WRONG AT ~11:45Z AND IS CORRECTED.** My first version was titled *"bare `python`
> is fatally broken"*. **It is not.** Bare `python` is healthy. **One specific interpreter is broken**,
> and which one you get depends on PATH. The original framing would have sent CRO hunting a
> machine-wide Python outage that does not exist. Correction made after measuring both interpreters
> side by side; detail below so the narrowing is auditable rather than asserted.

## The failure

A process invoking `python` **without the `~/bin` shim on its PATH** dies before executing a line:

```
Fatal Python error: Failed to import encodings module
Python runtime state: core initialized
ModuleNotFoundError: No module named 'encodings'
```

## The narrowed cause: TWO interpreters, only one broken

| interpreter | `sys.prefix` | verdict |
|---|---|---|
| `C:\Program Files\Python314\python.exe` | **`C:\Users\Opal Bloomberg\Desktop\ajb_workspace`** | ⛔ **FATAL** -- looks for its stdlib in `ajb_workspace\Lib` |
| `...\AppData\Local\Programs\Python\Python311\python.exe` | `...\Programs\Python\Python311` | OK |
| bare `python` in Git Bash | resolves via `/c/Users/Opal Bloomberg/bin/python` -> **Python311** | OK |

**Python 3.14 adopts the workspace as its prefix.** From its own fatal dump:
`sys._base_executable = C:\Program Files\Python314\python.exe` but
`sys.base_prefix = sys.prefix = C:\Users\Opal Bloomberg\Desktop\ajb_workspace`, stdlib dir
`ajb_workspace\Lib`, and `sys.path` = `[Python314\python314.zip, ajb_workspace, ajb_workspace\Lib,
C:\Program Files\Python314]`. The repo's `Lib/` exists and holds our own modules (`devices.py`,
`lgctfm_render.py`, `opal_data_harvest/`, `__pycache__/`) -- no `encodings`, hence the fatal.

**So the determining factor is PATH, not cwd.** CLAUDE.md already records that *"shims reach shells via
`~/bin` FORWARDERS (profiles never load)"*. A shell that has the forwarder gets Python311 and works; a
process whose PATH lacks it falls through to Python314 and dies.

## Ruled out by measurement

- No `pyvenv.cfg` in the workspace root (`ls` -> No such file).
- No `python*._pth` in the workspace root.
- `PYTHONHOME` / `PYTHONPATH` unset in my Git Bash shell.
- **`ajb_workspace\Lib` is not new** -- mtime 2026-10-14 18:21, and bare `python` worked repeatedly
  after that (including `freshness_check.py` and `lib/trading_calendar.py` from the workspace root at
  11:11Z today). **`Lib/` is necessary but not sufficient;** the interpreter choice is the other half.

## Still open for CRO -- the two I could not close

1. **WHY does Python314 resolve its prefix to the workspace at all?** `Lib/` adjacency alone should not
   do it from an arbitrary cwd, and I reproduced the fatal from `C:\` as well as from the repo. Suspects
   I did not confirm: a stray `python314._pth` under `C:\Program Files\Python314`, a registry
   `PythonPath`, or a machine/service-scope `PYTHONHOME`. **First read: `dir "C:\Program Files\Python314"`
   for `._pth` / a missing `Lib`.**
2. **Is `ajb_workspace\Lib` a good idea at all?** A top-level directory named `Lib` in a repo that
   agents `cd` into is a loaded gun for any Python that consults prefix-adjacent paths. Renaming it
   (e.g. `oplib/`) may remove the class rather than the instance. **Not my call -- it is a repo-wide
   rename with importers to follow.**

## The live consequence, and the workaround I applied

**My Teams inbox watcher died `exit 1` on arm** (task `bu9bon6km`) -- the Monitor's environment lacks
the `~/bin` forwarder, so its bare `python` was Python314. No `[TEAMS-ARMED]` receipt arrived, which is
the only reason I noticed; a silent arm is a deaf seat. **I was deaf on Teams ~11:4xZ to 14:28Z
(~2h45m).** Nothing was lost -- a direct poll since the last served message returned 0.

**Workaround, now live:** pin the interpreter in the arm line instead of trusting PATH --
`timeout 1770 "/c/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311/python.exe"
.claude/skills/teams-assist/teams-watch.py --server opal-gateway-bbg --identity 517aa5ee-... --channels
...`. Armed and receipted (`pid 35768`, `channels=1`). **This deviates from the canonical arm line in
`.claude/skills/bbg-teams-assist/SKILL.md:35`, which uses bare `python`.** I cannot edit that file from
this seat (deliberately unwritable). **Recommend the canonical line pin the interpreter** -- otherwise
every seat arming a Python Monitor is one PATH difference away from a silent deaf window.

## NOT affected -- and this matters for the incident it did not cause

**The Bloomberg pipeline uses explicit interpreter paths, never bare `python`:**
`scheduled_daily_pull.cmd` sets `PY=C:\Anaconda\envs\cma\python.exe` and
`PY_AWS=...\Python311\python.exe`. The 11:00Z scheduled run executed normally (it failed on the DAPI
precondition -- a separate matter, now resolved). **This defect did not cause today's pull failure.**

**Severity, my read:** MEDIUM-HIGH for agents, NIL for the data pipeline. It converts a Python-based
Monitor into a dead watch with no loud signal, and the blast radius is "every process whose PATH lacks
the forwarder" -- which is not a set anyone has enumerated.
