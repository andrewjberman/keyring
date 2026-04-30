# Session Log: ADHC_COMPIL.014 + ADHC_COMPIL.015
**Date:** 2026-04-30
**Agent:** 0.7.0_AE_CloudOps
**TOs:** ADHC_COMPIL.014 (comp-shell), ADHC_COMPIL.015 (validate resolver + noconfig)

---

## Session Summary

Both TOs completed in sequence (user direction: "do both of them i dont care the order").
.015 was executed first (builds on .009 which was already COMPLETE); .014 followed.

---

## ADHC_COMPIL.015 — Validate Resolver + NO_CONFIG Exit Semantics

### Fix 1: Script-id alias resolver

Root cause of the 12 FAIL→retry pairs: operators pass `D_04` (producer script-id)
when comp-validate configs are keyed on artifact-id (`cohort_a_summary`, `leaderboard`,
etc.). The resolver now checks the alias_map FIRST when an artifact filename is provided,
before direct artifact-id lookup. This correctly handles `D_04` being BOTH a direct
artifact-id (leaderboard) AND a producer script for 4 artifacts.

Key design decision: alias_map takes priority over direct lookup when artifact_filename
is provided. Without this, `D_04 + cohort_a_summary.json` would silently match the
leaderboard artifact config and run wrong checks.

Added `_emit_ambiguous_error()` helper to centralize the multi-artifact candidate list.

Added `producer_script:` field to all 11 BD config entries and 6 INF config entries
in both `gold_validate_config.yaml` files.

### Fix 2: MISSING_ARTIFACT and NO_CONFIG exit semantics

- `MISSING_ARTIFACT`: now exits 1 (was silent PASS). Header printed to stderr, dual-path
  error shown on Windows.
- `NO_CONFIG`: exits 0 with `NO_CONFIG: no validation rules defined for <id>` status line.
  `--strict` flag escalates to exit 2.
- Machine-readable status line prefixes: PASS:/NO_CONFIG:/MISSING_ARTIFACT:/FAIL:

### AC verification

All 15 ACs pass in `tests/comp_validate/test_resolver_and_status.sh`.

Tricky AC: AC9/AC10 (NO_CONFIG) required using an INF-only id (`INF_09`) that has no
partial match in BD config. `INF_D_04` (initially tried) matched D_04 via partial match
and ran the wrong checks.

### Commits

| Hash | Author | Description |
|------|--------|-------------|
| ee613f913 | 1.0.0_SA_CTO | feat(ADHC_COMPIL.015): script-id alias resolver + NO_CONFIG/MISSING_ARTIFACT |
| c1651ff7a | 0.4.0_DS_ClientPlatform | feat(ADHC_COMPIL.015): producer_script: fields in BD + INF configs |
| 615722995 | 1.0.0_SA_CTO | docs(ADHC_COMPIL.015): COMP_VALIDATE_PROTOCOL.md §10 |
| daa72fb83 | 0.7.0_AE_CloudOps | test(ADHC_COMPIL.015): test_resolver_and_status.sh 15 ACs |
| 9e584808d | 0.7.0_AE_CloudOps | log(ADHC_COMPIL.015): AC1-AC15 rows + TO status=complete |

---

## ADHC_COMPIL.014 — comp-shell Tool

### Design

Scanner in `org/modules/graph/shell_cli.py`. Detection logic:
- 6 forbidden utilities: pgrep, pkill, flock, pidof, setsid, wget
- Filters: comment lines, heredoc bodies, single-quoted strings
- Guard detection: `command -v <util>` or `which <util>` within 30-line lookback
- UNGUARDED → ERROR (blocks); GUARDED → WARN (advisory)
- Exit 0 = no ERROR; 1 = ERROR found; 2 = usage error

Exempt paths: `infra/aws/ec2/`, `infra/ec2/`, `data/`, `worktrees/`, `.tmp/`, `codex2/`
(per Rule 16: these paths run on Amazon Linux where all utilities are available).

### AC10 baseline scan findings

Rule-16 in-scope paths (`.tools/`, `org/mcp/`, `org/threads/`, `infra/aws/lambda/ci/`,
`infra/aws/terraform/`): **0 ERROR, 4 WARN** (all guarded pgrep in inbox-watch.sh files).

Workspace-wide `--all`: 2 remaining ERRORs are expected/known:
1. `scripts/_DEPRECATED_LOCAL_CRON/cron_health_monitor.sh` — deprecated script, not in
   Rule-16 scope, pre-commit hook will not touch it
2. `tests/comp_shell/fixtures/01_bare_pgrep.sh` — intentional test fixture

AC11 escalation check: no unexpected ERRORs in in-scope paths → hook shipped.

### ds-commit-gate.sh extension

Added .sh handling: for staged .sh files in Rule-16 in-scope prefixes, runs
`comp-shell scan`. Out-of-scope .sh (EC2-side, data scripts, deprecated) silently skipped
(counter stays 0, gate passes). EC2 test verified: `infra/aws/ec2/` script with bare
pgrep → `OK: pre-commit gate clean for 0 file(s)`.

### Commits

| Hash | Author | Description |
|------|--------|-------------|
| 74a1ade33 | 1.0.0_SA_CTO | feat(ADHC_COMPIL.014): comp-shell scan engine + comp-tools.yaml entry |
| f8c6c6676 | 0.7.0_AE_CloudOps | feat(ADHC_COMPIL.014): comp-shell wrapper + ds-commit-gate.sh extension |
| 7302dda71 | 0.7.0_AE_CloudOps | test(ADHC_COMPIL.014): 5 fixtures (bare/guarded/comment/string/heredoc) |
| bda581fcf | 0.7.0_AE_CloudOps | log(ADHC_COMPIL.014): AC1-AC13 rows + TO status=complete |

---

## ADHC_COMPIL TOs — Status Summary (as of this session)

| TO | Status | Notes |
|----|--------|-------|
| .008 | COMPLETE | AC3 two-phase filename resolver |
| .009 | COMPLETE | Windows POSIX path translator |
| .010 | COMPLETE | F.3 direction aliases + F.4 blast direction wiring |
| .012 | (DS scope) | comp-freshness — not AE |
| .013 | (pending) | comp-iam gaps — not yet started |
| .014 | **COMPLETE** | comp-shell — this session |
| .015 | **COMPLETE** | validate resolver + noconfig — this session |
