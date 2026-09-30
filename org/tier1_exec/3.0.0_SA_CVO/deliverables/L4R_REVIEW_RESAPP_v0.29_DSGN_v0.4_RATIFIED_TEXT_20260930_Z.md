# L4-R ratified-text review -- AMGT_RESAPP v0.29 and DSGN_AMGTV1 v0.4 (one re-homing act)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~08:3xZ
**Deliveries:** msgs 27025 (DSGN_AMGTV1 v0.4, half_hash `c0aa855a2ed8`) and 27026 (AMGT_RESAPP v0.29, half_hash `a0ec28b2a3b9`), both
at commit `44d6bc3e31`.
**Span:** from this seat's own signed bytes.
- `prd_signoff_lib.endpoint_hash` on `44d6bc3e31~1` reads DSGN `25db25c6cea4` and RESAPP `b34f9346d6dd`, which equal the hashes in
  this seat's signoff files. The whole ENDPOINT change is therefore commit `44d6bc3e31`.
- At `44d6bc3e31` the hashes read DSGN `186ec21fc20a` and RESAPP `5c8ae74337f5`.

## 1. WHAT WAS COMPARED

RESAPP FWD-21..FWD-29 as signed (the fence text at `44d6bc3e31~1`, including FWD-23's positive-control addendum) were compared
clause by clause with DSGN FWD-12..FWD-20 at `44d6bc3e31`.

The re-homing rule was also checked: where DSGN's ratified endpoint names a different form, that form wins, and every property is
carried.

| RESAPP | DSGN | properties carried | forms dropped | verdict |
|---|---|---|---|---|
| FWD-21 | FWD-12 | band == 1; the identity header is the band (Andrew's F1 word); white hairline tab panels; ACCEPT kept | the three-part Thesis layout and "on one screen", both replaced by DSGN FWD-6's three cards (a named form) | carried |
| FWD-22 | FWD-13 | units, tabular numerals, tooltip carrying the mnemonic and full-precision value verbatim; the six figures each on a named card | Stat tiles, replaced by FWD-4's cards (declared) | carried |
| FWD-23 | FWD-14 | PASS face, passage count, passage and accession FROM THE DOM, the zero title= census WITH the positive control in the same capture (application route, the tab's label, a non-zero denominator) | none. The surface is scoped to "the Thesis windows", which is where DSGN FWD-6 places drafted sentences; the Posture cites ride FWD-17 | carried |
| FWD-24 | FWD-15 | verbatim | none | carried |
| FWD-25 | FWD-16 | verbatim, except the TODAY measurement | none | carried |
| FWD-26 | FWD-17 | comparable beside the verdict; cites folded; the UNRESOLVED cite as an icon plus navy text, not amber | the verdict Stat (declared). Reasons as "numbered cards" becomes "numbered reasons": DSGN FWD-10 names its own form ("numbered reasons that each open to more"), so the rule covers it. **Addendum C's FWD-26 line should list it.** | carried |
| FWD-27 | FWD-18 | verbatim | none | carried |
| FWD-28 | FWD-19 | verbatim, tightened by "on every panel" | none | carried |
| FWD-29 | FWD-20 | the JSON clauses; person-read PNGs with a clause-cited rejection; "the same instrument reads today's page as failing", now in DONE WHEN (stronger) | **"the drafting, tabs and posture harnesses green" is ABSENT from DSGN FWD-20** | **NOT carried** |

## 2. THE DEFECT

- RESAPP FWD-29's DONE WHEN includes "the drafting, tabs and posture harnesses green". It is a mechanical pass condition, and so an
  operative constraint.
- DSGN FWD-20 does not contain it.
- Addendum C declares "FWD-29 -> DSGN FWD-20 ... NO LONGER PROMISED: nothing" and "every PROPERTY is carried. Nothing else is
  dropped." s.C.1 says the same.
- So the clause is dropped without a declaration. Since grading of FWD-21..29 moves to DSGN, nothing would grade it anywhere.

**One-line remedy, either:**
- (a) add "; the drafting, tabs and posture harnesses green" to DSGN FWD-20's DONE WHEN; or
- (b) declare it on the FWD-29 line of Addendum C as no longer promised, with its reason.

Option (a) is this seat's recommendation, because the harnesses are the page's only regression guard for the Thesis, tabs and
Posture paths.

## 3. VERDICTS

- **AMGT_RESAPP v0.29 ratified-text: SIGN.**
  - RESAPP's own text is accurate: each outcome's obligation moves, and the forms it names as no longer promised are forms DSGN's
    ratified endpoint replaces.
  - The defect is in the receiving text.
  - FWD-1..FWD-20, FWD-30, FWD-31 and every contract are unchanged at this commit (checked: the diff touches only the header,
    Addendum C in the fence, and s.C.1).
  - **Condition:** the sign rests on DSGN carrying FWD-29 whole. If option (b) is taken instead, the FWD-29 line of Addendum C
    changes, which is ENDPOINT text, and this half re-opens.
  - Wording note, not a condition: add FWD-26's reasons-as-cards to its line.
- **DSGN_AMGTV1 v0.4 ratified-text: REFUSE.**
  - One operative constraint is missing (section 2).
  - Every other clause of FWD-12..FWD-20 carries its RESAPP property (section 1).
  - Cost of the refusal: none to the schedule. The outcomes enter at round 12, and round 11 is already cut.
- **Authority:** F5 is the CTO's fork ruling @`ac5433b35b` ("presentation moves to DSGN_AMGTV1"), and DSGN's DONE WHEN was
  confirmed by Andrew on 2026-09-29. A form conflict resolved in favour of the page-owner's ratified form is inside that
  authority. No new Andrew-text is invented.
- **Section hygiene:** both fences now carry dated addendum headers and commit references. That matches the precedent in both
  PRDs (RESAPP's FWD-23 addendum and ADDENDUM B), so it is not a ground here.

## 4. DSGN_AMGTV1 v0.4 RE-REVIEW @badff0ef3b (msg 27039) -- SIGN

- `git diff 44d6bc3e31 badff0ef3b` on the DSGN PRD is ONE hunk: FWD-20's DONE WHEN gains "the drafting, tabs and posture harnesses
  green", placed before "AND the same instrument ...". Nothing else in the file moved.
- That is option (a) of section 2, verbatim from RESAPP FWD-29, so section 1's table now reads "carried" on all nine rows.
- **VERDICT: SIGN.**
- Record note, not a ground: the amendment rode commit `badff0ef3b`, whose message is about a different act ("sign(AMGT_CORPUS
  round 23 CRPS-y-4 CTO half)"). A reader following the PRD's history by commit message will not find this change there.
