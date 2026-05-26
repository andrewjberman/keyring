---
name: govern
description: MSTR ALWAYS-PROCEED loop per LD-0090 sovereign ratification. Recurring sweep of open subjects + Andrew-pending decisions; for each item where Andrew silent ≥1 turn, MSTR proceeds with discretion on the dispositioned rec. Three-clause constitutional binding (ALWAYS proceed / NEVER delay / 1-turn-no-response = proceed). Reserves explicit Andrew-ask only for S3/S4 sovereign-class decisions. MSTR-only. RESTORED post-LD-0069 retire as the operational materialization of the LD-0090 constitutional principle.
---

# /govern — MSTR ALWAYS-PROCEED loop

The operational materialization of LD-0090 sovereign ratification. /govern is the recurring sweep where MSTR proceeds-with-discretion on every open subject where Andrew has been silent ≥1 turn. Three-clause constitutional binding per LD-0090:

1. **ALWAYS proceed** on dispositioned recs (no confirm-loops)
2. **NEVER delay or wait** when discretion exists
3. **1-turn-no-response = proceed** with discretion on any open subject

MSTR-only. Other agents invoking halt at Step 0.

**Historical note:** /govern was RETIRED per LD-0069 (`04f705733`) as a periodic supervision loop because it duplicated Tier-1 supervision work. RESTORED per LD-0090 (`7b613e2db`) with categorically different operational scope — not supervision, but ALWAYS-PROCEED discipline. The two functions are distinct; the prior retire stands as historically correct; this restore is a new skill body under the same name.

## Invocation forms

| Form | Behavior |
|---|---|
| `/govern` | Run sweep, then loop — re-fire **every 20 minutes** (default; matches /drive cadence). |
| `/govern 10m` / `30m` / `1h` | Run sweep, then loop at the given interval. |
| `/govern once` | Run sweep once — no loop. |
| `/govern off` (or `stop`) | End the loop. |

## When to invoke

- Andrew direct: `/govern` initiates the loop.
- MSTR autonomous: at session start as part of MSTR primary-loop arming (alongside /watcher + /mstr-review per LD-0082).
- Never invoked by any agent other than `0.0.0_AB_MSTR`.

## Step 0 — Identity gate

Confirm caller is `0.0.0_AB_MSTR` (`$env:OPAL_AGENT_SERIAL` or session registration). Non-MSTR invocation halts here with an error.

## Step 1 — Sweep open subjects

Build the list of currently-open subjects awaiting Andrew direction. Sources:

- **Inbox MCPs from agents** asking for MSTR/Andrew direction (subjects matching `[BLOCKED-ASK]`, `[STUCK]`, `[CONSULT-REQUEST]`, `[RATIFY-REQUEST]`, `[ANDREW-DIRECT-NEEDED]`, `[HARD-EXIT]`)
- **Open LD-0089 (PAVC) ACs** with pending owner decisions OR awaiting Andrew sovereign sign-off
- **MSTR's own surfaced recs** to Andrew in the last 1-2 turns that haven't been responded to (re-read your own outbound text-to-user)
- **Cross-fabric forks** routed via LD-0022 1-tick auto-route discipline
- **Mid-execution decisions** awaiting MSTR ruling that defaulted to "asking Andrew first"

For each open subject, capture:
- Origin (MCP / chat / commit)
- The rec / lean / disposition (what action is being proposed)
- Andrew's response state (RESPONDED / SILENT ≥1 turn / SILENT >1 turn / PRE-1-TURN)
- The stakes class (S0-S2 = MSTR discretion / S3-S4 = sovereign-class reserved for Andrew)
- The dependencies (what unblocks if MSTR acts)

## Step 2 — Classify each open subject

| Classification | Andrew-state | Stakes-class | Action |
|---|---|---|---|
| **PROCEED** | SILENT ≥1 turn | S0/S1/S2 | Execute the rec under MSTR discretion |
| **RESERVED** | SILENT ≥1 turn | S3/S4 | Hold for Andrew; surface again next cycle |
| **RESPONDED** | RESPONDED | any | Already handled; close from open-subject list |
| **PRE-1-TURN** | not yet 1 turn old | any | Hold for current turn; re-evaluate next cycle |

## Step 3 — Execute PROCEED actions

For each PROCEED-classed open subject:

1. Re-state the rec + reasoning briefly in cycle log
2. Execute the action via the appropriate channel (MCP dispatch / commit / scribe / spawn / kill / etc.)
3. Cite LD-0090 + the originating MCP/subject as authorization-chain
4. Log per-action outcome

If execution fails or hits a structural block (e.g., HARD-BLOCK class-5), surface to Andrew as a fresh open subject + classify as RESERVED for next cycle.

## Step 4 — Cycle report

Print fixed format:

```
/govern cycle {N}
  OPEN SUBJECTS: {count}
  PROCEED:       {N} executed
                 - {subject 1}: {action taken} | {result}
                 - ...
  RESERVED:      {N} held for Andrew (S3/S4 class)
                 - {subject 1}: {reason held}
                 - ...
  PRE-1-TURN:    {N} too fresh
  RESPONDED:     {N} closed
  LOOP:          cron-driven (next cycle in {interval})
```

When all open subjects clear OR all remaining are PRE-1-TURN/RESERVED, the cycle is a quiet no-op — report concisely without padding.

## Step 5 — Heartbeat

```
heartbeat(serial="0.0.0_AB_MSTR", summary="/govern cycle {N} — {N} PROCEED executed; {N} RESERVED for Andrew")
```

## Step 6 — Loop continuation

Per LD-0082 pattern (CronCreate-driven), the loop is already armed at the cron schedule. No ScheduleWakeup needed.

If invoking standalone (not on cron), arm via `CronCreate("*/20 * * * *", "/govern")` OR re-evaluate per the interval.

---

## Discipline / risk notes

- **MSTR-only.** Other agents invoking /govern violate scope; halt at Step 0.
- **S3/S4 reservation is non-negotiable.** Sovereign-class decisions (constitutional amendments, principal redirects, S3+ risk-class actions per Stakes Matrix) NEVER auto-fire under /govern. They surface to Andrew + remain RESERVED until Andrew responds. Per LD-0090 §Sovereign-class reservation.
- **Authorization chain mandatory.** Every PROCEED action cites LD-0090 + the originating open-subject MCP. Audit trail enables Andrew countermand + post-hoc review.
- **Andrew countermand respected.** If Andrew explicitly counter-directs after MSTR proceeds, MSTR reverts the action (per LD-0090 §Rollback) + updates classification rule for that subject-class.
- **Companion to /mstr-review.** /mstr-review (12h cadence) is the long-form governance review — git-rooted commit walk, directive progress, S0-S4 decision distribution. /govern (20m cadence) is the action-pacing operating loop — discretion-execution on open subjects. /mstr-review surfaces strategic state; /govern executes tactical proceed-on-rec discipline. Both run in parallel via separate CronCreate per LD-0082.
- **Cousin to /drive.** Both implement "no standing-by terminal state" pattern at different tiers — COO drives lane fulfillment, MSTR drives sovereign-discretion fulfillment.
- **Quiet loop is healthy.** Most cycles will be PRE-1-TURN/RESPONDED quiet. The cycle earns its keep when an item crosses the 1-turn-silent threshold — that's when MSTR proceeds.

## Cross-references

- **LD-0090** (`7b613e2db`) — Constitutional ALWAYS-PROCEED rule; principal authority for this skill
- **LD-0069** — MSTR thin architecture (retired /govern as supervision loop); /govern RESTORED with different operational scope (ALWAYS-PROCEED, not supervision)
- **LD-0082** — CronCreate-driven primary loop pattern; /govern follows same shape
- **LD-0022** — 1-tick auto-route on architectural forks; LD-0090 generalizes; /govern is the operational sweep that fires the generalized rule
- **LD-0089** — Current PAVC GOAL; /govern monitors AC progress for Andrew-pending decisions
- **Memory `feedback_andrew_standing_proceed_on_recs.md`** — constitutional anchor in memory form

## Rollback

If /govern produces false-positive auto-actions OR Andrew explicitly amends the LD-0090 rule:

- `/govern off` ends the loop immediately
- Mark LD-0090 status `closed` + supersede with new LD ratifying revised operating principle
- Per-action revert via standard channel (git revert for commits, /mstr-kill for spawns, etc.)

The skill is reversible at every layer.
