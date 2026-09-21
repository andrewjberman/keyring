# /self-drive tick 4 -- **both lanes moving on their own; this tick's work was fixing two carriers of MY OWN that keep going stale**

**Seat:** `1.0.0_SA_CTO` · laptop · CLOUD · **UTC** 2026-09-21 ~04:0xZ
**Arming record:** `ANDREW_DIRECT_20260921_005xZ_...md` @`07b8a03ec3`, §8 @`57751941a0`
**State:** ARMED · cadence 30m · job **`1d285a54`** (re-cut, §3)

---

## 0. HEADER FIGURES -- EACH PRODUCED BY A CALL IN THIS TICK

| figure | value | call |
|---|---|---|
| projects in scope | 2, **PLACED stage 0**, flags `-` | `sequence-check --project` x2 |
| live COO lanes / cap | **3 / 3** | `sequence-check` CAPACITY |
| `MDPF_TAXSMA` | 27 orders, **6 complete**, 21 non-terminal | `git ls-files task-orders/` + first-word `<status>` |
| `NFRA_MCPINDEX` | **0 orders**, `dep_stage DECOMP` | same + `sequence-check` |
| positive control | 33 (`NFRA_OPLGTW`), 2 non-terminal | same |
| unread inbox | **0** | `ls` on my inbox slice |
| IRPT L9 slug | **NOT ARRIVED** | `ls -t read/` -- newest 4 read, none is a slug |

## 1. THE SCOPE MOVED WITHOUT ME, WHICH IS THE POINT

- **`MDPF_TAXSMA`: 4 → 6 complete** since tick 3, `2.0.0_SA_COO~T` at L7 rd1. No CTO act needed or taken.
- **`NFRA_MCPINDEX`: L5 v2 @`e4c6d91353` applies BOTH of tick 3's rulings** (`98952`). ⭐ **The lane added the
  falsifying arms unprompted:** `MX-c-3` now requires **a planted S3 reader to FAIL** the cell's test, and
  `MX-c-4` requires **a planted tool resolving through NEITHER registry to be REFUSED.** That is the
  three-arm discipline -- two arms show a fix works, only a planted negative shows the guard is load-bearing.
  It also settled what I left to it: **S3 versions ARE written this round**, because `FWD-10`'s ACCEPT names
  the versioned S3 home. **Correctly that lane's call, not mine.** L6 is unblocked and is its own.
- **`MX-r-1` keeps its refusal as written** on the rollback exposure. Right.

## 2. ⛔ MY OWN MEMORY EDITS WERE THE CLOBBER, AND `0.0.0_AB_MSTR` NAMED THE FIX WITHOUT INVENTING MACHINERY

`98932`: the remedy is **WHICH EXISTING TOOL**, not a new one. **The `Edit` tool REFUSES when the file has
changed since the seat last Read it** -- so a concurrent peer write surfaces as an error to re-read, never as
a silent discard. `python`, `sed -i`, a heredoc and `Write` carry **no such check**, ⭐ **and a python
anchor-replace IS a whole-file write however anchored the edit inside it looks.** That is exactly the gap I
fell through: I believed I was anchor-editing because the *edit* was anchored, while the *write* was total.
⭐ **`0.0.0_AB_MSTR` disclosed doing the same thing at ~01:1xZ rather than only reporting mine.**

**ADOPTED AND EXERCISED THIS TICK: every memory edit here went through `Read` → `Edit`.** The clause is now in
the file itself (1 occurrence; it was absent, checked before writing so as not to duplicate).

⛔ **AND I BROKE MY OWN NEW RULE IN THE EDIT THAT WROTE IT.** The clause says *"ADD bytes only by REMOVING as
many in the SAME edit"* -- my edit added **241 bytes net and put the file 133 OVER** the ceiling. Three
further `Edit`s brought it to **24,908 / 77 headroom**, all nine failure-mode faces, the overflow rule and the
new clause intact. ⭐ **A rule written and violated in one act is the sharpest evidence that stating a rule
does nothing** -- the same recognition-not-statement point the CVO and I settled an hour ago, arriving as a
fact about me rather than an observation about a law file.

⛔ **A SECOND SELF-CATCH IN THE SAME SEQUENCE: my verification `echo "UNDER"` was a LITERAL, printed beside a
measurement it did not read** -- it said UNDER while the file was 38 bytes OVER. **A LABEL WRITTEN BEFORE THE
MEASUREMENT, in the very check meant to catch a label written before the measurement.** Replaced with a
verdict DERIVED from the number (`if [ $H -ge 0 ]`). **COST: none -- derive the verdict.** NON-APPLICATION:
none.

## 3. ⭐ THE STRUCTURAL FIX: THE LOOP'S OWN PROMPT NOW CARRIES **NO STATE**

**This cron prompt has gone stale three ticks running** -- it still listed `G-C` and `R-OG-22` as carried
after tick 3 closed both, and still called `NFRA_MCPINDEX` pre-L5 after L5 landed. Each time I re-typed the
state; each time it aged within the hour.

**Re-cut as `1d285a54` carrying INVARIANTS ONLY** -- scope, the arming record, the standing holds, the
adjudication rule and the instrument rules -- **and pointing at the newest committed log for STATE.**
⭐ **THIS IS THE SAME CLASS AS "THE CURSOR IS DERIVED FROM THE COMMIT, NEVER THE LOG'S FILENAME": state typed
into a recurring carrier is re-issued, verbatim and confidently, long after it stops being true.** A cron is
the worst instance because it fires unattended every 30 minutes. **COST: none, and it removes a recurring
one.** **NON-APPLICATION: a one-shot prompt, which cannot age.**

## 4. OPEN CALLS AT ANDREW -- **2**, unchanged, neither adjudicable here

Enabling the five Schwab tools (NEVER-class served-output citation); and the owner of the live Gateway's
rollback repair (**REC: first act of whatever seat next holds `NFRA_OPLGTW`**). Neither moved this tick and
neither is re-asked.

## 5. STILL OWED HERE

**`IRPT_BCKEND` round-7 L10 analysis**, waiting on `3.0.0_SA_CVO`'s L9 slug, **measured absent this tick**.
The order slug → analysis → recut is load-bearing (LD-0521) and `2.0.0_SA_COO~B` is holding it correctly.

## 6. COMPLETION TEST

**NOT DONE -- 0 of 2 complete.** `MDPF_TAXSMA` active/EXECUTING; `NFRA_MCPINDEX` active/**DECOMP**. Both
REACHABLE, 0 UNREACHABLE. **No TO cut, no seat spawned, no apply** -- the no-new-seats hold is untouched.
**Push state: LOCAL** for `31704ee9d3` and this log; only `0.0.0_AB_MSTR` pushes CLOUD.

## Compiler Tools

`sequence-check.py` x2 · `git ls-files` + first-word `<status>` over three trees (one a positive control) ·
`Read`+`Edit` x4 on the shared `MEMORY.md` (the adopted instrument) · `wc -c` with a DERIVED verdict ·
`CronDelete`/`CronCreate` · inbox slice `ls`.
