# 2.0.0_SA_COO — SESSION LOG, 2026-08-25 01:00Z → 02:10Z

**archetype:** COORDINATE

**Continues** `2026-08-25/SESSION_0100Z_ROUND1_RULINGS_AND_THREE_REOPENS.md`. Delta only.
**Commits this window: 7** (32 this session — anchored count `--author='^2\.0\.0_SA_COO <' --perl-regexp`, measured, not
estimated; the base serial's 4,015 lifetime commits are NOT this session's number and must never be quoted as one).

---

## 1. ⛔ THE WINDOW IN ONE LINE

**I ordered every lane to audit its own task order for a defect I had just found in mine. Four lanes returned EIGHT
graded instances, and the three worst were all authored by me.** The instruction cost each lane minutes and bought a
falsified live-plane claim, a wrong-source pointer into a client-facing KPI, a self-contradicting spec, and — from a
different thread — a criterion that would have passed while publishing client bank routing numbers.

---

## 2. CURRENT STATE

| project | `dep_stage` | where it stands |
|---|---|---|
| **D1_CATVIEWS** | EXECUTING | 31 cells; both lanes delivering; 5 TO amendments landed from the self-scan |
| **ADVI_PERFRP** | EXECUTING | `DS~G` 9 cells done / 15 commits; `DE~D` d-1..d-3; `AE~G` start condition still UNMET |
| **ADVI_STITCH** | EXECUTING | Phase-A TOs cut, deliberately unseated |
| **ADVI_INSURE** | DECOMP | awaiting CTO alternate-signer re-cert; TOs stay uncut |
| **OPAL_GLDRNS** | DECOMP → SEATED | **NEW: D-1 mirror decomp @0aae28dd42, 25 cells; `0.4.0_DS_ClientPlatform~H` seated by MSTR on 21 of them, (e) held out** |

---

## 3. THE twr_daily CHAIN — closed in three tool calls, after I routed it to a seat

`ADVI_PERFRP-S3`'s 13-vs-9 column signature, **SOURCE-CONFIRMED** @`acf0132aef`:
`entrypoint:160` writes only date=D to the mirror → `c02:171-174` needs `date={prev}` for BMV → every row takes the
**5-key** refusal branch instead of the **9-key** OK branch → `c02:98` `pd.DataFrame(rows)` derives columns from rows.
**The four columns were never DERIVABLE, not dropped** — which flips the remedy from an engine schema fix to upstream
availability, and makes the obvious "always write the columns" fix a defect that would turn a loud refusal into a quiet
zero return.

⛔ **AND I ASSIGNED IT BEFORE I CHECKED.** I routed a two-leg investigation to `0.8.0_AE_CloudComp~F` while CTO's PRD
s.14 — naming the remedy — sat unread in my own inbox. One `comp-find` answered leg one. **BUILD LADDER RUNG 2 FAILING
AT THE ROUTING LAYER: the rung says check before you BUILD, and it applies identically to check before you ASSIGN — a
COO who skips it spends another seat's cycles instead of their own, so the waste is invisible to the person causing it.**
The stand-down crossed ~F's delivery; ~15 min, read-only, **not recorded as waste** — two independent derivations of one
mechanism is worth real weight under Rule 22.

**My three-value enum (never-written / schema-changed / partition-failed) was NOT collectively exhaustive** — the true
answer was a fourth state. Rule 24(i), in a schema I authored in the same hour I was enforcing Rule 24 on others.
**AN ENUM AUTHORED TO SCOPE AN INVESTIGATION IS AUTHORED AT THE MOMENT YOU KNOW LEAST ABOUT THE DOMAIN**, so it is the
enum most likely to miss a member and least likely to get a Rule 24 pass. ~F forced their answer into the closest member
and told me so.

---

## 4. THE SELF-SCAN — 8 instances, 4 lanes, and the grading is what made it useful

| lane | found | sharpest |
|---|---|---|
| `DS~G` | 2 of ~8 | **`AC6` named "a01 first/last-seen" and a01 CARRIES NEITHER FIELD.** A lane would stall or QUIETLY SUBSTITUTE — and a wrong new/lost count on an advisor KPI looks exactly like a right one |
| `DE~D` | 1 + a worse render-side find | `primaryCustodian: 'SS&C Black Diamond'` — **the DATA VENDOR, not the custodian**, on the flagship firm |
| `DS~F` | 3 of 18 checkable, 15 held | **O-6 asserted the OPPOSITE of its own citation** — a docstring narrating a PAST ABSENCE, cited as proof of presence |
| `DE~C` | 2 of 6 | **my amendment landed on the acceptance row and not the cell description** — the file said both |

⛔ **A CITATION IS NOT A CONTROL. It tells you someone looked — not that what they found says what they say it says.**
A wrong claim carrying a real `file:line` is HARDER to challenge than a bare assertion. Same asymmetry as
`primaryCustodian`: **correct-looking beats generic-looking at defeating review.**

⛔ **AN AMENDMENT LANDS ON EVERY SURFACE THAT CARRIES THE CLAIM, OR IT HAS NOT LANDED.** DE~C's grading is the mechanism:
the stale half sat where a builder looks for *what to build*; the fresh half where they look for *how it is judged*.
They used the right one **by reading order, not by a control.** *(MSTR derived the identical rule an hour earlier from a
different failure — independent convergence, both of us from being wrong in our own artifacts.)*

**THE REMEDY IS NOT FEWER VALUES IN TASK ORDERS — IT IS VALUES CARRYING THEIR SOURCE GRADE**
(MEASURED-with-denominator / RULED / INFERRED / ILLUSTRATIVE). DS~F found the counter-example in the same TO: O-4 shipped
a measurement WITH ITS FRAME AND ITS OWN CAVEAT, which is why they found `is_fee_earning` instead of recording inf as
dark. **Same author, same hour, both forms.**

**Why the instruction worked, in DS~G's words:** *the seat most likely to fill a plausible wrong value is the seat
TRUSTING ITS OWN TASK ORDER* — the one with least reason to doubt it. DS~F had ALREADY falsified one claim hours earlier
and never thought to audit the rest: **finding one instance did not make them suspect the population.**

---

## 5. Rulings issued (7 amendments, all AMEND — no re-opens, no re-certs)

**`AC9`/`AC13` PASS-ATTRIBUTION** — a whole-tree typecheck is a strong instrument about the TREE and not the LANE;
before/after ref pair, clean→clean across a peer's commit DISCLOSED not claimed. **`AC7` CUSTODIAN → SENTINEL** — a
MISSING PREDICATE, not a true absence (the exact discrimination my own `sma_separable` defect got backwards, in the
opposite direction); dropping the column converts a VISIBLE gap into an INVISIBLE one. **`AC6`** source corrected +
**new/lost DEFINED**: new = FIRST account appears, lost = LAST REMAINING account leaves, never any-account-out — which
would report churn every time a still-active client closes one account. **`AC10` PII ALLOWLIST NAMED** — as written it
passed on paging alone; an implementation emitting all 140 `fact_trn` columns would have PASSED. **No per-firm constant
may fill custodian**; the `FidelityCustodianBar` precedent denied as a licence *before* anyone points at it.

---

## 6. THE STANDING RULE I GOT WRONG TWICE

Issued: *no trigger may read the shared worktree* (from AE~G finding their own `ls`-keyed detector — **a trigger is just
evidence you act on immediately**, and the artifact never records which state it was built against).

- **MSTR's counter:** their letter-union reads disk but fires BACKWARD INTO AVOIDANCE. I amended to forward/backward.
- **`AE_CloudComp~F` falsified THAT:** their Gate 2 is backward-firing and **BLOCKS A PEER'S COMMIT AND UNSTAGES THEIR
  FILES on a false reason.** *Avoidance that acts on someone else's work is not the safe direction.*

⛔ **FINAL FORM: A CHECK MAY READ THE SHARED WORKTREE ONLY IF THE ENTIRE COST OF A FALSE READING FALLS ON THE CHECKER,
AND IS CHEAP.** Direction was never the variable — **WHO PAYS FOR THE FALSE READING IS.** Both corrections came from the
two seats the rule was aimed at, auditing their OWN instruments. That is the rule working.

---

## 7. GLDRNS — the decomp, and where I disagreed with the project owner

25 cells. **CTO scoped it "one entrypoint change"; the CODE may be one line, the OPERATIVE SURFACE is not** — a
NEVER#1 trading-calendar derivation (that file once carried a hardcoded date; a wall-clock D-1 passes every weekday test
and fails silently on Mondays), an ARMED hazard whose disarm sits in another lane's contract, a backfill over 6
partitions **nobody has classified**, and an acceptance bar a sovereign lift condition depends on. Flagged visibly, not
diverged silently. **CTO concurred.**

⛔ **RULE 24(iv) FAILS AND I NAMED IT: surface (e) does not move with the others.** A "fix the mirror" plan silently
covers five sixths of its own axis. MSTR seated ~H on 21 cells with (e) explicitly held out.

**`GLD-d-3`, added PRE-CERTIFICATION on AE~G:** `entrypoint:272` prints a hand-typed `stages=16`. **Correct today — and
this remedy is what makes it false. It is invisible PRECISELY BECAUSE it is currently accurate.** A defect the fix
creates. It rides my TO, because if AE~G derives the count in the same act as adding their own stage, the number moves
for two reasons at once and neither lane can attribute it.

---

## 8. Compiler Tools

| Tool | Result | Lesson |
|---|---|---|
| `comp-find --name 'twr_daily'` | **0 hits / 28,236 files** | a TABLE name is not a FILE name; the tool's own NO-HITS guard said so rather than letting it read as absence |
| `comp-find` with `\|` | 0 hits + **a WARNING naming the cause** | escaped pipes are literals in python `re`; the tool told me before I concluded |
| `comp-find -i 'twr'` | 2,830 / 26,292, banded | `[HEAD]` band put `c02_twr_engine.py:34` first — the producer, in one call |
| anchored `--author` | **7 this window / 32 this session** | the loose form substring-matches own lanes; 4,015 lifetime is NOT a session number |
| cell-id count control | 24 → **25**, per-surface printed | run before every commit; caught nothing this window, which is the point |
| bidirectional `cell_refs` | 0 unresolved / 0 unreached on all 5 amended TOs | held across 7 amendments |
| `safe-commit.sh` | 7 commits, `[msg-verify] MATCH` on all 7 | no gate refusals, no overrides |

---

## 9. For the next seat

1. **OPEN AT ANDREW:** the cot held-away SCOPE (D1-only vs all cot artifacts — **I refused to narrow "ANY figures"**;
   $30,322,927.42 measured, NOT APPLIED, and NEVER#3 already gates it without anyone minting a step), and the
   **insurance-vs-PropertyHome referent** (his "8m insurance" reconciles arithmetically to PropertyHome at $8,378,664;
   insurance-named accounts total $885,016.86 — **two readings survive and only he can settle which**).
2. **GLDRNS decomp needs certification** (CVO or base CTO) before its TO is cut. ~H is seated and briefed.
3. **INSURE's re-cert is still at CTO.** STITCH stays unseated by choice.
4. **Nothing is pushed by this seat** — say "LOCAL @hash, rides integration", never bare "landed".
5. **The lanes are more reliable than my rulings were this window.** Four of them filed findings against their own prior
   reports or their own instruments; three found defects in specs I wrote. Read what they send.
