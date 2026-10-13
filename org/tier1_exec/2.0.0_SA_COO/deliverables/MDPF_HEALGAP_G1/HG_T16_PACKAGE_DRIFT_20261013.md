# HG-t-16 package drift -- three vendored members of the characteristics producer's artifact differ between the live bytes and HEAD

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-13 ~15:1xZ. **Read at:** HEAD `34b7e3d62a` (the commit of the CTO's signed half, msg 4902).
**Why it matters:** the CTO half for HG-t-16 covers one rule, one `ListBucket` and the handler's new branch. `build_package.py --pin <HEAD>` builds the
function's whole artifact, and three of its six members have moved since the live artifact was built. Shipping them inside this apply is not covered by that half.

## Measured

Live artifact `s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip`, LastModified 2026-09-15T04:43:51Z, 180046 B,
function `CodeSha256` `rN/jcmeQk4F/...`. New build at HEAD: 197050 B. Member sha256 (first 16 hex), live against the build at HEAD:

| member | live | HEAD build | |
|---|---|---|---|
| `lambda_function.py` | `717c05095fc773c7` | `76a19fea21870faa` | the HG-t-16 change (covered) |
| `BUILD_MANIFEST.json` | `7ed4c7813a55184f` | `0ba2381f2c37e61b` | follows from the members |
| `data/assets/scripts/gold/build_satellites_characteristics.py` | `1d816a91c0c04960` | `1d816a91c0c04960` | same |
| `data/etfs/scripts/gold/etf_positioning_gold.py` | `93c87bd50ec90299` | `7d148279e5a755ea` | **DIFFERS, not covered** |
| `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` | `c677e8a5f6996555` | `92b64d97d69bfee9` | **DIFFERS, not covered** |
| `lib/trading_calendar.py` | `41b1c0c12651c62e` | `9bc467c6ce4d11e4` | **DIFFERS, not covered** |

## What each drift is (from the file's own git history; the live bytes equal the file at the named commit)

- **`etf_positioning_gold.py`** -- live == `09408b19e5`; four later commits, all `MDPF_SECHIST` (2026-10-09): `f9d959a290` gold blank-over-gap and MMF rule,
  `ed0b1fc0d2` MMF column reads the pull's TOT_RETURN_INDEX_GROSS_DVDS, `d3c47c1896` gap-record producer in the scheduled run, `ae567af9ef` MMF repair batch. Diff
  against live: 112 insertions, 6 deletions. This is the estate's return rule the producer imports for Bloomberg-sourced tickers' windows: the first run after
  the deploy could change the per-ticker return values that `characteristics.json` carries (at least the MMF tickers). **Effect on the served bytes: not measured.**
- **`etf_classifications_dynamodb.py`** -- live == `b0e1f33471`; two later commits (`cf24f07493` CUSIP filter in `find_by`, `a96e00c279`
  `classify_holdings` sums any class). The producer calls `get_item` only; neither changed function is on its path. Diff: 12 insertions, 3 deletions.
- **`lib/trading_calendar.py`** -- live == `0cbb0ad174`; three later commits (`3d7fb62105` weekly trading-day-frontier basis, `4b766e4e2d` fallback calendar
  covers 2010-2027, `b2b7488660` the fallback announces once per process on stderr). The producer's `resolve_bbg_as_of` reads the calendar; the changes are on
  the fallback path and new helper functions. Diff: 159 insertions, 18 deletions. **Effect on `resolve_bbg_as_of`: not measured.**

## What the act can do instead

- **(A) Ship HEAD's members** and ask the CTO to cover the three, naming the `etf_positioning_gold.py` effect on `characteristics.json` values (unmeasured).
- **(B) Ship the three members at their LIVE bytes**, so the new package differs from the live one in `lambda_function.py` and `BUILD_MANIFEST.json` only
  and the signed half covers everything the act changes. `build_package.py` reads members out of git at a pin and never from the working tree, so (B) needs a
  commit that holds the three files at the live bytes: a scratch branch, never merged. `safe-commit.sh` refuses that commit on the lane gate (`etf_*`
  paths are other lanes'); the sanctioned route is the audited `GIT_COMMIT_AUTHOR_OVERRIDE`, one audit row, on a branch that is never merged. Those lanes' own
  deployment of their changes stays theirs.

The issuer recommends (B): it keeps this apply to what the half names and leaves the other lanes' redeploy decisions with their lanes.
