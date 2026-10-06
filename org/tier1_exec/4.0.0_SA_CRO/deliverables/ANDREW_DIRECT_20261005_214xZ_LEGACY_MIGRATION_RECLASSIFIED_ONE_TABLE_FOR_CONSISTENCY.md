# Andrew-direct, 2026-10-05 ~21:4xZ (5:4x PM Eastern), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session, after this seat's answer on CIK.

> Also regarding the migration of BD-Securities to ETFClassifier, obviously we would have to run it on a 6 field basis
> with the new nomenclature/fields as part of the adaptation/reclassifier process. THe reason we have all of that
> stuff is becuase for Advisor Intelligence, we have that one massive table which facilitates that whole application.
> I just think it doesn't make sense to have multiple tables for this, and i think its a lot easier to have it in one
> place because that way we can be consistent with type, consistnet with layout/presentation, and perhaps most
> importantly of alll keep it consistent with asset class/ sub asset class/ sector

## What it states (as written, not widened)

- The legacy table's rows move to the canonical table THROUGH a reclassification into the canonical table's own
  nomenclature and fields ("the adaptation/reclassifier process"), not as they are.
- Why the legacy table exists: it serves Advisor Intelligence.
- Why one table: consistency of type, of layout and presentation, and above all of asset class, sub-asset class and
  sector.

## What this seat could not read from the words, and so did not decide

1. **"a 6 field basis".** Two readings fit what was measured today
   (`docs/briefs/one-classification-table-consolidation-analysis-20261005.md` section 2): the canonical table's SIX
   ASSET CLASSES (the legacy table has four), or SIX FIELDS per row (for example asset class, sub-asset class, sector,
   type, name, management style). Put to Andrew in the session.
2. **How much of the legacy table migrates.** It holds 10,873 securities; 2,053 label something held today. The
   analysis recommended filling rows for what is held. His words say "the migration of BD-Securities", which may mean
   all of it. Put to Andrew in the session.

## Bearing on the issued brief

`docs/briefs/mdpf-secclass-one-classification-table-midstream-brief-20261005.md` @6636ceef4c: consistent with its
finding F5 (the legacy rows cannot be copied across as they are) and its O6 (a stated mapping of classes). It adds a
named consumer the brief did not name by product: Advisor Intelligence. The trace found the Black Diamond gold library
already reading the canonical table only, and the 49 Financial chain still reading the legacy table (analysis 4.1 B2);
which Advisor Intelligence screens each feeds was not traced.

## Routing

One line to `1.0.0_SA_CTO` naming this record.
