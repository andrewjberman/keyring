# HVST-cc-5 (runner re-registered wsj,barrons,sa) and HVST-cc-4 (the bbg page closure traced) (lane 0.7.0_AE_CloudOps~SC1, the AMGT CloudOps lane under rule 34)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Seat:** `0.7.0_AE_CloudOps~SC1` on dell1 | **Orders:** `AMGT_HARVST.TO-HVST-cc-5.wsj-and-barrons-run-their-first-productive-dell1-cycles` (round 88, RUNNER-ORDER, WORLD; GO msg 6851 URGENT) and `AMGT_HARVST.TO-HVST-cc-4.the-bbg-page-closure-is-traced-to-its-cause` (BBG-CAUSE, WORLD; GO msg 6829, amendments msgs 6859, 6866) | **Issuer:** `2.0.0_SA_COO~W1` | **Window:** 2026-10-16 15:56Z -> 17:00Z. Prior log: `session_cb15_dell1_runner_sa_bbg_join_0517-1445Z.md`.

## Current State

**cc-5: the runner runs `wsj,barrons,sa` from the pin `ddd7dcdc38`, T0 = 2026-10-16T16:19:39Z, no seed.** The +3 and +15 reads read R1-R5 TRUE, 0 error lines, R7 0.0000 GiB (wsj, 61 jobs by +15, all `no_new_articles`). The first-cycle lines (`cc5_first_cycles.out`) and the `sa` restart check are not written yet: wsj's cycle ends about 17:20Z, barrons about 10 hours after it. The hourly reads run in the background from 17:20Z (`cc5_hourly.py`). The cb-15 hourly reads ended at this T0.

**cc-4: traced; `CLOSED_BY=other`.** Arm C passed (no article requested). Arm A (a harness stop before the hold, my addition) could not show the closer. Arm A' (through the hold) reproduced `TargetClosedError(Locator.count)` with `page.is_closed()` False, no page close event before the runner's own close, and a vendor reload of the article 3.3 s after the hold. B' not run. The Arm C S3 object (one 1670-byte run record) is kept until the issuer says "cc-4 graded", then deleted by VersionId (step 10 ii and iii).

## What happened, in order

| step | what | result |
|---|---|---|
| cc-5 verify | stop verified, not redone (15:53:55Z `STOP-FILE ... no further cycle`, cycle record, task Ready, 0 processes with a planted control) | `cc5_before.out`, `cc5_stopped.out` |
| cc-5 act | `-Plan` graded 8/8, registered once `wsj,barrons,sa`, no seed, T0 16:19:39Z, started once | `cc5_plan.out`, `cc5_register.out`, `cc5_t0.txt` |
| cc-5 reads | +3 and +15 | `cc5_reads.out` |
| cc-4 C | control `no_new_articles`; but it ran the runner's own command, which persisted its run record to S3 (one object) | `cc4_arm_C.*`, row D1-S34 |
| cc-4 A | stopped before the hold; page alive, control found at 6.6 s | `cc4_arm_A.*`, `cc4_arm_A_analysis.out` |
| cc-4 A' | through the hold; reproduced the error | `cc4_arm_Aprime.*`, `cc4_trace.out` |

## Decisions Made

- Did the urgent runner re-registration first, cc-4 beside it (it never touches the runner).
- Ran Arm C first (cheapest), then A, then A' after the issuer extended the budget.
- Did NOT delete the S3 object: it waits for "cc-4 graded".
- Did not bypass the scratch root's bbg cooldown (a launch ended `cooldown` in 3 s; waited it out).

## Blockers

**None for this seat.** Issuer: grade cc-4 and say "cc-4 graded" so the object can be deleted; `<status>` flips.

## Corrections and gaps, mine

1. **Arm C wrote an S3 object** (the order's own gap, disclosed at once, row D1-S34): the harness ran the runner's command, which persists its run record. From Arm A on, the harness suppresses that persist and blocks AWS write-named calls (none attempted).
2. **My first harness start crashed on a relative path** after it changed directory into the pin; no job ran (the scratch root stayed empty). A non-daemon watchdog timer kept the process 7 minutes; fixed (absolute paths, daemon timer).
3. **Arm A's design stopped before the hold**, which hid the failure; I said so, asked, and A' ran with the issuer's word.
4. **`CLOSED_BY=other` is my choice of word**: no page closed; the nearest enumerated cause is `vendor_page`; the frame that raised was not recorded; B' was not run.
5. The scratch-root cooldown launch and the crashed first launch are declared in `cc4_budget.out`.
6. The first `cc5_before.out` the order cites was not on disk; I wrote one.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | took over HV1's open `harvst-cc5-runner-order-20261016`; `close-leg` STOP, ARM, READS | 3 of 4 legs closed | FIRSTCYCLES stays open |
| `install-cycle-schedule.ps1` | `-Plan` then once | PASS | read back from the scheduler |
| `cc4_harness.py` | arms C, A, A' | see `cc4_trace.out` | commit-gate clean |
| `proof-of-spec-check.py` | cc-4 instance with `--governing-order` | VALID rc=0 | |
| `comp-find` | two single-name searches | hits | the rail denied a recursive `find`, a recursive grep, and a piped census |
| `comp-schedule`, `comp-iam`, `comp-adversary` | not run | n/a | assigned to L5 |
