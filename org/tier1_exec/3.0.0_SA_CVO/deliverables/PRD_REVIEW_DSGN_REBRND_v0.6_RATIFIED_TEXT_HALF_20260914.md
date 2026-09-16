# PRD REVIEW -- DSGN_REBRND v0.6 @97cf19d758 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96687 (18:45:08Z), and `1.0.0_SA_CTO` msg 96689.

**Prior:** v0.5 SIGNED, review @9b3289461f and stamp @d40b42d44b.

**Read, UTC 2026-09-14, after 18:45Z:**
- The PRD @`97cf19d758`. The working copy is identical to HEAD, and it is the one commit on the path since v0.5.
- The full diff v0.5 -> v0.6.
- Andrew's two records:
  - @`e7051143e2` (~18:1xZ, relayed as 96669);
  - @`0e0e97f75a` (~18:3xZ, relayed as 96682).
- On `feature/d13-visual-elevation`:
  - `design/brand/portal-opaque-ladder.json` @`401ad3b961`, read whole;
  - `design/brand/inversion-rule.json` @`1bedb59788`, read whole.
- The measured website file, which is unchanged since @d4b20a28ba and was read whole for the v0.4 review.

**Half hash:** the notifier's `f5421024e4f0`. The stamp is bound with `--expect-half-hash`.

## VERDICT: REFUSE on R3 -- a DERIVED value without its rule: the band-world rung

## THE DIFF OF THIS HALF, v0.5 -> v0.6

- **ENDPOINT:**
  - FWD-4's closed identity set gains "the sidebar rail's faint edge".
  - FWD-9's CONSTRAINT widens to FWD-1..8 and FWD-10..13.
  - FWD-12 (named layers) and FWD-13 (the state rule) are APPENDED.
- **CONTRACTS:**
  - The preamble's DERIVED list gains "the named-layer role rungs in each world, the per-state inks", with two rules added beside them.
  - The identity rule gains "the sidebar rail's faint edge added by his word, v0.6".
  - The `DesignContract` row gains the surface-layer, state and page-scope clauses, and the rail edge.
  - The `DesignTokens` row gains role-rung and state tokens.
  - MEASURED is unchanged, and still reads 9 of 9 against the file it cites.

## WHAT IS RIGHT

- **FWD-4.**
  - His word is *"I like faint indigo edge on the sidebar"*.
  - The set gains exactly that member. His wider sidebar question, keep the current treatment or revert to the DEV one, is recorded as open, not decided.
  - The PROOF still fails a sixth unnamed carrier.
- **FWD-12 and FWD-13 are verbatim to his words:**
  - *"Named layers is fine"*;
  - *"when a field/card is highlighted, because the text is light ... that text has to flip dark when the field is highlighted so that it retains legibility"*;
  - *"Text follows its current background is a good rule"*.

  Each PROOF discriminates. FWD-12's prints every neighbouring pair's ratio with a denominator. FWD-13's grades every (ground, ink) pair against the CONTRACTS bar, with the denominator roles x states x worlds.
- **No seat name enters ENDPOINT.** His words are cited as sources, and the history is in PROVENANCE v0.6.
- **MEASURED gains nothing, and nothing new is labelled captured.** This keeps the v0.4 and v0.5 corrections.
- **Counterpart agreement.**
  - `IRPT_FNTEND` consumes the tokens. The page-level surface scope is off by default, so no IRPT surface changes until it opts in.
  - `IRPT_FNTEND`'s PRD carries no surface-layer or state clause that this contradicts.

## R3 -- the band-world rung is classed DERIVED and carries no rule

**The carrier, the CONTRACTS preamble @`97cf19d758`:**
- DERIVED now includes *"the named-layer role rungs in each world, the per-state inks"*.
- The section's rule: *"A derived value is never labelled captured: its derivation rule is written beside it in the contract"*.
- The rules written beside the new values:
  - *"each role's light rung is derived from its dark rung by the inversion rule (`design/brand/inversion-rule.json` ... keep the contrast ratio and the role, re-derive the value, opacity 1.0)"*;
  - *"each state's ink is computed against that state's own ground to the contrast bar below"*.

**What is missing.** The light rung's rule presupposes a dark rung, and no rule says where the dark rung comes from. It is
not a FIXED brand value. `portal-opaque-ladder.json` @`401ad3b961` lists the band rungs `#0B111D`, `#101828`,
`#152037`, `#1B2946` and `#223358`, and none is one of the brand's four colours (`brand_source` in the same file). It is
not MEASURED either: the website file has no rung of any kind. So it is DERIVED, and the file that holds it states its
rule in its first line: *"ONE opacity (1.0). Hue held at the brand navy family (221 deg); lightness is the only
lever."* That rule is not beside the value in the ratified text. This is the v0.3 and v0.4 defect class, a value in
this section without the class-and-rule the section requires, now on the value v0.6 added.

**The fix, the CTO's to word. One clause, beside the other two:**
*"each role's band rung is a rung of the opaque ladder (`design/brand/portal-opaque-ladder.json` on
`feature/d13-visual-elevation` @`401ad3b961`: one opacity, hue held at the brand navy family, lightness the only
lever)"*, or whatever rule the CTO rules.

**Sign condition:** every DERIVED value in the preamble has its rule beside it, the band rung included. Nothing else in
this half needs to move.

## NOTES (non-blocking)

- **N1 -- FWD-12's single "tooltip" role should not read as deciding his three tooltip types.** His item 5 says there
  are *"three types of tooltips that vary slightly so id have to clarify each"*, and NOT COMMISSIONED keeps tooltip
  continuity out *"until he speaks"*. FWD-12's role table names one `tooltip` role. That is compatible if his three types
  share a ground. If his clarification gives them different grounds, the role table grows by his word. At the next bump
  of this half, one clause saying so would stop a grader reading FWD-12 as having decided it.
- **N2 -- at-the-cut figures inside ENDPOINT.**
  - FWD-12's PROOF carries *"(at the cut, seven container tokens alias `--bg-band`, portal/src/index.css:115-121 on the feature branch)"* and *"(bg 634, border 757, text 1,894 at the cut)"*.
  - FWD-13's PROOF carries *"(345 in 120 files at the cut)"*.
  - These are vintage-bound readings inside ratified text, and they age with the tree. The PROOF clauses stand without them, and cells R15-R17 already carry them.
- **N3 -- for R15, not this text.** The ladder the preamble will cite has 5 band rungs and 4 light rungs. FWD-12 names 8
  roles, and says no two neighbouring roles share a value. R15 has to extend the ladder or show the pairings. The PRD
  text is right to leave that to the cell.
- **N4 -- carried from v0.3:** the form of each identity member, and a bar on the accent's share, remain unbounded.
  With the rail edge there are now seven persistent carriers. The PROOF names them all and prints the share.

## NOT CLAIMED

- **The brief half.** It is `2.0.0_SA_COO~D`'s, and reads STALE at v0.6.
- **That the page-level surface scope is sound engineering.** It is cell R15's to prove with its pixel-compared render.
  The text names it a migration switch with one writer and a stated retirement, not a second system.
- **Any round-1 grade.** Round 1 is graded against the specification that issued it, and v0.6 is the round-2 addendum.
