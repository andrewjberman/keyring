---
name: comp-schedule
description: THE GATE LEDGER -- what is still armed, on whom, and is it still real. Answers the question nothing else in the estate answers: which preconditions, holds, moratoria and open deploy-ledger entries are STILL BLOCKING, who can discharge each one, and which ones look already-satisfied but are still armed. `comp-schedule` = every armed gate with per-carrier denominators; `--drift` = EXCEPTIONS ONLY (a gate whose discharge condition looks met while it stays armed); `--owner <serial>` = gates naming that seat; `--gate G-N` = one gate with its evidence; `--self-test` = 5 controls. VIEW-TIME COMPILED from the five carriers where gates already live -- there is NO artifact and NO registry, so nothing can go stale. Read-only over repo + git, no AWS, no model calls, deterministic. ⛔ IT COUNTS ONLY WHAT A MACHINE-OWNED GRAMMAR CAN SETTLE: the 135 project `blocking` fields are FREE PROSE and are reported as a READING LIST with their denominator, never as gates -- and a DRIFT CANDIDATE is a question for a named human, never a verdict, and this tool never closes a gate. Engine `.tools/comp-schedule`.
---

# /comp-schedule — the gate ledger

Andrew-direct 2026-09-01, VERBATIM:

> *"having 'preconditions' floating from 12 days ago with no immediate visibility is not good
> planning. I had asked for a comp-schedule or some kind of schedule function to track ongoing
> schedule checks/future gates/etc. If we are going to manage preconditions and other such gates
> over time, we need a clear way of managing these in that persistent location and clear means of
> cleaning/sweeping items from that list when they no longer are needed."*

## The problem it solves, and why the other two tools don't

| tool | answers | covers |
|---|---|---|
| `/schedule-check` | did the JOB run? | scheduled jobs (EventBridge + Scheduler). **Not gates.** |
| `comp-lease` | is the CLOSURE still valid? | C3 closures. **Not gates.** |
| **`/comp-schedule`** | **is this GATE still real?** | **gates — a promise to check something later.** |

**A job that stops firing gets noticed, because something expected output. A gate that outlives its
reason emits nothing at all** — no error, no alarm, no output. It just quietly keeps blocking, or
quietly stops protecting. That asymmetry is the whole reason this exists.

## Invocation

| form | behavior |
|---|---|
| `/comp-schedule` | Every armed gate, with each carrier's own denominator and decidability. |
| `/comp-schedule --drift` | **EXCEPTIONS ONLY** — gates whose discharge condition looks satisfied while still armed. **An empty drift view is the good day.** |
| `/comp-schedule --owner <serial>` | Gates naming that owner. Run it before a serve or promote. |
| `/comp-schedule --gate G-N` | One gate in full, with its evidence lines. |
| `/comp-schedule --self-test` | 5 controls. **Run this first.** |

## NOTHING IS STORED — that is the design, not an omission

The view is **compiled at read time** from the carriers where gates already live. There is no
artifact, no cache, no registry — **so there is nothing to go stale.** A hand-maintained gate list
would be one more thing that decays, which is the exact failure being fixed.

## ⛔⛔ THE ONE READING RULE — carriers are NOT the same kind of thing

**Read every number as *"of what this carrier can SETTLE"*, never *"of what is blocked."***

| carrier | decidability | what that means |
|---|---|---|
| **C1 SENTINEL** `# DEPLOY-SERVE-HELD:` | DECIDABLE | grammar owned by `safe_deploy_core.SERVE_HELD_RE` — the same regex that gates real deploys. **Counted.** |
| **C2 DEPLOY-LEDGER** `.open_deploys/` | DECIDABLE | an open entry file IS an armed gate; it names its own author. **Counted.** |
| **C3 MORATORIA** CLAUDE.md NEVER block | DECIDABLE | standing law. **Counted — but can never DRIFT** (there is no condition that could become satisfied). |
| **C4 SCOPE-GUARD** task orders | SEMI-DECIDABLE | decidable only after excluding inbox chatter; a scope_guard states SCOPE, not armedness. **Listed, not counted.** |
| **C5 PROJECT-BLOCKING** `org/projects/*.json` | ⛔ **NOT-DECIDABLE** | **free prose. NEVER counted.** Reported as a READING LIST with its denominator. |

### Why C5 is refused, measured before any code was written

`org/projects/*.json` is 348 files, 333 carrying a `blocking` key — **the carrier that looks most
like a gate registry.** It is prose:

```
   189   the word "None" written in English
   135   non-null prose ... of which  16 SELF-NEGATE  ("SEQUENCING (not a hard blocker)")
                                      65 use closed / complete / resolved / superseded language
   648   median characters.   30,625 at the longest.
```

**A 30,625-character `blocking` field is an essay, not a field.** Report "135 blocked" and you are
wrong before the second line — and no regex settles it, because the negation is *in the prose*.
**Refusing that total is the single most load-bearing decision in the tool.**

## ⛔ A DRIFT CANDIDATE IS A QUESTION, NEVER A VERDICT

`--drift` raises two signals, and **neither closes a gate.** The tool has no authority to discharge
anything and does not try:

1. **The gate's own reason text says the condition was met** — `SATISFIED`, `co-sign GIVEN`,
   `DISCHARGED` — while the sentinel is still armed.
2. **The reason names an artifact, in a waiting construction, that now exists** (`until X lands`,
   `pending X`).

⚠ **Signal 2 does not distinguish DESIRED from APPLIED.** A condition naming a *deploy* path is not
satisfied by a *repo* path. The tool prints what it found and names who can settle it.

> **Is signal 1 not the prose-reading the tool just refused?** No, and the distinction is the point.
> C5 is refused because prose would decide **whether a gate exists**. In `--drift` the gate is
> *already* established as armed by a machine-owned grammar; the prose is only its **reason**, and a
> satisfaction phrase raises a question **for a named human**. Deciding existence from prose is
> forbidden. Flagging a candidate from prose, and never closing on it, is not.

## What it found on its first live run

- **20 sentinel lines collapse to 4 gates.** One gate stamped across 12 files is ONE gate —
  **a line count is not a gate count.** (And 19 further raw matches were agents *quoting* a sentinel
  in inbox mail; `org/mcp/inbox` is excluded and the exclusion is declared in the output.)
- **A gate whose own comment says it was satisfied on 2026-07-13, still armed seven weeks later** —
  `convert_transactions_to_silver.py:94`, a multi-line sentinel reading *"NEVER#2 (never-widen
  co-sign): *** SATISFIED. *** CTO 113603Z + COO — co-sign GIVEN 2026-07-13."* This is the exact
  class Andrew described.

## `LAST VERIFIED` is DERIVED, and the tool says so on every row

It dates the **last edit** of the carrier — **not** the last time a human confirmed the gate is
still needed. Those are different acts and only one is recorded anywhere. The proxy is derived and
**labelled weak in the output** rather than hidden, because a field that must be hand-stamped is the
registry problem returning through a side door.

## How to use it

1. `--self-test` first. 5/5.
2. **Before a serve or promote:** `--owner <you>` — so a hold never surfaces as a surprise at deploy
   time.
3. **Weekly, or when something feels stuck:** `--drift`. Empty output is the good day.
4. **When a gate blocks a GO:** `--gate G-N` for who owns it, what lifts it, when anyone last looked.
5. Carry the bound with any result: **this is a list of what is ARMED, not a list of what is
   BLOCKING.** An armed gate whose reason expired is still armed until a human discharges it.

## Acceptance battery

`python .tools/tests/test_comp_schedule.py` — 9 legs (per-carrier denominators, prose-never-counted,
grammar-reused-not-copied, chatter excluded, gate-grain, UNREADABLE-never-zero, gate schema
complete-or-explicitly-UNKNOWN, drift-is-a-subset, and a planted **mutant** that flips
`PROSE_IS_NEVER_A_GATE` and must inflate the count to prove the separation is enforced by code
rather than by the data). Scored **0/9 before the tool existed, 9/9 after.**
