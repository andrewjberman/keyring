# ANDREW-DIRECT 2026-08-30 ~22:00Z — /open-calls, all four recommendations approved

**Channel:** Andrew, typed at the `0.0.0_AB_MSTR` terminal (laptop), answering this seat's `/open-calls`
card set. **Recorded by:** `0.0.0_AB_MSTR`, same turn, VERBATIM.

## VERBATIM

> all recs approved

## What he approved, quoted from the cards he answered — so the scope is exact and not reconstructed

His three words carry exactly the four recommendations as they were written to him, and nothing wider:

**CALL 1 (BLOCKING) — ETF Positioning promote, condition (ii).** REC as put to him: *"Waive it as written
and promote."* Grounds on the card: the served `sub_asset_class` VALUES are GICS sector names and
`industry_group` is the GICS industry group — both fields are GICS at different levels, so *"GICS replaced
by sub-categories"* is a false dichotomy, and satisfying it literally would require overturning the standing
ruling that `industry_group` is parallel to `sub_asset_class`, never a replacement.
→ **RULED: condition (ii) is WAIVED AS WRITTEN and the Positioning promote proceeds.**
⛔ Condition (i) — *"the daily Bloomberg pipeline COMPLETE with the FULL data structure for ALL ETFs"* — was
NOT the subject of this card and is NOT waived by it. Nobody may read this as clearing (i).

**CALL 2 (CARRIED) — Site Z's spent account.** REC: *"Restore when convenient, not urgently. Nothing on
this device depends on it, nothing is lost."* → **RULED: restore at his convenience; no urgency, no
escalation, and no seat waits on it as a blocker.**

**CALL 3 (CARRIED) — leg 2 of the cross-site sync.** REC: *"Yes, once Site Z is back."*
→ **RULED: leg 2 is APPROVED, to run when Site Z is reachable.** The word is given now; the act is
event-gated on Call 2, and this seat executes it — no further word is needed at that time.

**CALL 4 (CARRIED) — a second reviewer for the Y fabric.** REC: *"Leave it as staffed."*
→ **RULED: the Y fabric stays at its current shape** (two producers, one reviewer). No spawn follows. The
named tell stands: if that reviewer's verdict latency rises, `1.0.0_SA_CTO~Y` reports it rather than
absorbing it, and the question re-opens on that report — not on a timer and not on this seat's initiative.

## Execution, and who does what

| Ruling | Owner | State |
|---|---|---|
| (ii) waived; promote proceeds | Site Z (`1.0.0_SA_CTO~Z` / `2.0.0_SA_COO~Z`, D4 is SITEZ-placed) | **filed on the git trunk**; unexecutable until that account has usage |
| Restore the Site Z account | Andrew | his act |
| Leg 2 approved | `0.0.0_AB_MSTR` | executes when Site Z is reachable; no further word needed |
| Y fabric stays as staffed | `0.0.0_AB_MSTR` (holds the spawn primitive) | nothing to do; `1.0.0_SA_CTO~Y` told |

⛔ **THE PROMOTE RULING CANNOT BE DELIVERED OVER THE BUS.** Site Z's SQS consumer drains and destroys
messages while no model can read them (LD-0347 A1), so this ruling is filed as a **trunk envelope** where it
survives the outage and is read whenever that site regains usage. A bus send would have looked delivered and
lost his word.

## Dispatch — MEASURED, written after reading the send results rather than from intent

- **Trunk envelope `amb-b-0014`** (RULING, `requires_ack`), FILED at
  `org/mcp/agentbus-trunk/messages/20260830T220509Z__0.0.0_AB_MSTR__0.0.0_AB_MSTR~Z__RULING__amb-b-0014.json`
  — carries Andrew's three words verbatim, both site-Z rulings with their grounds, the explicit
  condition-(i) guard, the owner statement (D4 is SITEZ-placed, so the promote is `1.0.0_SA_CTO~Z`'s and
  `2.0.0_SA_COO~Z`'s act, not base's), and a pointer that `amb-b-0013` is still unacked and unexecuted.
  Ledger for the channel choice: **LD-0347 AMENDMENT 2**, written this turn.
- **MCP broadcast, same turn, 9 of 9 DELIVERED / 0 QUEUED / 0 REFUSED** (denominator 9 — the live roster
  is 10 seats and the tenth is this one):
  `1.0.0_SA_CTO~X` 89379 · `1.0.0_SA_CTO~Y` 89380 · `2.0.0_SA_COO~X` 89381 · `3.0.0_SA_CVO~X` 89382 ·
  `4.0.0_SA_CRO~X` 89383 · `4.0.0_SA_CRO~Y` 89384 · `0.7.0_AE_CloudOps~X` 89385 · `1.1.0_SA_KJ~Y` 89386 ·
  `1.2.0_SA_A0~Y` 89387. Each id is the tool's own per-recipient line, not a batch assertion.
  ⚠ DELIVERED here is the broker's word about its own filesystem+broker+channel write — **it is a SENT
  clock, not a READ one**; only a seat's own ack moves it to READ, and none is required (the broadcast
  says no reply needed).
- **`1.0.0_SA_CTO~Y` is answered inside that broadcast** on the certifier-capacity option it surfaced and
  did not request: the fabric stays as staffed, and the re-open tell it named stands as it wrote it.
- **Nothing here unblocks a live seat.** All four rulings land on site Z, on Andrew, or on this seat —
  which is why the broadcast closes with "keep working."

## ⛔ SCOPE LIMIT — what these three words DID NOT answer (recorded 22:0xZ, on `1.0.0_SA_CTO~X`'s ack 89390)

`1.0.0_SA_CTO~X` read the broadcast and, seeking no reply, marked a boundary I am adopting into this
record because it is right and because the risk it names is real:

> *"'all recs approved' is exactly the shape of a word that gets read wider than it was said"*

**HIS WORDS ANSWERED THIS SEAT'S CARD SET AND ONLY THIS SEAT'S CARD SET.** `/open-calls` is per-lane by
design — each seat renders from its own vantage, and Andrew runs it wherever he wants the view. He ran it
here. **Cards rendered at ANOTHER terminal are not in the denominator of these three words**, and two are
open right now:

| Open elsewhere, NOT closed by this ruling | Lane | Project |
|---|---|---|
| Explicit PRD ratification (carried since 2026-08-27; his 02:03Z "approved" amended sec 10.3(f) and left ratification **explicitly not decided**) | `1.0.0_SA_CTO~X` | `NFRA_C3MATERIALIZE` |
| Evidence-retention policy for the L3 decomposition runs | `1.0.0_SA_CTO~X` | `NFRA_C3MATERIALIZE` |

⛔ **A LATER RECONCILIATION OF "WHAT IS OPEN AT ANDREW" MUST NOT MARK THOSE TWO CLOSED ON THE STRENGTH OF
THIS ENTRY.** They were never put to him in this card set. The same discipline binds in both directions and
that lane applied it to itself in the same message: it read no fifth ruling into the four, and neither do I.
This is the standing carrier law — **verbatim scope; relay, never adjudicate wider OR narrower** — applied
to a word's REACH rather than its content, which is the limb that fails quietly.
