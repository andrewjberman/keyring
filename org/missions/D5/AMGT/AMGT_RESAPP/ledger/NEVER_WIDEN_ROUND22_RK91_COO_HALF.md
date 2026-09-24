# AMGT_RESAPP round 22 -- never-widen pair, `AMGT-rk-91` (move M2: `filings/v1/*.source.json` to silver + state) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.**
owed by `1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND22_RK91_CTO_HALF.md`, under a heading naming `AMGT-rk-91`.
**Sources:** decomposition s.30; CTO msg 24119 items 4-7; CTO msg 24112 (grant condition); CTO msg 24106 items 3 and 4
(UNRESOLVED markers to state; `filing_source` silver); PRD v0.17 @1f7459456a C-FORMAT-SEQUENCE (the filings split).
**Measured at the cut:** 2026-09-21T23:32Z, read-only. The worker's AC2 values are the rollback targets.

## `AMGT-rk-91` -- move M2

### THE ACT

One move, by `0.9.0_WK_AMGT_RESAPP~91`, AFTER `AMGT-rk-90` has read back, in ONE window:
1. COPY the 14 RESOLVED `.source.json` objects into `filing_source` silver (13 under
   `sec/harvest/silver/filing_source/`, 1 under `issuer-site/harvest/silver/filing_source/`), each graded by a
   per-object round-trip (row -> object EQUAL). Also copy the 180 `UNRESOLVED-SOURCE.source.json` objects VERBATIM to
   `amgt/harvest/state/filing_attempt/security_key=<slash-safe>/UNRESOLVED-SOURCE.json`. All by conditional put,
   builder addresses only.
2. SWITCH every reader and writer of `filings/v1/*.source.json` (the order's section 1 list) in one commit, landed
   before the copy.
3. IAM, then the redeploy, then IAM, strictly in this order:
   - ADD `amgt/harvest/state/filing_attempt/` to both limbs of `aws_iam_role_policy.scoped_amgt_api_grants`, then a
     live re-read shows it present.
   - REDEPLOY `opal-amgt-scoped-api`; its `_read_filing_source_object` now reads the state object.
   - REMOVE `filings/v1/` from both limbs, then a live re-read shows it absent and the state grant still present.

### BLAST RADIUS -- what the act MAY move, and nothing else

- **(B1) New objects:**
  - silver `filing_source` parquet parts holding exactly 14 rows, under `sec/` and `issuer-site/`;
  - exactly 180 keys under `amgt/harvest/state/filing_attempt/`.

  All of these prefixes are EMPTY at the cut.
- **(B2) The adapter's inline policy `opal-amgt-scoped-api-grants`:** pre sha `0c6b3cf46bdff811`, 4 statements.
  - It gains `amgt/harvest/state/filing_attempt/` on both limbs.
  - It loses `filings/v1/` on both limbs.
  - The statement count stays 4. Every other resource and list prefix is byte-equal pre and post.
- **(B3) The adapter's code:** CodeSha256, CodeSize, LastModified, and one new artifact version. The pre values are
  M1's post-act values, re-read at this order's AC2.
- **(B4) The served management block:** for every security, the thesis leaf's `management_status`, `roster_status` and
  `roster_reason` are EQUAL pre and post. The reader's SOURCE changes from `filings/v1/` to state; its ANSWER does not.
  The live check covers the three validation names.
- **Box-side:** the roster, enrich, management batch, posture batch and filings fetch/batch/battery/analyze read and
  write the new grammar from the merge.

**NOT moved (asserted):**
- the 12 `.analysis.json` objects and every reader and writer of them (gold, chain G);
- the 194 old `.source.json` objects: NO delete;
- `raw/*` and every other grant;
- the chatter Lambda and its role;
- any filings BRONZE, which comes only from the backfill's first fetch.

### WRITER CENSUS -- the act's own write set, one call deeper (Z-S192)

- **`write_filing_source_silver`** calls `store.silver_append`. It writes parquet parts only under `filing_source`,
  skips unchanged rows, and writes nothing else (rk-81 / rk-84).
- **`state_put_filing_attempt`:** new in this act, 1 conditional put per call.
- **The move CLI:** reads only `filings/v1/`. It makes no EDGAR, issuer or ESEF fetch.
- **The policy's writers this round:** 1, this order's two targeted applies.
- **The artifact key's writers:** 1, this order, running after M1's read-back.
- **Writers of the old `.source.json` path after the act:** 0 (AC5).

### EXPECTED OUTCOME, both branches

- **Branch A (14 of 14 round-trips equal, 180 of 180 state sha equal, both IAM re-reads as required):**
  - the served management blocks are EQUAL to pre;
  - the three validation names serve 200 on the thesis leaf;
  - the adapter holds no `filings/v1/` grant and does hold the state grant.
- **Branch B (any mismatch, or any served block differs):** ROLLBACK below, in reverse order. No reader is ever left
  with neither grant.

### PER-KEY ROLLBACK

- **Policy:** restore `filings/v1/` to both limbs FIRST (a targeted apply, then a live re-read shows it present). The
  state grant may stay, since it is additive.
- **Artifact:** `copy_object` from the AC2 pre VersionId, then the targeted apply. CodeSha256 must equal the AC2 pre
  value.
- **Code:** reverted by a NEW commit.
- **New S3 objects:** none removed; a delete needs a human word. Nothing reads them after the revert.

### NOT COVERED

This half does not cover, and the act may not perform:
- any S3 delete;
- any `.analysis.json` change;
- any EDGAR, issuer or ESEF fetch;
- any grant other than the two named;
- any function other than `opal-amgt-scoped-api`;
- running before `AMGT-rk-90` reads complete;
- a schedule change.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-22 issuance (the issuance commit's hash is
the signature's vintage).
