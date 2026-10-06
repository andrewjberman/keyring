# Andrew-direct, 2026-10-05 ~21:1xZ (5:1x PM Eastern), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session, after this seat reported the holdings check and
recorded his sector ruling.

> I want you to sketch out the implementation for this. I do not like using bd-securities and all these random tables,
> there should be one table for all classification efforts. I could tell that bd-securities was being used for the
> Investor Reporting page because all the names were all caps and not cleaned up nicely. If "Sector" inclusion can be
> managed surgically, and the gaps resolutely filled in, this should be manageeable. What I need you to do is assess
> the various shapes/demands for the components/functions you listed earlier and devise a plan to consolidate all the
> bd-securities info into the ETFClassifier table, in a manner that does not break any of those surfaces. I imagine
> that means there will have to be some migration ops for the relevant frontend aspects that call to other tables, so
> please trace any and all adapters that may need to be adjusted for this and write an analysis on the subject, a
> /brief-create, and issue that to CTO

## What this seat does with it (scope as stated, not widened)

1. Assess the shapes and demands of the components and functions listed in
   `docs/briefs/holdings-surfaces-canonical-classifier-check-20261005.md`.
2. Trace every adapter, backend and frontend, that reads a classification from anywhere other than the canonical
   table.
3. Write the analysis and a plan to consolidate `bd-securities` into the canonical table without breaking a surface.
4. Write the L1 brief with `/brief-create` and issue it to `1.0.0_SA_CTO`.

This seat builds nothing and changes no table. Related words of the same day: the canonical-only instruction
(`ANDREW_DIRECT_20261005_204xZ_HOLDINGS_SURFACES_ONLY_CANONICAL_ETFCLASSIFIER_TABLE.md`) and the sector ruling
(`ANDREW_DIRECT_20261005_213xZ_CANONICAL_TABLE_CARRIES_SECTOR.md`).
