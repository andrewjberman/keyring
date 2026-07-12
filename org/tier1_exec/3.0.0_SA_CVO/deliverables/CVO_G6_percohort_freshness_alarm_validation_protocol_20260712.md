# G6 Validation Protocol -- proving the per-cohort freshness stamp + alarm FIRES (CVO exercise spec)

**Author:** 3.0.0_SA_CVO~A (validator role, MSTR 235038Z) | **Date:** 2026-07-12
**Scope:** the EXERCISE that validates G6 (per-cohort freshness stamp + alarm, from the 14-cohort blueprint
b2a17a7e3) the instant DS+AE wire it. Rule-22a bar: a REAL stale input through the REAL path -- never a config read,
never a hand-set alarm state. Ready-to-run; no 49F/bd/schwab artifact is touched (fixtures are synthetic, Opal-side).

## 0. Live baseline (grounded 2026-07-12, the pre-G6 state the exercise improves on)

- The EXISTING global alarm WORKS and is FIRING now: `mdpf-daily-freshness-stale` state=ALARM (since ~07-09),
  `MDPF/DailyChain.TimeseriesStalenessDays` = 2.0 (07-10..07-12), threshold >=1. So the global stall IS caught.
- WHAT IT CANNOT DO (the G6 gap, live-proven): name WHICH cohort. 49financial has been rolled-forward since 07-06
  while inflection advanced -- one global number conflates "chain stuck" with "one partner stale." When the chain
  runs daily but ONE cohort rolls forward, the global as_of can advance and read fresh while that cohort silently
  ages (the hidden-PARTIAL class).
- **DISCREPANCY FLAG for the builders (DS+AE):** the timeseries carries `as_of_last=2026-07-08` while the newest
  per-date partition (2026-07-10.json) carries `as_of_date=2026-07-06` (forced to min-partner per the
  rolled_forward_note). Two vintage semantics on two artifacts. G6's per-cohort stamp should define ONE semantics
  (per-cohort as_of, never a cross-partner min/max) -- and the builders should reconcile which artifact the checker
  reads.
- **The exercise seam already exists:** the current checker takes `PLATINUM_BUCKET` / `TIMESERIES_KEY` env overrides
  (lambda_function.py:34-37). The G6 checker MUST keep that seam -- it is what lets this protocol point the REAL
  code at a FIXTURE without touching the prod artifact.

## 1. The five assertions (each with its falsifier, FP-R2)

| # | Assertion | Fixture | Expected | Falsifier (run it) |
|---|---|---|---|---|
| A1 | **The alarm FIRES on a stale cohort** | one cohort's `as_of` lagged >threshold trading days (state=rolled_forward), others fresh | that cohort's metric >= threshold; its alarm transitions OK->ALARM on the next eval | false if the metric stays 0 / the alarm stays OK -- then the stamp or the alarm wiring is dead |
| A2 | **No false alarm on fresh** (negative control) | all cohorts fresh (as_of = last trading day) | every per-cohort metric = 0; no alarm transition | false if any metric >0 on a fresh fixture -- noise-flood direction |
| A3 | **Per-cohort DISCRIMINATION** (R2-per-limb) | cohort A stale + cohort B fresh in the SAME artifact | A's metric >=1 AND B's metric = 0 (and only A's alarm fires) | false if B's metric moves with A's -- the "per-cohort" stamp is actually global |
| A4 | **rolled_forward counts as STALE** | a cohort present + value carried but `state=rolled_forward`, as_of old | metric reflects the true age (not 0) | false if a rolled-forward cohort reads fresh -- the exact 49F-since-07-06 blindness G6 exists to close |
| A5 | **A MISSING cohort row fails LOUD** (skip-on-missing-field shape) | a cohort absent from the artifact entirely | a distinct missing/staleness signal (e.g. READ_FAILURE-class value), never a silent skip | false if the checker emits nothing for an absent cohort -- absence reads as fresh |

Plus the standing instrument checks: the metric must be emitted per-cohort (dimension = cohort key), and a dead
checker must still be caught (`treat_missing_data=breaching` on the new alarms, same as the global one).

## 2. Method (the REAL path, not a simulation)

1. **Fixture placement (Opal-side only):** write the synthetic per-date artifact(s) to a NON-prod fixture key
   (e.g. `s3://opal-data-portal-v2/platinum/mdpf/_g6_fixture/...` or a scratch bucket the builders prefer) -- the
   fixture is synthetic JSON; no bd/schwab read or write.
2. **Run the REAL checker Lambda** (the G6 per-cohort version) with its env seam pointed at the fixture key --
   the same code path prod runs, alternate input. Invoke it directly (operational Lambda invoke); capture rc +
   the emitted metric values from the response/logs.
3. **Observe CloudWatch:** `get-metric-statistics` for each per-cohort metric (the emitted datapoints) +
   `describe-alarms` for the state transition after the eval period. The ALARM-state transition is the exercised
   proof; a metric datapoint alone is necessary-not-sufficient.
4. **Both directions in one session:** A2 (fresh) first (baseline OK), then A1/A3/A4/A5 (stale variants) -- the
   OK->ALARM transition on the stale run after a green baseline is the bidirectional proof.
5. **Evidence pack:** every claim OBSERVED with the exact command + output line (FP-R1); the alarm-state
   transitions captured verbatim; rc measured no-pipe.
6. **Cleanup:** delete the fixture keys; confirm the prod alarm state is driven by prod data again (the exercise
   must not leave a fixture-driven alarm state behind -- restore-in-finally checked explicitly, not assumed).

## 3. What I need from the builders (DS+AE) to run this

- The per-cohort metric NAMESPACE/NAME + dimension scheme (cohort key) they wire.
- The checker's fixture seam preserved (env-var bucket/key override -- already the pattern).
- The alarm names per cohort (or the single multi-dimension alarm design) + eval period.
- A heads-up when it lands on dev/prod so I exercise immediately (validation is the close condition for G6).

*Validator role only: I run the exercise + verdict the evidence; I do not build the stamp/alarm. The G6 build is
DS+AE via COO (MSTR 235038Z). G1-G5 remain HELD for Andrew's sovereign gos -- nothing here touches them.*
