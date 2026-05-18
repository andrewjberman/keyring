# Session Log — DS~A — MDPF_ASSETS.010: WS-E 49F non-model AUA residual (Cohort 1b)

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.010 (`dsa-wse-49f-non-model-aua-residual`) — MDPF Phase 2, WS-E, Cohort 1b. GO'd by COO (commit 6248f3e33).

---

## Summary

WS-E — the 49 Financial non-model AUA feeder (Cohort 1b) — built, verified, and
landed in one session. WS-E emits the contract-section-4 `non_model_aua` residual
artifact for `firm_id=49financial`: a LIVE residual, not an independently-sourced
figure.

**`non_model_aua(49financial) = $294,707,948.53`**
` = partner_custody_total $1,655,447,182.20`
` − model_aua_input (Cohort 1a) $1,335,951,335.82`
` − sma_aua_input (Cohort 1c) $24,787,897.85`

Per AMENDMENT 1 the residual subtracts BOTH managed sub-cohorts (subtracting only
`model_aua` would leave the SMA dollars in the residual while they are also
counted in Cohort 1c — a double-count).

Script: `data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` (new — commit
5661839ee, pushed CLOUD). Artifact: `s3://opal-data-mdpf/mdpf/feeds/non_model_aua/49financial/2026-05-18.parquet`
(uploaded 2026-05-18T19:33Z).

## Build

**Phase 1 — the Schwab-custody crosswalk + `partner_custody_total`.** The custodian
attribute is not on the `certified_aua` source (`silver/allocations`); WS-E builds
a stable `account_id -> billing_account_custodian` crosswalk by scanning the full
`silver/fees` history (the .001 audit method) — rebuilt each run. 1,855 partitions
scanned (24-worker thread pool, per-partition retry-once tolerance), 10,442 distinct
accounts, **0 custodian conflicts** (custodian is stable per account, confirming the
.001 finding). `partner_custody_total` = `certified_aua` (E_19 method: Σ
`account_market_value` minus the 3 liability `account_type`s) restricted to
Schwab-custodied accounts.

**Phase 2 — the residual artifact.** Emits the section-4 `non_model_aua` artifact,
one row per `(firm_id, as_of_date)`, AMENDMENT-1 schema (10 cols incl. the new
`sma_aua_input`). `model_aua_input` + `sma_aua_input` read from the WS-B
`model_aua_positions/49financial/2026-05-18.parquet`, split on `cohort_class`.

**Phase 3 — verified.** Ran 2026-05-18:

| Check | Result |
|-------|--------|
| `certified_aua` recompute vs published `gold/aua_certification/2026-05-14.json` | **PASS — matches to the cent** ($1,812,432,585.32) |
| Custody decomposition vs the .001 audit | **Exact** — Schwab $1,655,447,182.20 / ByAll $135,602,222.34 / Fidelity IWS $12,955,930.66 / unmatched $7,273,392.78 / DST $1,153,857.35 |
| `model_aua_input` + `sma_aua_input` vs the WS-B feed | **Exact** — $1,335,951,335.82 + $24,787,897.85 (matches WS-B Cohort 1a/1c to the cent) |
| section-7 dual identity (WS-E self-check) | **PASS** — `model_aua_input` == Σ `model_value`(cohort=model); `sma_aua_input` == Σ (cohort=sma) |
| `non_model_aua` >= 0 | PASS — $294,707,948.53 |
| 15-acct / $7.27M unmatched-custodian bucket | excluded from `partner_custody_total` + surfaced (not silently dropped) |

**End-to-end (WS-A aggregator dry-run, live S3 feeds).** `mdpf_aggregate_aua.py`
reads WS-E's artifact correctly. 49financial: `model_aua + non_model_aua` =
$1,655,447,182.21 = `partner_custody_total` $1,655,447,182.20 — the clean
three-way partition `custody − model − sma − non_model ≈ 0` holds to the cent
(1¢ float-rounding artifact).

## Reference reconciliation — the −8.48% explained

`non_model_aua` = $294.71M vs the contract Appendix-A reference ~$322M is −8.48%.
The gap is a single, fully-attributed line item, not residual noise:

- The reference's minuend is the 49F coworker spreadsheet's Schwab-custody view
  **$1,682.52M** (2026-05-15). WS-E's minuend is the **empirical** BD figure
  **$1,655.45M** (2026-05-14) — the E_19 `certified_aua` Schwab-restricted, which
  cross-checks to the published certification to the cent and reproduces the .001
  audit's custody decomposition exactly.
- The .001 brief + Appendix A already documented this: "$1,682.52M ... matches the
  .001 audit's $1,655.4M Schwab-custodied to ~1.6%." The ~$27M minuend difference
  propagates directly: $322M − $27M ≈ $295M.
- WS-E is **correct** to use the live-pipeline empirical figure — a residual feeder
  must compute off real pipeline data, not a static spreadsheet. The 4-day
  custody-date offset (BD 5/14 vs SmartX 5/18) is a roll-forward; if anything a
  5/18 BD figure would be higher, narrowing the gap.

## Acceptance criteria

| AC | Status |
|----|--------|
| AC1 — crosswalk built into the gold script (rebuilt from full `silver/fees` history each run); `partner_custody_total` = certified_aua Schwab-restricted computed | MET — $1,655,447,182.20; 1,855 partitions, 0 conflicts |
| AC2 — `non_model_aua` artifact ships for 49financial per section 4 — residual + `partner_custody_total` + `model_aua_input` + `sma_aua_input` + method + `custody_scope=schwab_only`; 15-acct/$7.3M bucket excluded + surfaced | MET — artifact in `s3://opal-data-mdpf/mdpf/feeds/non_model_aua/49financial/2026-05-18.parquet` |
| AC3 — `non_model_aua` verified near the Appendix-A reference; the section-7 `model_aua_input` check | MET — $294.71M; the −8.48% vs ~$322M is the documented $27M empirical-vs-spreadsheet Schwab gap. The AMENDMENT-1 section-7 DUAL identity is verified by WS-E's self-check. The aggregator-side GATE shows the expected pre-.013 single-check ERROR (see below) — resolved by MDPF_ASSETS.013, sequenced next on this lane. |
| AC4 — no emoji; ds-commit-gate exit 0; Rule 15; Rule 17; session log + Compiler Tools; RAVC2 | MET — gate exit 0; `from __future__ import annotations` first; WS-E only READS BD silver (no silver-side modification, Rule 17); RAVC2 to COO. |

## The section-7 aggregator gate — pre-.013 ERROR (expected, the .013 trigger)

The WS-A aggregator dry-run against the live S3 feeds returns
`reconciliation.overall = ERROR`. Neither cause is a WS-E defect:

1. **`identity_1.model_aua_input_check = ERROR`** — `49financial: model_aua_input=1335951335.82 vs positions sum=1360739233.68`. The CURRENT (pre-AMENDMENT-1) aggregator runs a SINGLE check: `model_aua_input == Σ ALL model_value`. WS-E correctly sets `model_aua_input` to the Cohort-1a (cohort_class=model) value only; the $24.79M delta is exactly the Cohort-1c SMA AUA. **This is precisely the MDPF_ASSETS.013 trigger** — .013 updates the aggregator to the AMENDMENT-1 DUAL check (`model_aua_input == Σ cohort=model` AND `sma_aua_input == Σ cohort=sma`), after which it passes. COO sequenced WS-E before .013 for exactly this reason.
2. **`identity_2_etf_residual = ERROR`** (`min_public_residual −427,370.31`) — ETF over-attribution in the `model_composition × model_aua_positions` decomposition. Entirely outside WS-E scope (WS-E emits `non_model_aua` only; it touches no ETF artifact). Pre-existing — flagged to COO, not a WS-E item.

`identity_1_aggregate_sum` itself = PASS (residual 0.0); `identity_3` = PASS.

## Compiler Tools

| Tool | Result |
|------|--------|
| `.tools/ds-commit-gate.sh` | PASS — py_compile + AST + ruff py39 clean (exit 0). One comp-constants drift caught: a module const `FIRM_ID='49financial'` collided with a canonical `FIRM_ID='inflection'` — renamed to `PARTNER_FIRM_ID` (the same fix WS-B applied). |
| `comp-pipescript io build_mdpf_wse_49f_non_model_aua` (TO mandate phase 1) | "Unknown script" — the comp graph does not index brand-new `data/mdpf/` scripts (same as WS-B/WS-C at first build). The I/O column surface was instead established by reading the canonical producer `E_19.write_aua_certification.py` directly: `silver/allocations` (`account_id`, `account_market_value`, `account_type`), `silver/fees` (`account_id`, `billing_account_custodian`), `gold/aua_certification/{date}.json`. WS-E's reads use explicit `columns=[...]` projection matching that surface exactly — a column gap raises `KeyError` loudly at read, not silently. |
| `comp-blast build_mdpf_wse_49f_non_model_aua` (TO mandate phase 3) | "No nodes matching" — expected for a brand-new feeder; this IS the mandate pass condition. Zero blast overlap with the SmartX EC2-exporter canonical path or the INF gold chain. WS-E is standalone: it READS BD silver + the WS-B feeder, WRITES only `opal-data-mdpf`. |
| `comp-validate` | N/A — no `gold_validate_config` entry applies to MDPF scripts (that config is BD-pipeline-specific). Verification is the in-script reconciliation block + the end-to-end `mdpf_aggregate_aua.py` dry-run. |

Note: a `<unknown>:91 SyntaxWarning: invalid escape sequence '\$'` surfaces in
`comp-pipescript`/`comp-blast` output — confirmed NOT in this script
(`python -W error::SyntaxWarning py_compile` clean; line 91 is `LIABILITY_TYPES`).
It is comp-tooling noise from another graph node.

## Files Modified

| File | Change |
|------|--------|
| `data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` | New — the WS-E feeder |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDPF_ASSETS.010.dsa-wse-49f-non-model-aua-residual.md` | status pending -> complete |

## Deploy Evidence

| Item | Result |
|------|--------|
| Script commit | 5661839ee, pushed CLOUD (safe-deploy: no runner-deploy scope — WS-E is a standalone MDPF script) |
| Feeder run | 2026-05-18 — `non_model_aua(49financial)` $294,707,948.53 |
| S3 landing | DONE — `s3://opal-data-mdpf/mdpf/feeds/non_model_aua/49financial/2026-05-18.parquet` (1 row), uploaded 2026-05-18T19:33Z |
| End-to-end | `mdpf_aggregate_aua.py` reads the artifact; 49F partition `custody − model − sma − non_model ≈ 0` to the cent |

## Cross-workstream note for COO / .013

WS-C's (`.008`, closed) `non_model_aua` artifact is pre-AMENDMENT-1 — its
`build_mdpf_wsc_inflection_feeder.py` `COLS_NON_MODEL_AUA` has 9 columns and
LACKS `sma_aua_input`; its `model_aua_positions` also lacks `cohort_class`. WS-E's
`non_model_aua` is the AMENDMENT-1 10-column schema. This is the same WS-C-is-pre-
amendment concern COO already flagged for .013 (the `cohort_class` check). For .013:
the aggregator must tolerate WS-C's missing `sma_aua_input` (inflection has no SMA,
so 0 is the correct value) — but per COO's directive, surface, don't default
silently. A small WS-C re-tag mirroring the WS-B re-tag is the clean follow-on.
Carried into .013 (self-sequenced next on this lane).

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — WS-E (.010) built + verified. `non_model_aua(49financial)` $294,707,948.53 lands in `opal-data-mdpf`; reconciles to the .001 audit + the WS-B feed to the cent; the −8.48% vs ~$322M is the documented $27M empirical-vs-spreadsheet Schwab gap. AC1-AC4 met. |
| **DS~A (self)** | MDPF_ASSETS.013 — the WS-A aggregation-script AMENDMENT-1 update — next, self-sequenced. It resolves the pre-.013 `model_aua_input_check` ERROR (single -> dual check) and must handle WS-C's missing `sma_aua_input` (surface, don't default). |
| **COO 2.0.0** | FYI not blocking — `identity_2_etf_residual` ERROR (`min_public_residual −427,370.31`): ETF over-attribution in the `model_composition × model_aua_positions` decomposition. Outside WS-E + .013 scope; flag for a WS-D.2 / model-composition follow-up. |
