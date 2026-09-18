# Deploy Completion Record
**Date opened:** 2026-09-18T03:39:42.417402+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-rtc-2 AMENDMENT 1 (R-45): DISTRIBUTION flag + 9 repo-path members re-minted to opal-data-mdpf investor_reporting; one real commit to the COT runner_common deployed on BOTH legs through safe-deploy; a one-leg MUTANT (stale-tree re-mint) then a restore re-mint. Blast radius: s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (versioned; pre-cell VersionId AxKzxFHuxAP7TTIJsmkxtWZxxgEgVJDC) and s3://opal-data-cot/code/gold/runners_cot/runner_common.py (versioned; pre-cell VersionId vrG96E7lhDeuxXs0IZigxHF0arWLhu_L, a comment-only change). Rollback per key: re-deploy the prior commit's bytes through safe-deploy (never a bare copy). Consumers: the ENABLED irpt-directory-refresh dispatch (13:00Z) reads the bundle and cannot use repo-path names until IB-rtc-3's unpack lands (its build already failed before this, rows S59/W2-S51); the COT gold runners read runner_common.py (comment-only).
**Authored by:** 0.4.0_DS_ClientPlatform~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the guard's DISTRIBUTION flag + route_bundle_members + its tests + the 9 repo-path members (3 flagged) on wk-irpt_bckend-3-ds2 | commit hash |  | OPEN |
| L2 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting: the explicit re-mint (safe-deploy.sh --mint-bundle investor_reporting) | BUNDLE MINTED line + head-object ETag/VersionId + 9 per-member sha stamps + source-repo-paths |  | OPEN |
| L3 | git | a REAL commit to one DISTRIBUTION member: data/cot/scripts/gold/runners_cot/runner_common.py (a comment block naming its two legs) | commit hash |  | OPEN |
| L4 | s3-prefix | the QA-deploy of L3 through safe-deploy.sh --commit-range: opal-data-cot code/gold/runners_cot/runner_common.py (loose) AND the bundle re-mint | the guard's DEPLOYED + BUNDLE MINTED + comp-pipescript VERIFY lines; loose ETag and VersionId before/after |  | OPEN |
| L5 | verify | two-leg CONSISTENCY after L4, 3 of 3 DISTRIBUTION members (consistency_ib_rtc_2.py) | the checker's CONSISTENT line with per-member ETag/md5 and sha256/sha256 |  | OPEN |
| L6 | verify | the MUTANT: a --mint-bundle from a worktree at the pre-L3 commit advances ONLY the bundle leg; the checker must read DIVERGED on the COT member; then a --mint-bundle from the tip restores and the checker reads CONSISTENT | both checker outputs + the mutant and restore VersionIds + the COT loose key's version count unchanged across the window |  | OPEN |

## Log

- 20260918T033942Z OPENED by 0.4.0_DS_ClientPlatform~X with 6 leg(s)
