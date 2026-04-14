# 0.4.0_DS_ClientPlatform -- Afternoon Session

**Date:** 2026-04-14 (EDT)
**Session span:** ~11:50 EDT to ~13:40 EDT (post-lunch continuation)
**Agent:** 0.4.0_DS_ClientPlatform

---

## Startup

Registered (PID 32048). Inbox empty on first check. Compiler context set.
Read morning session log (full_session_log.md) — continuing from where that left off.

Working from same 2026-04-14 date — this is the second session of the day.
Morning session shipped: D_00b fix #3 (OFC 1-office anomaly, commit 5b4439e1) and
D_02 canonical NNA all-role equal-weight refactor (commit d51e44ef).

---

## Work Completed This Session

| Work Item | Type | Commit | S3 ETag |
|---|---|---|---|
| Sydney Cobb NNA investigation (for Andrew) | Research | — | — |
| ADVI_OFFICE.W5 — verification of fix #3 covering continuous chart | Verification | — | — |
| ADVI_OFFICE.W9a — add ofc/nna_ofc to D_04 build_cumulative_chart | Feature | `416806a5` | a82c4bc0 |
| adv-donut-account-count — D_01 ADV segment account_count | Feature | `0ce31899` | 3facf1fa (superseded) |
| adv-donut-architect-filter — D_01 primary_role filter | Feature | `b7ee381b` | 04d1e49f (bundled) |
| PROFAU.007 prep — is_fee_paying scope check | Scoping | — | — |

---

## Sydney Cobb NNA Investigation

**Triggered by:** Andrew's case-study question about NNA attribution for a primarily local_ops advisor.

**Findings:**
- Role breakdown: 525 local_ops accounts ($139.5M AUA, 97.4% of book) vs 8 architect accounts ($2.9M AUA).
- Current model: D_02's `drop_duplicates('account_id')` picks one advisor per account (architect priority). Sydney's 525 local_ops accounts contribute $0 NNA — the architect "owns" them.
- NNA appears only Q3 2024 onward ($2.49M cumulative at 9/30/2024, +$408K Q4 2024) — matches Andrew's portal observation exactly. That's from her 8 architect accounts.
- AUA panel is a separate story — all roles aggregated without dedup. AUA jumped $46M → $137M on **April 7, 2026** in a single day: ~$108M of local_ops accounts added to her book (client migration event).
- After D_02 fix (`d51e44ef`) runs, Sydney's nna_canonical will reflect her equal-weight share of all 533 accounts' flows.

**Status:** Explanation delivered to Andrew. No code action — investigation-only.

---

## ADVI_OFFICE.W5 — Continuous Chart Confirmation

**Triggered by:** COO urgent check — "does fix #3 (5b4439e1) also fix OFC stacked timeseries, or only categorical views?"

**Answer:** Both. `_build_office_view` (D_00b:286) is the single function feeding both donut/histogram (`ofc_categories`) and continuous chart (`ofc_data`). The dict-key normalization fix corrects lookups for both paths.

**Verification:** Downloaded `platinum/firm/timeseries_chart.json` —
- `ofc.categories`: 10 offices (Austin, Dallas, LA, Jacksonville, Arkansas, Atlanta, Minnesota, Kansas City, Houston, Other)
- `ofc.data`: 2,291 daily rows (2020-01-02 to 2026-04-10)
- Latest row totals look real ($931.6M Austin, $367.8M Dallas, etc.)
- `nna_ofc`: same 10 categories, 2,291 rows

COO response: W5 accepted, W7 AE gold re-run is a no-op (QA run covered it).

---

## ADVI_OFFICE.W9a — D_04 ofc/nna_ofc in cumulative_chart

**Triggered by:** DE message to COO — `getPlatinumCumulativeChart()` reads `platinum/firm/cumulative_chart.json`, which has no `ofc` key. Portal falls through.

**Root cause:** `D_04.build_cumulative_chart()` (line 1519) extracts only geo/adv/nna_geo/nna_adv from `timeseries_chart.json` — ofc/nna_ofc never promoted to cumulative_chart.

**Fix:** 12-line addition following the exact geo pattern (lines 1553-1572):
```python
ofc = ts_chart.get('ofc', {})
nna_ofc = ts_chart.get('nna_ofc', {})

# and in chart dict:
'ofc': {
    'description': ofc.get('description', ''),
    'categories': ofc.get('categories', []),
    'data': _weekly_downsample(ofc.get('data', [])),
},
'nna_ofc': {...},
```

**Deployment:**
- Commit `416806a5`, pushed CLOUD
- S3 upload ETag `a82c4bc0b008443ca8fcbf94ca273d62`
- AE ran D_04 locally `--upload` (per Andrew's direction — no gold runner needed)
- AE confirmed exit 0, 20,476 platinum files written, ofc keys present in `platinum/firm/cumulative_chart.json`

**W9b verification (my spot-check):**
- ETag `5480356839d22dacf16192e47f67d611`, last-modified 17:04:42 UTC
- `ofc.categories`: 10 offices, 333 weekly rows. `nna_ofc`: same. Values match source.

---

## adv-donut-account-count (D_01)

**Triggered by:** RD found ADV donut segments had `relationship_count` but not `account_count`. Frontend `getRadialCount` falls back to `client_count` (mislabeled as relationships), showing wrong number.

**Fix:** `account_count` added to ADV segments in both D_01 code paths:
- Multi-role path: `len(adv_acct_ids)` (already-computed set)
- Fallback path: `int(arch_accts['account_id'].nunique())`

**Commit:** `0ce31899`. Initial ETag `3facf1fa` (superseded by bundled upload below).

---

## adv-donut-architect-filter (D_01, bundled)

**Triggered by:** DE found Alex Bright (local_ops primary) appearing in top-9 ADV donut. Intent: donut should show advisors whose PRIMARY role is architect, not anyone tagged as architect on a handful of accounts.

**Context:** COO flagged that AE was holding on D_01+D_04 re-run so I could bundle this into the same D_01 upload as account_count. (I had pushed too early on account_count alone — lesson: check for other in-flight scope before pushing.)

**Implementation:**
- Added `advisor_role_aua: dict[str, dict[str, float]]` tracking per-advisor per-role AUA in the multi-role loop
- Computed `primary_role[adv] = max(role_aua.items(), key=lambda kv: kv[1])[0]` after the loop
- Filtered `adv_sorted` to only advisors where `primary_role == 'architect'`
- Fallback path unchanged (already architect-keyed via adv_ts)

**Commit:** `b7ee381b` (25 insertions, 3 deletions). Combined ETag `04d1e49fcb119bc3cd62dbca73ba5880` sent to AE as combined GO — supersedes the earlier `3facf1fa`.

**Status:** AE holding released. Waiting on AE local D_01+D_04 run.

---

## PROFAU.007 Scoping

**COO request:** "Prep PROFAU.007 while DT pushes W4. Scope: add is_fee_paying per AdvisorClient entry in D_02 output."

**Finding:** The data work is already done. PROFAU.002 (commit `f2507121`) added `is_fee_paying` to D_02's `book.clients` list. NaN-bug fix followed (`b0ad9811`). Today's 10:01 EDT gold run produced live platinum — verified against Sydney Cobb: 241 clients, `is_fee_paying` present on every entry (0 missing), 28 fee-paying / 213 non-fee.

**Recommendation to COO:** Author PROFAU.007 as DE-only. DE scope is (1) add `is_fee_paying: boolean` to the AdvisorClient TypeScript type, (2) wire the L2 count split, (3) spot-check Sydney Cobb values.

**COO response:** Confirmed, authored as DE-only, DS clear of PROFAU work.

---

## Pending / Waiting

| Item | Blocked on |
|---|---|
| AE D_01+D_04 local run | AE (combined ETag delivered 17:38 UTC) |
| Travis Penfield 221M → 253M portal fix | D_02 gold run (fix is in S3, nightly will pick up; or on-demand local run) |
| ofc-l2-advisor-distribution (D_03) | Per COO: after AE clears D_01+D_04 |
| Q3/Q7 fee_earning_mask audit gaps brief | Discretionary, COO suggested |

---

## Compiler Tools

| Phase | Tool | Script | Result |
|---|---|---|---|
| W9a before write | comp-pipescript io | D_04 | Confirmed timeseries_chart in READS, cumulative_chart in WRITES |
| W9a before commit | py_compile | D_04 | SYNTAX OK |
| W9a after upload | ETag verify | D_04 | a82c4bc0 confirmed |
| adv-donut-account-count before write | comp-pipescript io | D_01 | Ran (confirmed I/O manifest) |
| adv-donut-account-count before commit | py_compile | D_01 | SYNTAX OK |
| adv-donut-architect-filter before commit | py_compile | D_01 | SYNTAX OK |
| PROFAU.007 scoping | comp-pipescript io | D_02 | Confirmed book.clients path, client_detail does NOT contain is_fee_paying |
| W5 verification | S3 artifact check | timeseries_chart.json | 10 offices, 2,291 rows verified |
| W9b verification | S3 artifact check | cumulative_chart.json | ofc/nna_ofc keys confirmed |

---

## MCP Signals Sent

| To | Subject | Outcome |
|---|---|---|
| 2.0.0_SA_COO | PROFAU.007 prep findings | Delivered, DS cleared |
| 2.0.0_SA_COO | W5 confirmed — fix #3 covers continuous timeseries | Delivered, accepted |
| 0.6.0_AE_PartnerETL | W9b GO + ETag a82c4bc0 (initial) | Delivered |
| 0.6.0_AE_PartnerETL | W9b update — run D_04 locally per Andrew | Delivered |
| 2.0.0_SA_COO | W9a complete | Delivered |
| 2.0.0_SA_COO | W9b complete (AE verified) | Delivered |
| 0.6.0_AE_PartnerETL | adv-donut-account-count GO (ETag 3facf1fa) | Delivered, later superseded |
| 2.0.0_SA_COO | adv-donut-account-count complete | Delivered |
| 0.6.0_AE_PartnerETL | Bundled D_01 GO — combined ETag 04d1e49f | Delivered |
| 2.0.0_SA_COO | Architect filter bundled, AE has combined ETag | Delivered |

---

## Files Modified

| File | Change |
|---|---|
| data/black_diamond/scripts/gold/D_04.client_portal_summary.py | ofc/nna_ofc added to build_cumulative_chart (12 insertions) |
| data/black_diamond/scripts/gold/D_01.partner_analytics.py | account_count on ADV segments + primary_role=architect filter (27 insertions, 3 deletions total across two commits) |

---

## Task Orders Flipped

| TO | Status change |
|---|---|
| ADVI_OFFICE.W9a.ds-cumulative-chart-ofc-key | pending → complete |
| adv-donut-account-count | pending → complete |
| adv-donut-architect-filter | pending → complete |

---

## Do NOT Rules (session observations)

- Do NOT push a gold-script commit before checking for other in-flight scope changes in the same file. adv-donut-account-count shipped too early; COO had to intercept AE to hold so I could bundle the architect filter. Pattern: when COO says "prep Y while X is queued", scan for any sibling TOs touching the same file.
- Do NOT conflate `relationship_count` and `account_count` on donut segments — they are different grains. A single relationship can contain multiple accounts.
- Do NOT assume primary role from role-tagged-on-account-count alone — it must be AUA-weighted. An advisor can be architect on 8 small accounts and local_ops on 500 large accounts; primary is local_ops.
