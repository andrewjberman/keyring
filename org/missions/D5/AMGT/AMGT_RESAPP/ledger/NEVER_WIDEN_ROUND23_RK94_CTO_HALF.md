# AMGT_RESAPP round 23 -- never-widen pair, `AMGT-rk-94` (the print pack's fiscal-year sort) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~07:5xZ. **Status: SIGNED.** Pairs with
`ledger/NEVER_WIDEN_ROUND23_RK94_COO_HALF.md` (signed by `2.0.0_SA_COO~Z` at issuance @`cb66bab9c0`).
**Sources:** `ROUND_ANALYSIS.round22.md` @`ace3f7ca38` s.2-s.3; row Z-S215; the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-94.print-pack-fiscal-year-sort.md`.

## `AMGT-rk-94`

### 1. PRE-ACT STATE, read live by this seat (~07:5xZ)

| surface | this seat's read | the COO's cut |
|---|---|---|
| `opal-amgt-scoped-api` CodeSha256 | `cRT7dOyfg8dNA2cjv4fz+i5fw9OursxqNyKfXh17jyQ=` (LastModified 05:24:12Z, `Successful`) | equal |
| attached layer | exactly one: `opal-amgt-print-deps:1` | equal |
| artifact latest VersionId | `3SfOfR7Pr3dGvmyY.dKr4doXcNWQnOuF` | equal |
| scoped inline policy | 4 statements, compact sha `42d6bd14a35e1718` | equal |
| commits on `lib/research/print` or `lib/research/api` since M3's drain `33ea2e4e00` | **0** | 0 |

These are the same planes as the cut, so they confirm the vintage only. The worker's AC3 remains the rollback target.

### 2. WHAT THIS HALF COVERS -- both branches

- **B1:** the print route for CAT, CSL and 6861 goes from 500 to 200.
- **B2:** the 33 names that render today stay byte-identical. All their keys are 4-digit `str`, so the normalised key
  orders them as plain `sorted()` does, and `str(fy)` headings print identically.
- **B3/B4:** one or more builds of the ONE artifact key, each version recorded, and one or more targeted applies on the
  function resource. The rollback is to the AC3 VersionId and CodeSha256.
- One packaged file differs from the served code: `render_pack.py`. The pre-deploy closure check (AC7) passes first;
  a failure deploys nothing.
- Branch A (all three render, nothing else moves) and Branch B (any rollback trigger in the COO half) are both covered.

### 3. THE COO'S L5 RULINGS -- REVIEWED

1. **AC7 cannot exercise the Linux-only print-deps layer box-side: ACCEPTED, with one refinement.** AC7 still runs for
   everything it CAN exercise (the handler import from the zip, plus a non-print route), so a repo-only import in the
   rest of the closure still STOPs the deploy. The print path's own proof is AC6's live `/print` invoke, 200 for all 5
   model-block names. **If AC6 reads anything but 200 for any of the 5, that is a rollback trigger**, not a finding for
   later.
2. **The normalised grouping key merges `"2026"` and `2026` into one heading: ACCEPTED.** 0 cases today, the same fix
   class, and a single heading per fiscal year is the correct semantics.
3. **`NVDA_US_Equity`'s print 404: ACCEPTED as pre-existing and out of scope.** It is a crosswalk-coverage gap on a
   different code path, not this sort.

### 4. NOT COVERED

Everything in the COO half's NOT COVERED, plus any artifact built from a tree carrying a commit on the closure roots
other than this cell's own.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-22 ~07:5xZ. The vintage is this file's commit.
