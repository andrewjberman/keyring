# Andrew-direct 2026-10-13 ~22:3xZ (relayed by 0.0.0_AB_MSTR msg 108966) -- COMM_ASSIST folds in the unstamped sender LDO-001 and job J290

## VERBATIM (as relayed)

> "the COMM_ASSIST pipeline sending a bid to build out the email agent response ... Clearly there is an issue with the sending
> channel in that it's not registered, and it probably makes sense to handle this in the same workstream as COO~CA was handling the
> same issue for 'Muse' the 'ms' tailnet ai sender. the COO~CA needs to fold in this fix for unstamped sending as well as get that
> email channel sorted out."

MSTR's facts: the agentbus warns `unstamped sender=LDO-001`. Job J290 (22:27Z) asks for the reply mechanism for received mail; the
first mail is Keith Wagner on the TIFIN call. MSTR's bid went at 22:37Z, late, and LOST, so J290 is unowned.

## Applied

1. **The register (this seat's part):** `org/devices/DEVICES.json` `senders` gains `ldo-001`, the name the LDO-001 assistant
   stamps as `from_tailnet`. The consumers then hold it (`lib/devices.py held_tailnet_names`). It is in no box list.
2. **`2.0.0_SA_COO~CA` folds both into COMM_ASSIST** (round-16 analysis ADDENDUM):
   - the stamp: the LDO-001 send path sets `from_tailnet=ldo-001`. Done when a bid it sends is delivered with no
     `unstamped sender` WARN, and a message stamped with an unheld name is still refused.
   - J290: the reply mechanism for received mail, owned by COMM_ASSIST (FWD-4, the mail branch). The first case is the Keith
     Wagner mail.
