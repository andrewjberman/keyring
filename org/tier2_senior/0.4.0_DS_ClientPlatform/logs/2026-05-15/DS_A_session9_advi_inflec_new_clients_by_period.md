# Session Log — DS~A — ADVI_INFLEC new_clients_by_period in INF_D_00d

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-15
**TO:** Andrew-direct (no formal TO) — via brief `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/deliverables/brief_ds_inflection_new_clients_by_period.md`
**Commit:** `4e4a3c321`

> Second topic of the 2026-05-15 session. The first — ADVI_ECLDAT freshness verify,
> bronze/silver/gold build, daily automation + portal-publish decouple — is logged in
> `DS_A_session8_advi_ecldat_freshness_and_gold.md` (including the automation addendum).

---

## Objective

Inflection ADVI -> Distribution -> Segment Analytics -> Continuous showed `0 New Clients`
(both AUA and NNA modes). Root cause: `INF_D_00d.cumulative_chart.py` never emitted
`new_clients_by_period`, so the FE "New Clients" tiles fell back to 0. 49Financial's
`cumulative_chart.json` carries the key off the same FE code path; Inflection's lacked it.

Fix: add the `new_clients_by_period` block to the Inflection cumulative-chart gold script.
Additive only, no FE change.

## Routing / authorization note

The task arrived via MCP from `0.4.2_RD_AdvisorIntelligence` (tier-3) framed as "Andrew
direct." Since I was in a live session with Andrew, I ACK'd the RD (RAVC, not silent) and
verified the directive with Andrew directly before executing rather than acting on the
relayed attestation. Andrew confirmed: "Yes I ack it, that's from me." Then executed.

---

## Implementation

Applied the RD brief's drop-in to `data/orion/scripts/gold/INF_D_00d.cumulative_chart.py`:

- `_MONTH_SHORT` constant + `build_new_clients_by_period(accounts_v2)` builder above `main()`.
- Builder: new households per period, keyed on the **earliest `account_start_date` per
  `household_id`** (Inflection "client" grain = household). `pd.to_datetime(errors='coerce')`
  + `dropna`. Emits `{quarterly, monthly, annually}`, each `[{period,label,count}]` sorted
  ascending. Returns `None` on missing inputs so `main()` omits the key (FE treats absent as 0).
- Wired `new_clients = build_new_clients_by_period(accounts_v2)` after `nna_adv_view` —
  `accounts_v2` is already loaded in `main()`, no new S3 read.
- Conditional `chart['new_clients_by_period'] = new_clients` after the `chart` dict.

`period`/`label` formats verbatim to the FE contract (`types.ts NewClientsByPeriodPoint`):
quarterly `2026-Q2`/`Q2 '26`, monthly `2026-05`/`May '26`, annually `2026`/`2026`.

No change to the `geo`/`adv`/`nna_geo`/`nna_adv`/`geo_drill` views. Gold tier — the
`dropna` business filter is tier-appropriate (not silver).

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/INF_D_00d.cumulative_chart.py` | Added `build_new_clients_by_period()` + `_MONTH_SHORT`; wired into `main()` + `chart` dict (+59 lines, additive) |

---

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `ds-commit-gate.sh` | PASS | py_compile + AST undefined-name scan + ruff py39 |
| `comp-pipescript io INF_D_00d` | No COLUMN GAP | `account_start_date` already in the loaded `accounts_v2` frame — no new column load, no gap |
| `safe-deploy` (pre-push hook) | PASS | `code/gold/INF_D_00d.cumulative_chart.py` DEPLOYED [inf] + verified |

---

## Verification — builder run on live `accounts_v2` 2026-05-15 (862 accounts)

Matches the RD brief section-5 ground truth exactly:

| Check | Expected (brief) | Actual | |
|-------|-----------------|--------|---|
| Total households all-time | 296 | quarterly=monthly=annually all sum to 296 | PASS |
| 2020-Q2 (original-book Orion migration) | 111 | 111 | PASS |
| Quarterly tail | 2025-Q4=10 / 2026-Q1=9 / 2026-Q2=10 | 10 / 9 / 10 | PASS |
| 2026 annual | 19 | 19 | PASS |
| Series sizes | — | 25 quarterly / 64 monthly / 7 annual | — |
| period/label formats | contract table | `2026-Q2`/`Q2 '26`, `2026-05`/`May '26`, `2026`/`2026` | PASS |

---

## Deploy Evidence

| Step | Result |
|------|--------|
| ds-commit-gate.sh | PASS |
| Commit SHA | `4e4a3c321` |
| Author | `0.4.0_DS_ClientPlatform~A` |
| Push | `origin/CLOUD` — `89d28b4c9..4e4a3c321` |
| safe-deploy | PASS — INF_D_00d.cumulative_chart.py deployed [inf], verified |
| Materialization | Deferred to 2026-05-16 06:00Z chain (`INF_D_00d` in CHAIN_FULL + CHAIN_INCREMENTAL) — per Andrew "next D run grabs it" |

---

## Acceptance Criteria Status

| AC | Criterion | Status |
|----|-----------|--------|
| AC1 | `new_clients_by_period` emitted with `quarterly`/`monthly`/`annually` | PASS |
| AC2 | Each entry `{period,label,count}`, sorted ascending, formats per FE contract | PASS |
| AC3 | Household grain, earliest `account_start_date` per `household_id` | PASS |
| AC4 | Counts match RD section-5 ground truth (296 total) | PASS |
| AC5 | Additive only — no change to existing views | PASS |
| AC6 | ds-commit-gate PASS + safe-deploy PASS | PASS |
| AC7 | RAVC to RD 0.4.2 with commit SHA + verification | PASS — RD validated `4e4a3c321`, loop CLOSED |

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **(automated)** | 2026-05-16 06:00Z chain materializes `platinum/firm/cumulative_chart.json` with the key; DistributionTab "New Clients" tiles render live on next page load |
| **0.4.2_RD_AdvisorIntelligence** | RAVC loop CLOSED (RD validated commit + FE-contract match) — section-5 S3 verify returns `present:true` post-06:00 |
| **Andrew** | Optional SSM-direct `--single INF_D_00d` run available if the fix is wanted live before 06:00; otherwise 06:00 closes it |

---

## Adjacent (non-deliverable)

Answered an INFGRO S3-fact question from `0.4.0_DE_ClientPlatform` mid-session (whether the
GRO C-tier outputs INF_C_02/INF_C_03 are materialized on S3 — yes, `client_performance.parquet`
carries the GRO columns; flagged a `performance_dim` freshness caveat). No code; DS~C/base owns
INFGRO. DE closed that loop.
