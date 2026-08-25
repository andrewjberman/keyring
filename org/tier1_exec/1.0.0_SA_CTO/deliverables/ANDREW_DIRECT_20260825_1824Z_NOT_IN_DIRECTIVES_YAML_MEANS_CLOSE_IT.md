# ANDREW-DIRECT 2026-08-25 ~18:24Z -- NOT IN DIRECTIVES.yaml = CLOSE IT. The predicate is MEMBERSHIP, not age.

**Channel:** CTO terminal, direct to `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`.
**Relayed same turn to:** `1.0.0_SA_CTO~X` (owns spring clean), COO, MSTR.

## VERBATIM

> "If the project is not attached to directives.yaml explicitly, i would almost blanket mark as
> superseded or indefinitely closed or something, can relay that to 1.0.0_SA_CTO~X as they are
> working on this now. There may be concepts in there that we want to return to and if thats the
> case we can reinvent a project, but it is a greater liability to have all this stuff floating
> unaddressed marked as live than it is to just close them all."

## WHAT THIS SETTLES

**It answers the open call `1.0.0_SA_CTO~X` carded to him: THE BAR.** Rule 25's 90-day dormancy
default selected ZERO projects (measured: 0 of 124 open at >=90d, oldest 68-81d), which left the
sweep with no predicate. **He has replaced age with MEMBERSHIP.** That is a strictly better
predicate for this purpose:

- **Age measures how long nobody touched it.** It cannot distinguish paused-with-intent from
  abandoned, and it false-negatives on anything recently poked.
- **Membership measures whether the work is CLAIMED BY A DIRECTIVE.** That is the property he
  actually cares about -- *"floating unaddressed marked as live"* -- and it is binary, checkable, and
  already recorded.

**And the recovery path is explicit and cheap: `we can reinvent a project`.** So the cost of a false
close is a re-mint, not lost work. **That asymmetry is the whole justification and it should be
quoted whenever someone hesitates over an individual specimen.**

## MEASURED SCALE (2026-08-25 ~18:2xZ, denominators printed)

```
  333  project JSONs total
  127  NON-TERMINAL (active | scoping | in-progress | on-hold | inactive | dormant | suspended)
   18  distinct project codes named anywhere in DIRECTIVES.yaml
  ---
  112  NON-TERMINAL AND NOT IN DIRECTIVES.yaml  -> would close under this ruling
        53 of them carry OPEN TO FILES (166 TO files)
        59 of them carry ZERO open TO files
```
**112 of 127 non-terminal projects -- 88% -- are not claimed by any directive.** That is the
liability he is describing, quantified.

## ⛔ THE CONSEQUENCE THE EXECUTING SEAT MUST HANDLE: 166 OPEN TO FILES

**Closing a project does not close its task orders.** 53 of the 112 carry 166 open TO files between
them. Heaviest: `MDPF_3FIRMS` 12 · `MDPF_CANPLAT` 10 · `DATA_PLATFORM` 9 · `ADVI_COTETL` 7 ·
`NFRA_PASSCRAFT` 7 · `MDPF_GLOBAL` 6 · `MDPF_TRGALN` 6 · `WSE_COTMDL` 6 ·
`NFRA_VELOCITY_CORE` 6 · `NFRA_VELOCITY_ESTATE` 6.
**A project closed while its TOs stay open reproduces the CLASS-A contradiction `~X` is already
sweeping** -- a terminal project with live task orders. The TO disposition rides the project close
or the sweep manufactures the defect it is fixing.

## ⛔ ONE SPECIMEN THAT NEEDS HIS EYE BEFORE IT SWEEPS -- surfaced, NOT an exception taken

**`MDPF_GLOBAL` is in the 112 and it carries HIS OWN UN-EXECUTED INSTRUCTION.**
Its `blocking` field reads: *"PRIMARY: COO decomposition of the T1-T5 execution plan (PRD Addendum C;
**NO ANDREW GATE ON STARTING -- the 08-03 memo IS the instruction**)"*, and its T1-T5 are
route/trigger canon, one synchronized daily schedule across all four scopes, a CloudFront/cache
census, MDPF silver dedup verification, and legacy decommission. **Ratified 2026-08-03 from an
Andrew-direct voice memo, un-gated, and undecomposed for 22 days.**

**It also overlaps the gold-consolidation directive he issued at ~17:55Z the same evening.**

⛔ **THIS IS NOT ME TAKING AN EXCEPTION.** His ruling explicitly contemplates this case -- *"there may
be concepts in there that we want to return to and if thats the case we can reinvent a project."*
**The reason to surface it rather than let it close is that MDPF_GLOBAL is not a CONCEPT to return
to; it is a LIVE RATIFIED INSTRUCTION of his that nobody executed.** Closing it and re-minting later
is a legitimate outcome he may well choose -- but he should choose it knowing that is what it is,
because the re-mint would have to carry the 08-03 memo's authority forward and nothing guarantees the
next author knows to look for it. *(The record for that class was written 40 minutes earlier:
`GLOBAL_COHERENCE_GATE_A_FILED_FINDING_LOST_ACROSS_A_HANDOFF_20260825.md` -- a correctly-filed
finding lost because nothing carried it to the next surface.)*

Same shape, lower stakes: `NFRA_VELOCITY_CORE` / `NFRA_VELOCITY_ESTATE` read `on-hold` under an
explicit **Andrew-direct 2026-08-03 suspension**. A blanket close would convert *his own deliberate
suspension* into a closure. **Suspended-by-him and floating-unaddressed are different states and
only the second is what he is targeting.**

## WHAT BINDS THE EXECUTION

- **The tag vocabulary is a Rule-24 act and it is `~X`'s**, already in flight: their proposed
  `status` (lifecycle) + `closure_reason` (termination cause) two-field split, reconciled against the
  existing `Lifecycle_Stage` prior art. **He named "superseded or indefinitely closed or something" --
  that is the INTENT, not the enum.** The enum still owes its four-postulate record.
- **Rule 25 stands: a close is a STATUS FLIP + REGISTRY MOVE. Nothing is deleted, no served key
  moves** (that would be NEVER#3).
- **The estate already has the procedure** -- `44c6925b35` (2026-05-22, Andrew-approved) closed 17
  dormant projects via a documented 3-step atomic close. Build-ladder rung 2: extend it.
- **Do not sweep a project a live seat is working right now.** Three of five live Tier-2 seats are on
  work with no directive home; the remedy there is a directive home, not a closure.
