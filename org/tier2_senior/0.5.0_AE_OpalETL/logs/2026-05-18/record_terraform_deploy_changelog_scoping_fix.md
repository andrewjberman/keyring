# 0.5.0_AE_OpalETL Session Log -- 2026-05-18 (record-terraform-deploy CHANGELOG-scoping fix)

**Agent:** 0.5.0_AE_OpalETL
**Date:** 2026-05-18
**Branch:** CLOUD
**TO:** record-terraform-deploy-changelog-scoping-fix (COO)
**Headline:** Fixed the CHANGELOG writer's two bloat causes (wrong git-log RANGE + no PATHSPEC) and compacted 8 bloated CHANGELOG.json files -- inf-pipeline 88,832 -> 1,490 lines. ~127k lines of derived bloat removed; zero deploy history lost.

---

## The bug -- two causes (not one)

The TO context assumed one cause (repo-wide git-log). Pre-investigation found two:
1. **RANGE.** `commits[]` was `git log PREVIOUS_COMMIT..commit`. `get_previous_commit()` returns the FIRST pipeline-Lambda's `last_deployed_commit` -- post-ADHC_DRIFTD.001 those are per-Lambda CONTENT commits. A stable Lambda keeps an ancient one, so the range stretched over ~1986 commits, not "since the last deploy."
2. **PATHSPEC.** The git-log was repo-wide -- no restriction to the pipeline's own paths.

`functions_updated` bloated from the same wrong range. COO approved fixing both (the range fix completes Phase 1's intent; not scope creep).

## Phase 1+2 -- writer fix (`infra/aws/lambda/ci/record-terraform-deploy.sh`)

The TMPJS_CHANGELOG JS block, restructured:
- Read + normalize the existing CHANGELOG FIRST; `rangeStart = cl.entries[0].deployed_commit` (the true last-deploy marker). `PREVIOUS_COMMIT` retained as the first-ever-deploy fallback.
- Build a pipeline pathspec: each managed Lambda's `source_dir` (non-EXTERNAL) + the pipeline's Terraform dir.
- `commits[]`: `git log <rangeStart>..<commit> -- <pipeline pathspec>`.
- `functions_updated`: per-function `git log <rangeStart>..<commit> -- <source_dir>` -- same corrected range.
- ADHC_DRIFTD.003 NUL-safe `%x1f` parsing + `parts.length===4` guard preserved verbatim. Legacy array-form handling preserved. `previous_commit` entry field left unchanged (out of scope). ADHC_DRIFTD.001 untouched.

## Phase 3 -- one-time compaction of existing CHANGELOGs

`.runtmp/compact_changelogs.py` (throwaway). Conservative: touches ONLY entries whose `commits[]` exceeds 100; reconstructs each via `git log` between adjacent entries' `deployed_commit` (oldest entry falls back to its own `previous_commit`), pathspec-restricted. Reconstruction failure would fall back to cap-at-25-with-note (0 needed -- all 28 reconstructed). Only the `commits[]` field is rewritten; entry count + every other field invariant.

| Pipeline | lines before | lines after | oversized entries reconstructed |
|----------|-------------|-------------|------|
| inf-pipeline | 88,832 | 1,490 | 8 (1986/1951/.../1636 -> 2-59) |
| bd-pipeline | 17,332 | 5,992 | 8 |
| portal-auth | 16,564 | 1,888 | 5 |
| news-pipeline | 8,853 | 2,001 | 2 |
| yang-pipeline | 6,958 | 4,378 | 1 |
| data-refresh | 1,983 | 411 | 2 |
| market-overview | 1,926 | 876 | 1 |
| smartx-pipeline | 1,974 | 102 | 1 |

Total: 144,422 -> 17,138 lines (~127k removed). 28 entries compacted across 8 files. Untouched files (no oversized entry): exec-summary, partner-firms, portfolio-management, security-scanner-pipeline, shared-infra, trade-pipeline.

**Verification:** entry COUNT unchanged per file (jq, 8/8 OK). `diff` of `jq 'del(.entries[].commits)'` pre vs post = empty for all 8 -> ONLY `commits[]` changed; version/date/functions_updated/artifacts/all metadata byte-identical.

**Out-of-scope finding (flagged to COO):** `infra/aws/terraform/partners-api/CHANGELOG.json` is pre-existing MALFORMED JSON -- a valid object, then a dangling fragment, then a duplicate object (line 221+). Not bloated (232 lines). Compaction skips it (skip-and-warn). It also currently breaks `record-terraform-deploy.sh`'s CHANGELOG write for partners-api (JSON.parse throws). Separate issue -- recommend a follow-up TO; NOT repaired here.

## Phase 4 -- writer-fix verification

`.runtmp/verify_writer.sh` -- extracted the patched JS, simulated a deploy against temp CHANGELOG copies (no real file touched):
- **inf-pipeline at HEAD:** range anchored on the last entry's `deployed_commit` (`7a10ddc...`). Unscoped count over that range = 23 (the range fix alone: 1986 -> 23). Scoped `commits[]` = **1**, `functions_updated` = **0** (pathspec fix: 23 -> 1). New entry unshifted (10 -> 11).
- **first-deploy fallback (no prior CHANGELOG):** rangeStart falls back to `PREVIOUS_COMMIT`; entry written, object-form `{_description,_pipeline,entries}`, no crash.

## Compiler Tools

| Tool / mandate run | Result |
|--------------------|--------|
| `sed -n '400,540p' record-terraform-deploy.sh` (Phase-1 mandate) | CHANGELOG writer block reviewed -- git-log fetch, gitLogRecords, updatedFunctions, legacy-array handling located; edit grounded in current code. |
| `for f in infra/aws/terraform/*/CHANGELOG.json; do wc -l ...` (Phase-3 mandate) | Post-compaction line counts materially reduced (table above); inf-pipeline 88,832 -> 1,490. |
| jq entry-count check (8 files) | All 8: count unchanged pre vs post. |
| comp-* infra tools | N/A -- CI tooling + JSON record-file edit; no S3/IAM/Lambda runtime surface. |

## Current State

- record-terraform-deploy.sh writer fix + 8 compacted CHANGELOG.json files: complete, committed, pushed.
- partners-api/CHANGELOG.json corruption flagged to COO (out of scope).
- Pipeline tags unchanged.

## Next Steps

- `[2.0.0_SA_COO]` RAVC2 validation AC1-5. Consider a follow-up TO for the partners-api/CHANGELOG.json corruption.
- `[0.7.0_AE_CloudOps]` awareness -- record-terraform-deploy.sh diff sent; CI tooling lane-adjacent.
- `.runtmp/compact_changelogs.py` + `verify_writer.sh` -- throwaway, leave or delete.
