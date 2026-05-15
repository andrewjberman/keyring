# Session — INFGRO.005 AC verification: GRO fields live, but return-% upstream defect found

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-15
**TO:** ADVI_INFGRO.005 (GRO side-by-side) — AC verification pass
**Outcome:** HOLD close recommended. Portal code verified correct; upstream gold defect blocks a clean close.

---

## Sequence

1. Session start — both INFGRO portal TOs gated on chain #30 (never fired).
2. AE 0.6.1 ran `--chain incremental` (Eclipse-decouple validation), completed 16:46Z — D-chain
   re-runs INF_D_00c.portal_leaderboard.py.
3. DS~A empirically confirmed C-tier GRO artifacts already materialized on S3
   (client_performance.parquet, 05-15 03:03 local, GRO decomposition cols present).
4. COO ACCEPTED the incremental-produced leaderboard.json as the INFGRO.005 AC1/AC7 gate,
   with the named gate: "pull leaderboard.json, CONFIRM firm-level GRO fields present."
5. Pulled `s3://opal-data-inf/platinum/firm/leaderboard.json` (LastModified 16:44:53Z,
   generated_at 2026-05-15T16:44:52Z). Verified beyond field-presence into AC1 "values match".

## Named gate — PASS (mechanically)

leaderboard.json carries every GRO field:
- Firm-level (QTD/YTD/MAX `.windows.*.summary`): `firm_nna_$`, `firm_return_pct_twr`,
  `firm_return_$`, `firm_epsilon_$`.
- Per-advisor (`.windows.*.entries[]`): `advisor_nna_$`, `advisor_return_pct_twr`,
  `advisor_return_$`, `advisor_epsilon_$`.

Portal Phase 2 code (`d4e28cca`) verified CORRECT:
- `AdvisorsTab.tsx` `GroHeroCards` L818-867 reads `summary?.['firm_nna_$']` /
  `['firm_return_$']` / `['firm_epsilon_$']` / `.firm_return_pct_twr` — exact key match.
- Per-advisor L387-390 / L434-437 / L1169-1281 read the `advisor_*` quartet — exact match.
- Unit handling correct: INF_D_00c emits `firm_return_pct_twr` already `×100` (percent-points,
  L702); portal renders `returnPct.toFixed(2) + '%'` — no double-conversion bug.
- AC5 PASS — `tsc -b --noEmit` clean.
- AC6 PASS — `comp-cache collisions`: `firm-leaderboard` key has 3 consumers (index,
  AdvisorsTab L252, ClientsTab) all typed `PlatinumLeaderboardResponse` — no new
  different-type collision. Same 4-key baseline as SHARED.006.

## The defect — `firm_return_pct_twr` / `advisor_return_pct_twr` are not a window TWR

AC1 is "hero card values MATCH leaderboard.json firm-level fields." The portal matches them
faithfully — but the leaderboard.json return-% values are themselves wrong:

| Window | firm_return_pct_twr | firm_return_$ | firm_epsilon_$ | firm_nna_$ |
|--------|--------------------:|--------------:|---------------:|-----------:|
| QTD | 0.038578 % | 3,250,211.72 | 12,326,710.66 | 1,361,547.46 |
| YTD | 0.009034 % | 2,206,325.18 | 16,496,354.51 | 4,327,984.81 |
| MAX | 0.004273 % | 10,139,171.81 | 61,667,076.03 | 136,281,616.16 |

Three independent tells:

1. **Inverted monotonicity.** `firm_return_pct_twr` QTD > YTD > MAX. A cumulative window TWR
   must grow with window length; this strictly decreases. MAX (inception-to-date) returning
   0.004% is impossible.
2. **Inconsistent with its own `return_$`.** MAX `firm_return_$` = $10.14M (largest — behaves
   like a correct cumulative sum) while MAX `firm_return_pct_twr` = 0.004% (smallest).
3. **Per-advisor return-% uncorrelated with book performance.** `advisor_return_pct_twr` for
   the 4 advisors = 0.036 / 0.059 / 0.039 / 0.055 (all ~0.04-0.06%), while the same payload's
   `performance.avg_twr_pct` = 13.71 / 0.70 / 14.31 / null. No correlation.

**Candidate root (gold-side):** `INF_D_00c.portal_leaderboard.py` `_aggregate_gro_firm_window`
L692-702 (and `_aggregate_gro_per_advisor_window` L657-671) compute
`weighted_twr = Σ(total_aua × return_pct_twr) / Σ(total_aua)` over ALL in-window rows, then
`×100`. If `return_pct_twr` is at daily / per-snapshot grain, this yields an AUA-weighted
MEAN daily return — which dilutes over longer windows instead of compounding. That matches
all three tells, and explains the epsilon-dominance (return component % ≈ 0 → the
NNA+return+ε decomposition leaks the AUA-growth residual into ε: ε = 73% QTD / 72% YTD).

This is an upstream gold-tier defect, NOT a portal bug. Routed to COO for dispatch to the
INFGRO gold owner (DS~C/base built INF_C_02 + INF_D_00c; CTO owns INFGRO architecture).

## Acceptance criteria status

| AC | Status |
|----|--------|
| AC1 | Portal renders leaderboard.json values faithfully — PASS on the rendering contract. BLOCKED on a clean close: the upstream `*_return_pct_twr` values are wrong (see defect). |
| AC2 | Per-advisor AUA/Return/NNA/epsilon columns wired — code verified PASS |
| AC3 | Epsilon quality indicator — code shipped (FE-derived); visual pending |
| AC4 | Pre-existing columns unchanged — visual pending |
| AC5 | TypeScript PASS — verified |
| AC6 | comp-cache no new different-type collision — verified PASS |
| AC7 | Screenshot — pending (visual pass; needs authenticated browser session) |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-cache collisions` | 4 shared keys, all same-type — no new different-type collision. AC6 PASS. |
| `comp-routes trace getFirmLeaderboard` | Confirmed S3 path `platinum/firm/leaderboard.json`, firm-routed to `opal-data-inf` for Inflection. |

## Current State

| Item | Status |
|------|--------|
| Inbox | Acted on all (COO ACCEPT + chain-#30-owner update) |
| INFGRO.005 | TO stays `pending` — HOLD close recommended to COO; gated on upstream return-% fix |
| INFGRO.006 | pending, dispatch-held |
| leaderboard.json evidence | `.runtmp/inf_leaderboard.json` (generated_at 16:44:52Z) |
| Watcher | LIVE |

## Next Steps

- [COO] Route the `*_return_pct_twr` window-aggregation defect to the INFGRO gold owner
  (DS~C/base + CTO). HOLD INFGRO.005 close until corrected.
- [DS~C/base + CTO] Diagnose INF_D_00c return-% aggregation — likely needs window-cumulative
  TWR (geometric link of daily factors) rather than an AUA-weighted mean of per-row return_pct_twr.
- [DE post-fix] On corrected leaderboard.json: re-pull, confirm plausible window TWRs
  (QTD < YTD < MAX, correlated with avg_twr_pct), run /frontend-dev for AC4/AC7, RAVC2 to close.
