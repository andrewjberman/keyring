# Post-holiday base-lane drive: TAGATTR/COTMVP served-validation + D_00 NNA today-anchor fix (bd+cot) + INF_D_04 WS-4 reconcile — 0.4.0_DS_ClientPlatform

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT, COORDINATE

**Date:** 2026-07-06
**Task Order:** ADVI_TAGATTR.DS-1 + ADVI_COTMVP.B-DS (both closed) + ad-hoc D_00 NNA data-quality fix (0.6.0_AE finding 07-02)
**Status:** COMPLETE

---

## Objective

Monday post-holiday (07-03..07-06 dormancy) base-lane restart per COO DRIVE GO 130757Z: re-confirm the pre-holiday-landed ADVI_TAGATTR.DS-1 full-tagged role emit against the served nightly, resolve the COTMVP.B-DS status (COO believed the DS leg stood-down), then drive the next addressable in-lane item — the still-live 0.6.0_AE D_00 NNA today-vs-data_as_of anchor bug.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript io | io D_00.portal_aggregates | PASS | consumers CLIENTS_TAB + HEADER_METRICS -> D_04; confirmed the NNA emit blast radius before editing |
| comp-pipescript deployed | deployed D_00.portal_aggregates | PASS | 4 MATCH bd-gold after the fix; verified my D_00 deploy |
| comp-pipescript deployed | deployed INF_D_04.client_portal_summary | PARTIAL | defaulted to the bd bucket for an inf script; no firm/tree scoping flag -> fell back to ETag md5 |
| comp-validate | D_00c.portal_leaderboard / D_04 --artifact | FAIL | registry name-resolution: neither the D_00c key nor D_04-as-producer resolves the served leaderboard.json; could not run the automated canonical-equality check |
| ds-commit-gate.sh | bd D_00, cot D_00 | PASS | py_compile + ruff clean, both files |

**What worked:** comp-pipescript io/deployed nailed the D_00 consumer set + deploy MATCH fast; safe-deploy pre-push hook auto-reconciled a stale gold-script deploy (INF_D_04) without manual `aws s3 cp`.
**What failed:** comp-validate could not address the served bd leaderboard.json — `D_00c.portal_leaderboard` isn't a registry key and `D_04` errors as "producer, not artifact-id" (5 artifacts, leaderboard not among the addressable ids). Substituted source-chain + served-label grounding + independent per-role magnitude check.
**Gap found:** (1) comp-validate has no addressable config for the served `platinum/firm/leaderboard.json` (the D_00c/D_04 emit); (2) `comp-pipescript deployed` has no `--tree/--firm` scope flag, so inf/cot scripts default to the bd bucket and report "no match" — both flagged for tool coverage.

---

## Work Completed

### 1. ADVI_TAGATTR.DS-1 — full-tagged role emit CONFIRMED (served + source), TO closed
Validated served `s3://opal-data-bd/platinum/firm/leaderboard.json` (generated 07-04 00:00Z, data_as_of 2026-07-01 — freshest POST-code-landing nightly; BD frozen over holiday). NOT label-only:
- `role_breakdown_semantics = advisor_tagged_full_nonadditive`; per-role `aua_basis = tagged_full_nonadditive`.
- SOURCE chain (D_00c.portal_leaderboard.py): `rd.aua` (L496) <- `at_role_breakdown` <- `_build_at_role_slice(melted, full_tagged=True)` (L1091) off a melt "one row per (account_id, advisor) -- full AUA, no split weight" (L1050), "NO split_pct weighting, NO intra-advisor role normalization" (L1011), canonical role_aua.aua override (L1137-47); split_pct demoted to `avg_split_pct` metadata.
- travis_penfield: architect 328,627,561.48 / implementor 28,341,715.87 / consultant 2,783,237.31 / additional_advisor 948,635.70; total_aua 444,185,773.56 (dedup, unchanged). Split->full magnitude signature: consultant +76.5%, architect ~flat.
- ARCH-GATE 2 EVOLVED (surfaced to COO/CTO): deployed `fee_basis = per_account_actuals_conserved_reconciled_to_c08_canonical` (fees ADDITIVE) per Andrew's 07-01 account-level fee ruling — differs from the TO's original "full-tag fees" text. COO ruled it a sovereign scope-evolution (shipped code correct), reconciling TO text.
- DE FE-loop CLOSED (a58ff3a7): donut center = dedup $444.19M not role-sum $360.70M, false "reconcile to Total" helpText gone, cross-advisor rollup guarded (ARCH-GATE 1).

### 2. ADVI_COTMVP.B-DS — DS emit LIVE-SERVING (not stood down), TO closed
COO believed the DS leg was stood down; live grounding refuted it. Served `s3://opal-data-cot/platinum/firm/client_directory.json` regenerated 07-06 02:05:46Z (data_as_of 07-02): 220 households, shape `{household_id,display_name,aua}`, 0 missing name, sum(aua) $434.17M (~=clients_tab headline), client/household names (not advisor). DE render-verified SOUND (roster populates, 220 sorted by $). COO reconciled TO->COMPLETE + project phase; disambiguated the STOOD-DOWN D1 NMNC-producer leg from this LIVE client_directory emit leg.
- Emit-polish note (DE) grounded to source + DISPOSED: 5/220 households render display_name==id; all 5 are IN the cot client_dimension but with relationship_name==raw-id AND client_name=<NA> (0 firm-wide resolutions), 4/5 dormant (NaT/0-active). Upstream A_04 name-coverage gap on dormant relationships, NOT an emit bug (id-fallback is correct). DE agreed: no A_04 finding needed now.

### 3. D_00 NNA today-vs-data_as_of anchor bug — FIXED on bd AND cot
0.6.0_AE finding 07-02 (CVO-grounded), still live: `build_header_metrics._nna_for_period` + `build_clients_tab._firm_nna_for_period` keyed the MTD/QTD/YTD period boundaries off `today` (run date) instead of `latest_date` (data frontier) -> zeroed nna_mtd/qtd across a month/quarter boundary during any data lag. Fix: anchor `_nna_for_period` cutoffs + period-start day-counts + q0-q3 `_quarter_nna` on `latest_date`. Surgical — legitimate run-date uses (cert-key lookup, cap-gains ttm, tenure, net_flows_ttm) untouched. Proven via boundary-crossing logic sim (old nna_mtd=0 -> new=correct June NNA 17,400). Extended cross-firm to cot (identical bug in build_header_metrics; cot has no firm-NNA clients_tab path). Both DEPLOYED+MATCH (ETag-verified), validate on next bd/cot nightly.

### 4. INF_D_04 WS-4 AC-2 deploy-drift reconcile (incidental, verified, cross-check answered)
The bd D_00 push's safe-deploy hook also deployed DS~A's committed-but-stale `INF_D_04.client_portal_summary.py` (b7ca1a07c) to opal-data-inf. Verified S3==git HEAD (ETag 967729c5). Grounded on the diff (not the message): b7ca1a07c IS the `build_timeseries_overview` `as_of_by_dim` emit DE flagged as the stranded WS-4 last gap — committed 13:33Z / deployed 13:35Z (reconciles the session-start "uncommitted INF_D_04"). Working tree clean, no residual. WS-4 AC-2 all-3-limbs (clients_tab/dashboard-header/timeseries_overview) committed+deployed+MATCH; gap CLOSED. Flagged DS~A + COO + CVO (first-emit-verify on tonight's inf nightly).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Validate TAGATTR on the 07-04 artifact, not wait for "tonight" | BD frozen over holiday -> 07-04 is the freshest POST-code-landing nightly; DRIVE-IMPERATIVE forbids passive "wait for tonight" when the logic is already confirmable. Data-advance re-confirm comes free on the next fresh nightly. |
| Ground the TAGATTR mechanism in source, not accept the label | Verify discipline: a labeling-only change could leave the split value; confirmed `full_tagged=True` chain so the value is genuinely full-tagged. |
| Fix cot D_00 myself in a cot-scoped commit (not route to ~C) | COO GO: rule-13 DS owns cot gold; identical surgical fix; no reason to fragment across lanes. Firm-separated commit (NEVER#1). |
| No code fix for the 5 unnamed cot households | Grounded to source: no name exists anywhere in the cot client_dimension to join; id-fallback is correct. Upstream A_04 gap on dormant relationships, low-value. DE agreed. |
| Defer net_flows_ttm today-anchor | Non-zeroing/low-impact (different metric, engagement block); logged here so it's not lost (COO note). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/.../task_orders/ADVI_TAGATTR.DS-1.*.md` | status->complete + validation_close block | Yes — `739651298` |
| `org/.../task_orders/ADVI_COTMVP.B-DS.*.md` | status->complete + validation_close block | Yes — `739651298` |
| `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` | NNA period windows anchor on latest_date not today (build_header_metrics + build_clients_tab) | Yes — `7272e0705` (DEPLOYED+MATCH) |
| `data/cot/scripts/gold/D_00.portal_aggregates.py` | same fix, build_header_metrics (cot-scoped) | Yes — `997f58fd2` (DEPLOYED+MATCH) |
| `data/inf/scripts/gold/INF_D_04.client_portal_summary.py` | none by me — safe-deploy reconciled DS~A's b7ca1a07c to S3 | (DS~A commit; deployed via my push) |

---

## Briefs Written

None — this session was served-artifact validation + surgical in-lane fixes; no new brief or data-contract.

---

## Blockers

None. All RAVC loops opened this session were CLOSED by COO + DE in-session. Base-lane queue cleared (COO-confirmed); the active INF gold un-freeze is DS~A's lane (perf_dim guard + tonight's dispatch), not this base lane.

---

## Current State

TAGATTR.DS-1 + COTMVP.B-DS TOs are status=complete with validation_close blocks (commit 739651298), both RAVC-accepted by COO and render-verified by DE. The D_00 NNA today-anchor bug (0.6.0_AE finding) is fixed on BOTH firms — bd `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` (7272e0705) and cot `data/cot/scripts/gold/D_00.portal_aggregates.py` (997f58fd2) — both DEPLOYED to their `code/gold/` S3 prefixes and ETag-verified MATCH; they validate on the next scheduled bd/cot nightly (nna_mtd/qtd will populate under lag instead of zeroing). INF_D_04 WS-4 AC-2 (b7ca1a07c, DS~A) is now committed+deployed+MATCH on opal-data-inf, closing the DE-flagged stranded timeseries_overview gap. All bd/cot NNA fixes are code-landed; nothing is half-deployed.

---

## Next Steps

1. **[3.0.0_SA_CVO] first-emit-verify tonight's inf nightly** — INF_D_04 as_of_by_dim on timeseries_overview + dashboard/header + clients_tab (WS-4 AC-2 close-gate).
2. **[3.0.0_SA_CVO] served-verify the next bd/cot nightly NNA** — confirm nna_mtd/qtd populate (non-zero under lag) post D_00 fix (7272e0705 / 997f58fd2).
3. **[0.4.0_DS_ClientPlatform] (self, deferred+logged)** — D_00 net_flows_ttm (L662 bd / L645 cot) shares the today-anchor; non-zeroing/low-impact, fix on next D_00 touch.
4. **[0.4.0_DS_ClientPlatform] hold available** — base lane cleared; event-driven on next COO dispatch. INF un-freeze is DS~A.
