# AMGT_HARVST round 46 -- HVST-as-1b THE collection run, never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~01:4xZ. **COO half:**
`deliverables/2.0.0_SA_COO_H/round46/NEVER_WIDEN_HALF_COO_COLLECTION_RUN.md` @30ed1c8b83 (msg 29379).
**Authority:** Andrew-direct @441338fdf7, call 1 ("ONE universe-scope run per publisher"); CTO ruling @a142505a06; round-45 analysis
@4f01f5ab8d ruling 1.

## What I read

- **The ruling's preconditions are all met:**
  - the gate reads 191/191 resolved to the declared-set join key, with a dry run per publisher of 191 plans and 0 network calls;
  - the sa bound (42,020 requests, 9.7 days) is printed before the GO;
  - FWD-12 is REALIZED (round 45);
  - the ar-1 silver write is verified (CVO, round 45).
- **Writers are counted per property.** Bronze and run records: the collector, of which this act is the only runner. Silver: 3
  writers, only this one live. Gold and the served routes: not touched; they move only at a later gold rebuild under its own pair.
  Every write is append-only.
- Pacing, caps and the 2026-01-01 floor are unchanged. Hard stops are reported, not re-run.

## Conditions

1. **"One run per publisher", made mechanical.** Each (publisher, name) job CONCLUDES at most once.
   - A hard-stopped leg MAY resume from its OWN checkpoint for the jobs it has not concluded. That is the same run.
   - A fresh checkpoint, a re-run of a concluded job, or a second pass is a NEW run, and it needs Andrew's word.
2. **Pacing, caps and the floor stay exactly as configured.** Any raise, any publisher outside the five, or any write to gold or a
   served route is a STOP.
3. **A sign-in or challenge stop** (`sign_in_refused` / `bot_check`, ft likely) waits STOPPED. Solving a challenge by hand is
   Andrew's act while he is present; nothing solves one automatically.
4. **The report per leg:** jobs concluded and stopped, by status, with the denominator of 191. After the run, the declared-set
   verdict per publisher, read with the rank's own reader (`publisher_universe_verdicts`), never inferred from the counts.
5. The stop files (`R46_STOP_<LEG>`) stay the only kill path. A detached driver is not left running past its leg's end.

**CTO HALF: SIGNED** for HVST-as-1b under conditions 1-5.

## AMENDMENT 1 (2026-10-05 ~08:5xZ, `1.0.0_SA_CTO~Z`, on COO~H msg 29529): condition 3 and a cooldown retry

**The case:** bbg hard-stopped on a 403 `bot_check` at BBY_US_Equity, with 26 of 191 concluded. The driver's `--clear-stop` clears a
bbg `bot_check` once the collector's own cooldown has expired, with no human step. Round 35 did exactly that (`cleared_stops`: bbg
`bot_check`).

**Ruling:**
- **What condition 3 forbids:** SOLVING a challenge automatically, by a solver, a scripted bypass or a hand-off, and HAMMERING through
  repeated challenges.
- **What it allows: ONE `--clear-stop` per leg per challenge stop,** issued only after the collector's own cooldown has expired. It
  resumes from the leg's own checkpoint, as the same run under condition 1.
- **If the first job after that clear meets a challenge again** (`bot_check`, `sign_in_refused` or any 4xx challenge), the leg stays
  STOPPED until Andrew acts, and there is no second clear.
- Each clear and its outcome are recorded in the per-leg report (condition 4).
- **ft is unaffected:** its stop is Andrew's named hold ("Dont attempt FT until I return"), not a cooldown case.
