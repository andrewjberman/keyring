# Proactive Downstream Check Protocol — 1.0.0_SA_CTO

**Date:** 2026-03-05
**Scope:** New startup protocol added to AGENT_START_HERE.md + session log template + CTO prompt

---

## Objective

Agents were starting with full context of their own work but zero visibility into what happened
downstream after a handoff. This caused gaps like the Y14 issue: J1+J2+J3 all delivered, auth
chain live, but no agent surfaced the missing task order on startup. Fixed by adding Step 2b
(Proactive Downstream Check) to the universal agent startup protocol.

---

## Design

### The problem

An agent marks a task order complete and logs `[0.4.0_DE_ClientPlatform] receive commit abc1234`.
Next session: they start fresh, read their own logs, see "complete." But they have no idea whether
DE actually acted on the commit, found a blocker, or is waiting on something upstream.
The blind spot is everything that happened AFTER the handoff.

### The mechanism

Two-direction check at startup, one hop deep:

1. **Downstream:** Scan most recent log's `## Next Steps` for `[agent_serial]` tags.
   Read each tagged agent's latest log folder. See what they did with the handoff.

2. **Upstream:** Check `<issued_by>` in pending task orders. Read issuing agent's latest log.
   See if scope changed or new dependencies emerged.

**Depth limit: one hop.** The startup cost of reading 2-3 agent log folders is negligible.
Recursing further would be an unbounded org scan — wrong for startup.

### The discovery mechanism

The `[agent_serial]` tags in `## Next Steps` were already in the template but used role names
(`[Dashboard Engineer]`) which can't be resolved to a folder path. Changed to full serials
(`[0.4.0_DE_ClientPlatform]`). Now Step 2b can resolve `org/tier2_senior/{serial}/logs/{latest}/`
mechanically.

### What this catches

- Task order marked complete but downstream agent blocked (you'd see it in their log)
- Handoff commit pushed but receiving agent hasn't started (AMBIGUOUS — surface in orientation)
- Issuing agent changed scope mid-task (you'd see it in their latest log)
- Gate cleared but no task order issued (the Y14 pattern — you'd see "J1+J2+J3 complete" in AE
  and DT logs at startup and immediately recognize Y14 is unblocked with no owner)

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/AGENT_START_HERE.md` | Added Step 2b (Proactive Downstream Check) between Steps 2 and 3 | No — local |
| `org/AGENT_START_HERE.md` | Updated Step 5 orientation summary template to include `Downstream check:` field | No — local |
| `org/AGENT_START_HERE.md` | Updated `## Next Steps` template to require agent serials, not role names | No — local |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | On Launch step 3 rewritten to incorporate Step 2b + DE/DT log reads for active projects | No — local |
| `org/tier1_exec/1.0.0_SA_CTO/logs/2026-03-05/proactive_downstream_check_protocol.md` | This file | No — local |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| One hop only | Startup cost must stay low. Two hops would be an org-wide audit, not a startup check. |
| `[agent_serial]` tags as discovery mechanism | Serials map directly to folder paths. Role names do not. Templates already had tags -- just needed the format tightened. |
| Step 2b not Step 6 | Must happen before adopting the role persona (Step 3) so the agent can contextualize what they read. Reading downstream logs without your role frame active is fine; acting on them requires the frame. |
| Role prompts: update CTO only now | AGENT_START_HERE.md is the canonical authority. Other role prompts will naturally incorporate Step 2b when agents read AGENT_START_HERE.md. A COO task order cascade is optional -- not required for the protocol to take effect. |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

Step 2b is live in AGENT_START_HERE.md. Next Steps template updated. CTO prompt updated.
All agents will encounter Step 2b on their next startup via the mandatory AGENT_START_HERE.md read.
Role prompts for non-CTO agents will be updated organically or via COO cascade.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Commit and push CLOUD** -- carries AGENT_START_HERE.md change,
   project JSON updates (V1VERS closed, YANGV2 Phase 3), REGISTRY.md, session logs.
2. **[2.0.0_SA_COO] Issue Y14 task order to RD** -- auth chain live, no task order exists.
3. **[Andrew] Go/no-go on NNA canonical fix** -- commits 9bfb289b+b4f2d7a7 awaiting decision.
