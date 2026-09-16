# PRD REVIEW -- DSGN_REBRND v0.8 @5dd24300f7 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96707 (19:19:09Z).

**Prior:** the v0.6 and v0.7 half was REFUSED on R3, review @b8aba1cc5f and stamp @e72f9fb6c9.

**Read, UTC 2026-09-14, after 19:19Z:**
- The PRD @`5dd24300f7`. HEAD and the working copy are identical, and it is the one commit on the path since v0.7.
- The CONTRACTS preamble, read in full at v0.8, character-diffed against v0.7.
- The ENDPOINT and CONTRACTS sections, line-diffed against v0.7.

**Half hash:** the notifier's `53f6c167b642`. The stamp is bound with `--expect-half-hash`.

## VERDICT: SIGN -- R3 closed; N1 and N2 taken; nothing else in this half moved

## THE DIFF OF THIS HALF, v0.7 -> v0.8 (the v0.6 bytes)

- **CONTRACTS: 1 line, the preamble.** The character diff has exactly one replace: *"light rung is derived from its dark"* becomes *"band rung is a rung of the opaque ladder (`design/brand/portal-opaque-ladder.json` on `feature/d13-visual-elevation` @`401ad3b961`: one opacity, hue held at the brand navy family, lightness the only lever); each role's light rung is derived from its band"*. MEASURED is byte-unchanged and still reads 9 of 9.
- **ENDPOINT: 3 lines.**
  - FWD-12 PROOF: the two at-the-cut figures are removed. That is N2.
  - FWD-12 CONSTRAINT: gains *"the one tooltip role does not decide Andrew's three tooltip types -- if his clarification gives them different grounds, the role table grows by his word"*. That is N1.
  - FWD-13 PROOF: the at-the-cut figure is removed. That is N2.

## R3 -- CLOSED

- The band rung now carries its rule beside it, in the ladder file's own words, pinned to the commit.
- The light rung's rule now chains from the band rung. The v0.6 text chained it from a "dark rung" that no rule defined.
- Sign condition from the v0.6 review: every DERIVED value the preamble gives a rule for is chained to a defined source. Met.

## THE WHOLE DERIVED CLASS, CENSUSED -- stated so that no member is left unread

This census should have run at v0.2. The v0.4 review's lesson was to census the whole class, not the member handed to
me. Here it is over the ten DERIVED members at v0.8:

| DERIVED member | rule pinned in the preamble |
|---|---|
| the status family | yes -- "status hues from the brand palette at fixed lightness steps, never from a template" |
| the data family beyond the model colours | no |
| the ordered-scale ramp steps | yes -- "ramps as lightness steps of one brand-derived hue" |
| the dark-mode values | yes -- "the same roles inverted" |
| the spacing scale | no |
| the four empty states | no |
| the accent's identity role | yes -- the closed list, extended only by his word |
| the text-selection highlight | yes -- FWD-4 and brief A23 |
| the named-layer role rungs (band and light) | yes -- the opaque ladder; the inversion rule |
| the per-state inks | yes -- computed against the state's own ground to the bar |

**7 of 10 have their rule pinned in the preamble. Three do not: the data family, the spacing scale and the four empty
states.** The section's sentence reads *"its derivation rule is written beside it **in the contract**"*, meaning
`portal/DESIGN.md`, which R7 produces, with R8 for the data family and R11 for the empty states. So the PRD pins some
rules and requires the contract to write the rest. By that sentence the three are the contract's to carry, and this
half has no gap.

That reading also bounds R3. R3 was the stricter reading: a rule the preamble had started to chain, for the light rung,
depended on a rung it never defined. The CTO took it. The three here have no such dangling chain.

**For R7 and L9, not for this text:** a contract whose YAML front matter names the data family, the spacing scale or the
empty states without a derivation rule beside each fails this sentence at grading.

## NOTES (non-blocking)

- **N3 carries.** The ladder has 5 band rungs and 4 light rungs, and FWD-12 names 8 roles. That is R15's to extend or pair.
- **N4 carries.** The form of each identity member, and a bar on the accent's share, remain unbounded. There are now seven persistent carriers, and the PROOF names them all.

## NOT CLAIMED

- **The brief half.** It is `2.0.0_SA_COO~D`'s, and reads STALE at v0.8.
- **That `portal/DESIGN.md` carries these rules.** It is on the feature branch, and this review did not read it. Round-1 row C-S12 (graduated) records that it carries no class labels at all.
