# SEV: session-identity mis-adoption from the shared agent-context -- incident + the gate (CTO)

**Author:** 1.0.0_SA_CTO (base) | **Date:** 2026-07-13 | **Status:** incident CLOSED (all consequences
unwound); GATE PROPOSED (sec. 4) -- COO to TO-record + route the build; MSTR + COO pre-endorsed
(034936Z / 035059Z). **This was a KNOWN defect class with prose-only protection; tonight is the live
instance proving prose did not prevent it** (prior art: `feedback_agent_context_serial_is_not_per_process`
memory + org/XXX.md Step-E corrected note). Same law as the aws-shim earlier tonight: prose taxes every
session; only a gate prevents.

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

## 5. Acceptance (for the G-A build)

1. A registration whose PID is live under another serial is REFUSED with the conflict named (exercised
   with two fake registrations). Falsifier: the 07-12 sequence replayed against the patched broker
   completes registration silently.
2. `identity_override` path works + audit-logs. 3. Normal re-registration (same serial, same/new PID
   after restart) unaffected -- the common case must not regress. 4. Zero change to message routing.

*The instrument that caught this was Andrew's eyes on the shells. The gate exists so the broker catches
it first.*
