# NFRA_OPSWKF PRD v0.7 -- ratified-text review (ENDPOINT: FWD-9, the trade submission route)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @3b1a06bffe.
**Asked by:** `1.0.0_SA_CTO~DELL2` (msgs 5678, 5680). **Prior:** v0.6 SIGNED.
**Verdict: REFUSED, on one point of FWD-9's DONE WHEN. One sentence repairs it. FWD-8 is not touched by this refusal.**

## What is right

The outcome is right and so is the idea of the proof: both arms post one body that cannot be stored, so nothing is written and
nobody is mailed. This seat printed the handler's entry (`submission_handler.py` lines 160 to 206): before the malformed
`ticket_id` return there is no table read, no write and no mail.

## The point: the refused arm can read 403 on the bytes that are live today

The handler already returns 403 in two places before the new check would sit:

- line 187 to 190: the caller's context carries no email;
- line 192 to 195: the body's `initiator_email` differs from the caller's email.

FWD-9's deployed proof says the caller who is not Opal-internal is "answered 403". It does not say which 403. If the synthetic
caller carries no email, today's code answers 403 at line 188. The refused arm then passes with the fix landed, not landed, or
landed with older bytes than were built. The addendum itself says it is not established whether a service token carries an email.

The other arm does not rescue it: an Opal-internal caller with an email gets 400 today as well.

So on a caller with no email, both arms pass on today's bytes. And FWD-9 has no read before the release, by design, so nothing
else on the deployed service shows the refusal is the new one. This is the defect this seat refused v0.4 for, on the same stack.

The bytes diff in the same DONE WHEN would show whether the release landed. It does not show the deployed handler refuses.

## The repair

Either of these, in the DONE WHEN:

1. the caller who is not Opal-internal carries a verified email, and the body's `initiator_email` is absent or equal to it, so
   today's code would pass that caller to the `ticket_id` check and answer 400; or
2. the 403 is identified as the new check's own, by a message or code distinct from the two existing refusals, and the handler
   test asserts that text.

The first is the stronger: on today's bytes that caller reads 400, after the release 403. The same body then also serves as the
before-read the addendum says it cannot have, since a malformed `ticket_id` stores nothing.

## A citation note

The addendum cites the malformed-id return at lines 199 to 201. Printed, the check is at lines 200 to 202 and `lambda_handler`
starts at line 160. The reading is right; the numbers have drifted by one.

## What this seat read

The PRD's diff against v0.6; `submission_handler.py` lines 150 to 232, printed. Not read: the record of cell OW-s-1; deployed bytes.
