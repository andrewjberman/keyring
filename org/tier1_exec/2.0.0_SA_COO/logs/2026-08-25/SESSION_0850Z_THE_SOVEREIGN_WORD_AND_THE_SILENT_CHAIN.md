# 2.0.0_SA_COO — SESSION LOG, 2026-08-25 08:50Z → 11:45Z

**archetype:** COORDINATE

**Continues** `SESSION_0750Z_THE_SILENT_GATE.md`. Delta only.
**Commits this window: 27. 88 this session** — anchored `--author='^2\.0\.0_SA_COO <' --perl-regexp`, measured.
**PUSH STATE at authoring: HEAD is on NO remote** (`git branch -r --contains HEAD` EMPTY, after an explicit `fetch`).
⛔ **RE-MEASURE THIS BEFORE REPEATING IT — the same line in the previous log was TRUE at authoring and FALSE inside an hour.**

---

## 1. ⛔ THE WINDOW IN ONE LINE

**Andrew ruled, the item his word pointed at was seated and closed inside an hour — and then a lane found that the
pipeline the whole publish intent rests on has been DEAD every Sunday and Monday, deterministically, and nobody knew
because its failure signature is identical to a healthy weekend.**

---

## 2. THE SOVEREIGN WORD, AND WHAT IT CLOSED

**Andrew-direct ~08:5xZ, VERBATIM: *"I'm fine with it on PROD, let's just get the data part sorted."***

| half | state |
|---|---|
| **BRANCH POSITION** | **RELEASED.** No revert, no hold; `0.2.0_DT_PortfolioAnalytics~Z` owed nothing. |
| **DATA / PUBLISH** | **STANDS.** *"let's just get the data part sorted"* says plainly the data is NOT sorted. |

⛔ **HIS RULING CONFIRMED THE CARD'S STRUCTURAL FINDING RATHER THAN OVERRIDING IT.** The measured fact was that branch
position protected nothing — two promotes in 45 minutes, two unrelated projects, neither naming a passenger — while
the DATA gate held throughout. **His sentence says the same thing in one line. The finding was right; the
recommendation attached to it was aimed at the wrong half.**

**THE ITEM HIS WORD POINTED AT WAS BLOCKED ON A SEAT, NOT A DECISION** (CTO measured it): no AE-class lane was free,
and the Cottonwood ingest fix sat authorized-but-unseated for ~3h. **Seated, applied, ledgered and CLOSED within the
hour** — `MODEL_DETAIL_SCOPE=all` live at 09:50:45Z, verified at my own seat against a `CodeSha256` the executing seat
**published before I measured it**. *A value stated in advance is a test; the same value produced afterward is a
description.*

---

## 3. ⛔⛔ THE FINDING OF THE SESSION: THE 49F GOLD CHAIN DIES EVERY SUNDAY AND MONDAY

Found by `0.4.0_DS_ClientPlatform~G` **while answering a different question**, source-confirmed at four seats.

```
a06_dim_identity_crosswalk.py:32   MAP_PREFIX = smartx/platform/silver/fact_allocation_account_map
                            :102   map_asof = args.map_date or map_dates[-1]     <- NO trading-day filter
                             :49   raise ValueError("empty allocation map partition")
LIVE  08-21 Fri 775,217 B | 08-22 Sat 4,507 B | 08-23 Sun 4,507 B | 08-24 Mon 776,585 B
      the two weekend partitions are BYTE-IDENTICAL: a parquet schema + footer, ZERO ROWS
SSM   08-23 FAILED · 08-24 FAILED · CHAIN ABORT stage=a06 (stage 7 of 16), nothing after it ran
```
> ⛔ **`c02_twr_daily` IS STAGE 15. TWR HAS NOT EXECUTED SINCE 2026-08-22.**

⛔ **AND `0.7.0_AE_CloudOps~G` TURNED IT FROM INCIDENTAL INTO DETERMINISTIC — the statement the remedy owner needs:**
**0 of 41 map partitions were EVER written before 12:45Z** (earliest in all history 13:12Z; the map writes `date=D` at
~13:15Z, **thirty minutes AFTER the chain fires**). So **`map_dates[-1]` at 12:45Z is ALWAYS D-1's partition — the
chain structurally never sees the current day's map.**
```
Sun 12:45Z -> Saturday's (EMPTY) -> ABORT     Mon -> Sunday's (EMPTY) -> ABORT     Tue -> Monday's -> proceeds
```
**NOT "sometimes the latest partition is empty." THE CHAIN ALWAYS CONSUMES D-1, AND D-1 IS EMPTY EVERY WEEKEND.**
**A remedy written against "handle empty partitions" fixes the symptom; the mechanism is the D-1 read.**

⛔ **WHY IT SURVIVED, AND IT IS THE UNCOMFORTABLE PART: A CHAIN THAT ABORTS SUNDAY AND MONDAY PRODUCES MISSING SUNDAY
AND MONDAY PARTITIONS — WHICH IS EXACTLY WHAT A CORRECT T-1 PIPELINE PRODUCES OVER A WEEKEND. NEVER#1 exists to stop
us calling that healthy pattern broken. Here the pipeline WAS broken, and the rule that protects against the false
positive is the same thing that made this false negative comfortable.**

---

## 4. ⛔ FOUR CRITERIA OF MINE FAILED THE SAME WAY — RECORDED AS A CLASS

| # | what it said | why no honest path existed | found by |
|---|---|---|---|
| 1 | *"0-diff re-plan after"* | the shared TF workspace held **3 foreign committed-but-unapplied changes**; a blanket 0-diff was reachable only by applying other lanes' cutovers | `AE~H` |
| 2 | *"count > the before-count"* vs **"30 of 64"** | **"30 of 64" fused two populations** (22 roster + 8 children); true coverage was **22 of 64**, gap **42 not 34** | `AE~H` |
| 3 | *"`comp-routes trace` … per key"* | **the tool takes a URL, not a key**, and the mapping was stated nowhere | `AE~G` |
| 4 | *"close through `deploy_ledger.py`, do not hand-edit"* | `cmd_close` **requires a sentinel that does not exist** for those entries; the two available paths **FALSIFIED or DESTROYED** | `DS~F` |

**ALL FOUR WERE WRITTEN TO BE PRECISE. Precision against an unchecked referent is what produced them** — and a
precise-but-wrong criterion does not look broken, **it looks like a competent seat failing.**
⛔ **#4 IS THE SHARPEST: a criterion that constrains the METHOD as well as the OUTCOME can eliminate every honest path
without saying so.** ⛔ **AND I RECORDED THE CLASS FIFTEEN MINUTES BEFORE #4 LANDED, THEN WROTE #4 INTO THE SAME TO
WHILE RECORDING IT.** Record: `A_CRITERION_IS_AN_INSTRUMENT_20260825.md`.
**A fifth, same family: I amended AC3 on a TO and left AC1 carrying the identical defect** (a line range that had moved
five times) — **a correction landing on one surface, which is a class I recorded this morning and adopted a control
for. I did not run the control.**

---

## 5. EVERY TO I ISSUED WAS INVISIBLE TO THE TO SYSTEM

Measured end to end, three rungs, each controlled:
```
1. ~lane folder, markdown header   -> ABSENT under BOTH the lane and base serial
2. BASE folder, markdown header    -> [UNKNOWN] (from unknown)   <- ONLY the folder changed
3. BASE folder + <task_order> XML  -> [PENDING] (from 2.0.0_SA_COO) + summary
```
⛔ **THE TOOL INVERTED: it returned the two TOs that were NOT the seat's assignment and omitted the one that WAS.**
**ALL FIVE TOs I HAD CUT FAILED ONE OR BOTH. Every one reached its seat because I typed a path into a message.**
**AND `list_task_orders` NEVER VALIDATES THE LANE** — MSTR's control: a FABRICATED lane returns the identical base
backlog; a fabricated BASE correctly returns "not found". **There is no query that returns only your lane.**
⚠ **`to-check.py` IS A DIFFERENT TOOL WITH A DIFFERENT MECHANISM** (`:639`, role-classified `assignee_serials`) — `DS~G`
falsified a fused reading of the two. **The practical rule is the UNION: base folder AND the XML block; either alone
leaves it invisible to a tool somebody uses.**

---

## 6. HOLDS — TESTED, NOT RESTATED. TWO OF FOUR WERE STALE.

| hold | verdict |
|---|---|
| `COT_CANON458` | **STALE — registration AND PRD both already discharged.** 7 cells sat behind a two-thirds-false blocker; seated at `DS~I`, delivered, VALID 5/5. |
| `ADVI_INSURE` | ⛔ **STALE BY NINE HOURS — certified @7397dfd83e at 00:01:03Z, on `origin/CLOUD` AND `origin/SITEZ`.** |
| `CAP` | **REAL.** Re-measured with the predicate read from source: **8 marker processes vs 12 live seats** — the check believes 12 spawns remain when 8 do. Routed to CTO for registration. |
| `STITCH` | unseated by choice. |
> ⛔ **A HOLD WHOSE BLOCKER IS CLEARED BY SOMEONE ELSE NEVER NOTIFIES THE HOLDER. Treat every line of a holds list as
> a claim under test, not as a record.**

---

## 7. Compiler Tools

| Tool | Result | Lesson |
|---|---|---|
| `bash -x` on `safe-commit` | found the swallow in one run | **trace a silent refusal; do not read the script and hypothesise** |
| `aws scheduler get-schedule` | `advi-49f-gold-floor ENABLED cron(45 12 * * ? *)` | ⛔ **`events list-rules` and `scheduler list-schedules` are DIFFERENT SERVICES.** MSTR's complete 137-rule census was a TRUE ZERO about the wrong plane |
| `deploy_ledger.py check --red` | RED, correctly | its denominator is **2 sentinels**, not **541 records** — 3 of 4 open entries cannot ring |
| `git var GIT_AUTHOR_IDENT` | returned `Andrew Berman` | not a caller field, and **not reliably a seat field** |
| object-count as an emptiness check (MSTR) | **1 object for the healthy day AND both failing days** | **an instrument that cannot separate the two states it is used to separate** |
| my own guessed predicates | `0` marker windows (titles, not cmdlines); `0` directive keys | **two clean confident zeros from frames I supplied, in five minutes** |

---

## 8. For the next seat

1. **THE PRE-FIRE EXPECTATION IS PINNED AS A DELIVERABLE**, not just a message: `PREFIRE_EXPECTATION_1245Z_20260825.md`.
   **`date=2026-08-25` WILL BE ABSENT AT 13:00Z AND THAT IS THE PASS.** Read against its table, not intuition.
2. **THE a06 DEFECT NEEDS AN OWNER — at CTO.** Not `DS~G`'s surface. **Do not author the remedy under fire pressure**;
   the open decision is whether 08-23/08-24 get backfilled once the chain runs clean.
3. **`WSE_COTMDL` R1+R2 are landed and code-verified.** Remaining acceptance is the **06:00Z scheduled run**: roster
   **64 of 64** AND the non-roster children **PRESENT**, reported as **two populations, never a fused delta**.
4. **TWO CALLS AT ANDREW:** the 49F unsupervised **$138,839,619.90** (rec INCLUDE, deliberately not defaulted), and
   whether 08-21 takes current Opal-membership or needs a re-pull at `all` scope.
5. **The cot EMIT REMAINS STOPPED.**
6. **CRO remains off-limits this session**; alternate certification signer is base `1.0.0_SA_CTO` only.
