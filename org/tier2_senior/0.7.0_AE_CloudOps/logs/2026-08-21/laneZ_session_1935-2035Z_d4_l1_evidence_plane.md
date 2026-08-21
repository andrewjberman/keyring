# 0.7.0_AE_CloudOps~Z -- session 1935-2035Z: D4/ETFS_POSITIONING L1 evidence plane

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

Site-Z CloudOps launch session. Arrived into the ETFS_POSITIONING priority declaration
(Andrew-direct ~19:3xZ via `0.0.0_AB_MSTR~Z`, relayed msg 4585). Startup per `org/XXX.md`,
then work in the one plane this seat owns that the producing seat structurally cannot
self-verify: the scheduled-task / power / S3-configuration layer under L1.

---

## Startup

- `/watcher`: registered `0.7.0_AE_CloudOps~Z` (PID 27220, broker 7800); persistent inbox
  Monitor armed, task `bjq7kuk0h`, confirmed `running` by TaskOutput. No orphan for this
  serial (6 other watchers live on the box, all with live parents, none touched).
- `org/XXX.md` Step 1b-D (owned-paths hook, idempotent no-op) + 1b-E (`.comp-graph/.agent_context`).
- **Step 1b-F: ZERO crons.** `CronList` empty at launch and at close. My row is the
  Tier-2/3 worker row -- `/watcher` once, zero crons, event-driven.
- Rules 26 + 27 read from `origin/SITEZ`, byte-identical to the session-start copy.
- Branch SITEZ. Note HEAD advanced ~4x during the session (7 seats share this checkout).

## Inbox

10 messages read and ACKed (2795, 2837, 4585, + the D4 thread). Dispositions:
- `D7_TICKETING.WA-APPLY` @`4e89e26736` and `GW-APPLY` @`8c1f26d84b` -- both **withdrawn by
  `2.0.0_SA_COO~Z`** under Rule 26 (work moved to site Z). Nothing to approve or hand back;
  nothing held on either.
- `0.4.0_DT_ClientPlatform~Z` msg 2795 (TAC-2 step-1) -- misrouted, explicitly not mine.
- Andrew-direct (2837): agents refer to other agents by FULL SERIAL. Adopted.

---

## Current State

### What I established (all in the cloud/OS plane, all on live primitives)

**1. D4/L1 corroboration.** Task `OPAL_BBGTML_daily_pull` Ready, NextRun 08/22 07:00,
LastResult 0. ETF leg reachable from both the publish-success path and the `:pub_failed`
fall-through; `RC_ETF` never assigned to `%RC%`; exit codes 60-63 disjoint from the models
chain's 0/1/9/20/30/40/50 -- isolation is structural, read from control flow not comments.
7/7 objects under `bbg/2026-08-20/`, matching the order's file list, s3api/UTC.

**2. Credential gap closed (negative result).** Box identity
`arn:aws:iam::313476888478:user/Andrew_Berman`, static key in `~/.aws/credentials`, no
`AWS_PROFILE`/`AWS_ACCESS_KEY_ID` override. Task principal `Opal Bloomberg`, Interactive --
the same user owning that file. Same credential resolution scheduled vs agent-invoked.
**Derivation, not an exercise** -- stated as such.

**3. Bucket configuration.** `opal-data-etfs` lifecycle = ONE rule, `abort-incomplete-mpu-7d`
(reaps incomplete MPUs, **expires no objects**). Versioning **never enabled** (empty response,
not `Suspended`). Consequences: nothing empties `bbg/` automatically, AND an empty listing
means genuinely empty rather than delete-markers hiding objects, AND same-key writes are
**destructive and unrecoverable**.

**4. THE L1-2 FINDING (primary).** `etf_daily_pull.py:57-58` derives `as_of = today + BDay(-1)`.
Computed on the deployed interpreter (PY_AWS Python311, pandas 3.0.3):

| fire (07:00) | weekday | as_of |
|---|---|---|
| 2026-08-22 | Sat | 2026-08-21 |
| 2026-08-23 | Sun | 2026-08-21 |
| 2026-08-24 | Mon | 2026-08-21 |
| 2026-08-25 | Tue | 2026-08-24 |

**First three fires -> ONE distinct as_of, not three.** All write the same keys; unversioned;
so fires 1+2 leave **no S3 trace**. L1-2's named instrument (live S3, s3api) could not
distinguish three fires from one Monday fire.
**THE PRODUCER IS CORRECT** -- this is NEVER#1 working as designed (Friday's data IS the right
answer Sat/Sun/Mon). The **criterion** mis-assumed that consecutive fires yield distinct dated
artifacts. Resolving the trading calendar before reporting is what kept this from being filed
as a false "stuck on one date for three days" outage.

**5. All amended evidence sources measured blind.** `LastRunTime`/`LastResult` single-valued;
`Microsoft-Windows-TaskScheduler/Operational` **IsEnabled=False, zero records**;
`run_manifest.json` same key all three fires. Named the per-fire wrapper logs
(`%USERPROFILE%/opal_bbg_logs/bbg_tplus1_<stamp>.log`, 30/30 present) as the surviving surface.

**6. I FALSIFIED MY OWN ADOPTED CLAIM.** I wrote "the instrument discriminates" (scheduled vs
ad-hoc); `1.0.0_SA_CTO~Z` adopted it verbatim into the amendment. **It was wrong** -- the
07:00 log had 0 ETF-LEG lines because the leg did not exist yet (appended 10:47:32, 3h47m
after the fire), a **code-change artifact**, not trigger provenance. Corrected within ~12
minutes, at the reach it had been adopted. `.cmd:215` sets `ETF_RUN_CLASS=scheduled`
**unconditionally on any wrapper run**, so A1 closes the direct-python axis and cannot close
the human-vs-scheduler axis; four hand-run wrapper invocations sit in today's log directory as
the standing proof.

**7. `StartWhenAvailable=True`** -- a genuine scheduled fire need not carry a 07:00:0x stamp.
Supplied the **false-negative** direction to a bound that had only considered false positives.
Also `WakeToRun=False`, `RestartCount=0`.

**8. My weekend-logon flag: DISCHARGED.** `2.0.0_SA_COO~Z` discharged it with better evidence
than mine (four weekend 07:00 fires already logged: 08/08, 08/09, 08/15, 08/16). My auto-logon
measurement is the mechanism behind it: `AutoAdminLogon=1`, and empirically the console session
logged on **within ~1 min of the 08/18 boot**. Registry alone was ambiguous (`DefaultPassword`
absent reads the same whether LSA-backed or broken); the boot/logon delta settled it.

**9. THE TWO MISSED FIRES, DIAGNOSED** (`2.0.0_SA_COO~Z` found them and declined to diagnose):
- **08/13** -- box DEAD 08/12 22:58:14 -> 08/13 17:37:45 (18h39m; id 41 + 6008 + 6005). The
  07:00 window fell inside it. The 17:45:54 run is 8m09s post-boot, which fits **catch-up**
  far better than a hand run (strong inference, not measured -- no trigger record exists).
- **08/11** -- **box AWAKE and healthy**: 33 System events in the 06:00-08:00 window, zero
  sleep/resume, no reboot. Fire absent, **cause unestablished.** This is the concerning one:
  **uptime does not protect the streak**, and the intuitive mitigation would not have prevented it.
- RMM patch window characterised: 08/12 03:52:45 `Advanced Monitoring Agent\winagent.exe`
  initiated a restart, then TrustedInstaller x2 -- three reboots in ten minutes, completing
  ~3h before the fire, which still succeeded. Two unexpected shutdowns in ten days (08/10, 08/12).

### Detector I own (disarm, not remediation)

Working-tree hazard: the scheduled task executes the shared checkout (7 seats), so a mid-window
edit resets what the L1-2 streak is a streak *of*, invisibly. Baseline hashes pinned, then
**re-pinned after A1 landed** (predicted and executed):

```
scheduled_daily_pull.cmd  89cc9c26f72b779966ff25e126ca0c2761303a3fcf99edb47e0e1d9a4faa44be
etf_daily_pull.py         871f4dc0e343ebf5464dce9bc33a59d529ad8ee90a6e858f5eba8f1e86cd3932
```
Both worktree == HEAD, porcelain clean, A1 `6729f104b7` confirmed ancestor, both A1 anchors
verified present **in the working tree** (`.cmd:215`, `.py:44`). **DISARMED != REMEDIATED** --
whether a scheduled task should execute a shared mutable checkout is UNOWNED, routed to
`1.0.0_SA_CTO~Z`.

### Outcome at other seats

L1-2's evidence source was amended **four times** and settled on option (b) -- the per-fire
wrapper logs, with an **unclosable residual stated on the cert's face** rather than papered
over. `1.0.0_SA_CTO~Z` ruled the provenance cleanup must not run before the hardcoded-floor
item is addressed (the item-4/item-5 coupling I surfaced). `3.0.0_SA_CVO~Z` filed S6 (L1-4
cannot fail across its own evaluation window) off the L1-4 edge.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | `"does an S3 bucket have a lifecycle expiration rule or versioning that could empty a prefix"` | PASS (routed, no fit) | Returned comp-iam / comp-keys / comp-whoread, near-tie, 79 tools. **None models bucket lifecycle or versioning config.** Correctly refused to guess. |

**What worked:** `comp-which` printed a near-tie warning and explicitly said the order is not a
ranking -- that is what told me no tool covered the question rather than that I had picked badly.

**What failed:** nothing.

**Gap found (routable):** **no comp-tool answers bucket-level LIFECYCLE or VERSIONING
configuration.** `comp-keys` answers what EXISTS under a prefix; nothing answers what will
DELETE it, or whether an empty listing means empty. Both were load-bearing tonight -- the
versioning state is what made "fires 1+2 are destroyed" a measurement rather than a guess.
Raw `aws` inspection used under an inline `# rail-checked:` marker naming the search first.

---

## Blockers

**None.** Nothing held, nothing awaiting me. Both former apply TOs withdrawn by their issuer.

---

## MCP traffic

~18 messages handled; 7 substantive dispatches sent (all 100% DELIVERED, per-recipient maps
verified; bodies positively controlled by grepping a pinned hash present in all four delivered
files, negative control 0).
**One send REFUSED for an empty body** -- malformed parameter tag; the broker's guard caught it
and the same malformation had leaked XML into my broker summary. Both fixed. Recorded because a
send receipt does not prove a body arrived: an empty body and a real one are byte-identical at
the recipient.

---

## Next Steps

- [1.0.0_SA_CTO~Z] UNOWNED remediation: should a scheduled task on this box execute a shared
  mutable checkout at all? Route or discard. No gate proposed and none implemented.
- [1.0.0_SA_CTO~Z] Monday certifier reading instruction, now symmetric (mine + COO's):
  **a stamp is not a trigger record in either direction.**
- [OPEN, unowned] **Why did the 08/11 07:00 fire not happen on a healthy, awake box?** Real
  investigation, not L1-2's, and largely unrecoverable (Operational log disabled, so no
  task-side record for that date exists). Deliberately not started tonight -- doing so would
  put this seat inside the criterion's own evidence window.
- [0.7.0_AE_CloudOps~Z] If the A2 fix lands before 08/24, **re-pin the detector at that commit**
  so the streak restarts visibly rather than running three fires over two programs.
- Discipline, not a gate: nobody hand-runs `scheduled_daily_pull.cmd` before 08/24 -- it is the
  one act that makes option (b)'s cert language true rather than merely careful.
