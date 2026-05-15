# DS~B Session 2 — SXPL_RESTIN.001 SmartX per-model availability assessment

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-15
**TO:** SXPL_RESTIN.001.dsb-per-model-availability-assessment (from 2.0.0_SA_COO)
**Project:** SXPL_RESTIN (SmartX REST Integration) — Andrew-directed initial TO

## Objective

Close the empirical gaps the SmartX HAR left: resolve all 7 modelIds, probe every
design-brief §6.2-6.4 endpoint per model, capture real response schemas, produce the
per-model x per-endpoint availability matrix, answer the §10 probe-settleable open
questions. Read-only. Deliverable = a brief.

## What was done

Built a read-only probe harness (`data/smartx/scripts/sxpl_restin_probe.py`) — mints a
ROPC token (Secrets Manager creds, never hardcoded), probes 7 modelIds x 13 endpoints,
captures HTTP status / bytes / depth-limited schema shape / classification. Throttled
3.6 s/call (~17 req/min). Ran 2026-05-15 18:11-18:21Z, ~95 calls, zero 429s.

First run timed out on a large `allocations/performance` payload and aborted; hardened
`http_get` (exception-safe, returns status -1 instead of crashing; 90 s timeout) +
incremental per-model JSON write, re-ran clean.

## Findings (all ACs met)

- **AC1** — 7 models resolved, all active Opal Capital LLC. 5 map to the exporter
  portfolios (ST/INT/LTC/LTA/UST, the `49Fi…` shortName family). The 2 previously-
  unidentified: **Opal Dividend Income** + **Pathfinder Focused Opportunities** — real
  active Opal models outside the legacy exporter's 5-portfolio scope.
- **AC2/AC3** — real schemas captured for all 13 endpoints; per-model x per-endpoint
  matrix delivered. All `api/3.1` + `performance` endpoints 7/7 populated. The legacy
  `api/3.0` host returns a 105 B status envelope (not usable) — v3.1 supersedes it.
- **AC4** — (1) NO historical-holdings endpoint: `holdings?date=`/`?asOf=` ignore the
  param, `holdings/historical` + `historicalholdings` 404 — daily weight history must be
  accrued by daily snapshotting. (2) 2 unknown models characterized (above). (3) Rate
  limit: ~17/min probed clean, zero 429s; 20/min (exporter config) is a safe planning
  ceiling, exact value unconfirmed (would need a deliberate burst test — not done).
- First-data-goal mapping confirmed: daily value = `enterprises/aum.performance[].closingEquity`;
  holdings weights = `reportedmodels/{reportedModelId}/holdings.percentOfPortfolio`.
  modelId vs reportedModelId chaining is a hard requirement (holdings 400s on a modelId).

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Per-model availability matrix | docs/briefs/smartx-per-model-availability-matrix-20260515.md | COO (TO-3 scoping), TO-2 AE |

## Files Modified

| File | Change |
|------|--------|
| data/smartx/scripts/sxpl_restin_probe.py | New — read-only SmartX endpoint probe harness (creds from Secrets Manager) |
| docs/briefs/smartx-per-model-availability-matrix-20260515.md | New — the deliverable matrix brief |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `.tools/ds-commit-gate.sh` (sxpl_restin_probe.py) | PASS — "All checks passed!" | py_compile + ds-precommit-check.py + ruff --target-version py39. Run twice (after the http_get hardening edit). |

No comp-pipescript — read-only investigation TO, no pipeline gold/silver/bronze script in scope (per the TO compiler_tools_mandate).

## RAVC2

- **COO 2.0.0** — SXPL_RESTIN.001 complete, AC1-5 all PASS. Deliverable brief:
  docs/briefs/smartx-per-model-availability-matrix-20260515.md. The matrix + schemas +
  open-question answers are the input to scope TO-3+.
- **CTO 1.0.0** — CC on RAVC2.

## Next Steps

- `[COO 2.0.0]` Scope TO-3+ (silver/gold modeling) against the matrix brief. Candidate
  TO-3 datasets beyond the first goal: enterprises/allocations, changerequesthistory,
  performance/models/performance.
- `[COO 2.0.0]` Decide whether the 2 non-exporter models (Dividend Income, Pathfinder)
  are in portal scope — a product call; flag to Andrew.
- `[AE — TO-2]` Matrix confirms the TO-2 daily pull is ~13 calls/day; drop the legacy
  api/3.0 host and allocations/performance from first-wave scope.
