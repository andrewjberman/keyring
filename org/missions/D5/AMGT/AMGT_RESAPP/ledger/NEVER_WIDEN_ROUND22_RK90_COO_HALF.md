# AMGT_RESAPP round 22 -- never-widen pair, `AMGT-rk-90` (move M1: `raw/bloomberg/` to the harvest grammar) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.**
owed by `1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND22_RK90_CTO_HALF.md`, under a heading naming `AMGT-rk-90`.
**Sources:** decomposition s.30; CTO round-21 analysis msg 24119 (`ledger/ROUND_ANALYSIS.round21.md` @739eb5f288)
items 4-7; CTO msg 24112 (grant condition); PRD v0.17 @1f7459456a C-FORMAT-SEQUENCE, C-HARVEST-HOME, C-DEDUPE-BY-KEY.
**Measured at the cut:** 2026-09-21T23:32Z, read-only. Where the worker's AC2 re-read differs, AC2's value is the
rollback target, never this file's.

## `AMGT-rk-90` -- move M1

### THE ACT

One move, by `0.9.0_WK_AMGT_RESAPP~90`, in ONE window:
1. COPY 110 objects from `raw/bloomberg/` to `bloomberg/harvest/bronze/<request>/security_key=<slash-safe>/<stamp>.json`
   through `lib.research.harvest.bloomberg.bronze_write` (the old bytes unchanged, metadata
   `received-form: bbg-client-json`), and 9 `pull_log.json` objects VERBATIM to
   `amgt/harvest/state/pull_log/security_key=<slash-safe>/<stamp>.json` -- all by conditional put, builder addresses
   only.
2. SWITCH every reader and writer of `raw/bloomberg/` (the order's section 1 list) in one commit, landed before the
   copy.
3. REDEPLOY `opal-amgt-scoped-api` (its freshness reader lists the new bronze prefix for the Bloomberg vendor) through
   `build-and-upload-scoped-amgt.sh` and ONE targeted apply on `module.scoped_amgt_api.aws_lambda_function.this`.

### BLAST RADIUS -- what the act MAY move, and nothing else

- **(B1) New objects:** exactly 110 keys under `bloomberg/harvest/bronze/` and 9 under `amgt/harvest/state/pull_log/`
  in `opal-data-harvest`. Both prefixes are EMPTY at the cut (0 and 0).
- **(B2) The adapter's code:** `CodeSha256` (pre `hP+6OO5PIBiaFL9IVCvFJ5ijaaVcme2q1tinW/oKa/U=`), `CodeSize`,
  `LastModified`; ONE new version of `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
  (pre VersionId `.BKJHDt8u.NTMdFQHOGf6pgAVdXpE52f`).
- **(B3) The served freshness answer** (`read_coverage_freshness`): the Bloomberg input column now reads the bronze
  prefix. The values must be EQUAL to pre for every name (the same stamps, relocated), and the row count unchanged.
- **Box-side code** (the Terminal pull consumer and the unit-map, FYE, fallback and coverage readers) reads and writes
  the new grammar from the merge. There is no schedule change.

**NOT moved (asserted):**
- the 119 old `raw/bloomberg/` objects: NO delete, left for Andrew's one batched word;
- `derived/model_block/` and every reader and writer of it (issuer Q1);
- the role and its inline policy (sha `0c6b3cf46bdff811`, 4 statements, equal pre and post);
- the `raw/*` grant (shared with `raw/seekingalpha/`, which retires at M3);
- every other function, including the chatter Lambda, whose 18 build inputs hold no reader of this prefix.

### WRITER CENSUS -- the act's own write set, one call deeper (Z-S192)

- **`bronze_write` -> `store.bronze_put`:** 1 conditional `put_object` per call plus `head_object` reads; it writes no
  second key, no index and no pointer (rk-81, merged @0731c87fca).
- **`state_put_pull_log`:** new in this act, 1 conditional put per call.
- **The move CLI:** reads only `raw/bloomberg/`. It makes no Bloomberg Terminal call and no vendor call.
- **Writers of the NEW prefixes after the act:** 1 per request kind, `bronze_write`, as C-DEDUPE-BY-KEY requires.
- **Writers of the OLD prefix after the act:** 0 (the order's AC5).
- **The artifact key's writers:** 1, this order's build script. There is no other writer this round:
  - M2 (`AMGT-rk-91`) redeploys the same function but is SEQUENTIAL, spawning only after this read-back.
  - M3 and M4 follow later.

### EXPECTED OUTCOME, both branches

- **Branch A (the copy is complete, sha_equal 119 of 119):**
  - the served freshness rows are EQUAL to pre (count and Bloomberg stamp per name);
  - the thesis and overlay leaves are unchanged (they read `derived/model_block/`, which is not moved);
  - the chatter Lambda is untouched.
- **Branch B (any copy mismatch, or the served freshness answer differs from pre):** ROLLBACK below. The code switch is
  reverted by a new commit. The copied objects stay, read by nothing after the revert, and are named in a BLOCKING row.

### PER-KEY ROLLBACK

- **Artifact:** `copy_object` of `research/opal-amgt-scoped-api.zip` from the AC2 pre VersionId, then the same
  targeted apply. `get-function-configuration` must print the AC2 pre CodeSha256.
- **New S3 objects (B1):** none removed; a delete needs a human word. They are harmless: nothing reads them after a
  code revert.
- **Code:** reverted by a NEW commit, never a reset.

### NOT COVERED

This half does not cover, and the act may not perform:
- any S3 delete;
- any IAM change;
- any write to `derived/model_block/` or `derived/model_block_fye/`;
- any Bloomberg Terminal or vendor call;
- any change to the chatter Lambda;
- any key outside B1;
- a schedule change.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-22 issuance (the issuance commit's hash is
the signature's vintage).
