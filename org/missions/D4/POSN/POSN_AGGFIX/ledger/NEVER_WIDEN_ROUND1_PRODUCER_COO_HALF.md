# NEVER-1 co-sign, ROUND 1 -- the COO half: the Positioning producer reads Opal's current assets by model and moves the aggregate out of the shared file into an Opal-only key

**Signer:** `2.0.0_SA_COO~Z` | **Date:** 2026-09-15 ~19:1xZ | **Act covered:** `POSN_AGGFIX.TO-A3-1` (cell `AF1-s-10`), the round's ONE producer
deploy through `infra/aws/terraform/yang-pipeline/` and its ONE driven run on the recorded event | **The other half:** `1.0.0_SA_CTO~Z`,
requested with the round-1 issuance; the act does not run until both halves are files at SITEZ (A3-AC1).

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| `aws_lambda_function` in `module.generate_positioning` (`yang-generate-positioning`) | code: TO-A2-1's `lambda_function.py` plus every commit TO-A1-1's A1-AC5 lists between the running bytes and HEAD | targeted plan `0 to add, 1 to change, 0 to destroy` (A3-AC4); deployed CodeSha256 == artifact (A3-AC7) | restore the artifact's prior VersionId (printed first at A3-AC3) as the latest object version and re-apply the targeted plan |
| `s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-positioning.zip` | overwritten by the build (versioned bucket) | head-object before and after (A3-AC3) | the prior VersionId |
| `s3://opal-data-portal-v2/json/positioning/positioning_data.json` | `current_holdings.AGG` removed; the five book `aum` values move from the July legacy figures to each model's own current `by_model` row; `generated_at` | prior vs new VersionId, per book non-aum identity and aum equality (A3-AC9) | copy the prior VersionId back as the latest version (a new version; no delete) |
| `s3://opal-data-portal-v2/json/positioning/opal_aggregate.json` | NEW key, the decomposition's 1.1 payload, `status OK` (or `UNAVAILABLE`) | head before (absent) and after, payload checks (A3-AC8, A3-AC9) | overwrite with a `status UNAVAILABLE` payload. An S3 delete is NOT part of this signature (it needs Andrew's word) |
| CloudFront invalidation by `yang-invalidate-cloudfront` on its recorded event | cache entries for the paths that event names | A3-AC8 | none needed: an invalidation removes cache entries only |
| `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/yang-pipeline/CHANGELOG.json` | the recorder's values | git (A3-AC11) | git revert |

**Writers of the named properties, counted (NEVER-1's rule), printed:** `json/positioning/positioning_data.json` -- **1 writer**, the producer
(`lambda_function.py:2627-2634`, `OUTPUT_KEY` :2529): measured at L5 by `comp-find "positioning/positioning_data" --band DEF` (17 DEF hits
across 61,858 files; 2 in code; the other code hit `build_satellites_characteristics.py:142` is a READER, `get_object` :230) and re-counted
by TO-A1-1's A1-AC2 on a different instrument before the act. `json/positioning/opal_aggregate.json` -- **1 writer**, the same producer (a
new key). **Readers named:** a book's `aum` -- 0 at text grain at L5 (A1-AC3 re-counts); `current_holdings.AGG` -- the satellites script's
`yang_index` (A3-AC10 exercises it before and after).

## What the act may NOT touch

Every other key under `json/positioning/` (A3-AC8 prints each key's LastModified before and after and any move is Branch B);
`allocation_summary.json` and `yang-generate-allocation-summary`; the `YangDataPipeline` state machine (never started); every other Lambda,
role and policy in the root; `platinum/mdpf/global/aum-metrics.json` and the MDPF gold producer (read only); the legacy
`json/portfolios/aum-metrics.json` object (no longer read, not modified); the portal, its gitlink, DEV and PROD.

## Both branches of every outcome named

- **The plan** reads `0 to add, 1 to change, 0 to destroy` on the one function: SIGNED. Any add, replace, destroy, or change on another address:
  NOT SIGNED -- the act stops on a row.
- **The driven run** writes `status OK` and the served delta is confined to {AGG removed, five book `aum`, `generated_at`, the new key}: Branch A,
  inside this signature. **It writes `status UNAVAILABLE`** (the platinum read failed at run time): the shared file then carries NO
  `current_holdings` and no `data_date` (today's wholly-failed arm: `generate_positioning_data` :2374-2381 and :2392-2395 @`605c03f81f`;
row `POSN_AGGFIX-Z-S1`), which breaks the Models view for every viewer -- that outcome is Branch B, and its
  rollback (the prior VersionId of the shared file restored, the function re-applied at its prior artifact) IS inside this signature and runs
  at once.
- **Any other served difference** (a holding, a weight, a benchmark row, another key moving): Branch B, the same rollback.

## The exposure window, named

Until `TO-C1-1`'s edge gate is live, `/api/general/positioning/opal_aggregate.json` is readable by any signed-in viewer. **This is not a
widening:** every figure in the payload is already reachable by any signed-in viewer today -- the aggregate holdings and `total_aum` in the
shared file's AGG block (the brief's F7), and the per-model and total AUM figures in `platinum/mdpf/global/aum-metrics.json` through
`/api/general/mdpf/global/aum-metrics.json` (`public-data-router/index.mjs:51-54`; the OAC grant covers `platinum/mdpf/*` per
`portal-proxy.ts:1366-1367` @edf85ce503). The gate closes the new key; D3's closure of the MDPF route is NOT this act's claim.

## Provenance

PRD v0.2 @`cbd85e5cff` C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED, C-CURRENT-SOURCE, C-OPAL-ONLY-DATA; decomposition round 1 @`605c03f81f` s.1.1,
s.1.3, AF1-s-10. Push state: LOCAL.

## CORRECTION (2026-09-15 ~19:2xZ, `2.0.0_SA_COO~Z`, on the CTO half @`ae1c985da4` and row `POSN_AGGFIX-Z-S2`; the signature above stands for the same act)

- **The writer count was WRONG: N = 3, not 1.** This half counted writers by a literal-key census (`comp-find --band DEF`), which cannot see a
  writer that addresses the key by PREFIX. The three writers of `json/positioning/positioning_data.json`, and after the act of
  `json/positioning/opal_aggregate.json`, each rule read by `1.0.0_SA_CTO~Z` (cited, not re-run here): (1) the producer, the act itself;
  (2) `yang-time-machine` (`infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py` :4-10, `restore_outputs`
  :197-239, skipping only `json/portfolios/` :52-58), restoring every key under `json/` that `capture-output-versions` recorded (:22, :62),
  Dev-triggered through POST `/data-refresh/time-machine`; (3) `infra/aws/lambda/v2_portal/yang_pipeline/scripts/rollback-protocol.sh`
  (:24-35 lists `json/positioning/`; :170-176 copy_object from a prior VersionId).
- **The act invokes neither writer 2 nor writer 3**, except its own Branch B rollback of the shared file's prior VersionId, which is inside this
  signature. `TO-A3-1`'s ledger entry names both (amended before hand-off, same commit as this correction).
- **The residual NEITHER half signs:** after Branch A, a restore by writer 2 or 3 to an execution before the change re-serves
  `current_holdings.AGG` and July's book `aum` to every signed-in viewer until the next pipeline run. It is not this act's key; it is row
  `POSN_AGGFIX-Z-S2`, carried to `1.0.0_SA_CTO~Z`'s round analysis.
- **The reader census `1.0.0_SA_CTO~Z` added:** `infra/aws/lambda/portal_data_proxy/lambda_function.py` `get_positioning_data` serves the whole
  shared file (:1705-1710) and heads it for health (:1989). It reads the file whole and so carries whatever the act writes; no field it names
  is outside the permitted set.
- **ADDENDUM (~19:5xZ, row `POSN_AGGFIX-Z-W1-S4`, measured by `TO-A1-1` A1-AC2):** writer 1 has TWO write sites in the producer file -- the
  Lambda handler's put (`lambda_function.py:2623-2630`), which is this act, and `main()`'s `--upload` put (`:2501-2508`), a manual CLI path
  this act does not invoke. `TO-A2-1` was amended before hand-off so that path writes the Opal-only key beside the shared file (A2-AC13). The
  writer count by program stays N = 3; by write site it is 4.

## ADDENDUM 2 (~21:3xZ, row `POSN_AGGFIX-Z-W1-S7`; the same line as the CTO half's ADDENDUM 1 @`10d61c774f`)

"A served difference" and "any other served difference", wherever this half names Branch A or Branch B, mean a difference in PARSED JSON
VALUES (dict key order ignored, list order compared), never a difference in raw bytes or a hash. The shared file's
`portfolios.<code>.benchmark.spread.segment` keys follow set iteration order under per-process hash randomisation, so two runs of identical code
can differ in byte order alone. A key-order-only difference is NOT Branch B. The permitted value differences stay exactly as named above:
`current_holdings.AGG` removed, the five book `aum` values, `generated_at`, and the new key. `TO-A3-1` A3-AC9 already compares parsed JSON.
