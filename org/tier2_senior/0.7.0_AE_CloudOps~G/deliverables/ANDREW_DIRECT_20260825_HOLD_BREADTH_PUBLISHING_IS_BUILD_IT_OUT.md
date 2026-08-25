# ANDREW-DIRECT 2026-08-25 ~04:0xZ — THE DEV-ONLY HOLD DOES NOT REACH THE PUBLISHER. Publishing is part of "build it out"; the hold binds the PROMOTE ACT alone.

**Received at:** `0.7.0_AE_CloudOps~G` terminal, directly — he was answering this seat's `/open-calls`
CALL 1. **Not a relay.**
**Recorded:** 2026-08-25T040153Z. **Broadcast:** same turn.

---

## VERBATIM

> **"Agreeed with your rec"**

Quoted exactly, including the typo, because the phrasing is the ruling and this record does not tidy
his words. He was answering CALL 1, whose REC he ratified in full.

## THE CALL HE ANSWERED, AND THE REC HE RATIFIED

**CALL 1 (put twice, 02:49Z and 03:39Z):** *Does the DEV-only hold reach the PUBLISHER, or only the
portal promote? (a) no PERFRP key publishes until the hold lifts, or (b) publishing is part of "build
it out" and the hold is the promote act alone.*

**The REC he agreed with had TWO parts, and both are ratified:**

1. **(b)** — publishing is part of "build it out"; the hold binds the promote act alone.
2. **THE ATTACHED CONDITION**, verbatim as I put it to him: *"PERFRP keys publish only after the
   round-1 emitters are wired and their first emission is read — never as a side effect of someone
   activating the publisher's schedule for the ten legacy twins."*

**Both halves bind. The condition is now HIS, not a recommendation** — a rec ratified whole is
ratified whole, and reading only the (b) half would be the widening this fabric's law forbids.

## WHAT MADE THE CALL NECESSARY (the measurement, not the argument)

His 01:1xZ hold is branch-shaped — *"stay on the DEV branch not promoted to PROD"* — but the data
layer is **not** branch-scoped. Measured: `platinum/advi/49financial/` is ONE key set in ONE bucket
with **no environment conditioning anywhere in the read path**, and the portal's own
`adviKeyRepoint.ts` records an exercised 200 through the auth path on **DEV and on PROD**. So
publishing a key makes it PROD-fetchable **with no promote occurring** — the promote and the data
exposure are two different events, and his sentence governed only one of them.

Supporting, and disclosed as evidence rather than as a ruling: PRD `s.11 #11` opens **"DEV render as
keys land"** — the PRD's own position is that publication is *how* the DEV render happens. That line
predates his 01:1xZ word, so it informed the rec; it did not decide it.

### ⛔ THE CONSUMER HALF — MEASURED BY `0.4.0_DE_ClientPlatform~D` (68637), NOT BY ME

When I put the call to him I said the exposure was narrow because *"the PROD build carries no PERFRP
card components until a promote ships them."* **That was an ASSERTION when I made it.** DE~D has since
measured it at `origin/PROD 8a96c91654`: none of their commits are on PROD, and `git ls-tree` for the
`perfrp/` renderer tree at the PROD ref **returns nothing** — the tree does not exist there. So a
published PERFRP key has **no consumer on PROD**: nothing there can fetch, parse or render it.

The assertion held. It was still unmeasured at the moment I rested a recommendation on it, and that is
recorded here rather than quietly upgraded to a measurement after the fact.

⛔ **AND THE DEPENDENCY MUST BE STATED, NOT ENJOYED AS COMFORT — DE~D's point and it is the sharper
one: THAT SAFETY IS A PROPERTY OF THE PROMOTE HOLD, NOT OF THE PUBLISH DECISION.** The moment the
renderer promotes, published keys become live client-facing surface **with no further act**. The two
holds are therefore **complementary and not redundant**: his DEV-only word is what makes publishing
safe, and neither hold should be described as belt-and-braces for the other.

**For whoever holds the promote (`0.2.0_DT_PortfolioAnalytics` or whichever DT seat is live):
RE-MEASURE THIS AT PROMOTE TIME.** *"No consumer on PROD"* is true at 2026-08-25 ~04:1xZ and is
exactly the kind of favourable fact that stops being true without anyone editing the sentence that
asserts it — the moment-encoded-as-mechanism class, applied by DE~D to their own measurement.

## WHAT THIS SETTLES

- The DEV-only hold **does not** reach the publisher. Wiring and publishing PERFRP keys proceeds.
- The hold binds **the PROD promote act**.
- PERFRP keys publish **only** after their emitters are wired and the first emission is read, and
  **never** as a side effect of a publisher-schedule activation done for the ten legacy twins.

## ⛔ WHAT THIS DOES **NOT** SETTLE — not adjudicated here

- **It does not lift the PROD hold.** That still requires the `s.14` end-to-end standard satisfied and
  **his word at the promote act**. Nothing here shortens that.
- **It does not touch the 49F switch hold** (on Mike). CTO ruled the two holds independent; satisfying
  one releases nothing of the other, and this ruling is about neither's satisfaction.
- **It does not ratify `s.14`.** That call is open and sits on CTO's list — ratify, replace, or name a
  verifier.
- **It says nothing about the ten legacy twins' own publication cadence.** It constrains only that
  PERFRP must not ride it.

## HOW I IMPLEMENT THE CONDITION — and why it needs NO new mechanism

**Wire each family's `EMITTERS` entry only once that family's emitter exists and its first emission
has been read. An absent entry cannot publish.**

That satisfies his condition by construction: if someone activates the publisher's schedule for the
legacy twins, an unwired PERFRP family is not in the registry and cannot emit as a side effect. It
needs no field, no flag, and no code — Build Ladder rung 1, the thing that does not need to exist.

⛔ **I deliberately am NOT implementing this by widening the `deferred` field, and the reason is my
own Rule-24 record.** `deferred` was minted for Transactions' **sovereign-ruled deferral** — permanent
until a ruling moves it. Using the same field for **not-yet-emitted staging** would put two intents on
one field (postulate (iii)) whose members take **different remedies and different clocks** (postulate
(iv)): Transactions un-defers on a CTO/Andrew ruling; a staged family un-defers when its emission is
read. That is the exact failure the two-field determination avoided, and re-committing it inside the
field that determination created would be worse than never having run the test.

**Incremental wiring is therefore the implementation, and `deferred` keeps its single meaning.**

## STATE AT THIS SEAT — unchanged by this ruling

Start condition still UNMET: `PERFRP_EMITTER_FAMILIES` carries the 11 names but **zero**
`script`/`leaf`/`needs` keys, no per-family emitter scripts exist, and no leaf has been emitted.
AC5 PASS; proof instance VALID rc=0. Nothing built, no criterion flipped, no infrastructure touched.
