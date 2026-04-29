# Session Log -- ADHC_OWNPTH.008: record-terraform-deploy.sh -> safe-commit.sh

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-29
**TO:** ADHC_OWNPTH.008.ae-record-terraform-deploy-safe-commit
**Issued by:** 1.0.0_SA_CTO
**Status:** COMPLETE
**Commit:** aa004108b

---

## Scope

Migrate `infra/aws/lambda/ci/record-terraform-deploy.sh` to commit via
`.tools/safe-commit.sh` instead of bare `git commit`. Adds `--author` flag,
preserves default behavior when flag omitted. Updates CLAUDE.md Rule 14a with
appendix.

## Why

4th observed sweep incident driven by record-terraform-deploy.sh
(`fe5a773f`, 2026-04-28: DT 0.1.0 news-pipeline log swept into AE 0.7
inf-pipeline deploy commit). TO 7 shipped the wrapper; this TO migrates the
loudest known offender to use it. Andrew direct quote (2026-04-22): "this keeps
happening -- propose owned-paths pre-commit hook, not more rules."

## Files Changed

| File | Change |
|------|--------|
| `infra/aws/lambda/ci/record-terraform-deploy.sh` | --author flag; replace bare `git commit` with `.tools/safe-commit.sh` invocation; usage block expanded |
| `CLAUDE.md` | Rule 14a appendix paragraph (1 paragraph; --author + contamination-abort note) |

## Patch Detail

### Argument parser (lines 38-51 -> 38-56)
Added:
```bash
RECORD_AUTHOR=""
        --author)
            RECORD_AUTHOR="$2"
            shift 2
            ;;
```

### Usage block
Added `--author <ident>` doc line + 4-line note on safe-commit abort behavior.

### Commit invocation (line 397 -> 407-432)
Replaced:
```bash
git commit -m "ci: record deploy ${PIPELINE} @ ${COMMIT_SHORT} [skip ci]
...
Recorded by: record-terraform-deploy.sh"
```
With:
```bash
PATHSPEC=("infra/aws/lambda/ci/lambda-source-map.json")
if [ "$CHANGELOG_WRITTEN" = true ]; then
    PATHSPEC+=("infra/aws/terraform/${PIPELINE}/CHANGELOG.json")
fi

AUTHOR_ARGS=()
if [ -n "$RECORD_AUTHOR" ]; then
    AUTHOR_ARGS=(--author "$RECORD_AUTHOR")
fi

"$WORKSPACE_ROOT/.tools/safe-commit.sh" \
    "${AUTHOR_ARGS[@]}" \
    -m "ci: record deploy ${PIPELINE} @ ${COMMIT_SHORT} [skip ci]
... (same trailer)" \
    -- "${PATHSPEC[@]}"
```

`set -e` at script top ensures safe-commit.sh non-zero exit kills the script
(verified in canary B).

Lines 252-266 (early-exit on unchanged source-map) **structurally preserved** --
no edits to that branch. Diff inspection confirmed.

## Canaries (temp git harness)

Built throwaway repo at `C:/Users/AndrewBerman/AppData/Local/Temp/rdeploy-canary-7521`
(used Windows-native path so bun could resolve source-map writes; `/tmp/` paths
silently fail under MSYS bun). Repo contained:
- `.tools/safe-commit.sh` (copy of real wrapper)
- `infra/aws/lambda/ci/record-terraform-deploy.sh` (the patched script)
- `infra/aws/lambda/ci/lambda-source-map.json` (1 stub function on test-pipeline)
- `infra/aws/terraform/test-pipeline/` (target dir for CHANGELOG.json)
- `infra/aws/lambda/test_function/handler.py` (stub source)
- `org/git-author-override-audit.log` (touch)

| Canary | Setup | Expected | Result |
|--------|-------|----------|--------|
| A clean index, no --author | clean index, fn bumped | commit lands; source-map + CHANGELOG only; default git identity | PASS exit 0; 2 files; AUTHOR=TestDefault `<test-default@opal.test>` |
| B contaminated index | unrelated `org/.../unrelated_v2.md` pre-staged | safe-commit.sh aborts exit 1; no commit; unrelated file still staged | PASS exit 1; HEAD unchanged; staged set retained source-map + CHANGELOG + unrelated_v2.md |
| C --author plumbing | clean; `--author "0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>"` | commit author = exact string | PASS AUTHOR=0.7.0_AE_CloudOps `<0.7.0_AE_CloudOps@opal.agent>` |
| D no --author default identity | clean; no flag | author = git config identity | PASS (covered by canary A: AUTHOR=TestDefault default) |
| Phase 3 short-circuit | run on no-op state | "Source map unchanged" early exit, no commit | NOT REPRODUCIBLE in harness (bun JSON tool rewrites timestamp every run, so source-map always diffs vs HEAD); structural preservation verified via diff -- lines 252-266 unchanged. This is pre-existing behavior, not caused by my patch. |

Canary B output (verbatim):
```
ERROR: staged index contains files not in declared pathspec.
       Commit aborted. Use --force to bypass (logs to audit).

Declared pathspec (2 file(s)):
  infra/aws/lambda/ci/lambda-source-map.json
  infra/aws/terraform/test-pipeline/CHANGELOG.json

Contaminating staged files (1):
  org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-04-29/unrelated_v2.md
```

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 -- before edit | `git diff --cached --name-only` | Empty -- clean index. PASS |
| 1 -- before edit | `ls -la .tools/safe-commit.sh && bash .tools/safe-commit.sh --help` | exists, exec-bit set, --help works (5155 bytes). PASS |
| 2 -- after edit, pre-commit | `bash -n infra/aws/lambda/ci/record-terraform-deploy.sh` | exit 0, syntax OK. PASS |
| 2 -- canary A | clean index record-deploy | exit 0, 2-file commit, default identity |
| 2 -- canary B | contaminated index record-deploy | exit 1, no commit, file preserved |
| 2 -- canary C | --author flag | author exact match |
| 2 -- canary D | no --author | default identity |
| 3 -- after commit | `git show --stat HEAD` | 2 files (CLAUDE.md + record-terraform-deploy.sh); author=0.7.0_AE_CloudOps. PASS |

## Owned-Paths Hook Note (informational)

Pre-commit hook fired WARN on the commit:
```
VIOLATION: CLAUDE.md -- lane=BASE_EXEC (Base workspace execs - CTO + COO);
agent=0.7.0_AE_CloudOps not in permitted_agents
```

This is correct: CLAUDE.md is in the BASE_EXEC lane (CTO/COO ownership). The
TO scope item 4 explicitly tasks AE with the appendix edit, so the warn is
operationally expected. Two options for CTO awareness:
- Accept WARN as documented exception for AE-issued TOs touching CLAUDE.md.
- Update `.owned-paths.yaml` to permit AE on CLAUDE.md when explicitly tasked
  (not recommended -- broadens the lane).

Logged in `org/git-author-override-audit.log` as WARN (not FORCE-BYPASS, no
contamination), 2026-04-29T12:25:34Z.

Recommendation: accept as one-off; CTO can decide whether to track or ignore.

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Bare `git commit` at line 397 replaced with safe-commit.sh + explicit pathspec | PASS |
| 2 | --author flag added, optional, defaults preserved | PASS |
| 3 | Canary A clean | PASS |
| 4 | Canary B contaminated | PASS |
| 5 | Canary C --author | PASS |
| 6 | Canary D default | PASS |
| 7 | Phase 3 short-circuit | Structural preservation verified via diff |
| 8 | Session log with all canary outputs | PASS (this log) |
| 9 | CLAUDE.md Rule 14a appendix | PASS (1 paragraph appended) |
| 10 | MCP CTO + COO with commit hash | PENDING (next step) |

## Out of Scope (Per TO)

- Other deploy scripts (`build-and-upload.sh`, `safe-ec2-deploy.sh`, EC2
  service deploy scripts) -- TO 10+ if Andrew prioritizes.
- Org-wide broadcast of safe-commit adoption -- deferred per ADHC_OWNPTH.json
  (until TO 4 observe-week results).
- Retroactive author fix on `fe5a773f`.
- CHANGELOG.json `agent` field cosmetic ('devops_technician' hardcode at line
  341) -- separate issue.

## Next Steps

- MCP 1.0.0_SA_CTO: TO 8 COMPLETE, commit aa004108b, all 4 canaries PASS,
  flag the CLAUDE.md owned-paths WARN for awareness.
- MCP 2.0.0_SA_COO: same closeout; org-wide deployment runbook references
  may want a one-liner about the new contamination-abort behavior.
- TO 8 status flipped to complete with completed_date + completed_commit.
- 4th sweep incident now has structural close. ADHC_OWNPTH.json project status
  note ("re-evaluate if 4th sweep incident occurs in next 48h") is satisfied
  by this TO -- CTO/COO can decide whether to fast-track ADHC_OWNPTH.005 Phase
  2 fail-closed flip given the 5+ sweep events in the 12h window before TO 7
  shipped.
