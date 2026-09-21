# AMGT_RESAPP round 22 -- never-widen pair, `AMGT-rk-92` (M3, the Seeking Alpha raw move) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.**
by `1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND22_RK92_CTO_HALF.md`, under a heading naming `AMGT-rk-92`.
**Sources:** decomposition s.30; `ledger/ROUND_ANALYSIS.round21.md` @739eb5f288 `:44` (msg 24119); PRD v0.17
@1f7459456a C-FORMAT-SEQUENCE `:895-905`; CTO msg 24112 (new grant re-read before an old one is removed).
**Measured at the cut:** HEAD `739eb5f288`, 2026-09-21 ~23:4xZ, read-only. The order's AC3 re-reads every value at
spawn; where it differs, the ROLLBACK TARGET is the worker's AC3 value.

## `AMGT-rk-92` -- M3

### THE ACT (three live acts, in this order)

1. **Copy, 18 conditional puts** (`IfNoneMatch "*"`, never overwrite) into `s3://opal-data-harvest/seeking-alpha/harvest/bronze/`:
   12 endpoint objects via `store.bronze_put("seeking-alpha", <symbol|report|analysis|news>,
   "security_key=<canonical>", "<old stamp>.json", <bytes>)`, and 6 article bodies via
   `harvest_grammar.put_article_bronze("sa", <id>, <bytes>, "json", <old stamp>)`. Canonical keys come from
   `crosswalk.resolve()`: BABA_US -> BABA_US_Equity, BA_US -> BA_US_Equity, COST_US -> COST_US_Equity (3 of 3 MEASURED).
2. **One adapter artifact upload** to `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
   (a new version).
3. **One targeted apply** (`HALT_ACK=1 .tools/safe-apply.sh`) over `module.scoped_amgt_api.aws_lambda_function.this`
   and the scoped role's inline policy. The plan must read `0 to add, 2 to change, 0 to destroy`.

### BLAST RADIUS -- what the act MAY move

- **(B1) 18 NEW objects** under `seeking-alpha/harvest/bronze/{symbol,report,analysis,news,article}/`. The prefix
  holds 0 objects at the cut.
- **(B2) The freshness route** `GET /api/scoped/amgt/freshness`, `seekingalpha` column: 0 of 250 landed -> exactly 3
  (BABA_US_Equity, BA_US_Equity, COST_US_Equity). This is the one SERVED change, and it is truthful: the stamps have
  existed since 2026-09-11 and were invisible only because the old keys were not canonical. The `serp` column stays
  NEVER, 250 of 250 (0 objects at either home). The `bloomberg` column must equal the pre-act read.
- **(B3) The scoped role's inline policy**, `scoped_amgt_pool_prefixes`: REMOVES `"raw/"` from both limbs and ADDS
  the builder key `bright-data/harvest/bronze/` to both limbs. The addition is a named WIDENING, needed so the serp
  column can leave `raw/`. It is a LIST grant on a prefix holding 0 objects. The statement count stays 4.
- **(B4) Function code attributes** of `opal-amgt-scoped-api`.
- **(B5) One new artifact version.** Prior versions are untouched.

**NOT moved:**
- the 18 source objects under `raw/seekingalpha/` and the 119 under `raw/bloomberg/` (no delete);
- the chatter role and function;
- every other route's status code (13 GET routes);
- the role's other 20 list entries;
- `raw/bloomberg/`'s readers. Those are M1's; M3 removes `"raw/"` only if AC0 shows no `raw/bloomberg` reader left.

### WRITER CENSUS -- the act's OWN write set, one call deeper (Z-S192)

- **S3 writes: exactly 18 puts plus 1 artifact put.** `store.bronze_put` is one conditional `put_object` each.
  `put_article_bronze` calls `store.fetch_key_exists` (a list), then one `bronze_put`. There is no Bloomberg call, no
  vendor call, no `_pool` write and no delete.
- **Writers of the property "the new seeking-alpha bronze prefix":** N = 2 code paths after this cell --
  `rest_fetch.land_harvest` and `sa_forecast_fallback` via `rf.land_harvest`. Neither runs in this act; both are
  hand-run and unscheduled.
- **Writers of the served freshness column: N = 1.** `read_coverage_freshness` reads key names; the adapter makes 0
  GetObject calls under the bronze prefix.

### EXPECTED OUTCOME, both branches

- **Branch A (expected):** 18 of 18 copied and read back equal. The freshness reads 3 of 250 for seekingalpha, 0 for
  serp, and bloomberg unchanged. The policy has no `"raw/"` and has `bright-data/harvest/bronze/`.
- **Branch B:** a copy that finds its key already present (`existed True`) counts as present only if its sha256
  equals the source; a different sha256 STOPS the act, and nothing is deployed.

### PER-KEY ROLLBACK (from the worker's AC3 values)

- **Artifact:** `copy_object` from the AC3 VersionId, then the same targeted apply for the function. Its CodeSha256
  must print the AC3 value.
- **Policy:** restore `scoped_amgt_pool_prefixes` to its AC3 contents, re-apply, and read the policy sha256 back
  against AC3.
- **The 18 new objects:** left in place. They are additive and unread once the readers roll back. Removing them is a
  delete, which needs a human word.

**Rollback trigger (any one):**
- a route status changes;
- `bloomberg` landed differs from pre-act;
- seekingalpha landed is not exactly the 3 names;
- the post CodeSha256 is not the uploaded one;
- AC5's pre-apply re-read does not show `seeking-alpha/harvest/bronze/` in both limbs. In that case the policy
  apply does NOT run.

### NOT COVERED

- any S3 delete;
- any object outside the two named new prefixes;
- a Seeking Alpha silver write (filled by the backfill run, not re-derived here);
- any vendor or Bloomberg call;
- the chatter Lambda or its role;
- any carry-along commit other than `AMGT-rk-90` / `AMGT-rk-91` and this cell's own;
- the old grant removed before the new grant is re-read present.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-22 issuance (the issuance commit's hash is
the signature's vintage).
