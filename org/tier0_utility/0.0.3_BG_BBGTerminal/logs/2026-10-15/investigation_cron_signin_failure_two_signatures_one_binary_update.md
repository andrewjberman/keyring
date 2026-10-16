# Investigation: why the 07:00 ET cron's sign-in has failed since 10-06 -- TWO signatures, one binary update, and it is NOT Python

**archetype:** DIAGNOSE
Andrew-direct, Teams 2026-10-15T17:13:06Z: *"Go figure out why the cron script is failing, if its a
python package issue, path issue, or whatever the case may be. Be comprehensive, and report back."*
Acked 17:14:25Z.

## HEADLINE

**Not Python. Not PATH.** The cron's Python half is healthy and pins its own interpreter. The failure
is **GUI automation against a Bloomberg Terminal whose executables were replaced on 10-06 at
04:04Z** -- and it is **two distinct signatures in sequence**, not one fault. The first was fixed; the
second is live and **already owned and instrumented by `0.7.0_AE_CloudOps~ZS`** under OPAL_BBGTML
Z6-R3/R7. **Tomorrow's 07:00 fire will name the remaining cause** -- the instrumentation for it landed
today at 14:30Z, ~7.5 h after this morning's run.

## 1. The denominator and the signature distribution -- 5 failures, 2 causes

Read every 07:00 log since the break. **N failures is not N causes:**

| morning | fill verdict | abort | signature |
|---|---|---|---|
| 10-06 | **VERIFY FAIL x3** -- `username glyph-runs 10 outside 11..12` | pre-submit, 0 attempts | **A** |
| 10-08 | window-not-found x1, then **VERIFY FAIL x2** -- same `glyph-runs 10` | pre-submit, 0 attempts | **A** |
| 10-11 | **VERIFY PASS** | `focus lost before submit` | **B** |
| 10-13 | **VERIFY PASS** | `focus lost before submit` | **B** |
| 10-15 | **VERIFY PASS**, then re-fill | `focus lost before submit`, re-fill `focus did not take (fg=32116010 != 266432)` | **B** |

**They are SEQUENTIAL, not interleaved** -- A on 10-06/10-08, B on 10-11 onward. So A was addressed
and B was either exposed by the fix or always second in line. **Signature A's measurement was
identical every time (exactly 10, never 9 or 11), which is a calibration mismatch, not flakiness.**

## 2. The trigger: a BINARY Terminal update at 10-06 04:04Z -- with a negative control

| evidence | reading |
|---|---|
| `C:\blp\Wintrv\wintrv.exe` mtime | **2026-10-06 00:04:08 local = 04:04:08Z** -- the Terminal's own main executable, replaced |
| `blpcrashmon.exe` mtime | 10-06 04:03:55Z -- same event |
| files written under `Wintrv` on 10-06 | **203**, ALL in hour 00 local (04:xxZ) |
| their composition | **155 `.dll` + 35 `.exe`** = 190 binaries, plus 8 `.b`, 2 `.db`, 2 `.dat`, 1 `.upd` |

⭐ **THE NEGATIVE CONTROL, which is what makes this causal rather than coincidental.** A larger Wintrv
write happened on **09-24: 965 files** -- and the unattended sign-in **kept working five more times
after it** (09-27, 09-29, 10-01, 10-02, 10-04). Its composition was **892 `.pak` + 44 `.dll` + 6
`.exe`** -- a RESOURCE update. **So "Wintrv changed" does not break the fallback; replacing 190
EXECUTABLES does.** One changes content, the other changes the UI's code: window classes, control
geometry, text rendering and focus behaviour -- precisely the two things that broke.

⚠ **Correcting the handoff I gave earlier:** I first read `C:\blp\Wintrv`'s DIRECTORY mtime (10-06
18:26 local) and treated ZB's "04:04Z" as imprecise. **The directory mtime was the misleading
instrument** -- a later touch. The 203 files are all at 04:xxZ and `wintrv.exe` is 04:04:08Z. **ZB's
timestamp was exactly right.**

## 3. ANDREW'S QUESTION ANSWERED: it is not Python, and not PATH

**The cron's chain:** `scheduled_daily_pull.cmd` -> `bbg_credentials.py` -> `powershell -File
bbg_fallback.ps1` -> `bbg_signin.ps1`.

| check | result |
|---|---|
| interpreter the cmd uses | `set "PY=C:\Anaconda\envs\cma\python.exe"` -- **explicitly pinned, never bare `python`** |
| that interpreter's health | Python **3.13.2**, `prefix = C:\Anaconda\envs\cma` -- correct, not the workspace |
| `bbg_credentials.py` imports | `__future__, hashlib, json, os, subprocess, sys` -- **100% stdlib, zero third-party** |
| did the Python half run every morning? | **Yes** -- every failed log contains `[fallback]` output, which only exists downstream of the credential wrapper launching PowerShell |

**There is no package to be missing and no PATH to resolve wrong.** The Python half worked on all five
failed mornings; the failure is strictly after it, in the GUI phase.

⚠ **AND A TRAP WORTH NAMING, because it would send a fixer the wrong way.** There **IS** a real Python
defect on this box today -- `C:\Program Files\Python314\python.exe` resolves `sys.prefix` to the
workspace root and dies `ModuleNotFoundError: No module named 'encodings'`; it killed my own Teams
watcher. **It is NOT this failure.** The cron never invokes bare `python`. Separate handoff:
`deliverables/HANDOFF_FOR_CRO_bare_python_fatal_encodings_20261015.md`. **Two Python-shaped facts on
one box on one day; only one is the cron's.**

## 4. Signature A, and why it stopped

`VERIFY: FAIL username glyph-runs 10 outside 11..12`. The verifier counts glyph runs in the username
field and expects 11-12 for the 12-character login; the reference fixture renders 11. It read **10**,
identically on every attempt across two mornings. **A binary update that changes font rendering or
field metrics shifts that count by one -- which is what a 10-vs-11 is.** It is a CALIBRATION
mismatch between the verifier's fixture and the post-update UI, not a bad fill. **Precedent in the
runbook:** the 08-16/17 failures were the same class -- the fill always worked and the VERIFIER was
mis-aimed, and the lesson recorded then was *"`dots:1/user:''` from the verifier is NOT evidence the
fill failed. READ THE SCREENSHOT."* Signature A is that lesson recurring against a new UI build.

## 5. Signature B is the LIVE blocker, and the cause is instrumented but not yet captured

`VERIFY: PASS` (9/9 dots, OCR 100%) then `focus re-assert 1/3, 2/3, 3/3 did not take` ->
`ABORT: focus lost before submit`. The script's submit phase re-asserts foreground up to 3 times and
**refuses to type a password into a window it cannot verify** -- correct behaviour, 0 attempts spent.

**What is known:** the contention is **TRANSIENT**. At abort, `fg=32116010 != 266432`; at 14:3xZ I
measured the foreground **and it was the login window itself** (hwnd 266432, pid 5276, `bplus64`,
"BLOOMBERG: Login"), with the console session `Active`. So something seizes foreground during the
fill-to-submit gap and later releases it.

**Ruled out:** no third-party scheduled task fires in the window -- the only tasks near 07:00 ET are
`Office Feature Updates` (06:10) and the two OPAL tasks. **So it is not a co-scheduled job.**
**Remaining prime suspect:** the updated `wintrv.exe`'s own startup sequence spawning a second window
after the login dialog appears -- which fits both the 10-06 trigger and the transience.

⭐ **It will be NAMED tomorrow, and that is a dated expectation rather than a hope.**
`0.7.0_AE_CloudOps~ZS` landed **R7 (TO-Z6-R7) at 10-15 10:30 local = 14:30Z**: *"foreground trace at
every focus abort."* `Get-FgTrace` appears **5 times** in the working-tree `bbg_signin.ps1` and prints
one ASCII line naming the foreground process, title, session and lock state at every focus abort. **On
this box an edit IS a deploy** (the task runs the working tree). **This morning's 07:00 run predates
it by ~7.5 hours, which is exactly why today's log has no trace.** The next fire captures it.

## 6. What I did NOT do, and why

**I did not attempt a reproduction.** The safe-looking path is `-ForceDown -DrySubmit` (TEST-ONLY
switches that exercise the down-path guards without touching live DAPI or the ledger) -- **but the
Terminal is currently logged IN and serving T-1 data.** A fill phase hunts a `BLOOMBERG: Login`
window that does not exist while logged in, so it would abort "window not found" and teach me nothing
about focus, while poking a live serving session. **Low information, non-zero risk, and the real
instrument fires tomorrow anyway.**

## 7. Ownership and what I recommend

- **Owner exists: `0.7.0_AE_CloudOps~ZS`**, OPAL_BBGTML Z6-R3 / Z6-R7. Commits 10-13 17:10, 10-14
  05:31, 10-15 10:30. **No new row needed and I filed none** -- ZB also holds `Z-S23`
  (`org/surprise_channel/OPAL_BBGTML/INVESTIGATION_v1.md` @eb80f77d65) for the 10-06 regression.
- **Recommend to the owner, as data not direction:** (a) read the R7 trace off the next failing fire
  before changing anything else; (b) if the thief is a `wintrv` child, a settle-until-stable-foreground
  loop will beat a fixed 3-try re-assert; (c) **re-check signature A's glyph tolerance against the
  post-10-06 build** -- it currently passes, but nothing recorded says the fixture was re-derived
  rather than the band widened, and a tolerance widened to swallow a rendering change can swallow a
  real mis-fill later.
- **Operationally until fixed:** the 07:30 backstop catches it every time and summons; the cost is a
  human sign-in per overnight-expiry morning, and a stale dashboard until someone acts.

## Compiler Tools

| tool | result | read |
|---|---|---|
| 5 x `07:00` pull logs, full fallback blocks | 2 signatures, sequential | **This is the whole investigation.** A per-morning "it failed" count would have reported 5 identical failures and hidden the 10-08/10-11 transition. |
| `Get-ChildItem Wintrv -Recurse` grouped by date AND extension | 10-06 = 203 files / 190 binaries; 09-24 = 965 files / 892 `.pak` | The **extension** breakdown is what made 09-24 a negative control instead of a louder version of the same thing. |
| `Get-Item wintrv.exe` | mtime 04:04:08Z 10-06 | Confirmed ZB's timestamp and corrected my own directory-mtime misread. |
| `Get-ScheduledTask` triggers filtered to T06/T07 | 3 tasks, none third-party in the window | Rules out a co-scheduled focus thief. |
| cma interpreter + AST import scan of `bbg_credentials.py` | 3.13.2, correct prefix; imports 100% stdlib | **Answers Andrew's question.** My own `importlib.util` probe errored (I failed to import the submodule) -- the AST list is what carries the conclusion, and it needs no probe. |
| `git log` on the two auth scripts | ZS active 10-13/10-14/10-15; R7 trace at 14:30Z | Found the owner and the dated expectation. Prevented me filing a duplicate row. |

---

# OUTCOME, 19:51-20:10Z -- routed on Andrew's word, CTO ruled, fix lands tonight

**Andrew-direct 18:00:40.595Z:** *"send this log to CTO and have them fix it."* Record:
`deliverables/ANDREW_DIRECT_20261015_1800Z_SEND_CRON_LOG_TO_CTO_AND_HAVE_THEM_FIX_IT.md`.

**Relayed to `1.0.0_SA_CTO~Z` 19:51:41Z, DELIVERED.** Carried the log path, his words verbatim, the
two-signature finding, the 10-06 trigger with its 09-24 negative control, and the not-python result.
**Scope relayed, not adjudicated:** I knew CloudOps~ZS already owned the defect and did NOT re-route
to ZS to save a hop -- but I put the ownership fact first, since the CTO assigning on top of a live
task order was the real risk.

**CTO~Z ruling @079108405c (msg 34565, acked):** COO~ZB cuts **R8** for CloudOps~ZS tonight, landing
before the 07:00 ET fire.

| change | detail |
|---|---|
| submit | **settle-until-stable-foreground**, bounded 90 s, 2 s stable required, **still 0 attempts on abort** |
| verify | **re-derived glyph fixture** |
| R7 | foreground trace **stays** |

⭐ **Both cautions I passed as data were adopted -- (b) and (c) explicitly.** The second is the one
that mattered: the glyph check currently PASSES, so there was no pressure to touch it, and nothing
recorded said whether the fixture had been re-derived or the band merely widened. **A band widened to
absorb a rendering change keeps passing a genuinely wrong fill later** -- the failure would have moved
from loud (verify aborts) to silent (verify approves a bad password). Re-deriving removes that.

**Tomorrow's 07:00 ET fire is the proof, and it is informative either way:** unattended success would
be the first since 10-04; failure yields the R7 trace naming the foreground thief. **There is no
branch where tomorrow teaches nothing** -- which is the property a good next step has.

**Owed by me:** read the 10-16 11:00Z result and report. Nothing tonight. Status given to Andrew
20:10:39Z (msg `1792095039653`).
