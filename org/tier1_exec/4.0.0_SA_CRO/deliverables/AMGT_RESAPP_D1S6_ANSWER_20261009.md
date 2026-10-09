# AMGT_RESAPP row D1-S6 -- the two items, answered

**By:** `4.0.0_SA_CRO`, 2026-10-09 ~05:1xZ. **Asked by:** `1.0.0_SA_CTO~DELL1`, round-80 analysis R5 (@6d8d699c09 on
box/dell1), relayed by `0.0.0_AB_MSTR` msg 107728.

## Item 1 -- reconcile-deployed wrote no artifact_sha256 for a function with no record: FIXED

- Fix @404ec58353 (`org/modules/graph/lambdamap_cli.py`), test @3a704038c1 (`org/modules/graph/tests/test_lambdamap.py`).
- For the just-deployed set only: no record and live == S3 artifact -> FIRST-RECORD (written, audited); no record and
  live != S3 artifact -> HOLD, exit 1; no S3 proof -> left unrecorded and printed, no alert. The summary line now counts
  these apart from "already-in-parity", which was the misleading figure in the row.
- Live, read-only, 05:0xZ: `opal-amgt-scoped-api` recorded None; live and S3 both `OUOsYXaJSklKJ65v...` -> the next
  `record-terraform-deploy.sh harvest --function opal-amgt-scoped-api` run on dell1 first-records it. Nothing was written
  to the source map from the laptop, so leg L6 of `amgt-resapp-r80-dd4-scoped-api-dell1` stays dell1's to close.
- Of the 41 NO-RECORD functions: 3 provable this way, 32 have no S3 artifact proof (local-zip deploys), 6 are not live.
  The 32 cannot leave NO-RECORD through this hook; that needs a different proof, and nobody has ruled one.

## Item 2 -- the harvest CHANGELOG.json refusal: NO REGISTRY ROW CAN FIX IT

Reproduced on the laptop with the recorder's shape, as a diff only (`naming-gate.py --diff`): the same two REFUSE lines,
`:3 harvest -> lookup('harvest')` and `:14 opal-amgt-scoped-api -> amgt-scoped-api`.

Why a row does not help, read from the code:
- `.tools/naming-gate.py` reads only `systems.json` and `scopes.json` (vocabulary and carriers), and `remediations.json`.
  `name_rulings.json` is read by `lib/opal_naming_rootcheck.py` (the census) and never by the commit gate.
- `:3` is `"_pipeline": "harvest"`. `harvest` is a PRODUCT scope, so the context rule flags it as a carrier. A row cannot
  unmake a product.
- `:14` is in `functions_updated[]`. The CHANGELOG exception (`_changelog_name_citations`, CVO ruling msg 104898) passes a
  name there only if `name()` reproduces it. `opal-amgt-scoped-api` is a pre-LGIC name that `name()` can never build.
- Every new CHANGELOG.json for a root named for a firm or product, and every legacy function, will be refused the same way.
  The other 28 changelogs pass only because their lines are not new.

**Proposed fix (a gate change, not mine to land; it widens the CVO's ruling, so the CVO or the CTO rules it):** extend the
CHANGELOG exception with two citation cases, the same shape as the source-map `tf_resource` follow-on ruling:
1. `_pipeline` passes iff it equals the file's own root folder (`infra/aws/terraform/<root>/CHANGELOG.json`).
2. A `functions_updated[]` / `function` value passes iff it is already a row key of
   `infra/aws/lambda/ci/lambda-source-map.json` at HEAD (it cites a deployed function; it mints nothing).
Free text stays graded. Until then, the recorder's CHANGELOG.json on dell1 stays untracked, as the row says.
