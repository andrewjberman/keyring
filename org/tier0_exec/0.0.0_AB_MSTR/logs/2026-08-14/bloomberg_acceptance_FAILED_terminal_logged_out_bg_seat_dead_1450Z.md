# 0.0.0_AB_MSTR -- Session Log -- 2026-08-14 (~1450Z)

**archetype:** ESCALATE

**Subject:** The ~11:00Z Bloomberg acceptance read (Andrew's own item, kept alive through the
MDPF_TRGALN governance) FAILED. The client-facing benchmarks dashboard is stale. Root cause is a
NEW, second failure mode (not the crash, not the reboot gap). Escalated to Andrew; remedy is his
decision and was deliberately NOT fired.

## The finding (grounded on both fabrics, independently)

- **MSTR~Z did the authoritative read from the producer box** (agentbus MessageId 5c561daf, 1450Z):
  served `model_portfolio_benchmarks.json` `data_as_of 2026-08-12`, unchanged since yesterday's
  17:45 catch-up; **today's 07:00 pull wrote nothing** (`OPAL_BBGTML_daily_pull` LastRun
  2026-08-14 07:00:01 **rc=1** "failed to start session"). `bloomberg_health = ok:FALSE`, **no
  listener on 127.0.0.1:8194** (DAPI transport down), `wintrv.exe` (Terminal) installed but **not
  running**.
- **I independently corroborated the served-state leg from the laptop** (not a relay): read
  `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` directly ->
  `data_as_of: 2026-08-12`, `generated_at: 2026-08-13T21:51:45Z`. Today's correct T-1 is
  **2026-08-13** (the same T-1 the MDPF pipeline correctly hit). So the dashboard **missed today's
  update** and is one trading day staler than it should be.
- **comp-freshness MASKED this**: its `yang_model_portfolio_benchmarks` entry reported PASS on a
  **flat 72h wall-clock threshold** (16.7h old), NOT the trading-day-frontier content check -- the
  exact NEVER#1 caveat. mtime-fresh, content-stale. Only the content `data_as_of` read catches it.

## Root cause (MSTR~Z, process-truth grounded) -- a DISTINCT failure mode

- The box is **HEALTHY**: 17h continuous uptime, zero new 6008/KP-41, **no reboot today**.
- The **Bloomberg Terminal logged out / died overnight** (Bloomberg sessions expire), with nobody
  managing it. Yesterday's 17:45 catch-up succeeded (Terminal up then); by 07:00 it was gone.
- **ROOT: `0.0.3_BG_BBGTerminal` -- the seat that OWNS the Terminal -- is NOT REGISTERED.** It died
  in the 08-12 crash and was **never respawned** (a human relaunched MSTR~Z at 17:57 but not BG).
  No BG = nothing alive to keep the Terminal logged in or re-login when it dropped.
- **AUTO-RECOVERY GAP (important):** today's failure would NOT have been caught by the staged
  self-heal design. No reboot -> no logon trigger -> auto-launch never fires. This is a
  **mid-session Terminal death**, distinct from the boot-recovery gap. Common root ("no BG agent
  alive") but a different trigger -- Andrew must know this before assuming auto-recovery covers it.

## The remedy -- and why it was NOT fired (correct)

- The fix is a **Bloomberg Terminal sign-in**. The AWS secret resolves clean (MSTR~Z safe-checked:
  `secret=bloomberg/terminal/login`, user present, pw_len ok -- **fingerprint only, no value
  printed, no login attempted**). So creds are valid.
- **Neither MSTR~Z nor I fired `terminal_signin.py`, and we recommend AGAINST auto-firing it** --
  for the tool's OWN design reasons, not caution: **(1)** its GUI leg is **UNEXERCISED** (sign-in
  ledger empty, zero attempts ever) -- this would be its first live run on a client-facing
  production dashboard; **(2) Bloomberg LOCKS THE ACCOUNT on repeated sign-in failures** -- a
  botched unattended attempt risks a locked terminal (a support call).

## Andrew's decisions (escalated via PushNotification 1452Z; no ANDREW broker serial)

1. **Fire the Terminal sign-in?** (the immediate fix; risky per above -- his call).
2. **Respawn `0.0.3_BG_BBGTerminal`** so the Terminal stays managed/re-logged-in going forward
   (a **site-Z MSTR spawn** -- MSTR~Z's act, not mine; entangled with #1 since BG's first job is the
   same sign-in).
3. **The auto-recovery design** needs a mid-session-Terminal-death arm, not only boot-recovery.

## Posture

- **HOLD on both fabrics**: do not fire the sign-in, do not respawn BG, until Andrew rules. Site-Z
  is holding; I concurred.
- **MDPF_TRGALN is CLOSED + /verify SOUND and fully unaffected** -- separate pipeline; its served
  artifacts correctly serve T-1 (08-13). This Bloomberg failure is orthogonal.
- I remain live + event-driven for Andrew's ruling and MSTR~Z's ACK.
