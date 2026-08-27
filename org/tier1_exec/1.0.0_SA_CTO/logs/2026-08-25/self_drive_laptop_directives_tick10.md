# /self-drive laptop directives -- self-drive log, ticks 9-10 (2026-08-25 11:27Z - 11:57Z)

**Driver:** `1.0.0_SA_CTO`. **state: ARMED.** **cadence:** 30m. **cron:** `f03462e0`.
**archetype:** VALIDATE. **secondary_archetypes:** COORDINATE.
**Push state:** landed LOCAL, rides MSTR integration. Continues `..._tick8.md` @`0f38be9156`.

## SCOPE + COMPLETION (both ticks)

```
5 laptop directives [D0 D1 D2 D3 D5] of 9 live -> 12 projects   scanned 328 JSONs
open TOs: D0=4  D1=0  D2=18  D3=6  D5=0
COMPLETION: 0 of 12 | UNREACHABLE 4 | UNCHANGED SINCE TICK 2
OPEN CALLS: 0 adjudicable both ticks -- no empty pitch
```
**The register backfill that makes 4 of these readable is with `0.0.0_AB_MSTR` and has not moved.**

## THIS WINDOW WAS ALMOST ENTIRELY PRE-FIRE VERIFICATION FOR THE 12:45Z ARTIFACT

**Andrew's data condition rests on that run.** Five things were established BEFORE it exists, by four seats,
none taking another's numbers.

### !! 1. THE MISSING `date=2026-08-24` IS **NOT** THE twr DEFECT -- MY FRAMING WAS WRONG
`0.4.0_DS_ClientPlatform~G` 70294 pulled the SSM history: **the last two scheduled runs FAILED.**
```
2026-08-24 12:45:41Z  advi-49f-chain-dispatch  Failed
2026-08-23 12:45:41Z  advi-49f-chain-dispatch  Failed
2026-08-22 12:46:01Z  advi-49f-chain-dispatch  Success
CHAIN ABORT stage=a06_identity_crosswalk rc=1 -- nothing after this stage ran
```
**`a06` IS STAGE 7 OF 16; `c02_twr_daily` IS STAGE 15. TWR NEVER EXECUTED ON EITHER DAY.**
> !! **I HAD PINNED THE GAP AS "the expected residue of the twr defect the fix exists to close." IT WAS NOT.
> THE PRODUCER NEVER REACHED THE STAGE THAT WAS DOING THE DOCUMENTED WRONG THING.**
> **I ATTRIBUTED A GAP TO THE DEFECT I ALREADY KNEW ABOUT** -- real, live, top of mind, **and not this one.**
> *A known defect is the cheapest available explanation for any adjacent symptom, and it fits without being checked.*
COO's pinned expectation SURVIVES (`08-24` written, `08-25` absent); **its premise was mine and was wrong.**

### 2. THE MECHANISM, AND THE TIMING THAT SETTLES TODAY -- verified at this seat
`a06` takes `map_dates[-1]` with **no trading-day filter and no non-empty check**; the map emits empty
partitions at weekends.
```
map partition sizes (measured here):        map WRITE times (s3api, UTC):
  date=2026-08-22    4,507 B  EMPTY           08-20 13:15:06   08-21 13:15:28
  date=2026-08-23    4,507 B  EMPTY           08-22 13:15:03   08-23 13:16:07
  date=2026-08-24  776,585 B  REAL            08-24 13:15:53
  date=2026-08-25    0 objects (absent)
```
**THE MAP WRITES AT ~13:15Z; THE CHAIN RUNS AT 12:45Z -- THIRTY MINUTES EARLIER.** So the chain always sees
D-1's map, which retrodicts both aborts (Sun sees Sat's empty, Mon sees Sun's empty) and **predicts today
proceeds** (Tue sees Mon's 776 KB). **Two 4,507-byte twins are the zero-row parquet signature, visible
without opening either file.**
!! **THE TRAP IN THE OBVIOUS FIX, recorded before the TO is written:** *"read today's partition"* or *"move
the chain later"* would **INVERT that ordering** and make the chain read a map that does not exist yet.
**The code is not wrong about WHICH date it wants -- it is wrong about NOT CHECKING WHETHER WHAT IT GOT IS
EMPTY.** The minimal correct fix is a non-empty/trading-day check on the partition it already selects.
**SYSTEMATIC SUNDAY+MONDAY OUTAGE OF THE WHOLE 49F GOLD CHAIN; recurs next weekend; routed to COO for a seat.**

### 3. RISK BOUNDED -- and I corrected a second overstatement of my own
I had said today tests TWO things because stages 8-14 had not run since 08-22. **Read the 08-22 log instead
of leaving it a worry:** `CHAIN OK date=2026-08-21 wall=96.8s`, 12 consecutive `rc=0`, `c02` present.
> **THE FULL CHAIN COMPLETED THREE DAYS AGO. TODAY IS ONE VARIABLE CHANGED, NOT TWO UNKNOWNS.**
**Both corrections this window were me reasoning about the chain instead of reading its log, which was one
`s3 cp` away each time.**

### 4. THE ARMING QUESTION -- a wrong-plane near-miss that could have triggered an ad-hoc fire
`0.0.0_AB_MSTR` enumerated **137 EventBridge RULES**, materialised, with controls, and found **no 12:45
schedule** -- then **named their plane and asked instead of concluding.**
**IT IS AN EventBridge SCHEDULER SCHEDULE, NOT A RULE -- two different services, two different APIs.**
`advi-49f-gold-floor` **ENABLED** `cron(45 12 * * ? *)` UTC -> `advi-49f-gold-dispatch`, negative control
fires, 18 schedules with no `NextToken`.
!! **I HIT THIS EXACT WALL EARLIER TONIGHT AND GOT THE LOUD FORM** (`events describe-rule` -> error).
**They got the SILENT form: a clean, complete, well-controlled enumeration of the neighbouring service**, and
`12:45` appears nowhere in the rules plane, so the zero has no tell. **Their "nobody fires anything ad hoc on
the strength of this message" is what kept a convincing absence from becoming a manual run** -- which would
have replaced the scheduled artifact with one that does not count.

### 5. PRE-FIRE BASELINE, MEASURED AT THIS SEAT -- the read is now a COMPARISON
```
date=2026-08-21  data.parquet  68,779 B   rows 7,335   cols 9
  [account_id, business_date, r_net, r_gross, status, flow_convention,
   schema_version, source_pipeline, _ingested_at]
  status census:  REFUSED-NO-BMV  7,335    <- ONE VALUE, 100%
  distinct accounts 7,335 | duplicate rows 0 | business_date uniform
  D-1 account set saved to scratchpad -- TAKEN BEFORE THE D ARTIFACT EXISTS
```
**The 7,335-of-7,335 figure has been quoted all session; this is the first time I opened the file.** It
reproduces exactly. **A baseline established after the result is a description; one established before it is
a control.**
!! **THE SHAPE I WILL DISTRUST MOST IS A CLEAN SINGLE-VALUE RESULT -- because that is exactly what the BROKEN
state looks like**, and after eight hours everyone expects this fixed. *`0.4.0_DS_ClientPlatform~F`'s line:
the numbers that AGREE with expectation are the dangerous ones.*

## THE FOUR PINNED EXPECTATIONS (all published before the artifact exists)

| pinned | by |
|---|---|
| ONE partition `date=2026-08-24`; **`date=2026-08-25` ABSENT IS THE PASS** | COO 70247, from DS~G's source read |
| **ZERO PERFRP leaves at 13:20Z is the PASS**; ANY appearance is a **gate failure / RED-ALERT** | AE~G 70287 |
| trigger is a REAL schedule, ENABLED, not chained off an upstream | MSTR / DS~G / me, three reads |
| `REFUSED-NO-BMV` = 0 for accounts present at BOTH D and D-1; the other two classes **reported and explained, never driven to zero** | ruled before the artifact existed |

## RESERVED (at Andrew) -- 4, unchanged
1. `ADVI_COTKEY` key of record. 2. Register backfill (**REC: mint 4 JSONs at true state**).
3. CVO's condition-4 no-gates test. 4. The **$138.8M** inclusion call.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `pandas.read_parquet` | the 08-21 artifact | **the baseline + the read path EXERCISED, not assumed** |
| `aws s3api head-object` | 5 map partitions, UTC | **the 13:15Z write time -- the fact that settles today** |
| `aws s3 ls --summarize` | map partition sizes | the 4,507-B empty-twin signature |
| `aws s3 cp` + `grep` | the 08-22 chain log | `CHAIN OK ... wall=96.8s` -- risk bounded to one variable |
| `aws scheduler get-schedule` + neg control | the trigger | ENABLED; and the RULES-vs-SCHEDULER plane boundary |
| `directives-check.py --json` | ticks 9, 10 | unchanged; 4 unreachable |

**What failed:** two overstatements of mine, both corrected in the safer direction (the gap's cause; the
two-unknowns framing). **Gap found:** `a06` has no non-empty guard -- a systematic weekend outage of the
whole 49F gold chain, previously undiagnosed.

## Next
- **[1.0.0_SA_CTO]** **read the 12:45Z artifact** against the pinned bar; tick 11 at :13; next log tick 12.
- **[2.0.0_SA_COO]** seat the `a06` non-empty guard (NOT before 12:45Z).
- **[0.0.0_AB_MSTR]** mint the 4 project JSONs.
- **[Andrew]** 4 cards.
