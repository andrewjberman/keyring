# Session 48 — DIAGFIX.010 Close + Geo Donut ACK + Wave 4 Active

**COO:** 2.0.0_SA_COO | **Date:** 2026-04-29 | **Continuation of:** Session 47 (PUSHFIX + INFGRD.006 dispatch)

---

## Inbox at Session Open

4 messages — all RAVC EVIDENCE / ACK from earlier sessions:

| From | Subject | Disposition |
|------|---------|-------------|
| 0.4.0_DS_ClientPlatform | RAVC ACK — DIAGFIX.010 GO received — starting Phase 1 bronze pull | Logged; superseded by EVIDENCE messages |
| 0.4.0_DS_ClientPlatform | RAVC EVIDENCE — DIAGFIX.010 Phase 1+2 SHIPPED | Verified |
| 0.4.0_DS_ClientPlatform | RAVC EVIDENCE — DIAGFIX.010 Phase 3+4+5 SHIPPED | Verified — RAVC-CLOSE sent this session |
| 0.6.1_AE_PartnerETL | RAVC — Geo donut fix shipped + DIAGFIX.009-NEW pricing-strategy TO filed | Verified — ACK sent this session |

## Ground Truth Verification

| Cited commit | Verified | Author |
|--------------|----------|--------|
| `2979c12a7` DIAGFIX.010 Phase 1+2 (bronze pull + silver convert) | YES (469 ins / 0 del) | DS |
| `e106bc7b8` DIAGFIX.010 Phase 3 (INF_I_D03 refactor — regex classifier killed) | YES (101 ins / 98 del) | DS |
| `6f60a47eb` DIAGFIX.010 Phase 4 (INF_I_D02d composer metadata propagation) | YES | DS |
| `e39ebd025` Geo donut fix (INF_D_04 _build_geo_view aum_snapshot source) | YES (67 ins / 36 del) | AE 0.6.1 |
| `394c34606` New DIAGFIX.009 TO (DS holdings pricing strategy) | YES (150 ins) | AE 0.6.1 |
| `03fb28ea0` DS session log DIAGFIX.009 VERDICT A + DIAGFIX.010 5-phase | YES | DS |

## DIAGFIX.010 — RAVC Validation + Definitional Verdict

**Acceptance:** all 5 phases shipped end-to-end with live re-run executed; mix_summary.json republished with classification_method=orion_native_v1 metadata.

**Win-condition reframe accepted.** COO TO target (44.8/21.3/5.4/28.5 ±2pp) was a mis-interpretation of Andrew's UI screenshot — that breakdown was top-9 named Morningstar Categories + a UI-display "Other" residual ($52.03M / 28.5%), NOT a true alternatives bucket. The Orion-native 4-bucket split (with alternatives extracted from Equity via asset_class keyword discriminator: Real Estate / Allocation / Multi-Asset / Target-Date / Commodities / Hedged / Long-Short / etc.) lands at:

| Bucket | Actual | Regex (was) | Delta |
|--------|--------|-------------|-------|
| equity | 53.93% | 70.29% | -16.36pp |
| fixed_income | 30.93% | 15.22% | +15.71pp |
| alternatives | 8.08% | 1.79% | +6.29pp |
| cash | 6.53% | 12.70% | -6.17pp |
| (unmatched) | 0.53% | n/a | small dim drift |

Bond-ETF over-classification (HTRB / BAGIX / BSIIX / BSNIX / TFEBX) fully fixed — was equity under regex, now correctly fixed_income via Orion productCategory=Bond. Alternatives 4.5x improved. **The classification source is now Orion-native and the regex over-classification problem is dead.**

DELETED in Phase 3 (DS): _CASH_PATTERNS / _FIXED_INCOME_PATTERNS / _ALTERNATIVES_PATTERNS / _INTL_EQUITY_PATTERNS / _classify_keyword / _normalize_classifier_pk / _load_bd_securities_cache / _classify / BD_SECURITIES_TABLE / _VALID_ASSET_CLASSES / _TICKER_ALPHA_RE / _NAME_SLUG_RE / _BD_SECURITIES_CACHE / _dynamodb resource. Net diff +3 lines but file significantly cleaner — 4 dead functions + 5 dead constants gone.

**bd-securities dependency completely eliminated.** D_03 IAM (dynamodb:Scan on bd-securities) — moot.

## Geo Donut Fix — RAVC Validation

INF_D_04 `_build_geo_view()` now sources AUA from aum_snapshot.managed_value per HH (canonical, same pattern as views.aua). Null/empty state_code routes to 'Other' instead of being excluded. Fallback to holdings.market_value retained when aum_snapshot unavailable.

- `views.geo.donut.total = $182,552,381` (matches firm AUA exactly)
- All 274 HHs had state data — 0 routed to 'Other' on this run
- WA dominates at 89.9% ($164.2M, 237 clients); CA/IN/MT/MN/TX/ID/AZ each 0.6-2.0%
- CF invalidation: `I87P8RW9ERQIRHLBA3GZ6CNVGE` (/platinum/firm/partner_analytics* + dashboard.json)

**Effective implication:** ADVI_INFGRD scope is now structurally complete. INFGRD.006 Task A managed_value column fix (DS) + downstream geo donut fix (AE 0.6.1) close the last aggregate views inheriting broken holdings totals.

## TO Status Updates (Edits Performed This Session)

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.010.ds-orion-native-classification-build.md` | status pending → complete + closure_evidence + closure_note |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.009.ds-orion-morningstar-category-hunt.md` | status pending → complete + closure_evidence (VERDICT A) |
| `org/projects/ADVI_INFLEC.json` | blocking field rewritten — Wave 3 closed (DIAGFIX.008/009-old/010), Wave 4 active (DIAGFIX.009-NEW pricing) |
| `org/projects/ADVI_INFGRD.json` | blocking field rewritten — .006 complete, geo donut downstream fix shipped, scope effectively closed |

INFGRD.006 TO status was already `complete` (DS~A self-marked); not edited.

## Numbering Collision Flagged

AE 0.6.1's new TO `ADVI_INFLEC.DIAGFIX.009.ds-holdings-pricing-strategy.md` (filed 394c34606) collides with old `ADVI_INFLEC.DIAGFIX.009.ds-orion-morningstar-category-hunt.md` (now complete). DS already ACK'd both contextually. Both flagged to DS + AE 0.6.1 via MCP this session.

**Recommendation:** rename new TO to DIAGFIX.011 in next dispatch wave for registry hygiene. Not halting DS Phase 1; file naming change will follow. Logged here so future COO sessions don't re-route the same TO.

## Follow-on TO Candidates (Logged from DS Phase 5 RAVC)

Not authored this session; tracked for future dispatch:

1. **Brandenburg attribution — DS_ClientPlatform scope.** 21 households / 67 accounts / $16.22M show silver `accounts_v2.representative_name` = 'Inflection Wealth Management' instead of 'Joe Brandenburg' (rep_id=6). Existing pull reads Orion's primary rep, not servicing rep. Resolvable via `GET /api/v1/Portfolio/Clients?representativeId=6` (returns the 21 cleanly). Augment silver accounts_v2 with `servicing_rep_id` / `servicing_rep_name` columns; downstream gold scripts honoring servicing rep where present. Doesn't block — Brandenburg's $16.22M already gets correct asset_class on Phase 3 chain re-run. Files for future TO authoring.

2. **Reporting/Scope endpoint discovery (HAR 7) — Books-tab follow-on candidate.** `POST /api/v1/Reporting/Scope` (flexible calc engine: Activity series / Performance series / Grouping by Asset Category with full per-asset detail + units/price/value rolled up). `POST /api/v1/Reporting/Custom/{reportId}/Generate/SlickGrid` (custom report runner). Significantly richer than current `/Portfolio/Clients/{id}/Assets`. Out of DIAGFIX.010 scope but enables future Books-tab work.

## Open Items at Session Close

| Item | Owner | Status |
|------|-------|--------|
| New DIAGFIX.009 (pricing strategy) Phase 1 Orion endpoint probe | DS 0.4.0 | DS ACK'd, executing |
| AE 0.6.1 stale heartbeat summary refresh | AE 0.6.1 | Flagged via MCP — "On HOLD — waiting for COO re-run GO after DS DIAGFIX.002a ships" is 2 waves stale |
| ADVI_ORIAPI Cycle 1 gate | — | 2026-04-30 12:13Z (first clean fire expected; AE 0.6.1 RAVC4 after) |
| ADHC_PUSHFIX | AE 0.7.0 | COMPLETE (registry confirms a27fdf831 + d1762a594 shipped) |
| ADHC_OWNPTH.009 tilde-alias fix | AE 0.7.0 | LOWER PRIORITY |
| ADHC_COMPIL.002 cascade gate | AE 0.7.0 | ACTIVE per session 46 |
| Brandenburg + Reporting/Scope follow-on TOs | COO | Logged, pending Andrew priority signal |
| DIAGFIX.009 numbering rename | COO | Pending — propose DS Phase 1 RAVC return as authoring trigger |

## Compiler Tools

| Phase | Command | Result |
|-------|---------|--------|
| N/A | No comp-* applicable | TO status edits + JSON edits + session log only — no Python or script changes by COO |

## COO Commit Scope

```bash
.tools/safe-commit.sh --author "2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>" \
  -m "dispatch(2.0.0_SA_COO): session48 — DIAGFIX.010 close + geo donut ACK + ADVI_INFLEC/INFGRD JSON updates" \
  -- org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.010.ds-orion-native-classification-build.md \
     org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.009.ds-orion-morningstar-category-hunt.md \
     org/projects/ADVI_INFLEC.json \
     org/projects/ADVI_INFGRD.json \
     org/tier1_exec/2.0.0_SA_COO/logs/2026-04-29/session48_diagfix010_close_geo_donut_ack.md
```
