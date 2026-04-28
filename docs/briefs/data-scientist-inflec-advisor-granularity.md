# Briefing — Inflection Orion Data Lacks Advisor-Level Granularity for BD/49F Portal Parity

**Author:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-04-27
**Audience:** 1.0.0_SA_CTO (via Andrew)
**Project:** ADVI_INFGRD (Phase 0 audit) → portal-layout strategic implication
**Source data:** `s3://opal-data-inf/bronze/orion/2026-04-21/` — full TRN (1.29M rows, 631 MB), AUM (979 rows), SlickGrid (1,476 accounts)

---

## 1. Executive Summary

The Inflection portal was being built to mirror the BD/49Financial advisor-centric layout (per-advisor leaderboard, per-advisor books, per-advisor compositions, per-advisor timeseries, drill-down panels). After auditing the Orion bronze CSVs to identify the firm-membership filter for ADVI_INFGRD, **the data does not support advisor-level granularity for Inflection.** Specifically:

- **Inflection has 4 employees** (Peter, Noel, Patrick, Joe — Andrew's list).
- **Only 2 of the 4 carry Orion `Rep ID` rows with their own client books.** Peter Lee (rep_id=12, 6 HH, $5.85M) and Patrick Scanlan (rep_id=11, 2 HH, $594K).
- **The other 2 (Noel, Joe) have no Orion rep_id at all.** They appear nowhere in the `RepName` / `Rep ID` columns across TRN, AUM, or SlickGrid. Their client-facing work either rolls up under the firm-level `rep_id=3` bucket or doesn't generate client-attributed transactions in Orion.
- **287 of Inflection's 295 households (97.3% by count, 96.8% by AUA) sit under the firm-level placeholder `rep_id=3` "Inflection Wealth Management"** — a single un-decomposed bucket. There is no Orion-side breakout of which Inflection employee manages which of these 287 HH.

**Implication:** the BD/49F advisor-centric portal panels (leaderboard with per-advisor entries, AdvisorBookView, per-advisor composition, advisor rolling flows, AdvisorPublicProfile, etc.) cannot be meaningfully populated for Inflection. They would render with 2 sparse advisors representing 3.2% of AUA, plus a giant unattributed bucket holding the other 96.8%. This is structurally worse than BD/49F's pattern and likely worse than no advisor-level UI at all.

**Recommendation for CTO discussion:** rethink Inflection portal layout. Treat it as a firm-centric tenant rather than forcing the advisor-centric mold.

---

## 2. Data Evidence

### 2.1 Full Orion rep inventory (base TRN, 1,288,096 rows scanned)

| Rep ID | RepName | HH (AUM) | Managed Value | TRN rows | Andrew's name match |
|---|---|---:|---:|---:|---|
| 3 | Inflection Wealth Management | 287 | $193,630,146 | 330,779 | firm placeholder (Noel + Joe likely aggregated here) |
| 11 | **Patrick Scanlan** | 2 | $594,439 | 68 | ✓ Patrick |
| 12 | **Peter Lee** | 6 | $5,845,497 | 1,559 | ✓ Peter |
| 4 | Keil Financial Partners | 10 | $6,171,347 | 1,830 | (Keil) |
| 5 | Jeremy Keil | 69 | $107,922,833 | 130,509 | (Keil) |
| 9 | John Kurcz | 128 | $84,586,748 | 222,321 | (Keil) |
| 13 | Dan Sinnen | 141 | $104,799,463 | 161,917 | (Keil) |
| 14 | Tim DeMuth | 183 | $92,850,865 | 244,977 | (Keil) |
| 15 | Kevin Christensen | 151 | $70,327,402 | 181,047 | (Keil) |
| 18 | Daria Zalewska | 1 | $388,692 | 1,019 | (Keil) |
| 1 | New Accounts Rep | 1 | $19,615 | 12,070 | routing placeholder |

**Total firm AUM in Orion:** $667,296,137 (matches `ADVI_INFLEC.md §2`).
**Inflection-only AUM (rep_id ∈ {3, 11, 12}):** $200,070,082, 295 HH.

### 2.2 Search for Noel and Joe across all 29 TRN columns

Word-boundary regex search on full base TRN (1.29M rows × 29 columns):

- **`\bnoel\b`**: 1,175 hits, all in column `Reg Name`, single distinct value `"Noel Soderblom"` — a CLIENT registration, not an advisor.
- **`\b(joe|joseph)\b`**: 9,791 hits, all in column `Reg Name`, 12 distinct values: `"Joseph J Holub"`, `"Joseph Marchewka"`, `"Joseph Becker"`, etc. — all CLIENTS, no advisors.
- **No hits in `RepName`, `CreatedBy`, `EditedBy`, `Description`, `TranNotes`, or any other field.**

Conclusion: Noel and Joe do not have rep_ids in Orion. Their work is either bucketed under rep_id=3 (firm placeholder) or untracked at the transaction level.

### 2.3 The 287-household firm bucket is opaque

The 287 households assigned to `rep_id=3 "Inflection Wealth Management"` carry no per-employee tag. Audit confirms:
- `RepName` is uniformly `"Inflection Wealth Management"` (no per-employee variant).
- `EditedBy` is uniformly `"DO 2768"` (a single Orion data-ops user account, not per-employee).
- `CreatedBy` is various Fidelity Single Line identifiers (G-prefix or IWS-prefix) tied to FIDELITY's account-rep identity, not Orion's per-employee identity. These don't decompose by Inflection employee.
- No `office`, `parent_rep`, `team`, `branch`, or sub-rep field exists in any of the 3 export types (TRN 29 cols, AUM 10 cols, SlickGrid 14 cols).

Per the PRD §2.3 / §9 Q1 hypothesis-list, **none of the candidate firm-membership / sub-advisor fields exist in the data we get from Orion.** What exists is `Rep ID` only.

---

## 3. Structural Implication for Portal

### 3.1 BD/49F advisor-centric panels — 5 of 17 panels structurally compromised

Per `INFLEC_BD_PARITY_MATRIX.md` v0.1 (commit `5dfa6a12`), 17 portal panels currently target Inflection. The advisor-level subset:

| # | Panel | BD/49F input | INFLEC under current data |
|---|---|---|---|
| 7 | AdvisorsTab leaderboard | per-advisor entries with role_breakdown | 2 sparse entries (Peter, Patrick) covering 3.2% AUA + giant firm placeholder |
| 8 | AdvisorsTab top-3 highlights | top 3 advisors by NNA / AUA | only 2 advisors exist as candidates |
| 9 | AdvisorsTab rolling flows (per-advisor LineChart) | per-advisor timeseries | renders for 2 advisors; 4 of 4 employees not all represented |
| 13 | AdvisorBookView panels (book, composition, mix, NNA clients, exec summary) | per-advisor S3 keys | only Peter + Patrick have populated advisor folders |
| 15 | AdvisorPublicProfile (Profile tab, non-admin) | reads leaderboard entry for own advisor_id | works for Peter / Patrick; Noel + Joe have no Orion advisor_id to bind to |

**These 5 panels render technically but tell a misleading story.** A user clicking "Advisors" sees 2 names (Peter, Patrick) plus the 287-HH firm bucket they don't recognize as a separate "advisor." The 4-employee mental model is not reflected anywhere.

### 3.2 Firm-centric panels — 12 of 17 panels remain fully viable

| # | Panel | Status under firm-only data |
|---|---|---|
| 2 | PartnerAnalytics header tiles | Renders correctly (firm AUA, NNA, q0..q3, NMNC/Existing radial — all firm-aggregate) |
| 3 | PartnerAnalytics period bars + GRO + Mix | Already correct (`timeseries_overview.json` post `159cadb5` fix) |
| 4 | PartnerAnalytics firm mix area chart | Already correct |
| 5 | DistributionTab snapshot (donut + bell) | F2 fix landed — renders aua + nna views; geo/adv as empty stubs (DROP per matrix) |
| 6 | DistributionTab continuous (stacked area) | Pending F4 emitter; geo + adv at firm level only |
| 11 | BooksTab firm dashboard | Pending F5 emitter + dashboard.json employee_leaderboard gap |
| 14 | ClientDetail drill-down | Works (`platinum/clients/{hh}/detail.json` per HH; 297 entries written) |
| 16 | DataSource footer / cohort note | Cohort A DROP per matrix |
| 17 | FidelityCustodianBar | Works (Inflection-only override) |

The firm-level panels have data backing for 100% of Inflection's 295 HH. They tell a coherent story: "Inflection manages $200M across 295 households, growing X% YTD, decomposed by client cohort and time."

### 3.3 The advisor-centric build is the wrong abstraction for this tenant

The BD/49F portal pattern was built around a firm of 150 offices × hundreds of advisors with a Schwab-grade rep-attribution model. That model assumes:
1. Every transaction is rep-attributed
2. Reps map to firms via stable IDs
3. Per-advisor performance is meaningful at scale

Inflection violates all three assumptions:
1. 96.8% of Inflection AUA flows through the firm bucket — not rep-attributed in any granular sense
2. The 4-employee firm has 2 employees with rep_ids, 2 without
3. Per-advisor performance comparisons across 2 reps with $6.4M combined book = signal noise, not insight

Forcing the BD/49F mold here produces a panel set that is technically correct (renders) but narratively incoherent (Peter has 6 HH; Patrick has 2 HH; the rest of the firm is "?").

---

## 4. Path-Forward Options (for CTO discussion)

### Option A — Firm-only Inflection portal (recommended)

Drop / hide advisor-centric panels for `firmId === 'inflection'`. Show firm-level metrics only.

- DE adds suppression rules (panels #7, #8, #9, #13, #15 hidden on Inflection view)
- Header tiles, partner analytics, books firm dashboard, client detail drill — all stay
- Inflection portal becomes a clean firm-level tenant: "Inflection Wealth Management — $200M AUA, 295 HH, growing X%"
- Easy to ship; matches data; no maintenance debt

**Cost:** loses parity narrative with BD/49F. The Inflection page looks structurally simpler than BD's. Likely fine for v1 since Inflection is a smaller firm; the simpler view is more honest.

### Option B — Synthesize per-employee partition inside the firm bucket

Maintain a manual `inflection_employee_assignment` mapping table: `{hh_id → employee_name}` where `employee_name ∈ {peter, noel, patrick, joe}`. Build per-employee leaderboard / books / etc. from this synthetic partition.

- Requires Andrew (or someone at Inflection) to provide the HH → employee mapping
- High maintenance burden — every new client needs assignment, every employee transition needs updates
- No data backing — purely a portal-side narrative overlay
- Risks staleness / drift from reality

**Cost:** large maintenance burden; ongoing accuracy risk; arguable whether it's better than just showing the firm view.

### Option C — Push Orion config change for per-employee rep_ids

Request Orion (vendor) to issue per-employee rep_ids for all 4 Inflection employees. Inflection updates each HH's `Rep ID` assignment in Orion to map to the correct per-employee rep. Bronze runner (W3.B per `ADVI_INFLEC_BRONZERUN_V2.md`) eventually enforces this at the export step.

- Solves the granularity gap at the source — best long-term solution
- Requires Inflection-side configuration change in Orion + back-population of historical HH assignments
- Long lead time (likely weeks-to-months)
- Possible future state once Inflection's account-management workflow stabilizes

**Cost:** time + Inflection cooperation. Doesn't help v1 ship.

### Hybrid recommendation

- **v1 (now):** Option A — ship firm-centric Inflection view; suppress advisor-centric panels via `firmId === 'inflection'` feature flag in DE.
- **Track for future:** Option C as the proper architectural fix when Inflection's Orion config is upgraded. ADVI_INFGRD already documents this as the "long-term vision" (PRD §8).
- **Do NOT do Option B** without explicit Andrew sign-off on the maintenance burden.

---

## 5. Filter Implementation (ADVI_INFGRD.002 unchanged)

The data finding does not change the silver-layer filter. INFGRD.002 still implements:

```python
INFLECTION_REP_IDS = {3, 11, 12}  # firm placeholder + Peter Lee + Patrick Scanlan
firm_mask = df['rep_id'].astype(int).isin(INFLECTION_REP_IDS)
```

- Captures all Inflection AUA ($200M, 295 HH including Peter+Patrick's 8 HH and the firm-bucketed 287 HH where Noel+Joe operate)
- Drops contamination ($467M, 684 HH from Keil affiliates Tim DeMuth, Kevin Christensen, Dan Sinnen, John Kurcz, Jeremy Keil, Keil Financial Partners, Daria Zalewska)
- Routing placeholder (rep_id=1) remains excluded via existing `rep_bucket='routing'`

Sanity check: $200.0M vs Andrew's $191M = +4.7%, within ±5% tolerance.

The portal-layout question is downstream of the filter. The filter ships as planned; the layout question is the orthogonal CTO/DE/Andrew decision.

---

## 6. Open Questions for CTO + Andrew

1. **Adopt Option A (firm-only) for v1?** If yes, COO scopes a DE TO for panel suppression rules.
2. **Is Inflection's Orion config upgradeable to per-employee rep_ids** (Option C path)? If feasible, the bronze runner work item should be prioritized.
3. **Are there other BD/49F portal patterns** worth evaluating against Inflection's data shape now (rather than discovering similar gaps panel-by-panel later)? The parity matrix v0.2 review pass is the natural place to do this.
4. **Should `ADVI_INFGRD.002` ship as designed** (rep_id allowlist filter), or is there value in pausing until the layout question is resolved? My recommendation: ship the filter now (data correctness is independent of layout), pursue layout decision in parallel.

---

## 7. References

- `docs/architecture/ADVI_INFGRD.md` — parent PRD
- `docs/architecture/INFLEC_DATA_INVENTORY.md` (commit `7d28f000`) — DS-side data inventory
- `docs/architecture/INFLEC_PORTAL_FIELD_USAGE.md` (commit `0c241ee0`) — DE-side portal panel inventory
- `docs/architecture/INFLEC_BD_PARITY_MATRIX.md` v0.1 (commit `5dfa6a12`) — joint parity matrix
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFGRD.001.ds-phase0-orion-csv-firm-tag-audit.md` — Phase 0 TO
- `data/orion/scripts/silver/convert_orion_to_silver.py:105-144` — `_apply_scopefix` filter site
- Source CSVs: `s3://opal-data-inf/bronze/orion/2026-04-21/{trn,aum}/*.csv` + `SlickGridExport_AlongsideL.csv`

---

## Addendum — 2026-04-28 — ORIAPI integration does not resolve the granularity gap

**Author:** 0.4.0_DS_ClientPlatform~A
**Trigger:** ADVI_ORIAPI breakthrough cascade (DS~B `e824e0fd` Orion API path discovery + AE 0.6.1~B v1.5.7/v1.5.8 autonomous JWT/Twilio/boot dispatch). CTO `a78362ac` ADVI_INFLV2 v0.2 amendment; CTO `34d2b757` new ADVI_INFSHIP synthesis PRD.
**Authority:** COO ACK 20260428T0344Z — addendum (not rewrite); brief's structural finding stands.

### A1. What ORIAPI changed

The Orion Connect API is now driveable end-to-end programmatically:
- `POST /api/v1/Reporting/Envision/ExcelReports/Verbose` creates queries from arbitrary schema
- `POST /{id}/Generate` runs them; CSV downloaded directly
- Autonomous JWT acquisition via `inf-jwt-trigger` Lambda + Twilio webhook + EC2 boot dispatch (no human in the loop except Orion 2FA recipient swap)
- Per-account dim pulls live for: Performance (TWR/Sharpe/Sortino/Drawdown/RSquared/StdDev), Tax (CostBasis/GainLoss 3-level paths), Geography (Household.StateCode/City), Activity (with `activityOptionId` per metric), Billing (fee subset for ~22% Inflection coverage)

Capability shifts catalogued in `docs/architecture/ADVI_INFSHIP.md` §1.1 + §1.2 (8 portal-ship verdict shifts for L4 + L3 + N1 panels).

### A2. What ORIAPI did NOT change

**The advisor-granularity gap is structural, not delivery-channel.**

The Orion *data model* still represents Inflection's 4 employees as:
- rep_id 3 — "Inflection Wealth Management" (firm-level placeholder; 821 accts / $191.9M / 96.1% of firm AUA)
- rep_id 11 — Patrick Scanlan (2 accts / $594K / 0.3% of firm AUA)
- rep_id 12 — Peter Lee (29 accts / $6.95M / 3.5% of firm AUA)
- (no rep_id for the other 2 Inflection employees — they exist in HR but not in Orion's Representative table)

The API surface confirms this empirically. Pulled via the new programmatic path on 2026-04-28:
- `silver/api_dims/household` (commit `ee1ddbbb`): 852 accts × 308 HH × `rep_id IN {3, 11, 12}`. Same rep_id distribution as the manual-CSV bronze scope. The API does not surface additional rep_ids; it just delivers the same data faster.
- `silver/api_dims/performance`: same 852 / 308. TWR + risk metrics now per-account, but advisor attribution still firm-bucket-only for 96% of AUA.
- `silver/api_dims/activity`: same 852 / 308. Cashflows fully decomposed (contributions, distributions, dividends, advisory fees), still under `rep_id=3` for the firm bucket majority.

### A3. What this means for portal layout

**Option A (firm-centric layout, 3-entry advisor list) still applies post-ORIAPI.** The brief's recommendation in §5 stands without modification:

| Panel/Module | Status post-ORIAPI |
|---|---|
| AdvisorsTab (drop entirely for Inflection) | UNCHANGED — drop |
| AdvisorPublicProfile non-admin | UNCHANGED — suppress |
| BooksTab L2 advisor list | UNCHANGED — 3 entries (IWM firm + Peter Lee + Patrick Scanlan); ADVI_INFLV2.008 freeze stands |
| Per-advisor mix/composition publishers (D_02, I_D03) | UNCHANGED — only meaningful for Peter and Patrick (4% of AUA combined); the other 96% is firm-bucket |
| Per-HH and per-account publishers (D_04, L4 summary, L3 timeseries) | **ENHANCED by ORIAPI** — these benefit from API enrichment (Geo, Performance, Tax, Billing) regardless of advisor structure |

### A4. What ORIAPI did improve

Even though advisor-granularity stays gapped, ORIAPI delivers real wins for the firm-centric layout:
- **Daily refresh** vs ~weekly manual CSV cadence
- **No Andrew-in-the-loop** for routine pulls (Twilio + Remember Device handles 2FA on most refreshes)
- **Per-account dims** now available for Performance + Tax + Geo that were previously absent or partial — this is what unlocks BooksTab L4 (account modal) and L3 (per-HH detail) panels
- **Reconciliation testable** — the API independently confirms the firm AUA ($199M API ~= $200M silver, +0.3%) which the previous manual-CSV path could only triangulate via Andrew's $191M target

### A5. Long-term path (unchanged)

Option C (Orion vendor config to add per-employee rep_ids for the other 2 Inflection employees) remains the only structural fix for the granularity gap. ORIAPI does not bypass the need; the API surface inherits whatever rep_id schema Orion is configured for. `ADVI_INFLEC_BRONZERUN_V2` parking lot still owns this when/if Andrew prioritizes the vendor request.

### A6. References (added since v1)

- `docs/architecture/ADVI_INFSHIP.md` (CTO 34d2b757) — synthesis PRD that incorporates this finding
- `docs/architecture/ADVI_INFLV2.md` v0.2 (CTO a78362ac) — layout v2 amendment with ORIAPI integration
- `docs/architecture/ADVI_ORIAPI.md` v0.5 + Appendix B — API contract + autonomous JWT
- `data/orion/manual_api/PATH_DISCOVERY.md` — Orion API path catalog
- `data/orion/scripts/silver/convert_orion_api_to_silver.py` (commit ee1ddbbb) — silver/api_dims/* converter (this addendum's empirical evidence)
- `s3://opal-data-inf/silver/api_dims/{household,performance,activity}/snapshot_date=2026-04-28/data.parquet` — empirical confirmation of the rep_id distribution post-ORIAPI
