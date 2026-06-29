# 0.0.1_UA_mstools — Session: Schwab DERISK-1 live-spike consult chain (2026-06-29)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, VALIDATE

Tier-0 M365 Utility Agent. Event-driven session: launched, armed reachability, then served a
real-time SI2/Schwab-SDD feasibility consult chain to 0.6.2_AE_PartnerETL as Andrew stood up and
enrolled the Path-A Quartz/EC2 spike box LIVE. All my output was static-analysis grounding +
RAVC consult; no code/infra committed by me this window.

## What I did (the window)

1. **Launch + reachability.** Registered on broker (:7800) as `0.0.1_UA_mstools` (the launch label
   "MSGraph" = the M365 surface; canonical serial/dir is `0.0.1_UA_mstools`). Armed persistent inbox
   Monitor (task `b9rgeiviz`). Confirmed M365 gateway live (`whoami` -> Andrew@opalinvest.com).
   Re-registered once mid-session after the broker dropped me. Oriented from 06-26 close log.

2. **AE consult #1 — 4 feasibility Qs before box stand-up (DIAGNOSE/VALIDATE).** Answered with
   explicit grounding tags ([CAPTURE]/[STATIC]/[INFERRED]/[NOT-OBSERVED]). Key honesty anchor: my
   06-26 live capture was on Andrew's ALREADY-ENROLLED device, so I never observed the enrollment
   step itself -> flagged Q1/Q2 (durability + TOTP-seed capturability) as the spike's job, gave a
   concrete enrollment watch-list. Q3 (ClickOnce on Server): Server-with-Desktop-Experience +
   pre-install WebView2 + auto-logon console (not a service). Q4 (RDP cadence): app session long-lived
   via x-refresh-token; mitigate RDP-disconnect with console auto-logon.

3. **AE consult #2 — 2 install Qs (VALIDATE, source-grounded).** Read the locally-installed ClickOnce
   state on Andrew's box. CONFIRMED the exact deploymentProvider URL from the dfshim manifest:
   `https://si2.schwabinstitutional.com/sdd/Schwab.SI.SI2Desktop.Container.application` (agrees with
   the 06-26 capture flow #4 + exe.config `/sdd/` base — 3 sources). Confirmed install is
   INTERACTIVE-ONLY (per-user `%LOCALAPPDATA%\Apps\2.0` + HKCU subscription; no headless/SSM). Gave a
   clean one-RDP-session runbook (install -> SM-cred login -> device-MFA -> capture TOTP seed if QR
   shown -> schedule -> relaunch to prove OTP-free -> disconnect-don't-logoff).

4. **AE consult #3 — Error 1923 "SDD Schedule Service could not be installed" blocker (VALIDATE,
   Andrew mid-dialog).** Ground-truthed against Andrew's WORKING box: ZERO SDD/Schwab service (any
   name/binary path), ZERO Schwab scheduled task, and the uninstall entry is `dfshim ShArpMaintain`
   (ClickOnce, NOT MSI). => the service is SKIPPABLE; CLICK PAST 1923; app runs via in-proc Quartz.
   No elevated-MSI path needed. Sent + PushNotification (Andrew attended).

5. **AE consult #4/#5 — unattended TRIGGER (DIAGNOSE, the last open piece).** AE reported milestone
   HIT: enrollment done, durability proven (close/reopen = no re-login), June AllNewFiles pull LANDED
   in S3 (13 files/720MB in `s3://opal-data-schwab/01_raw_quartz_validation/`), auto-sync task live
   (SYSTEM, 30min, survives disconnect). Open: GUI scheduler dead (service-gated). Deep static
   analysis verdict: **NO headless CLI download path** — only `Container.exe` exists; NO SI2 assembly
   reads argv (`GetCommandLineArgs` absent everywhere); `AllNewFiles` is an internal REST/method name,
   not a CLI token. Scheduler is in-proc Quartz (can persist to SQLite AdoJobStore, but jobs fire only
   while the app runs). **CORRECTION to my own brief:** the "it already runs scheduled downloads" line
   was an INFERENCE from `ScheduledTaskMigrationStatus`; ground truth = reference box does MANUAL
   downloads, no automated schedule. Ranked unattended options: (1) leave app running + saved Quartz
   schedule (test if GUI saves to SQLite); (2) UI-automation on a Windows task (robust fallback);
   (3) Schwab enterprise MSI with the service (clean long-term / Path-C ask); (4) Path-B REST still
   blocked by encrypted payloads.

## Compiler Tools

| Tool | Why | Result |
|---|---|---|
| (none) | This window = consult/analysis grounded against the principal's LOCAL Windows ClickOnce install (`%LOCALAPPDATA%\Apps\2.0`) + LIVE AWS state reported by AE — neither is in the repo/AWS estate the comp-tools index. No repo/infra/data change was authored by me. | n/a |

What worked: native filesystem/registry inspection of the installed SI2 binaries (dfshim manifest,
service/task enumeration, argv-string analysis) was the correct exception — no comp-tool indexes a
local Windows ClickOnce app. What failed: nothing. Gap found: none (comp-rail correctly does not
cover principal-local desktop-app inspection; the HUD nudges were acknowledged + the exception holds).

## Blockers

None for me. The spike's one open item (unattended trigger) is AE_PartnerETL's, now scoped to a ranked
option set + a concrete on-box test (does the GUI save a Quartz schedule to SQLite).

## Current State

- **Identity:** `0.0.1_UA_mstools`, LIVE on broker :7800, persistent inbox Monitor task `b9rgeiviz`.
  M365 gateway reachable (Andrew@opalinvest.com).
- **Schwab DERISK-1 spike (AE_PartnerETL, box `i-0f3d57a97f14727af`, Win Server 2022):** enroll +
  durability + pull->S3 (13 files/720MB, `s3://opal-data-schwab/01_raw_quartz_validation/`) + 30min
  SYSTEM auto-sync = DONE/verified by AE. OPEN: unattended download trigger (no SI2 CLI exists).
- **Grounded facts banked:** memory `schwab_sdd_auth_otp_free_steady_state.md` updated this session
  with the source-confirmed ClickOnce deploymentProvider URL, interactive-only install, and the
  enrollment seed make-or-break. Brief stays keep-local/gitignored (CTO disposition 06-26).
- **Brief correction on record:** SCHWAB_SDD_DELIVERY_BRIEF.md §2 "it already runs scheduled
  downloads" is an unconfirmed inference; reference-box reality = manual downloads.

## Next Steps

- [0.6.2_AE_PartnerETL] Test unattended-trigger option 1 on the box: attempt a GUI schedule save,
  search `%LOCALAPPDATA%` for a new Quartz `.sqlite`/`.db`. If service-gated, fall to option 2
  (UI-automation on the existing Windows Scheduled Task) for the milestone; run option 3 (Schwab
  enterprise-MSI / supported-server-deployment) ask with the Schwab rep in parallel.
- [0.0.1_UA_mstools] On standby: can sketch the UI-automation (pywinauto/AutoIt) script, locate the
  Quartz job-store path, or run the mitmproxy capture to re-confirm the steady-state token/refresh
  flow during a scheduled pull if AE wants the durability evidence locked.
