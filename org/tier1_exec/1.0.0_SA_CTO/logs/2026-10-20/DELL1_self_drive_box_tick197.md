# DELL1 self-drive box -- tick 197, 2026-10-20 ~17:18Z (delta: Track B rulings, Andrew's sign-in scripts, S16 ruled)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 17:18Z. Acked since tick 196: 8719, 8723, 8726, 8733.
- open_calls.json: 161 rows, 3 OPEN, all acts only Andrew can do.

## Acts and rulings
- **NFRA_FIDUPL Track B, Part 1** (P1 8723; feasibility record `deliverables/0.7.0_AE_CloudOps~NFRA1/FU-s-11_feasibility.md`):
  - The plugin installs. A Claude session needs Andrew's claude.ai `/login`.
  - Ruled: (1) a long-lived login on the SSM-only box is allowed, as Andrew's own act, and blocks nothing (act row 5013). (2) The
    agent's Chrome gets its own profile, and the puller runs with extensions disabled.
  - CloudOps installed `fidelity-vnc.service` (Xvnc :1, 127.0.0.1:5901 only) @f14a9c0d11.
- **Andrew asked for the "RDP" scripts.** The box is Linux and SSM-only, so the access is VNC through an SSM port forward.
  - Wrote `tmp/fidupl/01-05` (gitignored): prerequisites, start the screen with Chrome on the puller profile, tunnel plus viewer, an
    optional shell for `/login`, and stop.
  - All parse, the box reads SSM Online, and 02 and 05 were re-pointed at the service.
  - P1 was told to HOLD every box run until Andrew closes the screen (msg 8728).
- **P1 8733:** its one Track A attempt ran about 16:58Z, before the hold, and died at browser launch with no X server. There was no
  Fidelity traffic and no lockout exposure. REPAIR 9 waits for the X socket and disables extensions; it is in build.
- **HARVST instrument rows:**
  - The CVO refused the S10 disarm (8719). I relayed it to MSTR, and MSTR fixed S10 @bff9f2d966 and S11 @97cb3abc4c (8726). Relayed
    to the CVO.
  - **S16 ruled: no restore of the set-aside account-id hash list.** The dell1 scan is unprovisioned BY DESIGN (c7381f6135). Msgs 8730
    and 8731.

## Scope state
- **NFRA_FIDUPL:**
  - Orders pending: FU-s-2 (REPAIR 9), FU-s-10, FU-s-11 and FU-x-1.
  - 0 objects under `fidelity/`. The 3 fetch rules are DISABLED.
- **AMGT_HARVST:** round 100 is at W1.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **The Fidelity hand sign-in on the box** through `tmp/fidupl` 01, 02, 03, then 05 (his login).
- **5013:** `claude /login` on the box (his claude.ai plan). Optional; Track B.
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `ssm describe-instance-information`.
- PowerShell parser check.
- `open-calls.py add`.
