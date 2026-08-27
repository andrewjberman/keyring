# DEPLOY LEDGER — ADVI_49F.RPS-CUSTODY: WS-E custody-basis repoint to the 08242234 successor

**Opened:** 2026-08-27T17:12Z by `0.4.0_DS_ClientPlatform` (deploy-start; NEVER#6)
**Status:** **CLOSED 2026-08-27T17:33Z** -- all 7 legs landed, nothing stranded. Deployed and
verified on the DEPLOYED BYTES (not rc), emitted row carries the stated basis, proof instance VALID
rc=0. Closed in the same session it was opened.
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_49F.RPS-CUSTODY.stale-basis-materiality-then-repoint.md` (RPS-3)
**Authority:** `2.0.0_SA_COO` GO 76140 (2026-08-27T16:13Z) + target ruling **76210** (17:00:26Z —
target CONFIRMED `08242234`, `08335338` DISOWNED as an issuer name-is-not-identity defect) + 76212
(RPS-3/4/5 proceed; nothing further gates at the COO seat).
**Lane:** DS owns commit -> QA-deploy for `data/*/scripts/gold/*.py` (CLAUDE.md rule 13).

## What is changing and why

`data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` — the schwab-basis custody source moves:

| | from | to |
|---|---|---|
| bucket | `opal-data-bd` | `opal-data-assets` |
| prefix | `schwab/silver/rps` | `schwab/08242234/silver/fact_rps` |
| partition | `date=YYYYMMDD` | `date=YYYY-MM-DD` |
| value column | `market_value` | `market_value_settled_unsettled` |
| ticker column | `ticker` | `ticker_symbol` |

**Why:** the legacy prefix froze at `date=20260723` and was still the LIVE basis 25 trading days
later (SSM `/mdpf/custody_source` = `schwab`, read 2026-08-27), understating the served client-facing
`non_model_aua` by **$91,476,329.17 (+63.07%)** at as_of 2026-08-26 and drifting a further
**-$1.94M/day**. Full print: `deliverables/ADVI_49F.RPS-CUSTODY_RIDER1_MATERIALITY_PRINT.md`
@`a53fcf6459` (on origin) + @`5c3ed23e92`.

**Account identity is the load-bearing fact.** `08242234` "49 WEALTH MANAGEMENT LLC" (MDPF/SmartX)
reproduces the legacy figure **to the cent at 10 of 10 vintages** sampled across
2024-07-08..2026-07-23. `08335338` "49 FINANCIAL" (ADVI/Black Diamond) matched **0 of 10** and
diverges by +$55,083,179.72 at the 07-23 vintage. **Never repoint to 08335338 under this TO.**

## Pre-deploy evidence (all measured before this ledger opened)

| Check | Result |
|---|---|
| Successor EXISTS | 566 partitions, newest `date=2026-08-26` |
| Successor **CADENCE** (RPS-1b residual COO asked for) | **40 of 40 trading days present** 2026-07-01..2026-08-26; written ~10:16Z on T+1. Produced daily — not merely present. |
| Column mapping value-preserving | 10/10 vintages exact to the cent (the FINDING C equivalence obligation, discharged at 10 vintages, not one) |
| `py_compile` | OK |
| `ruff --target-version py39` | All checks passed |
| Ad-hoc QA run (`--custody-source schwab --dry-run`) | **TRUE rc=0, measured without a pipe.** Resolved `date=2026-08-26`, read the successor, `partner_custody_total` = **$1,732,745,674.50** — identical to the cent to my independent boto3/pandas measurement (different instrument, same number). Coherence gate PASS. |

## Legs

| Leg | Act | Status |
|---|---|---|
| 1 | RPS-1 / 1b / 1c materiality prints | DONE (pre-deploy) |
| 2 | Code change + gates (py_compile, ruff) | DONE (pre-deploy) |
| 3 | Ad-hoc QA dry-run through the production entry point | DONE (pre-deploy) — TRUE rc=0 |
| 4 | `safe-commit` the code change | **DONE** @`d5fd2e4c79` — commit-gate clean (py_compile + ds-precommit + ruff py39), risk-reflex CLEAN vs 1,891 danger nodes, msg-verify MATCH |
| 5 | `safe-deploy.sh` — S3 cp + SHA verify | **DONE** — gate PASS, TRUE rc=0 unpiped. First attempt fail-closed rc=3 on IDENTITY UNRESOLVED; resolved by writing the sanctioned session serial file, **not** by overriding |
| 6 | APPLIED-layer verification on the SERVED/stored artifact (Rule 22a), never rc=0 | **DONE** — deployed object read back, LF-normalised sha256 `b6c8a6ac…c0c51c6af` == local; 7/7 positive probes PRESENT, 3/3 negative controls ABSENT, control-of-the-control fires. Different instrument from the gate's `comp-pipescript` |
| 7 | RPS-4 basis stated in the emitted row; RPS-5 proof instance VALID by TRUE rc | **DONE** — emitted `custody_scope=schwab_native_rps_assets_only_08242234_fact_rps`, schema unchanged (11/11 cols); proof instance VALID TRUE rc=0 (pass 1 was rc=1 INVALID on 3 wrapper-structural violations — recorded in the instance) |

## RPS-4 — how the basis becomes visible downstream

The served row's `custody_scope` changes
`schwab_native_rps_assets_only` -> `schwab_native_rps_assets_only_08242234_fact_rps`, and the custody
dict gains `custody_source_uri`. Both are passthrough descriptors — **denominator: 2 content hits
estate-wide for the old value, being this producer and one doc; no consumer branches on it**, so the
change is schema-safe and the basis change is legible rather than silent.

## What this ledger does NOT close

- **The RPS-2 caveat.** COO ACCEPTED the caveat text and is surfacing the understatement to Andrew.
  The 23 served partitions from 2026-07-24..2026-08-26 carry the July-23 basis and this deploy does
  **not** rewrite them. No backfill is authorized by this TO.
- **The false Rule-25 dormancy marker** on `opal-data-bd/schwab/silver/rps/` — explicitly COO's lane
  (GO 76140, re-affirmed 76210). Untouched here. Note it becomes *more* dangerous after this deploy,
  not less: once WS-E stops reading the legacy prefix, the marker's "no live reader" claim becomes
  true-by-accident, and the blind census that produced it is still uncorrected.
- **Whether any downstream consumer re-derives or caches `non_model_aua`** — unmeasured by me; the
  caveat scope is stated over the WS-E feeder partitions I read.
