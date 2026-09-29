# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 19, `HVST-i-4` (redeploy the scoped API so both timeline routes serve the publisher codes) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~21:5xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round19/NEVER_WIDEN_HALF_COO_I4.md` @`0abf041dfa`, AMENDMENT 1 (msg 26721,
READ-acked). **Closure ruling:** `ledger/CTO_RULING_I4_CLOSURE_CONTINUATION_INERT_20260929.md` @`3a354b0720`.
**Seat:** `0.7.0_AE_CloudOps~A`.

## VERDICT: SIGNED -- `i-4` alone

## 1. RE-MEASURED BY THIS SEAT (~21:5xZ)

- **The deployed artifact, compared with HEAD entry by entry.**
  - The object is `opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`. Its latest VersionId is
    `61Fb7L90ggUdpjcXaX4T8CcMgquyzn0U` (40,097,441 B, sha256 `960e8d27624b61b4`), which equals the COO half's prior
    version.
  - Of its 80 source entries (`lib/**/*.py|json` plus the handler), **3 differ at HEAD:** `harvest/publication_gold.py`,
    `harvest/timeline_api.py` and `corpus/continuation.py`. This equals the COO half's section 2.
  - The handler (`lambda_function.py`, sourced from `infra/aws/lambda/research/scoped_amgt_api/`) is equal to HEAD.
  - The two `lists/data/*.json` files have no git history. The build copies them from RESAPP deliverables, so they are
    not a HEAD difference.
- **The HARVST change, read as a diff.**
  - `timeline_api.py` is +13/-1. The one modified line appends `publishers_covered` and `publishers_covered_codes` to the
    columns it reads.
  - `_codes_of` returns `None` for a part written before the column existed.
  - Both serializers gain the two fields. No existing field is removed or renamed.
  - `publication_gold.py` is +6.
- **The newest daily part** is `part-20260929T212132Z`, ETag `4743eb602f1d88b92017bae0022b66e1`, of 8 parts. It is
  `i-3`'s, as the COO half states.
- **`continuation.py` is INERT** on this function (the ruling @`3a354b0720`, AST trace). The COO seat reached the same
  answer independently on a second plane: 7 function-scope importers, none reached by `read_dossier`.

## 2. CONDITIONS

1. **The `--build-only` closure diff must show exactly the 3 source files** plus the wheels pinned on `HVST-a-2`'s halves.
   Anything else is a STOP. At build time the executor re-confirms that `continuation.py` equals CLOUD HEAD and still has
   no request-path caller.
2. **The budget:** a new unzipped total over 262,144,000 B is a STOP. It is 96.7% today.
3. **After the apply,** AC1 and AC2 must pass:
   - on the 149 PARTIAL days the codes read exactly ASML_NA 74 `['sa']`, ASML_US 74 `['sa']` and 992_HK 1 `['wsj']`;
   - DENIED days read `0` / `[]`;
   - every pre-existing series field is unchanged;
   - the three RESAPP control routes return 200.
   Any failure triggers the ROLLBACK to VersionId `61Fb7L90...` the same session.
4. **If another deploy moves the artifact before this act,** the COO half's section 6 re-read applies, and this half
   does not travel with it.

## 3. ROLLBACK

The COO half's section 6 stands: re-point the function to the prior VersionId and run `safe-apply` forward. No S3 delete.

## 4. NOT COVERED

- IAM, route, layer, runtime, memory or timeout changes.
- Any S3 delete.
- Any portal promote. The page's rendering of the codes is DSGN_AMGTV1's.
- Any served effect of `continuation.py`; none exists on this function.
