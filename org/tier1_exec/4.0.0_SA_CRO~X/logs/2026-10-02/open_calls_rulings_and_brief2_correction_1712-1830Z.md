# Open calls ruled, brief 2 corrected -- 4.0.0_SA_CRO~X

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE
**Date:** 2026-10-02 (17:12Z-18:30Z)
**Task Order:** ad-hoc, Andrew-direct (record @fc46925968, addendum 3 @7f197bcde6)
**Status:** COMPLETE

---

## Objective

Run `/open-calls` for Andrew on the three IRPT briefs, correct a false vendor gate found while sweeping, then record
Andrew's rulings verbatim and route them to 1.0.0_SA_CTO.

---

## Compiler Tools

No compiler tools were run: the window was a decision sweep and record edits (no code, infra or data change). Reads were
`org/ref/VENDOR_EGRESS_WHITELIST.yaml` and one native Grep over `org/missions/D9/IRPT/IRPT_BCKEND` for the standing
YCharts authority.

**What worked:** the whitelist read before listing a vendor call removed one call that was already answered.
**What failed:** none.
**Gap found:** none.

---

## Work Completed

1. `/open-calls`: three cards (precompute every 49 Financial account; YCharts for the five Analysis test runs; gross vs
   net). The sweep found Kimi whitelisted as VEW-3 ("Yes Kimi can be called freely"), so the gate-wiring vendor call was
   not listed.
2. Brief 2 section 3.3 corrected @8a961a8573 (it had said wiring the gates needed Andrew's word); one-line correction to
   1.0.0_SA_CTO (msg delivered 17:39Z).
3. Andrew ruled ~18:1xZ: 1 (a) approved; 2 yes, one at a time, queue empty, plus later direction toward ~90 s end to
   end; 3 gross for now, net-fee operations per custodian/vendor later. Recorded verbatim as addendum 3 @7f197bcde6,
   with RULED pointers in briefs 1 and 2; routed to 1.0.0_SA_CTO (msg delivered 18:18Z).
4. Acked 0.0.0_AB_MSTR msg 104349 (push hold while site Z merges); this seat does not push.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Naming (brief 1 call 3) not put to Andrew | The CTO's ruling unless the R20 exception route is chosen |
| Struck the Kimi vendor gate in brief 2 | A standing whitelist row already answers it; keeping it would manufacture friction |

---

## Files Modified

See commit messages: 8a961a8573, 7f197bcde6.

---

## Blockers

None at this seat.

## Current State

Briefs 1-3 (`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/IRPT_BRIEF_{1,2,3}_*_20261002.md`) and the record with addenda
1-3 (`.../ANDREW_DIRECT_20261002_145xZ_IRPT_THREE_SURFACES_STATUS_AND_THREE_BRIEFS.md`) are at HEAD of this lane's
commits, last @7f197bcde6. All LOCAL; a push hold is in force (msg 104349). Test files are in
`C:\Users\AndrewBerman\Downloads` (easy, Stevens, typo), cited by sha256 in the record, not in git.

## Next Steps

1. **[1.0.0_SA_CTO]** Fold briefs 1-3 and the three rulings into 2.0.0_SA_COO~P, ~Y, ~M.
2. **[4.0.0_SA_CRO~X]** Answer questions on the briefs; nothing else owed.
