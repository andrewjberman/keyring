# DS~D Session 3 — ADVI_INFINC.006 Pattern E TXN (account-level windowed pull)

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-05-15
**TO:** `ADVI_INFINC.006.dsd-pattern-e-txn-firm-windowed-pull` (COO-issued; resumed after the TXNAMG TO-3/TO-4 gate cleared)
**Status:** COMPLETE — Option A shipped + deployed + validated. RAVC2 to COO + CC CTO + AE 0.6.1.

## Current State

`pull_inflection_transactions_rest.py` migrated to a Pattern E incremental windowed pull on
the **account-level** Orion endpoint (CTO-ruled Option A). Daily 7-day trailing window +
weekly full-history backstop, both account-level, deduped by transaction id. Committed
`5c1ea192d`, pushed CLOUD, deployed to `s3://opal-data-inf/code/manual_api/`.

## What I Did

### Phase 0 — endpoint confirm + PERF probe (prior DS~D session + this session)
The prior DS~D session ran `inf_006_phase0_probe.py`. This session validated and acted on it.
- Firm `/Portfolio/Transactions`: 50-col schema, **missing 11 bronze-contract columns** — rejected.
- PERF `/Clients/{id}/Performance`: 7d/14d short windows return data in 1.5-2.0s, no timeout — **viable** (AC10). The "5y+ timeout" docstring does not apply to short windows.

### Phase 3 — validation surfaced the blocking finding
A full client-level pull = 1,186,804 rows vs the account bronze's 1,299,493 — a **144,453-row gap that is exactly all non-Complete transactions** (Rejected/Pending/Reversed). The client endpoint returns Complete-status only; 5 status-inclusion params probed, none expose non-Complete. Shipping client-level would silently drop ~11% of bronze incl. all Pending (in-flight flows) + Reversed (netting).

### STOP + escalation
Halted rather than ship a 144K-row bronze regression. Escalated to COO + CTO with a 3-option decision packet. Caught a message-crossing: COO/CTO's first "proceed on client-level" ratifications addressed the older firm-vs-client question and crossed the 20:01Z blocker in flight — re-surfaced rather than propagate a stale ratification.

### Resolution — CTO + COO ruled Option A
Account-level windowed pull. A Complete-only client bronze is a business-semantic row filter at ingestion (Rule-17-family violation); with the firm call-count win dead, Option B buys nothing.

### Implementation
`pull_inflection_transactions_rest.py` — account-level `/Accounts/{id}/Transactions`, windowed:
- INCREMENTAL (Mon-Sat): per account, trailing 7-day window; merge into the prior bronze snapshot; dedupe by `id` keeping the window row (backdated-correction-safe).
- FULL-PULL (Sunday / `--full-pull` / `INFINC_FULL_PULL`): per account, full history — the weekly backstop. Ships same-commit as the daily narrowing.
- Re-verified: the account endpoint **does accept `?startDate=&endDate=`** (the "no date params" docstring was wrong — third docstring-vs-empirical correction in the INFINC arc).

## Validation (live Orion + prod S3)

| Check | Result |
|---|---|
| AC3 no rows lost | account-windowed full-pull 1,299,831 = superset of current bronze 1,299,493 — **0 lost**, 338 newer |
| AC3 incremental reconciliation | incremental windowed merge = 1,299,831 — **reconciles row-for-row to the full-pull** |
| AC4 schema byte-identical | 31 cols, exact match |
| status fidelity | all 6 statuses present (Complete/Rejected/Pending/Reversed/+2) — vs client-level Complete-only |
| AC8 in-window capture | 338 newly-appeared transactions all within the 7-day window (all Pending — the class client-level drops) |
| AC9 weekly backstop | full-pull re-pulls unfiltered complete history — captures any-date correction |
| AC5 wall time | incremental ~11min, full-pull ~15min (local). **~1x, not ~2x** — see below |

## AC5 — speed objective empirically UNMET (flagged to COO + CTO 20:44Z)

The daily incremental is ~862 **sequential** account calls — the same call count as the
pre-Pattern-E pull. Windowing cuts each call's payload but not the call count or the
~0.8s/call latency floor. The firm-endpoint "1 call replaces 1,160" was the only real speed
lever, and it died (schema-incompatible). **INFINC.006 should be reframed as an architecture
migration** — the windowed-pull + weekly-backstop design, idempotent re-pulls, backdated-
correction correctness, and the append-only-ingestion foundation (TXNAMG §7-Q5) — not a
"~7min/day" speed win. Flagged to COO + CTO before commit; COO's full-GO + the architectural
rationale stand. A real speed win would need parallelizing the account calls (separate scope).

## Deploy

- Commit `5c1ea192d` (author `0.4.0_DS_ClientPlatform~D`), pushed CLOUD.
- `aws s3 cp` → `s3://opal-data-inf/code/manual_api/pull_inflection_transactions_rest.py` (21,835 bytes). safe-deploy does not map `manual_api/` — manual S3 cp per the TO Phase 4 + DS deploy ownership.
- Next daily chain `INF_API_PULL_TXN` picks up the new pull; mode auto-resolves (incremental Mon-Sat, full-pull Sunday). A prior baseline (`bronze/transactions/2026-05-15.parquet`) exists, so the first incremental run merges cleanly.

## Compiler Tools

| Phase | Tool | Result |
|---|---|---|
| Phase 2 | `ds-commit-gate.sh` on `pull_inflection_transactions_rest.py` | PASS — py_compile + AST undefined-name + ruff py39; `from __future__` first import |
| Phase 0/3 | empirical Orion REST probes + S3 parquet diffs | The authoritative basis — `manual_api/` pull scripts are not modelled in the comp graph (ADVI_TXNAMG PRD §5.2 / INFINC.005) |
| Phase 4 | `safe-deploy.sh` (via pre-push hook) | "no deploy-scope script files" — safe-deploy maps `scripts/{gold,silver,bronze}/` only; `manual_api/` S3 cp done manually |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — AC1-13: implemented + deployed + validated. AC1/AC2/AC5 deviations (account-level not firm/client; ~1x not ~2x speed) flagged for RAVC validation + the INFINC.006 reframe (architecture migration, not speed win). |
| **CTO 1.0.0** | CC — Option A shipped per ruling; AC5 ~1x empirical noted. |
| **AE 0.6.1** | CC per the TO `<ravc>`. |
| **COO 2.0.0** | PERF short-window probe positive (7d/14d viable) — COO authors a PERF Pattern-E TO off this RAVC2. |
| **DS~D (self)** | TXNAMG TO-7 (UNION extension) — CTO-ruled, COO to author with DS~D as receiver. Pending COO issuing it. |
