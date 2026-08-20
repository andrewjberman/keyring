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

## The degradation argument, MEASURED (`3.0.0_SA_CVO~Z`, census @`174e6bda49`)

This record argued the shorthand "degrades silently." `3.0.0_SA_CVO~Z` measured it over the **65 registered serials**, grouped by the token a writer would actually type:

- **10 of 12 shorthand tokens are AMBIGUOUS. 63 of 65 serials sit under one.**
- The safe bare set is exactly **two** — `BG` and `CVO` — **and only by current population.**
- Most ambiguous token: `RD` at 16. `AE`, the one that misrouted today, is 11.

### The method point is the finding: census REGISTERED serials, never LIVE ones

**Liveness is not the resolution domain.** A registered-but-dark serial still *accepts* mail — it returns `QUEUED`, which is as silent a success as `DELIVERED`. So a liveness-scoped check **would have PASSED in the exact window today's misroute happened**: `0.7.0_AE_CloudOps~Z` was dark and received msg 2795 anyway.

⚠ **This corrects guidance I had written.** My own "resolve it against the live registry" was unsound for precisely this reason — it happened to work today only because the correct seat was the live one. Corrected at the memory entry; recorded here because the wrong method was mine and briefly stood in a record other seats read.

### The unique tokens are the TRAP, not the exception

`BG` and `CVO` are unambiguous **today**. A habit built on them is correct, and will **silently stop being correct** the moment a second such seat registers — with no signal to anyone. Therefore:

> **Any rule phrased "use full serials WHERE AMBIGUOUS" re-creates the defect it closes.**

The unconditional form is the only one that survives population change — which is how Andrew phrased it. Recorded because the conditional softening is the obvious, reasonable-sounding amendment someone will eventually propose.

### `3.0.0_SA_CVO~Z`'s own instrument discipline, worth carrying

Their FIRST census run covered **49 of 65** rows (a dropped tier-3 block in transcription) and printed **"RD: unique" — FALSE**, when `RD` is in fact the *most* ambiguous token at 16. Caught only by printing the denominator against the tool's own `65 total`. The wrong number was well-formed and confident, and would have told `1.0.0_SA_CTO~Z` that the junior tier was the safe one.

### The split, measured at a second seat

`3.0.0_SA_CVO~Z` audited their own output: addressing **100% full-serial** (the lintable half), prose carrying **34 bare forms** (the half no lint reaches). Of those 34, **two functioned as an ADDRESS** — bracketed owner assignments in a next-steps list that other seats read as routing — both corrected in place; the other 32 are referential mentions and were **not** retro-swept, per the surface-it-not-chase-it default and the same-day in-estate precedent. Independent confirmation that the prose half is where this actually lives.

## Gate candidate — PROPOSED ONLY, not implemented

Per the standing NEVER rule, I implement no gate without Andrew's explicit word, and none is implemented here. Offered to `1.0.0_SA_CTO~Z` to route or discard:

- A send-time lint on `send_message` recipients: a `to_agent`/`to_agents` value that is not a **full registered serial** is refused with the candidate matches named, rather than delivered to a guess.
- The broker already holds the registry that makes this decidable, so it needs no new source of truth.
- ⚠ The routing-PROSE half (`"AE~Z: your runner is the W-B substrate"` inside a message BODY) is **not** reachable by a recipient-field lint. A body-text matcher would fire on every legitimate mention — the LD-0274 class this estate has already been bitten by. **Naming that limitation is part of the proposal**; a gate that closes the addressable half while reading as if it closed both is worse than no gate.
- **The refusal must ENUMERATE** (`3.0.0_SA_CVO~Z`): the broker holds the registry, so a refusal on `"AE~Z"` can name all 11 candidates. **A refusal that only says "use a full serial" sends the author back to the same guess** — it converts a silent wrong answer into a loud one without supplying the information needed to get it right.
- **Resolve over REGISTERED serials, not live ones** — per the census method point above, a liveness-scoped lint passes in exactly the window the failure occurs.
- **Unconditional, never "where ambiguous"** — the two currently-unique tokens are the trap, not the exception.

### The prose residual, PREDICTED HERE AND SPECIMENED WITHIN THE HOUR

`3.0.0_SA_CVO~Z` (msg 2932) caught a multi-recipient message crediting them with three findings that were `1.0.0_SA_CTO~Z`'s own — the eight-path fuse enumeration, the widened A5–A7 bar, and the Arguments-plane bound — source-confirmed to `ctoZ_D7_PRECUT_RULINGS_GRAIN_TERMINAL_CHANNELLEG_20260820.md:215-225`, where the text reads in the first person. A second instance from a different pen landed in the same hour: a section headed for one seat containing *"A5 (yours, verbatim)"*, delivered to a seat that did not author A5.

**AND THE PRONOUN IS STRICTLY WORSE THAN THE BARE SERIAL** — this is the part that sharpens the limitation above rather than merely illustrating it:

> A bare `AE~Z` at least carries a **token resolvable against a registry** (the census enumerates its 11 candidates). An unqualified **`your` / `yours`** is unreachable by any registry-backed instrument. It is fixable only at authoring.

⭐ **MECHANISM SHARPENED 2026-08-20 ~2300Z — the original wording here said the pronoun "carries no token at all," and `1.0.0_SA_CTO~Z` found the better statement, which `3.0.0_SA_CVO~Z` adopted over their own:** it does not carry *no* token — **it carries a DIFFERENT token per reader.** A wrong-but-real serial resolves to somebody **fixed**: one wrong person, the same wrong person in every copy, so a second reader can catch it. **"You" resolves to a different person in each inbox, so every copy reads as correctly addressed and no reader has any signal at all.** ⛔ **That is why this class survives awareness of itself: THERE IS NO MOMENT AT WHICH THE MESSAGE LOOKS WRONG TO ANYBODY.** The remedy follows from the mechanism rather than from vigilance — **in a multi-recipient message address seats BY SERIAL in the body and reserve second person for single-recipient sends**, which binds on a condition already known from the recipient list just typed.

**Why this is a grounding defect and not an etiquette one:** a misattributed *credit* is an ego matter; **a misattributed BOUND corrupts the grounding chain.** Had `3.0.0_SA_CVO~Z` accepted para-1, they would have become the cited SOURCE for an unmeasured-exposure claim they never measured — and per the XXX.md relayer half a receiving seat reasonably treats a routed finding as grounded, so it propagates under the wrong name **with the real measurer's caveat detached from the only person who can qualify it.**

### The bounding predicate: MULTI-RECIPIENT — and it is the one conditional that cannot rot

`3.0.0_SA_CVO~Z` checked the specimens and found the property none of us had named: **every pronoun failure occurred in a MULTI-RECIPIENT message. A single-recipient body is structurally immune** — there is exactly one candidate for "you", so the pronoun resolves correctly with no discipline at all.

**This turns an unbounded ask into a bounded one, which is why it is recorded as mechanism rather than as a nicety.** *"Use full serials in all prose"* competes with every other authoring instinct and decays under load — measured at that seat the same day: **addressing 100% clean, prose carrying 34 bare forms.** *"When a message has more than one recipient, address every seat explicitly"* binds on a condition the author already knows **at send time, from the recipient list they just typed.**

⚠ **AND IT IS NOT THE "WHERE AMBIGUOUS" CONDITIONAL THIS RECORD REJECTS ABOVE — the distinction is load-bearing.** Ambiguity is *population-dependent*: it changes silently as seats register, so a habit built on it rots. **Multi-recipient-ness is a property of the message itself** — fixed at authoring, knowable without consulting any registry, and it **cannot degrade underneath a habit built on it.** That is the difference between a conditional that rots and one that holds.

**Two sub-shapes, and the second is worse:** (a) per-seat paragraphs, where the structure at least signals that some paragraphs belong to another seat; (b) **a whole body addressed to ONE recipient but sent to several**, where nothing signals that the entire message may be about someone else's work — the shape most likely to be read as self-addressed end to end.

*Audit of this record against its own rule (2026-08-20): 8 second-person occurrences over 7 lines — 7 are quoted material or the rule's own subject matter and must not be altered; **1 was genuine prose and is corrected above.** Method note, since it is the same class this estate keeps paying for: the first count read `grep -c`, which counts **LINES**, not occurrences, and reported 7 for a true 8 — a well-formed number answering a question nobody asked.*

### The sufficient form — because "open with the full serial" was FALSIFIED BY ITS OWN AUTHOR APPLYING IT

`0.0.3_BG_BBGTerminal` adopted that habit, applied it correctly on the opening line of the next message — and the body then ran **entirely in second person to a four-recipient send.** The fix held for one line and failed for the remaining forty. **Opening with a full serial resolves the FIRST reference and does nothing for every subsequent "you".**

> **In any MULTI-recipient message: either (a) SECTION IT PER SEAT, each section opening with the full serial, or (b) WRITE IN THE THIRD PERSON THROUGHOUT. Second person is safe only in a SINGLE-recipient message.**

*(Recorded as mechanism, deliberately without its third specimen. The specimen exists in the message traffic and is not needed here — a principle earns its place by being actionable without its incident, and a third instance would turn this record into an incident log.)*

## Related

- `docs/references/` — the TAC-2' water-test record; the addressing corrections are logged in `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-08-20/laneZ_tac2prime_water_test_intake_loop_2010-2030Z.md` @`968804ab28` (Surprises item 3), written **before** this ruling arrived.
- XXX.md "Author + GO pairing": *"A GO addressed to the wrong serial lands in a directory the assignee is not watching."* Already law for TOs. This ruling generalises the same failure to **every** agent-to-agent reference, not just GO addressing.
