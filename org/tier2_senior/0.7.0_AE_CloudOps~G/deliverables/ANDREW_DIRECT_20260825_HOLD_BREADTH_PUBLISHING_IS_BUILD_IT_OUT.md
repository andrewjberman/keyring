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

### ⛔⛔ THAT WARNING FIRED WITHIN THREE HOURS. THE CLAUSE ABOVE IS NOW FALSE — 2026-08-25 ~07:1xZ

**`"a published PERFRP key has NO CONSUMER ON PROD"` IS FALSE AS OF 05:47:35Z.** Surfaced by
`0.4.0_DE_ClientPlatform~D` (69461) checking their own push state; **confirmed independently at this
seat on the artifact, with a positive control:**

- `origin/PROD` tip is now **`d9a98bcc39`** — my recorded O-5 baseline `8a96c91654` **has moved**.
- All **8** perfrp renderer files are present under
  `src/pages/AdvisorIntelligence/_shared/perfrp/` at that ref.
- Positive control: the same `ls-tree` returns **59** files under `AdvisorIntelligence/`, so an empty
  result would have been distinguishable from a broken read.

**THE PROMOTE POSTDATES HIS HOLD BY ~4.5 HOURS:** tip authored `2026-08-25T01:47:35-04:00` = **05:47:35Z**
by `0.2.0_DT_PortfolioAnalytics~Z`, subject *"merge DEV->PROD: v2.1.165 — ETFS_POSITIONING goes to
production for the FIRST time."* (Offset-bearing format deliberately; a hand-typed `Z` on a local
rendering is the error this seat made at ~06:5xZ and will not repeat.)

⛔ **THE MECHANISM, AND NO VERDICT IS OFFERED HERE — the scope of his word is his, and whether this
breaches the hold is COO's and CTO's:** the promote was **for ETFS_POSITIONING**. A promote is a
**whole-branch merge**, so it carried everything on DEV, including PERFRP's renderer. DE~D's DEV
commits are exactly what his word authorises. **Nobody promoted PERFRP on purpose — it arrived as a
SIDE EFFECT of another project's promote.**

**AND THAT IS THE SHAPE OF HIS OWN RATIFIED CONDITION, ON THE OTHER AXIS.** He ratified: publish
*"never as a side effect of someone activating the publisher's schedule for the ten legacy twins."*
The identical side-effect mechanism has now operated on the **PROMOTE** axis rather than the
**PUBLISH** axis — **and the protection he ratified only ever covered the axis he was asked about.**

**OPERATIVE CONSEQUENCE FOR THIS LANE:** publishing a PERFRP key is no longer the narrow act it was
when he ratified it — there is now a live consumer on PROD. **Nothing has been published and nothing
will be until this is ruled.**

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

---

## ⛔⛔⛔ CORRECTION 2026-08-25T08:2xZ — THE MECHANISM I GAVE ANDREW IS GONE. The condition now holds BY ACCIDENT, not BY CONSTRUCTION.

**Two claims above are FALSE as measured at 2026-08-25T08:15Z-08:25Z at this seat.**

### FALSE CLAIM 1 — "Start condition still UNMET ... zero `script`/`leaf`/`needs` keys" (line ~138)

TRUE when written at 04:01:53Z. **FALSE at 04:57:24Z**, 56 minutes later. All **11** PERFRP families
are wired into the publisher's `EMITTERS` with complete `script`/`leaf`/`legacy`/`needs` keys by
`9af61d7e2e` (`0.4.0_DS_ClientPlatform~G`, 2026-08-25T00:57:24-04:00 = 04:57:24Z). The per-family
emitter scripts exist — 18 PERFRP modules on disk and on the executing plane.

**This is the moment-encoded-as-mechanism class landing in my own record**: a state true of an instant,
written as a standing condition, in the file that records a sovereign ruling. It went stale without
anyone editing the sentence.

### ⛔ FALSE CLAIM 2 — the load-bearing one: "An absent entry cannot publish" (line ~120)

I told Andrew his ratified condition was satisfied **BY CONSTRUCTION**, verbatim above:
*"if someone activates the publisher's schedule for the legacy twins, an unwired PERFRP family is not
in the registry and cannot emit as a side effect."*

**TEN OF THE ELEVEN FAMILIES ARE NO LONGER ABSENT.** Only `perfrp_transactions_relationship` is
protected, by the `deferred` disarm (mine, `79a2eff0ed`) — which I verified present and correctly
ordered ON THE DEPLOYED BYTES (`:589` before `:592`, negative control 0).

And the publisher does not merely serve pre-existing artifacts — **it INVOKES the emitter**
(`subprocess.run(argv)`, deployed `:442`), so `status="built"` is produced BY the publish run itself.
The ten non-deferred families would build and publish on any `--publish` invocation.

### WHY THE CONDITION NEVERTHELESS STILL HOLDS — and why that is not reassuring

Measured, with controls, region `us-east-1` confirmed against the target Lambda's own ARN:

| # | Break | State |
|---|---|---|
| 1 | schedule `advi-49f-publisher` `cron(15 13 * * ? *)` | **DISABLED** (last modified 2026-08-19T17:32:28Z) |
| 2 | its target SSM document `advi-49f-publisher-dispatch` | **DOES NOT EXIST** |
| 3 | the 12:45Z chain's stage list | no publisher stage (`0.4.0_DS_ClientPlatform~G`, 69681 — not re-run by me) |

Controls for break 2: positive `advi-49f-chain-dispatch` returns its name; negative
`zzz-no-such-doc-9999` returns `InvalidDocument`; the target returns a response **byte-identical to the
negative control**. The absence is measured, not a wrong-region artifact.

⛔ **NEITHER BREAK IS A GUARD. A MISSING SSM DOCUMENT IS AN INCOMPLETE BUILD, NOT A CONTROL** — and the
routine act that finishes the publisher's deployment (create the document, enable the schedule) is
**exactly** the act Andrew's condition names: *"someone activating the publisher's schedule for the ten
legacy twins."* The protection he was promised was a property of the registry. What is actually holding
the line is two pieces of unfinished infrastructure that nobody is maintaining as a safeguard, that no
record describes as one, and that I do not own.

**I classified this ARMED while working and the measurement corrected me to INERT.** Recorded in that
order deliberately: harm requires two new acts, so it is INERT — but the disarm-by-construction I
described to Andrew is gone, and INERT here is a fact about infrastructure debt, not about a control.

### WHAT I AM *NOT* DOING, and why

**I am not removing the ten entries to restore my mechanism.** They are `0.4.0_DS_ClientPlatform~G`'s
landed work under their AC13, and reverting another lane's criterion-bearing commit to restore a
mechanism *I* described in *my* record is a cross-lane act I have no warrant for.
**I am not widening `deferred` to cover them** — my own Rule-24 determination forbids it (two intents,
two clocks, one field), and re-committing that violation inside the field the determination created
would be worse than never having run the test.

**The fork is genuine and it is not mine to close**: restoring the promised construction conflicts with
landed DS work. Routed to CTO with DS~G and CVO copied. Rule 27: **BLOCKING x INERT.**

**Nothing published. Zero PERFRP keys served. No schedule enabled, no document created, no entry removed.**
