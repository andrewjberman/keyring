# BRIEF -- 49F/Black Diamond parity: the 3-account validation, and why SI must come out of our function

**Author:** `0.4.0_DS_ClientPlatform~Y` | **Date:** 2026-09-01T00:xxZ | **Status:** findings + one recommendation
**Asked by:** Andrew (validation), routed via `1.0.0_SA_CTO` 90324. The SI recommendation is Andrew's own
instruction, recorded here with the measurements that support it.
**Scope:** ADVI_BDPARITY. Nothing here changes a live TO boundary or closes a face.

---

## 1. THE HEADLINE

Andrew asked for a live parity check on three named accounts, immediately. It was run. **Eight of nine
cells are EXACT, one is LARGE, the requested-vs-returned ranges matched 9 of 9, and the day-count
residual is zero on every cell.**

Separately and more consequentially: **"Since Inception" must be removed from the period set our
function exposes.** We cannot compute a true SI today, and neither can Black Diamond be trusted to
supply one. **Both halves are now measured, not argued.** The recommendation is to cap at 1Y.

---

## 2. THE VALIDATION RESULT

delta = ours - BD, SIGNED, in basis points of cumulative return. Thresholds are the CRO's ruled set
(EXACT `|d| <= 0.5 bp`, TIGHT `<= 10 bp`, else LARGE).

| BD | schwab | period | range_match | ours | BD | delta (bp) | class | days ours/BD |
|---|---|---|---|---|---|---|---|---|
| 20277481 | 0026881039 | QTD | True | 0.011767 | 0.011767 | +0.008 | EXACT | 42/42, 42/42 |
| 20277481 | 0026881039 | YTD | True | 0.083671 | 0.083712 | -0.407 | EXACT | 165/165, 165/165 |
| 20277481 | 0026881039 | 1Y | True | 0.101928 | 0.103800 | **-18.722** | **LARGE** | 252/252, 252/252 |
| 20265531 | 0022002671 | QTD | True | 0.014621 | 0.014621 | +0.000 | EXACT | 42/42, 42/42 |
| 20265531 | 0022002671 | YTD | True | 0.094498 | 0.094501 | -0.030 | EXACT | 165/165, 165/165 |
| 20265531 | 0022002671 | 1Y | True | 0.142046 | 0.142047 | -0.012 | EXACT | 252/252, 252/252 |
| 20350771 | 0065125789 | QTD | True | 0.015646 | 0.015646 | +0.000 | EXACT | 42/42, 42/42 |
| 20350771 | 0065125789 | YTD | True | 0.104161 | 0.104161 | +0.000 | EXACT | 165/165, 165/165 |
| 20350771 | 0065125789 | 1Y | True | 0.155256 | 0.155256 | +0.000 | EXACT | 252/252, 252/252 |

```
  EXACT 8 | TIGHT 0 | LARGE 1        denominator 9 cells (3 accounts x 3 periods)
  range_match 9 of 9 TRUE           day-count residual NONZERO on 0 of 9
```

**The one LARGE is the informative cell.** `20277481` 1Y reads 252/252 linked on **both** sides with
ranges matching exactly -- so it is not our missing days and not a window disagreement. It is a genuine
calculation difference, the same class as the eleven already open at P3. Two of the three accounts agree
with BD to **nine millionths of a basis point** on all three periods.

**A distribution, never a rate.** A single "parity rate" over nine cells would report the opposite of
what the data says, exactly as it did at P1.

⛔ **STANDING SENTENCE, UNCHANGED: parity is PROBED -- n=5 from P1 plus these 3 -- with 11 open
calculation differences and a twelfth found here. The 5,309-account census is ARMED AND UNFIRED.
Nothing in this brief may be read as "parity proven."**

---

## 3. THE RECOMMENDATION: DROP SI, CAP AT 1Y

**Andrew's instruction, recorded as given:** we should not be using SI in our function at this time.
Until we have validated complete and full data end to end, **"SI" for us is not true SI.** Stay with
**1Y max** for now.

The measurements below are why that is right, and each is independent of the others -- **fixing any one
of them still leaves SI wrong.**

### 3.1 OUR SIDE CANNOT SEE INCEPTION FOR MOST OF THE BOOK -- 57% left-censored

```
  our gold twr_daily span      2024-07-08 .. 2026-08-28   (540 partitions, ~2.1 years)
  W2 census cohort                                 5,309
  cohort accounts ALREADY RUNNING on our first day  3,027   = 57.0%
```
For those **3,027 accounts the true inception is at or before 2024-07-08 and is not observable from our
data at all.** Any "since inception" we computed for them would in fact be *since our data began* -- a
number that is not wrong so much as **mislabelled**, which is worse, because it is not checkable by the
reader and it moves if we ever backfill.

By contrast the shorter periods sit comfortably inside our history:
```
  QTD  2026-07-01 .. 2026-08-28   INSIDE our span
  YTD  2026-01-01 .. 2026-08-28   INSIDE our span
  1Y   2025-08-28 .. 2026-08-28   INSIDE our span    <- the longest period we can honestly support
```

### 3.2 BD'S SI FIELD IS NOT AUTHORITATIVE -- MEASURED 3 OF 3, AND IT CONTRADICTS ITSELF

The puller reports `accounts_without_anchor: [20277481, 20265531, 20350771]` -- **all three carry no
inception, because `dim_account_xref` has no inception column at all.** With no anchor to send, the
request builder falls back to `si_probe_start = inception or q_start`. The result, on live bytes:

```
  account     BD SI range returned        SI return       QTD return      identical?
  20277481    2026-07-01 .. 2026-08-28    0.011766547     0.011766547     YES
  20265531    2026-07-01 .. 2026-08-28    0.014621106     0.014621106     YES
  20350771    2026-07-01 .. 2026-08-28    0.015645826     0.015645826     YES
```
>> **BD returns a figure LABELLED "Since Inception" that is arithmetically the requested window,
   byte-identical to QTD, with nothing raised. 3 of 3.** <<

⭐ **AND THE SAME RESPONSE CONTRADICTS THAT SI FIGURE, WHICH IS THE SHARPEST FORM OF THE FINDING.**
In the very same payload for `20277481`:
```
  calendar 2024   notHeldInPeriod=TRUE   daysHeld=0     timeWeightedReturns ABSENT
  calendar 2025   heldEntirePeriod=FALSE daysHeld=210   periodLength=251
  "SI"                                   daysHeld=42    heldEntirePeriod=TRUE
```
**BD's own data says this account did not exist in 2024 and began partway through 2025 -- while its SI
cell claims a 42-day window.** BD had the information and still returned the probe start, because we
sent one. **The SI slot reports what it was asked for, not what it knows.** A consumer reading only the
SI cell would take a 42-day return as a multi-year track record.

### 3.3 THE FAILURE IS SILENT IN BOTH DIRECTIONS

Neither half raises an error. Our side would emit a confident number for a window we cannot see the
start of; BD's side emits a confident number for a window it was handed. **A wrong SI does not look
wrong** -- it looks like a short track record or a modest return, both of which are ordinary. This is
why the answer is to stop emitting the field rather than to caveat it.

### 3.4 WHAT WE SHOULD DO

```
  EXPOSE      QTD, YTD, 1Y                       every window start is inside our data
  DO NOT      SI                                 unobservable for 57% of the book, and BD's field
                                                 is not authoritative
  ALSO NOT    any calendar year before 2025      calendar-2024 starts 2024-01-01, which is BEFORE
                                                 our first day 2024-07-08 -- same defect as SI
```
**1Y-max is the recommended rule** because it is a stable invariant that does not need re-checking as
the book changes, whereas "whatever our earliest partition allows" quietly moves.

⚠ **Note for whoever implements it: the linking module is already correct and is NOT the thing to
change.** `parity_period_returns.py` refuses rather than approximates -- it emits
`UNAVAILABLE-NO-ANCHOR` with no anchor, and `UNAVAILABLE-NO-COVERAGE` when our side opens after BD's
first return day, "never approximated by a shorter window" (its self-test arms this explicitly and
passed 27 of 27 this session). **The exposure decision is upstream of it: which periods our function
offers at all.** Do not soften the module's refusals to make an SI column populate.

### 3.5 WHAT WOULD HAVE TO BE TRUE TO RESTORE SI

Stated so the door is not closed by accident:
1. **A real inception per account, from an authoritative carrier** -- not BD's SI echo. A promising
   candidate exists in the same payload: `notHeldInPeriod=TRUE` + absent `timeWeightedReturns` on a
   calendar year is how BD signals non-existence, so a calendar-year walk could DERIVE a founding year.
   **Unvalidated -- named as a path, not a solution.**
2. **Our daily series extending to at or before that inception**, or an explicit
   `UNAVAILABLE-NO-COVERAGE` for every account where it does not.
3. **The SI request carrying that anchor**, so BD is not free to echo a probe value back.
4. **A control that fails** when an SI figure equals its own QTD figure -- the exact signature measured
   at 3 of 3 above.

---

## 4. OTHER FINDINGS FROM THIS WINDOW

### 4.1 The 00:00Z session mint did not fire

At 2026-09-01T00:07:33Z the 49F session secret's `LastChangedDate` still read `2026-08-31T00:03:47Z`;
the prior cycle had landed by 00:03:47Z. **The session is UNROTATED, not expired** -- this pull made
three successful data calls at session age **23.83 h**, so there is positive evidence of life rather
than mere absence of failure. Rotation failure and expiry are different faults with different owners,
and "the pull failed" would have merged them. Surfaced; owner is not this seat. W2 is held rather than
fired on the old session.

### 4.2 `list-secret-version-ids` cannot answer "how old is this session"

`--include-deprecated` returned **10 versions ending 2026-07-02** while `describe-secret` reported
`LastChanged 2026-08-31`. Differencing them yields **1,415 h of age** -- pure truncation artifact.
A second seat hit the same wall independently on `blackdiamond/cot/session` and got **1,979.52 h**.
**Two secrets, two different absurd numbers, and no internal signal to either that it is wrong.** Use
`describe-secret`'s `LastChangedDate`; the version list answers a different question.

### 4.3 A relayed build had five wrong operands, two budget-critical

Re-verifying the inherited W2 build at the artifact rather than relying on it found: the resume
predicate named a `pull_date=` prefix that does not exist (the real form is a bare date segment --
listing the wrong one returns 0, reads as "nothing landed", and **re-pulls the entire 5,309-account
census**); N=50 batching is structurally unreachable in the deployed code; the pinned baseline is 18
objects, not 5; the invocation and runtime figures were the two-pass numbers; and pass 2 is not
implementable in the deployed puller at all. Two operands nobody had named -- `q_end` and `pull_date` --
both had to be pinned rather than derived.

### 4.4 An instrument error caught before it was reported

A first cohort pass read 67 where the plan said 66 and looked like a data defect. It was `astype(str)`
on a null column: 826 xref rows carry a null `schwab_account_id`, and the cast renders `None` as the
string `"None"`, which enters the set as a phantom key. **The plan was right; the instrument was not.**
Recorded because the same shape will recur.

---

## 5. EVIDENCE AND METHOD

- **Our side:** `data/assets/scripts/gold/runners_49f/parity_period_returns.py` `link()` -- geometric
  linking, because our gold chain emits DAILY returns only. **Self-test 27 of 27 arms passed in this
  session before it was trusted.** Input: 271 `twr_daily` partitions `2025-08-01..2026-08-28`, **0 load
  errors**, 813 rows, all three accounts present on all 271 days.
- **BD's side:** landed bronze, joined by the ruled method -- **position finds the cell, the dates
  certify it** (BD again returned `name: null` / `type: null` on every range). Cumulative TWR from
  `timeWeightedReturns.return`, `returnAnnualized: false`.
- **Vendor cost:** 3 data calls + 1 auth for the pull; 1 auth for the earlier pre-flight. **5 calls
  total this session.** Egress authorised Andrew-direct 2026-08-31 23:4xZ, verbatim: *"all vendor egress
  is allowed tonight for all agents."*
- **Objects landed:** `blackdiamond/49f/bronze/reporting_performance/2026-08-31/` -- three files,
  `pull_date` pinned, `q_start=2026-07-01`, `q_end=2026-08-28`.
- **W2's acceptance evidence intact, measured not asserted:** the pinned before-image re-verified after
  the pull -- **18 of 18 still at pinned VersionId, 0 moved, 0 disappeared.**
- **Detail record:** `org/tier2_senior/0.4.0_DS_ClientPlatform~Y/deliverables/ADVI_BDPARITY_SPOT3_PARITY_RESULT_20260901.md`
  @ `9f0d8a84dc`.

---

## 6. WHAT THIS BRIEF DOES NOT ESTABLISH

- **Not a census.** Three accounts. The 5,309-account run is built, exercised and unfired.
- **Not an SI comparison.** SI was deliberately excluded, and section 3 is the reason.
- **Not a verdict on the LARGE cell.** It is a calculation difference with both sides fully linked;
  diagnosing it is P3's.
- **Not a claim about the mint mechanism.** The rotation did not fire; why is unmeasured here.
