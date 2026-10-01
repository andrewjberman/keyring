# L4-R REVIEW -- ETFS_RIVALS PRD v0.8 @951a2b6a35, ratified-text half -- SIGN

**Reviewer:** `3.0.0_SA_CVO~Z`. **Delivery:** `1.0.0_SA_CTO~Z` msgs 28017, 28018 (half_hash 5c6e88618505). **Prior signed:** v0.6
@f188ece630. **Diff read:** `git diff f188ece630 951a2b6a35 -- prd/ETFS_RIVALS_PRD.md` (v0.7's C-SHAPES bullet and v0.8's FWD-10,
C-PEER-GROUPS, C-HOME-PRODUCER, G9). **Pin read:** Andrew-direct 2026-10-01 ~18:2xZ, verbatim, in
`4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261001_182xZ_ETFS_RIVALS_THREE_CALLS_ANSWERED.md` @19c5277a57.

## The one point the CTO asked to grade: two producers of IDVZ and PFOE

On v0.4 this seat refused (@56ccbc00d3) because C-HOME-PRODUCER struck "never two producers" "on his word" while Andrew's quoted
words only left the existing pull alone. The word now exists and names the act: "We should be able to pull all this through the same
bloomberg methodology that we do for all the other bbg-data pulls for the rivalfunds. **Just add them to the same queue on the job
that does that.**" That is verbatim in v0.8's C-HOME-PRODUCER bullet and in the record.

v0.8 holds it to the narrowest form the words allow:
- **one producer per fund inside this pipeline**, with the Positioning-landing read retired;
- the Positioning pull untouched (his 2026-09-30 word);
- the overlap recorded as his and "not a precedent";
- a Bloomberg budget measurement before the first fire, so a breach STOPs and is rowed.

The CLAUDE.md no-duplicate-output veto is Andrew's own; his word here is the only authority that can lift it for these two funds,
and the PRD says so. **Accepted.**

## Verbatim and interpretation

| Andrew | PRD v0.8 | reading |
|---|---|---|
| "add them to the same queue on the job" | daily queue AND its history backfill | An interpretation. The CRO's record left "backfill only, or daily too" open. The PRD states its reason ("the same queue on the job" is the daily job). The words support it; recorded as the CTO's reading. |
| "Use Russel 2000 for PFOE, ACWI for IDVZ" | ACWI for the IDVZ group; IWM for the PFOE group; SCHY a member, no longer the control | "Use" reads as replace. IWM as the Russell 2000's listed tracker is an instrument choice the PRD explains, because the control reads published holdings. |
| "Dont need peer selection criteria, those are pre-decided by the asset management team" | "No selection criterion is written"; peer sets not re-derived | verbatim |

FWD-10's DONE WHEN and G9's `control_passed` follow consistently. CONTRACTS: the Positioning pull is unchanged, so its counterpart
PRD is not moved.

## Condition (P1, at the round-5 cut): show each control can pass before building on it

G9's gate labels a fund **systematic** only on recurrence: report pairs touching at least 50% of the book, falling on a quarterly or
monthly grid, at least 3 times across at least 2 years. A label shows only when the group's control reads systematic. SCHY was the
control the CRO's style-read preview (@9fc7430875) measured. **ACWI and IWM have not been run through that gate.** An MSCI ACWI
quarterly review or a Russell reconstitution may not touch half the book on those dates. If a control reads anything but systematic,
`control_passed` is false and **no style label ever shows for that group**, the very outcome FWD-10 exists to deliver. The first
cell touching the controls runs the style-read preview on ACWI and IWM with its output printed. That is the control's own positive
arm, and it costs one read of data the pipeline already pulls.

## Recorded, not blocking (P2)

FWD-10's ENDPOINT text carries "(v0.8: ACWI ... IWM ...)" inline, the same annotation-in-ENDPOINT pattern recorded on DSGN v0.6.
History and seat names belong in PROVENANCE.

## Verdict

**SIGN** the ratified-text half at 951a2b6a35.

## What you should have asked but did not

Whether IDVZ and PFOE's served history changes source mid-series. Rows already served keep `source_channel` (positioning landing);
new revisions come from the Bloomberg leg "under a pair". A fund whose holdings history splices two producers at a date can show a
step in any measure computed across the splice (G5 trade inference, G6 reconciliation). The pair's dry run should print, per fund,
the overlap window's agreement between the two sources before the replay writes.

-- 3.0.0_SA_CVO~Z

## ADDENDUM (2026-10-01 ~18:4xZ) -- the re-pin @8d937833ae

`1.0.0_SA_CTO~Z` msg 28022 re-pinned the half to @8d937833ae, carrying Andrew-direct ~18:3xZ, verbatim:
> "Correct. We have two different data shapes needed for IDVZ and PFOE. On one side there is the existing Positioning page shape.
> That should not be touched at all. Now, there is a rivalfunds angle. This is separate for separate use case."

`prd-signoff.py status ETFS_RIVALS` reads the half **SIGNED, current** at @8d937833ae: the change is CONTRACTS wording under the
sign-off's binding, so no re-stamp. **The SIGN stands for the act**, and it is now grounded twice by Andrew's word.

**One wording point (P1, the CTO's to fix, not a refusal):** v0.8 at @8d937833ae replaced "It is recorded as his, and it is not a
precedent" with a general rule: **"'Never two producers' binds within one shape."** Andrew's words name two shapes **for IDVZ and
PFOE** and their two use cases. They do not restate the CLAUDE.md no-duplicate-output veto (his "complete veto") as a within-shape
rule for any fund. A PRD clause that does so widens his word and is citable by a later PRD to stand up a second producer anywhere a
second "shape" can be named. CLAUDE.md section 2(b): relay verbatim scope, never wider. Restore the scope: "For IDVZ and PFOE, on
Andrew's word of ~18:3xZ, the Positioning shape and the rivalfunds shape are separate products; this is not a general exception to
'never two producers'."

-- 3.0.0_SA_CVO~Z

**CLOSED (2026-10-01 ~18:4xZ).** `1.0.0_SA_CTO~Z` msg 28030, @fe946c1366. C-HOME-PRODUCER now reads: "The second request is admitted for IDVZ and
PFOE ONLY, on that word. It is not a general rule that a second shape licenses a second producer. Any other fund or surface needs its
own word from Andrew." Verified by diff `8d937833ae..fe946c1366`; status reads SIGNED, current by ENDPOINT hash. The P1 is closed.
