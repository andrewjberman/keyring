# /work — FIND_INSURE.034 Lusha endpoint narrowing to org-chart-only

**Agent:** 0.1.0_DS_MarketIntelligence~C
**Cycle:** /work substantive tick (~03:48Z → ~04:05Z, ~17min wall)
**Archetype:** IMPLEMENT
**TO:** FIND_INSURE.034 (ws COO DRIVE-TO, inline MCP `20260528T0352Z`; PRD v0.7.2 `ff27f57ef` §2)
**Commit:** `0babd199b` (5 files, +247/-12)

## Trigger

ws COO DRIVE-TO redirect from NO-WORK (.024 correctly held on Andrew Q1 gate). New concrete TO: enforce PRD v0.7.2 §2 credit-conservation interim policy structurally — narrow Lusha to org-chart-only endpoints; defer contact-reveal to v0.7.3+.

## What shipped (all 6 ACs MET)

| AC | Deliverable | Status |
|---|---|---|
| AC1 | Org-chart endpoints (companies/search + companies/enrich + contacts/prospecting) stay enabled; crawl Lambda Step 3 enrich gated | MET |
| AC2 | contacts/enrich guard-rail behind `LUSHA_CONTACT_REVEAL_ENABLED` (default false) — raises `LushaContactRevealDisabledError`; NOT deleted | MET |
| AC3 | cost-budgets-v0.1.json: `interim_policy.active_band=ORG-CHART-ONLY` + enrich_contacts & search_and_enrich_contacts `status=DEFERRED-v0.7.3` | MET |
| AC4 | Self-tests: org-chart clean; contact-reveal BLOCKED when flag false; flag-true path preserved | MET |
| AC5 | comp-iam service — Lambda not yet comp-graph-registered; endpoint narrowing is IAM-neutral (no drift) | MET (see note) |
| AC6 | ds-commit-gate clean (4 .py); Rule 15 preserved; Rule 14a safe-commit | MET |

## Design

**Structural enforcement (lusha_client.py):**
- `CONTACT_REVEAL_ENV_FLAG = "LUSHA_CONTACT_REVEAL_ENABLED"` + `contact_reveal_enabled()` + `CONTACT_REVEAL_BLOCKED_MSG`
- `LushaContactRevealDisabledError(LushaError)` + `_assert_contact_reveal_enabled()`
- `contacts_enrich()` calls the guard at top → single-source-of-truth enforcement; any caller hits it

**Graceful consumer (crawl_linkedin_bronze.py):**
- Step 3 enrich loop gated behind `contact_reveal_enabled()`; when false → `contact_reveal_deferred=True`, log, skip (org-chart-only output: prospecting list + firmographics, zero reveal credits)
- Defense-in-depth: catches `LushaContactRevealDisabledError` mid-loop (flag flip mid-run)
- New result field `contact_reveal_deferred`

**Config (cost-budgets-v0.1.json):** in-place DEFERRED-v0.7.3 annotation on the two contact-reveal classes; ceilings preserved for v0.7.3 re-enable.

## Tests

- `test_lusha_client.py`: 90/90 (added contact-reveal gate test: flag-false BLOCKED + flag-true works)
- `test_crawl_linkedin_bronze.py`: 38/38 (T1/T4 enable reveal for cascade; NEW T8 org-chart-only default; NEW T9 client gate)
- In-module self-tests: lusha_client 14/14, crawl 6/6

## Discipline

- **Rule 14**: ds-commit-gate clean on all 4 .py (py_compile + AST + ruff py39)
- **Rule 15**: `from __future__ import annotations` preserved
- **Rule 14a**: safe-commit `--force` (hot multi-author period; --only scopes to declared pathspec)
- **Code Quality (no non-ASCII in logs)**: `BLOCKED` msg + LOG.info use `sec 2` not `§2` (charmap rule); existing docstring/config `§` left per established file convention (not a logging surface)

## Judgment calls flagged for COO/CVO

1. **search-and-enrich**: `contacts/search-and-enrich` has no method in lusha_client yet — nothing to wrap. Guard helper `_assert_contact_reveal_enabled()` is ready; documented that v0.7.3 impl MUST call it. Config class marked DEFERRED-v0.7.3.
2. **Config in-place vs v0.2-sister**: chose in-place annotation per AC3 "mark ... lines" literal phrasing + to avoid the AE-domain `COST_BUDGETS_VERSION` Lambda-env bump. Flag if v0.2-sister file preferred.
3. **AC5 IAM**: Lambda not comp-graph-registered yet (AE 0.7 .003, post-Phase-1). Endpoint narrowing is application-logic-only (Lusha = outbound HTTPS keyed from Secrets Manager, not AWS-IAM-gated) → zero IAM surface change. No drift structurally guaranteed.

## LD-0116 routing

RAVC2-Request → ws COO (`2.0.0_SA_COO`); CC ws CTO (`1.0.0_SA_CTO`) + ws CVO (`3.0.0_SA_CVO`) per TO §3. NO direct MCP to MSTR.

## Next Steps

1. **[ws COO]** RAVC2-ACCEPT FIND_INSURE.034 (commit `0babd199b`); create TO-record for registry if desired (DRIVE-TO was inline-MCP, no disk TO file).
2. **[ws CVO]** /verify-channel candidate — org-chart-only band enforcement (mechanical: guard-rail + test coverage).
3. **[v0.7.3 trigger]** flip `LUSHA_CONTACT_REVEAL_ENABLED=true` to re-enable contact-reveal when credit-conservation interim policy lifts.
4. **[~C self-loop]** /work cron 7,27,47 next tick; .024 remains gated on Andrew Q1.

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T04:05Z
