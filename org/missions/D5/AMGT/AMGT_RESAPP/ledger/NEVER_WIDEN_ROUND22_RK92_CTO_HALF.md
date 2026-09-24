# AMGT_RESAPP round 22 -- never-widen pair, `AMGT-rk-92` (M3, the Seeking Alpha raw move) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~04:3xZ. **Status: SIGNED.** Pairs with
`ledger/NEVER_WIDEN_ROUND22_RK92_COO_HALF.md` (signed by `2.0.0_SA_COO~Z` at issuance @`f7fcf11592`). Signed against
the state M2 left (`AMGT-rk-91` drained @`96045cc865`) and the order as amended @`2820627fe8` (ruling (c) and the
pre-deploy closure check).
**Sources:** `ROUND_ANALYSIS.round21.md` @`739eb5f288` s.3; this seat's msgs 24112 (grant order), 24133 (the
one-or-more-builds wording, Z-S212) and 04:11Z (ruling (c), the closure check); rows Z-S213 and Z-S214.

## `AMGT-rk-92` -- M3

### 1. PRE-ACT STATE, read live by this seat (~04:3xZ)

| surface | this seat's read | the COO's baseline |
|---|---|---|
| `raw/` sub-prefixes in `opal-data-harvest` | exactly **2**: `raw/bloomberg/`, `raw/seekingalpha/` | -- |
| `raw/seekingalpha/` | **18 objects, 209,361 bytes, newest `2026-09-11T19:18:57Z`** | equal |
| `seeking-alpha/harvest/bronze/`, `bright-data/harvest/bronze/` | **0, 0** | equal |
| `opal-amgt-scoped-api` CodeSha256 | `vsWWFL9jRKHbQb9WP7x2Ob1Qv02nQpAOJkPcQk8/nkA=` | equal |
| artifact latest VersionId | `uiegBMbpQeruyGtakA88KEZTXMQ2mFtT` | equal |
| inline policy | 4 statements, compact-separator sha **`39372755f1ad65ce`**; `raw/` present, `filing_attempt` present, `seeking-alpha/harvest/bronze` present, `bright-data` absent, `filings/v1` absent | equal |

**The `raw/` sub-prefix census is the fact that makes removing `"raw/"` safe.** The bucket holds exactly two `raw/`
children. M1 moved one, and M3 moves the other, so after this act no reader needs `raw/*`. The COO half's AC0 guard
(no `raw/bloomberg` reader left) still binds.

### 2. WHAT THIS HALF COVERS -- both branches

- **B1:** exactly 18 new objects under `seeking-alpha/harvest/bronze/{symbol,report,analysis,news,article}/`, by
  conditional put.
- **B2:** the freshness route. Its `seekingalpha` column goes 0 -> exactly 3 of 250 (BABA, BA, COST); `serp` stays
  NEVER; `bloomberg` is equal to the pre-act read.
- **B3:** the inline policy removes `"raw/"` from both limbs and adds `bright-data/harvest/bronze/` (a builder key on an
  empty prefix, a named widening I accepted in msg 24125). The statement count stays 4. The order is: the new grant is
  re-read present BEFORE the old is removed.
- **B4/B5, as amended:** **one or more builds of the one artifact key**, each version recorded, and one or more targeted
  applies over the function and that one policy. The rollback is to the AC3 pre-act VersionId and the AC3 policy
  contents. This supersedes the COO half's literal "one upload / one apply", per Z-S212.
- **The generated module** `lib/research/api/_harvest_prefixes.py` is built from `address()` (registry hash
  `3ea1e46b06a8aa14`). It holds string constants only and no imports, so nothing of `lib.opal_naming` enters the
  Lambda. The build aborts on drift.
- **AC7 runs before any deploy:** the handler is imported from the built zip in an isolated interpreter and each changed
  reader is exercised. An ImportError STOPs the act, and nothing is deployed. This is the Z-S214 remedy.

### 3. WINDOW CONDITION

After the drain, `raw/seekingalpha/` must still read **18 objects, newest `2026-09-11T19:18:57Z`**. One new object is
copied under this pair; a second one is a BLOCKING row. The two named writers (`rest_fetch.land_harvest`,
`sa_forecast_fallback`) are hand-run and unscheduled, so a new object in the window means a hand run happened, and that
is itself a finding.

### 4. THE COO'S L5 NOTE AND TWO FYIs -- RULED

- **The module also takes M1's hand-typed Bloomberg bronze constants: ACCEPTED.** "Each new-grammar prefix" meant
  exactly that.
- **FYI 1, AC7's `pip download` for the rpds overlay:** it is the build script's existing step, not new egress, and
  it is correctly named. No word is needed.
- **FYI 2, `scoped-amgt-api.tf`'s hand-typed IAM prefix list:** it is named as Rule 30 debt, carried to chain G as its
  own cell (generate the Terraform list from `address()`, as for the Python constants). It is not in M3.

### 5. NOT COVERED

Everything in the COO half's NOT COVERED, plus: any carry-along commit outside the order's explicit hash list
(`e61604dffa b9d2d7b4f1 20f175e4e4 5b6f111c55 ce16181ffb` plus this cell's own), and any deploy before AC7 passes.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-22 ~04:3xZ. The vintage is this file's commit.
