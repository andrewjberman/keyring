# ADVI_COTBKF PRD v0.9 -- ratified-text review (CONTRACTS: C-BASIS item 2, the basis field is the build's existing one)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` @95da777fbf
(ADDENDUM v0.9). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6280 and its message. **Prior:** v0.8 @118f800793 (REFUSED).
**Verdict: SIGNED. One note on a value whose meaning is tightened.**

## The repair is better than what was asked

The refusal asked for a census, a mapping, and a sentence on splits around two new tokens. v0.9 withdraws the tokens. The basis
is the per-point column the build already writes, with the two values it already has.

This seat printed `commonwealth_daily_valuation.py` lines 186 to 192, 209 to 212 and 246 to 260: the input carries a `basis`
column; its values are `as_traded_close` and `store`; every point starts as `store` and a substituted point is given the other.
The text matches the code. Nothing is minted that the build did not already say.

The three points of the refusal, each answered:

- **The collision is gone.** The upper-case token in the served blank reason is left alone and no field reuses it.
- **The four series classes are placed:** they class a whole series, are never written to the minted table, and stop deciding what
  is substituted for a fund. The addendum names that decision as the mechanism of the defect: the 15 failing funds were classed
  `other`, so they kept their store points. Under C-BASIS every fund is substituted whatever its class.
- **Splits are in the meaning:** `as_traded_close` means the traded price only after this project's split scaling, and a point that
  has not passed it is not written with the value. The proof gains an arm for a fund that split.

The census is given with its counts and with what was not searched. `store` is honestly defined: what it does with distributions
is not known for that point, and for a fund it prices nothing.

## The note: the value is not new, but its meaning is now stricter than the rows that carry it

`as_traded_close` is written today wherever a store point was replaced by the vendor's close. The comment above the code says
that close is split-adjusted only. v0.9 says the value means the traded price only AFTER split scaling. So the contract now
promises something of every row carrying the value, and whether the rows written so far keep that promise depends on where the
split scaling sits in the build relative to this substitution. This seat did not read that.

It matters beyond funds. The column is per point for every security type, and exchange-traded securities split far more often
than funds do. The proof's split arm is cut for a fund. The build's cell should show, for every security type, that a point is
given `as_traded_close` only after the scaling, or the value's meaning should be stated as holding for funds only until that is
shown. One count settles it: points carrying the value on a date before a known split of their security, with and without the
scaling applied.
