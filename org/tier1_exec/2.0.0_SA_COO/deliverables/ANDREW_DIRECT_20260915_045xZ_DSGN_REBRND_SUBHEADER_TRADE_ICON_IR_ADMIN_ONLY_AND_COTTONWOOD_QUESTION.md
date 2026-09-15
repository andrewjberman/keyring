# ANDREW-DIRECT 2026-09-15 ~04:4xZ-~04:5xZ -- DSGN_REBRND: "OPAL-ADVISED" SUBHEADER; A NEW TRADE SUBMISSION ICON; INVESTOR REPORTING FOR OPAL ADMINS ONLY; AND HIS QUESTION ON THE COTTONWOOD FREEZE

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. These are three
consecutive messages, received while the Cottonwood trace (~04:0xZ word, @ab499609ac) was being verified.

## VERBATIM AND ENTIRE

> Also when you have a chance on the front-end, in the "Model Portfolios" page, change the subheader line to
> "Opal-advised assets in total and by category." Also we need a different icon for Trade Submission in the sidebar,
> the paper icon is better for Investor Reporting. Speaking of Investor Reporting, that page needs to be listed for
> Opal Admins only in the tsx for that page.

> Also what was your conclusion on the category-views freeze?

> Did you get to the bottom of it?

## WHAT IT SETTLES

1. **The Model Portfolios Asset Category Views subheader reads "Opal-advised assets in total and by category."** Today
   it reads "Opal-managed ...".
2. **Trade Submission gets a different sidebar icon.** The paper icon (FileText, which both entries use today) stays
   with Investor Reporting.
3. **Investor Reporting is listed for Opal Admins only.** The gate is to live "in the tsx for that page", not only in
   the menu.
4. **Two questions on the Cottonwood freeze.** This seat answered them at the terminal in the same turn: the
   cottonwood pair identity gate compares two cent-rounded totals in floating point, so an allowed 2-cent gap fails
   and the Global fold is skipped. The evidence and the remediation route are in 96899.

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote. The portal
freeze and the feature branch stand.
