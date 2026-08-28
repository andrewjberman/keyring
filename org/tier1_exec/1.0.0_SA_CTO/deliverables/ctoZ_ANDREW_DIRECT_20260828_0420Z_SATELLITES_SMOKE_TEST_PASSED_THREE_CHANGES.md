# ANDREW-DIRECT 2026-08-28 ~04:2xZ — SATELLITES SMOKE TEST PASSED, THREE CHANGES

**Received at:** the `1.0.0_SA_CTO~Z` terminal (site Z), 2026-08-28 ~04:2xZ, in three consecutive sends
**Channel:** direct terminal message, with a screenshot of the rendered page
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn as receipt, per `org/XXX.md`
**Broadcast:** msgs 12691-12696 (the three items) and 12700-12705 (the Satellite-98 supersession),
6 recipients each, 12 DELIVERED / 0 QUEUED / 0 REFUSED.

---

## 1. ⭐ THE HEADLINE, WHICH IS NOT ONE OF THE THREE ITEMS

**HE SMOKE-TESTED THE SATELLITES VIEW ON A LOCAL BUILD AND IT PASSED.**

> "I just build a localhost on 5173, Satellites product looks very good, its basically done"

That is **the bar he reserved to himself for D4**, exercised on a real build against the nine real
books. ⛔ **IT IS NOT A CLOSURE AND NOBODY WRITES ONE.** His standing word: *"I dont want to see
comp-closure on the directives item until i smoke it and its DEFINITIVELY done."* He said **"basically
done ... a couple points id add"** — **the points are the remaining distance.**

## 2. THE INSTRUCTION — VERBATIM, UNEDITED, ALL THREE SENDS

**SEND 1 (the three items):**

> I just build a localhost on 5173, Satellites product looks very good, its basically done only a
> couple points id add [image] first we're getting cut off on the right, so I think there has to be
> some effort here to either make it horizontally scrollable in "Positioning Summary", or just shrink
> the text and bars, but i think a scroll is probably more realistic. Second, need a logical color
> gradient for the toggle selectors of the different satellites, probably just make a gradient that
> spans from orange for the shortest to yellow to green to blue to red, figure out how to blend as
> needed so each has a color spanning betwween those in that order. third, Satellites doesnt ned a
> firm selector, because only one firm has this function. maybe good to keep the dropdown code
> available just comment it oout and have it default to cottonwood, just in case later we may add
> other custom models for other firms.

**SEND 2 (supersedes item 1):**

> one coment, i dont think we have to display visually satellite 98, even if we track it otherwise,
> the premise is that its the same characteristics as 90, so no need to show two, just a frontend
> change only, that would solve the issue with the width and no need for arrows

**SEND 3 (clarifying send 2):**

> *scrollbar would not be necessary i mea[n]

⛔ **The typos are his and are preserved. A tidied quote is a paraphrase wearing quotation marks.**

## 3. THE OPERATIVE SET, AFTER SUPERSESSION

| # | Item | State |
|---|---|---|
| 1 | Horizontal scroll / shrink on POSITIONING SUMMARY | ⛔ **SUPERSEDED by sends 2+3.** Not needed. |
| 1' | **Do not DISPLAY Satellite 98** (same characteristics as 90) | **FRONTEND ONLY.** Still tracked. |
| 2 | Colour gradient for the per-satellite selectors — orange → yellow → green → blue → red | STANDS. Two asks open (§5). |
| 3 | **No firm selector** on Satellites; keep the dropdown code **commented**, default **cottonwood** | STANDS. |

## 4. ⛔ THE ARCHITECTURE LIMB ON 1' — THE ONE THAT CAN BE GOT WRONG CHEAPLY

> *"even if we track it otherwise ... just a frontend change only"*

**THE FILTER IS A RENDER-LAYER FILTER.** It is **NOT** a registry edit and **NOT** a producer change.
The registry keeps **NINE** books; `platinum/satellites/registry.json` stays exactly as published and
verified (2,196 B, 9 books, 9/9 summing to 100.000). The producer keeps deriving 98. **THE PAGE SHOWS
EIGHT.**

⛔ **DO NOT drop 98 from `SATELLITE_MEMBERS`, the registry, or the producer.** That destroys tracked
data to solve a display choice, and it silently changes what the derived predicate admits — against
his own ~22:5xZ ruling (*"Does it say 'Opal Satellite' in the name? Add it and track henceforth"*).

## 5. TWO ASKS PUT BACK TO HIM ON ITEM 2 — NOT GUESSED

**(a) GRADIENT DIRECTION.** *"orange for the shortest."* Measured from his own screenshot, Duration
runs `2.89 · 2.89 · 2.90 · 2.90 · 2.90 · 2.63 · 2.37 · 1.81 · 1.81` across Satellite 15 → 98. **So the
shortest DURATION is 98 (rightmost), which would run the gradient right-to-left** — while the natural
reading of his sentence puts orange on Satellite 15. **These are opposite, and building it backwards
is a visible error on a page he just approved.**

**(b) WHICH ELEMENT.** A grep of `portal/src/pages/Positioning/` for chip / selector / `BOOK_COLORS`
returns **nothing**, so *"the toggle selectors of the different satellites"* does not resolve to an
element this seat can name. **The DE lane identifies it on the rendered page before building.**

## 6. ⛔ ITEM 3 REVERSES WORK SHIPPED ONE HOUR EARLIER, AND THAT IS FINE

`ETFS_SATELLITES.TO-9-DE` — the internal-viewer firm SELECTION — was cut, built, accepted 5/5 and
certified between 03:09Z and 03:38Z. **He has now seen it and does not want it.**

⭐ **NOBODY TREATS THIS AS WASTED OR AS A DEFECT.** The selector is what made the view **reachable**
for him at all — without it he hit a 400 and could not have smoke-tested. **It did its job, and he is
now ruling on the product.** His remedy preserves the reasoning: commented out, not deleted, because
other firms may get custom models later. **A re-scope, not a rework.**

## 7. ⭐ HE INDEPENDENTLY CONFIRMED A FINDING THIS SEAT FILED AND HALF-RETRACTED

At ~01:5xZ this seat filed a SURPRISE {OBSERVATION}: Satellites 90 and 98 have **identical
constituents** and *"will render as two columns of identical numbers under different names ... a
client looking at them side by side will ask."* I attached a **wrong** supporting premise (a broken
duration ladder, from reading `ULT` as Ultra-**Short**) and retracted that premise when
`0.4.0_DS_ClientPlatform~L` falsified it.

**THE OBSERVATION WAS CORRECT AND ANDREW REACHED THE SAME CONCLUSION FROM THE RENDERED PAGE TWO HOURS
LATER.** His screenshot confirms it column-by-column: 90 and 98 identical on Cost 35.71, Beta 0.96,
Duration 1.81, Yield 1.99, # of ETFs 16, allocation 8.1/91.9.

⚠ **Recorded precisely because the reasoning was wrong: a right observation with a wrong rationale is
still a right observation, and retracting the rationale must not be read as retracting the finding.**
DS~L's measurement — distinct `model_id`s, identical children — is exactly what makes the display
filter **correct rather than a data bug**.

---

*Recorded by `1.0.0_SA_CTO~Z`. Nothing outside the quoted blocks in §2 is his word.*
