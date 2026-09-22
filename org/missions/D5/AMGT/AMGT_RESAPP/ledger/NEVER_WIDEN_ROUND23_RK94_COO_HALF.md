# AMGT_RESAPP round 23 -- never-widen pair, `AMGT-rk-94` -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.**
by `1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND23_RK94_CTO_HALF.md`, signed against live reads. The order does not act
on one half (its AC0).
**Sources:** decomposition s.31; CTO msg 24146 (row `AMGT_RESAPP-Z-S215`, step 1); the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-94.print-pack-fiscal-year-sort.md`. **Measured at the cut:** 2026-09-22, SITEZ
`218ff3c994`, read-only by the issuer. Where the worker's AC3 re-read differs, the ROLLBACK TARGET is the worker's value.

## `AMGT-rk-94` -- the print pack's fiscal-year sort

### THE ACT

One or more builds of the ONE artifact key `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
by `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` (each version recorded), then one or more TARGETED
applies of `module.scoped_amgt_api.aws_lambda_function.this` via `HALT_ACK=1 bash .tools/safe-apply.sh
-chdir=infra/aws/terraform/harvest apply -target=...` (plan: `0 to add, 1 to change, 0 to destroy`). Deploy ledger
`amgt-rk94-print-pack-fy-sort`, opened before the first upload, closed on the post-act read. **The pre-deploy closure
check (order AC7) must pass first; a failure deploys nothing.**

The code the artifact carries differs from the served code (served source `33ea2e4e00`, M3's drain, CodeSha256
`cRT7dOyf...`) in EXACTLY one packaged file: `lib/research/print/render_pack.py` (the normalised fiscal-year sort and
grouping key). The new test file is NOT packaged. Carry-along at the cut: 0 commits on the closure roots since
`33ea2e4e00` (order AC4 STOPs on any commit not this cell's).

### BLAST RADIUS

What the act MAY move, and nothing else:
- **(B1) The print route's response for the three mixed-key names** -- `CAT_US_Equity`, `CSL_AU_Equity`,
  `6861_JP_Equity` -- from 500 to 200 (a rendered pack).
- **(B2) The print pack's fiscal-year ORDER for any name**: unchanged for the 33 names that render today (all their keys
  are 4-digit `str`, and the normalised key orders them exactly as plain `sorted()`); the grouping key `str(fy)` renders
  the same heading text. Their pack text lines are byte-identical.
- **(B3) Function code attributes:** `CodeSha256`, `CodeSize`, `LastModified` of `opal-amgt-scoped-api`.
- **(B4) One or more new versions of the artifact key** (versioning `Enabled`); prior versions untouched.

NOT moved (asserted by the order, AC6): the scoped role and its inline policy (4 statements, compact-separator sha
`42d6bd14a35e1718` at the cut, equal pre and post), the attached layer `opal-amgt-print-deps:1`, environment, timeout,
memory, the route table, the 12 non-print GET routes' status codes (200 each at the cut), `NVDA_US_Equity`'s print 404
(pre-existing; not covered by the crosswalk), every stored model block and every other S3 object.

### WRITER CENSUS

- **Artifact key:** N = 1 writer this round -- this order's build script run. No other round-23 order redeploys this
  function.
- **Function code:** N = 1 writer -- this order's targeted apply.
- **The value on the print route:** N = 1 rule -- `render_pack.build_pack`'s grouping and sort, reached from
  `scoped_amgt._print_pack` (function-scope import, `scoped_amgt.py:3953`). The model block it renders is READ, never
  written, by this act; its producers (the mixed int forecast years) are chain G's (ruling step 2).
- **The act's own write set, one call deeper (Z-S192):** the build writes the zip locally and uploads ONE object; the
  apply updates ONE function's code. render_pack writes its PDF and text to the runtime's temporary directory only.
  0 S3 writes outside the artifact key.

### EXPECTED OUTCOME -- read from the code's own rule

- The three mixed-key names render: years in ascending numeric order, then any non-numeric label last. For CAT the
  headings run `2016 .. 2025` (stored `str`) then `2026, 2027, 2028` (stored `int`, printed identically).
- The 33 currently-rendering names: unchanged, byte-identical pack text.
- `NVDA_US_Equity`: still 404 (identity-unresolved, a different code path).
- Every other route: unchanged.

### PER-KEY ROLLBACK

- **Artifact key:** `aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key
  research/opal-amgt-scoped-api.zip --copy-source "opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<AC3 VersionId>"`
  (`3SfOfR7Pr3dGvmyY.dKr4doXcNWQnOuF` at the cut). No version is deleted.
- **Function code:** the same targeted apply; `get-function-configuration` must print the AC3 CodeSha256
  (`cRT7dOyfg8dNA2cjv4fz+i5fw9OursxqNyKfXh17jyQ=` at the cut).
- **Rollback trigger (any one):** post-act CodeSha256 not equal to the uploaded sha; any non-print route or any print key
  whose AC3 status was 200 no longer 200; the scoped policy sha moved.

### NOT COVERED

Any edit to a producer or a stored model block (chain G); any IAM, layer, environment, timeout, memory or route change;
any file packaged other than `render_pack.py`; a portal change; any artifact-version delete; any S3 write outside the
artifact key. The held branch `wk-amgt-14-50` is not read or named as a surface.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-22, at the round-23 issuance (the issuance commit's hash is
the signature's vintage).
