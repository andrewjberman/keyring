# Bloomberg Terminal — sign-in recovery after a crash / logout

**Authored:** 0.0.3_BG_BBGTerminal, 2026-08-11, off the live recovery at ~0845-0852Z.
**Trigger:** Andrew-direct via Teams 2026-08-11 08:44:06Z — *"figure out a solution to manually
sign in to Bloomberg"* after the 08-10 ~2023Z antivirus crash left the Terminal down ~12.5h.
**Status:** EXERCISED end-to-end on this box; the Terminal was signed in and the pull path
verified by running it, not by reading config.

---

## Why this document exists

`bbcomm` restarts on its own after a crash — **so the box looks half-healthy and is not.**
Measured this incident: `bbcomm` came back at 17:20 ET (21:20Z) while `wintrv.exe` (the
Terminal itself) never did. Nothing on the box reports that gap, and the 07:00 ET scheduled
pull would have run against a dead DAPI. **A running `bbcomm` is not a running Terminal.**

## Preconditions

| # | Check | Command / expectation |
|---|---|---|
| P1 | An **interactive console session** exists | `query session` -> a `console` line, `Active`. GUI sign-in has nowhere to go without it; a services-only session cannot be driven. |
| P2 | Credentials in hand | The Terminal login is a **person's** Bloomberg login (this box: the daily-pull user). See CREDENTIAL HANDLING below — do not source it from a chat thread as routine. |
| P3 | Terminal not already running | `Get-Process wintrv` empty. If it IS running, you have a different problem (logged out vs not launched). **P3 IS NOT A GREEN LIGHT — P0 BELOW OVERRIDES IT.** |

### ⛔ P0 — RUN THIS FIRST. An absent `wintrv.exe` is NOT evidence you need to sign in.

**Added 2026-08-12, measured, after the 0752Z RMM reboot.** `wintrv.exe` was absent all morning —
only `bbcomm.exe` + `blpcrashmon.exe` running (denominator: 316 processes on the box, exactly 2
Bloomberg ones) — **and the entitlement was live the whole time.** The 07:00 ET scheduled pull
produced correct login-scoped CIX data with no GUI and no agent anywhere in the path.

**So the two process readings are each non-discriminating, in opposite directions:**

| Date | `bbcomm` | `wintrv` | `bloomberg_health` | Entitlement | Lesson |
|---|---|---|---|---|---|
| 2026-08-11 | up | **dead** | `ok:false` | **DEAD** (12.5h) | a running `bbcomm` is **not sufficient** |
| 2026-08-12 | up | **absent** | `ok:true` | **LIVE** | a running `wintrv` is **not necessary** |

`bloomberg_health` read cleanly through *both* states, so **it cannot discriminate either** — it is
an instrument that could not have said otherwise. Neither the process list nor the health check
answers "is the entitlement live."

**THE ONLY TEST THAT HAS EVER DISCRIMINATED — resolve the `.ST` custom index.** CIX resolution is
terminal/login-scoped, so a correct series is the sole evidence that an entitled session backs
`bbcomm`. Run it through the **pull's own interpreter** (`C:\Anaconda\envs\cma\python.exe`), three
layers, and run the generic-ticker control as a **separate request** so a CIX failure cannot be
blamed on a dead transport:

1. `blpapi.Session` + `openService("//blp/refdata")` — transport.
2. `SPX Index` HistoricalDataRequest returns rows — positive control.
3. `.ST Index` HistoricalDataRequest — **PASS = ~683 rows, inception `2023-12-29` @ `100.0000`.**

**If layer 3 passes, STOP. Do not launch `wintrv`, do not sign in. There is nothing wrong.**

**Why this gate exists and is not pedantry:** a sign-in attempt is *not free*. The 08-11 recovery
below burned a failed login attempt, and **Bloomberg locks the account on repeated failures** —
so acting on the absent-`wintrv` false premise converts a non-problem into a lockout and a support
call. The wrong inference here is the natural one, which is exactly why it needs a gate rather
than a caution.

⚠ Retrieval trap when you check the pkl instead of the wire: `.ST` lives in the **`bbg_ticker`**
column, **not** `index_name` (which carries `Short Term`). Filtering the wrong column returns a
clean empty set that reads as *absence* and sends you hunting a defect that does not exist. Print
the denominator and a positive control beside any zero.

*Known mis-resolution shape (2026-08-03): ~1449 rows at price ~1.9. It passes every row-band and
shape gate the tripwire applies — which is why the tripwire structurally cannot catch it, and why
this content check is run by hand after any pull that crossed a reboot or a fresh login.*

## Procedure

1. **Launch the Terminal**
   `Start-Process "C:\blp\Wintrv\wintrv.exe" -WorkingDirectory "C:\blp\Wintrv"`
   Give it ~12s. Expect `wintrv` + `blpsmarthost` + several `blpwtk2_subprocess` (the
   Chromium-based SmartClient UI).

2. **Find the login window — NOT via `MainWindowHandle`.**
   `wintrv`'s `MainWindowHandle` is **0**; the login window belongs to a separate
   SmartClient pid. Enumerate visible top-level windows and match the title
   **`BLOOMBERG: Login`** (`EnumWindows` + `GetWindowText`). Working snippet in the session
   log for 2026-08-11. *Going straight to `Get-Process wintrv | MainWindowHandle` fails and
   looks like "no window exists".*

3. **Focus it, and VERIFY the focus took** — `SetForegroundWindow`, then read
   `GetForegroundWindow()` back and compare. **Abort if it does not match.** Never send
   keystrokes to a window you have not confirmed is focused: the keystrokes are a password.

4. **Fill the fields by DIRECT CLICK on each — never `{TAB}` between them.**
   `{TAB}` from Login Name does **not** land on Password on this dialog (it moves into the
   language selector). Measured consequence: the password was typed into the **unmasked
   Login Name field**, displayed in plaintext on screen, and burned a failed login attempt.
   Click coordinates on this box's layout (1920x1080 primary, dialog centred):
   Login Name `(659, 348)` · Password `(659, 426)` · Login button `(590, 482)`.
   Clear each field first (`^a` then `{DELETE}`) — a retry inherits the previous contents.

5. **VERIFY BEFORE SUBMITTING.** Screenshot the dialog and confirm Login Name shows the
   username and Password shows a masked dot-count matching the credential length. **Bloomberg
   locks accounts after repeated failures — an unverified submit risks a lockout that turns a
   12-hour outage into a support call.** Only click Login once the fields read correctly.

6. **Confirm on BOTH layers — neither alone is sufficient:**
   - Port: `Get-NetTCPConnection -LocalPort 8194` -> `Listen` (owned by the `bbcomm` pid).
   - MCP: `bloomberg_health` -> `ok: true`, service `//blp/refdata`.
   - **The pull interpreter (the one that matters):** the MCP server runs under a DIFFERENT
     Python than the pull, so a green `bloomberg_health` does NOT prove a runnable pull. Open
     a real session from the pull env:
     `C:\Anaconda\envs\cma\python.exe` -> `blpapi.Session` start + `openService("//blp/refdata")`.
     Script: `scratchpad/cma_connect_check.py` pattern (session connect, no data request).
     **A bare `import blpapi` is NOT this check** — an import proves the package is installed
     and answers nothing about reachability.

## Observed this run

No second factor (no B-Unit / biometric prompt) — username + password went straight through
to a live Terminal. **Do not generalise that to every login**; Bloomberg can demand B-Unit or
a Bloomberg Anywhere confirmation, and if it does, the sign-in needs the human who holds it
and this procedure stops at step 5.

## CREDENTIAL HANDLING (the part to fix)

The credential reached this seat as **plaintext in a Teams message** — it is now permanent,
searchable and backed up in the chat store, and it passed through an agent transcript.
Recommended to Andrew in-thread: **rotate it, keep the new value in AWS Secrets Manager**
alongside `opal/mcp/opalbloomberg-login` (the pattern already used for this seat's own
login — secret NAME citable, VALUE never), and delete the messages.
**The value is not recorded in this document, in the session log, or in any thread file, and
must not be.**

## The gap this recovery does NOT close

**Nothing detects a dead Terminal.** This outage was found only because a human asked how
things were going ~12.5h in. The 07:00 ET pull has no precondition check on DAPI liveness, so
with the Terminal down it fails (or worse, produces nothing) on a schedule nobody is watching.
Fixing that is a **route/schedule design question, not a monitor** — per the standing alarm
moratorium, do NOT reach for an alarm here. Routed to MSTR~Z for CTO/Andrew disposition.
