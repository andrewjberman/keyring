# 0.4.0_DS_ClientPlatform~A -- build_canonical_daily.py --date compact/hyphenated normalization (CVO flag, durable close)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE
**window:** 2026-07-01 ~1834Z -> 1853Z (COO redirect after INFREF ROOT-2 close) | **serial:** 0.4.0_DS_ClientPlatform~A | **branch:** CLOUD

## HEADLINE
Durably closed the CVO compact-date flag on `build_canonical_daily.py`: `--date` now accepts BOTH compact `YYYYMMDD` and hyphenated `YYYY-MM-DD`. Prepped + tested, held for the 0.5.0 active-use gate, landed **b96326b22** after 0.5.0 released the file.

## Root cause + fix
The /49-schwab-conv skill derives `$LATEST` as **compact** `YYYYMMDD` (line 94/96 -- correct for the schwab-silver `date=` partition checks) but reused it at line 111 for `build_canonical_daily.py --date`, which assumed **hyphenated**. Compact input crashed `position_t0`'s `strptime('%Y-%m-%d')` (L119) and produced a `NoSuchKey` in `build_gold_holdings` (CVO flag 2026-07-01, hit on the 06-25 canonical).
Fix (script-side durable): added `_normalize_date()` (accepts compact/hyphenated, validates + fails loud on bad dates) and normalized `args.date` **once** in `main()` (`t1 = _normalize_date(args.date) or latest_rps_date()`, wrapped in try/except -> rc=1 on bad date) before it flows to any downstream. + `import re`. + SKILL.md Step-7.5 note (both forms accepted). Zero behavior change for existing hyphenated callers.

## Verification
- ds-commit-gate: clean (py_compile + AST).
- Unit: `_normalize_date` -- `20260625`/`2026-06-25`/`  20260618  `/`""` all resolve correct; `20261340` -> ValueError (fail-loud).
- Crash-site proof: `strptime('20260625','%Y-%m-%d')` raises (the original bug); `strptime(_normalize_date('20260625'))` works.
- E2E: `python build_canonical_daily.py --date 20260625 --dry-run` -> header `date=2026-06-25`, every downstream PLAN gets hyphenated, exit 0 (read-only, no writes/subprocess in dry mode -- safe during 0.5.0's run).

## Coordination (the seam)
COO's gate: no mid-active-use script change (0.5.0_AE_OpalETL was mid the 06-26..30 canonical roll-forward). I PREPPED + TESTED, held the commit/push (push=safe-deploy), pinged 0.5.0 + RAVC'd COO. 0.5.0 then RELEASED it -- its roll-forward was SUPERSEDED by Andrew's ruling (MDPF 49F custody -> Schwab-native basis switch; provenance found MDPF reads bd/silver/allocations + FEES-crosswalk frozen 06-25, NOT Schwab RPS silver). Landed on the free-ping. COO pre-accepted the prepped fix (RAVC) + accepted the land.

## Land
Commit **b96326b22** on origin/CLOUD (verified HEAD==origin/CLOUD). `build_canonical_daily.py` is a REPO-RUN script (skill invokes it directly) -> safe-deploy: no-deploy-scope, so commit+push IS the land (origin==local = the deployed-MATCH analog). 2 files: `data/canonical/schwab/build_canonical_daily.py` + `.claude/skills/49-schwab-conv/SKILL.md`. Pathspec-scoped via safe-commit (shared worktree had unrelated dirty files from other agents -- excluded).

## Current State / Next Steps
- CVO compact-date flag DURABLY CLOSED; next Schwab pull is trip-proof regardless of doc form.
- [incoming] Basis-switch project (0.5.0 authoring design brief via COO): MDPF 49F custody -> Schwab-native touches my lane -- `compute_partner_custody_total` / `build_mdpf_wse_49f_non_model_aua.py` (remove the frozen bd/silver/FEES-crosswalk dependency). Offered 0.5.0 an early DS read; will pick up on the COO project/TO.
- INFREF ROOT-2 (prior window): closed + tri-attested (fix 4cf997274, holdings/perf 06-26 re-emitted). Residual C_02/C_03 self-heals on nightly under CVO L6.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| ds-commit-gate.sh | py_compile + AST on build_canonical_daily.py (pre-commit, twice) | clean both times |
| comp-pipescript deployed | check if build_canonical_daily.py is S3-deployed | no match -> REPO-RUN script (commit+push is the land; no S3 deploy) |
| comp-grep | locate build_canonical_daily.py + the /49-schwab-conv Step-7.5 refs | found; grounded the $LATEST compact-vs-hyphenated mismatch |

**What worked:** the compact-vs-hyphenated grounding came straight from the skill's own `$LATEST` derivation (line 94 `# e.g. 20260618`) -- the doc showed the exact defect. Dry-run mode short-circuits all subprocess/writes -> safe e2e test during another agent's active run.
**What failed:** a verification helper wrote to `/tmp` (invalid on Windows Git Bash -> `C:\tmp`); cosmetic, re-run unnecessary (committed file == tested working-tree file).
**Gap found:** none new.

## Blockers
NONE. Fix landed + RAVC-closed. Basis-switch follow-on is a future project (not yet chartered) -- not a blocker.
