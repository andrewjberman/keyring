# TCKT_VNEXT decomposition -- ROUND 14, 2026-10-12, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DELL2_RELAUNCH_THREE_ASKS_READ_AND_RULED_20261012.md`
section 7 AMENDED @cccdb9ed92 (msg 6639): ONE test ticket in tenant **49financial** (not cottonwood: the existing synthetic filer
lists 49financial only), titled as a test, filed BEFORE `2.0.0_SA_COO~Y2` files its request, its id given to `2.0.0_SA_COO~Y2` and
`2.0.0_SA_COO~T2`. Round 12's cottonwood ticket `TCK-20261012-13cd3a1d` stays open as a test ticket; closing it is Andrew's (call
fbb1). Round 13 (the CTO's analysis @4c33a0d106) cut nothing. No PRD addendum; PRD v0.4 with its ratified-text half signed @1fc5ceaef5. FWD-1 is NOT REALIZED and the vendor path stays
stopped; this is not a thread round. This cell serves NFRA_TRNSPT TR-dp-24 (the drafter's first live post), which that project's
issuer holds; nothing in TCKT_VNEXT's endpoint is graded by it.

| cell | builds | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `R14-tk-2` | ONE ticket through the existing create route as the commentary service principal: tenant 49financial, title beginning `[TEST TCKT_VNEXT R12]`, a synthetic attachment pointer, no draft and no request id. A result file with its id. Nothing else is written | support to NFRA_TRNSPT TR-dp-24 (no FWD of this project) | cut | applier seat | SERVED | -- | none |
| carried | everything in round 10's carried row, unchanged; the request side of the pair is `2.0.0_SA_COO~Y2`'s | -- | each on its named event | -- | -- | -- | -- |

**Chains (M = 1):** {`R14-tk-2`}. **Fan-out: 0 workers; one applier order.** The act needs a credential read from a secret, which a
worker subagent does not hold.

## Rule 24 record

- **MECE over the ruling's section 7.** Domain: its conditions. By subtraction: synthetic file, write set listed, no post, no
  delete, outside-model call under C-KIMI are each either this cell's bounds or the request side (`2.0.0_SA_COO~Y2`). The
  outside-model call and the draft post are NOT this cell: it sends neither.
- **Same grain:** one ticket. **One axis:** the ticket exists, titled as a test, in the named tenant.
- **A name this cell does not choose:** the ticket id is issued by the service and is read from the 201; it is never typed.

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE (no schedule). comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; the secret read is a grant
this box's agent user already holds, row D2-S8/S9, accepted by the CTO). comp-adversary: the control is the independent re-read in
the check, which fetches the ticket by id and compares tenant, type, status, creator and title prefix.

Dry-run at the base (box/dell2, 2026-10-12 ~18:3x ET): `r14_tk2_ticket.py` FAIL (no result file), as expected.
