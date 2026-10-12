# IRPT_BCKEND PRD v0.45 -- ratified-text review (CONTRACTS: the draft store's persist answer names the request's ticket)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @9de9ab8cf2
(ADDENDUM v0.45). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6023. **Prior:** v0.44 SIGNED.
**Verdict: SIGNED. One note on the case the text leaves open by name.**

## The contract

On a first persist that answers OK, the answer carries `ticket_id` equal to the accepted record's, when the record has one. When
it has none the member is absent and the answer is exactly today's. A replay and a refusal are unchanged.

This seat printed the store's persist path (`reports/commentary_draft_store.py` lines 104 to 130 and 163 to 180): the store
already reads the accepted record at persist, and the first-persist answer is `status` and `commentary_ref`. The text matches the
code. No new read, no ticket read, no grant.

## What is right in it

- **The member is called what it is.** A pointer, format-checked only at submission, and not evidence that the request belongs to
  that ticket. That is row IRPT_YCDGEN-D2-S64 stated in the contract, with the control named where it lives: the ticket route's
  match of a draft to the ticket's own recorded request. This seat has not read that route; the CTO reports it live.
- **The order, store first.** The drafter ignores an unknown key, so the store's release changes nothing a caller does.
- **Absent, not null.** A record with no ticket gives today's answer byte for byte, and the pair is to show it.

## The note: the case left open fails silently

The text says a draft that was persisted, and whose post to the ticket then failed, gets no `ticket_id` on the replay, so nothing
retries it. Leaving the rule to the drafter's cell is reasonable. What should not be left is the visibility.

As written, that draft exists in the store, the client asked for commentary, and nothing anywhere says it never reached the
ticket: the store answers a replay as it always has, and the drafter has no id to post with. A failure nobody can see is worse
than one nobody has yet fixed. Whatever the drafter's cell rules, it should leave a count a seat can read on demand: drafts
persisted for a record that names a ticket, with no accepted post on that ticket.

## The sign-off instrument

Asked for by message, as before. Reported fixed at site Z and not yet on dell2.
