# 0.4.0_DE_ClientPlatform — Session Log 2026-06-05 (~1620Z–1850Z)

**Role:** Tier-2 DE, MDLP_DISTFIX Phase-0 LEAD investigator (Andrew-named) + downstream consumer-owner / served-verify.
**Outcome:** All 3 distribution data-integrity root-causes confirmed vs LIVE served artifacts; 2 PRD-hypothesis corrections accepted (PRD v0.1→v0.2→v0.3); I1+I2 collapsed to one MDPF re-source workstream that AE shipped same session; data-layer smoke PASS; supplied the contract + reconciliation answers that kept two wrong numbers off Andrew's screen.

---

## Startup
- /watcher: re-registered (was STALE), armed persistent inbox Monitor, /work 20m cron armed (later cancelled per LD-0157).
- Read PRD `docs/architecture/MDLP_DISTFIX_PRD.md` (54a980467).

## Phase 0 — Investigation (investigation-only, no fix)
Confirmed every conclusion against the ACTUAL served S3 artifact (body + LastModified), not proxies.

- **I1 CONFIRMED exactly:** Global `account-distribution.json` == 49F per-firm BYTE-IDENTICAL (6,838 / $1,379,701,688.62 / all percentiles / min). Inflection separate (400/$96.6M). `compute_account_distribution.py` computes ONE distribution over the whole SmartX parquet — no partner dimension; Inflection (orion) never folded into "Global". Fork: aggregate vs relabel.
- **I2 CONFIRMED but REFRAMED (PRD hypothesis falsified):** not a print bug, not just funded-period fallback. The smartx-exporter EC2 (i-06ebcb27395eb3f49) is STOPPED and the EventBridge `smartx-daily-export-trigger` is DISABLED → aum-metrics + all 3 account-distribution artifacts genuinely 4d stale (LastModified Jun 1). aum-timeseries fresh via separate path → why the area chart updates daily but distribution/metrics don't. PRD's "generated_at regenerates daily" falsified by served.
- **I3 CONFIRMED + producer CORRECTED:** not INF_D_07a/D_01 (PRD guess) — it's `INF_D_04.client_portal_summary._build_geo_view` ("Account Sizes By State"), which computes percentiles as RAW `aua_series.quantile()` (no `vals>0`, no $1K floor; served min=$0.00) while `_compute_histogram_block` floors $1K. The geo percentiles BYPASS `_calc_distribution_stats_adv`, so the shared >=$1K helper must refactor `_build_geo_view` too (spanning bd D_01 + bd D_04 + orion INF_D_04).
- Brief committed `a015fe84a` (`docs/briefs/mdlp-distfix-phase0-investigation-findings-20260605.md`); RAVC2 to COO + CTO. CTO accepted → PRD v0.2 (ee52d92cc), both corrections folded.

## I2 re-investigation (Andrew challenge — self-correction)
Andrew challenged: radial == fresh area chart → raw SmartX flows, break is distribution-specific. He was right.
- Traced both paths. Per-account AUA IS fresh daily via the NEW MDPF path: `opal-data-mdpf/mdpf/feeds/model_aua_positions/{firm}/{date}.parquet` (account grain, today's partition). `compute_account_distribution.py` was the last consumer on the dead EC2 parquet.
- Fix = RE-POINT (zero EC2, zero cost), strictly better than re-enable. Also dissolves I1: the feed is partner-dimensioned (49financial=smartx + inflection=eclipse) → true Global = per-account union.
- RAVC2 → CTO accepted → PRD v0.3 (a4e2bdd2a). I1+I2 → one re-source workstream; smartx-exporter EC2 = cost-audit-R5 decommission candidate. Facts held, fix-framing corrected.

## Downstream support (consumer-owner)
- **Re-source contract to DS:** answered 6 questions (schema/grain account_id×model_key, per-acct=sum(model_value) model-only for PARITY [served≈model-only: 6,884/$1.377B vs served 6,838/$1.380B], no period/status replication, by_model native per-firm + Global union, partner-set={49F,INF}, FE shape unchanged). Surfaced 3 decisions (SMA inclusion, Global by_model taxonomy, Global partner-scope).
- **INF consumer-confirm (Option A):** proved MDPF-INF feed == served eclipse-gold BYTE-IDENTICAL at matched as-of (05-29: 400/$96.6M/identical percentiles). The 400→450/$96.6M→$115M is pure freshness drift, NOT scope divergence. No eclipse-must-stay reason. Flagged expect-a-visible-catch-up for Andrew awareness.

## Re-source SHIPPED (AE) — served-verify + smoke (close gate)
- **DATA SMOKE PASS:** Global 7,301 / $1,491,982,925.05 (true union, dust-floored min $1,037, p10 $7,988, by_model 5+2 INF blends). 49F 6,852/$1.377B. INF 449/$115.1M/min $1,151/p10 $18,381 (was $8.42 dust). Reconciles EXACT: 6,852+449=7,301; $1,376,858,220+$115,124,705=$1,491,982,925 to the cent. All PRD §6 data checks satisfied.
- **VISUAL SMOKE blocked on JWT:** Node+Edge Playwright launches fine (LD-0144); app reachable; `window.__devBypass()` seeds shell; BUT all portal data fetches are Lambda@Edge-auth-gated at CloudFront (`/api/general/...` 401 "LambdaGeneratedResponse") because dev-bypass-token isn't a real JWT → 401→logout→bounce to /login. Known limitation. Recommended Andrew's direct eyeball (he offered + specified). Reported to COO+CTO.

## I2 residual (Andrew/CTO caught) — aum-metrics
- Confirmed Global AUM-by-Model donut + Total-AUM cards read stale `aum-metrics.json` (Jun 1) — $ stale ~1-2% AND still I1-pinned-to-49F (7,039/~$1.4B vs fresh true-Global 7,301/$1.492B) AND `total_aum`=$0 bug. DS aum-metrics re-source must fix $ values + true-Global aggregation, not just timestamp.
- **DS reconciliation Q answered:** Total-AUM card = `opal_aggregate_aua` $1,807,839,716.27 (read pre-computed from `json/mdpf/global/aggregate-aua-timeseries.json`). DS's $1.899B = `partner_aua_subtotal` which double-counts `cohort_2b_audit` $90,875,859.89 (the ~$91M gap; identity_1 PASS). Don't re-derive the subtraction; read the canonical field. Kept a +$91M-wrong Total-AUM off Andrew's screen. Model donut $1.492B locked.

## Open / next
- DS authoring aum-metrics GLOBAL re-source (onto MDPF aggregate). I co-own the served-verify: donut-center == $1.808B, model slices == bell-curve $1.492B, when it ships.
- Andrew product call outstanding: "Global" labeling (true all-partner aggregate — now cheap — vs SmartX/model-book relabel).
- Visual pixel-confirm of the corrected bell curve needs a real authenticated session (Andrew eyeball or real-token smoke).

## Governance / fabric
- LD-0157: cancelled /work 20m cron (75048b98); now event-driven via inbox Monitor + COO /drive. Broker status leads with WORKING:/IDLE: token.
- Inbox Monitor self-healed once (exit-143 → re-armed bchvgg661).
- Memory banked: `feedback_stale_artifact_check_for_newer_parallel_path_before_revive` (stale artifact ≠ stale data — check for a newer parallel path before reviving infra).

## Commits this session
- `a015fe84a` — Phase-0 investigation findings brief.
- (This log.)
