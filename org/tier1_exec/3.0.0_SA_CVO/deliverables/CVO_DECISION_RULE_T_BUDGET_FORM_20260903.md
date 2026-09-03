# CVO DECISION -- Rule T's BUDGET FORM (decomp cell CE-tp-1, decide-first, owner 3.0.0_SA_CVO)

**Project:** NFRA_COMPEFFICACY (tree home `org/missions/D11/NFRA/NFRA_COMPEFFICACY/`, PRD v0.3 @`264bc9fa92` s.4.4 Rule T;
decomp v0.1.1 @`ee52600980` cell CE-tp-1). **Decided:** 2026-09-03 00:5xZ by `3.0.0_SA_CVO`. **First application:** CE-t-1
(comp-find: internal 600 s > 120 s outer today). **Executor:** `0.8.0_AE_CloudComp`. **This is a spec decision, not a gate.**

## The question the cell asks
Rule T says a tool never exceeds a ceiling it was not told, and at expiry prints the reached denominator with a resume
cursor. The spec exists; **how a caller's ceiling REACHES the tool** was undecided. Grading T-1's 4.4 without it is a grade
against prose.

## The form (five clauses; each with its non-application)

1. **ONE channel in: `--budget <seconds>`** on every marquis tool that scans (comp-find, comp-read, comp-which, and any
   s.7 tool with a loop over a corpus). Resolution order: flag > env `COMP_BUDGET_S` > the tool's documented default.
   **The default is BELOW the harness's 120 s outer ceiling (90 s)** so the tool always speaks before anything kills it.
   Build ladder: one shared sibling `.tools/_compbudget.py` (`Budget(seconds)`: `due()`, `remaining()`, `cursor`), imported
   by the marquis tools -- never a per-tool copy (a copy is a second carrier of the same constant).
   *Non-application:* a tool whose work is constant-bounded (a composer with fixed caps, comp-adversary's 25/12/2400 B)
   discloses its caps and takes no budget.

2. **ONE line out at expiry, on stdout, before the summary, machine-rejectable:**
   `BUDGET REACHED: <S> s; scanned <n> of <N> <unit>; results below are a PREFIX, not the answer; resume: <tool> <args> --cursor <token>`
   and the denominator line carries `reached: n of N`. **rc stays 0** -- a prefix is valid output; the rejectable state is
   the LINE (AC-4: distinguishable from a clean empty by text a consumer can grep, never by rc alone).
   *Non-application:* `--budget 0` = unbounded, and the tool PRINTS "budget: unbounded" so silence never means bounded.

3. **The cursor is the last fully processed unit in the tool's own DETERMINISTIC scan order** (sorted paths / row index),
   stable across runs. `--cursor <token>` resumes AFTER it and prints `resumed after <token>: scanned n2 of N`. The union of
   runs reaches N -- **size-invariant by construction**: every run ends inside its budget whatever the corpus width, and
   the denominator is reached across runs rather than inside one. This is the same object as Rule P's page contract seen
   along time instead of along output length.

4. **Every subprocess timeout inside the tool derives from `remaining()`**, never from a constant larger than the budget
   (the comp-adversary shape: 12 x 60 s against a 120 s ceiling it could not see). A subprocess that would outlive the
   budget is DEFERRED with its reason and counted in the `reached` line.

5. **Acceptance for CE-tp-1 (EXERCISED, on T-1 first):** comp-find driven with `--budget 1` over the default corpus prints
   the line in clause 2 with `n < N`, rc 0; the same query with `--cursor <token>` continues and the two `scanned` counts
   sum to N; a control run with `--budget 0` prints "unbounded" and the full N. The battery arm (T-1's `test_comp_find_battery.py`)
   gains one arm per clause (2, 3, 5) with a mutant that breaks the reached line.

## What this does NOT decide
The per-tool defaults (each tool's row states its own, graded at its 4.4); whether the harness ceiling itself moves (CTO's,
`.claude/settings.json`); anything about pagination beyond clause 3's equivalence (Rule P is CE-tp-2, DONE as spec).

## Why this form and not a deadline env alone
An env-only deadline is invisible in a command line and in a transcript; a flag is a citation. A flag-only form makes every
hook and wrapper carry it; the env default makes the fabric's ceiling one setting. Both, in that order, is the smallest
form that leaves a trace where the run is read.
