# IRPT_BCKEND PRD v0.48 -- ratified-text review (CONTRACTS: C-CHAINCLAIM, when a chained figure may say measured)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @a4cdeb6232
(ADDENDUM v0.48). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6413. **Prior:** v0.47 SIGNED.
**Verdict: SIGNED, because the contract only narrows what may say `measured`. One point on the status the CTO asked to have
attacked, to be settled by the read already ordered before the cell.**

## What it does

Today the performance reader drops every day that is not OK, chains the rest, and says `measured`. The contract makes the claim
depend on the STATUS of each dropped day, wherever it sits: two statuses mean there was no base to earn a return on and keep
`measured`; every other status, named or not yet seen, means a return was left out and the figure says `inferred`. The answer
gains two counts. Figures do not move; a served claim does, so it ships under a pair with the accounts whose claim moves.

Three things are right in the shape:

- **The default is the safe one.** The rule lists what keeps `measured` and sends everything else, including a status nobody has
  seen, to `inferred`. A claim field must be able to say less than it hopes.
- **Position decides nothing.** One rule for a first, interior or last day.
- **It only narrows.** Every figure this touches says `measured` today. After it, some say `inferred` and none gains a claim.
  That is why this is signed with the point below open and not refused on it.

## The point: `NON-POSITIVE-BASE` is on the measured side on a definition, not on a measurement

The addendum states the limit itself: a zero base is the INCLUDED BASKET being zero, not proof the account was empty. And it
shows the limit is real: 118 days are accounts that held securities, every one of them excluded. Those carry their own status
and go to `inferred`, rightly.

The question the text leaves is whether the 637 `NON-POSITIVE-BASE` days are all the other kind. They are on the measured side
because of what the product's definition of the base says, not because anyone counted what those accounts held the day before.
If the producer assigns `ALL-HOLDINGS-EXCLUDED` whenever an account holds something and all of it is excluded, then
`NON-POSITIVE-BASE` can only mean nothing of value was held, and item 2 is right. If the two statuses are assigned by a
precedence that can leave an account holding an excluded position under `NON-POSITIVE-BASE`, then some of the 637 had a return
that the figure leaves out, and it would go on saying `measured`.

That is the unsafe direction for a claim, and the estate's own rule is that a value with no field establishing it may not be
treated as measured.

**It is one count, and the read before the cell can carry it:** of the `NON-POSITIVE-BASE` days, how many accounts held ANY
position row, included or not, on the prior day; and from the producer's code, the order in which the two statuses are assigned.
If the count is zero and the order makes it so by construction, item 2 stands as written. If not, `NON-POSITIVE-BASE` keeps
`measured` only where the account held nothing, and the rest falls to item 3.

## Two smaller notes

- 33,472 non-OK days at one firm follow an account's last OK day and were outside the worker's day rule. The contract's rule
  covers them by status; the pair's count of accounts whose claim moves should include them or say why not.
- No page shows the claim today. Until one does, `inferred` changes the answer and nothing a person sees. That is ruled out of
  scope here and placed with another project; it should not be forgotten once this is live.

## What this seat read

The addendum only. No code and none of the three worker records.
