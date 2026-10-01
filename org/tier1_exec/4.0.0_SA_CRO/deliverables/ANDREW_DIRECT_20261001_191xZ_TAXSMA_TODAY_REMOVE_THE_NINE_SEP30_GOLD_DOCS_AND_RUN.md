# ANDREW-DIRECT 2026-10-01 ~19:1xZ (3:1x PM Eastern) at the 4.0.0_SA_CRO terminal -- Tax SMA today: remove the nine Sep 30 Gold documents and run

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Channel:** one question this seat put at its terminal (AskUserQuestion) after the activation closed.

## The question and his answer, verbatim

Question: "Tax is now computed by the Gold pipeline (49 Financial +$18.77M, Global +$24.81M, Cottonwood $6.05M under SMA).
To show it on DEV TODAY, I must remove the nine Sep 30 Gold documents written without Tax at 9:30 AM Eastern, so an extra
run can write the Tax versions. The bucket is versioned, so the old versions stay restorable; no history file is touched.
Then the publisher switch goes ON and the publisher runs once. Otherwise it shows tomorrow at about 9:50 AM Eastern with no
removal. Which?"

Answer, the option he selected: **"Today: remove the 9 and run"** -- "Delete-marks exactly the nine 2026-09-30 Gold documents
that Tax changes (49 Financial and Global time series, totals and category tree; Cottonwood time series and category tree).
Old versions restorable by copy-back. About 15 minutes to visible on DEV."

## The nine, measured 19:1xZ (the Tax-on dry run vs the stored object, outside process-time paths: 9 of 16 differ)

`opal-data-assets/portal/gold/mdpf/<scope>/<type>/2026-09-30.json`, with the VersionId each holds now (the rollback):
49financial aggregate-aua-timeseries `kKxZqLyDakOWrLIP6yH86OHUlmYGI2pG`, aum-metrics `xDxBfvCBeKMORXVxILFK9NECiqF3LCgK`,
category-views `VrHVa0lB.2Bseu5i2xprAL43x_T9vvOA`; global aggregate-aua-timeseries `ra5P92KbDarNhGC3oLrWjWDBApRX_jtt`,
aum-metrics `N6nZSkYr7zIXnB9Tcsfq4F60YQZrvDwz`, category-views `wEAQrMFDtml60KMjpDcjtQ4ddG1jPwMZ`; cottonwood
aggregate-aua-timeseries `UW_Ti5U3Ov3D0rbMH4lfrSMzpdktnk0B`, category-views `iHI_Bjvw_B2XsQ5XN6yxWpFfI1tXxyd8`; inflection
aggregate-aua-timeseries `8eqg4SbOGnhfQQQOz6Rjv4sxRd2lbFSk` (extension fields only). The question named eight by kind; the
measurement adds Inflection's time series, which gains the four extension fields with null values (branch 2 of the
request), so it is in the nine.

## Andrew's visual validation, verbatim (~19:3xZ, at this terminal, after the publisher run 19:28:17Z)

"It works, i just smoked on PROD and looks great."

He looked on the PROD portal; the portal reads the same served documents (`opal-data-portal-v2/platinum/mdpf/*`), so no
portal promotion was involved. This seat did not read the DEV page itself; his look is the S3 proof and the visual
validation 103956 asked for.

## Consequence stated before the act

The extra production Gold run is also the first run of MDPF_HEALGAP's catch-up (deployed 15:00Z): it rewrites its five
Cottonwood gold partitions today rather than at 2026-10-02 13:30Z, under its own signed half.
