# CVO close-gate cert — ETFS_SETUP/AVGCAP internal-only-scope = PASS

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Window:** ~16:53-17:00Z
**Gate:** ETFS_SETUP/AVGCAP internal-only-scope close-gate — CVO ingestion->presentation /verify on the LIVE presentation artifact. Requested by 2.0.0_SA_COO (DRIVE 165237Z). 0.5.0_AE presentation-deploy live, no code outstanding.
**Scope certified:** INGESTION -> PRESENTATION on the live daily-by-partner artifact. **EXPLICITLY OUT OF SCOPE:** the daily-PUSH (SES recipient-list) activation — that's a separate Andrew SES gate; this cert is independent of it and does NOT assert the push works.

## VERDICT: PASS — the ETF-ownership presentation artifact is live, fresh, reconciles to the cent, and labels provenance honestly. Internal-scope close-gate satisfied.

Grounded on the LIVE served artifact (`s3://opal-data-etfs/platinum/etf_ownership_dashboard.json`), not 0.5.0_AE's citation self-report.

---

## AMENDMENT 2026-07-01 ~17:20Z (Andrew-challenged — correcting an overclaim + completing the source trace)

**What the original cert overstated:** the "RECONCILIATION" section below labels the two rollups tying to grand_total as "the ingestion->presentation integrity core." That is WRONG. The partner-rollup and ETF-rollup are the two MARGINS of the same per-partner-per-ETF matrix — they sum to the matrix total by construction, so their agreement is an INTERNAL-CONSISTENCY check (catches a dropped partner/ETF or a `_stage_` double-count leak), NOT a source-correctness validation. The original cert did NOT trace a single dollar to the ingestion source. Andrew challenged this directly; the challenge was warranted.

**Source trace now COMPLETE (the real validation), all 3 firms to the cent:**
- **49F** vs raw Schwab RPS `opal-data-bd/schwab/silver/rps/date=20260624/` (match on stripped fixed-width ticker): DIVZ 172,375,369.44 / IDVZ 146,830,347.13 / PFDE 123,202,894.89 / PFOE 66,945,563.93 = $509,354,175.39, EXACT to the cent; distinct-account counts exact (5431/5422/5393/5393 — artifact correctly dedups 2 multi-lot accounts on PFDE/PFOE).
- **Inflection** vs Orion `opal-data-inf/gold/canonical/holdings_2026-06-30.parquet`: $42,736,704.86, all 4 cells EXACT to the cent.
- **Cottonwood** vs Black Diamond `opal-data-cot/gold/canonical/holdings/2026-06-29.parquet`: $2,047,135.23, all 4 cells EXACT to the cent.
- Grand total $554,138,015.48 fully source-grounded. **The numbers are correct** — this UPGRADES the cert from internal-consistency to source-validated.

**Process (grounded from Lambda env):** per-firm producers `bd-49f-etf-ownership-daily` (Schwab RPS) / `inf-etf-ownership-daily` (Orion holdings, sentinel-gated) / `cot-etf-ownership-daily` (Black Diamond holdings), each filtering to `config/etf_universe.json` {DIVZ,IDVZ,PFDE,PFOE} -> `daily/{firm}/{date}.json` -> `etfs-canon-fanin` -> `etf-ownership-dashboard` (+ SES internal). Firm-separated per bucket. NOTE: 49F is on Schwab RPS, NOT SmartX.

**Missing-days findings (business days, ex-Juneteenth 06-19; corrected after a self-caught `ls`-mtime contamination in the first pass):**
- **49F**: output last 06-24; missing 06-25/26/29/30 + 07-01 (5 days). Schwab manual-batch cadence (D6 no SLA) = the honest "7d stale" label. The structural fix is a daily feed (SmartX).
- **Inflection**: output+holdings missing **06-26** (a Friday) though `silver/positions_mv/snapshot_date=2026-06-26/` EXISTS -> the rebuilt gold canonical-holdings compute SKIPPED 06-26 (all holdings re-stamped 07-01 01:06 = last night's INFREF rebuild). A rebuild-completeness gap; CAUSE inferred (rebuild log not yet read). Intersects L1/L6. My L3 timeseries parity would NOT have caught it (staged==served both absent 06-26) — an honest limitation of c5a4fc883. + 07-01 = today.
- **Cottonwood**: output missing 06-23/06-24/06-30 though Black Diamond source HAS those days -> cot producer left 3 available days uncomputed (incl. 06-30, so cot serves a day staler than necessary). + 07-01 = today.

**Net:** the ETFS cert VERDICT (internal-scope PASS) STANDS and is now STRONGER (source-validated). The missing-days items are a SEPARATE data-completeness concern (routing pending Andrew) — they do not retract the PASS on the values that ARE present.

---

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
