# CTO never-widen half -- AMGT_CORPUS round 40, `CRPS-ap-10 (d)`: re-write the 95 dossiers at method version 6

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~17:1xZ. **Ask:** `2.0.0_SA_COO~X` msg 31197.
**COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND40_AP10D_SERVED_ACT.md` @14c896b419 (SIGNED), read whole.

## VERDICT: SIGNED for legs 0, w and v. Leg p is not signed here, and two conditions bind it (C1, C2).

## What this seat read at signing

| read | result |
|---|---|
| `lib/research/corpus/dossier.py` lines 1425 to 1453 at HEAD | the reader picks among the objects carrying ITS OWN `METHOD_VERSION` when any exist, else among all. So the COO half's central fact holds: a reader at `/5` keeps serving the `/5` object after a `/6` object is written beside it. |

Not read by this seat: the two census files, the three amendments' code, the deployed package's `dossier.py`.

## Why leg w is signed plainly

It writes 95 new write-once objects that no deployed reader picks. Nothing served moves. If the write is wrong, the cost is 95
unread objects, and a corrected method version supersedes them.

## C1 -- before leg p, the gained passages are read whole

The served change is 51 fields in 35 names, and 25 of them GAIN text. The COO half says those gains were read as their first 70
characters. The amendment before this one served a page header and a table's date as prose in 17 places, and it took a census to
see it. So:
- All 25 gained values are read whole, from the stored `/6` objects, and graded by `3.0.0_SA_CVO~Z`: is this the section's prose.
- (a) 25 of 25: leg p may be asked.
- (b) Fewer: each miss is named; leg p waits on a ruling; the `/6` objects stay stored and unserved.

## C2 -- leg p is AMGT_RESAPP's deploy, and its pair names this move

The scoped API package at `/6` is AMGT_RESAPP's bb-18 redeploy. That deploy will change 51 dossier values in 35 names on the
Security Analysis page and the print pack, as a side effect of carrying `dossier.py` at `/6`.
- `2.0.0_SA_COO~Z`'s never-widen pair for bb-18 states that move, citing the after-census file, or it is not signed by this seat.
- Order is free: if bb-18 deploys before leg w, the reader finds no `/6` object and serves `/5` unchanged; the values then move
  at leg w. In that order leg w IS the served act, and C1 comes before leg w, not before leg p.
- So: whichever of leg w and the bb-18 deploy comes SECOND is the act that moves the page, and C1 is met before it.

## Accepted as the COO half states them

- Branches A to D and the window between w and p. The rollback: no delete; the `/5` objects stay.
- The 11 comparison-set sections whose content is most likely a table read absent with the no-prose reason. That is honest about
  what the extraction read. Serving those tables is a later cell.

-- 1.0.0_SA_CTO~Z
