# T5 DEAD-CONSUMER KILL K4 -- json/portfolios Feb-2026 residue (6 objects) (change record + rollback note)

**Executor:** 0.7.0_AE_CloudOps~F | **Executed:** 2026-08-04T04:58:09-04:58:28Z | **Status:** CLOSED (verified)
**Authorization:** COO GO 042634Z (CTO split-gate 042600Z, Andrew categorical). Kill-list row 11 @b877dbc0f5.

## WHAT DIED (exact keys -- the 4-way basename collision navigated by FULL bucket+key)
`s3://opal-data-portal-v2/json/portfolios/{account_distribution[UNDERSCORE],latest,manifest,metrics,summary,timeseries}.json`
(6 objects, all Feb-2026 vintage: 02-19/02-20).

**Deliberately NOT touched, verified surviving post-delete:** hyphenated `account-distribution.json`
(07-23, row-8 SUPERSEDED class), `aum-metrics.json` (07-23), `aum-timeseries.json` (07-27, row 9 --
CTO-deliberate freeze, excluded this wave), both firm prefixes. NB `json/latest/manifest.json`
(the LIVE-fetched manifest, DT W9 capture) is a DIFFERENT key in a DIFFERENT prefix -- unaffected.

## WHY DEAD
5+ months frozen; zero readers found (T5.A caller sweeps: portal fetch chain deleted 07-29, zero
non-comment refs; these six predate even the legacy chain's current shape).

## MECHANISM + ROLLBACK
Versioned bucket -> delete markers. Marker VersionIds:
- account_distribution.json: `CzjTf8MJWwLg3R6KRGN.lUNXtvGbhepy`
- latest.json: `Z1jTYJ4163jy_yGbbg1Yicl9RNmSLiF2`
- manifest.json: `p7rWk7hR_gHBSUBYPElghypByZSb8137`
- metrics.json: `jS14_ycRUmVpQpg_9mV78c_.Cw4WD1Wk`
- summary.json: `5v50iFHpVe527fZZGuQHPSHcqck61qoY`
- timeseries.json: `CG1tPOLd5VYe3XvvQuhDblrx_gZtkYrz`
Rollback: delete the marker version per key (same form as K3).

## VERIFY
Post-delete listing shows EXACTLY the protected survivors (measured 04:58Z, output in the record
commit). Access window: no logs exist on this bucket (stated honestly, same as K3).
