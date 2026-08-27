# 2.0.0_SA_COO — SESSION LOG, 2026-08-25 15:45Z → 19:3xZ

**archetype:** COORDINATE

**Commits this window: 19** — measured on `%aI` client-side, **not** `--since`. See §6; the first
count I ran returned **0** and was wrong.
**PUSH STATE at authoring: LOCAL, rides MSTR integration.** Re-measure before repeating.

---

## 1. ⛔ THE WINDOW IN ONE LINE

**A four-day client-facing outage turned out to be two unrelated defects wearing one symptom; half is
fixed and verified, half is one deploy away — and almost every wrong turn today came from a correct
instrument answering a question nobody had checked was the right one.**

---

## 2. WHAT SHIPPED

| | |
|---|---|
| **`MDPF_COTREMEDIATION` stage-3 decomp** | 42 cells, alignment both directions with denominators, **CERTIFIED on substance** by CVO (`@73dd2c9251`) — no cell invalidated, no re-decomp owed, cells **EXERCISED** rather than reviewed |
| **Two TOs cut** | DS + AE, both carrying `UNCERTIFIED DECOMP` on their face per the degraded-state clause |
| **Cottonwood RESTORED** | `as_of_last` 08-19 → **08-24**, `n_dates` 458 → 461 (exactly the three converted partitions), `source_keys` advanced. Verified at three seats |
| **Global** | root-caused, fixed, hotfix pin built + exercised through the production entry point. **Still dark at log time — the deploy is the last mile** |
| **Four durable records** | owed seatings + open calls · lane exhaustion · S5 twin precondition · P0 state (twice, superseded once) |

---

## 3. THE OUTAGE WAS TWO DEFECTS, AND THE SECOND WAS INVISIBLE UNTIL THE FIRST WAS FIXED

**COTTONWOOD** — an **internal unsequenced change**, not vendor drift. We amended BD template 226355
in place `@17c38a26f2`; the next scheduled export carried 21 columns; `assert_declared_header`
correctly refused; silver froze. **The attribution was overturned mid-decomp** (Andrew ordered the
re-verify) and no cell encoded the dead story.

**GLOBAL** — a **coherence gate applying a clause outside its domain.** Clause (vi) compares a **sum
over legs whose membership varies by date**; cottonwood contributes on 18 of 461 dates and `08-19` is
the one date whose neighbours both lack it. Its own roster entered and left beside its own values.
**There was never a foreign-day roster.**

> ⛔ **AND IT SURFACED ONLY BECAUSE WE FIXED COTTONWOOD.** Clause (vi) skips the last date
> structurally; the island sat on the one index it could not reach. **The repair made it interior.
> The defect did not appear today — its TESTABILITY did.**

**And a third thing nobody was looking for:** `meta.value_date_rekey` — BD kept **delivering** on
08-20..08-24 while every delivery carried `2026-08-19` valuations. **The cadence never stopped, so
nothing that watches arrival could see it.**

---

## 4. ⛔ THE CLASS THAT RAN THROUGH THE ENTIRE DAY

**Six instances, six seats, one shape: a correct instrument answering a question nobody checked was
the right one.**

| seat | the instrument was right about | the question was |
|---|---|---|
| every freshness probe | the FILE's age | the DATA's age |
| `2.0.0_SA_COO` | 137 EventBridge **Rules** | 155 trigger objects across **two services** |
| `3.0.0_SA_CVO` | `13:31:05` — a true time | **which day** (the format dropped the date) |
| `0.0.0_AB_MSTR` | a clean 404 | in the **wrong bucket tree** |
| `1.0.0_SA_CTO~X` | the item schema's own conditionals | applied to the **wrong plane** |
| `2.0.0_SA_COO` | one executor's deployed bytes | **there were two executors** |

**`1.0.0_SA_CTO~X`'s generalisation covers all of them:** *a tool that borrows a schema, a query or a
sweep inherits that artifact's PLANE silently, and every control you write afterwards is written
from inside it.*

⛔ **MY OWN RIDER, ADDED AND THEN IMMEDIATELY VIOLATED BY ME:** *a second seat's confirmation is not
corroboration if it used the first seat's method.* **I applied it backwards within the hour** —
credited two seats with independent instruments when their core method was identical. **`~B` refused
the credit and was right.** *A false confirmation in the generous direction is the one nobody
contests.*

**THE ONE GENUINE CORROBORATION OF THE DAY, for contrast:** `~B` cherry-picked a pin; `~N`
materialised the same tree per-member independently; **21 members compared, 21 identical.** *Two
routes, one tree.*

---

## 5. FOUR THINGS I GOT WRONG, AND WHO CAUGHT EACH

1. **Cleared a fire on a read covering the wrong executor** — and told `~N` **not** to re-derive it.
   **`~N` checked anyway, using CVO's own rider, and caught a client-visible flip-flop before it
   happened.** *Ad-hoc restore → scheduled run re-breaks it → a green "restored" report already
   filed against the second failure.*
2. **Then INVERTED that ruling** on a premise `~N` had already withdrawn — **asking for a grep whose
   answer had landed 17 minutes earlier.** *The queue was moving faster than I was reading it.*
3. **Seated `OPAL_ASSETS`** — a terminal, directive-less project — **to do work my own S1 pre-filter
   already covered.** Andrew caught it. **Third fabricated work item I killed today** (with the D8
   "missing schedule" whose backstop already existed, and the S3 first-mint that was a true
   non-member).
4. **Briefed a seat on "the uploader was never built"** — quoted from the report's own exec summary.
   **`~I` measured it: built 2026-08-11, scheduled, ran that morning.** ⛔ **The falsehood is a
   HARDCODED STRING the pipeline PUBLISHES** (`estate_report_runner.py:616`) — true when written,
   false since, emitted present-tense for 14 days. **Four seats inherited it by honest citation.**

---

## 6. ⛔ `git log --since` TAKES LOCAL TIME — A NEW MEMBER OF A CLASS ALREADY IN OUR LAW

I ran `--since='2026-08-25T15:45'` for my own commit count. **It returned `0`.**
**`--since` read that as LOCAL 15:45 = 19:45Z — the future.** True count: **19**.

**CLAUDE.md already warns that `--date=format:'…Z'` stamps a false `Z` and `--date=short` crosses
midnight silently. `--since` is the same defect on the INPUT side** — a UTC-looking string silently
reinterpreted. **Remedy is identical: use a form carrying its own offset (`%aI`) and filter
client-side.**

⛔ **And it was a SELF-SUBJECT claim** — figures about my own record are the one population no
external check covers. **Nobody would have contested "0 commits."**

---

## 7. WHAT ANDREW CHANGED TODAY, AND WHAT IT COST TO FIND

- **"Why are we spawning DS~N?"** → measured: **58 lanes / 364 open TOs**. Unclosed TOs consume a
  lane letter's **legibility**. **Reframed spring clean from hygiene into seat supply — and the sweep
  landed within the hour: 385 → 183 open TOs, board coverage 12.1% → 62.5%.**
  *(I over-stated it as a permissions "wall"; MSTR corrected it — a fresh tilde inherits its base.)*
- **"Is the marker a deprecated holdover?"** → **no**, live and fired today. **Testing the premise
  falsified two of my claims.**
- **"Why are we in projects outside directives?"** → `OPAL_ASSETS` stood down; **101 projects closed
  on membership, not age.**
- **Rule 22 → EVIDENCE LAW** (`THING`/`WHOLE`/`LAYER`/`NO`, scaled by who eats the error) and
  **CLAUDE.md cut 55%** with **32 rules and 42 mechanism tokens intact**.
- **D10 minted.** ⛔ **And the sweep created an ordering hazard nobody had stated: a project minted
  before its directive row is BORN CONDEMNED.**

---

## 8. FOR THE NEXT SEAT

1. **GLOBAL IS THE ONLY LIVE OUTAGE ITEM.** Pin `530ba66971` built + exercised green through
   `lambda_handler`. **`~B` ships on `~N`'s green without me.** ⛔ **NEVER#6 discharges on the SERVED
   payload — not the deploy, not the gold write.** Two true completion reports did not sum to a
   restored product this afternoon.
2. **THE INVARIANTS SURVIVED ALL DAY — DO NOT RELAX THEM AT THE LAST MILE.** No weakening/bypass/
   `--force` of the coherence gate · **nobody touches `2026-08-19`'s data to make it pass** ·
   49f + inflection move zero data-bearing fields · acceptance is the SCHEDULED run.
3. **OWED SEATINGS: 3.** 3F-S5 twin (with the `PROVENANCE_CONTRACT_START` precondition — **cite it or
   the disarm did not happen**) · estate-report consumer wire (`~I` live) · D1_CATVIEWS needs a real
   289-line read before it deploys.
4. **TWO SOVEREIGN CALLS OPEN.** The estate-report corpus frozen 25 days under 160 queued proposals ·
   the spring-clean bar (largely overtaken by the membership sweep).
5. **`account_count` IS FANNED-OUT.** cottonwood's own artifact says *"never total this column"*; the
   gate and the composition both total it. **A served `account_count` is overstated.** With CVO.
