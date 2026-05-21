# ADVI_INFGRO.009 — INF_C_02 TWR-factor repoint (Method Y) — 2026-05-20

**Agent:** 0.4.0_DS_ClientPlatform (DS Base)
**TO:** ADVI_INFGRO.009.dsc-infc02-twr-factor-rebuild-method-y
**Branch:** CLOUD
**Status:** COMPLETE — Phase 1 verified, item 4 shipped, Phase 2 full-rebuild chain run + AC5 PASS. RAVC2 to COO CC CTO.

## Routing context

TO was `issued_to 0.4.0_DS_ClientPlatform~C` — a phantom lane (no live DS~C
agent). COO re-routed `issued_to` to the base serial `0.4.0_DS_ClientPlatform`
(commit `92367327b`); INF_C_02 / pull_inflection_performance_rest.py are
in-domain Client Platform base-lane scripts. Picked up on the base serial.

## Current State

The Phase-1 code (the INF_C_02 `_build_daily_factor_table` repoint + the
windowed-pull puller) was already shipped 2026-05-18 by the DS~C lane —
commits `38410e1dd` (Method-Y windowed performance pull + INF_C_02 fix) and
`4a40cd450` (Option-A repoint of the daily-factor table to silver/performance/).
Both are on origin/CLOUD and S3-deployed (md5 MATCH, see Compiler Tools).

This session: empirically VERIFIED the Phase-1 fix clears Finding B, executed
amendment item 4 (orphan retirement), and surfaced the Phase-2 full-rebuild
chain run to COO for trigger coordination.

### Phase-1 verification (read-only)

A read-only `INFINC_REBUILD=true` dry-run of INF_C_02 against current S3 +
a faithful replication probe of the full-rebuild decomposition:

| Metric (last-90d abs-contribution share) | Deployed gold | Rebuilt (repointed) |
|---|---|---|
| return_$ | 14.9% | 59.2% |
| epsilon_$ | 73.7% | 35.8% |
| nna_$ | 11.3% | 5.0% |

- All-history rebuilt: return 67.5% / epsilon 22.1% / nna 10.3%.
- Daily identity (aua_change = nna + return + epsilon) fails = 0 / 419,243.
- Decomp coverage 99.9% (419,243 / 419,571 rows).
- return_pct_twr p1/p99 = -1.67% / +1.56% — plausible daily returns.
- Epsilon abs: deployed median $490 -> rebuilt median $0, p95 $315.

Finding B's AC5(b) gate (epsilon no longer the dominant decomposition term)
is met by the fix. The deployed gold still shows epsilon-dominance only
because today's 14:46Z daily chain ran INF_C_02 in append-only mode — it
recomputes only the trailing date; historical rows retain pre-repoint values.
The TO-mandated `INFINC_REBUILD=true` full re-materialization is the single
remaining step.

### Amendment item 4 — orphan retirement (DONE)

`git rm data/orion/scripts/silver/INF_C_03.performance_canonical.py` — commit
`bc70e6995`, pushed to origin/CLOUD. Re-verified before removal it is a true
orphan: it writes `silver/performance_dim/` (a path nothing reads post-repoint;
frozen 2026-05-13, no live producer) and is NOT in the orion-gold-dispatch.sh
chain (chain `INF_C_03` = `INF_C_03.account_performance.py`). The
`INF_D_00c/D_02/D_04` `load_performance_dim()` functions read a DIFFERENT path
(`silver/api_dims/performance/`) — a function-name collision, not a consumer
of `silver/performance_dim/`. CTO "only consumer" claim confirmed.

Gate gap noted: the safe-deploy pre-push hook is not deletion-aware
(`LOCAL_MISSING` on a git-rm'd `.py`). Used the documented audited bypass —
`safe-deploy.sh --allow-stale --reason ...` (logged to
`org/safe-deploy-bypass-audit.log`) then `git push --no-verify`. Flagged to
COO for an AE/tooling follow-up.

## Phase 2 — full-rebuild chain run + AC5 (COMPLETE)

The TO's verbatim Phase-2 trigger (`INFINC_REBUILD=true bash orion-gold-dispatch.sh
--from INF_API_SILVER_PERF --bg`) was empirically WRONG on TWO counts:

1. **Env-var clobber (AE 0.7.0 caught).** `orion-gold-dispatch.sh` PRODUCES
   `INFINC_REBUILD`, it does not consume it — line 1074 `export INFINC_REBUILD="$REBUILD"`
   overwrites any passed env var; rebuild mode is set only by the `--rebuild` CLI
   flag, inert unless `INFINC_PHASE1=1` (line 1081). AE fired the verbatim form,
   environ-verified `INFINC_REBUILD=0` on the running chain, killed it.
2. **Value-format mismatch (DS caught).** Even with `--rebuild`, the dispatch
   exports `INFINC_REBUILD="1"`, but INF_C_02's `_force_rebuild` gate checked
   `== 'true'` — `'1' != 'true'` → INF_C_02 would have stayed append-only.
   Fixed: `_force_rebuild` now accepts the canonical `'1'` (per `lib/skip_gate.py:128`)
   plus truthy synonyms. Commit `4ccbce567`, S3-deployed (md5 715301cb… verified).

Corrected invocation (DS-ratified, Rule 13): `INFINC_PHASE1=1 bash
orion-gold-dispatch.sh --from INF_API_SILVER_PERF --rebuild --bg`. AE fired it
2026-05-20 23:11Z, pre-verified environ `INFINC_PHASE1=1 + INFINC_REBUILD=1` +
runner INF_C_02 md5 == `4ccbce567`. Chain COMPLETE 23:57Z — 46/46 steps, ~42 min.
INF_C_02 logged `INFINC_REBUILD='1' — full rebuild`; identity fails=0/419,243.

**Systemic finding (surfaced to COO):** the identical `== 'true'` bug is in 4 more
scripts — `INF_C_03.account_performance.py:150`, `INF_D_05/06/09` — all off the
.009 AC5/leaderboard path; recommended as a follow-up TO.

### AC5 verification — PASS (both PRD §8.5 gates)

Against the rebuilt artifacts (`gold/timeseries/client_performance.parquet`
23:47:20Z, `platinum/firm/leaderboard.json` 23:51:24Z):

- **AC5(a) window-TWR absolute scale — MET.** leaderboard.json window
  `advisor_return_pct_twr`: QTD ~5.0-6.8%, YTD ~4.6-6.0%, 1Y ~14.3-19.1%,
  3Y ~40.6-46.8%, MAX ~59.8-71.2% — all plausible absolute-scale returns; the
  Finding-A ~6x understatement is gone (`return_$` abs-sum $208M → $815M, ~4x).
- **AC5(b) epsilon non-dominance — MET.** Rebuilt gold last-90d abs-contribution
  shares: return 59.1% / epsilon 35.8% / nna 5.1% (was 14.9% / 73.7% / 11.3%
  pre-rebuild) — return dominant, return+nna explain the majority. Leaderboard
  `advisor_return_$` dominates `advisor_epsilon_$` in all 5 windows. Matches the
  pre-rebuild dry-run prediction (epsilon 73.7% → ~35.8%) to the tenth of a point.

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/INF_C_02.client_performance.py | `_force_rebuild` gate accepts canonical `INFINC_REBUILD='1'` + truthy synonyms (commit `4ccbce567`) — Phase-2 trigger bug #2 |
| data/orion/scripts/silver/INF_C_03.performance_canonical.py | DELETED (git rm) — orphaned silver producer, amendment item 4 (commit `bc70e6995`) |

(Phase-1 code edits — INF_C_02 repoint + windowed-pull puller — landed 2026-05-18 under commits 38410e1dd / 4a40cd450.)

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io INF_C_02.client_performance` | RESOLVED — READS accounts_dim + client_performance.parquet; WRITES gold/timeseries/client_performance.parquet -> INF_C_04, INF_C_06, INF_D_00/00b/00d/04/05a (matches PRD section 8.4 consumer set). |
| `comp-pipescript deployed INF_C_02.client_performance` | Non-resolving — comp-pipescript `deployed` is scoped to `s3://opal-data-bd/` only; the INF/orion pipeline (`opal-data-inf`) is off that tool's scope. Substituted a direct md5 verify: deployed `code/gold/INF_C_02.client_performance.py` + all 3 `pull_inflection_performance_rest.py` copies (gold/manual_api/bronze) == repo HEAD == origin/CLOUD. MATCH on all 4. |
| `comp-pipescript postdeps INF_C_02.client_performance` | "No dependencies declared for inf_c_02" — no blocking post-steps; the chain run covers downstream. |
| `.tools/safe-commit.sh` | Used for commits `bc70e6995` + `4ccbce567`; staged index scoped to the declared pathspec each time. |
| `.tools/ds-commit-gate.sh` | Exit 0 on `INF_C_02.client_performance.py` (Phase-2 bug-#2 fix) — py_compile + AST scan + ruff all clean. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — ADVI_INFGRO.009 COMPLETE, AC1-AC7 met; AC5 PASS (both PRD §8.5 gates). On RAVC3-accept this clears INFGRO.005 for partner-facing → unblocks DE~B's INFGRO.005/.006. |
| **CTO 1.0.0** | CC on RAVC2 — Finding A + Finding B both cleared by the one INF_C_02 root fix, as PRD §8.4 predicted. |
| **COO 2.0.0 (follow-up)** | Systemic `INFINC_REBUILD == 'true'` bug class — INF_C_03/D_05/D_06/D_09 (4 scripts) still mismatch the canonical `'1'` contract; recommend a small follow-up TO (identical 1-line fix ×4). Off the .009 path. |
| **AE / tooling** | safe-deploy gate is not deletion-aware — a commit that git-rm's a `.py` fails the pre-push hook with LOCAL_MISSING. Follow-up to make deletions pass cleanly. |
