# CERT — `ETFS_POSITIONING.TO-1` **8 of 8** · `ETFS_POSITIONING.TO-5` **6 of 6**

**Certifier:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~19:3xZ
**Authority:** Andrew-direct ~16:5xZ (*"If CVO~Z needs to do some final certifications and etc. on ETFS
or D4 work, that is fine, i can handle that with them directly"*) and ~18:5xZ (*"completely wrap up D4"*).
These are items 1 and 2 of the D4 close-out — the two that needed a body. **Both bodies delivered.**

| TO | instance | verdict |
|---|---|---|
| `ETFS_POSITIONING.TO-1` | `0.4.0_DS_ClientPlatform/deliverables/…TO-1_PROOF_OF_SPEC.json` @`de3c5125d2` | **8 of 8 CERTIFIED** |
| `ETFS_POSITIONING.TO-5` | `0.7.0_AE_CloudOps/deliverables/…TO-5_PROOF_OF_SPEC.json` @`f32d343133` | **6 of 6 CERTIFIED** |

---

## STEP-ZERO COVERAGE — run at this seat, against the FACE'S OWN authoritative `expected_criteria`

```
TO-1  rc=0 VALID   acceptance rows=8  violations=0   coverage 8/8
      forward-1 8/8 · forward-2 5/5 · backward 5/5   decomp id space = 23
TO-5  rc=0 VALID   acceptance rows=6  violations=0   coverage 6/6
      forward-1 6/6 · forward-2 2/2 · backward 1/1
      NEGATIVE CONTROL: same instance + one bogus id -> rc=1. The check discriminates.
```
**rc captured before any pipe.** 3-arg form throughout — the 2-arg form returns a clean rc=0 that says
COVERAGE UNCHECKED, and that is the form this certificate exists to not rely on.

### Both TOs skip an id, and in both cases the absence is DECLARED — checked, not assumed
- **`ETFS-TO1-AC4` — REASSIGNED off the TO** by issuer AMENDMENT B (2026-08-21T21:0xZ), because it
  required a schedule and therefore Terraform: *"I placed an infra criterion on a scripts TO. A
  criterion an assignee cannot discharge without leaving their lane is a mis-cut criterion."* Removed
  from `expected_criteria` and from the `<criterion>` elements. **The executor routed the lane seam
  rather than assuming it, and was right.**
- **`ETFS-TO5-AC6` — NEVER MINTED.** The face says so in terms.
⭐ **A skipped id is exactly where a certifier should suspect a silent omission. Both survive the check
because both were declared on the face rather than quietly dropped.**

---

## ⛔ FINDING — `TO-1`'s FACE CARRIES A STALE INVOCATION LINE THAT FAILS A CORRECT INSTANCE

`…TO-1.…md:63` tells a reader exactly what to run:
```
python .tools/proof-of-spec-check.py <instance>.json \
  ETFS-TO1-AC1,ETFS-TO1-AC2,ETFS-TO1-AC3,ETFS-TO1-AC4,ETFS-TO1-AC5,ETFS-TO1-AC6,ETFS-TO1-AC7
```
**That id list is stale in BOTH directions** — it still carries `AC4` (reassigned away 7 days ago) and
predates `AC8`/`AC9`. It disagrees with the `expected_criteria` element on the same face.

**MEASURED, by running it against the correct instance:**
```
TRUE rc = 1   INVALID
  VIOLATION: coverage-frame: expected=7 carried=8 matched=6
  VIOLATION: coverage: criterion 'ETFS-TO1-AC4' … has NO instance row (silent omission)
  VIOLATION: coverage: instance row 'ETFS-TO1-AC8' is NOT in the TO's expected set (unexpected addition)
  VIOLATION: coverage: instance row 'ETFS-TO1-AC9' is NOT in the TO's expected set (unexpected addition)
```
>> ⛔ **A CORRECT INSTANCE, RUN THE WAY ITS OWN TO INSTRUCTS, READS INVALID — AND EVERY VIOLATION IS
   WORDED AGAINST THE EXECUTOR.** *"Silent omission"* and *"unexpected addition"* describe a careless
   filer. **The filer did exactly right**; the instruction is what moved.
⚠ **This is the day's recurring shape, now on a TO face:** two carriers of one truth on the same
document — an `expected_criteria` element that is authoritative and current, and a prose invocation
example that is neither — with **nothing marking which is which.** A certifier who trusts the copy-
pasteable line over the element publishes a false INVALID and blames a lane.
**REMEDY (issuer's, `2.0.0_SA_COO~Z`): delete the id list from the example, or regenerate it from the
element.** Not a gate — the certification below does not depend on it, because I did not use that line.
⭐ **Credit where it belongs:** the checker's own output refuses to be quoted out of context —
*"alignment above is computed on a STRUCTURALLY INVALID instance … NOT evidence of validity. Do not
quote them without the verdict."* That warning is the reason a stale run cannot silently look clean.

---

## `ETFS_POSITIONING.TO-1` — 8 of 8

Highlights, and what makes each certifiable rather than merely green:

- **`AC2` / `AC3` — the shell-upgrade path is EXERCISED, not coded.** `AC3`'s own sharpest-test clause
  binds (*"if a code edit is needed to pick them up, AC3 FAILS"*), and the instance proves the negative
  the right way: the **same function object**, no edit between runs, fixture rows added → DIVZ and IDVZ
  upgrade `book_only → full`, PFDE unchanged as a control. **The full/shell decision is made in ONE
  place from DATA (`len(rows) > 0`) and no ticker is named anywhere.**
- **`AC5` — the criterion the TO declared unsatisfiable at cut time.** It required the FIRST **scheduled**
  `bbg/{date}/` landing, and the discriminator is the manifest's own `run_class` field rather than a
  date: `bbg/2026-08-21/run_manifest.json` reads `run_class='scheduled'`. ⭐ **An indeterminate anchor
  resolved by a declared field instead of by wall-clock inference.**
- **`AC6` — the vocabulary was ADOPTED, not minted**, and the MECE hunt found a real uncovered member
  (`2602335D` / TPG Inc, 1 of 106 unique non-cash tickers) **handled as `null` + a manifest count rather
  than swept into an "Other" bucket.** Hunting the uncovered member is postulate (i)'s whole point and
  it is usually skipped.
- **`AC7` — the write boundary is a RUNTIME REFUSAL, not a comment.** `_assert_write_boundary()` raises
  on every forbidden prefix; 0 S3 writes across 4 dry runs; publish additionally gated on `--publish`
  **and** an env grant.
- **`AC8` / `AC9` — served-plane, and the object is PINNED**: ETag `4c7ff3c6…`, VersionId
  `5UfK2PDL0Xl…`, LastModified `2026-08-28T13:01:26Z`, **ContentLength 146,944 B == 146,944 B read to
  disk**. 16 of 16 equations hold across 4 books; 39 of 39 sector keys ordered with the append control
  intact. **A byte-count equality between declared and read is the cheapest possible guard against a
  truncated fetch, and almost nobody prints it.**

---

## `ETFS_POSITIONING.TO-5` — 6 of 6

- **`AC1` — BOTH EventBridge planes censused**: 140 events-rules **and** 18 schedules, with a mutant
  invocation returning no match. ⭐ **`list-rules` structurally cannot see a Scheduler entry**; a
  single-plane census here would have been a clean, confident, wrong answer.
- **`AC3` / `AC7` — 4 of 4 scheduled fires** logged a PUBLISHED line, 13 log streams enumerated, live
  head-object plus a negative control.
- **`AC4` — the RE-CUT criterion, and it certifies on the re-cut, not the original.** The original
  demanded an equality the producer's own guard rejects as degenerate (*"a guard whose two sides are
  the same expression over the same clock has no input that makes it fire"*). **A build that PASSED the
  original would have shipped a guard that can never fire.** As re-cut it requires `as_of` DERIVED from
  data and reconciled against the calendar, stamping `trading_days_behind` — **4 of 4 fires report
  `trading_days_behind=1`**, read at source at HEAD. Original struck in place, not deleted.
- **`AC5`** — 8 of 8 TF root blocks enumerated; 3 pattern hits, **3 of 3 comments, 0 resource
  declarations**, with a positive control.

---

## SCOPE — what this certificate does NOT say

- **It does not close `ETFS_POSITIONING` or D4.** Andrew ruled *"D4 is done"* a **READ**, not a close
  order; the register act travels through his direct channel with this seat. **Nothing here stamps it.**
- **It does not reach `ETFS_INGEST.TO-6`/`TO-8`** — 9 of 12 criteria there remain NOTHING FILED and no
  instance exists. Separate, still open, and the issuer's fork (seat it, or stand the criteria down).
- **It does not assert `alloc_hedge` is safe.** `ETFS-TO1-AC8`'s three-term invariant PASSED as written
  and the served object carries a **fourth** bucket the equation does not name. Measured by the issuer:
  `"alloc_hedge": 0.0` is a **hardcoded literal**, unreachable from data — **so the trap arms on a
  future CODE EDIT, never on a dataset**, and the durable fix is an invariant over ALL buckets. Filed
  INERT; recorded here so a future FAIL is not read as a producer defect.
- **`AC5`'s scheduled-landing evidence is cited, not re-derived** — the run_class read is the
  executor's; re-running it at this seat would be repetition.

**Push state, MEASURED:** both instances **LOCAL** at certification time (`ls-remote` read); push is the
integrator's leg under the standing hold. This certificate is likewise local at authorship.

— `3.0.0_SA_CVO~Z`
