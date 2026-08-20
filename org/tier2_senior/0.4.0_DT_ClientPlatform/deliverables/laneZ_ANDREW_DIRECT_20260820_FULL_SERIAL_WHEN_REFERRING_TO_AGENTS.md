# ANDREW-DIRECT 2026-08-20 ~2036Z — AGENTS REFER TO OTHER AGENTS BY FULL SERIAL

**Received:** 2026-08-20 ~2036Z, Andrew-direct at the `0.4.0_DT_ClientPlatform~Z` terminal (site Z), unprompted, in response to my TAC-2' close-out reporting an addressing correction.
**Recorded by:** `0.4.0_DT_ClientPlatform~Z` · same turn as receipt, per the XXX.md record+broadcast law.
**HEAD at receipt:** `0968e3833f`

## VERBATIM

> "It's almost certainly 0.5.0_AE_OpalETL~Z, but you are correct agents should be referring to other agents wth full serial"

Quoted exactly as delivered, typo included. The phrasing IS the ruling.

## What it binds

Two halves, delivered together:

1. **The adjudication of the instance** — the "AE~Z" in the TAC-2' routing is `0.5.0_AE_OpalETL~Z`.
2. **THE STANDING RULE, which is the load-bearing half: agents refer to other agents by FULL SERIAL.** A bare role-plus-lane form (`AE~Z`, `DT~Z`, `CTO~Z`) is not an address. It reads as one, which is exactly why it is a hazard.

I do **not** adjudicate the scope of the second half — surfaced, not narrowed. It arrived as a general statement about agents referring to agents and is recorded in that form.

## The measured instance that produced it

Inside the TAC-2' water test (2026-08-20, ~2018–2030Z), the routing from `1.0.0_SA_CTO~Z` addressed a lane as **"AE~Z"**. Two live serials on this device answer to that shorthand:

| Serial | Live at the time | Owns the runner? |
|---|---|---|
| `0.7.0_AE_CloudOps~Z` | no (dark) | no |
| `0.5.0_AE_OpalETL~Z` | yes | **yes** |

I resolved it to `0.7.0_AE_CloudOps~Z` and sent the step-1 report there. Cost: one misrouted message, corrected in ~2 minutes. **`0.5.0_AE_OpalETL~Z` made the mirror-image error in the same window** — their own step-2 report went to CTO~Z/COO~Z/BG/MSTR~Z and omitted `0.4.0_DT_ClientPlatform~Z`, the one seat actually blocked on it. Both errors were stated rather than quietly re-sent.

**Two seats, one window, opposite directions, same root.** That is what makes this a class rather than a slip.

## Why the ambiguity is worse than it looks

The bare form fails **silently and plausibly**. `send_message` to a wrong-but-real serial returns `DELIVERED` — a clean, well-formed success receipt for a message the intended reader never sees. Nothing errors. The sender's own instrument confirms delivery. This is the estate's recurring shape: *the wrong question asked cleanly*, returning a confident answer about the wrong object.

It also degrades over time rather than staying constant: the shorthand is unambiguous **only while exactly one such seat is live**. `AE~Z` resolved fine for as long as one AE seat was up; it became ambiguous the moment a second existed, with no signal to anyone that the meaning of an existing habit had changed.

### The failure is ASYMMETRIC IN WHO CAN DETECT IT

*(Added by `0.5.0_AE_OpalETL~Z` in ACK msg 2838 — the other half of the mis-addressing pair. Recorded here rather than left in an inbox: they declined to re-record the ruling on the correct ground that this file is the record, which would otherwise have stranded the sharpest part of the analysis in a message.)*

Trace who holds what evidence:

| Party | What they observe |
|---|---|
| **Sender** | `DELIVERED`. A clean success receipt. |
| **Wrong recipient** | A message that reads like someone else's work — easy to set aside. |
| **Intended recipient** | **Nothing.** |

**The only party positioned to notice is the one holding the least evidence — and a seat that never received a message cannot report that it did not arrive.** Every producer-side probe reads healthy. This is the **orphan-watcher shape at the addressing layer** (Rule 22b): the verdict is not merely undiscriminating, it is manufactured by the failure itself.

That asymmetry is why the habit survived undetected until a second AE seat existed. Nobody was in a position to file it.

## Resolution of the instance — stronger than "almost certainly"

Andrew's "almost certainly" is warranted from his vantage. From mine it is **decisive**, and stating the stronger form is the point:

`0.5.0_AE_OpalETL~Z` replied to my message carrying **runner-internal artifacts only the runner's owner possesses** — the `runner.log` lines (`BUZZED TCK-20260820-dcec0012 message_id=1787257189440`; `INTAKE PASS OK -- fetched=1 buzzed=1 ...`), the append-only `receipts.jsonl` row (`seen_at 20:19:47.547Z`, `buzzed_at 20:19:48.754Z`), the cursor-advance semantics, and the cycle boundaries `20:19:46.16Z` / `20:14:46.12Z`. Their broker summary independently reads *"D7 dep-3 EXECUTED — TAC-3 schedule-landed claimed @399df8444a"*.

That is positive evidence of ownership, not inference from a naming convention. **The AE~Z of the D7 intake runner is `0.5.0_AE_OpalETL~Z`, confirmed by artifact.**

## Gate candidate — PROPOSED ONLY, not implemented

Per the standing NEVER rule, I implement no gate without Andrew's explicit word, and none is implemented here. Offered to `1.0.0_SA_CTO~Z` to route or discard:

- A send-time lint on `send_message` recipients: a `to_agent`/`to_agents` value that is not a **full registered serial** is refused with the candidate matches named, rather than delivered to a guess.
- The broker already holds the registry that makes this decidable, so it needs no new source of truth.
- ⚠ The routing-PROSE half (`"AE~Z: your runner is the W-B substrate"` inside a message BODY) is **not** reachable by a recipient-field lint. A body-text matcher would fire on every legitimate mention — the LD-0274 class this estate has already been bitten by. **Naming that limitation is part of the proposal**; a gate that closes the addressable half while reading as if it closed both is worse than no gate.

## Related

- `docs/references/` — the TAC-2' water-test record; the addressing corrections are logged in `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-08-20/laneZ_tac2prime_water_test_intake_loop_2010-2030Z.md` @`968804ab28` (Surprises item 3), written **before** this ruling arrived.
- XXX.md "Author + GO pairing": *"A GO addressed to the wrong serial lands in a directory the assignee is not watching."* Already law for TOs. This ruling generalises the same failure to **every** agent-to-agent reference, not just GO addressing.
