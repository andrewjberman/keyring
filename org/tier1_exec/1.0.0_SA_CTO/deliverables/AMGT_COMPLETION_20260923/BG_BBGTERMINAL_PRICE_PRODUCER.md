# `0.0.3_BG_BBGTerminal` -- THE LEAD PANEL PRICE PRODUCER, OWNER AND RUN

Exact seat: `0.0.3_BG_BBGTerminal`. Reviewer: `3.0.0_SA_CVO~Z`. Runtime: CLAUDE. Author:
`1.0.0_SA_CTO~Z`. Read, in this order and before any Bloomberg act:

1. `integrations/bloomberg/READ_HERE.md` -- **CLAUDE.md names this MANDATORY for ANY Bloomberg scenario.**
2. This mandate.
3. `RULINGS.md` **R-15**, **R-21** (its card-answer table at `:1493-1495`), **R-41**, **R-41a** -- in this
   same folder. R-21 sat unread in this seat's inbox from 03:17Z; it is the authority for everything below.
4. `org/tier1_exec/4.0.0_SA_CRO/deliverables/LEAD_PANEL_END_TO_END_GAP_BRIEF_20260923.md`, hop 6a and item 4.

**WHY THIS MANDATE EXISTS AND WHY IT IS LATE.** R-21 said *"a mandate follows from this seat"* and none was
written. `0.0.0_AB_MSTR~Z` measured this seat NOT REGISTERED (last log 2026-09-23 11:30-11:50Z) and spawned
it at 09:31:52Z, LIVE PID 16952. ⛔ **`1.0.0_SA_CTO~Z` then compounded it: R-41 routed "who owns the price
producer" to MSTR as an open seating question when R-21's own table had ALREADY recorded Andrew's answer
naming this seat (`:1494`, call 3).** The question was answered ~03:2xZ and re-asked at ~09:2xZ. That is this
seat's lost six hours, and it is named here rather than left as ambient lateness.

## THE DELIVERABLE

**A person opening the Lead Panel sees Trending x Price for the AMGT universe with a price generation dated
the current trading day, produced by a scheduled deterministic producer -- not by the 14-day dated fallback.**

⛔ **THE CLOCK IS REAL AND IT IS FIVE DAYS.** The Lead Panel's price generations are dated **2026-09-15** and
are served ONLY through a 14-day dated fallback that **stops finding them on 2026-09-29**. After that a
baseline cannot distinguish *"the producer never ran"* from *"the producer ran and found nothing"* -- the two
read identically, which is why this is a deadline and not a preference.

## AUTHORITY -- GRANTED, AND THE CONSTRAINT IS ON MECHANISM, NOT ON WHETHER

⭐ **THE VENDOR WORD IS GIVEN. DO NOT WAIT FOR IT AND DO NOT ASK FOR IT AGAIN.**
- **R-15** @`884475c5a1`, Andrew-direct ~02:4xZ VERBATIM: *"you have egress for whatever calls you want"*, whose
  recorded narrow read authorizes **"(i) the price pull"** by name.
- **R-21** @`b390c36444`, ~03:2xZ VERBATIM: *"all recs approved, and you have all the egress you want for
  vendors. Only thing I'd note is that the pull should be deterministic/scripted in nature like the existing
  pull, i do not like the idea of relying on an agent for..."*

⛔ **SO THE ONE BINDING CONSTRAINT IS R-21's MECHANISM CLAUSE, AND R-21b MADE IT A GRADING CRITERION:** *"a
candidate whose evidence depends on a vendor call made in an agent turn is a FAIL ON MECHANISM, EVEN IF THE
DATA IS RIGHT."* The producer is a **deterministic, scripted, re-runnable artifact with a trigger** --
`price_axis_pull.py` + `generation.py` + the schedule -- in the shape of the existing `OPAL_BBGTML_daily_pull`
family this seat already runs. **An agent-typed lookup is a FAIL even if every number is correct.**

⚠ **This grant covers the PRICE PULL. It does not reach `rk-49`/Lusha, which R-21's same table itemises as
WITHHELD (`:1495`), nor any other gate** -- R-15's own line: egress authorizes NO OTHER GATE.

## First action

Run the existing producer once, ad-hoc, as a QA fire, and read back the generation it writes. CLAUDE.md
permits exactly this: *"Ad-hoc gold runs are PERMITTED FOR QA; production pipelines MUST be scheduled"* --
so the ad-hoc fire is the test and **the SCHEDULED fire is the acceptance**, never the other way round.
Report the generation date, the row count, and the denominator of names attempted vs resolved.

## Acceptance IDs

- **B1 -- THE PRODUCER RUNS DETERMINISTICALLY.** A scripted, re-runnable invocation with a trigger, no agent
  turn in the evidence path. Graded against R-21b.
- **B2 -- A CURRENT-DAY GENERATION EXISTS AND IS SERVED.** A generation dated to the trading-day frontier,
  and the Lead Panel reads it rather than the 2026-09-15 fallback. ⛔ **Resolve the TRADING CALENDAR before
  calling anything stale** -- `lib/trading_calendar.py`, one frontier; everything is `T-1` unless declared and
  Friday IS Monday's answer.
- **B3 -- THE SCHEDULE IS THE PRODUCTION TRIGGER.** Ad-hoc is QA only; success-of-upstream as the sole
  trigger is a defect by CLAUDE.md.
- **B4 -- THE FALLBACK'S EXPIRY IS NO LONGER LOAD-BEARING** by 2026-09-29, or this seat states in STATUS.md
  which named act it waits on and who owns it.

## Write surface

The price producer and its schedule on the terminal box, plus this seat's own
`org/tier0_utility/0.0.3_BG_BBGTerminal/` tree. **Nothing in `lib/research/` and nothing on
`add_security` / `crosswalk.py`** -- that surface is `2.0.0_SA_COO~Z`'s and carries two open clauses
(R-38's one-put-per-run, R-40's universe-input passing). Patches for another owner's surface go to that owner.

## NON-NEGOTIABLE GATES THIS MANDATE DOES NOT LIFT

| gate | what it requires here |
|---|---|
| **NEVER-2, deploy ledger** | An entry in `org/critical_paths/change_management/` **OPENED BEFORE** the first scheduled fire and closed with per-leg proof. ⚠ Read EVERY live worktree when censusing `.open_deploys/`, not just this tree -- a worker's entry sits on a branch until its drain. |
| **NEVER-1, never-widen** | If a run MOVES SERVED OUTPUT, it carries the CTO+COO sign-off pair. **FIRST COUNT THE WRITERS of the key and PRINT N.** A verified DELTA=0 needs no hold. |
| **Rule 30, LGIC** | Every new S3 address is `lib/opal_naming.py` `address()` output and every resource name is `name()` output. A builder refusal is a missing registry row under `infra/logic/registry/`, never a hand-typed workaround. |
| **Moratorium** | No alert, alarm, SNS, SES send, notification, freshness-checker or monitor unless Andrew explicitly asks. |
| **No shadow pipeline** | Andrew's complete veto: no build-alongside, no duplicate output path, no standing parity comparator. Port directly. |

## Reporting

Overwrite `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/LEADPANEL_PRICE/STATUS.md` in place
(`/closer` FILES OVER MAIL -- a current-state file, not a journal; git history is the journal): pins, write
claims, next proof, dependencies with owner, limits. One message per milestone to `1.0.0_SA_CTO~Z` and
`3.0.0_SA_CVO~Z`, carrying one of interface-published / blocker / review-handoff. No ACK messages.

⭐ **IF THE PRODUCER ALREADY WORKS AND ONLY THE SCHEDULE IS MISSING, SAY SO IN ONE LINE AND STOP** -- the
build ladder's first rung is YAGNI and its second is *the estate already has it*. This mandate asks for a
served current-day generation, not for new code.
