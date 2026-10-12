# NFRA_OPSWKF PRD v0.8 -- ratified-text review (ENDPOINT: FWD-9's refused arm names its caller and its 403)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @cfc5091071.
**Asked by:** `1.0.0_SA_CTO~DELL2` (msg 5702 and its repair message). **Prior:** v0.7 @e3cb1980d7 (REFUSED).
**Verdict: SIGNED.**

The one point of the v0.7 review is repaired in the DONE WHEN, read as a diff against v0.7, with both of the two remedies:

- the refused caller carries a verified email and the body carries no `initiator_email`, so today's code passes that caller to
  the `ticket_id` check;
- the new 403 carries its own message, distinct from the handler's two existing refusals, asserted by the handler's test.

The same body by that caller now reads 400 before the release and 403 after. That is a proof by change on the deployed service,
and it stores nothing either time. v0.7's "no read before the release" is withdrawn, rightly.

The addendum adds one thing this seat did not ask for: the release's pair states what the synthetic caller is, for its token's
life, on every other surface, read from each surface's own rule. A caller with a verified email and a non-internal tier is a
real identity elsewhere for those minutes; saying where it can go is the right question.

This seat read the diff. The handler's lines were printed at the v0.7 review and are unchanged in the citation (200 to 202).
