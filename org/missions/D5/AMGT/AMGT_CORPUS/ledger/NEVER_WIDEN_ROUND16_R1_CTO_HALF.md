# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 16, `CRPS-r-1` (register `amgt-induction-daily`) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~22:5xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND16_INDUCTION_SCHEDULE.md` @`7e6944a068` (msg 26765, READ-acked).

## VERDICT: REFUSED -- branch 2 is not safe to sign, and the pinned code cannot confine a fire to branch 1

A half must cover BOTH branches (CLAUDE.md NEVER-1). Branch 1 (population 0) is sound as written. **Branch 2 is not.**

1. **Branch 2 writes identity to a place the next pool build cannot see (`Z-S63`, graded here as ARMED and real).**
   - A fire with N > 0 appends N rows to the PINNED checkout's `registrations.json` and puts a pool that includes them.
   - Every other `write_pool` caller builds from CLOUD's `registrations.json`, which lacks those rows. This seat's round-15
     census of `write_pool|write-pool` found **13 DEF writers**: filings, management, peers, posture, social,
     `build_universe`, `add_security` and others.
   - `build_crosswalk` builds from its inputs, not from the served pool: round 15's census read a HEAD build equal to the
     pool, record for record.
   - **So the next CLOUD-side `write_pool` silently drops every identity the scheduled fire registered.** That is a served
     identity regression on a later, unrelated act, which no gate grades.
2. **Neither mode confines the pinned code.**
   - `induction_scheduled` offers `--mode fire|dry-run`, and the action sets `OPAL_INDUCTION_FIRE=1`.
   - A dry-run-only task is a daily detector writing a log. That is a monitor, which CLAUDE.md forbids without Andrew's
     ask.
   - A fire-mode task cannot refuse branch 2 without a code change and a re-pin.

## WHAT MAKES IT SIGNABLE -- the fix, cut into round 17

**One invariant, in the ONE function every pool write passes through (`crosswalk.write_pool`, or `build_crosswalk`
beneath it):**

> **A crosswalk build never drops a record present in the latest served pool.** It unions the latest pool's records with
> the build's own. A record leaves only through an explicit retirement input, which is none today.

- This makes the SERVED POOL the durable home of every registered identity, whichever checkout registered it. It fixes
  `Z-S63` for the scheduled fire and for any other writer on stale inputs, including laptop/site-Z divergence.
- **AC (mechanical):**
  - a planted pool record absent from the build's inputs survives the next `write_pool`;
  - the negative control: a planted retirement removes it;
  - today's pool round-trips digest-equal: 237 in, 237 out.
- **Then** `r-1` re-signs on the SAME act, re-pinned to the commit carrying the invariant. Branch 2's rows then live in the
  pool whatever `registrations.json` a later writer reads. The pinned checkout's file becomes a local trace, not the record.

## Why waiting costs nothing

- The population is **0 of 96** (the COO half's before-state).
- The scheduled fire's first real work waits for a new evidenced folder. The last one, Hitachi, arrived once in 4 days and
  is already registered.
- One round's delay loses no identity. Registering today risks losing one silently.

## NOT REFUSED

- The pinned-checkout mechanism.
- The 13:00Z cadence, and the builder-derived task name.
- The ad-hoc QA plan and the stop limbs.

All of these stand for the re-sign.
