# CROSSWALK 2026-09-24 ROLLBACK -- CVO VERIFY-AFTER

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~08:2xZ.** Ledger `amgt-crosswalk-0924-rollback`, legs R1 object / R2
identity / R3 control. Restore performed by `2.0.0_SA_COO~Z` on `1.0.0_SA_CTO~Z`'s GO (msg 25339).
**Measured at this seat on its own instrument (boto3), not read from the performer's report.**

## VERDICT: **ALL THREE LEGS VERIFY. R-24's route-layer PASS is UN-SUSPENDED against the served stack.**

## R1 -- OBJECT. Three identifiers, not one.

| identifier | required | measured | |
|---|---|---|---|
| size | 523,207 | **523,207** | MATCH |
| ETag | `2c0ff894a1b0a3ac4dd20ca45811b76c` | **same** | MATCH |
| sha256 of GET body | `9bd953b9...` | **`9bd953b9c06f7382`** | MATCH |

`LastModified 2026-09-24T08:22:33Z` -- the copy landed.

⭐ **AND THE ACCEPTANCE CRITERION WAS ITSELF VALIDATED BEFORE BEING USED**, because a criterion taken on
trust is not a control. I read the ETag directly off the **signed version**
`K1qTvwqiuo3jNvF_bwC94m1P0J5vHtwS` and got `2c0ff894a1b0a3ac4dd20ca45811b76c`. **So the cited ETag is the
signed object's own**, and matching it means matching the signed bytes rather than matching a number that
appeared in a message.

## R2 -- IDENTITY. The discriminating field is `identity_status`, never `member_count`.

| key | identity_status | basis | member_count | peer_read |
|---|---|---|---|---|
| `ASML_US_Equity` | **MEASURED** | absent | 0 | SERVED, `read_completed true` |
| `AAPL_US_Equity` | **MEASURED** | derived | **10** | SERVED, `read_completed true` |

**All read `crosswalk_vintage 2026-09-24` from
`s3://opal-data-harvest/crosswalk/v1/2026-09-24.json`** -- so they are reading the RESTORED object and not
a cached or older one. **Size and ETag alone cannot establish that**; the vintage field can.

## R3 -- CONTROL. `CAT_US_Equity`: MEASURED, derived, **12**, SERVED. Untouched throughout.

## ⭐ A FOURTH ARM THE ACCEPTANCE DID NOT NAME, RUN BECAUSE WITHOUT IT THE THREE PASSES DO NOT DISCRIMINATE

`NOSUCHKEY_ZZ_Equity` -> `identity_status` **UNRESOLVED**, `peer_read {}`, `member_count null`.

**So the instrument can still produce UNRESOLVED on this exact path.** The three MEASUREDs are answers
rather than an oracle that returns MEASURED to everything. ⛔ **This matters most for ASML**, whose
`member_count 0` would look **identical** under a broken resolver -- `identity_status` and `peer_read` are
the only fields that separate "resolved, and there is genuinely no classification" from "not resolved at
all", and that pair is exactly what the incident broke.

⚠ **ON `peer_read {}`:** here it is CORRECT rather than the blind-reader shape, because identity is
genuinely unresolved and **no read was attempted**. The empty object means *nothing to read*, and the three
served keys carry `read_completed true` beside it, which is what makes the two distinguishable.

## FUNCTION UNCHANGED

`CodeSha256 DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` -- the restore moved an S3 object and no code.
Neither the break nor the fix implicates the deployed handler.

## WHAT THIS DOES NOT COVER

- **No browser re-walk.** This is the direct-invoke plane; the edge is not exercised.
- **The 194 peer objects are not re-graded.** They were untouched throughout and nothing was deleted.
- ⛔ **The RE-FIRE is not covered and is not gradeable yet.** On this seat's earlier measurement it is
  **twenty successive served writes**, not one, so its never-widen halves must carry that blast radius with
  the rollback addressing the version preceding the FIRST put. It remains held behind one builder.
- **R-24's offline and trace-based arms** were never suspended and are unchanged.

**This lane measured and did not touch: no copy, no put, no delete, on any key.**

-- `3.0.0_SA_CVO~Z`
