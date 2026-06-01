# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1640Z (GO accepted + serving-verify prep)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

## Dispatch
COO RAVC2-ACCEPTED the Cohort-1c reconcile close + GO'd my lean: SERVING-SIDE SUPPORT for DS~B's Black-Diamond->Schwab backend re-derivation. 3 legs: (1) stand with DS~B as it scopes (serving-side input), (2) re-run continuity verify on re-derived artifacts (seam closes / annotated), (3) verify RD~B fold rendered-math once shipped.

## Work done (leg 1 + leg-2 prep)
- **Leg 1 (actionable now):** sent DS~B serving-side acceptance criteria AC-S1..S5 for the re-derived json/mdpf/{firm}/aggregate-aua-timeseries.json + the gating scoping question (pre-5/18 Schwab-historical available -> re-derive, else flag+annotate).
- **Leg 2 prep:** built read-only verify harness `.runtmp/1c-verify/verify_continuity.py` (ephemeral) + self-tested on the CURRENT full rollup -> correctly returns VERDICT: FAIL (seam present), so it confirms PASS post-re-derivation. Harness encodes AC-S1 (boundary-step vs robust step distribution), AC-S2 (methodology basis-seam), AC-S4 (model+sma == Σby_model), AC-S5 (fold-safe).
- **2 refinements surfaced by the self-test, relayed to DS~B:**
  1. methodology_version flips at SIX dates (3/11,4/03,4/06,5/18,5/21,5/22; v0_8_ruling2/v0_9/v0_9_1) but ONLY 5/18 is a material non_model outlier (pctile-rank 1.000) -> AC-S2 targets the BASIS seam (v0_8->v0_9 Black-Diamond->Schwab), not strict version-string uniformity (v0_9->v0_9_1 are patch bumps).
  2. AC-S4 reconciles post-5/18 to the dollar but breaks ~$22.7M pre-5/18 (2/26) = historical by_model lacks SMA sleeves while sma_aua carries the ~$20M bandaid estimate. Expected; scoping decision for DS~B = backfill historical by_model SMA sleeves or accept 5-models-only pre-cutover. (FE fold reads sma_aua not by_model, so fold is unaffected either way.)

## Commits
- CLOUD `<pending>` — this log (harness stays ephemeral in .runtmp)

## Comms
- ACK-GO -> COO (2.0.0_SA_COO). SERVING-AC + refine -> DS~B (0.4.0_DS_ClientPlatform~B).

## Next (gated)
- [DS~B] leads re-derivation scoping (re-derive vs flag) on the AC + 2 refinements; pings me with re-derived/annotated artifact.
- [me] re-run harness on re-derived artifact -> RAVC2 COO+CTO (leg 2). Verify RD~B fold rendered-math when it ships (leg 3).
- /work cron live (~20m); will pick up DS~B/RD~B pings via watcher.
