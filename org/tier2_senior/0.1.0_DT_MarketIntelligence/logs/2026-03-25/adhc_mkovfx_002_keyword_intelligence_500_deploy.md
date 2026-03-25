# Session Log: ADHC_MKOVFX-002 -- Keyword Intelligence 500 Deploy

**Agent:** 0.1.0_DT_MarketIntelligence
**Date:** 2026-03-25
**Task Order:** ADHC_MKOVFX.002.dt-keyword-intelligence-500-deploy.md
**Project:** ADHC_MKOVFX

## Summary

Deployed two fixes for the TopicCloud keyword intelligence 500 error across
market-overview and news-pipeline. Hit two post-deploy regressions caused by
the portal_data_proxy zip missing vendored dependencies.

## Deliverables

| Tag | Pipeline | Change |
|-----|----------|--------|
| `market-overview-v1.6.5` | market-overview | portal_data_proxy: try/except for keyword-intelligence route |
| `news-v2.7.3` | news-pipeline | keyword_intelligence_generator: MAX_KEYWORDS 10->20 (code + Terraform env var) |
| `market-overview-v1.6.6` | market-overview | Hotfix: add session_tracker.py to source map files[] |
| `market-overview-v1.6.7` | market-overview | Hotfix: rebuild zip from _build_tmp/ with vendored openai+pydantic deps |

## Commits

| SHA | Description |
|-----|-------------|
| `ab904f54` | Code + Terraform changes (DS co-authored) |
| `ee23aa4a` | Upload artifacts for both pipelines |
| `8f3a35d7` | Record deploy market-overview |
| `4120fa6c` | Record deploy news-pipeline |
| `25ca4c2d` | Hotfix: add session_tracker.py to files[] |
| `99040592` | Hotfix: rebuild zip from _build_tmp/ with vendored deps |

## Post-Deploy Regressions

### Regression 1: `Runtime.ImportModuleError: No module named 'session_tracker'`

- **Cause:** Source map files[] only listed `lambda_function.py`. `session_tracker.py`
  (imported at line 78) was excluded from the zip.
- **Fix:** Added `session_tracker.py` to files[] in lambda-source-map.json.
- **Tag:** `market-overview-v1.6.6`

### Regression 2: `503 -- OpenAI not available in this environment`

- **Cause:** `build-and-upload.sh` only zips files listed in the source map's files[]
  array. The portal_data_proxy Lambda has vendored Linux wheels for openai, pydantic,
  pydantic_core, httpx, etc. in a `_build_tmp/` directory (~2,800 files, 8 MB).
  The build script produced a 28 KB zip with just 2 .py files instead of the full
  8 MB deployment package.
- **Root cause of root cause:** The source map _note said "extract production zip,
  swap lambda_function.py, rezip" but build-and-upload.sh does not implement that
  workflow -- it only zips files[]. The note was documentation, not enforcement.
- **Fix:** Rebuilt zip from `_build_tmp/` directory which contains the complete
  vendored environment with pre-compiled Linux wheels. Added `_build_note` to
  source map to prevent future misuse of build-and-upload.sh for this function.
- **Tag:** `market-overview-v1.6.7`

## Lessons Learned

1. **build-and-upload.sh is not universal.** Functions with vendored deps in
   `_build_tmp/` cannot use the standard build script. The script only zips
   files[] entries from source_dir, not the full deployment directory.

2. **Source map _note fields are advisory, not enforced.** The note correctly
   warned against rebuilding, but nothing prevented build-and-upload.sh from
   producing an incomplete zip. The new `_build_note` field makes the constraint
   more visible but still relies on operator awareness.

3. **Import errors mask the real deployment.** The Lambda crashed on `import`
   before any handler code ran, producing API Gateway's generic
   `{"message":"Internal Server Error"}` -- identical to the original bug symptom
   but with a completely different cause.

## Status

Task order marked **complete**. All acceptance criteria met pending manual
verification of TopicCloud keyword clicks in the portal.
