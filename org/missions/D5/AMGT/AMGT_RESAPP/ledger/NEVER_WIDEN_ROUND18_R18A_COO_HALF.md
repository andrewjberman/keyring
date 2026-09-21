# AMGT_RESAPP round 18 -- never-widen pair, R18-A -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.** The CTO half is
owed by `1.0.0_SA_CTO~Z` per msg 23958 at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND18_R18A_CTO_HALF.md`,
under a section headed with the same cell id. The order does not act on one half (its AC1).
**Sources:** decomposition s.26; `ledger/ROUND_ANALYSIS.round17.md` @4a2f054389 R18-A (`:82`), graduation `:47`,
disjointness `:87-89`; msg 23958; the bound in `AMGT-rk-68`'s order section 4 (`:166-176`); the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-74.served-crosswalk-vintage-field.md`.
**Measured at the cut:** 2026-09-21, read-only, by the issuer. Every value below is re-read by the order's AC3/AC4 at
spawn; where a re-read differs, the ROLLBACK TARGET is the worker's AC4 value, never this file's.

## `AMGT-rk-74` -- the served crosswalk vintage field

### THE ACT

One redeploy of Lambda `opal-amgt-scoped-api`, by `0.9.0_WK_AMGT_RESAPP~74`, through exactly this path:
`build-and-upload-scoped-amgt.sh` (one S3 write: the artifact key
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, a new version), then a TARGETED
`HALT_ACK=1 .tools/safe-apply.sh ... -target=module.scoped_amgt_api.aws_lambda_function.this` whose plan must read
`0 to add, 1 to change, 0 to destroy` on that one resource. Ledgered under slug `amgt-rk74-served-crosswalk-source`,
opened before the upload and closed on the post-act served read.

The code the artifact carries differs from the served code (source `55e3a56854`, the `AMGT-rk-37` redeploy) in
EXACTLY two files, measured by subtraction over the artifact's whole packaged population (50 closure sources + 7
`DATA_MEMBERS` + the build script = 58 paths; `git log 55e3a56854..HEAD -- <58>` = 1 commit, 1 file):
1. `lib/research/api/scoped_amgt.py` -- this cell's edit: `_identity_block` gains `crosswalk_source` right after
   `crosswalk_vintage`, valued `crosswalk.loaded_from()` read inside `resolve_identity()`'s existing `try`.
2. `lib/research/identity/crosswalk.py` -- **`AMGT-rk-68`, commit `0164b134ac`** (+42/-5), riding along as rk-68's
   order bound this redeploy to name: `CROSSWALK_KEY_RE`, `CrosswalkKeyShapeError`, a paginated pool listing that
   refuses any non-dated key, and `_RESOLVED_FROM` / `loaded_from()`. Not edited by this cell.

Any third file in the carry-along voids this half (order AC3 STOPs).

### BLAST RADIUS

What the act MAY move, and nothing else:
- **(B1) The identity block of every `/security/{key}/{overlay|thesis|peers|coverage|print|ledger|versions|compare}`
  response** gains ONE key, `crosswalk_source`, at index 3. Every existing identity key keeps its value and its order.
  At the cut 7 of 8 security leaves return a JSON identity block (print does not), 0 carry the key.
- **(B2) The crosswalk load behind that block (rk-68 riding along).** The pool listing is paginated and a key under
  `crosswalk/v1/` that does not match `^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$` refuses the load, where the served
  bytes took newest-by-sort. Live prefix at the cut: 2 keys, 2 matching, 0 non-matching, newest
  `crosswalk/v1/2026-09-19.json`, each document's `as_of` equal to its key date (2 of 2).
- **(B3) Function code attributes:** `CodeSha256`, `CodeSize`, `LastModified` of `opal-amgt-scoped-api`.
- **(B4) One new version of the artifact key** in `opal-313476888478-lambda-artifacts` (versioning `Enabled`); prior
  versions untouched.

NOT moved (asserted by the order, AC5/AC6): role `opal-amgt-scoped-api-role` and its 1 inline policy (sha256 over
sorted JSON `9e440a8e5330...` at the cut, equal pre/post), environment keys `[HARVEST_ARTICLES_TABLE,
HARVEST_METRICS_TABLE]`, 1 layer, timeout 29, memory 512, the 16-route table and the gateway route set, the 13 GET
routes' status codes (13 of 13 = 200 at the cut; LOST [] GAINED [] required), any other function.

### WRITER CENSUS

The property this half names an outcome for is the SERVED identity block and the function's code; each has its
writers counted:
- **Artifact key `research/opal-amgt-scoped-api.zip`:** N = 1 writer this round -- this order's build script run.
  No other round-18 order writes or redeploys this function: round 18 is R18-A + R18-C (Andrew-direct ~16:5xZ,
  record @c5532df80a), R18-C touches no packaged path, and R18-B is deferred past manager review (any of its groups
  on a packaged path drains after this one and carries its own pair).
- **Function code of `opal-amgt-scoped-api`:** N = 1 writer -- this order's targeted safe-apply.
- **The value of `crosswalk_source` on the served block:** N = 2 rules, both read: this cell's `resolve_identity()`
  (sets it from `loaded_from()` inside the `try`, `None` when the crosswalk is not read) and rk-68's
  `load_crosswalk()` (`crosswalk.py:698-719`, records `"s3://opal-data-harvest/" + key` for the pool branch at
  `:716`, `"file:" + path` for a local branch at `:713`). The served function has no `AMGT_CROSSWALK_PATH`, so the
  pool branch is the one reached.
- **The crosswalk objects themselves:** 0 writers in this act. The crosswalk producer
  (`python -m lib.research.identity.crosswalk --write-pool`) is not run by any round-18 order; if one wrote a new key
  mid-act the outcome below still holds per branch.
- **Beside the round:** the `AMGT-rk-48` direct act (drained @5a2ebfa1e1) rewrote `management/v1` objects the
  security routes READ, and 2 `raw/bloomberg/` stamps (row Z-S192). It wrote no identity-block input, so B1 is unaffected; the route census compares status codes only, never bodies.

### EXPECTED OUTCOME -- read from the producer's own rule, both branches

- **Branch A -- every key under `crosswalk/v1/` matches (the state at the cut, 2 of 2):** `_read_pool_latest()`
  returns the newest key; every security-leaf identity block carries `crosswalk_source
  "s3://opal-data-harvest/crosswalk/v1/2026-09-19.json"` beside `crosswalk_vintage "2026-09-19"`, and every other
  identity key is byte-equal to its pre-act value. Status codes unchanged 13 of 13.
- **Branch B -- a non-matching key appears under `crosswalk/v1/`:** `_read_pool_latest()` raises
  `CrosswalkKeyShapeError` before reading any object; `resolve_identity()`'s `except Exception` (`scoped_amgt.py:1775-1777`)
  catches it, so every crosswalk-resolved name becomes UNRESOLVED (or MEASURED on the landed block where one exists)
  with `reason` beginning `crosswalk not read: CrosswalkKeyShapeError`, `crosswalk_vintage None`, `crosswalk_source
  None` -- never a 500. This branch MOVES served identities and is NOT the expected state: if the order's AC4 sees a
  non-matching key before the build, the order STOPs and nothing is deployed; if one appears after the deploy, the
  AC6 identity comparison fails and the rollback below is executed (the rollback restores newest-by-sort, which is
  itself the pre-act behaviour).
- **Branch C -- the crosswalk read fails for any other reason:** the same `except`, the same UNRESOLVED-with-reason
  shape, `crosswalk_source None`; identical to the pre-act failure shape except for the added `None` key.

### PER-KEY ROLLBACK

Read from THIS act's pre-act values (order AC4, written to the worker's `.scratch/rk74_pre.json`); the cut values are
shown for orientation only.
- **Artifact key `research/opal-amgt-scoped-api.zip`:** `aws s3api copy-object --bucket opal-313476888478-lambda-artifacts
  --key research/opal-amgt-scoped-api.zip --copy-source
  "opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<AC4 ArtifactVersionId>"`
  (`YjjMpD9ULicxQPnExgUVIbVQkUOQ_l8k` at the cut). The module's `data "aws_s3_object"` resolves the current version,
  so no Terraform edit and no VersionId is ever handed to Terraform. No version is deleted.
- **Function code:** the same targeted `HALT_ACK=1 .tools/safe-apply.sh ... -target=module.scoped_amgt_api.aws_lambda_function.this`;
  then `get-function-configuration` must print the AC4 `CodeSha256`
  (`QwET8XtX3Z53ylyStMoiX/yaC0Slfrc959+rUGlHGME=` at the cut), and the 13-route census must equal the AC4 baseline.
- **Served identity block:** restored by the two steps above (no separate store holds it).
- **Crosswalk objects, role, environment, routes:** nothing to roll back -- the act writes none of them.

Rollback trigger (any one): post-act `CodeSha256` not equal to the uploaded sha; any of the 13 routes LOST; any
identity block unequal to its pre-act value once `crosswalk_source` is set aside; any block without the field or
naming an object other than the newest pool key; a moved role policy hash. The ledger leg closes with the rollback
proof and a BLOCKING row is filed.

### NOT COVERED

This half does not cover, and the act may not perform: any edit to `lib/research/identity/crosswalk.py`; any write
to a crosswalk object or any pool object in `opal-data-harvest`; putting the field inside the crosswalk document; an
environment variable (including `AMGT_CROSSWALK_PATH`), role, policy, layer, timeout or memory change; any route
table, gateway route or authorizer change; any resource other than `module.scoped_amgt_api.aws_lambda_function.this`
and the one artifact key; any packaged-file change other than the two named under THE ACT (a third file is a new
half); a portal change to display the field; any rollback that deletes an artifact version. The held branch
`wk-amgt-14-50` is not read or named as a surface.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-18 issuance (the issuance commit's hash is
the signature's vintage).
