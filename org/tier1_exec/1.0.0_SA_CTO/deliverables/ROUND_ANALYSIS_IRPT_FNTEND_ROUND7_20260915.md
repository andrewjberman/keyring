# ROUND-7 ANALYSIS -- IRPT_FNTEND

**Seat:** 1.0.0_SA_CTO. **Stamp:** 2026-09-15 ~03:1xZ.

**Inputs:**
- 3.0.0_SA_CVO's slug, msg 96838: record @`ac41c29ce1`, carriers C-S93..C-S98, `REMEDIATION_v3.md` @`2d42ebd1b0`.
- 2.0.0_SA_COO~F's packet, msg 96814.

**Round 7 delivered:**
- 4 of 4 orders drained.
- All 4 judgment criteria graded PASS; 3 carry a qualification.
- 10 new rows, all INERT: 5 dismissed and 5 graduated.

**The project still cannot close.** Its closing proofs need IRPT_BCKEND, as round 6 said.

## Rulings on the five open rows, and on the F42-AC10 qualification

1. **W1-S69 -- my bar was wrong.**
   - The check for "the runtime stays node" named `process.release.name`, which reads `node` under bun too.
   - From now on, a criterion that names a runtime names a reading that DIFFERS under the other runtime: the
     listener's image name, and `process.versions.bun` absent.
   - F45-AC10 stands, on the discriminator the worker added.
   - The clause in the task order is 2.0.0_SA_COO~F's to write.
2. **W1-S70 corrects one of my reasons.** In the FE-s-45 adjudication, s.5 said an edit to `vite.config.ts` stops the
   dev server restarting. It does not: vite restarts on a config edit (`isConfig`). RULING (B) stands on its other two
   reasons: every dev user's runtime would move off node, and the proxies were never exercised under bun.
3. **W6-S1 -- fixed by this seat in `.tools/tests/test_governing_binding.py`.**
   - The per-battery bound goes from 560 s to 900 s. That is about 3 times the 275 s the slow battery takes alone.
   - An rc of 124 now prints TIMEOUT, never RED, and the summary counts timeouts separately.
4. **W4-S16 -- fixed by this seat in `.claude/skills/canonical-flow/SKILL.md` Step 3b.** The skill gains:
   - the `--governing-order` call for L7 -> L8;
   - a NOT-BOUND verdict row;
   - "THE FOUR VERDICTS" in place of three.
5. **W3-S35 -- the adapter gives the reason; the validator does not change.**
   - The facts at portal DEV `1f3ce9f0`: `validateContract` appears 9 times -- 1 definition and 8 test uses. No
     production path runs it.
   - So a response with no status reaches the screen as UNCERTAIN, with nothing to explain it.
   - The fix: when the adapter supplies its explicit unknown because a response carried no status, it also supplies a
     `partialReason` saying so.
   - Relaxing the validator instead would also admit a producer's reasonless non-READY state, because it cannot tell
     the two apart.
6. **F42-AC10 qualification -- a non-authoritative cohort reads "withheld", not "unknown".**
   - RULING W keeps "unknown" out of any state that has a truer word. A value the panel declines to assert is
     withheld, not unknown.
   - The change is at `ScopeSummary.tsx:118`, the "Cohort (not asserted)" rows.
7. **W3-S33 -- 2.0.0_SA_COO~F's cell, as measured.** F40-AC5 and F41-AC2 get explicit per-test timeouts.

## Round 8 -- ONE issuance of three small cells

1. The per-test timeouts (W3-S33).
2. The adapter's reason on the no-status path (W3-S35), with a test that runs a no-status body through the real
   adapter and `validateContract`, and reads 0 problems.
3. "withheld" for the non-authoritative cohort (F42-AC10).

The runtime wording from item 1 above applies to any future criterion.

**At Andrew, raised by 3.0.0_SA_CVO:** whether to backfill remediation rows for items graduated earlier that never got
one. The CVO's census counts 42 for IRPT_FNTEND and 291 across 11 channels.
