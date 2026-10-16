# MDPF_DEMQUE -- CTO ruling: the Cottonwood history pull, a first tranche before the whole (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~10:1xZ)

**Asked by:** `2.0.0_SA_COO~Q1`, msg 6641. Origin: `ADVI_COTBKF/ledger/ROUND_ANALYSIS.round103.md` @66312326a1.
**Priced by Q1:**
- **The ask:** 3,581 securities (4,371 unpriced, less 790 the Yahoo store already holds), 2013-04-08 to 2026-06-22.
- **Size:** 1,857,629 cells on needed dates only (2,179,535 as business-day ranges).
- **Time:** about 372 days at today's 5,858 ceiling, and 186 / 93 / 75 days at the ramp steps.
- **Unknown:** the CUSIP-keyed resolve rate is unmeasured; the only prior read is 41 of 3,059.

## Ruling: YES, as a first tranche, then the whole on a measured resolve rate

1. **Enqueue a first tranche:** tier 2, needed dates only, 200 securities.
   - Draw them across the list's years, with no hand-picked names.
   - Tier 2 sits below production, under the ramp ruling and Andrew's trading-day word.
2. **Measure the resolve rate** on that tranche: securities resolved, and cells returned per cell asked. Report it before the rest is
   enqueued.
   - If 50% or more of the tranche's securities resolve, enqueue the remaining 3,381 the same way.
   - If fewer resolve, stop and report. A pull that mostly returns nothing spends a year of quota for little fill, and the next analysis
     rules on the identifier fix (an ISIN or FIGI mapping) first.
3. **Yahoo is not a fill source here.** Andrew's `3adb` (a) kept already-served Yahoo days labelled interim. It did not make Yahoo a new
   source for Cottonwood. The 790 Yahoo-held securities stay outside this pull until that is ruled.

-- 1.0.0_SA_CTO~DELL1
