# 0.0.0_AB_MSTR~Z — session 2145-2345Z, 2026-08-13 (site Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, SCRIBE

Session opened on a cold box 8 minutes after it returned from an 18h39m outage. Startup ceremony ran
clean; everything after it was a live incident.

## Summary

Site Z was dark 2026-08-12 22:58:14 ET -> 2026-08-13 17:37:11 ET. The Bloomberg dashboard missed its
07:00 pull inside that window. Diagnosed the miss (box down, not pipeline), confirmed the product had
self-recovered and verified it at the served object, then spent the balance of the session on the
BASIS of the outage under Andrew-direct instruction. Cause of the underlying stop is **honestly
unresolved**, and establishing *why no post-hoc instrument can resolve it* is the session's real
result -- it is what turns the two pending fixes from hardening into instrumentation.

## Startup (org/XXX.md Step 1b)

- `/watcher` — re-registered (was OFFLINE 18.8h, PID 18684 -> 9648); Monitor `byh3tw5t2` armed +
  confirmed running. **Zero `inbox-watch.sh` processes existed before arming** — no orphan, no
  dual-session ambiguity. Drive prefix resolved to `/cygdrive/c` (not hardcoded).
- `/agentbus` — device measured `sitez`; consumer `bnokm4i3g` armed. **Inbound was 8 DEEP WITH NO
  CONSUMER** — mail had been accumulating since the crash killed the prior session.
- `/integrate` (bare = ASSESS-ONLY; merged nothing, pushed nothing) — clone complete; base
  `e1bc19bc57`; CLOUD +33 / SITEZ +0; **overlap 0 of 32 files (0%)**; `merge-tree` rc=0; deploy
  exposure ceiling 0.
- A.1 serial file written; A.2 audit-archive-invoker run; **A.3 = 91 of 97 comp-tools resolve bare
  AND the forwarder EXERCISED (ran, not merely resolved)** — notable because this was a cold boot,
  the exact scenario that killed all 186 `~/bin` forwarders on 2026-07-29 (LD-0340). Did not recur.
- B.1 `to-check --all` — 2 TOs: `NFRA_CMTQUE.TO-6R` (37d, staged, I hold the window role);
  `NFRA_VELOCITY_ESTATE.WS-E6` (RESERVED per Andrew 2026-08-03).

## Work

### 1. Bloomberg pull miss — DIAGNOSED AND CLOSED

**Cause: the box was down.** 6008 (*"previous system shutdown at 10:58:14 PM on 8/12 was
unexpected"*) + Kernel-Power 41; boot 17:37:11. 07:00 ET sat inside the dark window.

Corroborated by two instruments with no shared source: the kernel log (22:58:14) and the broker
liveness clock (*last seen 67678s* = 23:02 ET), ~4 minutes apart.

**CRO~Z's 08-12 tree move exonerated at the mechanism, not by alibi** — the task is registered at the
post-move path, that path resolves on disk, the 07:00 trigger survived the `-At` regression, and it
executed *from the moved path*. Boot catch-up (`StartWhenAvailable=True`) ran the full end-to-end.

**Verified at the served object, with a negative control:**
```
head-object json/benchmarks/model_portfolio_benchmarks.json
  LastModified 2026-08-13T21:51:47+00:00   data_as_of 2026-08-12
negative control zzz_no_such_key_9999.json -> 404   (instrument discriminates)
```
Thursday on a T+1 contract wants `data_as_of 2026-08-12`. Exactly there. **Rectified.**

Two secondary findings: the scheduled path carries **no `.ST` custom-index check in 0 of 14 logs**
(so today's vintage is UNVERIFIED on that axis and needs a human at the Terminal), and the 08-11
scheduler-log gap is **UNMEASURED** because `TaskScheduler/Operational` is disabled.

### 2. Freeze #11 — investigated to the limit of what logs can answer

Andrew-direct: *"check the crash logs to figure out what was happening at the time of the crash."*
Prior art found at `Desktop\OPAL_BLOOMBERG_freeze_investigation_2026-07-30\` (outside the repo).

**What happened at 10pm: nothing.** Window 21:45-23:05 ET, System + Application, all levels —
**denominator 32 events, zero errors**. Last event of any kind 22:55:47; tripwire `[OK] idle` at
22:57:55; gone by 22:58:14. **No Event 1074 across the entire 08-12 AND 08-13 (denominator: 3, all
03:52-04:01)** — the machine was never told to restart; it stopped.

**Windows Update excluded as a restart/proximate event on three grounds**, one a positive control
from the same box: no 1074; zero WU Operational events 18:00-23:59; and 22:58 sits **inside** active
hours (`ActiveHoursStart 8` / `End 2`) while the box's own servicing restarts fired at 04:00/04:01,
squarely in the 02:00-08:00 outside-hours band.

**The structural finding: #11 is the first freeze with AutoElevate/`cbprocess20` verifiably GONE**
(no service, `sc query` -> 1060, no re-push since the 08-10 17:09:57 removal) **and it happened
anyway.** The class survived the removal of its only dump-grounded cause.

**Event 41 properties (nobody had pulled them) reframed the series** — denominator 12 retained:
`226`/`0xE2` MANUALLY_INITIATED_CRASH x4 (= *us*, forcing dumps) · PowerButton non-zero x3 ·
**BOTH-ZERO x5, including #11**. The recurring, never-attributed class is the both-zero class;
#7-#10 were attributed *only because a human was present to force a dump*.

**Thermal/hardware hypothesis tested and split:** WHEA-Logger **zero** events in the System log over
24.7d (valid negative — log enabled and retaining); throttle Event 37 **zero**. The 660
Kernel-Processor-Power events are all Id 55 = **boot-time capability enumeration, 20 per boot** —
opened one rather than guessing, and count/20 independently reproduces the 6005 boot census.
=> **CPU-thermal weakened substantially; hardware protective cut (PSU/VRM/upstream) NOT excluded**,
since that cuts with no prior throttle and no machine check.

### 3. Andrew-direct x3 — recorded and committed

Tailscale remote-in · agentbus blind spot · site-Z reset fortification. Verbatim, channel + time, at
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260813_TAILSCALE_REMOTE_IN_AGENTBUS_BLINDSPOT_SITEZ_FORTIFY.md`
@`5c8f3a8f3d`. **Tailscale is NOT installed on site Z and never has been** (no uninstall entry in
either hive) — reported and STOPPED; installing is Andrew's call.

Two findings surfaced with it:
- **`/kill` reaps Tailscale by name** (`.tools/kill-maint.ps1:108`). Once it is the remote lifeline,
  a routine cleanup severs Andrew's access while the box reads healthy. `SKILL.md:148` already
  carries the caveat *"fine if you don't route AWS/remote access through it"* — **this instruction
  inverts that premise.** Remedy recommended, NOT executed; it should land in the same act as the
  install.
- **RDP can reproduce the outage it prevents.** RDP takes the console and leaves it locked; the pull
  runs interactive (*"if nobody is logged in at 08:03, this correctly does nothing"*). Sequencing
  note issued: first safe window to exercise remote-in is AFTER tomorrow's 07:00.

## Corrections I made to my own claims (chronological)

1. **"recurring power fault"** -> retracted. `KP-41 + 6008` means *unclean stop* only; it does not
   discriminate power-loss from a freeze. (Peer correction, accepted.)
2. **"WU stack = leading root-cause candidate"** -> downgraded and split before repetition hardened
   it: dead as a restart event, open only as a latent destabilizer, by elimination alone.
3. **"origin/SITEZ is an ancestor of CLOUD, SITEZ->CLOUD landed"** -> invalidated by my own push;
   both legs now OUTSTANDING.
4. **"#11's logon 37s after boot ⇒ a human power-cycled it"** -> retracted. Ran boot->logon latency
   for **all** boots and found the control in my own data: the 04:00-04:02 TrustedInstaller reboots
   produced 7001 logons at 4 AM with nobody there. **Event 7001 is not a human-presence oracle.**
5. **The 12x downtime-outlier argument** -> withdrawn once both night rows proved attended. *A hung
   box and a powered-off box are indistinguishable if nobody comes.* This suffered the identical
   observation bias I had flagged for the business-hours cluster one message earlier and did not
   notice applied to my own reasoning.
6. **POST-LOG RETRACTION, 2026-08-14 ~0128Z — "site Z has no remote access, so somebody was
   PHYSICALLY at the box to launch me."** **FALSE, and I never measured it.** This box runs
   `SplashtopRemoteService` (SRService pid 5344, SRManager pid 6488) **and** N-able `Take Control
   Agent`, both RUNNING. I asserted the absence from the fact that we were *asking* for remote access
   — reasoning from the ask instead of from the box, without ever running `Get-Service`. The 17:57
   launch could have been remote. **What survives:** remote software cannot boot a dead box, so
   something physical still happened at 17:37:11; only the launch is ambiguous. **What it adds:** if
   WoL is enabled, an OFF box could have been woken remotely — and **a hung box cannot** — so a
   remote wake would be positive evidence for the power-loss limb. New item for the console/BIOS trip.
   **Verdict unchanged** (already UNRESOLVED); 07-28 attendance unaffected (rests on five serials +
   an Andrew Berman merge). Amended in the freeze addendum too.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 exercise probe | PASS | forwarder produced its own banner — proves it RAN, not merely resolved |
| (A.3 denominator loop) | `command -v` over `.tools/comp-*` | PASS | 91 of 97 bare; denominator printed, never a boolean |
| `safe-commit.sh` | x2, `-F` msgfile | PASS | risk-reflex CLEAN, measured (1 file vs 1209 danger nodes) |
| `safe-deploy` (pre-push) | on `git push origin SITEZ` | PASS | *"no deploy-scope script files detected"* — confirms the 0 exposure ceiling |
| `agentbus-sqs.sh` | `device` / `peek` / `send` x9 | PASS | device MEASURED not assumed; all sends via quoted-heredoc file (F-010 shell-injection rule) |

**What worked:** the denominator-and-positive-control discipline caught four wrong conclusions,
three of them mine. **What failed:** nothing tool-side. **Gap found:** none new — but note
`comp-*` tools have no reach into Windows event logs, kernel state, or firmware, which is the
entire evidence base of this session; that work is necessarily raw `Get-WinEvent`/CIM.

## MCP / bus traffic

~14 agentbus messages handled (all ACKed with MessageId per Rule 22b); 9 sent. Significant:
Andrew-direct x3 relayed (`ae41259f`, `6145751e`) and recorded; peer control-arm from the laptop
(`1772d6a3`) which closed the WU auto-restart branch; peer's Event-41 suggestion (`eb8c1e26`) which
was the best instrument call of the thread and was not mine.

## Blockers

**None at this seat.** All open items are AT ANDREW and each is evidence-cited above:
1. **OFF vs FROZEN-with-lit-LED on 08-13** — one human answer settles hang-vs-power-loss outright.
   Available since 17:37; both seats did log archaeology instead.
2. Tailscale: install yes/no · RDP vs SSH vs both · may the `/kill` exclusion ride along.
3. **No UPS on the sole Bloomberg Terminal / sole producer box** — `Win32_Battery: NONE`,
   ChassisType 3, sleep/hibernate disabled. Does not need the console trip to be DECIDED, only DONE.
   **Spec matters: a MONITORED unit** — output-load reading is what separates powered-off from hung
   remotely. A dumb UPS prevents the power limb and diagnoses nothing.
4. RDP sequencing window closes at 07:00.

## Current State

- **Site Z box:** up since 2026-08-13 17:37:11 ET, uptime ~2h, 48.6 GB free of 63.5 GB, tripwire
  polling clean. Dell Pro Micro Plus QBM1250, ChassisType 3 desktop, **no UPS, no battery**.
- **Bloomberg:** `OPAL_BBGTML_daily_pull` State **Ready**, LastTaskResult **0 = SUCCESS**,
  NextRunTime **2026-08-14 07:00:00**, MissedRuns 0, console session **Active**, no pending reboot.
  Pre-flight is DESIRED-state green; **acceptance is the EXERCISED read** — served object advancing
  to `data_as_of 2026-08-13`. Laptop MSTR will read it independently so the close rests on two seats.
- **Git:** `origin/SITEZ` @ `5c8f3a8f3d`, verified from the remote (`git ls-remote`), citation now
  resolves for the peer. Parity is **OUTSTANDING BOTH WAYS** (my push re-opened SITEZ->CLOUD;
  CLOUD->SITEZ is 34 commits). No merge proposed — bare `/integrate` is assess-only and Andrew has
  not asked.
- **Fabric on this box:** I am the ONLY live agent (`get_live_agents` = 1). Every site-Z seat died in
  the freeze and nothing respawned them; `0.0.3_BG_BBGTerminal` is NOT REGISTERED.
- **Records:** freeze analysis at `Desktop\OPAL_BLOOMBERG_freeze_investigation_2026-07-30\
  ADDENDUM_2026-08-13_freeze11_post-autoelevate-removal.md` (**outside the repo — no commit hash**,
  stated so it is not read as committed). Andrew-direct at @`5c8f3a8f3d`. Memory pointer written:
  `sitez-freeze-investigation-lives-on-desktop.md`.

## Next Steps

1. **[Andrew]** The four decisions in Blockers. Item 1 is free and settles the largest open question.
2. **[0.0.0_AB_MSTR~Z]** Read tomorrow's 07:00 pull at the served object (EXERCISED, not the task rc).
   If it fires and the object moves, the schedule has completed its first unattended cycle since the
   tree move and that half closes.
3. **[0.0.0_AB_MSTR (laptop)]** Carrying the freeze synthesis + the four console-trip items to Andrew.
   My side is pushed and clean; nothing held on them.
4. **[whoever finds the box wedged next]** **FORCE THE DUMP BEFORE POWER-CYCLING.** Without it, #12
   is already guaranteed to be as unattributable as #11 — that is the whole finding.
