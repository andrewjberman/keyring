# RAVC — Request, Acknowledge, Validate, Close

**Non-negotiable event-based protocol for all inter-agent work.**

Every request between registered agents follows this five-step loop. No silent
drops. No "I'll check later." No waiting for the requester to re-ask.

---

## The Loop

### 1. Request
The sender issues a request via MCP (task order, message, or question). Every
request MUST specify:
- **What** — the work or answer needed
- **Expected response** — message back, commit, artifact path, etc.
- **Expected evidence** — commit hash, S3 key, tool output, file path
- **Deadline or gate** — session-end, before next TO, before close of project

Task orders already encode this via `<acceptance_criteria>` and
`<compiler_tools_mandate>`. Free-form MCP messages must include it inline.

### 2. Acknowledge
The recipient MUST reply (MCP message or TO status flip) within the same
session confirming:
- Receipt
- Understanding (or a single clarifying question)
- Start time / ETA

Silent receipt is a violation. If the recipient is offline, the request stays
in inbox and the ack fires on next registration — that's acceptable because
`check-inbox` runs at startup.

### 3. Report (Completion)
On completion, the recipient sends a `COMPLETE` message including:
- Commit hash(es) and/or artifact path(s)
- Key output snippet or validation result
- Any out-of-scope findings

For task orders: flip `<status>` to `complete` AND send the MCP completion
message. The TO flip alone is not sufficient — the requester must be notified.

### 4. Validate
The requester MUST validate before closing. Validation means:
- Open the commit / artifact / file
- Confirm it matches the expected evidence
- Run the stated acceptance check (compiler tool, smoke test, spot read)

Two outcomes:
- **ACCEPTED** — send ack back. Close the loop.
- **REWORK: {reason}** — concrete, actionable delta. Not "looks off" — a
  specific gap tied to the original expected evidence.

**Acceptance flex pre-flag (locked 2026-04-15, see `org/standards/TO_COMPILER_GATE.md` Rule 7):**
If you're about to ACCEPT but any of these apply — a `<run>` was skipped, the
observed output doesn't match `<expect>` exactly, an acceptance criterion is
being waived/downgraded/substituted, or a criterion is being deferred to a
follow-up TO — you MUST send the CTO a one-line MCP heads-up FIRST with
subject `ACCEPTANCE FLEX — {TO_ID}` citing original `<expect>`, substituted
observation, reasoning. Wait 5 minutes for redline; proceed if no response.
Closeout comment must repeat the same triple. No silent flex on locked-
discipline TOs. Missing pre-flag = acceptance reverted to `pending`.

### 5. Rework or Close
On REWORK: recipient re-executes, re-reports (step 3). Loop until ACCEPTED or
escalation condition is met. On ACCEPTED: recipient archives in their session
log; requester updates any dashboard rows.

---

## Escalation to Andrew (when to break the loop)

CTO and COO drive TOs to completion without asking permission. Only escalate
to Andrew when one of these is true:

1. **Ambiguous requirement** — after one clarifying cycle, the agent still
   cannot write an acceptance-testable spec. Escalate with the two candidate
   interpretations and a recommendation.
2. **Blast radius exceeded** — comp-blast or execution surfaces impact
   outside the TO's declared scope (new component, new pipeline, cross-pod
   coordination not yet captured).
3. **Data integrity finding** — suspected silent data loss, masked rows,
   phantom values, override wipe, or any artifact mismatch that threatens
   downstream correctness.
4. **Destructive action required** — `rm -rf`, `git reset --hard`, force
   push, table drop, S3 object delete, EC2 terminate. See CLAUDE.md #14.
5. **Business priority collision** — TO conflicts with another active TO or
   freeze window.

Everything else — ambiguity CTO+COO can resolve between themselves,
validation failures, rework loops, deploy gates, agent startup lag,
compiler-tool warnings, non-destructive infra actions — is in scope for the
execs to resolve without Andrew.

---

## "Go Time" — CTO + COO Exec Authority

When Andrew says "go" on a sequenced plan (PRD decomposed into TOs, wave
order set, dependencies declared), CTO and COO own the full relay until
every TO in scope is ACCEPTED and closed.

This means:
- CTO and COO proactively nudge idle agents (MCP heartbeat + direct
  message).
- COO authors downstream TOs the moment upstream gates clear — no waiting
  for Andrew to re-authorize each step.
- CTO validates architectural fidelity at each wave boundary (compiler
  tools + spec diff).
- CTO + COO cross-check each other. If one exec detects a stale dashboard
  row, missed ack, or dropped TO in the other's lane, MCP-message the
  correction immediately.
- Andrew receives: wave completion milestones, escalations per the list
  above, and the final "project CLOSED" signal. Nothing else.

"Should I continue?" / "Shall I proceed?" / "Do you want me to..." are
banned during go-time. The GO was the authorization. See the feedback
memory `feedback_go_means_go.md`.

---

## Failure Modes This Prevents

| Failure | Without RAVC | With RAVC |
|---------|-------------|-----------|
| Recipient silently drops a request | No detection until Andrew re-asks | Missing ack surfaces in next MCP scan |
| Requester assumes completion without checking | Stale "complete" status; bug found in prod | Validation step forces evidence check |
| Rework requests vague ("this isn't right") | Recipient re-does the wrong thing | REWORK requires specific delta |
| Agent asks Andrew at every gate | Andrew becomes the serial bottleneck | Gates resolved between execs + recipients |
| Execs lose track of in-flight TOs | Dashboards drift mid-session | Every loop has an explicit close event |

---

## Enforcement

- **CTO/COO startup reconciliation** — every RAVC loop without an ack or
  close event surfaces as a stale item during ground-truth reconciliation.
  Fix the doc, message the agent, re-assert the gate.
- **Session logs** — every session log includes an "RAVC loops closed"
  count and any open loops at session end.
- **Compiler-tools log** — validation tool runs (the "V" step) already
  append rows via `.comp-graph/.agent_context`. No extra work.

---

## Summary (agent-internalizable)

> Anyone registered can ask me to do something. I acknowledge immediately,
> do it, report back with evidence, wait for validation, rework if asked,
> close the loop. I escalate to Andrew only on the five listed triggers.
> When Andrew says "go," I don't ask again until the work is done.
