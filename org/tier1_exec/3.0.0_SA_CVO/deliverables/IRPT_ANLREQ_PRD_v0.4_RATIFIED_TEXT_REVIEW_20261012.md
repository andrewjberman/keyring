# IRPT_ANLREQ PRD v0.4 -- ratified-text review (CONTRACTS: C-STOREDINPUT, what a stored input is bound to when the reader changes)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @4b1447e2cc
(ADDENDUM v0.4). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6294. **Prior:** v0.3 SIGNED.
**Verdict: SIGNED. Two notes; the second is about people, not code.**

## The contract

The template stored at acceptance records the reader's version. Same version as the running reader: the re-read must equal the
stored template, as today. Different or absent: the re-read is not compared, and the input stays bound by its digests, its
references, its owner and its source. The reader's new findings apply at the upload door only.

This seat printed `uploads.py` 516 to 539 at its grade of rounds 14 and 15, and lines 519 to 526 and 546 to 552 now: the re-read
must equal the stored template today, and the digests the contract leaves in place are there. The text matches the code.

**"Compare the holdings alone" is rightly refused.** The new reader changes the holdings on exactly the sheets it exists to
catch, so that comparison would refuse the same inputs for the same reason.

**The order is right this time.** Item 1 of the list is the count of stored inputs the new reader would read differently, cut
before the re-land. The round 14 build was reverted because that question came last.

The re-land carries this seat's two repairs from the round 14 grade as its first step. Row D2-W53-S9 has an owner and a rule.

## Note 1: the version constant is a discipline; give it a test

The contract rests on one sentence: the constant is "changed in the same commit as any change to what the reader returns".
Nothing makes that so. If a change to the reader forgets the constant, the versions are equal, the re-read is compared, and
every earlier input is refused. That failure is loud and safe, which is the right way round. It is also the round 14 failure
again. A test that pins the reader's output on the fixture sheets to the constant's value, and fails when the output moves and
the constant does not, turns the sentence into a mechanism. It belongs in the re-land's cell.

## Note 2: item 4 leaves a known-wrong input in use and nobody is told

The addendum says plainly what it gives up: an input stored under the earlier reader keeps whatever that reader made of it. Two
accounts merged into one holding list, or a totals row counted as a holding, "stays in that stored input until the person
uploads again".

The person has no reason to upload again. Nothing tells them. And a report can be made from that input.

The count in item 1 will say how many there are. When it is in, each affected stored input needs a decision that is not "wait":
the filer is told, or the input is marked so the page that offers it says its sheet would be turned back today, or it is shown
that none was ever used for a report. Which of these is a ruling, and it is small while the number is small. It should be made
when the count lands and not left to the phrase.

## What this seat read

The addendum; the lines above. Not read: the reverted reader beyond what the round 14 grade read; the form; the tests.
