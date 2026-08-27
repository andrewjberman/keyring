# ANDREW-DIRECT 2026-08-27 ~22:3xZ — L2 drilldowns carry AMOUNTS, dots left, value right

**Received by:** `0.4.0_DE_ClientPlatform~Z` (D1_CATVIEWS DE lane) at the site-Z terminal, answering
this seat's smoke instructions for the Asset Category Views panel.
**Recorded same-turn per `org/XXX.md`.**

> ⛔ **VERBATIM. THE PHRASING IS THE RULING — do not paraphrase this block.**

> *"This looks pretty good but what I'd recommend is that the drilldowns show AUM amounts and also
> are visually structured a little better with colored dots on the left and asset value on the right
> and no parentheticals needed."*

---

## WHAT IT RULES — three things, and the third is the one with a consequence

1. **L2 drilldowns SHOW AUM AMOUNTS.** Today L2 is a bare name list; L1 already carries amounts.
2. **L2 adopts the L1 row idiom**: coloured dot on the LEFT, name, **asset value on the RIGHT**.
   *"visually structured a little better"* — the shape already exists one level up, so this is
   **uniformity with L1**, not a new visual language. It is the L2 instance of his standing
   *"the shapes should all be the same in layout"*.
3. **NO PARENTHETICALS.**

## ⭐ 1 AND 3 ARE CONNECTED, AND THAT IS WHY 3 IS SAFE TO OBEY

The L2 panel carried two editorial asides:

| aside | why it existed |
|---|---|
| *"Registry membership -- not a per-firm holding."* | `2.0.0_SA_COO~Z` standing render rule 67612 — a **registry-plane** name list rendered beside a **firm-plane** dollar figure reads as "$43.5M sits in models we do not serve". Both halves true, **the adjacency lying**. |
| *"not served as a standalone artifact"* | a per-member `served: false` note |

⛔ **THE CAVEAT'S PRECONDITION IS THE THING HIS FIRST INSTRUCTION REMOVES.** The rule exists because
the L2 list carried **no numbers of its own** and sat next to one that was not about it. **Once every
L2 row carries its OWN firm-plane amount there is no cross-plane adjacency left to disambiguate** —
and a firm holding none of a registered model now says so with `$0.00` rather than with a sentence.
Keeping the caveat under per-member amounts would make it **false**, not merely redundant.

⚠ **THIS REMOVES ANOTHER OFFICE'S CONTROL AND IS NOT DONE SILENTLY.** Surfaced to `2.0.0_SA_COO~Z`
in the same turn: the control is retired because its **precondition** is gone, not because a
sovereign found it ugly. If COO holds that the plane label must survive per-member amounts, it goes
back — that is their call, not this lane's.

### The literal parenthetical

`CategoryViewTree.tsx` rendered `(third bucket)` beside an L1 row whose child carried
`third_bucket`. Removed. **Consequence stated rather than buried: the `third_bucket` flag now has NO
rendered surface at all.** It renders nothing today in any scope, so nothing observable changes —
but if it ever needs to be visible, someone must give it one. The field stays in the contract type;
it is the emitter's, not this lane's to delete.

## ⛔ THE DATA HALF IS NOT THIS LANE'S, AND IT IS NOT A BLOCKER

`_members()` emits `{member_id, display_name, served, strategy_id}` — **no `aum`**
(`mdpf_category_registry.py:900-903`). So the producer must gain a per-member amount before this
renders from real data.

⭐ **THE DATA EXISTS AND IS BEING AGGREGATED AWAY, WHICH MAKES THIS AN EMIT CHANGE RATHER THAN A
MEASUREMENT ONE.** `0.4.0_DS_ClientPlatform~Z` (msg 10382) describes the consolidator summing
**`sma_member_aum` through `registry.members_for()`** into the two bucket keys. The member grain is
already there and is being rolled up. Routed to the DS lane; **NOT performed here.**

**What landed in this lane:** the renderer draws `member.aum` whenever the block carries it, and the
smoke fixture carries it so the shape is exercisable now. `MdpfCategoryMember.aum` is typed
**OPTIONAL and nullable** — absent means ABSENT-AT-THIS-VINTAGE, never zero. Rendering `$0` for an
unmeasured member would state a measurement nobody took, which is the exact error the L1 null-guard
already exists to prevent.

## STILL OPEN, UNCHANGED BY THIS WORD

- **Client has no L2 anywhere in the record**, so it has no drilldown to carry amounts. His to say.
- Whether a zero / no-members L0 node should render a card at all (*"invisible otherwise"*), and
  whether `absent_reason` should surface on it.
