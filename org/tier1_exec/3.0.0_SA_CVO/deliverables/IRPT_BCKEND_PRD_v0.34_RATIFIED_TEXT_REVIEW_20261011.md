# IRPT_BCKEND PRD v0.34 -- ratified-text review (ADDENDUM v0.34, Cottonwood's date basis per account-day)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @e7c6ab606f.
**Verdict: REFUSED as written, on two defects of the text. Both are repairs of wording, not of the rule's direction.**

The rule's direction is sound and fits the ENDPOINT, which is unchanged: a return is served for an account-day only when the day
and the prior trading day are each on the account's own date or hold nothing the date basis can move. Nothing is shifted or
inferred from a neighbour. The cost is stated (25.0 percent of eligible account-days blank; 169 of 999 accounts never served).

## Defect 1: `OWN_DATE` admits a day nobody fully measured

The addendum defines `OWN_DATE` as "every GRADEABLE moved security of the account that day sits at its own date's close". An
account-day that also holds a priced security the instrument cannot grade (outside the anchor, no CUSIP, a negative position) and has
no row at neither close is therefore `OWN_DATE`, and is served.

The read the addendum rests on says so in its own "Not measured" list
(`deliverables/0.9.0_WK_IRPT_BCKEND~288/IB127-1_ACCOUNT_DAY_CLAIMS_READ.md` line 82, printed by this seat): "Whether an OWN_DATE day
also holds an ungradeable row; it is claimed OWN_DATE." Its rule (line 9) makes a day not-graded only when no moved row is gradeable
or a row sits at neither close.

That contradicts the addendum's own sentence: FWD-3's "that account's own end-of-day holdings" "is not met by a basis nobody
measured". On such a day part of the value is on a basis nobody measured, and the day is served with the claim `OWN_DATE`.

**What would let this half be signed:** either (a) an account-day holding any ungradeable priced security is `UNGRADEABLE`, whatever
its other rows read, and the blank share is re-counted under that rule; or (b) the text says such a day is served, says why that
meets FWD-3, and carries the count of such days. The count is not known today.

## Defect 2: the closed kinds of `UNGRADEABLE` do not hold a case the same addendum creates

The addendum lists four kinds: a priced security outside the anchor, a position with no CUSIP, a row at neither close, a negative
position. Its "daily order" paragraph then says "A day graded before its anchor lands is `UNGRADEABLE`". That day has none of the
four kinds. A producer following the text must either invent a fifth kind or mislabel the day as one of the four.

By rule 24, postulate (i), a closed set is checked by subtraction from its domain. The domain here includes the not-yet-anchored
day, and the set does not cover it.

**What would let this half be signed:** a fifth named kind for the anchor not yet landed, or a sentence that such a day is not
stamped at all until the anchor lands.

## Two smaller points, not grounds by themselves

- **Precedence is in the worker's record, not in the text.** The record orders the claims (a neither row first, then prior close,
  then own date). The addendum's four bullets do not say which wins when a day fits two. A reader of the PRD alone cannot tell.
- **The value-enum arrives without its rule-24 record.** `date_basis_claim` and its kinds are a new closed vocabulary. The addendum
  cites three reads and no four-postulate record or token census.

## A finding about the instrument, for the gate's owner

The addendum's heading says "CONTRACTS changed: the ratified-text half re-opens". `python .tools/prd-signoff.py status IRPT_BCKEND`
read, before this review, `ratified-text SIGNED 3.0.0_SA_CVO current` at v0.34. This seat's last signature is on v0.33 @13ee60595d.
The half's hash is taken over the ENDPOINT and CONTRACTS sections; an addendum appended below them changes the contract in substance
and leaves that hash where it was. So the gate read a signature on text the signer had not seen. This review was made because the
issuer's packet (msg 4965) said the half re-opens, not because any instrument asked.

## What this seat read

The addendum's 30 lines (`git show e7c6ab606f`); the worker's record at lines 5 to 82; the signature file
`prd/signoff/3.0.0_SA_CVO.json`. Not read: the instrument's code; the gold's producer (none is built).
