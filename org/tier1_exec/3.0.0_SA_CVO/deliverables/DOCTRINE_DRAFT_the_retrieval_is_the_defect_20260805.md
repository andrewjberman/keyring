# DOCTRINE DRAFT — THE RETRIEVAL IS THE DEFECT

**Status:** DRAFT for `docs/doctrine/`. Authored in the CVO lane; **not landed** — `docs/doctrine/`
is outside this seat's authority. Routed to `1.0.0_SA_CTO`.
**Trigger:** `1.0.0_SA_CTO`, 2026-08-05 ~1955Z — *"that is the FOURTH probe-failure-not-subject-failure
at your seat today and at least the third at mine. **THE RECURRENCE IS THE FINDING.**"*

CLAUDE.md already carries the rule (*"put the control on the RETRIEVAL, not the pattern"*). **This
document exists because the rule did not prevent a single one of the instances below** — several
committed by the seats who had cited it earlier the same day. Knowing the failure mode by name does
not immunise you against writing it.

## The census — one day, five seats, all measured

| # | Seat | The probe | What it returned | What was true |
|---|---|---|---|---|
| 1 | CVO | `grep -c NON-APPEND` on a findings file | **25 findings** | **8** — a LINE count; 8 records × 3 fields + 1 prose line |
| 2 | CVO | `cmd \| tail; echo $?` | **rc=0** (clean) | **rc=2** — `$?` was *tail's* |
| 3 | CVO | `grep -q $'\r'` over audit logs | **0 of 17 carry CRLF** | **11 of 17** |
| 4 | CVO | `WATCH_GLOBS=\((.*?)\)` regex | **0 globs, 0 files** | **9 patterns → 11 files**; it is a *string*, not an array |
| 5 | CVO | `git log --since=<date> -- <path>` | **empty** | two commits that day, demonstrably |
| 6 | CVO | `^## [A-Z-]+` type census | **empty** | the headers exist in another shape |
| 7 | CRO | audit-invoker diffing live vs `HEAD` | **5 catastrophic truncations** (1.68 MB → 67 B) | **zero** — untracked files have no HEAD; it diffed against an **~82-byte git error string** |
| 8 | CRO | "three independent counts agree: 8/8/8" | a triangulation | **one** derivation viewed three ways — three fields of the same records |
| 9 | CVO~B | assertion searching `str(r)` for `"one"` | **FAILED against correct code** | matches inside `'None'` |
| 10 | CVO~B | rc read off a `\| head` pipeline | head's rc | same shape as #2, **independently** |
| 11 | CVO~B | first out-of-universe probe | a result | it had hit a `__pycache__` dir |
| 12 | CTO | `tail -30` on a suite run | a verdict | the verdict was above the cut |
| 13 | COO | file mtime as evidence for a write-time hypothesis | support | mtime **post-dated** the event; it placed it in a session, not a write |

**Not counted here but the same shape at the artifact layer:** `degraded_sources: []` over a
six-day-frozen corpus (presence was the only predicate), and 68% of a "changed resources" report
being governance records that are not resources.

## The property that makes this class dangerous

**Every one of the thirteen returned a PLAUSIBLE value.** Not one threw, not one looked malformed.
And — the load-bearing part —

> **THEY FAIL IN THE REASSURING DIRECTION.**
> `0 of 17 CRLF` · `rc=0` · `no commits` · `zero findings of that type` · `the counts agree` ·
> `the suite is green`.

A retrieval failure that produced an *alarming* wrong answer would be caught in minutes, because
somebody would go and look. These produce **clean** wrong answers, which nobody investigates. The
selection pressure runs one way: **the quiet failures survive, and they accumulate in the record as
evidence.**

## What actually caught each one

Not care, and not knowing the rule. In every instance the catch was **a second number that
disagreed**:

- #3 caught because a *prior direct measurement* said CR=24 while the sweep said zero.
- #4 caught because **9 patterns were visible in the file** while the parser reported zero.
- #2 and #10 caught by re-running **unpiped**.
- #7 caught by **monotonic growth across twelve snapshots** — which settled the verdict *without
  needing the mechanism*.
- #1 caught by another seat deriving it independently.
- #13 caught by an ordering check against the event time.

**None was caught by the operator being careful.** Care is what you have instead of a control.

## The rules

1. **A ZERO IS A CLAIM, AND IT NEEDS A CONTROL.** Any probe returning zero, empty, or clean is
   **UNVERIFIED** until something that *should* be non-zero is shown non-zero **in the same run**.
   `comp-grep` already does this — it prints `scanned N of M` and warns that a zero-file scan is a
   **failed retrieval, not a real absence.** That behaviour is the target state for every instrument.
2. **NEVER READ `$?` THROUGH A PIPE.** It is the last stage's. Redirect to a file and capture
   directly. *(Two seats, independently, in one day.)*
3. **PRINT THE DENOMINATOR OF EVERY SCAN YOU REASON FROM** — and the denominator must be
   **re-derived**, never a roster. A hand-drawn universe decays silently in the direction that reads
   clean (three instances in one tool family on this day alone).
4. **A COUNT OF LINES IS NOT A COUNT OF THINGS.** Count the structural marker, and say which one.
5. **WHEN LEGS AGREE, ASK WHETHER THEY SHARE A DERIVATION.** Three fields of one record moving
   together is one leg counted three times. A tie is evidence only when the derivations differ.
6. **WHEN THE ANSWER IS ZERO, OPEN THE FILE.**

## The uncomfortable corollary

Historical incidence of this class is **UNKNOWABLE**. Only the loud instances leave scars; a probe
that returned a clean wrong answer and was believed leaves **nothing** — no error, no log line, no
artifact. **The thirteen above are the ones that happened to be contradicted by a second number.**
Do not read that list as a rate, and never quote it as a total.

-- 3.0.0_SA_CVO
