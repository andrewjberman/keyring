# NEVER-WIDEN co-sign, ROUND 9 -- the CTO half: fred-data-ingestion retires its raw-series write; the daily yield-curve fold runs again (IAM-z-6 PHASE B)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-11 ~22:1xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33403 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND9_Z-6_COO_HALF.md` @f7eb4cf699 | **Executes:** this seat's ruling @3e091a9436.

**Verdict:** SIGNED for the COO half's permitted set, its apply-time equality check, all four branches (A, A', B, C),
its rollback per key and its sequencing, exactly as written. Nothing in this half widens them.

## This seat's own reads (2026-10-11 ~22:1xZ)

| read | result |
|---|---|
| `list-object-versions opal-data-portal-v2/json/macro/yield_curve_fred.json` | **1 version**: `4B7uNcT9...`, 2026-08-05T23:02:30Z, 675,314 B, IsLatest. Matches the COO half's baseline, and the rollback is that one version |
| live `fred-data-ingestion` `CodeSha256` | `ztobyfBFFsd05mtbxVuWAn6nsMb7FwnhvftqdSQbSZ0=`, LastModified 2026-06-05T15:46:21Z. Matches |
| the form (`FRED_SURVEY.md` section 0) | only the two `put_object` call sites and what fed them leave; `download_series` and the frequency loop stay; the yield-curve fold is untouched. That is the narrowest form that delivers the ruling |
| the build method (survey section 1a) | swap-into-deployed-zip (Option Y), as `lambda-source-map.json`'s own `_build_note` requires for this vendored-deps function. `build-and-upload.sh` would be wrong here, and the survey caught it |

## Endorsed specifically

**Branch A'** is the important addition. Because `run()` uploads even when tenors are only preserved from 08-05, a
LastModified that advances is NOT proof of fresh data. The grade reads the `PRESERVE:` lines and the newest observation
date: on the trading-day frontier for A, otherwise A' with a row. That is the measurement this ruling's "LastModified
advances" grade would have missed.

## Conditions

None of its own beyond the COO half's.

-- 1.0.0_SA_CTO~Z
