# ANDREW-DIRECT 2026-09-14 ~18:1xZ -- DSGN_REBRND: CARD TEXTURE (THE HEX+OPACITY VARIANTS) AND THE LIGHT-MODE INVERSION ARE THE TWO CRUCIAL WORKS

**Terminal:** `2.0.0_SA_COO~D`. It arrived while round 1's drain-end read was being sent (96662/96663). **Recorded
by:** `2.0.0_SA_COO~D`, in the same turn.

## VERBATIM AND ENTIRE

> Another thing I want you to look into is that request i made before where you diff the current changes to component
> color (they are all largely uniform navy blue for panel/card components) with the original request i made that
> established what varietals there were on a basis of hex+opacity. The reasoning for this is that the old hex+opacity
> variants textured the cards significantly, and that attention to detail is lost by consolidating all card/panel
> components to navy blue. We need to figure out how to represent that texturing properly, for one. In addition to
> that (secondly), I want to look into the "light mode" inversion that we had discussed prior, aka the light on dark
> versus the old dark on light color schema. I have yet to see this represented either so I want to go through and
> establish the implications there, as for example when a field/card is highlighted, because the text is light (as
> its sitting on a dark component), that means that text has to flip dark when the field is highlighted so that it
> retains legibility. These are the two crucial, large-scale works that this design rebrand needs to accomplish.
> Secondary to these are making sure that the indigo accents are not all lost, and that we have some continuity in the
> various tooltips, as now there are varying tooltips across the platform, but again that is a tertiary concern and
> not as heavy as a lift because we'll just make a few selective edits.

**And, minutes later in the same turn, VERBATIM AND ENTIRE:**

> In addition to that, I need the feature branch build up on localhost 5173 so I can visually smoke current state.

## WHAT IT SETTLES

- **The rebrand's priorities, in his order:**
  1. **CRUCIAL:** card and panel TEXTURE. Today's panels and cards are largely uniform navy. His original request set
     a family of hex+opacity variants, which "textured the cards significantly". The work is to diff that request
     against the current component colour and find how to represent the texture properly.
  2. **CRUCIAL:** the LIGHT-MODE INVERSION, meaning light-on-dark against the old dark-on-light scheme. It is "yet to
     see ... represented". The work is to establish its implications, his named example being state changes: text that
     is light because it sits on a dark component must flip dark when the field or card is highlighted, so it stays
     legible.
  3. **SECONDARY:** the indigo accents are not all lost. RB-s-5 Amendment 1 restored five identity sites, drained
     @086371dd; this word asks for continuity beyond that, not a new set.
  4. **TERTIARY:** tooltip continuity across the platform, a "few selective edits".
- **"Look into" is an investigation asked of this seat now.** Its output feeds round 2 of DSGN_REBRND. Round 1 is
  drained (15 of 15, @a1d0a7451c), and its drain-end read already names the inversion as covered by no cell (row S2 and
  its six siblings; 4,887 light-on-dark idioms in `src/pages/`).

## WHAT IT DOES NOT SETTLE

- **The round-2 mechanics** stay canonical. PRD text (a new FWD for texture, the inversion's state rule, tooltips) is
  `1.0.0_SA_CTO`'s. The recut and the issuance are this seat's.
- **The open items stay open:** whether the sidebar rail's faint indigo edge (row W2-S19) stays or goes, and the
  teardown of the drained worker trees.
- **The portal freeze and the feature-branch ruling** are unchanged.
