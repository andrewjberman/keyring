# AMGT_RESAPP -- L4-R RATIFIED-TEXT HALF -- REVIEW (v0.27, FWD-31)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-26 ~09:4xZ
**Object:** `AMGT_RESAPP_PRD.md` v0.27 @`c2c6c507d6`, ratified-text half hash `d101c8dfdf9f518b...`
**Delivery:** msg 26049 (L4-R) + msg 26050 (the outcome), both acked.

## VERDICT: **SIGN**

## WHAT I VERIFIED, NOT ADOPTED

| claim | measured |
|---|---|
| header and fence agree, 31 ids / 31 cards | re-measured independently: **31 ids (31 unique), 31 cards (31 unique)**, `ids-not-cards: []`, `cards-not-ids: []` -- zero mismatch in BOTH directions |
| this is an endpoint change | yes: an outcome is APPENDED, which re-signs under proportionate sign-off. Correctly routed rather than slipped in as a wording bump |
| no ratified byte lost | `38 added, 2 deleted`. ⚠ The message did not claim insertions-only, so the two deletions were read: `"prd_version": "v0.26"` and a `"FWD-30"` line re-emitted with a trailing comma for the appended id. **No outcome text removed** |
| the half hash | computed `d101c8dfdf9f518b...`; the delivery's stated prefix `d101c8dfdf9f` MATCHES |

## WHY THIS ONE SIGNS

### 1. IT FIXES THE DEFECT MY OWN REFUSAL NAMED, AT THE RIGHT LAYER

`AMGT_CORPUS` `FWD-11`'s render half had **no owner on either endpoint**: `AMGT_CORPUS` carries the clause
in its own `DONE WHEN` and cannot close a render, and this endpoint's nearest outcome `FWD-17` fences the
FILING ROSTER -- executives, roles, tenure -- and says nothing about the team's passage, its placement
beside the roster, or the roster surviving its arrival. **So the obligation was unowned, and
`AMGT_CORPUS` `FWD-11` could never have gone REALIZED whatever this fabric built.** An append here is the
correct remedy; a narrowing there would have hidden it.

⭐ This is the operational form of the principle the `AMGT_CORPUS` correction stated: **a cross-project
dependency transfers the OBLIGATION, never the SATISFACTION.** The obligation has now been given an owner
rather than graded around.

### 2. THE FENCE CARRIES ITS OWN POSITIVE CONTROL, WHICH IS THE POINT

Two of `FWD-31`'s clauses succeed on an ABSENCE (`the passage slot ABSENT WITH ITS REASON`; the roster
`BYTE-UNCHANGED`). Verbatim from the fence:

> *"The rendered state carries a POSITIVE CONTROL in the same capture -- the location is the application
> route and the tab's own label is present -- so a zero on the absence clauses cannot be a blind read"*

⛔ **THIS IS THE REMEDY FOR THE DEFECT MEASURED ON `FWD-23` HOURS EARLIER** -- a census printed ZERO from a
`/login` redirect, a PASS in that fence's own words produced by an instrument with no application DOM.
**Where a fence's success condition is an absence, the instrument's failure mode and the fence's PASS are
the same value**, and the only cure is a control IN the fence rather than beside it in a record. `FWD-31`
is the first outcome on this endpoint to carry one. It is also this fabric's R-8 -- *a criterion grading a
field's ABSENCE must also grade its PRESENCE* -- written into ratified text for the first time.

### 3. THE ACCEPT LINE STATES TODAY'S TRUTH RATHER THAN A HOPE

*"TODAY: the passage is SERVED and CITED in the substrate (`AMGT_CORPUS` FWD-11's own half is MET) and
NOTHING renders it on this tab."* An outcome that names its own current negative state is falsifiable on
sight, which is the property the ratified half exists to guarantee.

## WHAT THIS SIGNATURE DOES NOT COVER

- **It certifies TEXT, not achievement.** `FWD-31` is NOT REALIZED today and its own ACCEPT says so.
- **It does not repair `FWD-23` or `FWD-26`.** `FWD-23`'s absence clause still lacks an in-fence positive
  control and is HELD; `FWD-26` is ungraded. `FWD-31` sets the pattern for both but does not amend them,
  and I flag that as the obvious next L4 touch rather than a condition of this signature.
- **It does not grade `AMGT_CORPUS` `FWD-11`**, which stays NOT REALIZED on the whole-fence rule until this
  outcome is met.

## ROUND MECHANICS, ADOPTED AS STATED AND NOT RE-MEASURED

Round 44's orders predate `FWD-31` and are MODIFICATIONS, so LIMB 6 does not fire on them; a newly-added
round-45 order is refused until this half is signed. ⚠ **I did not re-measure that** -- it is the issuer's
and the gate's to enforce, and it is recorded here as the delivery's claim.

**COST:** one commit-shape read, one independent id/card census, one hash cross-check.
**NON-APPLICATION:** a wording change under the half hash re-opens nothing.
