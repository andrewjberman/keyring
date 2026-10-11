# IRPT_BCKEND PRD v0.37 -- ratified-text review (ADDENDUM v0.37, a second witness of the date basis)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @8c12f97cc4.
**Asked by:** `1.0.0_SA_CTO~DELL2` msg 5275.
**Verdict: REFUSED as written, on two points. The first is substance, the second is one sentence.**

What is sound, and stays: a witness never supplies a served figure; the set of witnesses is closed at two; a security with no ticker
stays `OUTSIDE_ANCHOR`; the cost is given as a sizing with nothing stamped; the witness is fetched on a schedule. This seat's census
agrees: `date_basis_witnesses`, `SCHWAB_ANCHOR` and `YAHOO_CLOSE` occur in 0 tracked files of the three trees.

## Point 1: the safety argument leaves out the one error that is not chance

The addendum says: "an error in a witness has one safe direction and one unlikely one: a wrong close blanks a day; to pass a day
wrongly it would have to equal the source's own mark within 1e-4 by chance."

That is true of a wrong PRICE. It is not true of a wrong DATE. The whole question a witness answers is which day a mark belongs to.
If the reader labels a fund's net asset value one day off, the mark that truly sits at the prior close equals the reader's bar for
day t exactly, every time. The day is then stamped `ACCT_OWN_DATE` and served, on the wrong basis, systematically and not by chance.

Nothing in the read tests the reader's date labels for the securities this witness is for:

- The one control is VTI, an exchange-traded fund that the first witness also carries (the record's line 40, printed by this seat).
  It shows the reader's dates are right for a security that trades on an exchange.
- The securities the second witness is wanted for are mostly mutual funds: the top ten behind `OUTSIDE_ANCHOR` are mutual funds
  (the round 133 packet). A fund's value is struck after the close and published late. No fund in the read is carried by both
  witnesses, so no fund's date label was compared with anything.
- The earlier read says so in its own words: the claim that the reader's Close is that day's value is `inferred`, because no second
  public source was allowed (the rounds 133 and 134 packet).

So for funds the date basis would rest on the label of the witness, and ENDPOINT FWD-3, as v0.34 put it, "is not met by a basis
nobody measured".

**What would let this half be signed:** the text names the date-label risk beside the price one, and makes `YAHOO_CLOSE` a witness
only for a class of security whose date labels have been measured against an independent dated source. Exchange-traded securities
have that today by the overlap with the first witness. For mutual funds the addendum names the check that admits them (a sample of
funds and dates against one independent dated value) and says that until it is read, a fund stays `OUTSIDE_ANCHOR`.

## Point 2: the text does not say which witness grades a security both carry

A security can have a close in both witnesses (VTI does). The addendum says a row "sits at a close when it equals the witness's
close" and that `date_basis_witnesses` lists "the witnesses used". It does not say which one is used when both hold a close, nor
what the row reads if they disagree. The read used the first witness wherever it has the security and the second only elsewhere
(the record's line 26, printed). The contract should say that.

**What would let this half be signed:** one sentence: `SCHWAB_ANCHOR` grades every security it carries; `YAHOO_CLOSE` grades only
a security the first does not carry.

## The gate

`prd-signoff.py status IRPT_BCKEND` read this half SIGNED and current at v0.37 before this review, on the v0.36 signature. The
delivery came by message.

## What this seat read

The addendum in full (the PRD from its v0.37 heading); the record `deliverables/0.9.0_WK_IRPT_BCKEND~296/IB136-1_ALL_SECURITIES_NAV_EFFECT_READ.md`
at lines 3, 13, 22, 26, 33, 38 and 40, and a search of it for any check of date labels, of an overlap between the witnesses, or of
a second source (none found in its 42 lines). Not run: the read itself.
