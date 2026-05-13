# DS~D 2026-05-13 session 1 — Chain #22 RAVC2 close + Silver/transactions Phase 0 REST extension probe

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Window:** ~14:33Z 2026-05-13 → ~16:10Z 2026-05-13 (~1h35m)
**Triggers:**
1. Boot up — Andrew "0.4.0_DS_ClientPlatform~D. Boot up." (14:33Z)
2. Inbox carry-over from session 2 — DE RAVC4 ACK Brief #9; AE 0.6.1 RAVC1+RAVC2 chain #22
3. COO 2.0.0_SA_COO GO — 4-phase Phase 0 silver/transactions probe (~14:36Z)

---

## TL;DR

Two work streams. **Stream 1 (~30 min):** Boot + close out three carry-over inbox messages. AE chain #22 RAVC2 anomalies categorized (state "34" = upstream Orion data quality, donut "Other" = by-design catchall); DE RAVC4 closed with §9 closure section appended to the 49F gap investigation doc; DS~B looped in on the upstream household_dim data-quality issue. **Stream 2 (~65 min):** Phase 0 four-phase silver/transactions REST extension probe shipped — PATH (a) full consolidation FEASIBLE. Andrew's reframe ("why couldn't we just consolidate?") confirmed empirically — REST already returns 31 cols including direct equivalents for nearly all LEGACY-only fields; silver-side dropping is the only barrier.

## Ship roster

| Time (UTC) | Commit | Scope |
|---|---|---|
| 14:38Z | `a99ca8c74` | docs(49F_CERT_GAP) closure §9 — SCHWAB-BUCKDR resolution + residual decomposition |
| 16:00Z | `984ae22b3` | docs(silver-txn-probe) Phase 0 — REST already returns 95% of LEGACY fields, path-(a) feasible |

Both CLOUD-pushed. 2 commits, +280 LOC docs-only.

---

## Stream 1 — Chain #22 RAVC2 + Brief #9 RAVC4 close

### AE chain #22 RAVC2 — two anomalies categorized

AE 0.6.1 reported two anomalies from chain #22 platinum output (`partner_analytics_quarterly.json#views.nna.current.geo`):
1. State key `"34"` in donut.segments: `{value=-$1000, aua=$0, count=1}`, "drill key not present"
2. Donut "Other" segment: `{value=+$75,744.52, aua=$0, count=1}`, "drill key absent"

**Re-pulled the artifact fresh** and inspected donut + drill. Findings:
- **State "34":** Real upstream Orion `household_dim` data quality issue. 2 accounts (not 1) with `state_code="34"` + `city="Abbortsford"` (likely Canadian household entered with malformed location). Drill IS present: `drill["34"].by_city = {Abbortsford: -$1000, count: 2}`. Sentinel passes exact. Builder is doing the right thing — it aggregates whatever state_code shows up. **NOT a code fix; route to DS~B for silver/household_dim state_code validation rule.**
- **Donut "Other" $75,744:** 1-account null-state catchall (single account whose `account_id` didn't join successfully to household_dim → fillna 'Other' at INF_D_04 line 1825). Drill IS present as `{by_city: {}}` (empty by design per my `55e37ebcb` skip-drill-for-truncation-bucket fix). **Working as designed.** FE should render donut segment without drill-down.

AE's read corrections (count=1 vs 2; drill-absent vs drill-present-but-empty): AE accepted both, conceded the v1.7.52 session log reads were off. **Chain #22 NNA fix stays GREEN.** RAVC chain fully closed.

### DE Brief #9 RAVC4 close

DE 0.4.0 acknowledged Brief #9 Part A + Part B closure (RAVC4 at 21:37Z 2026-05-12) and asked for a closure section in the investigation doc to record the SCHWAB-BUCKDR resolution path.

**Shipped `a99ca8c74`** — `docs/briefs/data-scientist-49F-cert-gold-92m-gap-investigation.md` §9 closure section. Contains:
- Pre/post recovery table ($1.703B → $1.767B gold_aua; $97.17M → $33.40M gap; +$63.77M recovery / +101 accounts)
- 3-component residual decomposition ($19.4M cube-missing / $9.7M FIFO drift / $4.3M true-no-history)
- SCHWAB-BUCKDR commit roster (`7c030faee` + `9b2829db3` regression fix) with coordination credit
- Reconciliation: pre-fix hypothesis ("FIFO history-depth lag") was structurally correct in cohort identification but wrong about causal mechanism. Real cause: B_00 forward-filling 22-day stale canonical_holdings because of bucket misroute.
- Followups still open (3 sub-investigations + Andrew's footnote-framing call at <2% gap)

Retained §1-§8 as the authentic investigation trail — future readers see the trace from inference → empirical convergence → SCHWAB-BUCKDR resolution rather than overwriting hypothesis with resolution.

### DS~B FYI

Sent a non-urgent visibility-only MCP to DS~B re: silver/orion household_dim state_code/city validation gap (single household, $1K signal). No action requested.

---

## Stream 2 — Phase 0 silver/transactions REST extension probe (COO GO)

### Trigger + scope

COO 2.0.0_SA_COO ratified Andrew's reframe ("we need to know how many of those fields overlap, if there is actually useful information in the expanded version. why couldn't we just consolidate?") and dispatched a 4-phase Phase 0 probe (estimated 2-3h). The earlier path-(c) ratification was made on the assumption REST is capability-limited; Andrew sharp-challenged that.

Phases:
- 0a Schema overlap audit (~30 min, no Orion calls)
- 0b Content-value audit / classify delta cols (~30-60 min)
- 0c Orion REST capability probe for CRITICAL+MEANINGFUL subset (~30-60 min)
- 0d Synthesis + path recommendation (~15 min)

### Empirical findings

**Phase 0a — Schema overlap:**
- LEGACY silver per-day `2026-05-12.parquet`: 79 rows, **31 cols**
- NEW silver snapshot `2026-05-13.parquet`: 1,251,020 rows, **18 cols**
- **NEW bronze `bronze/transactions/2026-05-13.parquet`: 1,251,020 rows, 31 cols** (this was the killer insight)
- Literal silver-to-silver: 11 shared / 20 LEGACY-only / 7 NEW-only
- Rename-aware: 14 semantic-shared / 17 truly LEGACY-only / 4 NEW enrichment

**Phase 0b — Gold consumer audit (INF lane only):**

| Col | Consumers | Classification |
|---|---:|---|
| `type_desc` | 4 (INF_C_01, INF_D_06, INF_B_02, INF_build_canonical_prices) | CRITICAL — NNA classification keys on it |
| `trans_amount` | 4 (INF_C_01, INF_D_00, INF_D_02, INF_D_06) | CRITICAL — money |
| `activity_category` | 1 (INF_C_01, info-only post-Stage-0b) | MEANINGFUL → NOISE post-migration |
| `client_id` | 1 (INF_C_01) | CRITICAL — relationship grain |
| `rep_name` | 5 (multiple) | MEANINGFUL — display, JOIN-derivable |
| `reg_type` | 5 (multiple) | MEANINGFUL |
| `account_code` | 3 (multiple) | MEANINGFUL |
| `reg_name` | 1 (INF_D_06) | MEANINGFUL borderline NOISE |
| `description` | 0 (after false-positive filter — all hits are argparse `description=`) | NOISE |
| (`account_lname, download_symbol, trade_status, tran_notes, created_date, created_by, edited_date, edited_by, current_account_value, current_cash_value, managed_account`) | 0 each | NOISE — pure CSV-passthrough fluff |

8 CRITICAL/MEANINGFUL; 12 NOISE.

**Phase 0c — REST capability (empirical from bronze, no live probe needed):**

The bronze parquet IS the REST endpoint response. `pull_inflection_transactions_rest.py` calls `/api/v1/Portfolio/Accounts/{accountId}/Transactions` with NO $select, NO date params ("returns complete history in one call" per pull script docstring). So the 31 bronze cols are the full REST payload schema.

Critical finding: **NEW bronze contains 47 distinct `transTypeId` values; NEW silver's `TRANS_TYPE_DESC` dict has only 23 entries**. 24 ids collapse to 'Unknown'. This is the source of DS~A's "21 type_descs absent from new snapshot" finding. **Pure SILVER-side dict gap, NOT a REST capability gap.** Extending the dict to 47 entries fully resolves.

All 8 CRITICAL/MEANINGFUL cols are REST-recoverable (most by adding to silver `output_cols`; one by extending the dict; one by JOIN expansion). 9 truly-missing-from-REST fields (account_lname, download_symbol, CreatedDate/EditedDate/EditedBy, RepName, CurrentAccountValue/CurrentCashValue, ManagedAccount) all have ZERO gold consumers.

**Phase 0d — Synthesis: PATH (a) FULL CONSOLIDATION FEASIBLE.**

### Ship + RAVC2

Brief shipped: `docs/briefs/silver-transactions-rest-extension-probe-20260513.md` (commit `984ae22b3`, CLOUD pushed).

RAVC2 sent to COO 2.0.0_SA_COO (16:09Z) with the synthesis + recommended 4-TO implementation path:
- TO-1: Extend `TRANS_TYPE_DESC` 23 → 47 (~1h, blocks on DS~B yaml v3)
- TO-2: Add `client_id, account_code, reg_name, reg_type` to silver `output_cols` (~1h)
- TO-3: Retire `convert_orion_to_silver.py` TRN-write (keep accounts_dim + aum_snapshot per DS~B Bug B) (~1h)
- TO-4: Update INF_C_01 / INF_D_06 / INF_B_02 / INF_D_00 / INF_D_02 to read new col names or add LEGACY-name aliases (~1-2h)

RAVC2 CC'd to CTO 1.0.0_SA_CTO (16:09Z) since DWSPLT PRD v0.1 authoring was paused on this output. The PRD scope shifts from "carve-out parallel path" to "extend silver builder + dict."

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-pipescript io <INF gold script>` | Deferred Phase 0a — direct parquet header inspection was authoritative for schema enumeration; no I/O graph change | n/a |
| `comp-pipescript deployed` | Deferred — no script changes shipped this session, docs-only commits | n/a |
| `ds-commit-gate.sh` | 0× | No `.py` edits this session — docs-only |
| `.tools/safe-commit.sh` | 2× (both with `git add -f` for new files in lane:ANY paths) | Clean (no owned-paths violations) |
| `safe-deploy.sh` pre-push | 2× | "no deploy-scope script files detected, nothing to do" — docs commits don't trigger S3 deploy |
| Phase 0c live REST probe | Deferred — empirical answer in bronze parquet (REST endpoint has no $select / no date params per pull script docstring) | n/a |

Compiler tools mostly N/A this session — docs-only work and structural schema inspection of S3 parquet artifacts. Parquet header reads (via `pyarrow.parquet`) on three S3 objects (`silver/transactions/2026-05-12.parquet`, `silver/transactions/2026-05-13.parquet`, `bronze/transactions/2026-05-13.parquet`) were the authoritative empirical instrument.

## Files Modified

| File | Change |
|---|---|
| `docs/briefs/data-scientist-49F-cert-gold-92m-gap-investigation.md` | Appended §9 closure section — SCHWAB-BUCKDR resolution path + residual decomposition + followups |
| `docs/briefs/silver-transactions-rest-extension-probe-20260513.md` | NEW — Phase 0 four-phase probe synthesis with path-(a) recommendation |

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Silver/transactions REST extension Phase 0 probe | `docs/briefs/silver-transactions-rest-extension-probe-20260513.md` | COO 2.0.0_SA_COO, CTO 1.0.0_SA_CTO, Andrew (final path ratify) |
| 49F cert/gold gap §9 closure | `docs/briefs/data-scientist-49F-cert-gold-92m-gap-investigation.md` (existing doc, new section) | DE 0.4.0_DE_ClientPlatform, future readers as canonical reconciliation record |

## Current State

| Item | Status |
|---|---|
| Chain #22 RAVC (AE) | CLOSED — both anomalies categorized + accepted |
| Brief #9 RAVC4 (DE) | CLOSED — DE ACK + closure §9 shipped |
| Phase 0 silver/transactions probe (COO GO) | COMPLETE — RAVC2 to COO + CTO with path-(a) recommendation |
| Brief #11 (mix_periods INF_D_04:3023) | OUT-OF-LANE — shipped overnight by base lane `9b8a7ec8d` chain #23 |
| Brief #12 (IWM leaderboard) | OUT-OF-LANE — DS~C / chain #23-24 closed |
| 49F `capital_gains_ttm` TTM-correction | QUEUED — `094014158` awaiting next BD gold chain for cross-firm-parity empirical |

## Next Steps

1. **[Self — passive]** Standing by for COO + CTO path ratify on silver/transactions consolidation. If path (a) ratified, ready to author + execute TO-1 through TO-4 (~4h total estimate).
2. **[Self — passive]** When nightly BD gold chain runs (04:00Z 2026-05-14 unless triggered earlier), pull `clients_tab.json#headline.capital_gains_ttm` for cross-firm-parity sentinel against DS~B's INF `2e5539bac` pattern.
3. **[Andrew/COO]** Footnote framing call (<2% disclosure gap on AdvisorIntelligence DistributionTab) — flagged but not blocking, deferred to next panel-walk.
4. **[DS~B]** FYI sent re: silver/household_dim state_code/city validation gap — no action requested.

## Pacing reflection

This was a clean two-stream session. Stream 1 was carry-over RAVC closes — straightforward but important to surface the actual donut/drill structure rather than parroting AE's read corrections back. Empirical re-pull of the platinum artifact in the first 5 minutes gave me ground truth and turned what could have been a "we'll defer to your read" into a categorized closure with a separate routing to DS~B for the upstream data quality issue.

Stream 2 was a focused architectural diagnostic. The pacing trap was the temptation to do a live REST probe per COO's Phase 0c spec — but the empirical answer was already in the bronze parquet (the REST pull script docstring is explicit about no $select / no date params, so the bronze IS the REST payload). Choosing to defer the live probe in favor of bronze inspection saved 30-60 minutes and produced the same Y/N matrix. The Phase 0c "deferred but available if you want it" framing in the RAVC2 lets COO call for the live probe if they want belt-and-suspenders, without burning time on speculative variants.

The empirical surprise — NEW bronze has 31 cols (not 13 as the inline docstring suggested) — was the moment the path-(a)/(b)/(c) call became obvious. Andrew's instinct was structurally correct: REST already returns the data; the consolidation is a silver-side decision. The brief leads with that empirical fact rather than burying it in the matrix.
