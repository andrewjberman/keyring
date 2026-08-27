# ANDREW-DIRECT 2026-08-27 ~19:3xZ — the Asset Category Views VISUAL SPEC

**Received by:** `0.4.0_DE_ClientPlatform~Z`, at the site-Z terminal, during his own visual smoke of
portal `7ed51b9e`.
**Recorded same-turn per `org/XXX.md`** ("ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION RECORDS IT
DURABLY AND BROADCASTS IT -- SAME TURN. NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.")

---

## VERBATIM

> "Ok that's fine, the issue now is simply a better execution on the visual. The Premise should be
> left to right three cards, Models, SMAs, Client. Drilldown at Models should Primary and Custom,
> either of which can be clicked for L2 drill which is the 5 UST ST INT LT ULT models for primary,
> and any custom models for custom, like Opal Fixed Income. For SMAs that should be the strategy
> SMAs. For Client it should be Client Opal-Supervised and Client Opal-Unsupervised. VIsually these
> need to be much nicer, I think a logical approach is simply a horizontal bar that is color coded
> and dollar amounts."

---

## THE SPEC, DECOMPOSED (structure only — no interpretation added)

```
L0   three cards, LEFT TO RIGHT, in THIS order:   Models  ·  SMAs  ·  Client

L1   Models   -> Primary | Custom          (BOTH clickable, each drills to L2)
     SMAs     -> the strategy SMAs
     Client   -> Client Opal-Supervised | Client Opal-Unsupervised

L2   Models > Primary -> the 5: UST, ST, INT, LT, ULT
     Models > Custom  -> any custom models (his example: "Opal Fixed Income")

VISUAL  "much nicer" — his proposed approach: a HORIZONTAL BAR, COLOR CODED, with DOLLAR AMOUNTS.
```

## WHAT THIS CHANGES vs THE SHIPPED RENDER

| | shipped (`7ed51b9e`) | this spec |
|---|---|---|
| L0 form | four square tiles, emitter's peer order | **three cards, left-to-right, named order** |
| L0 order | `view_plane.peers` as emitted | **Models · SMAs · Client** |
| L1 Models | Primary / Custom as text rows | same two, **each clickable to L2** |
| L2 | Custom members only | **Primary (5 archetypes) AND Custom** |
| idiom | text rows + a footnote | **color-coded horizontal bar + dollar amounts** |

## ⛔ WHAT I AM NOT INFERRING FROM THIS, AND AM SURFACING INSTEAD

1. **ALTERNATIVES.** His 2026-08-24 ~18:5xZ word ruled L0 = `{Client, Models, SMAs, Alternatives}`
   with "Alternatives L1 deferred". This word names **three** cards and does not mention it.
   ⚠ **He was almost certainly describing the REAL state, not superseding that ruling:** Alternatives
   only appeared on his screen because **my synthetic fixture invented $3M for it**. On real data the
   presence predicate (`D1-h-p1`, served AUM > 0) renders **no tile** — so the live L0 is already
   three. **I am fixing the FIXTURE, not deleting the Alternatives code path**, and flagging the
   question rather than answering it for him.
2. **INSURANCE** stays out of the tree (view-plane flag) — untouched by this word.
3. **CLIENT LABELS.** He says "Client Opal-Supervised" / "Client Opal-Unsupervised". The renderer
   draws `child.label` from the emitter and **must not hardcode** these — a label supersession
   already happened once on this surface. If the emitter's labels differ from his words, that is a
   DS/emitter reconciliation, not a renderer literal.
4. **THE `D1-inv-4` SUM LINE and the predicate-unavailable state** are not mentioned and are
   **not removed** — they are ruled behaviour from prior words and survive a visual restyle.

## STANDING CONSTRAINTS THAT DO NOT MOVE

- **D1_CATVIEWS is NO-SHIP** (lifts only BY NAME, `build_package.py:266`). This is a portal-DEV
  render change; it neither lifts nor touches that.
- **Membership is never computed in the renderer.** The block carries its own partition; we render
  what it designates. A prettier bar does not become a place to derive numbers.
- **Rule 27:** this seat is currently seated `ETFS_INGEST`. A sovereign instruction overrides a
  seating directive (`org/XXX.md` authority hierarchy); surfaced to COO/CTO/MSTR same-turn rather
  than adjudicated here.
