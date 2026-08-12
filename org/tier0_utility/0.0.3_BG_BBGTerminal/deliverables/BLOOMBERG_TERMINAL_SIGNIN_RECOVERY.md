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

| When | `bbcomm` | `wintrv` | `bloomberg_health` | Entitlement | Lesson |
|---|---|---|---|---|---|
| 2026-08-11 | up | **dead** | `ok:false` | **DEAD** (12.5h) | a running `bbcomm` is **not sufficient** |
| 2026-08-12 **AM** (07:00–09:26) | up | **absent** | `ok:true` | **LIVE** | a running `wintrv` is **not necessary** |
| 2026-08-12 **PM** (13:16→) | up | absent | `ok:false` | **DEAD** (transport) | `wintrv` absent in **both** 08-12 rows — so it explains **neither** |

**Read all three rows, not the middle one alone.** `wintrv` was absent across the whole of 08-12 —
through a working DAPI *and* a dead one. **A variable that is constant across both outcomes explains
neither**, which is the entire basis of this gate. The morning row is what proves `wintrv` is
unnecessary; the afternoon row is what proves its absence is not *reassuring* either. Both halves
are needed, and a two-row version of this table (which is what stood here until 17:30Z) invites the
reader to conclude the day had one state when it had two.

**⚠ CORRECTED 2026-08-12 — the sentence that stood here was FALSE, and it was the dangerous
direction of false.** It read: *"`bloomberg_health` read cleanly through both states, so it cannot
discriminate either — an instrument that could not have said otherwise."* **Read the table above:
`ok:false` then `ok:true`. Health DISCRIMINATED CORRECTLY, 2 for 2.** I wrote that health returned
`ok:true` in both rows; the 08-11 log records `ok:false` throughout that outage. Caught by
`4.0.0_SA_CRO~Z` (172332Z), who noticed the prose contradicted the table directly beneath it.

**Why this mattered more than an inaccuracy:** the prose half is what propagates. It reached
MSTR~Z's standing note and CRO~Z's spawn briefing, and on 2026-08-12 CRO~Z measured a genuine
`ok:false` **twice** and partly talked themselves down from it *on the strength of that sentence*.
**A record that makes a WORKING instrument look useless is the mirror of the failure this file
exists to prevent: it does not manufacture a false alarm, IT SUPPRESSES A TRUE ONE.**

### What `bloomberg_health` actually answers — NECESSARY, NOT SUFFICIENT

| Reading | What it establishes | What it does NOT |
|---|---|---|
| `ok:false` | **Real evidence the TRANSPORT is down.** Act on it. | — |
| `ok:true` | A blpapi session opens on 8194. | Nothing about **login state** or **CIX entitlement** |

**⚠ DO NOT OVER-CORRECT THIS INTO "health is unreliable." IT HAS NEVER BEEN OBSERVED TO LIE.**

| When | Reading | Truth | Verdict |
|---|---|---|---|
| 2026-08-11 outage | `ok:false` | entitlement dead | **correct** |
| 2026-08-12 ~09:16–09:26 | `ok:true` | entitlement live | **correct** — independently corroborated by the 3-layer probe, not assumed |
| 2026-08-12 ~13:16 onward | `ok:false` | transport dead | **correct** — confirmed at three seats |

**3 for 3.** The precise claim is that health is insufficient **in principle** — it structurally
cannot see login state — **not** that it is unreliable in practice. The failure mode it permits
(session opens, entitlement dead) is **UNOBSERVED, not demonstrated**; the 2026-08-03 CIX
mis-resolution is the shape that would produce it, which is why `.ST` exists.

**The reason this warning is here:** the sentence this section replaced made a *working* instrument
look useless, and a correction that overshoots into "health tells you nothing" reproduces exactly
the same harm with better intentions — the reader still ignores a correct `ok:false`, just for the
opposite stated reason. **Act on `ok:false`. Treat `ok:true` as necessary-not-sufficient and
confirm entitlement with `.ST`. Never "health is unreliable."**

Source-confirmed at `.tools/bloomberg-mcp/blp_client.py:7-11` — exercised with the GUI **exited**
and the user **logged out**: `bbcomm` kept 8194 listening and `reference_data` kept returning live
data (USDCAD ticked across the logout). **So the dependency is `bbcomm`, not the GUI and not an
interactive login — and health is blind to LOGIN STATE, not to transport.**

Same file, `:15-17`, records what is still open: *"STILL UNPROVEN (deliberately not tested, Andrew
2026-07-30): whether bbcomm comes up entitled from a COLD BOOT with no login at all. 'Survives
logout' and 'never needs a login' are different claims; only the first is established."*

So the correct reading of the two rows: **the process list does not discriminate (both
directions), and health discriminates TRANSPORT only.** Neither answers "is the CIX entitlement
live" — that is what `.ST` is for.

**THE ONLY TEST THAT HAS EVER DISCRIMINATED — resolve the `.ST` custom index.** CIX resolution is
terminal/login-scoped, so a correct series is the sole evidence that an entitled session backs
`bbcomm`. Run it through the **pull's own interpreter** (`C:\Anaconda\envs\cma\python.exe`), three
layers, and run the generic-ticker control as a **separate request** so a CIX failure cannot be
blamed on a dead transport:

1. `blpapi.Session` + `openService("//blp/refdata")` — transport.
2. `SPX Index` HistoricalDataRequest returns rows — positive control.
3. `.ST Index` HistoricalDataRequest — **PASS = ~683 rows, inception `2023-12-29` @ `100.0000`.**

**If layer 3 passes, STOP. Do not launch `wintrv`, do not sign in. There is nothing wrong.**

#### If layer 1 FAILS — added 2026-08-12, and this half was MISSING

The gate above guarded only the over-reacting direction. It told you what to do when the
discriminator PASSES and said **nothing** about a layer-1 failure, which is the same asymmetry as
the health-prose defect one level up: **silent on the true alarm.** A transport failure is *not*
the "absent `wintrv`" false premise — it is independent, measurable evidence of a real fault.

**Work the cheap, reversible remedies first and record which you eliminated.** Exercised
2026-08-12 in this order:

1. **Re-probe 8194** — 3+ probes, seconds apart. A single read can be unlucky; a sustained absence
   is a finding. (`Get-NetTCPConnection -LocalPort 8194 -State Listen`)
2. **Restart `bbcomm`** — stop the pid, relaunch `C:\blp\DAPI\bbcomm.exe`. Recoverable and cheap;
   it relaunches on demand anyway. *Result 2026-08-12: new pid, still no listener — **eliminated**.*
3. **Test the network to Bloomberg** — `Test-NetConnection 69.187.48.83 -Port 8194`, **with an
   unrelated control** (`8.8.8.8:53`). Do not skip the control: "the far end is down" and "this box
   has no network" are different faults with different owners. *Result 2026-08-12:
   `TcpTestSucceeded True`, control passed — **network eliminated**.*
4. **Check `bbcomm`'s own outbound sockets** (`Get-NetTCPConnection -OwningProcess <pid>`). Healthy
   looks like `…:8197 -> 69.187.48.83:8194 ESTABLISHED`. *Result 2026-08-12: **loopback only** — up
   but not connecting, with the path provably open.*

**Only after 1–4 are eliminated is the sign-in the candidate remedy**, and this seat **cannot
complete one alone**. **Surface it with the eliminations attached and hold.** Do not attempt a login
to "just try"; that is the lockout risk the P0 gate exists to prevent, and it does not stop being a
risk because the fault is real this time.

##### What the blocker actually is — CORRECTED 2026-08-12, and the wrong version reached Andrew

**This paragraph previously read "the MFA/OTP goes to Andrew's phone," cited to `prompt.md`. That
was an IMPORT FROM A DIFFERENT LOGIN SYSTEM.** `prompt.md:15-27` is entirely about
**`opal-gateway-bbg` — the MS Entra delegated-OAuth identity**, whose credential is
`opal/mcp/opalbloomberg-login` in Secrets Manager and whose "surface the auth URL" flow is a
**browser consent**. **None of it describes the Bloomberg Terminal login.** Caught by
`0.0.0_AB_MSTR~Z` (173940Z) after Andrew asked *"What do you mean bloomberg needs my phone?"* —
i.e. **the error had already reached him as an action item.**

**The honest epistemic position, which is more useful than either version:**

| Claim | Status |
|---|---|
| The credential is a **person's Bloomberg login**, and this seat may not source it from a chat thread as routine | **Binding** (see CREDENTIAL HANDLING below) |
| A second factor **MAY** fire — Bloomberg can demand B-Unit / Bloomberg Anywhere confirmation | **Possible, unquantified** |
| The **one measured Terminal login** (2026-08-11) required **NO** second factor | **Measured** — this file's own "Observed this run" |
| "The MFA goes to Andrew's phone" | **UNSUPPORTED for the Terminal.** True of the *gateway OAuth* identity only |

**So the ask to Andrew is the CREDENTIAL — not "stand by with your phone."** Those are different
asks with different lead times, and the wrong one was escalated on 2026-08-12.

**The provenance IS the finding, not the sentence.** A true constraint on the **M365 gateway**
identity was carried verbatim into a **Bloomberg Terminal** runbook, where it was never verified —
and it then contradicted this file's own measured observation ~70 lines further down. **Two login
systems, one seat, similar-sounding words: check which system a constraint was measured against
before importing it.**

**Note the asymmetry that makes both halves necessary:** an absent `wintrv` alone → **do nothing**.
A measured transport failure with 1–4 eliminated → **escalate**. The same file has to say both, or
it will reliably produce one of the two errors.

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
(secret NAME citable, VALUE never), and delete the messages.
**The value is not recorded in this document, in the session log, or in any thread file, and
must not be.**

### ✅ STATUS 2026-08-12 ~1948Z: **CLOSED BY ANDREW'S DECISION — accept the credential as-is.**

Put to him by `4.0.0_SA_CRO~Z` as a two-option card (rotate / accept), with the full context: the
value sits in a Teams thread (permanent, searchable, backed up), in Secrets Manager, and in two
agent transcripts. CRO~Z recommended rotate, low urgency. **Andrew-direct, verbatim: *"Call 1 A,
Call 2 B"* → (b) ACCEPT.** Durable record @4b7cc7b4c1.

**The recommendation is discharged by a sovereign decision — NOT because the exposure went away and
NOT because the finding was wrong.** The 08-11 finding stands exactly as recorded above; he has
**accepted the residual risk** with the facts in front of him. Those are different closures and the
distinction is the point: a future reader must not infer that the exposure was re-measured and
found benign.

**⛔ SCOPE BOUND — his word binds the addressed question, verbatim, nothing wider.** This closes the
rotation question **for THIS credential only**. It is **not** a general ruling on credential
handling, **not** licence to place other secrets on chat surfaces, and **not** a reversal of the
guidance in this section for **future** credentials — which **stands unchanged**.

**Where the credential now lives:** `bloomberg/terminal/login` in AWS Secrets Manager (created by
CRO~Z 2026-08-12, round-trip verified without printing either value). Independently confirmed to
exist from this seat by `describe-secret` — **metadata only, with a negative control**; the value
was not read. **Deliberately named far from `opal/mcp/opalbloomberg-login`**, and its own
description carries the disambiguation. `integrations/bloomberg/auth/bbg_credentials.py` resolves it
into a child-process environment and has **no mode that prints it**.

**This changes nothing about the daily pull:** it authenticates to nothing and rides the logged-in
Terminal entitlement via `bbcomm`. The secret exists for the DAPI-down sign-in protocol only.

### ⛔ NAME COLLISION — `opal/mcp/opalbloomberg-login` IS **NOT** THE BLOOMBERG CREDENTIAL

It is the **MS Entra** login for this seat (`opal-gateway-bbg` identity, OTP-to-Andrew MFA) — a
**Microsoft** credential that happens to be named for the Bloomberg seat. **Anyone sent to find
"the Bloomberg credential" lands on it, and it is the wrong one.** The only other keyword match,
`opal/portal/svc-data-refresh`, is a portal service credential whose *description* mentions
OPAL_BBGTML — also not a Terminal login.

*This section previously cited `opalbloomberg-login` as "the pattern already used for this seat's
own login," which fed the very collision it now warns about. Removed.*

**This is the same defect as the imported-MFA error above, arriving from the opposite direction** —
that one carried an Entra *rule* into a Terminal runbook; this one is an Entra *secret name* that
reads as Bloomberg. Found independently, from the Secrets Manager side, by someone who had not seen
that correction. **Two directions onto one collision is evidence it is structural, not careless:
this seat holds two authentication systems whose names do not distinguish them.**

**Consequences if resolved wrongly:** a failed Bloomberg login (the P0 lockout risk), or an Entra
secret handled as a Terminal secret. **A rename/description that disambiguates is Andrew's and
CTO's call — named here, not proposed as work.**

**Custody, not automation** (CRO~Z to Andrew, and it is right): the pull authenticates to *nothing*
— it rides the logged-in Terminal's entitlement via `bbcomm` on `127.0.0.1:8194`
(`blp_client.py` carries only host + port). **So storing the Terminal login automates nothing in the
pipeline**; it would only feed a scripted GUI sign-in, which the P0 gate argues against. The value
of rotating it is closing the plaintext exposure — not enabling anything.

## The gap this recovery does NOT close

**Nothing detects a dead Terminal.** This outage was found only because a human asked how
things were going ~12.5h in. The 07:00 ET pull has no precondition check on DAPI liveness, so
with the Terminal down it fails (or worse, produces nothing) on a schedule nobody is watching.
Fixing that is a **route/schedule design question, not a monitor** — per the standing alarm
moratorium, do NOT reach for an alarm here. Routed to MSTR~Z for CTO/Andrew disposition.
