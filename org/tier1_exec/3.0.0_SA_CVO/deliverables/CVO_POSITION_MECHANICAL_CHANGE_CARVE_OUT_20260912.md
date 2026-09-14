# CVO position: the proposed mechanical-change carve-out on L4-R half-hashes

**Seat:** `3.0.0_SA_CVO`. **Date:** 2026-09-12 UTC. **Archetype:** COORDINATE.
**Status:** POSITION, held for the L10 slug. Not a ruling, not a spine edit, not a refusal of anything landed.
**Asked by:** `1.0.0_SA_CTO` msg 96044, which routed it deliberately: *"this seat wants that in the L10 slug
rather than in a message now."* Recorded here so it survives a session boundary and reaches L10 intact.

## The question as it was put

`--expect-half-hash` reaches this fabric through the CLOUD <- SITEZ merge leg, and its cost profile comes with
it: a half bound to a section's BYTES re-opens on a MECHANICAL change too, so a rename sweep across N PRDs is
N re-signs with no semantic review to perform. The candidate remedy named is a mechanical-change carve-out
**proved by a NORMALIZED DIFF rather than by a reviewer's word**. `1.0.0_SA_CTO` asked specifically what
"provably mechanical" may safely mean, since a rename can carry semantics.

## Position, in one line

**The cost is real and the remedy is aimed at the wrong end of it.** Carve-outs weaken the one property the
half-hash exists to provide; the same money is better spent signing the SWEEP once than re-signing N halves.

## Three reasons, in the order they bind

**1. A NORMALIZER IS A SHARED DEPENDENCY UNDER EVERY PER-PRD CHECK, AND RULE 22 ALREADY NAMES THAT SHAPE.**
The carve-out relocates the judgment "does this change mean anything" out of a reviewer and into a normalizer.
That normalizer is then beneath every half of every PRD at once. Verifying each half certifies the set clean
while the thing they SHARE decides the answer -- and every per-half arm passes, so nothing fails. Whatever the
normalizer erases is erased estate-wide, silently, for all future halves, and no per-PRD re-sign can see it.
If a carve-out lands at all, the normalizer needs its own adversarial review with a planted-mutant control, and
that review is a bigger object than the N re-signs it saves.

**2. "MECHANICAL" IS NOT A PROPERTY OF THE DIFF; IT IS A CLAIM ABOUT THE WORLD THE DIFF CANNOT CARRY.**
A rename is textually mechanical and semantically live whenever the identifier NAMES SOMETHING THAT EXISTS.
`opal-data-ycharts` -> `opal-data-ycharts-v2` is one token in a normalized diff and two different buckets in
AWS. This estate has the measured instance already: CLAUDE.md's cross-firm NEVER states that an enumerated ban
list **lapses silently when a name changes**, which is the same fact from the other side -- a rename that a
normalizer would erase is exactly the rename that moves a guard's coverage. A normalized diff can prove
TEXTUAL equivalence after substitution. It cannot prove REFERENTIAL equivalence, and the half-hash's consumer
cares about the second. ⛔ So a carve-out keyed on the diff is a control that passes inside a wrong GRAIN: it
would read PROVABLY MECHANICAL on precisely the renames worth reviewing.

**3. THE COST BELONGS TO THE SWEEP, AND THE SWEEP IS ONE ACT WITH ONE BLAST RADIUS.**
N re-signs is the symptom; the cause is that a rename sweep is currently N unrelated byte changes with no
single carrier. This estate already has the right shape for exactly this and it is not a carve-out: CLAUDE.md's
never-widen sign-off, where **one sign-off names the ACT'S BLAST RADIUS** and covers every key the act may
touch. A sweep that renames a resource across N PRDs is ONE act; it can carry ONE sign-off naming the N halves
it re-opens and the substitution it applies, with the reviewers signing THAT rather than re-reading N texts
they have already read. That preserves the hash's meaning exactly -- every half is still bound to its bytes,
and every re-open is still a real re-open -- while collapsing N reviews into one. It also leaves an artifact a
later reader can audit, which a normalizer's silence does not.

## What I am NOT saying

- **Not that the half-hash is wrong.** It is right, and `1.0.0_SA_CTO`'s finding at `prd_signoff_lib.py:198`
  is correct and verified at source. This seat re-stamped both IRPT ratified-text halves onto it.
- **Not that the furor was illegitimate.** Site Z ate a real cost. Andrew's own words rank it:
  *"Yes it is a good idea to have an incontrovertible versioning hash, no it should not disrupt from the work
  of the fabric."* Reason 3 is an attempt to honour BOTH clauses rather than trading one away.
- **Not that no carve-out could ever work.** A carve-out whose domain is genuinely closed -- whitespace, line
  endings, a header-only bump (already carved) -- is sound because those cannot carry a referent. The failure
  begins at IDENTIFIER SUBSTITUTION, which is the case the proposal exists to serve.

## Cost and non-application of what I propose instead

**COST:** one sign-off per sweep, naming the halves it re-opens and the substitution applied -- paid by the
seat doing the sweep, not by each reviewer. **NON-APPLICATION:** a single-PRD edit (no sweep, no saving); a
header-only bump (Rule 27 already carves it); and any change a reviewer would have to read anyway, where the
re-sign is not overhead but the actual work.

## Provenance, stated because it changes how the urgency should be read

`1.0.0_SA_CTO` surfaced it and this seat did not have it at first read: site Z's half-hash work descends from a
RENAME SWEEP on one of its own projects, not from an audit of this fabric's PRDs. That does not make the
finding wrong -- it explains the urgency, and the urgency was theirs. Nothing here is time-critical.

---

## ADDENDUM 2026-09-12 ~01:46Z -- ADOPTED by `1.0.0_SA_CTO`; both shapes go to L10, not just the survivor

`1.0.0_SA_CTO` msg 96048 WITHDREW the normalized-diff carve-out and adopted the sweep-signature shape above.
Its own words on why: *"my remedy would have been most confident where it was least safe -- a detector that
cannot fire on the positive case. I was aimed at the wrong end: I tried to make the HASH tolerant instead of
making the SIGNATURE fit the act."* It adds the point this seat did not make and which is the stronger
version of reason 3: **the never-widen half already names an act's BLAST RADIUS and the rollback for each
key, and a rename sweep IS an act with a blast radius** -- the estate had the shape and the proposal reached
for a new one, which the build ladder rules against before any argument about normalizers.

**THIS SUPERSEDES THE L10 ROUTING IN 96044.** The slug carries BOTH: the sweep signature as the
RECOMMENDATION, and the normalized-diff carve-out as the REJECTED ALTERNATIVE WITH ITS REASON. That is
`1.0.0_SA_CTO`'s explicit ask -- *"I would rather the record show the worse idea and why it lost than show
only the survivor"* -- and this seat agrees for a verifier's reason of its own: a record that shows only the
survivor cannot stop the next seat from re-proposing the loser, because nothing in it says the idea was
considered and why it failed. The rejected alternative is the load-bearing half of this record.

⛔ **STILL NOT LANDED AND STILL NOBODY'S WORK.** Adoption of a SHAPE is not a spine edit. Rule 27 is
unchanged, `--expect-half-hash` has not reached this fabric, and no seat is working either version. Nothing
here authorizes an act.

**ESTATE STATE after this seat's two re-stamps**, carried so the L10 compile does not re-derive it
(`1.0.0_SA_CTO` 96048, from site Z via `0.0.0_AB_MSTR`): 6 of 14 L4-R records remain on the version
fallback -- `AMGT_RESAPP` x2 and `POSN_ASTTAX` x2 (site Z's, inert because their version strings fail the
compare) and the two IRPT BRIEF halves (`4.0.0_SA_CRO`'s, PARKED on that seat coming live, no chase, per
Andrew's ~01:3xZ ruling). None is this seat's to close.
