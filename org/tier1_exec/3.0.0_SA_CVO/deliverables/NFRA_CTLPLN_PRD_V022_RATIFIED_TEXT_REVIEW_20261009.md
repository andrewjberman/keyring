# NFRA_CTLPLN PRD v0.22 -- L4-R review of the ratified-text half (on 1.0.0_SA_CTO msg 107788)

**archetype:** VALIDATE

PRD: `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` @333d2b37b3. The pins it names: the per-box branches (law
@538f0f51a7), deploy on the authoring box's push and the pinned-build rule (@ccbe8b8be1: "an OPEN ledger admits only the build it
pins"), and the push law (record `ANDREW_DIRECT_20261009_044xZ_PUSHES_NEED_NO_APPROVAL_EXCEPT_CLIENT_FACING_PROD.md`, law
d92d08c448).

## Verdict: REFUSE, on one finding of placement; the substance is signable

**The finding.** The addendum says the four outcomes are "amended in place and keep their ids" (step F0), but the ENDPOINT section
is unchanged:
- `:30` FWD-1 and `:55` FWD-4 still carry their old cards. FWD-4 still reads "without that box pushing".
- `:63` FWD-5 still reads "Publishing work ... only a deploy a box names".
- `:71` FWD-6 still reads "Site Z pushes a routine round on its own, and waits for Andrew on any round that would put ...".
- The re-based cards were appended instead, in the addendum at `:869-907`.

The PRD now states two versions of each of FWD-1, FWD-4, FWD-5 and FWD-6. The old FWD-6 contradicts the push law: site Z no longer
pushes for the cluster, and a routine push waits for no one.

`prd-signoff.py` binds a half to the ENDPOINT and CONTRACTS section bytes, so it reads my v0.19 signature as current at v0.22
(`status`: ratified-text SIGNED, current; the stored file is `prd_version v0.19`, endpoint_hash 33c11e39...). A sign stamped now
would bind the OLD cards. The same blind spot covers the v0.20 contract change and the v0.21 move, both written as addenda.

**What makes it signable.** Replace the four cards in the ENDPOINT section with the addendum's text, keeping the ids, and leave the
addendum as the record of why. The half's hash then moves, the notifier re-offers the half, and I sign the same text.

## The substance, read against the pins (signable as written)

- **FWD-1:** the round is planned and graded on the laptop and worked on dell1, which pushes `box/dell1`; the integrator merges;
  "nobody on dell1 writes the shared trunk". This agrees with the per-box law, and with LGIC_BLANKFIX's move to dell1 (dell1 cuts
  round 9 from the laptop CTO's analysis).
- **FWD-4:** each box pushes its own branch and the integrator merges on its schedule; O3's "no more than one unpushed round per
  lane" is kept.
- **FWD-5:** "only a script that an open signed change names, at the exact version it signed, goes live", which is the pinned-build
  rule @ccbe8b8be1. "Merging the shared trunk deploys nothing" keeps O4's negative arm.
- **FWD-6:** this is the push law. One note (P2): the law's "an unsure page counts as client-facing" is not in the ACCEPT. Carry it,
  or accept that the law alone holds it.

## For the CTO (mechanism, P1)

An ENDPOINT or CONTRACTS change written only as an addendum escapes `prd_signoff_lib`. The fix is one of two: the binder hashes
the addenda that declare an ENDPOINT or CONTRACTS change, or the spine's F0 "amended in place" is made mechanical (a check that
an addendum declaring an ENDPOINT change also changed the ENDPOINT section).

-- 3.0.0_SA_CVO

## Re-review at @6c5cf02601 (1.0.0_SA_CTO msg 107792): SIGN

The four cards now replace FWD-1, FWD-4, FWD-5 and FWD-6 in place in the ENDPOINT section. Each is byte-identical to its card in
addendum v0.22 (a card-by-card compare of the two copies at 6c5cf02601: 4 of 4 identical). The diff 333d2b37b3..6c5cf02601 touches
only those four card bodies, one blank line, and a placement note in the addendum. The substance was read above and stands. The
P2 note on FWD-6 ("an unsure page counts as client-facing" is held by the law, not the ACCEPT) stays a note.

-- 3.0.0_SA_CVO
