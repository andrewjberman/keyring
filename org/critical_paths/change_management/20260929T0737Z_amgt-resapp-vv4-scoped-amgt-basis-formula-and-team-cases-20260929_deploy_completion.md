# Deploy Completion Record
**Date opened:** 2026-09-29T07:37:02.468426+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 47 AMGT-vv-4: opal-amgt-scoped-api carries the basis-true formula, the Base-case label and the team's cases, plus ONE read-only pool prefix. Under both never-widen halves, SIX stop limbs.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| CLOSURE | verify | the closure diff against the DEPLOYED artifact (CodeSha256 CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=) by CONTENT, with stop limbs 1-3 graded CLEAR BEFORE any upload, including that the dossier read closure carries no fitz/pymupdf | per-limb verdict with a denominator on both sides and a planted-mutation control per identity verdict |  | OPEN |
| A1 | activation | ONE S3 artifact write research/opal-amgt-scoped-api.zip; the prior VersionId is re-read AT BUILD TIME and is the rollback | head-object new VersionId + content-sha256 equal to the locally computed sha of the graded zip |  | OPEN |
| IAMPREFIX | activation | ONE entry amgt/harvest/gold/research-dossier/ added to local.scoped_amgt_pool_prefixes and nothing else; the file's existing statements then grant GetObject under it and a prefix-conditioned ListBucket on it | the applied inline policy read back on the APPLIED plane, resource count and prefix-condition count before and after |  | OPEN |
| PDF | verify | stop limb 5: the served /print pdf OUTPUT byte-unchanged pre vs post apply, on the content-stream oracle | pre/post digests over a multi-currency sample, the pair reading DIFFERENT CodeSha256, plus an instrument control |  | OPEN |
| TIMELINE | verify | stop limb 6 (the CTO half s.3.2): the served /timeline output byte-equal before and after for 992_HK_Equity and BA_US_Equity plus a day route with events on each; any differing JSON path other than a timestamp STOPS and rolls back | per-path JSON diff before vs after, the pair reading DIFFERENT CodeSha256, with the differing-path count printed |  | OPEN |
| VAC1 | verify | vv-4 AC1: deployed CodeSha256 moved off CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM= and LastUpdateStatus=Successful | vv-4.AC1.py exit 0 |  | OPEN |
| VAC2 | verify | vv-4 AC2: FWD-30 on the served plane, absences missing=0 and EXPORT-COMPARE OK on N of N | vv-4.AC2.sh exit 0 |  | OPEN |
| VAC3 | verify | vv-4 AC3: formula as ruled M of M, team_cases as the dossier holds them N of N, at least one case SERVED | vv-4.AC3.py exit 0 |  | OPEN |
| REPLAN | verify | terraform 0-diff replan after the one apply | plan reports no changes |  | OPEN |
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260929T073702Z OPENED by 0.7.0_AE_CloudOps~A with 10 leg(s)
