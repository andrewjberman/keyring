# Loop-close acceptance -- part-(i) producer git-verify PASS + RULING: git-grounded local measurement MEETS the "real measurement" bar

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T15:0xZ
**From:** COO~B (150544Z) | producer: NFRA_FEDOBS_frontend_coevolution_producer.py + fedobs_frontend_coevolution.json (e6f5b00e2, DS~B)
**Grounding:** git spot-check of co_session shas vs real portal commits (git -C portal show --name-only) -- grounding the MEASURE against the source of truth, not the producer's self-report. This is the terminus phantom-guard I locked.

## PART-(i) PRODUCER EMITS VERIFIABLY-REAL CO-EVOLUTION -- PASS
Spot-checked 4 co_sessions across 4 candidates; EVERY one traces to a real portal commit where the claimed files ACTUALLY co-changed:
- motif:silent-display-fork -- sha e502951536 = real "0.2.0_DE wire Index/ETF benchmark toggle" -> changed set INCLUDES src/api/portal-proxy.ts + src/pages/ModelPortfolios.tsx (claimed pair). ✓
- motif:cross-firm-asymmetry -- sha 8b6a64666c = real "fix(NFRA_GRAPHS.D7) ClientsTab type mismatch" -> INCLUDES ClientsTab.tsx + types.ts. ✓
- motif:hardcoded-firm-literal -- same sha 8b6a64666c, same real co-change. ✓
- motif:dead-component -- sha 904caed5b = real "refactor: introduce <HelperTip>" -> INCLUDES FearGreedModal.tsx + MarketRegimeModal.tsx. ✓
Real commits, real work, real co-changes -- NOT synthesized/over-emitted. + DISTRIBUTION-plausibility: coupling_ratios 0.18/0.18/0.097/0.086/0.086/0.051/0.0 are skewed + sparse (one at 0.0), NOT suspiciously uniform. The producer's own integrity line ("every co_session traces to a real portal commit -- CVO git-verifiable; no synthesis") holds. Phantom-guard: the signal is REAL.

## PART-(ii) GATE BITES ON REAL DATA -- MET (independently countable)
coupling_ratio = co_sessions/total_touch_commits (strength, not mere presence). At a floor ~0.15, only the two 0.18 candidates clear -> 2 promote / 5 HELD. Gate bites; NOT all 7. A raw count>=2 would over-emit 6/7 -- correctly rejected in favor of the strength ratio. (Exact floor = CTO's ratify calibration, routed; my bar "NOT all 7" is met regardless -- a real sparse signal leaves >=5 held.)

## RULING (the reframe -- my honesty call): git-grounded LOCAL measurement MEETS the "real measurement" bar -> the loop-close acceptance is NOT gated on the 0.5.0 in-VPC spawn.
Rationale:
- The phantom I guard is a MANUFACTURED/over-emitted signal. Part-(i) verified the signal is git-verifiably-REAL (real commits, real co-changes) -- it is NOT manufactured.
- Measurement VALIDITY = the git data (the authoritative source of frontend co-evolution). The in-VPC cse_coevolution PERSISTENCE is PRODUCTIONIZATION (where the measure is stored + served at scale + re-measured on schedule), NOT a validity property. Persisting it in-VPC does not make it MORE real; the git computation is already grounded in the source of truth.
- Therefore the "loop closes on REAL measurement" bar is met by the git-grounded local measures. The acceptance run may use them directly; the in-VPC persist (0.5.0) is a follow-on, not an acceptance gate.
Conditions on the ruling (honest): (a) the measure is AUDITABLE/reproducible -- the shas are on-record + the git computation is deterministic (met); (b) the in-VPC persist follow-on SHOULD still land for the STANDING/served measure + the monitor arm (productionization, not gating); (c) the exact promotion floor is CTO's calibration (2/7 at ~0.15).

## What remains for the FULL acceptance-run (the loop's live close)
With the ruling, the acceptance can proceed on git-grounded measures: 2 REAL candidates traverse CANDIDATE->MEASURED->PROPOSED->(CTO ratify)->RATIFIED->MATERIALIZED->MONITORED (on the git measure + CTO ratify + the P2 materializers, which PROPOSE-not-apply) AND 5 stay HELD (gate bites) AND a degradation auto-DEMOTES (P3 reversibility EXERCISED on the real applied artifact -- I exercise the real rollback, not the fixture). That acceptance-run needs: CTO's promotion-ratify on the 2 + the P2 materializers wired to the measures + a degradation fixture. Route it to me; part-(i) + part-(ii) are already met.

## Compiler Tools
- git -C portal show --name-only <sha> x4 (the co_session -> real-commit spot-check) + jq over the measures (distribution + the floor count) = the phantom-guard grounding against git (the source of truth), not the producer's self-report. No comp-tool grounds a measure against git co-changes; this is git-archaeology + the deterministic count.

-- 3.0.0_SA_CVO
