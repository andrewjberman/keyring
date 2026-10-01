# MDPF_TAXSMA -- FAST pin grades (`3.0.0_SA_CVO`, 2026-10-01 ~06:3xZ)

**Asked by:** `1.0.0_SA_CTO` 103508. **Implementing seat:** `4.0.0_SA_CRO`. **Pins named by:**
`org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md` (as of 03:5xZ). **Lease:** FAST `MDPF_TAXSMA` read live until
06:20:24Z at 05:51Z (`drive-mode.py status`). **Graded at:** CLOUD HEAD (local), portal DEV `54bd4224`. Read-only:
two `get-function-configuration`, one `get-function` (the gold zip), two test runs.

| pin | claim | read | grade |
|---|---|---|---|
| TX-k-1, the gold package, deployed 02:17Z | built from `e8994f23af`; Tax code present; Tax DISABLED | live `mdpf-gold-lambda` CodeSha256 `7hI4flW5RZfisph6h7/HSsIWxwSMBFcdXMPMhjF9P/U=`, LastModified 02:17:00Z, equal to STATUS; the zip downloaded from Lambda hashes to the same value; 40 file members, 26 `.py`, six of them `taxsma_*.py`; 19 of 26 `.py` members are byte-equal (line endings normalised) to a file of the same name under `data/mdpf` or `lib` at `e8994f23af`, 0 differ, 7 have their source outside those two trees and were not compared; the function has 1 environment key and 0 carrying TAX | PASS on deployed bytes |
| TX-u-1 / TX-u-2, the publisher, deployed 02:21Z | switch OFF | live `opal-assets-mdpf-portal-publisher` CodeSha256 `pj+Jat96t5dijB+0SQF918S1pi3AZBs1eQNvMXLYEJA=`, LastModified 02:21:34Z, equal to STATUS; `TAXSMA_ROLLOUT_SWITCH` reads `OFF` (the one TAX key of 9) | PASS on the applied plane; the zip was not downloaded |
| TX-r-1, the Tax-off release is a zero business delta | 16 of 16 bodies process-time only | not re-run; the served arm is ledger leg V2 at the 13:50Z publisher run, which has not happened | NOT_EVALUATED until leg V2 |
| E2c `1e5e13d223`, E2d `46d04eb7b6`, E2e `dfe374adfb` (candidates, not deployed) | 223, 226 and 227 tests | all three are ancestors of HEAD; `py -3.12 -m pytest data/mdpf/tests/taxsma`: 227 passed in one process at HEAD | PASS on a test run; the offline real-data runs (Global 2,091,754,766.55; Cottonwood SMA 6,049,368.78) were not re-run |
| TX-c-1 / TX-c-3, portal `370d2fe8` | accessor and caption | ancestor of portal DEV HEAD; `bun test src/api/endpoints/__tests__`: 10 pass, 0 fail | PASS on a test run; no signed-in render exists (nothing serves Tax) |
| TX-i-1, TX-i-2, TX-i-3 (IAM applies) | applied, simulated | not re-read | NOT_EVALUATED |

## Observations (not grades)

- **O-T1.** STATUS says "39 modules" for the gold package; the zip holds 40 file members, 26 of them Python. The two
  counts measure different things; the STATUS line should name its unit.
- **O-T2.** The E2e defect (the prelude's default valuation date) is stated as present in the deployed code. This
  seat's scan of the six bundled `taxsma_*.py` files found neither `expected_last_trading_day` nor
  `prev_trading_day`, so the default lives in another member and the claim was not confirmed on deployed bytes. It is
  harmless while Tax is DISABLED; it is a stop for activation (STATUS next-proof 5 already says the rebuild is
  required first).
- **O-T3.** The lease read 06:20:24Z as its end at 05:51Z. Past that instant the project reads FULL unless
  re-armed; a FAST item landed after it would be outside the lease.

## Not verified by this seat

Leg V2; the two prelude roles in use; the Gateway route; the first-day and weekend parked rules; push state beyond
local CLOUD.

-- 3.0.0_SA_CVO

## Pre-read for TX-r-1 leg V2, 14:0xZ -- the 13:50Z publisher run (the leg is the lane's and is still OPEN)

Ledger `mdpf_taxsma-tx-r-1`, leg V2: "both served category-views keys content-equal to before on every field other
than generation time (DELTA=0, comparison printed)". This seat's read, before the lane's proof exists:

- The run happened on the deployed code: publisher `CodeSha256` `pj+Jat96..` (the built zip's, LastModified
  02:21:34Z), `TAXSMA_ROLLOUT_SWITCH` OFF; request 1c6abe65 at 13:50:49Z published 18 objects, 0 failed, roster
  complete.
- Four category-views keys were written (49financial, cottonwood, global, inflection), each compared here with its
  prior S3 version (2026-09-30 13:50Z): top-level keys equal 4 of 4; leaf paths and types equal 4 of 4 (121 or 122
  leaves each); the token "tax" occurs 5 times in each object in both versions, so no node appeared or vanished.
- Leaf VALUES differ on 17 to 23 leaves per object: `as_of` (2026-09-30 today by the run's log; the prior value
  was not printed), the provenance fields, and AUM figures.

**So the leg as worded cannot read DELTA=0 across two as-of days:** generation time is not the only field a day
changes. What this read supports is the weaker and true statement (same shape, same node set, Tax absent as before).
A DELTA=0 on values needs the same gold input published by the old and the new code. NOT a grade: the lane's proof
is graded when it lands.

-- 3.0.0_SA_CVO
