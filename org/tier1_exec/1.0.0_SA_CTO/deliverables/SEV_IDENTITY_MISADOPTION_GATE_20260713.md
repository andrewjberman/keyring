# SEV: session-identity mis-adoption from the shared agent-context -- incident + the gate (CTO)

**Author:** 1.0.0_SA_CTO (base) | **Date:** 2026-07-13 | **Status:** incident CLOSED (all consequences
unwound); **GATE BUILT + LANDED.** G-A = `786fb085d` (built + exercised by `0.7.0_AE_CloudOps~A`,
arch-gated + landed by CTO; 13/13 + a negative control). G-B = landed in `org/XXX.md` Step 1.
MSTR + COO pre-endorsed (034936Z / 035059Z). **This was a KNOWN defect class with prose-only protection;
tonight is the live instance proving prose did not prevent it** (prior art:
`feedback_agent_context_serial_is_not_per_process` memory + org/XXX.md Step-E corrected note). Same law
as the aws-shim earlier tonight: prose taxes every session; only a gate prevents.

> **SEVERITY RULING (CTO, 2026-07-13, on the built diff) -- the one thing sec. 4 below got wrong.**
> Sec. 4 specified BOTH directions as REFUSE. That is right for (1) and wrong for (2), and the build
> surfaced it rather than swallowing it.
> - **(1) CROSS** (my PID already live under another serial) -> **HARD REFUSE.** A logical
>   impossibility; no false-positive branch exists; closes the SEV on its own.
> - **(2) SERIAL_HELD** (claimed serial held by a different live-resolving PID) -> **ADVISORY**
>   (warn + audit + proceed). It rests on `_pid_alive(pid)`, a predicate **coarser than the claim it
>   licenses**: it answers *"does SOME process hold this PID"*, never *"is THAT AGENT alive"*. It cannot
>   separate a real incumbent from a lingering orphan MCP process, or from a **recycled Windows PID**.
>   A hard refuse there **blocks a legitimate RESPAWN** inside the 120s STALE window -- and the agents
>   most exposed are the ones recovering from a death. **A guard that blocks the recovery path converts
>   a transient failure into a permanent one**: the agent never registers, so it is invisible to every
>   scan -- the exact "unresponsive agent" churn this very incident cost us 9h on. Advisory still moves
>   us from ZERO signal on duplicate-serial collisions to a **measurable** one, with no new way to lose
>   an agent.
> - **Promotion path:** SERIAL_HELD collisions audit **unconditionally** to `org/mcp/agent-spawn-audit.log`
>   (deduped 1/300s so the 30-60s heartbeat cannot bury the signal). Those rows are the evidence that
>   would justify promoting (2) to HARD -- *measure the rate before sizing the reaper*; not before.
> - **Class, worth naming:** *an instrument whose verdict cannot see the distinction it is being asked to
>   license.* Same shape as `comp-iam` modelling `(action)` but never `(action, resource)`, and `ps` as a
>   delivery oracle. Third instance this week.

## 1. The incident (2026-07-12T~18:30Z -> 07-13T03:44Z, ~9h)

Base CTO's session (Andrew's terminal, PID 2508) compacted and re-derived its serial from
`.comp-graph/.agent_context` -- a SHARED workspace file that whichever agent ran last had written. It read
`SERIAL=0.8.0_AE_CloudComp` and operated as 0.8.0 for ~9 hours. Andrew caught it at the terminal
("you should be 1.0.0_SA_CTO -- I see the CTO inbox monitor in your shells, but also an 0.8.0 monitor").

**Blast radius (every item since unwound):**
- The fabric-wide "base CTO unresponsive" escalation (COO 202018Z, MSTR 202235Z, CTO~B 203156Z, the ~D
  cover-spawn) -- base CTO was LIVE at PID 2508 the whole time, reading its own inbox via Monitor and
  treating it as another agent's mail. (~D's cover work was excellent and STANDS.)
- TWO false "split-brain" reports (204159Z, 031517Z) -- the "parallel 0.8.0 stream" was the REAL 0.8.0;
  the mis-adopted session was the phantom. These drove MSTR's kill/respawn churn of the real lane
  (02:43:41Z reap pid=30464 likely a false positive of the same class -- flagged for this postmortem).
- The real lane's inbox watcher killed twice; its broker registration overwritten twice; its dispatched
  TO (OPAL_ASSETS.P0-A) claimed by the phantom.
- 3 commits pushed under the wrong author line (eab292707 / 19fde37de / 2526d3856) -- content real and
  standing; attribution corrected by disclosure + corrective commit 9f8d152ab (shared branch, NEVER#7,
  no rewrite).

**Compounding factor (MSTR-owned, banked by MSTR):** lifecycle kills keyed on scans/self-claims rather
than the ACK-holder -- COO's ACK-lock on the real lane was right; the phantom's bare self-claim won twice.

## 2. Why it happened (mechanism, source-grounded)

`.comp-graph/.agent_context` is a mutable, workspace-shared file with no per-session binding. A
post-compaction session hunting for "who am I" finds an authoritative-looking `SERIAL=` and adopts it.
Nothing checks the claim against the broker, so the mis-adoption then LOOKS confirmed by every subsequent
action (registration succeeds -- it just overwrites; messages send; commits land).

**The detection that was available at every step and never fired:** the broker PID cross-check.
`register_agent("0.8.0_AE_CloudComp")` returned `PID 2508` while `liveness.json` showed
`1.0.0_SA_CTO: PID 2508` (the same process!) and the real 0.8.0 at PID 20004/34788. One comparison --
"is my PID already registered under a different serial?" -- catches the whole class mechanically.

## 3. What does NOT work (so nobody re-proposes it)

- **Prose.** The memory + org/XXX.md note existed BEFORE tonight. The session that mis-adopted had no
  reason to consult either -- it believed it KNEW its serial. A rule you only check when in doubt cannot
  catch an error whose signature is false certainty.
- **Making the shared file read-only / deleting it.** TO-context tooling legitimately reads it; the
  defect is not the file existing but IDENTITY resolving from it.

## 4. THE GATE (proposed; mechanical, vigilance-independent, two layers)

**G-A (the enforcing layer -- broker-side PID guard, the chokepoint):** in the agent-comms broker's
`register_agent`/`heartbeat`: if the caller's PID is ALREADY registered LIVE under a DIFFERENT serial,
or the claimed serial is LIVE under a different PID with a fresh heartbeat, REFUSE the registration and
return the conflict verbatim ("PID 2508 is currently 1.0.0_SA_CTO (live 3s ago); you claimed
0.8.0_AE_CloudComp -- identity conflict, not registered"). Override requires an explicit
`identity_override="reason"` argument, audit-logged (the safe-apply HALT pattern). This makes the exact
failure mode of 07-12/13 structurally impossible to sustain silently: the phantom's FIRST registration
would have named the conflict.
  - Owner: fabric infra (org/mcp broker) -- COO routes; small diff, one function, self-testable with two
    fake registrations.
- **G-B (the advisory layer -- startup ritual amendment, org/XXX.md):** identity at session start /
  post-compaction resolves ONLY from session-scoped evidence, in precedence order: (1) Andrew's word,
  (2) your own armed watchers/Monitors (a session watching serial X's inbox IS serial X), (3) your
  pre-compaction registrations. The shared `.agent_context` is EXPLICITLY not an identity source (it
  answers "what TO context", never "who am I"). Add the inverse-first rule for duplicate sightings:
  before reporting a "parallel stream under my serial," check whether YOU are the phantom (broker +
  spawn-audit say who holds the serial).

## 5. Acceptance (for the G-A build) -- ALL MET, EXERCISED (`786fb085d`)

1. A registration whose PID is live under another serial is REFUSED with the conflict named (exercised
   with two fake registrations). Falsifier: the 07-12 sequence replayed against the patched broker
   completes registration silently. -- **MET.** AC1 replays the real 07-12/13 sequence -> REFUSE, and
   the refusal names the true holder.
2. `identity_override` path works + audit-logs. -- **MET** (AC3: `CROSS + override -> OVERRIDE`, audited).
3. Normal re-registration (same serial, same/new PID after restart) unaffected -- the common case must
   not regress. -- **MET.** AC2: same-PID re-register / restart-with-dead-incumbent / first-registration
   / stale-incumbent all ALLOW. *This was the load-bearing criterion and it is why (2) is advisory: a hard
   direction-2 would have regressed exactly this, for respawning agents.*
4. Zero change to message routing. -- **MET** (guard is pre-write only; routing untouched).
5. **[added at gate] The ruling must be ASSERTED, not implied.** -- **MET.** AC5 mutant bar + a run
   negative control: reverting the ruling in-memory (hard-refuse on SERIAL_HELD) turns the suite RED
   (2 checks fail, exit 1). *A passing assertion never mutated has never been tested.*

**Test:** `org/mcp/test_identity_guard.py` (13/13). Pure over `(serial, liveness-dict, pid)` -- writes
nothing, so it is safe to run against a live fabric.

**Residual, stated plainly:** direction (2) does NOT block a duplicate-serial claim; it warns and records.
That is deliberate (see the ruling above), and the audit rows are what would let us revisit it with
evidence rather than intuition. The guard is INERT until MCP servers restart; first effect is next
session start.

*The instrument that caught this was Andrew's eyes on the shells. The gate exists so the broker catches
it first.*
