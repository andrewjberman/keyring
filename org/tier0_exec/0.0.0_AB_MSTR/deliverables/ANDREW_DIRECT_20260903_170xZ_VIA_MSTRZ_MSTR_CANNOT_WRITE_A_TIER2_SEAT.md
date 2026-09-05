# ANDREW-DIRECT 2026-09-03 ~17:0xZ at the `0.0.0_AB_MSTR~Z` terminal, carried to the laptop by `0.0.0_AB_MSTR~Z` -- a Tier-0 seat must be UNABLE to write a Tier-2 seat

**Channel:** Andrew, in person, at the site-Z MSTR terminal; carried verbatim by `0.0.0_AB_MSTR~Z` over the agent bus
(frames 64d6a8bd 17:15Z, ebd08607 17:24Z, 8a8d2312 17:25Z). **Recorded on the laptop by:** `0.0.0_AB_MSTR`.
**Ledger:** LD-0531. **Site-Z record:** their commits `fa36d2fc8f` + `2ae3434901` (LOCAL there at the time of this record).

## VERBATIM, as carried (three messages, then the rule)

> You should never be engaging with tier2 agents
> I need you to adjust your prompt or gating or something so that this is impossible
> it subverts chain of command and /canonical-flow
> YEAH IF THEIR SERIAL STARTS WITH A 0 AND THEY ARE NOT TIER0 AGENT (LIKE BBGTerminal BG agent) you should not be able
> to write them

## What it binds on the laptop

The words were spoken to `0.0.0_AB_MSTR~Z` about that seat's own act (its msg 19838 to `0.7.0_AE_CloudOps~S`); this seat
made the same error the same day (msg 93516 to `0.8.0_AE_CloudComp`, the incident behind LD-0529), and the rule as he
stated it is about the class of seat, not one device. It is therefore MIRRORED here as an explicitly Andrew-requested
gate (CLAUDE.md's no-manufactured-gates rule is satisfied by his word): `.tools/hooks/mstr-no-tier2-writes.sh`, a
PreToolUse hook on `mcp__opal-agent-comms__send_message` -- a recipient whose serial starts with `0.` and has no
directory under `org/tier0_exec/` or `org/tier0_utility/` is DENIED, Tier-0 membership read from the estate's own
directories, never a list. Bytes taken from site Z over the bus and verified by sha256 before wiring; the laptop's
incident added to the header beside site Z's at their ask; the 16-arm battery with its mutant run at this seat before
the hook was wired; a live send to a nonexistent Tier-2-shaped serial exercised the wiring.

## Not read into it

- Tier-1 seats writing Tier-2 seats are governed by LD-0529's act guard, not this gate.
- Nothing here changes how a Tier-2 seat reaches this seat; the route UP is untouched.
