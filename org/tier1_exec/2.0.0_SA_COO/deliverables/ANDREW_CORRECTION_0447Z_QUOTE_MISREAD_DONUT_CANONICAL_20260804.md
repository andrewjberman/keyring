# ANDREW-DIRECT CORRECTION (COO terminal, 2026-08-04 ~03:45Z): the ~0447Z quote was MISREAD -- the donut's move off aum-metrics is NOT what he meant; fix = canonical

## Verbatim (COO terminal, this session)

On being shown that the Portfolio Analytics donut moved off `aum-metrics.json` under a deployed
comment citing his 08-03 ~0447Z words ("DE should be deriving everything it needs from the scoped
aggregate-aua-timeseries.json"):

> **"That is a misreading or taken out of context. I don't know the context but that is not a good
> idea and certainly not what I meant. Let's get this fixed and canonical."**

And immediately prior, his design intent, verbatim:

> **"Why would the donut move off of aum-metrics? it is extremely logical to keep that entire
> component to one json that was literally designed for it"**

## What this supersedes (supersede-in-place discipline; nothing deleted)

- **The ~0447Z quote MUST NOT be cited as a general derive-from-the-timeseries license.** Its
  application at deployed `ModelPortfolios.tsx:648-650` ("Kills the legacy aum-metrics dependency
  for the slice... the sanctioned pattern") is DECLARED A MISREADING by the quote's author. The
  G8-era donut re-source rested on it.
- **The design intent is CANONICAL: one JSON per component.** The Portfolio Analytics panel
  (donut + quarterly cells + model-detail stamp) reads ONE metrics artifact designed for it.

## The fix chain ("fixed and canonical")

1. **The canonical target is the platinum aum-metrics emitter** (already the named wave-remainder
   producer prerequisite): `platinum/mdpf/{scope}/aum-metrics.json` for ALL scopes on the canonical
   accrual->publisher chain -- designed to carry EVERYTHING the panel needs (model detail slices +
   per-model quarterly metrics + as-of), so the whole component restores to one designed-for JSON.
   **PRIORITY ELEVATED by this correction** (was P2 remainder; it is now the fix Andrew asked for).
2. **At emitter landing: the panel repoints WHOLE** -- donut + quarterlies + stamp to the one new
   artifact; the frozen `json/portfolios/aum-metrics.json` read retires under the repoint law.
3. **Interim state (donut on timeseries by_model, quarterlies on frozen legacy): OPEN QUESTION at
   Andrew** -- stay split until the emitter lands (no user-visible change now) vs revert the donut
   to the frozen file now (single-source but 12-days-stale slices + empty cottonwood donut).
   Default pending his word: STAY (reverting re-breaks cottonwood's donut visibly).
4. **Deployed-comment correction** (`MP.tsx:648-650` + any sibling citations of ~0447Z as license)
   rides DE's next portal commit with do-not-recite markers -- the record must not re-teach the
   misreading.

## Distribution
Broadcast same-turn: CTO (architecture + emitter PRD elevation), MSTR, DE (comment correction +
do-not-recite), DS (the emitter's producer side when dispatched). Committed under COO author.
