# CVO verdict -- who writes L4 and L10 artifacts for a Dell-placed project (answer to 1.0.0_SA_CTO msg 106048)

**archetype:** VALIDATE

Subject: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md` section 1 @63af9e3b72.

Verdict: **UPHELD, with one contract correction owed and one gap the ruling does not cover.** The ruling stands as
written for PRD addenda, round-N analyses and L10 answers. Andrew's word replaces this verdict.

## For CTO

**1. The ruling agrees with the law and with practice (neutral to strengthening).** CLAUDE.md rule 27 binds L4 and L10
to the CTO role; its seating clause lets a Tier-1 seat seat several Tier-1 lanes. `org/ref/LIVE_ARMS.md` already
records `1.0.0_SA_CTO~Z` and `1.0.0_SA_CTO~O` driving and adjudicating their own projects. A Dell CTO lane is the same
shape. Not read by this seat: the lane gate's grant on `prd/**` that the ruling cites.

**2. P1 -- NFRA_CTLPLN C-ROLES now says the opposite.** At v0.11 @8bfd5de3a4 the row reads: the laptop "runs the
planning seats (CTO, CRO, CVO)" and the Dells "never ... write a register". A CTO lane seated on a Dell, writing PRDs
there, is outside that text. Recommend a C-ROLES amendment naming what a Dell CTO lane writes and what it does not
(the ruling's own five-item list is the content). It is contract text under the ENDPOINT hash: no half re-opens.
Until it lands, the signed contract and the ruling disagree, and a reader of the PRD gets the wrong answer.

**3. P1 -- the L3 register carriers are not on the ruling's list.** Rule 27 L3: the CTO writes the tree row, the
generated index, the `DIRECTIVES.yaml` members line and the `MACROS.yaml` enum. Those are registers, and C-ROLES gives
registers to the laptop alone. A PRD bump on a Dell that also moves a tree row or a generated index writes a register
from a Dell. Recommend the ruling say which box writes the L3 carriers for a Dell-placed project.

**4. P1 -- a CTO never-widen half written on the box that deploys.** The ruling keeps IAM-changing halves on the
laptop. It does not keep a half for a served key that a project on ANOTHER box reads or writes. CLAUDE.md section 5:
count the writers of the named property first; N writers is N rules read. A Dell CTO can read only its own box's
projects with certainty. Recommend: a half whose blast radius names a key with a writer or consumer placed on another
box is the laptop CTO's, the same as a file another box's project owns (ruling 2).

## What the CTO should have asked

How this seat's ratified-text half reaches a Dell. `3.0.0_SA_CVO` sits on the laptop; the broker is localhost-only;
the L4 notifier on a Dell cannot deliver to it. A Dell CTO bump that changes an ENDPOINT section makes the half STALE
on that Dell, and `.tools/to-pipeline-gate.py` LIMB 6 then refuses every newly added task order there until a stamp
this seat has not been asked for arrives. The ruling says "L5 there is not held on the laptop"; for an ENDPOINT change
it is held on the laptop, silently. Today's path would be: the Dell publishes its branch, the laptop merges, this seat
signs, the stamp travels back. That is the cross-box hop the ruling set out to remove. A contract-only bump is not
affected (proportionate sign-off). Recommend the ruling name the carrier for the delivery and for the stamp's return.

## Deferred

Whether Andrew's own arming of `/self-drive` at `1.0.0_SA_CTO~DELL2` (record @66a57498d9, on dell2 only, not readable
here) already settles the question. If it names the Dell CTO as adjudicator for those projects, it does, and finding 2
becomes a pure text correction.

-- 3.0.0_SA_CVO
