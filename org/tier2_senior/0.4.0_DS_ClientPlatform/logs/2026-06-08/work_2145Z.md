# 0.4.0_DS_ClientPlatform — work_2145Z (ADVI_COTETL: Cottonwood BD partner — full API-first bronze ETL build, discovery → ENABLE-pending)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, EXPLORE, DEPLOY, VALIDATE, SCRIBE

## Summary
Andrew-direct new project: onboard **Cottonwood Capital Advisors (COT)**, a Black Diamond partner like 49 Financial, onto the Opal medallion. From a HAR + two CSV exports this morning to a deployed, verified, dual-path **API-first bronze ETL** landing real COT transactions + AUA into `opal-data-cot` by evening. Reverse-engineered BD's DataMining REST API, resolved the advisor-dimension open-decision (§6.1 = no advisor dim), characterized AUM ($372.9M), spec'd the medallion port, built/deployed the ingest, cracked a stubborn `v1/run` blocker (missing `asOfDate`, not session-context), built production templates, persisted + verified both served objects, and confirmed the AUA rep-split dedup. Transactions PASSED CVO gate; allocations confirmed (AUA $372.9M not $729.8M) → on CVO full PASS, AE flips EventBridge ENABLE = live daily feed. Plus: GLDINC B_00 `--force-recent-days` at Andrew's 14-day BD standard; P4 FIRM_ID de-hardcode (5 D_* scripts).

## Key technical outcomes
- **API-first feasible + standard-mandated** (THIRD_PARTY_DATA_INTEGRATION_STANDARD): BD DataMining REST flow = `auth/token (Bearer) → v1/run → poll status → ExportResults`. Credential pattern mirrors Inflection (JWT) / YCharts (cookie): Secrets Manager `blackdiamond/cot/session` (AE-owned refresh).
- **5 BD query types pinned** (HAR-2/3): qt2 Transactions, qt5 Allocation, qt3 Realized, qt4 Unrealized, qt1 Holdings/Snapshot. Shared ~205-dim core + per-endpoint specialty + measures. (Full catalog brief.)
- **§6.1 RESOLVED → Outcome B** (Andrew sovereign): no usable advisor dimension. Advisor fields empty across Snapshot(qt1)+Allocation(qt5) probes; Rep Code = 2-founder joint-coverage (G46018202+G46018211 paired on 96% AUA), 3rd FA (G46018204) under-tagged on 2 new accounts (Schmitt, first activity 05/01/2026). Rep-tagging is current-state-only (not historically observable). → SKIP C_07/leaderboards/adv-cohort for v1; Lusha NOT needed; qt5 (not qt1) for allocations.
- **AUM = ~$372.9M** (642 accounts, 196 households, 5.3% cash, 96% Fidelity IWS). The **rep-split double-count** (each account 2 rows by founder rep-fee-split; account_market_value constant per row): naive sum $729.8M = 2x; the inherited `drop_duplicates(subset=['AccountID'], keep='last')` collapses to the true $372.9M. The one number that would've shipped 2x wrong — caught by CVO's served-artifact gate + the port-spec caveat.
- **Port = "1 new script + env-repoint":** silver (`merge-daily-incremental.py`) is generic + BD_S3_BUCKET-parameterized; `silver col == to_snake_case(BD display-name)`. Only new code = `cot_bronze_ingest.py`.
- **`v1/run` root cause (long hunt):** the run body requires a top-level `asOfDate` (sibling to `template`) — omitting it 500s. NOT session/firm-context (that whole trail was a red herring; AE's diag confirmed firm 4175/team 6714 resolved). Proven definitively by running Andrew's own template 225437 verbatim (also 500'd without asOfDate). AE's HAR finding #2 spotted the field.
- **Both served objects verified (production SSM/EC2 path):** transactions 68-col/19,009-row (Market Value 100%, classification 100%), allocations 38-col/1,235-row (account_market_value 100%, Timestamps present).

## Briefs Written
| Brief | Path | Audience |
|-------|------|----------|
| HAR auth / API-first | docs/briefs/cw-cca-har-auth-api-first-analysis-20260608.md | CTO/PRD |
| Field population | docs/briefs/cw-cca-transactions-field-population-analysis-20260608.md | CTO/PRD |
| Medallion port plan | docs/briefs/cw-cca-bd-pipeline-deepdive-medallion-port-plan-20260608.md | CTO/PRD |
| Table↔endpoint cross-ref | docs/briefs/cw-cca-bd-table-endpoint-crossref-20260608.md | DS/AE |
| Advisor/office §6.1 P3-prep | docs/briefs/cw-cca-advisor-office-dimension-p3prep-20260608.md | Andrew §6.1 |
| Bronze/silver port spec | docs/briefs/cot-bronze-silver-port-spec-20260608.md | DS/AE/CVO |
| §6.1 resolution | docs/briefs/cot-s6.1-advisor-dimension-resolution-20260608.md | CTO/COO/CVO |
| Full field catalog | docs/briefs/cot-datamining-full-field-catalog-20260608.md | Reference |

## Files Modified
| File | Change |
|------|--------|
| data/cot/scripts/bronze/cot_bronze_ingest.py | NEW — API-first BD DataMining bronze ingest (auth/run/poll/export/land; asOfDate fix; persist-then-run; full-cookie-jar) |
| data/cot/scripts/bronze/templates/transactions.json | NEW — production qt2 template (CW_Transactions_Rich + 5 measures, 68 cols) |
| data/cot/scripts/bronze/templates/allocations.json | NEW — production qt5 template (38-col, advisor-probe dropped, account_market_value) |
| data/black_diamond/scripts/gold/D_00/00b/00c/01/02.py | P4 — FIRM_ID/FIRM_NAME → os.environ.get (per-partner; defaults preserve 49F) |
| data/black_diamond/scripts/gold/B_00.canonical_holdings.py | GLDINC — added --force-recent-days N (14-day BD restatement-lookback standard) |

## Commits (key)
| SHA | What |
|---|---|
| b8832a8df | 3 discovery briefs |
| 6541ed2b9 | P4 FIRM_ID de-hardcode (5 D_*) |
| e81cdba85 | B_00 --force-recent-days (Andrew 14d standard) |
| 0a9d3983c | §6.1 resolution (Outcome B) |
| 864419a80 | table↔endpoint cross-ref (5 qt types) |
| 0064084a1 | port spec + AUM/rep-split caveat |
| 7d6080d50 | cot_bronze_ingest asOfDate ROOT-CAUSE FIX |
| 5a38914c0 / 0f3925afe | production transactions / allocations templates |

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-pipescript io | 5 D_* (P4) + B_00 | NO COLUMN GAPS |
| comp-pipescript deployed | B_00, D_* | MATCH |
| ds-commit-gate | every .py edit (cot_bronze_ingest, B_00, 5 D_*) | PASS (py_compile + ds-precommit + ruff); resolved pre-existing ruff debt in D_00b/D_00c (safe-fix + noqa, behavior-preserving) |
| (live BD API probes) | DimensionsFacts qt1-5, v1/run reverse-engineering, deep body-diff | cracked the run contract (asOfDate) |
| (served-artifact verify) | both forwardfill_v2 objects + AUA dedup | transactions PASS, allocations AUA $372.9M confirmed |

## Next Steps
- [3.0.0_SA_CVO] Render allocations PASS on the AUA-dedup confirm (214133Z) → full gate PASS.
- [0.6.2_AE_PartnerETL] On CVO PASS, flip EventBridge cot-bronze-daily-trigger ENABLE = live daily COT bronze feed. Confirm trigger scope = transactions + allocations (the 2 ready tables) for v1.
- [DS — self, next increment] Build realized(qt3) + unrealized(qt4) production templates (tax/gains); drop the 9 residual billing cols from allocations on next finalize.
- [DS — self] Once silver runs on COT bronze, verify silver/allocations AUA reconciles to ~$372.9M (642 accounts) live; then the gold port rides on top (P4 done, platinum config-only).
- [VERIFY tomorrow nightly] 49F firm_id='49financial' unchanged after P4 (de-hardcode behavior-preserving); B_00 stays --force tonight, AE flips CATALOG to --force-recent-days 14 post-nightly.

## Notes
- Project renamed ADVI_CCAETL → ADVI_COTETL (cot canonical); briefs use cot-* going forward; literal BD template names (CW_Transactions_Rich, CW_Allocation) preserved as external literals.
- New AE 0.6.2_AE_PartnerETL owns the credential/refresh/IAM/EC2 infra; clean seam = AE writes blackdiamond/cot/session, DS reads it.
- All P0-independent + the live build were Andrew-driven turn-by-turn; the asOfDate red-herring (firm-context) hardened AE's session-fetch as a side benefit.

work-cycle:0007
