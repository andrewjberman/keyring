# Deploy Completion Record
**Date opened:** 2026-09-29T01:15:16.737931+00:00
**Status:** OPEN
**Deploy:** COMBINED scoped-API act naming BOTH orders: AMGT_RESAPP.TO-AMGT-uu-4 (the adjusted Base case) and AMGT_HARVST.TO-HVST-a-2 (package + mount the two timeline routes). One HEAD build, one artifact, one safe-apply, under all four never-widen halves. Rolls back as ONE.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| SHA | verify | the pyarrow==16.1.0 cp311 manylinux2014_x86_64 wheel sha256 as the build's own pip download prints it, RECORDED BEFORE ANY UNPACK; a second or different wheel is a STOP | the printed sha256 plus the wheel filename, recorded here before the unpack step runs |  | OPEN |
| SIZE | verify | stop limb 2: unzipped total of the package PLUS every attached layer against 262,144,000 B, the smaller figure governing if a smaller is met | the printed unzipped total with the layer and package broken out, and its verdict against the ceiling |  | OPEN |
| CLOSURE | verify | the closure diff against the DEPLOYED artifact VersionId 0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS by CONTENT, graded against the UNION of all four halves' limbs | per-limb verdict with a denominator on both sides and a planted-mutation control per identity verdict |  | OPEN |
| A1 | activation | ONE S3 artifact write research/opal-amgt-scoped-api.zip (prior VersionId 0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS is the rollback, re-read at build) | head-object new VersionId + content-sha256 equal to the locally computed sha of the graded zip |  | OPEN |
| ROUTES | activation | the two timeline route keys mounted on API 7k3ed8px20 (16 -> 18), and no other route | get-routes with every page counted client-side, before and after |  | OPEN |
| IAMGRANT | activation | ONE read-only statement on opal-amgt-scoped-api-role: s3:GetObject on arn:aws:s3:::opal-data-harvest/amgt/harvest/gold/* and no other IAM change | the applied inline policy read back from the APPLIED plane, resource count before and after |  | OPEN |
| PDF | verify | uu-4 stop limb 5: the served /print pdf OUTPUT byte-unchanged, pre-apply capture vs post-apply, on the content-stream oracle | pre/post content-stream digests over a multi-currency sample, the pair reading DIFFERENT CodeSha256, plus an instrument control |  | OPEN |
| VUU4AC1 | verify | uu-4 AC1: deployed CodeSha256 moved off vBSCqd71wGn1GNOpaWGKr+KdI6t+zo3QVovzEd9Mrew= and LastUpdateStatus=Successful | uu-4.AC1.py exit 0 |  | OPEN |
| VUU4AC2 | verify | uu-4 AC2: FWD-30 on the served plane, absences missing=0 and EXPORT-COMPARE OK on N of N | uu-4.AC2.sh exit 0 |  | OPEN |
| VUU4AC3 | verify | uu-4 AC3: served bases ADJUSTED AND BASIS-CARRYING M of M, both halves' expected M=70 | uu-4.AC3.py exit 0 |  | OPEN |
| VA2AC1 | verify | a-2 AC1: both timeline routes answer for 992_HK_Equity, HTTP 200 WITH DATA, in-region duration under 29 s | a-2.AC1.py prints AC1 RESULT: PASS (0 failure(s)) |  | OPEN |
| VA2AC2 | verify | a-2 AC2: code moved off the prior sha, a new artifact version latest with the prior standing, and /thesis /overlay /peers 200 as RESAPP controls | a-2.AC2.py prints AC2 RESULT: PASS (0 failure(s)) |  | OPEN |
| REPLAN | verify | terraform 0-diff replan after the one apply | plan reports no changes |  | OPEN |
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260929T011516Z OPENED by 0.7.0_AE_CloudOps~A with 14 leg(s)
