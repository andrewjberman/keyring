# ADVI_COTBKF PRD v0.10 -- ratified-text review (CONTRACTS: C-BASIS, the basis value against the split scaling)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` @4d488ab2f0
(ADDENDUM v0.10). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6374. **Prior:** v0.9 SIGNED with this as its note.
**Verdict: SIGNED. Two things the signature rests on that nobody at this desk has read.**

## What changed

v0.9 said the value `as_traded_close` means the traded price only after this build's split scaling, and that a point which has
not passed the scaling is not written with the value. This seat's note asked where the scaling sits against the substitution.
The read was made, and the answer is that v0.9's sentence described a build that does not exist: the value is written before
the split plan runs, the split step records nothing per point, and a point can leave marked with the value and unscaled on 9
of 11 paths (the worker's count, the lines read by the issuer).

v0.10 withdraws the sentence and says what is true:

- the value says where a point came from, not that it is the traded price;
- under C-BASIS a fund point comes from one source, another box's as-traded column, which is stated to have later splits already
  undone, so the point is the traded price and this build's split step is NOT applied to it;
- applying it would scale the same split twice;
- the cached vendor close is no longer a source for a fund point, so in what C-BASIS mints the value has one meaning.

The proof's split arm is replaced to match: a fund that split, priced on both sides of the split, reproduces the price paid, and
the count of fund points this build's split step changed is zero.

That is a contract corrected on a measurement, by the seat that wrote the wrong sentence and doubted it. It is signed.

## The two things it rests on

1. **That the other box's column has later splits undone.** This is that box's ruling, relayed, read by the two issuers and by
   neither the CTO nor this seat. The whole of item 2 turns on it: if the column were split-adjusted like the vendor's close, not
   applying this build's split step would leave a split fund priced wrong, the mirror of the double scaling. The proof's arm (a)
   is the control, and it is the right one: the price paid on both sides of a split.
2. **Arm (b) leaves that untested if no held fund split.** Then the run reports the count searched and the property of the column
   stands on the other box's word alone. That is acceptable for funds that did not split, because for them the question does not
   arise. It should be said in the result in those words, and not as a pass of the split arm.

## One thing left open by the text itself

For security types C-BASIS does not re-price, the value keeps today's meaning with the limit just measured: it does not record
whether the split scaling reached the point. The addendum calls that "row material". This seat has not seen the row; if the
round's packet does not carry one, it is filed at the compile.
