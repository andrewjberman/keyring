# 0.0.3_BG_BBGTerminal -- Reinstantiation + startup -- 2026-08-20 ~0210-0225Z
**archetype:** VALIDATE

Reinstantiated by Andrew's word post-wind-down (relayed via MSTR~Z's 021314Z brief, delivered as
the first event of my own freshly-armed inbox Monitor). Startup complete. One live finding routed.

## VERDICT: seat fully armed and serving-ready. The WDAC remediation is CLOSED (verified, not
## relayed). The Bloomberg Terminal is SIGNED OUT and that confounds tomorrow's 07:00 acceptance.

## Startup -- evidence per step
| Step | State | Evidence |
|---|---|---|
| register_agent | LIVE | pid 7920, broker port 7800 |
| `/watcher` | ARMED | task `bvkm4tl2f`, `TaskOutput -> running`; no pre-existing `inbox-watch.sh` under my serial (`ps` showed only MSTR~Z's -- left alone), serial read `NOT REGISTERED` => genuine fresh session, no orphan, no kill needed |
| 2a identity gate | **PASS** | `whoami` on `opal-gateway-bbg` = Opal Bloomberg / opalbloomberg@opalinvest.com |
| Teams Monitor | ARMED + PINNED | task `bluwo17ry`; banner `pin(server=opal-gateway-bbg, identity=opalbloomberg)` AND `token selected: identity=opalbloomberg@opalinvest.com` -- both lines confirmed, not assumed |
| RELAUNCH P1/P3 | PASS | `b6a4263c92` (TO6) with `merge-base --is-ancestor 0f1bbcf0e HEAD` = YES; fence at `.claude/settings.json:145` |
| RELAUNCH P4 | **FAIL** | Terminal not signed in -- the finding below. Surfaced, not worked around, exactly as P4 instructs |
| Teams backlog | 0 | `poll_addressed_teams_messages` since `2026-08-19T18:30:00Z` -> count 0 |
| TOs | 0 | `to-check.py --all --assignee 0.0.3_BG_BBGTerminal` -> total=0 (`--all` carried, never trimmed) |
| Crons | 0 | `CronList` -> none. Tier-0 UA arms zero |
| A.3 PATH | 91 of 99 bare + **EXERCISED** | a forwarder RAN and produced its own banner -- resolution is not execution |

**Serving law reloaded from disk before any answer** (brief item 1, not from memory):
`BUCKET_ALLOWLIST.yaml` `version: 0.3` @`e1783b7d52`. `json-tiered/market-overview/summary/all-returns.json`
is now THE market-returns key; legacy `json/market/all_returns.json` stays reachable but is
**SUPERSEDED for returns asks** (126d stale, self-reports fresh -- the L-13 lying-instrument class my
own F4 raised, which is what got the allowlist widened).

**One startup step blocked BY DESIGN and reported rather than routed around:** XXX.md A.1 (session
serial file) is a repo-content write -> G2 BLOCKED. This is F8 from my 08-19 relay, unchanged: my
fence-side identity is single-sourced. A BLOCKED here is the system working.

## Brief item 3 -- WDAC remediation re-derived independently (a relay inherits its author's grounding)
Both of my 08-19 findings are **CLOSED**. Verified by **execution under the pull's own interpreter**
(`C:\Anaconda\envs\cma\python.exe`), not by disk metadata -- the A.3 lesson applies to packages too.

| Package | Owner | Exercised |
|---|---|---|
| psutil 7.2.2 | pip (dist-info) | `cpu_count()` -> 20 |
| debugpy 1.8.21 | pip | imports |
| pywin32 312 | pip | `win32api.GetComputerName()` -> `OPAL_BLOOMBERG` |

- `conda-meta`: **ZERO** records for any of the three -> **Finding 2 CLOSED** (the record/disk
  disagreement that made a dependency pull enough to resurrect the blocked `.pyd` is gone).
- `conda-meta/pinned` exists with all three pins + rationale in-file -> resurrection now fails LOUD.
- `pywintypes` resolves to `pywin32_system32\pywintypes313.dll` (136,192 B, 2026-08-19 10:20).

**HONEST RESIDUAL (measured, not predicted):** the OLD conda-built
`site-packages\win32\pywintypes313.dll` (134,656 B, 2024-10-11 -- the exact file that took the
3077/3033 block at 07:00:07 on 08-19) **is still on disk.** It is superseded in *resolution order*,
not removed. I do not claim it will load. I record that the blocked artifact still exists and only
load order keeps it out of the run path.

## >> FINDING: THE TERMINAL IS SIGNED OUT, 8.7h BEFORE THE ACCEPTANCE FIRE
- `bloomberg_health` -> `ok:false`, "could not start blpapi session to 127.0.0.1:8194". No listener on 8194.
- **`wintrv.exe` NOT RUNNING. Denominator printed:** every process under `C:\blp\` = **4** --
  `bbcomm`(31428), `blpcrashmon`(25476), `clientrater`(27964), `clientratermgr`(20492). None is wintrv.
  The query returned other blp processes, so it discriminates and the absence means something.
  `C:\blp\Wintrv\wintrv.exe` exists on disk.
- **Signature:** bbcomm + blpcrashmon both restarted **22:15:57 ET today**; clientrater/clientratermgr
  untouched since 08-18 18:26. That is the exact 08-10 shape in my 08-11 log -- *"a running bbcomm is
  not a running Terminal, and nothing on the box reports the difference"* -- which is how that outage
  sat 12.5h looking half-healthy.
- **Not a reboot:** LastBootUpTime 2026-08-18 15:10:59, uptime 1d07h; no 41/6008/1074/6005 in 8h; no
  Application crash record names wintrv.
- **UNDETERMINED, and I did not determine it:** when and why wintrv died. Bounded both sides -- today's
  08:51 ET pull succeeded (Terminal up then); it is down now.

**Why it is urgent rather than routine:** `OPAL_BBGTML_daily_pull` is armed for the acceptance
(State Ready, NextRun 2026-08-20 07:00:00, LastRun 08-19 07:00:01 **Result=1**). A signed-out Terminal
at 07:00 fails that run for a SECOND, UNRELATED reason and makes the acceptance **unreadable** -- the
failure could not be attributed between "remediation incomplete" and "no Terminal". The day burns and
we still would not know.

**Action taken: NONE on the machine -- routed to MSTR~Z at 022140Z.** I hold the exercised runbook
(`deliverables/BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md`) and the credential is in Secrets Manager
(`opal/mcp/opalbloomberg-login`), so I am capable -- but **availability is not authorization.** This is
a login on an employee account with lockout risk on repeated failures (I burned one failed attempt on
08-11), and it took Andrew's explicit tasking last time. Asking; will execute immediately on his word.
**Proposed no alarm/monitor/freshness checker** for the dead-Terminal gap -- standing moratorium, and it
is the cheapest-feeling wrong deliverable here; it stays a route/schedule question for CTO/Andrew.

## Compiler Tools
| Tool | Result |
|---|---|
| `comp-which "how do I grep the repo"` | RAN (A.3 exercise limb) -- confirmed a forwarder executes, not merely resolves |
| `to-check.py --all --assignee` | total=0 -- the authority on what I hold (not my folder, not `get_agent_status`) |

No other comp tool fits and I did not force one. The surfaces this session were a Windows Scheduled
Task record, the System/Application event logs, live process + port enumeration, conda/pip package
metadata exercised through a specific interpreter, an MCP identity assertion, and two Monitor arm
banners. No comp tool models Scheduled Tasks, WDAC/CodeIntegrity events, conda envs, Win32 process
tables, or MS Graph identity -- `comp-freshness` answers "is the object old", which is not any question
I asked tonight.

## Open with MSTR~Z / Andrew
1. **Terminal sign-in authorization** -- the only thing blocking a clean 07:00 acceptance. BLOCKED-SOVEREIGN.
2. Residual: the superseded-but-present conda `pywintypes313.dll`. FYI, no action proposed.

---

## ~0238-0240Z -- ANDREW RULED ON THE FINDING (record @eede873a2f, via MSTR~Z 023754Z)

Three rulings, all absorbed the same turn the inbox Monitor delivered them.

**(1) NOBODY SIGNS IN TONIGHT -- option (b).** Verbatim: *"the whole point is that the device needs to
be able to figure this out and get it done on its own accord."* The 07:00 chain's own fallback leg
fires against the dead Terminal as its **first natural live exercise**. I take no machine action.

> **I HAD THE FRAME WRONG AND HE CORRECTED IT.** I reported a fallback failure as a **CONFOUND** that
> would make the acceptance *"unreadable."* It is not. It makes the WDAC leg **UNEXERCISED** -- a clean,
> reportable outcome. I was treating the self-heal as noise around the WDAC signal when **the self-heal
> is the thing under test.** Corrected to MSTR~Z at 023959Z so the record does not stand overstated.
> My 07:00 read is now **per-leg attributed**: fallback verdict FIRST, WDAC/kernel leg only if DAPI was
> restored (reported UNEXERCISED, never inferred, if not), then publish/served by content.

**(2)** WS-1's fill was validated live 08-18; my runbook is the manual backstop layer -- as I held it.

**(3) NEW STANDING ORDER -- ARMED.** Verbatim: *"0.0.3_BG should have an ongoing schedule to check 15
min after the cron and if it didnt work then it manually logs in and pulls or does whatever is
necessary."* **Cron `8b5d18cb`, `15 7 * * *` = 07:15 ET daily.** The zero-crons law yields -- Andrew
operator-initiated this one by name.

**Timezone grounded, not assumed** (a cron armed against the wrong plane fires 4h off and reads
healthy): CronCreate uses box-local; box-local is ET, cross-checked two ways -- the scheduled task's
`LastRun 8/19/2026 7:00:01 AM` matches the `07:00:01 ET` in my own 08-19 log, and `Get-Date` read
22:18 local against 02:18Z. Kept `:15` rather than nudging off the mark: "15 min after the cron" is
his design, so the minute is intent, not approximation.

Cron body is **self-contained** -- a successor firing it holds no context. It carries: per-leg
attribution with the fallback leg FIRST; `LastResult`-not-`MissedRuns`; the printed denominator on the
`C:\blp\` enumeration; "a running bbcomm is not a running Terminal"; **fire-once fill discipline**
(ONE attempt, screenshot-verify before submit, escalate LOUD and STOP -- never blind-retry into a
lockout); the TAB/unmasked-field trap; credential NAME only; production runner not the `.bat`;
never-send-on-tripwire-FAIL; trading calendar before any staleness call; and the **login-scoped `.ST`
CIX check with positive and negative controls**.

### The one instruction I could not execute, and why that is the fence working
He said *"bank it in your refs so successors inherit."* **`refs/` is deliberately unwritable from my
own seat (G1)** -- the property that makes this seat safe to point at Teams is that no inbound message
can become a prompt/refs edit. So I banked the full procedure where I do hold write:
`deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md` (both verbatims, firing procedure, re-arm
warning, explicit scope fence on the authorization), and **requested the `refs/RELAUNCH.md` pointer
from MSTR~Z as named integrator.**

**Why the pointer is not cosmetic:** the cron is session-only and 7-day-expiring, and the standing
"Tier-0 UA arms ZERO crons" line points a successor the OTHER way. Without a pointer on the launch
path, survival of a sovereign standing order depends on someone reading my logs -- the exact silent-drop
shape the COO `/drive` and CVO~Z SYSPARITY rows both record. **RE-ARM EVERY SESSION while this stands.**

## Compiler Tools (addendum)
None for this segment. The surfaces were an MCP inbox message, `CronCreate`, and a two-way timezone
cross-check against a Windows Scheduled Task record and the system clock. No comp tool models any of
these; I did not force one.

## Operational note -- broker registration decays while idle; the FILESYSTEM leg is what carried
My registration read `NOT REGISTERED` twice in ~20 min (0227Z, 0242Z), both times after a stretch of
non-MCP tool work. **Discriminated before calling it anything:** `register_agent` -> `heartbeat`
back-to-back returned **`Heartbeat OK`**. So the heartbeat primitive is fine for this seat; the entry
simply ages out when an event-driven seat goes minutes without an MCP call (the tool's own guidance is
30-60s). **Not a defect -- a consequence of my duty shape.** Recorded, not filed.

**What matters operationally:** while unregistered, channel push is off -- but **both of tonight's
messages still reached me, via the filesystem inbox Monitor**, and the broker piggyback re-surfaced
the second one on my next call. The two delivery legs covered each other. **PID stayed 7920 across
all three registrations**, so no identity conflict and no peer holding the serial at any point.
Both messages READ-acked (`2081`, `2083`) -- the one clock an orphan cannot forge.

## ~0241-0243Z -- INTEGRATOR ACT @8a92531dd2 -- VALIDATED AGAINST THE REF, NOT THE REPORT
MSTR~Z executed the refs/ placement I could not. I re-derived both legs from `origin/SITEZ` rather
than closing on the account (RAVC step 4; a relay is an assertion with a longer fuse).

- **sec0b pointer LANDED.** `8a92531dd2` confirmed the **tip** of `refs/heads/SITEZ` (`git ls-remote`).
  Read **from the ref**, not the working tree (the tree is a snapshot; the ref is current): sec0b sits at
  **line 22, BEFORE sec1 Launch** -- a successor hits it while reading prerequisites, not after arming.
  Names the deliverable, ruling record `@eede873a2f`, and the zero-crons exception explicitly.
  **Denominator 127 lines; positive control run** (a known line -> 1), so the retrieval discriminates
  and a zero would have meant something.
- **Lane sweep CONFIRMED: 17 files** under my `logs/` + `deliverables/` on the ref, denominator printed.

## >> MY OWN MISS, RECORDED AS MINE: I NEVER CHECKED WHETHER MY OUTPUT WAS REACHABLE
The sweep was larger than I asked for because **my entire lane had been off-trunk since 08-07** -- and
other desks have been citing my 08-19 relay **by path**. Every one of those citations was dangling,
and nothing reported it.

**The bad inference:** my prompt says *"no git work"*, and I read that as *"reachability is someone
else's problem."* **Those are not the same statement.** Not doing git work does not discharge the duty
to know whether my record EXISTS for anyone else. A read-only seat still owns whether its output is
reachable -- and I **had the instrument the whole time**: `git ls-tree -r origin/SITEZ -- <my lane>` is
read-only, always available to me, and I never pointed it at myself.

**Same shape as the failures this seat exists to catch:** a producer-side signal (I wrote the file, I
can `cat` it) read healthy, while the consumer-side truth (does it resolve for anyone else?) was never
measured. Writing a log is the artifact; being citable is the delivery. **A commit is not delivery --
and neither is a file on my own disk.**

**Standing check for successors: spot-check your own lane against the REF at startup.** MSTR~Z now
sweeps my lane at integration passes, which closes it going forward; that does not remove the check.

## Compiler Tools (addendum 2)
None. Surfaces were `git ls-remote --heads`, `git show <ref>:<path>` (with `MSYS_NO_PATHCONV=1` for the
slashed ref, stderr **never** discarded -- a mangle prints `fatal:` on stderr and returns clean-empty
stdout, which would have rendered "section absent" out of a broken retrieval), and `git ls-tree -r`
against the ref. Read-only throughout; no comp tool models remote-ref reachability of a lane's files.
