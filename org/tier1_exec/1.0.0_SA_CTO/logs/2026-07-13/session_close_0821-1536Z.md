# 1.0.0_SA_CTO — session 0821Z–1536Z — host outage, fabric recovery, the INF phantom, and Andrew's TIME-LOCK ruling

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, COORDINATE, IMPLEMENT

## Summary

Session opened on a dead fabric. Diagnosed the outage, recovered the fabric, then spent the day on an INF
served-number incident in which **six proposed mechanisms were all falsified** and the real cause was in a log
file nobody had read. Closed with an **Andrew sovereign ruling** that settles advisor attribution permanently.

**28 commits.** Everything committed and pushed to CLOUD. **Nothing served — the INF served spine is untouched
since 2026-07-10.**

## 1. THE OUTAGE — not a host crash

Andrew: *"the computer may have crashed."* It did not.

    08:16:17Z  low virtual memory -- python.exe (PID 19224) at 39.9GB
    08:16:45Z  dwm.exe crashes
    08:17:56Z  low virtual memory -- same python at 43.2GB
    08:19:20Z  *** WindowsTerminal.exe FAULTS *** (module igd10umt64xe.DLL, the Intel GPU driver)
    08:19-08:20Z  all 8 agent sessions die (last telemetry fabric-wide: CVO~B 08:20:09Z)

The box **never rebooted** — up continuously since 05:05:10Z (a clean, user-initiated restart 3.5h earlier).
**WindowsTerminal was hosting every agent tab and it took them all with it.** Commit limit on this host is
**46.2GB**; the leaker was at **43.2GB** — one process took essentially the machine's entire memory budget.

**WHAT PYTHON 19224 WAS: STILL UNIDENTIFIED, AND I DID NOT GUESS.** Process gone, no process-creation audit,
no agent transcript shows any heavy python job. `INFERRED`, non-actionable (Rule 22).
**Built `.tools/mem-sentinel.ps1` (`3edf3b029`) so the next one NAMES ITSELF** — records the command line of
any process crossing 4GB private bytes. Armed under a persistent Monitor. **Self-test FAILED first** (my
harness's `Start-Process` quoting killed the hog, and the harness then reported *"the sentinel did not name
it"* — collapsing COULD-NOT-OBSERVE into OBSERVED-NOTHING). Fixed; it now proves the hog is real before it may
judge the sentinel. **PASS on the second run.**

## 2. FABRIC RECOVERY — the broker was forging liveness

`agent-poller.py:_pid_alive()` calls Windows `OpenProcess` without `GetExitCodeProcess` — which **succeeds on
an exited process**. So a dead agent's poller heartbeats **forever**, and `register_agent` then refuses the
serial as *"held by a LIVE process."* **The forgery made dead agents UNRESPAWNABLE.** (MSTR's root-cause;
verified by me with positive controls before acting.) Cleared 8 zombie registrations → broker truthful.

**AND I BROKE THE FABRIC DOING IT.** Every live agent carried a healthy watcher **and** an orphan racing it.
I `Stop-Process -Force`'d the 5 orphans from PowerShell — **the kill CASCADED and took all 10 healthy watchers,
including my own.** *I deafened the entire fabric while repairing its hearing.* Caught **only** because I had
asserted the spare-list before the kill (`must be 10/10` → came back **0/10**). Zero agents harmed; CVO and DS
auto-re-armed. **Use `.tools/kill-orphans`, never `Stop-Process` on an MSYS bash.**

## 3. FABRIC-INFRA FIXES (all committed, all exercised)

| Fix | Commit | Note |
|---|---|---|
| never-rules-gate: override marker was a **universal disarm** | `0332d5d55` | one string anywhere waived EVERY rule. 54/54, proven-RED two-sided. |
| never-rules-gate: **early-exit disarm** (F-022, self-found) | `0332d5d55` | a scratch-branch rebase `exit 0`'d the whole hook, skipping terraform/stash. |
| `deregister_agent` **strips the ~lane suffix** and kills the BASE agent | `47163c850` | **IT DEREGISTERED ME, MID-INCIDENT.** register writes `~B`; deregister deleted the base. 15/15, proven-RED. |
| deregistration wrote **NO audit line** (750 entries, zero records) | `e5fcb9e58` | the one primitive that can un-person an agent, with no trail. **My first draft referenced a `WORKSPACE` constant that does not exist — a SILENT NO-OP AUDIT, shipped as the fix FOR a missing audit.** Caught by checking. |
| orphan-reaper had **NEVER ONCE REAPED ANYTHING** and stamped "cleaned" every time | `920a7bb77` | MSTR's; 3 defects. **`shutil.which("bash")` reports a healthy bash while `subprocess` runs the WSL shim — THE OBVIOUS DIAGNOSTIC EXONERATES THE CULPRIT.** I verified it on this host before signing. |
| ...and that fix was **INERT ON THE RUNNER** | `8dfece4dc` | **suppressed by the residue of the bug it fixes** — the old hook wrote its "cleaned" marker unconditionally (368 stale markers, every live session). Fixed by **versioning the marker**, not by a destructive sweep. |
| never-rules-gate **P1**: negative control RED + a hole that **executed a real commit message** | `071fbda9f` | see §6. |
| governance audit logs **ALL UNTRACKED** | `fcff61ebc` | 13 logs / 34,180 lines. **MSTR's census found 4.** Snapshot archived + byte-verified; new `GOVERNANCE_AUDIT` owned-paths lane. |
| ...and I **swept in MSTR's live-log un-ignore** | `29f35fcca` | would have conflicted on every pull, for every agent, forever. **Caught by my own control.** |
| CLAUDE.md **15,118 → 3,652 words** (Andrew-directed; MSTR-authored) | `71b37d07d` | Rule 22a alone was **11,016 words = 72%** — **and I wrote almost all of it today.** 7 NEVER + 26 numbered rules verified intact; both pointers resolve. |

## 4. THE INF INCIDENT — six mechanisms, all false

**THE PHANTOM (real, served, client-facing):** `patrick_scanlan` short **$52,604.80** since 2026-07-09; a
phantom advisor `inflection_unmapped_rep` carrying his money; re-fires every run.

**ROOT CAUSE (DS, source-confirmed):** Orion's `/NewPortfolio` **stopped returning 3 accounts on 07-09**.
`rep_id` is MANUFACTURED by an `accounts_v2` join (`convert_transactions_to_silver.py:519`), so the departure
NULLs it → `INF_C_01`'s 4-entry map yields NaN → `.fillna()` → catchall.

**MECHANISMS PROPOSED AND FALSIFIED