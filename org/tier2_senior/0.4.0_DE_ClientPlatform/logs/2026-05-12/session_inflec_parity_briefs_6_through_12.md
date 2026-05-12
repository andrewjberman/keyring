# Session — Inflec/49F parity briefs #6 through #12 + INFAUACANON FE evolution

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-12 (continuation post-context-summary boundary)
**Predecessor log:** [session_inflec_parity_briefs_1_through_5.md](./session_inflec_parity_briefs_1_through_5.md)

---

## Scope

Continuation of the Inflection portal parity sweep started morning of 2026-05-12. Briefs #1-5 already shipped by DS~C in the morning chain (#15 + #16 + INFLIFECYCLE solo); this session covered briefs #6 through #12, three FE portal commits on the AUA canonicality flow, and one FEEACCFTS portal commit reframing fee-status cards from clients → accounts.

---

## Briefs authored + dispatched

| # | Brief | DS recipient | DS status |
|---|---|---|---|
| 6 | INFLEC_ADVISOR_PUBLIC_PROFILE | DS~C + AE 0.7 | Issue 2b shipped DS~C; Issue 3 Lambda shipped AE 0.7 (`249bfcf47`); FE layout flag deferred to next session |
| 7 | INFLEC_FIRM_OVERVIEW_FEE_VALIDATION | DS~C | INFCTSLIMFIX shipped (`12cae4086`) |
| 8 | INFLEC_DONUT_CANONICALITY (geo+aua UNTAGGED segments) | DS~C | acked, in flight (chain #18 booted with `fad5fd9a5`) |
| 9 | 49F_CERT_GOLD_92M_GAP + firm account counts | DS~D | Part B shipped (`8bb342de4`); Part A doc shipped (`b0d650be7`) |
| 10 | INFLEC firm-level account counts | DS~C | shipped (`eea448321`), awaiting chain regen |
| 11 | INFLEC per-advisor mix_periods (L1 lookback) | DS~C | dispatched, no ack yet |
| 12 | IWM leaderboard vs book.json AUA mismatch ($253K/$510K) | DS~C | dispatched, no ack yet |

All briefs in `docs/architecture/_drafts/INFLEC_*_BRIEF.md` (or `docs/briefs/` for the 49F gap doc, moved by DS~D due to `.owned-paths.yaml` ANY_CTO restriction on `docs/architecture/**`).

---

## Portal FE ships

All on portal DEV branch. Author: `0.4.0_DE_ClientPlatform <0.4.0_DE_ClientPlatform@opal.agent>`.

| Commit | Subject | Files | Lines |
|---|---|---|---:|
| `fcf8b4ae` | `fix(INFAUACANON)`: drop 49F-era geo-as-canonical override; read firm AUA from views.aua.donut.total | DistributionTab.tsx + PartnerAnalytics.tsx | +58 / -27 |
| `e505b49b` | `fix(INFAUACANON)`: apply firmHeadlineAua canonical override to DistributionQuarterlyStrip current cell | DistributionTab.tsx | +17 / -1 |
| `bfe4abf6` | `fix(INFAUACANON)`: use transaction-tracked metrics.aua as canonical; surface silver cert in Assets Overview footnote | DistributionTab.tsx + PartnerAnalytics.tsx | +56 / -20 |
| `5a31973b` | `feat(FEEACCTS)`: reframe fee-paying / non-fee-paying cards from client grain to account grain (L0 + L1) | types.ts + ClientsTab.tsx + AdvisorBookView.tsx + ConsolidatedOverviewPanel.tsx | +56 / -27 |

Total: 4 commits, 187 insertions, 75 deletions across 7 files. Typecheck PASS on all. All pushed `origin/DEV`.

### INFAUACANON evolution (3 commits)

The radial-center/strip/tile AUA canonicality conversation evolved across three commits as Andrew walked the implications:

1. **`fcf8b4ae`** — switched `firmHeadlineAua` from `views.geo.metrics.aua` to `views.aua.current.donut.total` (canonical for both partners). Inflection radial $201M → $203M, Assets Overview tile fixed.

2. **`e505b49b`** — strip render in DistributionTab.tsx:3260 has its own `getAuaForPeriod('current')` that also needed the canonical override. Added `firmHeadlineAua` prop threading through DistributionQuarterlyStrip. Inflection strip current-cell $201M → $203M.

3. **`bfe4abf6`** — Andrew clarified: 49F's `views.aua.donut.total = $1.80B` is the silver-allocations `certified_aua` (D_01 PSCFIX cert override), while `views.aua.metrics.aua = $1.70B` is the transaction-tracked `gold_aua`. Andrew's directive: surface the transaction-tracked total ($1.70B), not the silver allocation. Reverted `firmHeadlineAua` to `metrics.aua`. Added a new gold-text disclosure footnote in the Assets Overview panel, above the "New Client Assets" line, that surfaces the cert value when it exceeds the transaction-tracked total:
   > "Total firm AUA is $1.80B. The Advisor Intelligence dashboard only tracks transaction-driven assets under advisory."

   Footnote suppressed automatically for Inflection (where the values are equal — no cert override emitted).

### FEEACCTS (1 commit) — clients → accounts grain shift

Andrew flagged "19 Non-Fee-Paying Clients" on 49F as misleading: clients can hold mixed fee/no-fee accounts (taxable brokerage + held-away IRA is the canonical example). Counting at client grain forced an arbitrary one-or-the-other call. Account grain is unambiguous.

- Added optional `fee_earning_account_count?` + `non_fee_earning_account_count?` to `ClientsTabHeadline` + `HeaderTotal` types
- L0 Books Tab Firm Overview cards relabeled "Fee-Paying Accounts" / "Non-Fee-Paying Accounts" / "Total Accounts"; read from new fields with em-dash fallback
- L1 AdvisorBookView Book Overview cards relabeled same way; reads `bookData.book.fee_earning_account_count` (already emitted per-advisor today by `_aggregate_billing_per_advisor` in D_02 / INF_D_02) — works immediately, no DS dependency
- ConsolidatedOverviewPanel METRIC_CARD_STYLE extended with color presets for the new labels

---

## DS coordination summary

### DS~C (Inflection lane)

Briefs shipped today by DS~C:
- `12cae4086` INFCTSLIMFIX — removed `'fee_earning_aua': 0.0` hardcode from `INF_D_00.portal_aggregates.py:311`
- `eea448321` INF firm-level account counts — extended `_derive_fee_earning_aggregates` + dual-source pattern in `build_clients_tab_slim`
- `fad5fd9a5` Brief #8 (geo/aua UNTAGGED segments) — in flight, chain #18 booted 16:47Z

Briefs awaiting DS~C ack:
- Brief #11 per-advisor mix_periods (`INF_D_04:3023` hardcoded `[]`)
- Brief #12 IWM leaderboard/book.json alignment (`INF_D_00c` rep_bucket vs advisor_key routing)

### DS~D (49F BD lane)

Brief #9 shipped in two parts:
- Part B (`8bb342de4`) — firm-level account counts at `clients-tab-slim.json#headline` + `gold/artifacts/summary/header_metrics.json#total`. Modified `D_00.portal_aggregates.py` + `D_04.client_portal_summary.py`. Carried 22 ruff-violation cleanups on D_00 in same commit (gate-driven, behavior-preserving).
- Part A (`b0d650be7`) — $92M cert/gold gap investigation doc at `docs/briefs/data-scientist-49F-cert-gold-92m-gap-investigation.md` (path moved from architecture/_drafts/ due to .owned-paths.yaml restriction).

### AE 0.7 (Cloud Ops)

- Brief #6 Issue 3 INFADVTSSCHEMA Lambda fix shipped `249bfcf47` + Terraform apply 0-diff + `inf-portal-publisher` invoked 16:10Z. All 4 Inflection advisor `timeseries.json` artifacts now emit FE-compatible schema (`advisor_id`, `advisor_name`, `data`, `nna`, canonical cumulative fields).
- bd-gold-trigger fired 17:31Z for 49F Part B regen, runner launched 17:39Z, D-section ETA ~17:54Z.

---

## $92M gap investigation — key empirical findings

DS~D's Part A doc (`docs/briefs/data-scientist-49F-cert-gold-92m-gap-investigation.md`) **partially refuted** Andrew's "$92M of accounts with no transaction history" hypothesis. Six-cohort breakdown:

| Cohort | Accts | AUA | % of gap |
|---|---:|---:|---:|
| Recently-onboarded (2025-Q4 → 2026-Q2), gold normalization lag | 174 | $65.6M | 67.5% |
| Per-account AUA computation drift + 18 gold-only accounts | n/a | $21.1M | 21.7% |
| Older accts dropped at normalization | 202 | $4.5M | 4.6% |
| Truly no transaction history (Andrew's literal cohort) | 12 | $4.3M | 4.5% |
| Zero-balance shells (correctly dropped) | 165 | $0 | 0% |
| Documented liability exclusions | 31 | -$4.8M | n/a |

Dominant mechanism is **new-account onboarding lag** between BD allocation snapshot (fast) and gold positions_cube + FIFO cost-basis pipeline.

DS~D's §5a investigation went deeper and located the proximate cause: **Schwab RPS feed is dark since 2026-04-20**. `B_00.SCHWAB_RPS_PREFIX = 'schwab/silver/rps/'` against `opal-data-bd` — last partition `date=20260420/`, mtime 2026-04-22. The live Schwab feed lives in a different bucket (`s3://opal-data-schwab/silver/RPS/`) with current data uploaded daily. B_00 reads the stale mirror → forward-fills every day from 2026-04-20's reconciled canonical. BFIX2/BFIX3 rescue paths only run on the Schwab-reconciled branch, not on forward-fill → new accounts during the dark window cannot enter canonical_holdings.

Operationally separate from the cert disclosure conversation: **49F's portal is currently operating on forward-filled 2026-04-20 data with daily re-pricing**, not actually-current canonical holdings. Worth surfacing to AE 0.7 as a separate incident regardless of the disclosure footnote outcome. Andrew aware; no immediate action yet.

Andrew's directive stands: track only what we actually have transaction history for. Disclosure footnote (commit `bfe4abf6`) is the correct mitigation. No compute changes to gold.

---

## Key memory updates

Andrew confirmed several non-obvious decisions worth persisting:

1. **"Use total AUA as a function of what we actually have tracked, don't use silver allocations"** — definitive policy on the cert/gold reconciliation. $1.70B (gold transaction-tracked) is the canonical for 49F display; $1.80B (silver/allocations cert) is surfaced as a contextual footnote, not the headline number. Encoded in `bfe4abf6` commit body + FE comment block at `DistributionTab.tsx:2996+`.

2. **"Reframe clients → accounts for the fee paying containers at firm overview AND book overview"** — both L0 and L1 surfaces. A client can hold a mix of fee-paying and no-fee accounts; counting at client grain is ambiguous. Account grain is unambiguous. Encoded in `5a31973b` commit body.

3. **DS~C is the source of truth on the Inflection mix routing**. The `inflection_wealth_management` advisor_key catchall (book.json $510K) is canonical; `rep_bucket='firm'` (leaderboard $253K) is stale legacy routing. Confirms project memory `project_inflection_iwm_catchall_bucket.md` and resolves the "minor anomaly" DS~C flagged on chain #17 acceptance smoke.

No new memory files written this session — existing memories at `memory/feedback_*` + `memory/project_*` continue to apply.

---

## Next session

Pending DE work carried over:
- [DE next session] **Layout flag commit for Inflection AdvisorPublicProfile** (Brief #6 Issue 1): flip `advisorPublicProfile.enabled: true`, add `roleComposition.enabled: false`, gate the RoleDonut render. Wait until AE 0.7 INFADVTSSCHEMA artifact lands have been validated end-to-end first.
- [DE next session] **Granularity-switch in PartnerAnalytics** (Brief #5 follow-up): wire the `Interval: Month/Quarter/Year` toggle to pick `.months` / `.years` / `.quarters` arrays from `timeseries_chart.json` (DS shipped these in INFLIFECYCLE `8fa237b73`, but `PartnerAnalytics.tsx:240` still hardcodes `.quarters`).
- [DE next session] Smoke after 49F + Inflection chain regens land. Verify L0 fee-status account counts transition em-dash → real numbers automatically.
- [DE next session] Briefs #13+ — Andrew will continue walking the Inflection portal panel-by-panel.

Pending DS~C work:
- Brief #8 in flight (chain #18 / fad5fd9a5)
- Brief #11 + #12 dispatched, awaiting ack

Pending DS~D work:
- Brief #9 Part B regen awaiting bd-gold-trigger D-section completion (~17:54Z ETA at log-write time)
- Optional follow-ups from §6 of gap investigation doc: Penfield 2025-Q1 stranded cluster, 18 gold-only accounts. Non-blocking.

Pending AE 0.7 work:
- bd-gold-trigger regen verification (Part B account counts surface on next portal refresh)
- Possible separate incident on Schwab RPS feed dark window (B_00 SCHWAB_RPS_PREFIX points at stale mirror)

---

## RAVC log

| Timestamp (Z) | From | To | Subject |
|---|---|---|---|
| 17:12 | DE | DS~D | Brief #9 (49F gap + account counts) |
| 17:13 | DE | DS~C | Brief #10 (Inflection account counts) |
| 17:23 | DS~D | DE | RAVC2 ACK Brief #9 — Part B first |
| 17:31 | DS~D | DE | RAVC4 Brief #9 Part B SHIPPED `8bb342de4` |
| 17:44 | DS~C | DE | RAVC Brief #10 SHIPPED `eea448321` |
| 17:48 | DS~D | DE | RAVC4 Brief #9 Part A SHIPPED `b0d650be7` |
| 18:02 | DE | DS~D | ACK Brief #9 Part B + Part A |
| 18:03 | DE | DS~C | ACK Brief #10 + Brief #11 dispatch heads-up |
| 18:02 | DE | DS~C | Brief #11 (per-advisor mix_periods) dispatched |
| 18:47 | DE | DS~C | Brief #12 (IWM leaderboard/book.json) dispatched |

---

## State as of log close

- Portal DEV: 4 commits ahead of pre-session HEAD, all pushed
- DS~C lane: 3 commits shipped + 2 briefs awaiting ack
- DS~D lane: 2 commits shipped, awaiting chain regen verification
- AE 0.7 lane: Lambda fix shipped + Terraform applied + invocation done
- Andrew: aware of the Schwab RPS dark-feed finding, has chosen not to action it this session; aware of the $92M gap investigation outcome; signed off on the FE evolution path (canonical = transaction-tracked, cert as footnote)

**End of log.** Watcher running. Standing by for chain regens + DS~C acks + Brief #13+ from Andrew.
