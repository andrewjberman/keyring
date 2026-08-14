# ANDREW-DIRECT 2026-08-13 — Tailscale remote-in · agentbus blind spot · site-Z reset fortification

**Recorded by:** `0.0.0_AB_MSTR~Z` (site Z) · **Channel:** relayed over NFRA_AGENTBUS from
`0.0.0_AB_MSTR` (laptop), messages `ae41259f` (~2225Z) and `6145751e` (~2228Z), both delivered
2026-08-13T22:28–22:30Z · **Andrew's channel:** MSTR terminal (laptop).

Per `org/XXX.md`, a sovereign instruction is RECORDED VERBATIM and BROADCAST the same turn. The
receiving seat does not adjudicate scope. This file is the durable half.

---

## VERBATIM

**~2225Z:**
> *"Communication is absolutely crucial to maintain, if there is actually a confirmed blind spot
> between laptop and sitez fabrics via agentbus, that has to be rectified. furthermore the basis for
> the sitez device reset needs to be understood and fortified against completely. Additionally, I
> recommend we set up a tailscale remote now so this never happens again"*

**~2228Z, two messages:**
> *"need to have mstr~z set up tailscale on their device"*

> *"i need private access to remote in to that device at any time"*

**Scope note (not adjudicated, recorded as stated):** the second pair RAISES the bar from *agent
reachability* to **private interactive remote-in, at any time, including when every agent on the box
is dark** — which is precisely the state that cost the 2026-08-13 Bloomberg pull.

---

## STATE AT TIME OF RECORD — measured, not assumed

**Tailscale is NOT installed on site Z, and never has been.** Reported and STOPPED there; installing
software on this box is Andrew's call.

| check | result |
|---|---|
| `tailscale.exe` on PATH | NO |
| `C:\Program Files\Tailscale\` · `(x86)\Tailscale\` | ABSENT |
| `Get-Service Tailscale` | NOT INSTALLED |
| any `tailscale*` service or process | NONE |
| Uninstall registry, **both** hives | **NO ENTRY** — virgin box, not a reverted one |

Consequence: there is no `tailscale up` to run and **no login URL to send.** Target tailnet (from
the laptop, for when it is authorized): `goldengate.dev` · identity `andrew@goldengate.dev` ·
MagicDNS `tailea9e23.ts.net` · laptop peer `Andrew` `100.113.169.87` (tailscale 1.102.2), currently
**zero peers**.

**Division of authority on the join, recorded because it should never be automated:** `tailscale up`
prints a login URL; the agent sends the URL and **never authenticates**, never enters credentials,
never uses a found auth key. Andrew opens it in his own browser under his own identity. An agent
enrolling a machine onto the owner's private mesh on their behalf is exactly the act that must stay
manual.

---

## ⛔ FINDING — OUR OWN TOOLING WOULD SEVER THIS THE DAY IT IS BUILT

**`/kill` reaps Tailscale by name.**

```
.tools/kill-maint.ps1:108
  $appName = '^(msedge|chrome|chromium|ms-teams|Teams|tailscale|tailscaled|tailscale-ipn|' +
             'mscopilot|mscopilot_proxy|copilot|Spotify|Slack|Discord|Zoom|WhatsApp|Skype|' +
             'GoogleUpdate|SpotifyWebHelper)(\.exe)?$'
```

`/kill apps go` and `/kill all go` both match it. Once Tailscale is this box's remote lifeline, a
routine cleanup by any agent **severs Andrew's access — while the box still reads perfectly healthy
from the inside.** That is the same shape as every other failure in this incident.

**The skill doc already anticipated it, with a precondition that this instruction INVERTS:**

> `.claude/skills/kill/SKILL.md:148-150`, verbatim: *"Stopping the process may be restarted by the
> SCM and/or briefly drop tailnet connectivity — **fine if you don't route AWS/remote access through
> it**, but know that's what happens."*

Andrew is asking to route remote access through it. The doc is not wrong; **we are changing its
premise.** This is the general class named in CLAUDE.md — a claim about the world, written into an
artifact, with no mechanism keeping it true when the world moves.

**Recommendation (NOT executed):** remove `tailscale|tailscaled|tailscale-ipn` from the apps regex
and replace the `:148` caveat with a hard DO-NOT-KILL note — landing **in the same act as the
install**, so the protection and the thing it protects never exist apart. Not edited yet: there is
nothing to protect until the install is authorized.

---

## ⛔ FINDING — THE REMOTE-IN FIX CAN REPRODUCE THE OUTAGE IT IS MEANT TO PREVENT

Two mechanisms, not equivalent for a **Bloomberg Terminal** box:

- **(A) RDP over the tailnet** — full desktop. The only option that lets Andrew drive the Terminal
  and sign it back in; almost certainly what *"remote in"* means.
- **(B) `tailscale up --ssh`** — shell only, tailnet-identity authenticated, no port exposure.
  Safer, sufficient for logs/diagnostics, **cannot** drive the Terminal.

**Recommended: (A), bound to the Tailscale interface only** — firewall scoped to the tailnet /
`100.64.0.0/10`, never LAN-wide, never an internet-facing 3389. *"Private"* is his word, and an
exposed 3389 on this box is a materially worse posture than today's. (B) can ride along; they are
not exclusive.

**THE COUPLING, and it is not theoretical.** An incoming RDP session takes over the Windows console
and **leaves it LOCKED on disconnect.** The 07:00 Bloomberg pull runs in interactive user context —
its own wrapper says so:

> `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`, verbatim: *"USER CONTEXT IS
> DELIBERATE … A SYSTEM-context task would run with no Terminal session and fail every time. **If
> nobody is logged in at 08:03, this correctly does nothing.**"*

So: RDP in → disconnect → console locked → the next 07:00 fires into a locked session and **does
nothing, silently, on a healthy box, with a green task and no error anywhere.**
**That is the 2026-08-13 symptom with a completely different cause and none of its evidence trail** —
no crash, no dark window, no 6008 to find. The fix for the outage can manufacture the outage.

**Mitigation to decide WITH him, not implemented:** after an RDP session either reconnect the session
to the console (`tscon`) or leave the box signed in; or prefer (B) for routine diagnostics and
reserve (A) for when the desktop is actually needed. **No checker is being built for this** (standing
alert/monitor moratorium) — it is a usage note that belongs beside the RDP decision.

---

## Agentbus blind spot — status at time of record

Confirmed by the laptop seat on its own evidence, twice, and not re-litigated here: deaf
17:12:31Z→20:20Z (~3h08m) and 21:51:58Z→22:21Z (~29m); in both, `TaskOutput(<consumer>)` reported
`running` throughout while messages accumulated as `NotVisible`, and re-arming restored delivery
instantly.

**Site Z's own consumer, measured 2026-08-13T22:32Z:** inbound `laptop→sitez` **0 visible / 0
NotVisible** — no pile-up, no deaf window since arming at 21:47Z (task `bnokm4i3g`). Outbound shows
7 `NotVisible`, which is the laptop side's in-flight, not ours, and `NotVisible` is a gauge, not a
receipt (Rule 22b).

⚠ **One short session on one device is a sample, NOT a clean bill for the mechanism.** Both observed
deaf windows were on the laptop consumer; that is where the evidence is, and site Z's silence so far
is not counter-evidence.

---

---

# UPDATE 2026-08-14 ~0105Z — ⛔ GO RECEIVED. DECISIONS 1 AND 2 ANSWERED.

**Andrew-direct, MSTR terminal, relayed `f024bd2c`, VERBATIM:**
> *"tailscale yes we want it, full desktop would be nice but commandline is fine too if we can just
> use powershell on the other device"*

**Decision 1 — install: YES.** **Decision 2 — command-line is acceptable**, full desktop merely
*"would be nice."* **Decision 3 — already closed elsewhere:** LD-0410 removed
`tailscale`/`tailscaled`/`tailscale-ipn` from `/kill`'s reap list, so the lifeline is protected
*before* the install rather than after.

**His acceptance of command-line resolves the RDP hazard in our favour** — command-line access does
not take over the console session, so the SSH leg carries none of the locked-console risk and does
**not** need to wait until after 07:00. RDP stays prepared-not-enabled.

## STATUS: BLOCKED ON ELEVATION ONLY — handed off, not stalled

```
WindowsIdentity : Opal_Bloomberg\Opal Bloomberg
ELEVATED        : False          (the account IS in Administrators; this session is not)
```
Tailscale is a machine-scope MSI with a service; no user-scope path exists.

⛔ **The install was NOT attempted unelevated, deliberately.** It would raise a **UAC dialog on the
console** — a GUI prompt this session cannot answer, sitting modal on a box with nobody at it. **That
console session is load-bearing:** the 07:00 pull runs in interactive context and tomorrow is its
first unattended fire since the tree move. Precedent is the same folder's 2026-08-10 handoff, where
`msiexec` was blocked in-session and Andrew ran it manually.

**Handoff (elevated-ready, every command, auth boundary intact):**
`Desktop\OPAL_BLOOMBERG_freeze_investigation_2026-07-30\HANDOFF_elevated-install-tailscale_2026-08-14.md`
*(outside the repo — no commit hash, stated so it is not read as committed).*

## ⚠ TWO SITE-Z MEASUREMENTS THAT CONTRADICT REASONABLE LAPTOP-SIDE ASSUMPTIONS

| | site Z (measured) | laptop (peer-measured) |
|---|---|---|
| `Get-Service sshd` / `sshd.exe` | **NOT PRESENT** / **False** — only the **client** `ssh.exe` exists | RUNNING / present |
| PowerShell 7 (`pwsh.exe`) | **ABSENT** (7 and 6); only 5.1 at `System32\WindowsPowerShell\v1.0\powershell.exe` | — |

⇒ **OpenSSH Server is a SECOND INSTALL on this box, not a config change** — a separate
authorization, not a flip of an existing service. ⇒ The proposed `DefaultShell` value would have
pointed at a **nonexistent binary**; the handoff uses the 5.1 path.

*This is the third laptop→site-Z generalization to produce a wrong premise in one evening (after the
08-10 KP-41 correlation and the "your consumer still has the defect" claim). The axis, not the
individual errors, is the thing worth carrying.*

## ⛔ A HAZARD IN THE SSH STEP THAT NEITHER SEAT NAMED

`Add-WindowsCapability -Online -Name OpenSSH.Server` **creates a firewall rule that opens port 22
broadly.** The tailnet-only binding is therefore **not** a later hardening step — it must land in the
same sitting, or there is a window in which this box has an internet-reachable `sshd`. That is
strictly worse than today's posture, which is no remote access at all.
```powershell
Set-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -RemoteAddress 100.64.0.0/10
```

## STILL OPEN AT ANDREW (the original three, less the two now answered)

1. **Install Tailscale on site Z** — yes/no. Everything else is blocked on this.
2. **RDP-over-tailnet vs SSH-only vs both** — with the console-lock/07:00 coupling above understood.
3. **May the `/kill` exclusion land in the same act as the install** — so the lifeline is never one
   routine cleanup away from being cut.

## RELATED, SAME DAY (context, not part of this instruction)

- Bloomberg pull outage diagnosed + rectified; served `data_as_of 2026-08-12` verified at the object.
- Freeze #11 (2026-08-12 22:58:14 ET) — the *"basis for the sitez device reset"* Andrew wants
  understood. Full analysis:
  `Desktop\OPAL_BLOOMBERG_freeze_investigation_2026-07-30\ADDENDUM_2026-08-13_freeze11_post-autoelevate-removal.md`
  (that folder is **outside the repo**, so it carries no commit hash — stated so it is not read as
  committed). Current standing: cause **honestly unknown**; no dump exists; WU excluded as a
  restart/proximate event on three grounds; the `cbprocess20`/AutoElevate cause of freezes #7–#10 is
  verified gone, so **the freeze class survived the removal of its only dump-grounded cause.**
