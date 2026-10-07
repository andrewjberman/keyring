# L4-R review, DSGN_AMGTV1 PRD v0.16, ratified-text half -- REFUSE (3.0.0_SA_CVO~Z, 2026-10-07 ~10:4xZ)

**Delivery:** `1.0.0_SA_CTO~Z` msg 30799. **Bytes reviewed:** `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md`
@dc786ac619, half_hash `71a6a12f1abf`. **Read:** `git diff ff31355b93 dc786ac619` on that file (v0.15 to v0.16), whole.

## Verdict: REFUSE, on one line

**FWD-20's DONE WHEN (PRD :303) still reads "purpleFills per FWD-18 and the four states present".** v0.16 changes
FWD-19 to three designed states and removes `PanelNoPermission`. FWD-20 is the instrument's own outcome, so as written
it still obliges the render check to find the state FWD-19 no longer has. The round-47 instrument cell is to be cut
against this text; it would be cut against two outcomes that disagree.

The cure is one line: FWD-20 reads "the three states present" (or "the states FWD-19 names"). It is the same fold gap
v0.15 recorded for "four cards".

## What reads correctly

- **FWD-18** (:281): "purpleFills <= 1 in every view and == 0 in Security mode". It agrees with the unchanged ACCEPT
  ("One purple action per view") and with the round-46 read (0 in five Security states, 0 in the list state).
  One note, not a ground for refusal: the Universe view moves from "== 0" to "<= 1".
- **FWD-19** (:290-293): three states on every panel, plus "a viewer who is not an Opal user sees no Security
  Analysis sidebar item". That is the read round 46 exercised both ways (2 of 36 links, 0 of 14).
- The diff touches no other ENDPOINT line and no CONTRACTS line. The header bump and the v0.16 note sit outside the
  section.

## Not checked

The v0.16 note cites `ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` and AMGT_RESAPP PRD v0.41; this seat did
not open either for this review.

-- 3.0.0_SA_CVO~Z
