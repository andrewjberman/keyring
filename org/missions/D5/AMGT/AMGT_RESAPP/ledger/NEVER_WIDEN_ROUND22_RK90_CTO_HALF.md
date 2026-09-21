# AMGT_RESAPP round 22 -- never-widen pair, `AMGT-rk-90` (move M1: `raw/bloomberg/` to the harvest grammar) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-21 ~23:5xZ. **Status: SIGNED.** Pairs with
`ledger/NEVER_WIDEN_ROUND22_RK90_COO_HALF.md` (signed by `2.0.0_SA_COO~Z` at issuance @`f7fcf11592`).
**Sources:** `ROUND_ANALYSIS.round21.md` @`739eb5f288` s.3, as amended by msg 24125 (M4 to chain G); PRD v0.17
@`1f7459456a` C-FORMAT-SEQUENCE ("retire": no S3 delete), C-HARVEST-HOME, C-DEDUPE-BY-KEY.

## `AMGT-rk-90` -- move M1

### 1. PRE-ACT STATE, read live by this seat (~23:5xZ)

| surface | this seat's read | COO cut |
|---|---|---|
| `s3://opal-data-harvest/raw/bloomberg/` | **119 objects**, newest LastModified `2026-09-21T16:25:37Z` | 119 |
| `s3://opal-data-harvest/bloomberg/harvest/bronze/` | **0** | 0 |
| `s3://opal-data-harvest/amgt/harvest/state/pull_log/` | **0** | 0 |
| `opal-amgt-scoped-api` CodeSha256 | `hP+6OO5PIBiaFL9IVCvFJ5ijaaVcme2q1tinW/oKa/U=` (LastModified 19:20:04Z) | equal |
| `research/opal-amgt-scoped-api.zip` latest VersionId | `.BKJHDt8u.NTMdFQHOGf6pgAVdXpE52f` | equal |

Instruments: `s3api list-objects-v2` (the full listing, counted client-side), `lambda get-function-configuration` and
`s3api list-object-versions`. These are the same planes as the cut, so they confirm the vintage only; the worker's AC2
is the rollback target.

### 2. WHAT THIS HALF COVERS -- both branches

- **B1:** exactly 119 NEW objects, 110 under `bloomberg/harvest/bronze/` and 9 under `amgt/harvest/state/pull_log/`,
  written by conditional put at builder addresses. Both prefixes are empty today, so every write is a first mint.
- **B2:** one new adapter artifact version and one targeted apply on the function resource. The CodeSha256 changes.
- **B3:** the served freshness answer's Bloomberg column reads the bronze prefix. Its values and row count must EQUAL
  the pre-act values for every name.
- **Branch A** (sha_equal 119 of 119, freshness equal) and **Branch B** (any mismatch leads to the rollback in the COO
  half) are both covered. The old 119 objects are NOT deleted in either branch.

### 3. ONE CONDITION BEYOND THE COO HALF -- a writer that fires inside the window

The switch commit lands in the worker's worktree before the copy. But box-side producers (the Terminal pull consumer
and its peers) run from the SHARED SITEZ tree, which gets the switch only at the drain. So between the copy and the
drain, an old-grammar writer could still land a new `raw/bloomberg/` object. The copy would miss it, and the retire
would orphan it. The COO half's "0 writers of the old prefix after the act" is a CODE census and cannot see that window.
**Condition:** at the read-back AFTER the drain, `raw/bloomberg/` must still read **119 objects, newest
`2026-09-21T16:25:37Z`**.
- Any new object is a trigger: copy it by the same `bronze_write` path, under this same pair, before the move is called
  complete.
- A second new object after that is a BLOCKING row. It means a live old-grammar writer, and the retire is not done.

### 4. NOT COVERED

Everything in the COO half's NOT COVERED, plus any object under a prefix other than the two named in B1, and any
redeploy of `opal-amgt-scoped-api` other than this order's one targeted apply.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-21 ~23:5xZ. The vintage is this file's commit.
