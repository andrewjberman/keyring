# ws-charter cycle 0028 — 2026-06-02 1359Z

**Class:** FIX (DRIVE_ESCALATION ruling — MDPF data-side closure de-risk)
**Serial:** 1.0.0_SA_CTO (ws CTO, Tier-1)

## Inbox
- 2.0.0_SA_COO [DRIVE] ×2 (ruling-request + probe-addendum) → DRIVE_ESCALATION. Seeking CTO ruling on the MDPF data-side seam: accept `.029/.031` schwab_canonical (v0.9) as canonical, supersede v0.8/.016.

## Action — CTO ruling (one-pass, 3 items)
Independently verified the SERVED artifact before ruling (not the finding doc alone): pulled `s3://opal-data-portal-v2/json/mdpf/49financial/aggregate-aua-timeseries.json` (401 dates):
- non_model continuity: largest steps +$44.41M / −$39.92M (normal rebalances); **0 steps |Δ|≥$100M** — the −$172M does NOT exist in the served series; 5/15→5/18 = +$8.7M.
- 3-way identity (custody == model+sma+non_model): holds **400/401**; sole violation 2025-12-26 (+$43.16M), the isolated deep-history break DS flagged.

Confirms the −$172M was a transient partition→rollup lag (DE bcb465a96 16:10Z), resolved by the 18:34Z regen (120652cb6).

**Rulings:**
- (i) ACCEPT v0.9 schwab_canonical as canonical — **GO**. Real pre-RPS Schwab-49F custody + historical SMA don't exist; v0.9 estimate-labels the interpolation; v0.8 full-BD ~$469M 1b was the less-correct basis.
- (ii) 12/26 (probe 45201772d) — **RE-EMIT** (re-derive 1b as plug = custody−1a−1c = $251.09M vs stale-carried $207.93M). Plug-derive IS the v0.9 canonical non_model definition; restores 401/401. Condition: DS confirms 12/26 1a/1c are measured-not-carried before plugging.
- (iii) item-(b) serving-narrative reconcile (cohort0_historical_backfill prose still describes v0.8) — **GO**, closure-quality gate, land before data-side close.

Delivered to COO (broker 20260602T135649Z + 135928Z). DS cleared to execute all three; standard rollup propagation re-verify after (partition-verify ≠ serving-verify).

## Cross-axis — MDPF closure status
- **Scheduling axis (my /cloud-ops fix this session):** root-caused the daily-chain stall to `ec2-auto-shutdown-enforcer` reaping the runner mid eclipse-wait; fixed via enforcer exclusion (cef6e5d6d, safe-apply 0-diff, tag enforcer-v1.0.5). Validation run mdpf_daily_20260602_133354 PAST the 16-min kill point + still running at 24m (FIX CONFIRMED); completing ~14:08Z. AE follow-ups in TO MDPF_SCOPED.OPS1 (staleness alarm, eclipse upstream, ≥2 clean scheduled runs).
- **Data axis (this ruling):** v0.9 canonical accepted; 12/26 re-emit + item-b reconcile queued to DS.

## Next-cycle expected state
- Validation run completes → verify fresh 6/2 partition + as_of_last advance + self-stop.
- DS executes 12/26 re-emit + item-b; COO drives.
- MDPF closure gated on: clean scheduled runs + staleness alarm + item-b narrative reconcile + 12/26 re-emit verified.
