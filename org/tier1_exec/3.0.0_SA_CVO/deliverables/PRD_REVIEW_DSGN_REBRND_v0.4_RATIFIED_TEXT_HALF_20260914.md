# PRD REVIEW -- DSGN_REBRND v0.4 @4ebd24684b -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96641 (17:13:55Z).

**Prior:**
- v0.2 was SIGNED @8ad762f7bf.
- v0.3 was REFUSED on R1, review @d779f0b32f and stamp @a878d78f90.

**Read, UTC 2026-09-14, after 17:13Z:**
- The PRD @`4ebd24684b`. HEAD and the working copy are identical to the pin, and it is the one commit on the path
  since v0.3.
- The full diff v0.3 -> v0.4.
- `design/brand/opalinvest.com.json`, read WHOLE: 111 lines, not a pattern search.

**Half hash:** the notifier's `40e01b9ae580`. The stamp is bound with `--expect-half-hash`.

## VERDICT: REFUSE on R2 -- R1's defect, one grain smaller: the text-selection highlight is classed MEASURED and the website does not measure it

## THE DIFF OF THIS HALF, v0.3 -> v0.4

- **ENDPOINT:** FWD-4's SOURCE gains *"Andrew-direct 2026-09-14 ~15:0xZ (the identity set; PROVENANCE v0.3)"*. This is
  N1, taken. No seat name enters the section, and nothing else in ENDPOINT moved.
- **CONTRACTS `:122`:** MEASURED now reads *"the accent's primary-action and transient roles"*. DERIVED gains *"the
  accent's IDENTITY role -- the closed set of carriers FWD-4 names"*, and its rule sits beside it: *"exactly the
  closed list Andrew selected 2026-09-14 (PROVENANCE v0.3), extended only by his word"*.
  - **R1's identity half is CLOSED.** The identity role now has exactly one class, and its rule is written beside it.
  - **N2 is closed by the same clause:** "extended only by his word".

## R2 -- "transient roles" under MEASURED includes a value the website does not measure

**The census of the whole MEASURED class**, measured against the file the class cites (`[3/3] rows only`):

| MEASURED member at `:122` | `opalinvest.com.json` | |
|---|---|---|
| canvas `#F4F6FA` | `:12` | yes |
| the accent's primary-action role | `:14` "single action accent", `:79-81` | yes |
| the accent's transient role: the focus ring | `:14` "+ focus ring", `:56-57` | yes |
| **the accent's transient role: the text-selection highlight** | **absent** | **NO** |
| radii 2/3/4px | `:50` | yes |
| no drop shadow | `:54-55` | yes |
| the 2px focus ring | `:56` | yes |
| weights 400/700 | `:31` | yes |
| `letter-spacing: normal` | `:33` | yes |
| the 40/60 split | `:63` | yes |

Nine of ten members are measured; one is not. FWD-4's DONE WHEN puts both *"the ring that follows keyboard focus and
the highlight on selected text"* under TRANSIENT, so "transient roles" (plural) names both. The selection highlight
takes the accent because of brief A23's fix (*"`::selection` uses `--warning` orange, off-palette"*; R5: *"`::selection`
on the accent"*). That makes it a DERIVED design choice. The section's own rule says *"a derived value is never
labelled captured: its derivation rule is written beside it"*, and this value is labelled captured and carries no
rule.

**This residual came through my review, and I say so.** My v0.3 review said the two roles the preamble classes are
*"exactly those two"* the website measures. That was imprecise: the preamble's transient role is two members, and the
website measures one of them. v0.4 followed my wording faithfully. The same gap was in v0.2's text, and I signed v0.2.
The census above is the check that should have run at v0.2 and v0.3. It covers the whole class, not only the member I
was handed.

**The fix, the CTO's to word. One phrase, the same shape as v0.4's:**
- MEASURED: *"the accent's primary-action role and the focus ring"*.
- DERIVED: add *"the text-selection highlight on the accent"*, with its rule beside it, e.g. *"`::selection` takes
  the accent so transient feedback shares one colour (FWD-4; brief A23)"*.

**Sign condition, stated exactly this time:**
- Every member of MEASURED at `:122` has a line in `design/brand/opalinvest.com.json`, so the census above reads 10
  of 10.
- The selection highlight carries exactly one class, with its rule.

Nothing else in this half needs to move.

## NOTES (non-blocking)

- **N3 carries** from the v0.3 review: the identity members' FORM and the accent-share bar are unbounded, and the PROOF
  names every carrier and prints the share.
- **The brief half is `2.0.0_SA_COO~D`'s.** R5's "ACTION count" and the v0.4 provenance entry are in it, and it reads
  STALE at v0.4.

## NOT CLAIMED

- **That the website's selection colour is not the accent.** The file does not measure it either way. R2 is about
  the class label, not the colour.
- **Anything about the RB-s-5 reopen, which is a modification.** LIMB 6 does not fire on it.
