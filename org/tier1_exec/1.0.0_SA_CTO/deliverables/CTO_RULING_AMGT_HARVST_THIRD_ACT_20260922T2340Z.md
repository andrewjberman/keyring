# CTO RULING -- `AMGT_HARVST` h-10: the THIRD live act is GRANTED, CONDITIONAL on a no-network rehearsal

**2026-09-22 ~23:4xZ, `1.0.0_SA_CTO~Z`.** Authority: Andrew's session egress grant (@`c5f33fe8a3`), exercised per
act through this seat, and the AMGT adjudication word. Raised by `2.0.0_SA_COO~Y` (msg 24451).

## WHAT HAPPENED -- the second granted act spent, nothing landed

- The `bbg` per-symbol probe was the **FIRST vendor call of the run**: a real call to `www.bloomberg.com` against a
  **186.6h-old parked session**, which returned a genuine `transport.VerificationRequired`.
- **That exception was UNCAUGHT in `__main__.py`'s run handler, so the process crashed BEFORE `Worker.run()`.**
  `sa`, `ft`, `wsj` and `barrons` never got a fetch attempt, live or in replay.
- **Nothing reached the store** -- 89 bronze article objects before and after, 0 bronze listings, 0 silver
  `listing_hit` rows, no new run records. **The harvest write path we both verified was never exercised live.**

⭐ **THE EVIDENCE BOUND, DISCLOSED BY THE WORKER AND CONFIRMED BY THE ISSUER, AND IT CUTS AGAINST THEM:** the event
ledger is unchanged at 233 lines, **and that is NOT evidence the probe made no call** -- the probe's `Publisher` is
constructed with `record=lambda value: None`, so a probe-leg http event **can never appear in that ledger.** The
vendor call is evidenced by the exception naming `www.bloomberg.com`, not by the ledger. **They volunteered the one
fact that makes their own reassuring number worthless.**

## ⛔ THE ROOT CAUSE, IN THE ISSUER'S OWN WORDS, AND IT GENERALISES

> **"The plan print proves COST; it proves nothing about REACHABILITY."**

**That is the finding, and it is bigger than this project.** Both granted acts were preceded by a printed, sized
plan. **A sized plan is a SPEND control. It is not a CORRECTNESS control**, and nothing in either cut exercised the
run handler end-to-end without vendor calls. **Two granted acts have now been spent on defects only the live path
could reveal -- which is the definition of a control that was never built.**

Beside it, a second precise self-conviction: the Phase 0 amendment **specified the SUCCESS path and left the
FAILURE path unspecified**, and the worker implemented exactly what was written. ⚠ **The order's own contract
already answered it** -- the probe is *"adopted or recorded UNRESOLVED with its reason"* -- so **a probe failure is
a RESULT to record, never an abort.** The contract was right and the amendment did not carry it through.

## RULING

**1. THE THIRD LIVE ACT IS GRANTED, CONDITIONAL on the rehearsal passing**, with its evidence shown to this seat
before anything fires. The rehearsal as the issuer specified it is adopted whole:

- the full run handler, **all five publishers**, harvest mode ON, with an **INJECTED probe FAILURE** -- the exact
  exception class the live run raised;
- **the network POISONED at the real call sites**, per `3.0.0_SA_CVO~Z`'s sharpening: a no-network phase that
  PASSES is self-certifying only if it **could not** have reached the network, **so the control to name is the
  POISON, never the absence of permission**;
- writes to an isolated prefix or a stub;
- and it proves the three things two attempts never proved: **the handler REACHES `Worker.run()` after a probe
  failure; EVERY publisher job starts; the harvest write path produces bronze AND silver rows.**

**2. CUT IT AS PHASE 0b ON THE SAME OPEN ORDER.** The issuer's preference and the right one: the decomposition is
frozen, `h-10` is already phased, and re-homing would cost a round for no gain.

**3. ⚠ THE REHEARSAL PROVES THE HANDLER. IT DOES NOT PROVE THE SESSIONS -- and I am naming that because it is the
next way this could spend and land nothing.** The publisher sessions are ~7.6 days old and **one of five has now
demonstrably challenged.** The other four are unmeasured.

⭐ **The fix resolves this rather than dodging it:** once a probe failure is a RESULT rather than an abort, a
challenged publisher is **recorded `UNRESOLVED-CHALLENGED` and the run CONTINUES to the others** -- which is
exactly what the contract always said. **So stale sessions become a recorded outcome instead of a crash, and the
third act is worth firing even if more publishers challenge.** What it must not do is crash on the second one.

**4. THE SPEND WAS NOT A TOTAL LOSS, and I grade that honestly rather than writing the run off.** Bloomberg's
per-symbol `news()` route is now **measured: `UNRESOLVED-CHALLENGED` against a 186h session.** PRD s.3 asks for
exactly that -- *"tried once ... adopted or recorded UNRESOLVED with its reason."* **It is UNRESOLVED with its
reason. That is a real PRD outcome bought with the spend**, and it should be recorded as one.

**5. ROWS:** `-Z-W10-S4` ARMED (the uncaught probe exception), `-Z-W10-S3` ARMED and un-root-caused. Neither is
closed by this ruling.

## WHAT THIS COSTS ANDREW, STATED PLAINLY

**Two granted vendor acts, both spent, both landing nothing** -- the first on unreachable harvest wiring, the
second on an unhandled failure path. **Both were the issuer's cut defects, both were self-disclosed with the
measurement attached, and neither worker did anything wrong.** He is told in the same terms.

-- `1.0.0_SA_CTO~Z`
