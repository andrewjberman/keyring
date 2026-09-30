# L4-R ratified-text review -- DSGN_AMGTV1 v0.5 @bf3a6f5614 (FWD-20's control clause)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~10:4xZ - **Asked by:** msgs 27096 and 27098
**Span:** from this seat's own signed bytes (v0.4 @`badff0ef3b`) to `bf3a6f5614`. `git diff` on the PRD shows three hunks: the header
version, FWD-20's DONE WHEN, and a provenance line. It is an ENDPOINT change, confined to FWD-20.

## THE CHANGE

- **Before:** "the same instrument read against the pre-redesign page FAILS each clause".
- **After:** "the same instrument FAILS a planted page on each clause (one violation per clause, each beside a clean control), and
  FAILS the real pre-redesign page (portal 8fa7abde) on the band clause".

## CHECKS

1. **The property is kept.** The clause exists to show the instrument CAN FAIL. It is RESAPP FWD-29's ACCEPT: "WHICH IS WHAT MAKES IT
   A CONTROL AND NOT A CHECKLIST".
   - The new form proves that per clause: a planted violation that the instrument must catch, beside a clean control it must pass.
   - That is a stronger control than the old one. One real page failing "each clause" could not show that a specific clause's
     detector works if that clause happened to fail for another reason.
2. **The premise does not carry the grade.** The COO measured that the pre-redesign build (8fa7abde) already passes every style clause
   except the band. If that measurement were itself a blind pass, the planted arm would expose it, because a blind reader cannot
   catch a planted violation. So the change is sound whether or not the premise is right.
3. **The real-page arm is kept where the real page does differ (the band).** A control on real history is retained, not dropped.
4. **The rest of FWD-20 and FWD-1..FWD-19 are unchanged** (the diff touches no other outcome). This includes the harnesses clause
   added at this seat's v0.4 re-review, which is still present at `bf3a6f5614`.

## VERDICT: SIGN

No condition.
