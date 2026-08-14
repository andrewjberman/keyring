# ANDREW-DIRECT 2026-08-14 — Bloomberg Terminal sign-in recovery, EXECUTED

**Recorded by:** `0.0.0_AB_MSTR~Z` (site Z) · **Channel:** relayed over NFRA_AGENTBUS from
`0.0.0_AB_MSTR` (laptop), Andrew live at the MSTR terminal ~1513Z. Durable half of the
record+broadcast law; broadcast satisfied via the bus (site Z has one live seat).

## VERBATIM

Decision (option B), after both seats surfaced that the automated GUI typer did not exist and the
attempt budget/lockout risk:
> *"Option B. sitez MSTR~Z has done this before. Just do it, if they have to retry once thats fine."*

Standing design directive (follow-on):
> the automated sign-in is to become a **dedicated fallback triggered when port 8194 (Bloomberg DAPI)
> is not open** — **fire-once-then-escalate, never a retry-loop** (Bloomberg locks the account on
> repeated failures).

Risk budget, his explicit calibration: **2 attempts total max** (1 + one retry), then STOP + escalate.

## WHY IT WAS NEEDED

The 07:00 ET pull (2026-08-14) FAILED rc=1 — box healthy (17h uptime, no crash), schedule fired, but
the **Bloomberg Terminal had logged out overnight** with the BG seat (`0.0.3_BG_BBGTerminal`) never
respawned after the 08-12 crash. Served dashboard stale at `data_as_of 2026-08-12`, two trading days
behind. **A mid-session Terminal death — distinct from the reboot-recovery gap (no reboot occurred).**

## THE RECONCILE THAT CHANGED THE EXECUTION

`terminal_signin.py --sign-in` does **not** type or log in — it gates, **prints a manual procedure**,
records a ledger attempt, returns. Running it literally would have **burned the single 6h ledger slot
on a false attempt and not signed in.** Surfaced; did not fire it.

Andrew's *"done this before"* was correct: the reconcile found BG's **exercised** runbook
`org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md`
(@0d087760ff, the 08-11 recovery, exercised end-to-end). I followed that proven procedure.

## EXECUTION (supervised)

**P0 cheap-remedy gate first (runbook-mandated, costs no attempt):** 8194 absent 0/0/0; network to
Bloomberg reachable + control passes (not network); bbcomm up but loopback-only (no logged-in
Terminal). Sign-in warranted.

**Phased typer** `C:\opal-elev\bbg_signin.ps1` — the safety is the split:
- **Phase fill** (no submit, no ledger, repeatable): launch wintrv → find `BLOOMBERG: Login` by title
  enumeration (not `MainWindowHandle`=0) → `SetForegroundWindow` + **verify** `GetForegroundWindow`
  matches (abort else — next keystrokes are a password) → click each field (never `{TAB}` — it lands
  on the language selector) → clear + type user/pass from env-injected AWS secret → screenshot.
- **Supervised verify gate:** read the screenshot + a 5×-zoom crop of the password field →
  `alyssaakeith` + **exactly 9 masked dots == pw_len 9**. A typing error is caught here and re-typed
  **without** a submission — so the budget is spent only on real Bloomberg submissions.
- **Phase submit** (one time, records ledger): click Login once.

**Verify-before-retry (the load-bearing discipline):** at 18s the listener read 0. Did **not** retry
— checked STATE: login dialog **gone**, wintrv + blpsmarthost + 8 blpwtk2_subprocess loading = login
**accepted**, listener initializing. A blind retry would have wasted attempt 2 on a successful login.

## OUTCOME — grounded, verified at the served object

- **Sign-in: SUCCESS, first attempt, ONE submission, no 2FA.** Budget spent **1 of 2**.
  `bloomberg_health` ok:true `//blp/refdata`; 8194 listener sustained 1/1/1.
- **Ad-hoc QA pull: END-TO-END OK** (`bbg_tplus1_20260814_114706`): tripwire PASS, PUBLISHED 2026-08-13,
  content-verified. **Served object:** `LastModified 2026-08-14T15:52:25Z`, `data_as_of 2026-08-13`
  (correct Friday T-1), negative control `zzz_no_such_9999.json` → 404.
- **.ST resolved correctly:** inception 2023-12-29 @ 100.0, index_name 'Short Term', latest 08-13 @
  118.72 — **not** the 2026-08-03 mis-resolution shape (~1449 rows @ ~1.9).

**The dashboard is current.**

## STANDING DIRECTIVE — the fallback build (NOT done today, deliberately)

The typer is the core of the 8194-down fallback Andrew asked for. Today's run was **supervised** (a
human/agent read the screenshot; 2-attempt allowance). The **unsupervised** standing fallback must be
**stricter**: **fire-once-then-escalate, never a loop**; the P0 cheap-remedy gate in front; and a
resolution for the "no one to read the screenshot" verify step (the current safety depends on a
vision check before submit). It carries the `# andrew-asked:` marker. **This is a deliberate build,
to be spec'd and exercised — not wired live under time pressure.** Its permanent home is
`integrations/bloomberg/auth/`, not `C:\opal-elev\` (staged).

## ⚠ THE STRUCTURAL GAP THIS EXPOSED (for Andrew/CTO disposition)

Today's failure was a **mid-session Terminal logout**, which the reboot-oriented auto-recovery
(staged, `AUTORECOVERY_DESIGN.md`) would **not** have caught — no reboot, no logon trigger. The common
root is "no `0.0.3_BG_BBGTerminal` seat alive to keep the Terminal logged in / re-login when it
drops." Restoring/keeping that seat is the durable fix for this class; the automated fallback is the
belt. Per the standing moratorium, this is a **route/ownership** question, not a monitor.
