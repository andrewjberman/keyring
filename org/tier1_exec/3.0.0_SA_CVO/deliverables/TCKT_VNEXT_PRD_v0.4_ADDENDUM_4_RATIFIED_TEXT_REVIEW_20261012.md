# TCKT_VNEXT PRD v0.4 ADDENDUM 4 -- ratified-text review (CONTRACTS: C-FENCE, the users row must be active)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` @fc2100e1e2
(ADDENDUM 4). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6235. **Prior:** ADDENDUM 3 SIGNED by this seat @b667a5fb11.
**Verdict: SIGNED. One note.**

## The gap, and it was in what this seat signed

ADDENDUM 3's contract sentence asked only that a PROFILE row EXISTS. A caller presenting the address of a DISABLED row is
admitted. This seat reviewed that sentence, printed the code beside it, and did not ask what a row's status does. Through the
portal the gap is bounded by sign-in; by direct invoke it is not.

## The rule

The internal caller's one PROFILE row must carry `status` exactly `active`; any other value, and an absent one, is refused with
the same answer as a failed lookup. It can only refuse more. The value set was read whole: `active` 54, `disabled` 2, of 56, none
absent. It locks out two rows, both already refused at sign-in. The four postulates are answered in the text: one remedy moves
disabled, absent and unseen together and does not move active.

The proof is the round 7 shape with the right two changes: a refused arm that is served before and refused after, and a served
twin that is a non-human active row, never a person's address.

## Not read, and said by the text itself

The CTO read the slug, not the applier's findings file and not the sign-in code. This seat read neither either. "The same test
sign-in applies" therefore rests on the applier's read of 11 code files.

## The note: two checks that must stay one test

The rule is defined as "the same test sign-in applies", and it will live in a different function from sign-in. Today both read
one value set of two members. If sign-in is ever changed to admit another value, or to compare differently, this check refuses
staff that sign-in admits, and nobody learns it until a ticket page fails for a signed-in person. The pair should say where
sign-in's test is, by file and line, so the next change to either is made with the other in view; and the count the CTO ordered
(active rows with the internal firm id on a domain that is not Opal's) should come back before the release, since an active row
of that shape is admitted by this rule as it is by every other.

## The sign-off instrument

The fixed tool flagged this half's text as changed since signed, before this review. That is the tool doing what it could not do
this morning.
