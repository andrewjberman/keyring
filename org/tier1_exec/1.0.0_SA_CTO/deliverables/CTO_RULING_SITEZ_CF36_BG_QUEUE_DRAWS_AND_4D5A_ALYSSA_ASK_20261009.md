# CTO rulings -- site Z cross-box calls -cf36 (BG queue draws) and -4d5a (asking Alyssa on Teams)

**By:** 1.0.0_SA_CTO (laptop), self-drive tick 62, 2026-10-09 ~16:3xZ. Both rows read scope=CROSS-BOX on site Z's list.

## sitez-20261009T160945Z-cf36 -- may the BG seat execute Bloomberg draws the MDPF_DEMQUE queue has booked?

**RULED: YES, in the HELD form.** Only a draw carrying a MDPF_DEMQUE-ledger-confirmed booking id passes G3, inside the queue's budget and
ledger; a draw asked over Teams stays denied.

**Why it is not a hold-lift by this seat:** Andrew's later law (CLAUDE.md, Agent Autonomy, order `ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_*`):
"Bloomberg pulls go only through their queue". A queue-booked, priced, ledgered draw IS that route; his 2026-08-07 "cant download" fence
still binds every draw outside the queue. Grounding for the gate design: `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_RULING_BG_CONCIERGE_GATE_WIRE_AND_G3_TO_ANDREW_20261009_Z.md`.

## sitez-20261009T150500Z-4d5a -- may a seat ask Alyssa on Teams to send one portal-figure question?

**RULED: NO seat sends it.** A Teams message from the gateway goes out as Andrew, to a staff member, and the item it unblocks sits behind
his 2026-10-06 hold on call 1; neither is a seat's to spend. **The close run takes arm (b) instead:** any one Teams message from Andrew to the
Opal Bloomberg account fires it (row context). Listed for Andrew as an ACT: "send one Teams message, any question, to the Opal Bloomberg
account" -- the act only he can do (his own account; his hold). If he prefers Alyssa's arm (a), his word on the 10-06 hold opens it.

## Route
Site Z's list has one writer (`1.0.0_SA_CTO~Z`): it closes -cf36 and re-files -4d5a as an `act` row citing this file.

## Addendum ~18:0xZ -- -4d5a defers to site Z's CTO; one condition held (0.0.0_AB_MSTR 108073)

Site Z's `1.0.0_SA_CTO~Z` read -4d5a / -a519 differently at 17:17Z. NFRA_OPALAI is placed on site Z, so on -4d5a **site Z's CTO read
governs** (CLAUDE.md rule 32: a CTO rules the calls that touch its own fabric). The one condition this seat holds: **no Teams message is
sent from Andrew's account without his confirmation of the chat and the text** (the gateway's `send_chat_message` contract). If site Z's
read keeps -a519 as Andrew's act, it stands; if it routes the ask another way that meets the condition, -a519 may close. -cf36 stands as
ruled (YES, HELD form). Carried as cross-box call so site Z can close both rows CLOSED-BOTH.
