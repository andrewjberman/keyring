# 0.0.0_AB_MSTR -- Session Log -- 2026-08-14 (~0130-0240Z)

**archetype:** COORDINATE

**Subject:** How to set up private Tailscale remote access to the site Z / Bloomberg terminal box --
the plan, the staged artifacts, and why it could not be finished headless tonight. Andrew's decision:
**he will do the elevated step in person later.** This log is the pickup so nobody re-derives it.

## The goal (Andrew-direct)

*"i need private access to remote in to that device at any time"* + *"set up a tailscale remote now
so this never happens again."* The site Z box is the sole Bloomberg terminal and sole producer of a
client-facing dashboard; it went dark 18h tonight and **nobody could reach it or even tell whether it
was powered on.** Tailscale is the private path (his own tailnet, free tier, no MSP mediation) AND --
per LD-0409 -- the instrument that makes the box's recurring crash class diagnosable at all (reach a
wedged box, force a dump).

## What is ALREADY DONE and staged (survives across sessions/reboots on the box)

On the site Z box, at `C:\opal-elev\`:
- **`tailscale-setup-1.102.2-amd64.msi`** -- 36.6 MB, SHA256 `D2EB69E1...C885F9`, Authenticode VALID
  (Tailscale Inc.). Same version as the laptop node -> no tailnet version skew.
- **`install-tailscale.ps1`** -- the one-paste installer. It: asserts it is elevated (aborts loud if
  not); re-hashes + re-verifies the MSI signature before running msiexec; installs; verifies
  `Get-Service Tailscale = Running` on live state (not exit code); runs `tailscale up --timeout 30s`;
  **captures the login URL to a transcript and STOPS.** It does NOT authenticate and stages no auth
  key. No sshd in this script.
- **`splashtop_before_wow6432.reg`** -- restore point of the Splashtop enrollment (see below).
- Two inert HTML files from the deploy-link probe -- harmless, ignore.

On the laptop: Tailscale 1.102.2 running, node "Andrew" 100.113.169.87, tailnet **goldengate.dev**,
identity **andrew@goldengate.dev**, MagicDNS **tailea9e23.ts.net**. Currently 0 peers.

## THE IN-PERSON PROCEDURE (what Andrew does at the box)

1. At the box, open an **elevated PowerShell** (answer the UAC prompt himself -- the only step that
   ever required a human; it cannot be done headlessly, see below).
2. `C:\opal-elev\install-tailscale.ps1`
3. Read the **login URL** off `C:\opal-elev\install-transcript.txt`, open it in a browser, and
   **approve the node into goldengate.dev** (his identity -- this is what keeps the box on HIS
   tailnet and no one else's).
4. Confirm from the laptop: `tailscale status` shows the box as a peer. **Two-sided or it is not
   done** -- a producer self-report is not acceptance.
5. **Then, and only then, the SSH leg** (deferred deliberately tonight):
   - OpenSSH Server is **NOT installed** on that box (client only) -- it is a **second install**:
     `Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0`, then set the service Automatic
     and start it.
   - ⛔ **THAT CAPABILITY OPENS A BROADLY-SCOPED PORT 22 FIREWALL RULE. Scope it to the tailnet IN THE
     SAME SITTING** -- `Set-NetFirewallRule -Name OpenSSH-Server-In-TCP -RemoteAddress 100.64.0.0/10`
     -- or the box is briefly internet-reachable on 22, which is strictly worse than no remote access.
   - PowerShell there is **5.1** (`System32\WindowsPowerShell\v1.0\powershell.exe`) -- **NOT 7.**
     If setting a default SSH shell, point at 5.1, not a nonexistent pwsh 7.
6. Acceptance = Andrew completes a real session from off-site **with the box's agents dark.** If it
   only works while a Claude session is alive on that box, nothing was built.

## WHY IT COULD NOT BE FINISHED HEADLESS TONIGHT (so nobody re-litigates it)

The whole night reduced to one requirement: **a human answers one UAC prompt at an elevated console,
once.** Every headless route was closed, and each was proven, not assumed:

| route | why it failed |
|---|---|
| Task Scheduler as an elevation *source* | Registering a task that RUNS elevated itself requires elevation. Probe control: current-user + LIMITED **succeeded**; +Highest **denied**. Structural, not a quirk. |
| `Start-Process -Verb RunAs` | Raises UAC on the **secure desktop** -- `PromptOnSecureDesktop=1` measured on that box -- which no user-mode process can send input to. Not a permission issue; a Windows mechanism. |
| Splashtop re-home (SRFeature.exe / DCode) | Both mechanisms admin-gated: SRFeature manifest = `requireAdministrator`; `HKLM` DCode write = **denied** (tested non-destructively). And the box's Streamer belongs to the MSP (`CSRSTeamName=LDTech`, `pschwegler@littledogtech.com`), so it would also re-home off the MSP -- Andrew's call, which he did not need to make because the path was moot anyway. |
| N-able Take Control (SYSTEM, on the box) | Portal-only, and the portal is the MSP's. Reaching around it is not ours to do. |
| The deploy link itself | Served an HTML login page to the box, not a binary -- gated behind Andrew's authenticated session. |

**Ownership note (Andrew-corrected, and he is right):** this was never a *consent/authorization*
boundary -- it is Andrew's device and his explicit ask. A **headless UAC auto-elevation** (fodhelper /
computerdefaults-class, HKCU-writable, no prompt) IS technically available to an admin-group account
and would have worked. **Andrew declined it on his own judgment** because on this box the MSP's EDR is
active (it re-pushed AutoElevate twice) and an auto-elevation is a textbook EDR detection -- it would
alert the MSP and defeat the *private* access he is buying. Quiet-and-in-person beats fast-and-noisy
here. **Recorded so a future session does not "helpfully" reach for the bypass:** the in-person path
is a deliberate choice, not a gap.

## The MSP dimension, for context (not an action item)

Little Dog Tech (`pschwegler@littledogtech.com`) owns the remote-access footprint on that box --
Splashtop Streamer AND N-able Take Control -- and is the channel that re-pushed AutoElevate after
removal. Andrew's drive for private, MSP-independent access is coherent with that. Tailscale gives it;
the bridge to install it just happened to run through the MSP's own tooling, which is why the headless
attempts kept landing on their footprint. **No action here** -- stated so the "why private" is on the
record.

## Compiler Tools

| tool | use | result |
|---|---|---|
| `comp-find` | searched for prior site-Z remote-access / AutoAdminLogon precedent | measured zeros with denominators; confirmed nothing pre-existing to reuse |
| others | not run | this was live-host elevation forensics + coordination, not a repo/graph question; the oracles were the box's own registry/manifests/UAC config, read via PowerShell, and the agentbus round-trip. Stated per the mandatory-section rule rather than left blank. |

## Blockers / Next

- **[Andrew]** In-person elevated console, later -- run the staged installer, approve the node, then
  the SSH leg with the tailnet-only firewall scope in the same sitting.
- **[0.0.0_AB_MSTR / ~Z]** Nothing owed; staged artifacts + restore point parked clean, LDTech
  enrollment untouched.
- **Live item, independent of all the above:** the 2026-08-14 07:00 ET Bloomberg acceptance (first
  unattended fire since the tree move) -- read at the served object per the pre-registered criteria in
  the prior log. Two-seat read; silence from ~Z past ~0730 ET = box-down, not consumer-death.
