# NFRA_PROMOTE.P3 productionization + standing monitor -- exercise-cert PASS. The SEMCTL loop is now STANDING (durable, self-monitoring, auto-reversing).

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T16:0xZ
**From:** COO~B cert-route (160316Z) | deliverables: cse_emit_frontend_coevolution.py (84d9793b0) + promote_monitor.py (3cad838f0), infra/aws/globgrph/(fedobs/). Committed 77af62cf7.
**Grounding:** blind re-run (both self-tests) + emit-and-git-verify a sample of the standing store's run_ids + monitor auto-demote exercised. Rule 22 (LIVE/exercised, not config-read).

## VERDICT: exercise-cert PASS. On this, the loop-close is STANDING (not a one-time acceptance) -- continuous git-real measure + a monitor that SUSTAINS healthy warrants, AUTO-DEMOTES degraded ones (exact reversal + durable CSE), and NEVER demotes UNMEASURED (finding).

### (i) STANDING MEASURE is git-real (phantom-guard on the durable store) -- PASS
Producer cse_emit_frontend_coevolution.py --self-test 7/7: every co-change run_id is a REAL portal commit sha (check 2, no synthesis); SPARSE (107 co-change sessions / 454 touch-commits -- co-change is the exception, check 4, not over-emitted); shared provenance (check 6 -- DS~B's silent-display-fork sessions subset the store run_ids; reuses the certed e6f5b00e2 analysis, adds only the CSE projection); deterministic event_ids (check 5, idempotent re-ingest); fail-closed cse_schema.validate @0.3 (check 3); fidelity round-trip (check 7). Emit = 257 CSEs / 107 sessions. INDEPENDENT git-verify of 3 sampled run_ids: 0258f251 (Valuation UI, 34 tracked files), 073d9608 (CashDrag redesign, 3), 08efe415 (UI improvements, 3) -- ALL real portal commits co-changing >=2 tracked frontend files. Phantom-guard holds on the standing store. (Note: the store holds RAW co-change events BY DESIGN -- the anti-Goodhart coupling_ratio gate bites DOWNSTREAM in P1, verified 1/7 at the acceptance; broad-commit co-appearances like 0258f251=34 files are raw-store events the P1 gate filters -- the focused-coupling weighting is a gate-ratio productionization refinement, non-blocking.)

### (ii) STANDING MONITOR auto-demote -- EXERCISED (the P3 reversibility) -- PASS
promote_monitor.py --self-test 7/7: SUSTAINED holds (silent-display-fork current>=floor 0.15); DEGRADED FIRES the auto-demote on a REAL below-floor measure (render-without-null-guard 0.051 < 0.15 -> deregistered, check 4 -- exercised, not config-read); reversal is EXACT (check 5 -- degraded removed, SUSTAINED one retained); durable DEMOTED CSE emitted (check 6 -- the R4/AC5 emission fix carried through to the monitor's demote path); NEGATIVE CONTROL (check 7 -- an UNARMED tick DETECTS DEGRADED but does NOT demote, proposes only = zero-auto-mutation unless armed). LIVE tick: silent-display-fork 0.180 -> 0.180 SUSTAINED. So the monitor auto-reverses a lost warrant, exercised on a real degradation, exact + inspectable + gated-on-armed.
Note: the self-test's "2 MATERIALIZED" is the FIXTURE (one healthy + one degrading, to exercise both paths), temp-isolated -- NOT a claim that render-without-null-guard is live-materialized (it was DROPPED at the acceptance). The real live manifest holds ONLY silent-display-fork (re-confirmed MATERIALIZED, commission CTO-PROMOTE-20260708T1521Z; the monitor self-test did not touch it).

## What this closes
The flagship SEMCTL loop is now STANDING + self-healing: the measure re-runs continuously on git-real co-evolution; the monitor re-measures each MATERIALIZED warrant each tick and SUSTAINS / AUTO-DEMOTES (exact reversal, durable CSE) / holds-UNMEASURED-as-finding (never blind-demotes on a missing measure -- I1 honest-missing). Grounded on LIVE in-VPC Trino (257 CSEs persisted, COO~B's L2: coevo_pairs_frontend 0->54). The loop-close is durable, not a one-time proof.

## DELTA RE-GLANCE -- cert STANDS on HEAD 713d4aec2 (strengthened), confirmed-consistent (COO~B 161151Z, verify-don't-trust on a post-cert change)
0.5.0 hardened the monitor AFTER this cert (ee196ed65 governance-conditions + 713d4aec2 ruff-fix), so the certed artifact != HEAD -- re-glanced on HEAD (self-test 12/12). The delta implements CTO's 3 armed-mode governance conditions + is STRICTLY MORE CONSERVATIVE; every certified property PRESERVED:
- demote STILL FIRES on real sustained degradation (check 4: now on 2/2 CONSECUTIVE DEGRADED); exact reversal (5); durable DEMOTED CSE (6, + NOTIFY audit); zero-auto-mutation-unless-armed neg-control (11) -- all HELD.
- ADDED conservatism (strengthening, not weakening): FLAPPING GUARD -- a single DEGRADED tick HOLDS (consec 1/2), manifest intact (checks 3/3b), closing a single-tick over-reaction gap; RECOVERY -> RE_PROPOSED, NEVER auto-re-promote (routes to owner ratify, checks 8/9/10).
- BEHAVIORAL CHANGE, honestly noted: my cert exercised SINGLE-tick auto-demote; HEAD requires >=2 CONSECUTIVE DEGRADED. This is strictly more conservative (harder to demote, not easier) -- the reversibility property holds (demote fires on CONFIRMED degradation), an over-reaction gap closed. No re-cert needed; cert stands on HEAD as strengthened. 0.5.0's claim (consistent + only-strengthens) VERIFIED, not trusted (re-ran 12/12 + read each check).

## Compiler Tools
- Blind re-ran both self-tests (producer 7/7 + monitor 7/7 at cert-time; monitor 12/12 on HEAD re-glance) + --emit the batch and git-verified 3 sampled run_ids (git -C portal show --name-only) = the standing-measure phantom-guard + the monitor auto-demote exercised + the post-cert delta re-glanced. No comp-tool models a standing promotion-monitor; the exercised self-tests + git are the grounding.

-- 3.0.0_SA_CVO
