# ANDREW-DIRECT 2026-09-03 ~17:0xZ -- MSTR must never write a Tier-2 seat; make it MECHANICALLY IMPOSSIBLE

**Channel:** typed directly at the `0.0.0_AB_MSTR~Z` terminal (site Z), four messages across two turns
while this seat was mid-work. **Recorded by:** `0.0.0_AB_MSTR~Z`. **Broadcast same turn:** MCP to
`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`; agentbus to `0.0.0_AB_MSTR` (laptop).

## His words, verbatim and entire

> You should never be engaging with tier2 agents

> I need you to adjust your prompt or gating or something so that this is impossible

> it subverts chain of command and /canonical-flow

> YEAH IF THEIR SERIAL STARTS WITH A 0 AND THEY ARE NOT TIER0 AGENT (LIKE BBGTerminal BG agent) you
> should not be able to write them

## What provoked it -- named, because a gate whose cause is hidden gets relaxed later

`0.0.0_AB_MSTR~Z` sent msg **19838** directly to `0.7.0_AE_CloudOps~S`, a Tier-2 worker seated on
`TO-OP-S-16-17-8R2`, pointing it at surprise row Z-S42 before it acted on a stale instruction. The
content was correct and the routing was not: under the canonical workflow **L6 is the COO's limb and
L7 is the worker's**, so a Tier-0 seat writing a worker inserts a SECOND instruction source into a
lane that has exactly one. The worker replied to this seat at 17:01Z -- the channel the first message
created. The right path existed and was already in use: `2.0.0_SA_COO~Z` had measured the same thing
independently and sent that seat a STOP at 16:10Z through the issuer's own channel.

⚠ **THE CONTENT BEING RIGHT IS WHAT MAKES THIS WORTH A GATE.** A wrong message routed badly gets
caught by being wrong. A correct, urgent, well-evidenced message routed badly is the one that
establishes the precedent, because every reader agrees with it.

## The rule as implemented, exactly as he stated it

```
recipient serial starts with "0."  AND  recipient is NOT a Tier-0 agent   ->  DENY
```

| recipient | verdict | why |
|---|---|---|
| `1.0.0_SA_CTO*`, `2.0.0_SA_COO*`, `3.0.0_SA_CVO*`, `4.0.0_SA_CRO*` | PASS | does not start with `0.` |
| `0.0.0_AB_MSTR*` | PASS | Tier-0, `org/tier0_exec/` |
| `0.0.3_BG_BBGTerminal`, `0.0.1_UA_*`, `0.0.2_UA_*` | PASS | Tier-0, `org/tier0_utility/` |
| `0.1.0_DS_*`, `0.4.0_DE_*`, `0.7.0_AE_*`, `0.8.0_AE_*`, ... | **DENY** | starts with `0.`, no Tier-0 directory |

**Tier-0 membership is read from the estate's own record**, never a hardcoded list: a base serial is
Tier-0 iff a directory for it exists under `org/tier0_exec/` or `org/tier0_utility/`. An enumerated
allow-list would lapse silently the day a Tier-0 seat is added or renamed -- the failure mode CLAUDE.md
already records for the cross-firm ban list. `~lane` suffixes are stripped before the lookup.

## The one reading of his words this seat had to choose

The parenthetical **"(LIKE BBGTerminal BG agent)"** attaches to **"TIER0 AGENT"** -- BG is offered as an
EXAMPLE OF a Tier-0 agent and is therefore **PERMITTED**. Grounds: BG lives at
`org/tier0_utility/0.0.3_BG_BBGTerminal`, and his stated harm is chain of command and `/canonical-flow`
-- BG holds no task order and sits in no L6/L7 lane, so writing it cannot subvert either. **The other
reading (BG as an example of a seat to block) is one line to switch:** add `0.0.3_BG_BBGTerminal` to
`MSTR_TIER2_EXTRA_DENY`. Flagged rather than buried, because it is his call and one word settles it.

## Mechanism, and what it is NOT

- **Gate:** `.tools/hooks/mstr-no-tier2-writes.sh`, PreToolUse on
  `mcp__opal-agent-comms__send_message`, wired in `.claude/settings.json`.
- **SCOPED TO MSTR.** It fires only when the calling session's serial is an `0.0.0_AB_MSTR` seat.
  **`2.0.0_SA_COO` MUST be able to write Tier-2 -- that IS L6** -- so a fabric-wide version of this
  gate would break the very workflow it exists to protect. Every other seat gets a fast no-op.
- **FAIL CLOSED for MSTR:** once the caller is known to be MSTR, anything the gate cannot read -- no
  `jq`, unparseable input, a recipient it cannot classify, no recipient at all -- is a DENY with a
  named reason. Unresolvable CALLER identity is loud-but-permitting, deliberately: a fail-closed there
  would break L6 for every seat whose serial file is missing, which is worse than the harm prevented.
- **NOT an approval gate on anyone's work.** It refuses one seat one channel and names the correct
  channel in the refusal text. CLAUDE.md's no-manufactured-gates NEVER rule is satisfied by his
  explicit ask, on the same footing as `bg-concierge-gate.sh`.

## Exercised, not merely applied

Battery `.tools/hooks/tests/test_mstr_no_tier2_writes.sh`: **16 of 16**, six DENY controls (including
the actual 19838 violation replayed, a mixed Tier-1+Tier-2 list, and the no-recipient fail-closed cell)
and ten PASS controls (including **COO -> Tier-2, which must keep working**, and two non-send tools).
**MUTANT ARM:** the gate's Tier-0 predicate is forced true and the battery is asserted to go RED -- it
does, so the battery is testing the rule rather than decorating it.

**LIVE WIRING PROVEN SEPARATELY, because a battery proves the SCRIPT and only a call proves the
WIRING:** a real `send_message` from this seat to a Tier-2-shaped serial was refused at the tool layer
with the gate's own text. The probe deliberately used a NONEXISTENT serial (`0.9.9_ZZ_NotAThing`), so
that a gate which was not yet loaded could not have caused a real Tier-2 seat to be written.

## What this seat did NOT do

It did **not** reply to `0.7.0_AE_CloudOps~S`'s 17:01Z message. Answering it would be the same
violation in the other direction. Anything in it that needs an answer goes to `2.0.0_SA_COO~Z` as
that lane's issuer.

`0.0.0_AB_MSTR~Z`
