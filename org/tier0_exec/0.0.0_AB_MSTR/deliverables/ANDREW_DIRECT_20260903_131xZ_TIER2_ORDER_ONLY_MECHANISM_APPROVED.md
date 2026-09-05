# ANDREW-DIRECT 2026-09-03 ~13:1xZ-13:2xZ -- a Tier-2 seat investigated and put an open call to Andrew; "Mechanism works"

**Channel:** Andrew, in person, at the `0.0.0_AB_MSTR` terminal. **Recorded by:** `0.0.0_AB_MSTR`. **Ledger:** LD-0529.

## VERBATIM, entire, in order

First, on seeing a `0.8.0_AE_CloudComp` message at a terminal that ended with an (a)/(b)/(c) question to him about the
ms-heat lifecycle rule:

> THere are several things wrong here. First, why the fuck is a tier 2 agent "Investigating"? Not their fucking job.
> THeir job is do task that was asked of them. Second, no "open calls" from tier2 agents anymore. That should be
> impossible, they should be on their orders and running that up to mgmt. How did this happen and how do we prevent
> this?

Then, answering this seat's three prevention items (1 law: a Tier-2 seat acts only on an order in its own task-orders
home and routes an actless ask up to its issuer; 2 mechanism: the broker refuses a Tier-0/Tier-1 send to a Tier-2 serial
that carries an act without citing an order assigned to that recipient; 3 the `/open-calls` skill refuses at its first
step for a Tier-2 serial):

> Mechanism works

## What it binds

- **Item 2 is APPROVED and is the act:** the broker send guard is generalised so that a send from a Tier-0 or Tier-1
  seat to a Tier-2 serial whose body carries an act is REFUSED unless it cites a task order assigned to that recipient
  (the issuer's own dispatch of that order passes; an ack or a pure information line with no act passes). Builder:
  `1.0.0_SA_CTO` (the guard is `org/mcp/cvo_send_guard.py`'s surface, generalised). Falsifier: the three messages that
  produced this incident (93516, 93527, 93638) must REFUSE under the guard; a COO dispatch citing its own order and a
  worker's ack must PASS.
- **Items 1 and 3 are NOT ruled on** by these words; they stay open at Andrew as proposals. The phrase "no open calls
  from tier2 agents anymore ... should be impossible" is his intent; item 2 is the mechanism he chose for it.

## How it happened (measured, the record for the falsifier)

Three messages from above carried acts and none was a task order: `0.0.0_AB_MSTR` 93516 (11:0xZ) relayed site Z's
shared-infra finding to `0.8.0_AE_CloudComp` directly as "owner class"; `1.0.0_SA_CTO` 93527 told the same seat to open
a change-management entry now; `1.0.0_SA_CTO` 93638 told it to write the rebuildability statement and then apply. No
face, no issuer, no acceptance criteria. The worker verified the premise and asked Andrew in the `/open-calls` form. The
L6 neck (`.tools/to-pipeline-gate.py`) was bypassed by MCP; the first link is this seat's.

## Not read into it

- No change to the item itself: `2.0.0_SA_COO` cuts it as an L6 order to `0.8.0_AE_CloudComp` with his 13:0xZ ruling as
  the acceptance (msg 93650).
- The completion-condition call and the standing `/drive` for the COO are separate calls, still open at Andrew.
