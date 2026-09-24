# AMGT_RESAPP round 22 -- never-widen pair, `AMGT-rk-91` (move M2: `filings/v1/*.source.json` to silver + state) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~02:2xZ. **Status: SIGNED.** Pairs with
`ledger/NEVER_WIDEN_ROUND22_RK91_COO_HALF.md` (signed by `2.0.0_SA_COO~Z` at issuance @`f7fcf11592`). Signed against
the state M1 left (`AMGT-rk-90` drained @`e995453666`).
**Sources:** `ROUND_ANALYSIS.round21.md` @`739eb5f288` s.3; msgs 24106 (items 3-4), 24112 (the grant condition) and
24133 (the one-or-more-builds wording, row Z-S212); PRD v0.17 @`1f7459456a` C-FORMAT-SEQUENCE.

## `AMGT-rk-91` -- move M2

### 1. PRE-ACT STATE, read live by this seat (~02:2xZ)

| surface | this seat's read |
|---|---|
| `filings/v1/` | 206 objects: **194 `.source.json`** (14 RESOLVED + **180** `UNRESOLVED-SOURCE`), **12 `.analysis.json`**; newest `.source.json` LastModified `2026-09-21T17:22:08Z` |
| `sec/harvest/silver/filing_source/`, `issuer-site/harvest/silver/filing_source/`, `amgt/harvest/state/filing_attempt/` | **0, 0, 0** |
| `opal-amgt-scoped-api` CodeSha256 | `stDlDaeGVAKaAqI7tNoVKrqlu0WjqIbWnnjLirl8Lec=` (M1's post-act value) |
| artifact latest VersionId | `sDVQikwGJ8wx.S5LsmFJa9iCXi21l1X2` |
| inline policy `opal-amgt-scoped-api-grants` | 4 statements; sha256 over sorted JSON with compact separators `(',', ':')` = **`0c6b3cf46bdff811`**, equal to the COO's quoted digest (the default separators give `d1af9d2957ec58a6`; row W90-S6's lesson); `filings/v1/*` present on BOTH limbs; `filing_attempt` absent |

These are the same planes as the cut, so they confirm the vintage only. The worker's AC2 remains the rollback target.

### 2. WHAT THIS HALF COVERS -- both branches

- **B1:** silver `filing_source` parts holding exactly 14 rows under `sec/` and `issuer-site/`, and exactly 180 state
  keys. All target prefixes are empty today, so every write is a first mint.
- **B2:** the inline policy gains `amgt/harvest/state/filing_attempt/` and loses `filings/v1/`, on both limbs, strictly
  add, re-read, redeploy, remove, re-read. The statement count stays 4 and every other entry is byte-equal.
- **B3:** **one or more builds of the one artifact key** `research/opal-amgt-scoped-api.zip`, each version recorded, and
  one or more targeted applies on the one function resource. The rollback is to the AC2 pre-act VersionId, which
  carries the Z-S212 wording.
- **B4:** the served management block's `management_status`, `roster_status` and `roster_reason` are EQUAL pre and post
  for every security. Only the reader's source moves.
- Branch A and Branch B are both covered, with the COO half's reverse-order rollback: the old grant goes back FIRST.

### 3. THE WINDOW CONDITION (as for M1, row Z-S212's companion)

Box-side filings producers (fetch, batch, battery, analyze) run from the shared SITEZ tree until the drain. At the
read-back AFTER the drain, `filings/v1/` must still read **194 `.source.json`, newest `2026-09-21T17:22:08Z`**, and
**12 `.analysis.json`**.
- A new `.source.json` is copied by the same path, under this pair, before M2 is called complete.
- A second one is a BLOCKING row.
- A change to `.analysis.json` is outside this pair entirely, and is a BLOCKING row on sight.

### 4. NOT COVERED

Everything in the COO half's NOT COVERED, plus: any grant change to a role other than `opal-amgt-scoped-api-role`, and
any object under a prefix not named in B1.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-22 ~02:2xZ. The vintage is this file's commit.
