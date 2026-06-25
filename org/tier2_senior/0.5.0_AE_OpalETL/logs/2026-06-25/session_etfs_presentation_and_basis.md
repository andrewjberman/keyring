# Session Log -- 0.5.0_AE_OpalETL -- ETFS presentation deploy + 49F-daily basis resolution + W2 refresh

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Date:** 2026-06-25 | **Window:** ~17:59Z (post-W2-log) -> 18:51Z

## Summary

Four COO-dispatched ETFS items: (1) re-invoked W2 on the fresh RPS-thru-06-24 batch; (2) GROUNDED that RPS is daily-granular -> resolved the 49F-daily ~4% basis fork (Andrew confirmed RAW-SCHWAB); (3) pre-staged the canonical/holdings fallback producer; (4) DEPLOYED DE's ETFS presentation-producer as a Lambda + internal reader-IAM + schedule (the last ETFS infra leg). Plus the _stage-double-count correction (structural DS-allowlist fix, no S3-delete).

## 1. W2 refresh (ITEM 1)

Re-invoked the deployed bd-49f-etf-ownership-daily for 06-22/23/24 (fresh RPS batch): wrote daily/49financial slices $518.93M/$513.53M/$509.35M. DS re-ran AVGCAP -> 3-partner June monthly thru-06-24 (49F $515.24M) served.

## 2. 49F-daily basis (ITEM 2 -- the high-leverage grounding)

GROUNDED (Rule 22): the fresh RPS 06-22/23/24 are DISTINCT daily snapshots (own file_dates, distinct DIVZ MVs 172.89M->173.76M->172.38M, varying acct/row counts) -> RPS is daily-GRANULAR at the raw-Schwab basis. FALSIFIED the "~4% fork" premise. Reframed: daily-VALUES(raw-Schwab, no step, v0.9-consistent) vs real-time-FRESHNESS(BD-canonical, ~4% lower). Fed to CTO/CVO -> CVO recommended RAW-SCHWAB -> ANDREW CONFIRMED raw-Schwab. Canonical producer = fallback-only (do NOT deploy). 49F-daily decoupled from silver-fire.

## 3. Canonical fallback producer (pre-staged, NOT deployed)

bd-49f-etf-ownership-daily-canonical built + proven (06-15..06-18) -- surfaced the ~4% BD-reconcile-vs-raw-Schwab basis delta that drove item 2. Stays staged-dormant as the documented fallback (Andrew chose raw-Schwab). Commit 9e89b0d70.

## 4. ETFS presentation DEPLOY (the main deliverable)

DEPLOYED etf-ownership-dashboard Lambda (shared-infra, tag shared-infra-v1.32.0): wraps DE's compute (dashboard_compute.py vendored @5c983f163+), AE handler owns the platinum write + SES push. Daily 16:00Z schedule. Internal reader-IAM: read opal-data-etfs daily/monthly/config + WRITE platinum/* ONLY, ZERO firm-bucket grants.

## Deployment Sequence + Verification (AE)

- code (468e... lineage) -> TF+source-map (shared-infra/etfs-presentation.tf) -> build-and-upload (pipeline=shared-infra -> artifact shared-infra/etf-ownership-dashboard.zip; FIXED TF artifact_key etfs-pipeline/->shared-infra/ after a 404, re-planned) -> plan 9-add/0-change/0-destroy -> safe-apply HALTGT "Apply complete! Resources: 9 added" -> 0-diff "No changes" -> record-deploy (5e23e9dec) + tag shared-infra-v1.32.0 + push -> ledger CLOSE (468e94bde).
- LIVE invoke (deployed role): `{"status":"ok","platinum_key":"platinum/etf_ownership_dashboard.json","grand_total_ownership_value":593732130.11,"partners":3,"push":{"pushed":false,"reason":"ses-unconfigured"}}` -- == local test to the cent. comp-freshness platinum PASS (18:48Z).
- Live get-role-policy: ReadEtfsSlicesMonthlyConfig(daily/monthly/config) + WritePlatinumDashboardOnly(platinum/*) + scoped List; ZERO firm-bucket grants -> NEVER#1 intact, internal-only (CTO-blessed bar met).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-freshness | RPS 06-22/23/24 + canonical/holdings + platinum dashboard | PASS (RPS daily-granular grounding; platinum write verify) |
| comp-iam | service etf-ownership-dashboard + live get-role-policy | PASS (read-etfs + write-platinum only, zero firm-bucket) |
| ds-commit-gate | dashboard lambda_function.py + dashboard_compute.py + canonical producer | PASS |
| comp-glob/comp-grep | DE source, ASTN push, etfs IAM, yang-lambda module, build scripts | PASS (no SES identity exists -> 0.7.0 pull) |

**What worked:** comp-freshness disambiguated RPS daily-granularity (distinct snapshots) cleanly -> drove the basis decision to the simplest answer. Live get-role-policy proved internal-only firm-sep.
**What failed:** build-and-upload keys the artifact by the pipeline ARG (shared-infra), not the TF dir name -> my TF artifact_key etfs-pipeline/ 404'd; fixed to shared-infra/. (Banked: shared-infra-rooted lambdas get artifact key shared-infra/{fn}.zip.) Verified the DE script by RUNNING it (Rule 22) -- my first Read was a stale snapshot showing an undefined `granularity`; the live file is clean (DE renamed to `freshness`), so I did NOT false-flag a bug.
**Gap found:** no SES verified identity in the estate (push-infra) -> pulled 0.7.0; no ETFS-presentation pipescript thread.

## Current State

- ETFS presentation LIVE: Lambda etf-ownership-dashboard (shared-infra-v1.32.0, role etf-ownership-dashboard-role), daily 16:00Z -> opal-data-etfs/platinum/etf_ownership_dashboard.json ($593.73M, 3 partners). PUSH inert until 0.7.0 SES (noreply@opalinvest.dev) + recipient-list + ses:SendEmail Sid -- NO stranded leg.
- 49F-daily basis = RAW-SCHWAB (Andrew-confirmed); W2 producer live (bd-v2.39.0) emits daily slices per RPS batch; canonical producer staged-dormant fallback.
- _stage_49f_canonical: COO held the S3-delete (Andrew gate); DS adds an AVGCAP allowlist (structural); future canonical-prove -> non-daily prefix.

## Next Steps

- **[2.0.0_SA_COO / Andrew]** the SES RECIPIENT LIST (who gets the internal ETF-dashboard email) -> I relay to 0.7.0.
- **[0.7.0_AE_CloudOps]** provision SES identity noreply@opalinvest.dev + verify recipients; give me the identity ARN -> I add the ses:SendEmail Sid + set SES_SENDER/SES_RECIPIENTS env -> push activates.
- **[3.0.0_SA_CVO]** internal-only-scope close-gate cert (citations handed) + re-cert post-SES.
- **[1.0.0_SA_CTO]** the opal-data-bd/schwab/silver/rps canonical-thread reg (taken) + the ETFS pipescript coverage.
- **[0.4.0_DE]** owns dashboard_compute.py canonical (re-sync the vendored copy on change).
