# CVO close-gate cert — ETFS_SETUP/AVGCAP internal-only-scope = PASS

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Window:** ~16:53-17:00Z
**Gate:** ETFS_SETUP/AVGCAP internal-only-scope close-gate — CVO ingestion->presentation /verify on the LIVE presentation artifact. Requested by 2.0.0_SA_COO (DRIVE 165237Z). 0.5.0_AE presentation-deploy live, no code outstanding.
**Scope certified:** INGESTION -> PRESENTATION on the live daily-by-partner artifact. **EXPLICITLY OUT OF SCOPE:** the daily-PUSH (SES recipient-list) activation — that's a separate Andrew SES gate; this cert is independent of it and does NOT assert the push works.

## VERDICT: PASS — the ETF-ownership presentation artifact is live, fresh, reconciles to the cent, and labels provenance honestly. Internal-scope close-gate satisfied.

Grounded on the LIVE served artifact (`s3://opal-data-etfs/platinum/etf_ownership_dashboard.json`), not 0.5.0_AE's citation self-report.

### 4-check (verify-channel) + ingestion->presentation integrity
- **EXISTS:** present at opal-data-etfs/platinum/etf_ownership_dashboard.json (6983 B), Lambda `etf-ownership-dashboard` (PLATINUM_KEY + ETFS_BUCKET env confirmed).
- **FRESH:** LastModified 2026-07-01T16:00:04Z (~55min before cert), generated_utc 16:00:03Z, run_as_of 2026-07-01. Regenerated today.
- **NOT-FROZEN:** daily partitions present for all 3 partners (daily/{49financial,inflection,cottonwood}/); phase-confirmed daily fires 06-28..07-01. Live-firing, not a one-off.
- **SCALED / decision-useful:** grand_total_ownership_value $554,138,015.48; 4-ETF universe (DIVZ $188.7M / IDVZ $159.2M / PFDE $133.3M / PFOE $72.8M); 3 partners; per-ETF-per-partner + partner-total + per-ETF-all-partners rollups (D4's three rollups). Correct magnitude, matches COO's cited $554.14M.

### RECONCILIATION — exact (the ingestion->presentation integrity core)
- **[RECON 1] partner rollup == grand_total to the cent:** sum(49financial 509,354,175.39 + inflection 42,736,704.86 + cottonwood 2,047,135.23) = 554,138,015.48 == grand_total. **delta $0.00.**
- **[RECON 2] ETF rollup == grand_total to the cent:** sum(DIVZ+IDVZ+PFDE+PFOE) = 554,138,015.48 == grand_total. **delta $0.00.** Two independent rollups cross-foot exactly.
- **`_stage_` double-count guard HOLDS:** a `daily/_stage_49f_canonical/` partition exists, but the partner rollup sums to exactly 3 real partners with $0.00 residual — the AVGCAP CANONICAL_PARTNERS allowlist (DS 5dea9da91) correctly excludes `_stage_` from the presentation. No double-count leak.

### PROVENANCE HONESTY (the internal-scope bar — stale data must be labeled, not hidden)
- Per-partner honest labels present: 49financial `basis=daily-granular, days_stale=7, as_of=2026-06-24, freshness='7d stale', source_as_of_worstcase=2026-06-24` — correctly discloses the Schwab batch-cadence lag (D6: ad-hoc every 5-10d, no SLA), NOT masqueraded as current. inflection `days_stale=1, current`; cottonwood `days_stale=2, current`. Every partner carries as_of + freshness + days_stale + worstcase.
- **internal_only: true**, title "Opal ETF Ownership by Partner", SUBJECT_PREFIX "[Opal Internal]" — correctly scoped internal.
- monthly_context wired (available=true, latest_month 2026-06) — the monthly leg (separately CVO-pre-certed 175140Z) is carried in.

### Disposition
- **Internal-only-scope close-gate = PASS.** The ingestion->presentation chain is live, produces a fresh daily artifact, reconciles to the cent across two independent rollups, excludes the `_stage_` footgun, and labels every partner's freshness/basis honestly. COO may close the internal-scope leg.
- **Residual (NOT in my cert scope, flagged for COO/Andrew):** the daily-PUSH (SES recipient-list) activation is a separate Andrew gate — this cert does NOT assert email delivery works. (COO noted the month-end report passed its first live fire today, Andrew-confirmed; that is COO/Andrew's evidence, not mine.)
- **P2 note (non-gating):** 49F is 7d stale by Schwab batch cadence (structural B2, not a defect) — honestly labeled, decision-useful. The next Schwab manual batch refreshes it; freshness is cadence-bound, not broken.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-which` (ETFS artifact) | route | backstop -> rail-checked (found bucket via Lambda env: ETFS_BUCKET=opal-data-etfs) |

What worked: two independent rollups (partner + ETF) both reconciling to grand_total to the cent is the decisive ingestion->presentation integrity proof — a partial/broken ingestion would break one. No comp-tool reads the etfs artifact body / reconciles rollups, so ran rail-checked.

— 3.0.0_SA_CVO
