# CVO delta 2026-09-01 03:00Z - 05:00Z -- W2 fired, overspent, was fixed mid-run, completed at 100%, and graded PASS; and the parity census turned into an audit of OUR OWN gold

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

Delta since `session_cvo_2309-0300Z_seat_migration_certifications_and_the_serve_precondition.md`
@`bb58c33ef0`. Zero commits by this seat in the window; the work was grading, and the artifacts
graded belong to other lanes.

---

## 1. WHAT COMPLETED

**ADVI_BDPARITY P2-2 (W2) -- the full-population parity census -- FIRED AND COMPLETED.** Andrew
granted vendor egress 03:4xZ; COO discharged the second limb separately as `Y-MINT-SEQ`, deliberately
renaming it so ONE LABEL could not carry TWO GATES (had it released under the name "W2" an hour
earlier, a 5,309-account vendor pull would have fired with no sovereign word).

```
  accounts        5,309 of 5,309    100%
  cells attempted 15,927  = 15,445 COMPARED + 112 SELF-INVALID + 370 NO-LINKABLE-DAYS
  classes         EXACT 6,226 / TIGHT 7,225 / LARGE 1,994 (1,516 not explained by coverage)
  range_match     15,445 / 15,445  -- 100% AT POPULATION SCALE
```

---

## 2. THE GRADE -- pre-registered BEFORE the fire, at 90610

Criteria were filed before the run precisely so they could not be written to the result. All four MET
plus the pass bar. Arithmetic re-derived at this seat: every per-period class sums to its n, class
totals match, and the two denominators close exactly.

**The ratified standing sentence, replacing the one this fabric was required to use all night:**
> Performance-feed parity is MEASURED at n=15,445 cells over 5,309 accounts, with 1,994 LARGE cells
> (1,516 not explained by coverage) remaining open. **NOT "parity proven."**

⭐ **`range_match` 100% is the strongest result and it is about the METHOD, not the data** -- P1 could
assert the request-side contract at n=5; it now holds across 5,309 accounts, validating the ruled
position-plus-dates join outright.
⚠ **Counterweight in the same table:** 1Y carries 949 of 5,156 day-count residuals (18.4%) against
QTD's 0.9%. A 20x non-uniformity, surfaced and correctly left UNDIAGNOSED.

---

## 3. ⛔ THE 5x VENDOR OVERSPEND -- caught by a probe the executing seat designed against itself

`0.4.0_DS_ClientPlatform~Y` fired chunk 1 of 45 as a bounded rate-limit probe rather than committing
the full budget. It found a defect that was **not the risk it was looking for**.

```
  chunk 1        600 vendor calls for 120 accounts = exactly 5.0x. 480 wasted.
  CAUSE          a bare boto3 lambda client carries read_timeout=60s and RETRIES ON TIMEOUT.
                 A 120-account chunk takes ~168s. Client gave up at 60s; botocore re-invoked; 5x.
  SHAPE          IT FAILED SILENT TOWARD MONEY -- the runner counted ZERO landed and aborted
                 while the vendor had been charged five times. The report and the bill disagreed
                 and only the bill was right.
  had it fired all 45 chunks as one act: ~26,500 calls instead of 5,309
```

**Fix `e352f70476`, verified at source by this seat:** `read_timeout=360` (above the function's own
300s ceiling), `total_max_attempts=1`, and TWO import-time asserts that read the APPLIED config off
the client object and refuse.
⭐ **The near-miss inside the fix is worth more than the fix:** its FIRST version used
`retries={"max_attempts": 1}`, which botocore renders as `total_max_attempts: 2` -- `max_attempts` is
the RETRY count, not the TOTAL. **That would have quietly halved a 5x overspend to a 2x while looking
correct and testing green.** Caught only by reading the applied config. DESIRED != APPLIED, on a
config literal.

**The fix completed the full state ladder, which is rare here:** DESIRED (the literal) -> APPLIED
(the asserts) -> **EXERCISED (5,189 keys)**. COO ordered the re-probe on exactly that ground.

**Version census re-derived at this seat** (`s3api list-object-versions`, own query, own histogram):
`5,189 keys at 1 version / 120 at 5 / ZERO at any other count`. **The binary shape is the finding** --
a partially-effective fix would leave 2s or 3s somewhere in 5,189 keys. Bound stated: same substrate
as the executing seat's check, so a re-derivation rather than a second plane; its CloudWatch
invocation count (51) is the genuine second plane.

**Ledger closed:** 5,843 calls vs 5,358 clean = **485 overspend (+9.1%), all of it chunk 1**. Projected
5,843 before the resume ran, measured 5,843 after -- a pre-registered number landing exactly is a
control on the ledger, not a boast.

---

## 4. ⭐ THE CENSUS BECAME AN AUDIT OF OUR OWN GOLD -- the most consequential outcome

The harness exists to check BD's numbers against ours. **It caught ours.**

Specimen: account `0077573397`, 1Y off by 636,011%, full 252/252 day coverage both sides. One day
(2025-10-15) moves bmv `$2.33` -> emv `$1,164.46` with **zero recorded cash flow and status OK**.

**Population: 114 rows of 1,525,152 daily returns exceed |r_net| > 1.0** -- and they are NOT all
small-base (BMV p90 `$364,544`, max `$4.6M`). The first specimen was unrepresentative of its own class.

### 4.1 The call that changed the outcome: READ, do not SCREEN
`0.4.0_DS_ClientPlatform~Y` proposed raising `NEAR_ZERO_BMV`, then **refuted its own hypothesis by
measurement before anyone acted**: 13,211 rows under $10 BMV to catch 36 = **367 false positives per
true one**, and it would still miss the rest. It also proved **the TWR identity holds EXACTLY on every
pathological row** -- the producer did correct algebra on wrong inputs -- so no formula-based screen
can exist.

**This seat's inference, which COO adopted as the ruling:** *"the data does not separate cleanly" is
an argument AGAINST a screen, not for a better bound.* A threshold nobody can derive is a threshold
nobody can defend at review, and **114 rows is not a screening problem, it is a reading problem.**

⛔ **AND COO CORRECTED ME, CORRECTLY:** the screen has **TWO CONSUMERS WITH OPPOSITE ERROR COSTS.**
For P3's input, a false positive is free and a false negative means *tuning our producer until it
reproduces a garbage figure that matches the vendor, baking the defect in behind a GREEN PARITY
CLASS*. That consumer wants over-inclusion; an underivable bound is CORRECT there. My argument held
only for the REPORT. **I collapsed "underivable" and "unsafe", which are different properties.**
**General form: a control with two consumers has two error costs, and one threshold cannot serve
both. "Is this threshold defensible?" has no answer until you name the consumer.**

### 4.2 What reading produced that a screen could not
```
  A  no recorded flow, value moved       79 rows / 70 accts   bmv median    $23.75
  B  flow > 10x the base                 21 rows / 17 accts   bmv median   $35,689
  C  flow recorded, comparable to base   14 rows -- NOT DISPOSITIONED, and said so
  control: TWR identity holds 114 of 114
```
>> **"70 broken accounts" became "~35 DATES with a flow-ingestion failure, FOUR carrying 52%."** The
remediation is **PER-DATE, not per-account.** A screen returns a COUNT; the date-clustering is a
property of the LABELLED set and is invisible without per-row mechanism labels. <<
**Its control is what makes it a finding rather than a pattern:** the clustered dates carry a NORMAL
population-wide `cf_net==0` rate (84-86%, same as controls) while control dates carry **ZERO** blowups.
First half rules out "those dates were odd for everyone"; second rules out "we found clustering
because we looked for it."
⭐ **A and B are different defects and only A is a data defect** -- B is a real flow against a base too
small to divide by: the return is meaningless but nothing is missing. Reporting all 114 together would
have overstated the data defect by ~21 rows and aimed remediation at the wrong producer.

---

## 5. Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `aws s3api list-object-versions` | 2 (bucket probe + full histogram) | PASS | re-derived the 5,189/120/0 version shape independently; the discriminator was the ABSENCE of a third value |
| `git show e352f70476` | 1 | PASS | read the retry fix at source rather than accepting "both arms exercised" |
| python arithmetic re-derivation | 1 | PASS | every census line closed; caught nothing, which is the correct outcome for a control |

**What worked:** re-deriving the version histogram myself. The executing seat's claim was true, but
"zero duplicate writes" was the sentence the whole vendor ledger rested on and it cost one query.
**What failed:** nothing this window.
**Gap found:** none new; the per-DATE producer defect (s.4.2) is an UNCOVERED item with no owner --
surfaced by `1.0.0_SA_CTO` at 90743, allocation is `2.0.0_SA_COO`'s, widen-or-not is Andrew's.

---

## 6. Current State

- **P2-2 CENSUS DELIVERED** `ADVI_BDPARITY_P2-2_CENSUS_RESULT_20260901.md` @`3637812fbc`, push state
  LOCAL. Graded PASS. **P3-EXACT is SEATED** (`0.4.0_DS_ClientPlatform~C`) and unblocked on completion,
  not on the grade -- correctly, since a classification only the grader needs must not gate a sequencer.
- **Vendor ledger CLOSED** at +9.1%, fully attributed, no open spend.
- **W2's original purpose is DISCHARGED.** The sentence "parity is PROBED at n=5, census armed and
  unfired" is retired and replaced by a measured one.

## 7. Blockers

**No CVO-owned blocker.** Open items belong elsewhere and all are named with owners:
- 1,994 LARGE / 1,516 unexplained -> P3-EXACT's material.
- 1Y day-residual 20x non-uniformity -> surfaced, UNDIAGNOSED, no owner named yet.
- C-class 14 rows -> `0.4.0_DS_ClientPlatform~Y`, deliberately deferred.
- **per-DATE flow-ingestion defect -> NO OWNER.** Not in Andrew's ruled 22-TO D2 bar. Two failure
  modes both invisible to him: quietly absorbed (D2's bar widens past what he ratified) or quietly
  dropped (a measured defect in the figures D2 exists to publish). Carried to him at this terminal.

## 8. Next Steps

1. **[Andrew]** The per-DATE re-ingest: inside D2's bar, its own carrier outside it, or wait. Any is
   fine; the failure is it going nowhere while looking handled.
2. **[Andrew]** Certification word on `comp-read --enumerate` (graded 8/8 on committed bytes at 03:0xZ).
3. **[0.4.0_DS_ClientPlatform~Y]** The C-class 14, when resumed. Must NOT be folded into A or B.
4. **[3.0.0_SA_CVO]** Grade P3-EXACT outputs as they land; otherwise proof-of-spec management.

---

## 9. CORRECTION, appended 2026-09-01 ~05:0xZ -- the label above is SUPERSEDED

**This section is APPENDED rather than the text above being rewritten**, so what was known at
05:00Z stays legible. The numbers in s.1 and s.2 are UNCHANGED and still close.

`s.1` and `s.2` record the 112 withdrawn cells as **SELF-INVALID**. That token is WITHDRAWN.
`2.0.0_SA_COO` has ruled the label **`NOT-COMPARABLE`** (05:0xZ), and it is the right one:

- **Withdrawing the 112 before comparison was CORRECT** and is not disturbed -- they cannot be
  meaningfully compared and must not inflate an agreement rate.
- **Calling them SELF-INVALID asserted a different claim** -- that our data is WRONG -- which the
  evidence had not established. **~21 of them have NO MISSING DATA**: a real recorded flow against a
  base too small to divide by. The value is sound; only the percentage is meaningless.
- `0.4.0_DS_ClientPlatform~Y` corrected its own delivered artifact AFTER it graded PASS.

⛔ **AND THIS SEAT'S FAILURE IS THE PART TO CARRY, because it is not an oversight.** I did not skim
the label -- **I singled it out and PRAISED it to Andrew** as evidence our own bad data could not
inflate the agreement rate. I was right about the withdrawal and I repeated the overstating label
while commending it.
>> **A grader who COMMENDS the defective element is worse than one who overlooks it, because the
commendation travels.** <<
⭐ **And the refuting evidence was in my own hands one message earlier.** My grade of the 114
(`90742 s.4`) established that A and B are different defects and that **B has nothing missing** -- I
wrote *"reporting these together would have overstated the data defect by ~21 rows"* about the 114,
then failed to apply the identical argument to the 112. **Same evidence, same seat, same hour,
carried in one direction and not the other.**

**The gold defect is UNDIMINISHED by this.** It narrows a LABEL on a withdrawn population; it does
not touch the 79 missing-flow rows, the ~35-date clustering, or the two-way-audit finding.
