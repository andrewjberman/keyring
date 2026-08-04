# LT/ULT backend diagnosis + render close (Andrew-direct localhost item)

**archetype:** DIAGNOSE
**Session:** 2026-08-04 ~21:40Z-22:50Z (same session as the FE-half log)
**Agent:** 0.2.0_DE_PortfolioAnalytics

## Trigger
Andrew-direct at my terminal (~21:40Z, verbatim recorded + broadcast to COO/CTO/MSTR 214330Z/214444Z):
smoked localhost:5175, LT/ULT not displaying on Positioning/Attribution/FactorTilts; validate FE,
then look into the backend NOW. COO re-sequenced DS's producers batch to NOW on his word.

## FE validation
Covered -- his localhost runs the fixed seams (Vite serves the working tree carrying 604101df +
02b7f351; v2.1.158 live on PROD per DT 214818Z), and the fixture proof (both synthesized vintages,
all 5 models, screenshots read) shows the FE renders the instant rows exist. The absence was DATA.

## Backend diagnosis (live primitives, not repo -- Rule 22a)
- Deployed lambdas ALL pre-rename: get-function-configuration LastModified = positioning 06-01,
  holdings-attribution 07-01, factor-tilts 05-04. Stale hardcoded LTC/LTA filters match EMPTY
  frames vs model_20260804_v1.pkl (carries LT/ULT) -> silent row drop.
- Artifacts unregenerated (12:37/13:16Z), all UST/ST/INT only.
- Repo: positioning+attribution fixes existed only as UNCOMMITTED working-tree edits (last commits
  06-01/07-01); factor-tilts working tree STILL carried legacy MODEL_CODES :36 -- flagged loud to DS
  (215413Z, the committed-but-never-deployed class one layer earlier: edited-but-never-committed).

## Close (all same evening, Andrew watching live)
DS commit 89a3cca5ed -> DT TF apply v1.5.3 (22:17:48Z, CodeSha256 x4 verified by DS) -> 4/4
artifacts regenerated 22:32-34Z with LT/ULT rows (LT 15 / ULT 14 holdings; zero LTC/LTA residue) ->
my observed render verify 3/3 PASS on the actual served bytes (fixtures = fresh S3 bodies):
- Positioning: real distinct allocations (LT 9.3/90.7, ULT 4.8/95.2), breakdown + selector populated.
- FactorTilts: LT/ULT bars all 6 factor groups; AGG recomputed incl. their AUA weights (R2 0.605).
- Attribution: ULT tab full 14-row table (95.1% equity, total 100.00); LT likewise.
Reported to DS/COO (224426Z/224452Z) + Andrew at terminal. Zero further FE work was needed --
exactly the dependency direction the both-vintage fixture proof predicted.

## Compiler Tools
| Tool | Result |
|---|---|
| aws lambda get-function-configuration (x3) + s3api head-object (x3+4) | rail-checked live primitives -- grounded the deployed-vintage vs repo vs artifact three-way divergence |
| comp-* routing | comp-freshness/comp-pipescript cover gold trees, not these v2_portal lambdas' deploy-vintage question; raw primitives were the right layer for a fresh-change APPLIED-truth read (Rule 22a) |

## Carry
- TO_PORTALREFRESH_FE_01 status reads ACTIVE but was delivered 07-17 -- reconcile with DT when convenient.
- Integration window 22:49Z cascade: seat verified CLEAN at 22:52Z, acked to COO 225313Z.
