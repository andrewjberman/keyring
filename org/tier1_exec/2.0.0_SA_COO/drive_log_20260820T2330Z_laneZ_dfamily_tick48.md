# /drive tick 48 — 2.0.0_SA_COO~Z lane Z — 23:29Z→23:35Z

**Cycle result: completed the status-field census across all six W-lane TOs — 4 of 6 were stale — and
found a cross-lane hazard neither TO's owner could see from inside their own lane.**

## Movement — short-window artifact again, no conviction drawn

Tick fired ~40s after the prior marker, so `since_tick=0` across six seats is a **window artifact**,
not a signal. Ages: 0.0–3.4m for six seats; `0.4.0_DT_ClientPlatform~Z` at **23.3m** and
**CLOSED-BY-DECLARATION** (0 TOs, nothing held, by their own close).

⚠ **Pre-empting a false positive next tick:** DT~Z will cross the 30m STALE threshold shortly. **That
will be a classifier artifact, not a stall** — the seat declared closure with nothing outstanding.
Recorded here so a future tick does not open a nudge ladder on a seat that finished its work and said
so.

Denominator: 23,521 telemetry rows.

## Discharging last tick's named candidates — both stale, in DIFFERENT ways

| TO | status field | verdict |
|---|---|---|
| **W-A** | *"pending — queued behind dep-3"* | **STALE** (fixed tick 47) |
| **W-B** | *"ACTIVATES when TAC-3 reads schedule landed"* | **STALE — trigger MET *and* MOOT** |
| **W-C** | capacity-blocked / two-link chain | **STALE** (fixed tick 47) |
| **W-D** | *"activates after W-A … once a nudge path exists"* | **STALE — both conditions met-or-nearly** |
| **W-E** | *"DESIGN GATE FIRST at CTO~Z"* | **OPEN BY DESIGN** — correctly awaiting a gate |
| **W-F** | carries Andrew's rulings + the gate rulings | ✅ **CURRENT — no correction needed** |

**DENOMINATOR: 6 W-lane TOs, all six read at source this session. 4 stale, 1 current, 1 open-by-design.**

**W-B** — TAC-3 *did* read schedule-landed (dep-3 ACCEPTED 19:59:41Z @399df8444a), so the trigger
fired ~3.5h ago **and is now moot**: the @3388 numbers ruling drops the stream entirely. **A field
promising activation for a DELETED TRANSPORT** — the same class that cost two ticks on W-A. The
re-cut block at the top already said so; **the status field contradicted it.**

**W-D** — both conditions met-or-nearly and **neither is what binds.** Condition 2 (*"once a nudge
path exists"*) is **MET** — the scheduled backstop is live and exercised straight through the
23:15:55Z credential boundary. **And this TO called it correctly in advance** — *"W-B stream not
required"* — which is precisely why dropping W-B's transport costs this lane nothing. Condition 1
(*"after W-A"*) is **build-side met, apply-side pending**, and the shared-file collision it guards is
a build-time concern, so **name which one you mean** before treating it as clear. **What actually
binds is the two holds:** limb (1) on the Teams prohibition, limb (2) at Andrew.

>> ✅ **W-F IS THE COUNTER-EXAMPLE AND IT IS WORTH MORE THAN THE FOUR CORRECTIONS.** Its field was
maintained **as the rulings landed** — Andrew's ~20:50Z forks, the @c9459dfa2f gate rulings, the
21:39Z channel exclusion — **which is exactly why it did not rot like the other three.** *Recording a
verification that found nothing, because a verification that finds nothing is still a verification.*

## The cross-lane hazard

**W-F `<status>`:** *"DO NOT BUILD THE DELIVERY LEG until CTO~Z names the surface it DOES use (**the
detect/deliver seam points at the email DL**)"* — and, separately, *"WHICH THREAD = INTERNAL by
default."*

**W-E `:37`:** *"The DL's **audience**"* — listed as an **OPEN design question.**
**W-E `:142`:** the DL must be *"**provably NOT** the internal audit trail / routing / internal notes."*

>> ⛔ **W-F IS INTERNAL BY RULING; THE DL IS CONSTRAINED TO BE PROVABLY-NOT-INTERNAL, WITH ITS
AUDIENCE UNDETERMINED.** Routing W-F's escalation onto the DL would put an *"Opal was late"* message
onto a surface whose defining constraint is that it does not carry internal material — and telling
the client we were late is the exact product decision carded to Andrew.

**THE HAZARD IS THE ADJACENCY, NOT THE SENTENCE.** The parenthetical is a *hint about the seam* and
was plainly meant as one. But **it is the only surface named anywhere in that field**, the channel is
already excluded by ruling, and a builder reading *"do not build until the surface is named"*
followed immediately by a named surface **has been given a direction whether or not one was
intended.**

⚠ **NOT CLAIMED:** I have **not** established the DL is client-facing — **its audience is open, and
that is the point.** If it resolves to internal-or-mixed, the collision disappears. What is
established is that **the collision is unresolvable until that audience is ruled, so W-F's delivery
leg is gated on a W-E decision, and neither TO says so.** Routed to `1.0.0_SA_CTO~Z`, who owns both
gates. **I named no surface.**

## Carry-forward

- **W-A: apply leg only** (laptop, WA-6 grant first, then deployed WA-1/2/8)
- **W-C: one link back** (W-A apply), then capacity — still not binding
- **W-D: the two holds bind, not the sequencing**
- **W-F: delivery surface gated on W-E's audience ruling** — newly surfaced, at CTO~Z
- **W-E: design gate at CTO~Z**, correctly open
- Item A (five `_meta` marks) build → both gateway changes on one boot test
- A1 on the next real client ticket
- ⚠ DT~Z will read STALE next tick by threshold — **declared close, not a stall**
