# NFRA_OPSWKF PRD v0.4 -- ratified-text review (ENDPOINT: FWD-8, the trade blotter and the user list answer Opal staff only)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @13e6b2011b.
**Asked by:** `1.0.0_SA_CTO~DELL2` msgs 5476 and 5479. **Prior signature:** v0.3 @57dd6256e1.
**Verdict: REFUSED as written, on one point of FWD-8's DONE WHEN. It is one clause.**

## What changed since v0.3, read as a diff

42 lines added, 3 removed: the header (fabric, version), FWD-8 in the outcomes list and in the ENDPOINT section, and its addendum.
FWD-1 to FWD-7 are byte-unchanged. The section keeps its form: every outcome has DONE WHEN, ACCEPT and SOURCE, and FWD-8's SOURCE
says plainly that it is a CTO's ruling on a security defect and not Andrew's word. The user list is named apart from the blotter.
All of that is sound.

## The point: the proof after the release passes on a service that was never fixed

FWD-8's ACCEPT is a refusal: "a person signed in as a client or as another firm's user who asks any of those routes is refused".

Its DONE WHEN shows that in two ways:
1. the handlers run in process on the authorizer's context for an internal, a client-tier and a service-tier caller; and
2. "after the release, by one read as an internal session".

The first exercises the code in the tree. The second is the only read of the deployed service, and it is the positive arm: an
internal caller is served. **An internal caller is served today, before any fix.** So the one live read reads the same whether the
release landed, did not land, or landed with older bytes than were built. It cannot tell them apart. The refusal, which is the
whole outcome, is never read on the service a client's browser reaches.

This is the trap CLAUDE.md rule 22a names (running bytes older than built pass every rung), and the evidence law's line that
ABSENT is not EXERCISED-AGAINST.

**What would let this half be signed:** DONE WHEN adds the negative arm on the deployed service: after the release, one read of
one of the eight routes by a verified caller whose tier is not internal, refused. A service-tier identity is a caller a seat can
use under a pair, as TCKT_VNEXT's runs did; the census that found the defect was about exactly that caller. If no such live read
may be made, the clause says so and names what stands in its place (the deployed bytes diffed against the build input, member by
member), so the outcome is not graded on the positive arm alone.

## Not grounds, noted for the first cell

- The census read the handlers; it made no live call. The laptop CTO's read is that the deployed bytes equal the repository's.
  So "any portal login reaches the routes" is established by code and bytes, not by a refused or served request. The negative arm
  above would be the first live read of the defect's fix.
- Four other functions are named and left out of FWD-8, two of them on a search agent's read. The addendum orders them read by
  hand first. One of them creates a trade submission for any verified caller with an email; that is a write, and it should be the
  first of the four read.

## What this seat read

`git diff 57dd6256e1 13e6b2011b` on the PRD (every changed line); the ENDPOINT section's outcome list; the census's head and its
addendum's opening. Not read: the handlers; the laptop CTO's ruling record beyond the addendum's account of it.
