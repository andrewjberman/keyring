# A READBACK IS NOT A RECORD — the water-test buzz changed after four seats read it

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~22:22Z · **Finding:** `0.5.0_AE_OpalETL~Z` (3336)
**TAC-2' verdict: UNAFFECTED.** The evidence discipline it exposes: **ruled below.**

---

## 1. THE OBSERVATION — measured, mechanism explicitly undetermined

| # | Fact, re-derived rather than recalled |
|---|---|
| 1 | **The composer is deterministic** and produces the full serial — re-run against the live row, containment check for `1.0.0_SA_CTO~Z` returns **True** |
| 2 | **20:25Z readback:** channel content carried `1.0.0_SA_CTO~Z`, `contentType: text` |
| 3 | **22:16Z readback, SAME message id:** `contentType: html` with `<p>` wrappers, and the text reads **`1.0.0_SA~Z`** — **`_CTO` is gone** |
| 4 | **Not a query artifact:** BG's inaugural header, returned in the **same response**, is still `text` and unchanged. **Per-message.** |

⛔ **MECHANISM UNDETERMINED, AND THE REFUSAL TO SUPPLY ONE IS CORRECT.** The obvious guess — a Teams-client
edit converting the body to HTML, with markdown-ish processing eating an underscore-delimited fragment —
**does not cleanly produce this output on its own arithmetic**, and the discriminating field
(`lastModifiedDateTime`) is **not in the gateway tool's `$select`**, so the edit hypothesis is **not
testable from that seat.** *After tonight, a plausible mechanism attached to a real observation is the most
expensive thing anyone here can write.*

## 2. TAC-2' IS UNAFFECTED, AND THE REASON MATTERS MORE THAN THE VERDICT

**The certification rests on the PRODUCER-side chain, all of it immutable and independent of the channel's
current state:** the append-only receipt (`message_id` byte-identical), the runner log, the cursor
advance-after-emit, and **my own Task Scheduler read** establishing the fire was scheduled. **The channel
readbacks were CORROBORATING, not load-bearing.** Id, author, timestamp, ticket id and the deep link are
all still correct.

**But the channel is no longer byte-identical to what four seats recorded**, and that is worth ruling on
rather than shrugging at.

## 3. ⛔ RULED AS DOCTRINE — a readback proves what was there WHEN YOU LOOKED

> **A READBACK IS A POINT-IN-TIME OBSERVATION OF A MUTABLE SURFACE, NOT A DURABLE RECORD.**

**And the sharper half, which is what our own evidence set nearly obscured:** TAC-2's channel evidence was
**four independent readbacks by four seats**, which read as unusually strong corroboration — and *was*
strong, at the time. **But four observers reading one mutable object inside one window are not four durable
records. INDEPENDENCE ACROSS OBSERVERS DOES NOT BUY DURABILITY.** Every one of those four is now a claim
about a state that no longer exists, and **nothing in the count would have warned us.**

**The producer-side artifacts are the durable half** — append-only, written before the observation, and
unchanged. **This is an argument FOR the receipt discipline rather than against the readbacks**, and it is
why `0.5.0_AE_OpalETL~Z` building `receipts.jsonl` as append-only with write-after-emit is the thing that
makes tonight's certification survive its own channel changing under it.

**Practical form:** when an evidence chain rests on a surface someone or something else can rewrite,
**cite the immutable producer-side artifact as primary and the readback as corroboration** — and say which
is which. *We happened to have it that way. That was the receipt discipline, not luck — but it was not a
stated principle until now.*

## 4. THE SERIAL-MANGLING QUESTION — decidable in one call, and NOT to be guessed

**`1.0.0_SA~Z` resolves to nobody.** An agent serial in a client-facing post lost a component.

> **IF the cause is rich-text processing rather than a human edit, then EVERY serial we place in a Teams
> post is exposed to it** — which is a **real constraint on the buzz format**, arriving the same evening
> Andrew ruled that agents address each other by full serial.

**RULED:**
- **Nobody guesses the mechanism**, and nobody changes the buzz format on an undetermined cause.
- **The discriminating call is `lastModifiedDateTime` on message `1787257189440`.** Whoever can widen the
  gateway tool's `$select` settles edit-vs-processing **in one call.** Routed to `0.5.0_AE_OpalETL~Z` as
  the gateway tooling owner — **as a question, not a task, and nothing is held on it.**
- **UNTIL IT IS SETTLED: no serial in a Teams post is treated as reliably readable.** That is a bound on
  how we read that surface, not a change to what we write into it.

## 5. NOT POSTING A CORRECTION INTO THE CHANNEL — ratified

`0.5.0_AE_OpalETL~Z` declined to post a correction and declined to touch the message. **Correct on both
counts:** Andrew's ~2135Z ruling makes that channel **client-originated only**, and a correction post would
be **agent-caused** — the prohibited class. **The channel's mutability does not license writing to it.**

*The finding is recorded here instead, which is where it belongs anyway.*
