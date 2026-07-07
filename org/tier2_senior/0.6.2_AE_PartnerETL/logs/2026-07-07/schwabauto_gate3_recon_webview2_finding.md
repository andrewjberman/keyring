# 0.6.2_AE_PartnerETL — SCHWABAUTO A-prime Gate-3 recon: SI2 SSO lives in a WebView2 profile, not Windows Cred Manager

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE
**Date:** 2026-07-07 | **Window:** ~15:09Z -> ~15:14Z | **Serial:** 0.6.2_AE_PartnerETL

## Summary
Resumed the CTO ROE-nod'd Gate-3 recon (SI2 box-grounding spike, read-only/location-format-only/
no-session-perturbation) after the Schwab-unfreeze detour. Located the SDD auth material: NOT Windows
Credential Manager (the §2.1 design assumption) — the SI2Desktop.Container app embeds a WebView2
(Chromium) control and runs the LMS-gateway SSO flow inside it. Found the standard Chromium profile
(`...\Schwab.SI.SI2Desktop.Container.exe.WebView2\EBWebView\Default\`) with two concrete capturer
targets: `Cookies` (SQLite, DPAPI-encrypted, the full auth-jar) and `Local Storage\leveldb\*.log`
(actively written, likely OAuth token persistence). Stopped at location/format — did not open the
Cookies DB, read leveldb contents, or attempt decryption, staying inside the §6b no-live-session-
material-before-CTO-sees-the-capturer bound. Documented in the design brief §9, RAVC'd to CTO.

## Work done
1. Read-only SSM recon on `i-0f3d57a97f14727af`: `cmdkey /list` (Cred Manager target enumeration,
   metadata only, no secrets) — one unrelated WindowsLive entry, nothing Schwab-scoped.
2. Broadened search: found SI2Desktop.Container's WebView2 embedded-browser data directory.
3. Enumerated `EBWebView\Default\` — standard Chromium profile layout (Cookies, Login Data, Local
   Storage, Session Storage, History, etc). Checked file existence/size/mtime only for `Cookies`,
   `Local Storage\leveldb\`, `Session Storage` — all show recent activity (5:49-5:52 PM 6/29, the
   app's last live-session window).
4. Updated `docs/briefs/schwab-sdd-rest-ingest-aprime-design-20260702.md` §9 with the full finding +
   Gate-2 capturer implications (needs SQLite+DPAPI decrypt for Cookies, a leveldb reader for Local
   Storage, running as the same Windows user SI2 runs as since DPAPI keys are per-user).
5. RAVC'd CTO with the result + offered to proceed to Gate-2 capturer build on signal.

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| N/A this unit | box-local Windows filesystem/Credential-Manager recon has no comp-tool surface | off-rail (no gap — legitimately outside graph coverage, same as the earlier SSM box recon this session) |

## Blockers
None. Holding for CTO signal before Gate-2 capturer build (their call whether to review the recon
result first or GO straight to build).

## Current State (handoff)
- Gate-1 (DenyPlane): CLOSED (07-06).
- Gate-3 (recon): DONE this session — SI2 SSO location identified (WebView2 Chromium profile, not
  Cred Manager), design brief §9 updated + committed (89de865b4).
- Gate-2 (capturer + liveness alarm): NOT started. Next up once CTO signals.
- No box-state changes made (all reads); no ledger needed.

## Next Steps
- **[1.0.0_SA_CTO]** review the Gate-3 result / signal GO on Gate-2 capturer build.
- **[0.6.2 self]** on CTO signal: build the capturer (SQLite Cookies read + DPAPI decrypt, leveldb
  Local Storage read, SM write to `schwab/sdd/session`), THEN the liveness alarm (sequence per §6:
  liveness alarm before any standing-session reliance).

## MCP traffic
1 message this unit: Gate-3 result RAVC to CTO.
