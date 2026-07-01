# MDPF WS-E swap — handoff spec for DS~A (0.4.0~A, the WS-E author)

**From:** 0.5.0_AE_OpalETL | **To:** 0.4.0_DS_ClientPlatform~A (authored `build_mdpf_wse_49f_non_model_aua.py`) | **Design:** `mdpf-49f-custody-schwab-native-basis-switch-design-20260701.md` (CTO-arch-gated) | **Trigger side (DONE):** `mdpf-trigger-repoint-schwab-rps-freshness-spec-20260701.md` + deployed `mdpf-pipeline-v1.3.0` (dormant).

## Context (you have the full MDPF picture — this is just the swap deltas)
Andrew ruled the 49F custody basis to **Schwab-native, straight RPS, assets-only (eschew cash), re-baseline**. My trigger leg is deployed DORMANT: the `mdpf-daily-trigger` reads the shared flag `/mdpf/custody_source` (SSM, currently `bd`) ONCE per fire, gates on it, and **STAMPS the resolved value into the dispatch env** (`export CUSTODY_SOURCE=<bd|schwab>`). Your WS-E swap keys off that SAME value — one-read-propagated, so a single flip moves the gate + your compute atomically.

## The swap (`build_mdpf_wse_49f_non_model_aua.py`) — 4 deltas

1. **`compute_partner_custody_total` — add a `schwab` branch (gate on CUSTODY_SOURCE):**
   - `schwab`: **straight sum of RPS asset Market Value** from `schwab/silver/rps` (latest `date=YYYYMMDD/` partition) — **assets-only (exclude cash), Schwab-scoped-BY-CONSTRUCTION** (RPS is Schwab-native → **NO `bd/silver/fees` crosswalk, NO `bd/silver/allocations` read, NO gold/aua_certification cross-check needed** — the fees crosswalk existed only to restrict the mixed BD basis to Schwab; RPS is already all-Schwab). This is the freeze fix at the root (fees was the frozen input).
   - `bd` (default): CURRENT behavior unchanged (allocations + fees crosswalk).

2. **CUSTODY_SOURCE resolution:** read from the RUN ENV (`os.environ.get("CUSTODY_SOURCE","bd")`) — the trigger dispatch stamps it; do NOT do an independent SSM read on the dispatch path. **Ad-hoc/off-dispatch fallback:** if the env is absent (a manual run not via the trigger), read the SSM param `/mdpf/custody_source` directly (same source of truth).

3. **COHERENCE FIX (the latent bug — do this WITH the swap):** in `build_non_model_aua`, when `schwab`, scope the model + SMA legs to **custodian == Schwab** before the residual. `wsb_49f_smartx_model_aua.py` `model_aua_positions` HAS a `custodian` column (~line 74). So `non_model = RPS_custody(Schwab) − model(Schwab) − sma(Schwab)` — all three Schwab-scoped → coherent. Without this, you'd subtract all-custodian model/sma from a Schwab-only custody → an understated/negative residual (the incoherence I flagged in the design).

4. **Assets-only / liabilities:** per Andrew "eschew the cash, keep it to assets, straight RPS" — sum RPS asset positions' Market Value; exclude cash rows (you know the RPS SecurityType/cash convention). Keep the existing `LIABILITY_TYPES` handling consistent with assets-only.

## Deploy posture
Deploy your swap **DORMANT behind CUSTODY_SOURCE** (default `bd` = current behavior, zero change) — matches my trigger. The cutover is then a SINGLE flag flip, never a code-race. Test both branches (bd = unchanged; schwab = straight-RPS-sum + coherent residual) before the co-activation.

## Co-activation sequencing (confirmed w/ COO)
1. [DONE] Trigger dormant-deployed (`mdpf-pipeline-v1.3.0`; `/mdpf/custody_source=bd`; gate reads flag + stamps dispatch).
2. [YOU] WS-E swap dormant-deployed (schwab branch + model/sma Schwab-scope, gated on CUSTODY_SOURCE, `bd` default).
3. [ME] leg-2 Q1 Schwab-native sanity gate (partition/schema + position-count ~91,200 + account-count ~5,890 + DoD-move band) — wired before the flip.
4. [FLIP = the co-activation window, CTO never-widen + CVO co-sign]: `aws ssm put-parameter /mdpf/custody_source=schwab` — ONE atomic flip moves both. Ledger opens AT the flip.
5. [CVO] parity-verify the FIRST post-flip nightly: dispatches on RPS-fresh AND serves straight-RPS-sum; the served basis-step documented (Andrew ruled the re-baseline) + coherent (non_model not negative); MDPF un-freezes (clears the frozen aggregate-aua-timeseries + the non_model_assets DE surface).
6. [ROLLBACK] any fail → `put-parameter /mdpf/custody_source=bd` (both revert atomically) + WS-E revert if needed — never half-land.

RAVC me + COO at WS-E-swap-dormant-deployed; then COO calls the co-activation window. Ping me on any delta question — I own the trigger + flag + sanity-gate side.

*Author: 0.5.0_AE_OpalETL, 2026-07-01.*
