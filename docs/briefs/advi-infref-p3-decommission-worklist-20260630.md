# ADVI_INFREF P3 -- Post-Cutover Decommission Worklist (PREP, not execute)

**Author:** 0.4.0_DS_ClientPlatform~A | **Date:** 2026-06-30 | **Status:** DRAFT / ledger-ready
**Requested by:** 2.0.0_SA_COO (INFREF rebuild-window pre-stage #2)
**Execution gate:** Andrew-confirm (destructive: lambda/rule deletion) + a post-cutover soak. This
document is the ordered plan so the day-after is a **checklist, not a scramble**. Nothing here runs
until (a) L5 swap is CVO-cosigned GREEN via `validate_post_swap.py`, and (b) the categorical EC2
CHAIN_PULL has produced all bronze artifacts on **N>=3 consecutive scheduled nights** in PROD.

---

## Doctrine (applies to every leg below)

- **Each leg is a deploy-ledger leg -- NEVER half-land.** Open an
  `org/critical_paths/change_management/{ts}_{leg}_decommission.md` entry at leg-start, close it at
  completion. An unclosed leg at session end = COO alarm (CLAUDE.md NEVER-half-land rule).
- **Reversible-first ordering:** DISABLE the EventBridge rule (stop the cron; lambda + code stay
  intact, re-enablable in one click) -> SOAK one full cycle -> only THEN delete the resources via
  Terraform. Never delete-before-soak.
- **Per-leg PRE-DECOMMISSION consumer-trace gate (Rule 20):** before retiring ANY producer, prove
  no live consumer still reads its output path -- `comp-blast <artifact>` + `comp-platinum reverse`
  + confirm the gold chain reads the NEW silver (typed parquet), not the OLD `bronze/orion-api/{date}/*.csv`.
  A producer whose output still has a live reader is NOT a decommission candidate yet -- that reader
  is an un-migrated LEG-1/LEG-2 dependency and must be repointed first.
- **Destructive -> Andrew-confirm:** lambda/rule deletion is unrecoverable-class (CLAUDE.md Agent
  Autonomy). The disable step is reversible (no confirm needed); the DELETE step needs Andrew go.
- **Terraform-only:** all 9 lambdas + their crons live in `infra/aws/terraform/inf-pipeline/`.
  Removal = delete the `aws_lambda_function` + `aws_cloudwatch_event_rule` + `aws_cloudwatch_event_target`
  + `aws_lambda_permission` blocks, then `.tools/safe-apply.sh`. Never console-delete.

---

## PRECONDITION P0 -- categorical-ingestion parity confirmed in PROD

Before ANY leg: confirm the scheduled EC2 CHAIN_PULL categorically produces the full bronze set the
9 lambdas used to produce. This is the L1 categorical proof, but validated on **>=3 consecutive
scheduled-nightly artifacts** (not a resume-skip / manual run). Gate:
`comp-pipescript deployed` + `comp-freshness` on each bronze dim for 3 nights. RED on any night = halt
decommission, the replacement is not stable.

---

## GROUP A -- the 9 redundant pull-cron lambdas (CHAIN_PULL now produces these)

Source: `pipescript advi-inf` thread `inf-bronze-api-pull`. Each row = one decommission leg. Order by
leaf-first (least-depended-on first) so a surprise reader surfaces on a low-blast-radius leg.

| # | Lambda | EventBridge cron (UTC) | Produced (OLD path) | CHAIN_PULL replacement | Pre-decommission consumer-trace |
|---|--------|------------------------|---------------------|------------------------|--------------------------------|
| A1 | `inf-tax-daily` | 55 12 | `bronze/orion-api/{date}/tax_*.csv` | INF_API_PULL_TAX + INF_API_SILVER_TAX | confirm gold reads silver tax dim |
| A2 | `inf-billing-daily` | 35 13 | `bronze/orion-api/{date}/billing.csv` | INF_API_PULL_BILLING + INF_API_SILVER_BILLING | confirm gold reads silver billing dim |
| A3 | `inf-performance-daily` | 40 13 | `bronze/orion-api/{date}/performance_dim.csv` | INF_API_PULL_PERF_DIM + INF_API_SILVER_PERF_DIM | confirm gold reads silver perf dim |
| A4 | `inf-api-txn` | 0 13 | `bronze/orion-api/{date}/transactions.csv` | de-converted txn pull -> `bronze/transactions/{date}.jsonl.gz` | confirm silver txn built from new bronze |
| A5 | `inf-api-assets-v2` | 45 12 | `bronze/.../assets` | de-converted assets pull -> `bronze/assets/{date}.jsonl.gz` | confirm silver assets_v2 from new bronze |
| A6 | `inf-api-positions` | 50 12 | `bronze/.../positions` | de-converted positions pull -> `bronze/positions/{date}.jsonl.gz` | confirm silver positions_mv from new bronze |
| A7 | `inf-unified-account-dim-daily` | 40 12 | `bronze/orion-api/{date}/unified_account_dim.csv` | INF_API_PULL_UNIFIED | confirm accounts_dim reads unified from CHAIN_PULL |
| A8 | `inf-accounts-v2-daily` | 35 12 | `bronze/orion-api/{date}/new_portfolio_accounts.json` | CHAIN_PULL accounts_v2 leg | confirm accounts_v2 consumers |
| A9 | `inf-api-reps` | 30 12 | `bronze/orion-api-v2/{date}/{representatives,household_rep_mapping}.json` | CHAIN_PULL reps leg | **HIGHEST CARE** -- household_rep_mapping feeds accounts_dim + household; confirm repoint landed |

**Per-leg mechanic (each of A1..A9):**
1. Open ledger entry. Run the consumer-trace gate (Rule 20). RED -> STOP, repoint first.
2. Disable the EventBridge rule (reversible): `aws events disable-rule --name <rule>` OR set
   `is_enabled = false` in TF + `safe-apply`. Lambda + code untouched.
3. SOAK one scheduled cycle. Confirm the bronze artifact still appears (from CHAIN_PULL) via
   `comp-freshness`, and gold/platinum still GREEN via `validate_post_swap`-class check.
4. Andrew-confirm -> delete the TF resource blocks + `safe-apply` -> 0-diff. Close ledger.

**A9 caveat:** `household_rep_mapping.json` is a LEG-1 dependency (accounts_dim + household repoint).
Do NOT disable A9 until the household repoint to accounts_v2 has landed AND soaked -- else household
geo goes stale again (the exact 1204h-stale incident this refactor fixes).

### A9 precondition -- LEG-1 household repoint (GROUNDED 2026-06-30, execute post-cutover)

The freeze mechanism, source-confirmed: `data/inf/scripts/silver/convert_orion_api_to_silver.py`
`build_household()` L141 -- `geo = read_bronze_csv(snapshot_date, 'geo_verify')`. household silver
sources household_id / household_name / state_code / city / country / rep_id / rep_name from the
**frozen** `geo_verify` bronze CSV (last 20260428 -> household frozen 05-11 / 1204h stale). AUA comes
from unified (unchanged, not the freeze). The gold layer already half-patches this: INF_D_00d
`_supplement_hh_dim_state()` L174 back-fills `state_code` gaps from `accounts_v2.state` (ADVI_INFTGT.TO-4b,
$14M invisible GEO-AUA fix) -- proving accounts_v2 is fresh + carries `household_id` + `state`.

**The repoint:** move `build_household`'s geo source from `geo_verify` -> `accounts_v2` (fresh,
CHAIN_PULL-produced daily; silver `silver/api_dims/accounts_v2/`), AUA still from unified.

**Field-coverage RESOLVED 2026-06-30** (accounts_v2 silver 2026-06-30 = 863 rows, 45 cols, FRESH).
The 7 geo_keep fields map as -- 5 clean, 1 constant, 1 sourced-elsewhere:
| household dim field | accounts_v2 source | note |
|---|---|---|
| household_id | `household_id` | clean |
| state_code | `state` | clean (rename) -- this is the field INF_D_00d already patches |
| city | `city` | clean |
| rep_id | `rep_id` | clean |
| rep_name | `representative_name` | clean (rename) |
| country | (constant `US`) | all Inflection accounts are US; or carry last-known. Trivial. |
| household_name | NOT in accounts_v2 | **redundant in this dim** -- real consumers source it elsewhere: INF_A_04.client_dimension loads household_name from `silver/aum_snapshot` (L83-84); INF_D_04 from its own `Household.Name` map. Confirm no consumer reads household_name FROM `silver/api_dims/household/` (comp-blast), then null/drop it, OR left-join from aum_snapshot for completeness. |

Disposition: **near-clean single-source swap** -- 5 fields direct from accounts_v2, country constant,
household_name dropped/null (or aum_snapshot join). No re-introduction of geo_verify. Execute
post-cutover with fresh silver in place; final consumer-check on household_name first (Rule 20).
This repoint gates A9 -- A9 stays LAST until it lands + soaks.

---

## GROUP B -- redundant / stub producers

| # | Resource | Evidence | Action |
|---|----------|----------|--------|
| B1 | `inf-client-detail` Lambda (10240MB) | STUB, W4.6 never implemented; `get-policy` = ResourceNotFoundException (no API Gateway wired); no S3 output; frontend-orphan. Client detail is served from `platinum/firm/client_directory.json`. | Confirm no wiring -> delete TF (Group-B leg). Reclaims 10GB reserved memory config. |
| B2 | `INF_D_00e.fresh_header_supplement.py` | Superseded freeze workaround; producer git-rm'd (a406ed891); removed from all 5 chains. | DONE (backend). Verify no chain still references it (`comp-grep INF_D_00e`). |
| B3 | `platinum/firm/header_metrics_fresh.json` (324B) S3 object | Orphaned -- its INF_D_00e producer is gone; FE DEV consumer removed (ad97d915). | S3 object delete (destructive -> Andrew-confirm). Verify 0 consumers via `comp-platinum reverse` first. |

---

## GROUP C -- yahoo thread artifacts (GROUND-TRUTH AT EXECUTION)

COO named "the yahoo thread artifacts" for decommission. NOT in the `advi-inf` estate thread --
likely a separate price-feed thread. **To ground before drafting legs:** `pipescript --resource yahoo`
+ `comp-blast` on any yahoo-produced artifact to confirm zero live inf consumers. Held as a
placeholder leg-group; do not author delete steps until the resource set + consumer trace is grounded.
(Flagged, not silently dropped -- CLAUDE.md no-silent-cap.)

---

## Execution sequence (day-after checklist)

1. **P0** categorical parity: 3 consecutive GREEN nights. (gate)
2. **Group B** first (lowest risk: stubs/orphans, no live cron). B1, B2-verify, B3.
3. **Group A** leaf-first: A1 -> A2 -> A3 (tax/billing/perf: isolated dims) -> A4 -> A5 -> A6
   (txn/assets/positions: de-converted) -> A7 -> A8 -> A9 (account/reps: highest fan-in, A9 last).
4. **Group C** only after grounding (§C).
5. Final: `pipescript advi-inf --validate` clean; update `EC2_MANIFEST.json` / source map if any
   runner role narrows; deploy-hygiene single-home sweep.

**OUT of decommission scope (do NOT retire -- separate sources):** `inf-bronze-runner-ec2` (Orion
Eclipse bulk pull -- a DIFFERENT data source from the REST API CHAIN_PULL); `inf-ec2-launch-resilience`
(reliability automation); `inf-gold-*` (the compute stage the refactor KEEPS). Verify each stays wired.
