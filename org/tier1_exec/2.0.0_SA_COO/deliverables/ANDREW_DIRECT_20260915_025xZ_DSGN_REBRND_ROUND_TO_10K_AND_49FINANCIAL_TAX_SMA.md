# ANDREW-DIRECT 2026-09-15 ~02:5xZ -- DSGN_REBRND: ROUND AMOUNTS TO THE NEAREST $10,000; LOOK INTO WHY 49FINANCIAL'S TAX SMA IS NOT SURFACED

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. It follows his
~02:4xZ word (record @fe76e3e036), which set amounts to the nearest dollar.

## VERBATIM AND ENTIRE

> Yeah maybe we round to the nearest $10,000, therefore it will almost certainly be 0. Also, we should be tracking Tax
> SMA for 49Financial. I don't know why we're not surfacing that here, we should have been able to track it, may be
> worth looking into that while you're on the subject.

## WHAT IT SETTLES

1. **Asset Category Views amounts round to the nearest $10,000.** This supersedes ~02:4xZ's nearest dollar. His
   stated aim is that a near-zero residual, like the Opal-Unsupervised remainder, reads $0.
2. **An investigation, not a build.** He asks why 49Financial's Tax SMA does not appear in the SMA category, and says
   it should have been trackable. This seat looks into it now (read-only) and reports the cause to him. No data,
   registry or producer change is authorized by these words.

## HOW 2.0.0_SA_COO~D APPLIES ITEM 1, AND SAYS SO

- **Every amount in the view is rounded to the $10K grain before it prints:**
  - under $5,000 prints "$0";
  - $57,300 prints "$60K";
  - from $1M up, the existing two-decimal millions ("$21.68M") already sit on that grain;
  - billions keep "$X.XXB".
- **A bucket or member that prints "$0" has no width in a bar.**
- **The ~02:4xZ rule that a zero L1 bucket is SHOWN as $0 stands.**

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote. The portal
freeze and the feature branch stand.
