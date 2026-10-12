# TCKT_VNEXT PRD v0.4 -- ratified-text review (CONTRACTS: C-FENCE, an internal caller the users table does not know is refused)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` @8bb81f8d6c
(ADDENDUM 3). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6087.
**Verdict: SIGNED. One point for the release's pair, on who else is classed internal.**

## The rule, against the code

This seat printed `ticket_center/lambda_function.py` lines 300 to 333 and 362 to 402. The addendum describes the code exactly:
for an internal caller the firm scope is read from the caller's own PROFILE row; more than one row refuses; a lookup that fails
refuses; a malformed list refuses; and no row at all returns no scope, which reads every firm. The one case in which the service
knows nothing about the caller is the one it admits without a fence. The addendum turns that case into a refusal with the same
answer as a failed lookup.

It is the control arm of this seat's own grade of round 6: an internal caller with a made-up address and no row was served.

## The point the CTO asked to have attacked

A row with no firm list, or an empty one, still reads every firm. The text says so, says it is how all-firm staff are represented
today, and rules nothing on it. That is acceptable as a stated limit: it is a known row, where the case being closed is an unknown
caller. It deserves its own row because "empty means all" is the kind of default that later reads as an accident.

## One point for the pair: every caller classed internal, not only people

The addendum says who this can touch: a constructed event, a row deleted after its token was issued, an address that does not
match its row. And the pair counts that every active internal USER has one PROFILE row.

The code classes a caller internal by one test: the firm id is Opal's and the caller is not a service subject (lines 312 to 328).
A service subject is classed first and never reaches the scope lookup, so the three named service callers are untouched; read by
this seat. What the count should also cover is any NON-HUMAN identity that carries Opal's firm id without the service marker: a
test filer, a packager, a job. Such a caller with no PROFILE row is served today and would be refused after the release, and no
person would notice until its path ran. Earlier records of this estate name at least one synthetic caller with Opal's firm id.
This seat did not list them; the pair should, from the token issuers, before the apply.

## The proof

Served before and refused after for a constructed internal caller with no row; and a twin whose address already has a row, served
after, with no row written for it. Both arms, by the instrument used for FWD-2. Sound.

Row D2-S46 stays ARMED, as the text says: this narrows what a made-up internal caller gets; it does not narrow who may invoke.

## The sign-off instrument

`prd-signoff.py status` read this half SIGNED and current before this review (printed by this seat). Asked for by message.
