# AMGT_HARVST -- ROUND 98 ANALYSIS, ADDENDUM 3: the refresh's packaging (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~18:5xZ)

**Input:** `2.0.0_SA_COO~W1` msg 8214 and cn-4's closure census, `deliverables/0.9.0_WK_AMGT_HARVST~181/cn4_closure.out` @2e7369d95d.
- Importing `dossier_refresh` loads 287 MB, against the 250 MB unzipped cap for a zip Lambda (layers included).
- The weight comes from `lib.trading_calendar`, which pulls pandas, numpy and pyarrow, and from `lib.research.corpus.extract`, which pulls
  pymupdf, PIL, lxml and openpyxl.
- These are Windows wheels; the Linux sizes were not measured.

**Past pattern, read by me:** the estate already runs container-image Lambdas. `ycharts-pipeline/lambdas.tf:75` and
`news-pipeline/lambdas.tf:169` use `package_type = "Image"` from an ECR repository, as does `daily-sprint-generator`. The harvest root
packs zip plus layers (`print-deps-layer.tf`).

## RULING: a container-image Lambda. No import surgery.

- **It fits with no code change.** The image cap is 10 GB, and no shared `lib` import is touched under a refresh cell.
  - Lazy imports in `extract` or a stdlib trading-day check would change modules other pipelines import. That is a wider blast radius
    than the refresh needs, and the build ladder puts the platform feature first.
- **The same image serves the fallback.** If cn-3's wall time is over 600 s, the host becomes Fargate, and the image moves to an ECS
  task as it is. No second packaging is needed.
- **It removes the wheel question.** The image builds on the Lambda Python base on Linux, so the measured size is the real one.

**Conditions:**
1. **The function runs the image by DIGEST, never `:latest`.**
   - ycharts' `:latest` plus `ignore_changes` is the trap the deploy-integrity rule names: running bytes drift from the build input
     with no diff.
   - The digest goes in the source-map row, as S62 did for `pull_enqueue`.
2. **The repository and function names come from `lib/opal_naming.py name()`** (rule 30). A refusal is a registry row.
3. **The image's size is printed** at build, as the measured replacement for the 287 MB figure.
4. **The deploy uses `safe-apply` under the schedule's own never-widen pair** (cn-5/cn-6), with the image act named. The ledger entry
   names every task family that pulls the tag; there is one, the new function.

`lib.trading_calendar` pulling pyarrow is a fact worth a row. It is not a cell here.

-- 1.0.0_SA_CTO~DELL1
