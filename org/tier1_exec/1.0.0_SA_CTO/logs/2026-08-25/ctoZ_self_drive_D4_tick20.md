# /self-drive D4 -- ticks 19-20 log (2026-08-25 01:40Z - 02:08Z) -- state: ARMED

**archetype:** COORDINATE · **secondary:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick18.md`.
**This window contains the first PROOF of the night and the closest call this seat has had: a fifth wrong framing, drafted at full reach, killed by one measurement before it was sent.**

## SCOPE + COMPLETION

```
D4 "ETF positioning variant" -> device SITEZ · open TOs 6
  members: ETFS_CANON(scoping) · ETFS_POSITIONING(active) · +ETFS_INGEST(claimed, active)
  COMPLETION TEST: NOT DONE -- 0 of 2 member projects `complete`.  REACHABLE 2 / UNREACHABLE 0.
  denominator: 1 of 9 live directives · 0 ahead of origin/SITEZ · 0 open calls at Andrew
```

## ⭐ THE PROOF -- `0.7.0_AE_CloudOps~Z`, msg 6909

`build_tables()` verified PURE (zero I/O), called TWICE with **one variable changed** and everything
else identical (`as_of=2026-08-21`, same universe / netassets / characteristics / fund_daily / history):

```
A  silver/holdings/2026-08-21.parquet  114 rows  [PFDE,PFOE]   -> DIVZ 0 · IDVZ 0 · PFDE 90 · PFOE 24   2 full, 2 SHELL
B  silver/holdings/2026-08-24.parquet  187 rows  [all four]    -> DIVZ 29 · IDVZ 44 · PFDE 90 · PFOE 24  4 FULL, 0 shell
```
⭐ **FRAME A REPRODUCES THE LIVE PORTAL EXACTLY. That control is what makes it proof and not a sixth
story -- the apparatus was shown able to display the failure, and frame B filled anyway.**
**Nothing written, nothing published.** Cause settled: the holdings partition is the binding
constraint. **Not characteristics, not classification, not `is_cash`, not the vocabulary.**

## ⛔ AND I ALMOST SHIPPED FRAMING #5 -- THE MOST DANGEROUS ONE YET

Drafted, addressed to six seats, unsent:
> *"Gold correctly served T-1. Friday IS Monday's right answer. NEVER#1. The pipeline is healthy and
> the fabric is one step from 'fixing' a working pipeline."*

**FALSIFIED IN ONE CALL** against `lib/trading_calendar.py` -- the file NEVER#1 names as the ONE
frontier definition:
```
expected_last_trading_day(2026-08-24 13:00Z) -> 2026-08-24   <- gold's OWN expected at its run
gold served                                     2026-08-21   <- ONE TRADING DAY BEHIND IT
```
⛔ **The previous four wrong framings would have shipped a WRONG NUMBER. This one would have STOPPED
THE FIX ENTIRELY -- while quoting a NEVER rule to do it.** The reflex that caught it is the one I
have been pressing on every other seat all night; it is the only reason it did not go out.

## ⭐ MEASURING IT FOUND THE STRUCTURAL DEFECT UNDER TONIGHT

```
lib/trading_calendar.py   expected = TODAY, if a trading day    (date-only, no close-awareness)
etf_daily_pull.py:68      expected = LOCAL today + BDay(-1)     = YESTERDAY
```
>> **TWO DEFINITIONS OF `expected`, ONE TRADING DAY APART, BY CONSTRUCTION, EVERY DAY.** The L1 pull
**can never reach** the calendar's frontier -- it targets T-1 while the calendar names T.
⛔ **SO GOLD'S `resolve_as_of` GUARD SITS PERMANENTLY 1 BEHIND ITS OWN `expected`, AND THEREFORE
STRUCTURALLY CANNOT REPORT A 1-DAY LAG.** 2-behind is the first state it could ever detect.
**NEVER#1's harm in the mirror: not a false outage -- a guard DESENSITISED BY CONSTRUCTION**, which
is why this has been true for weeks with nobody seeing it.
⚠ `expected_last_trading_day(2026-08-25 02:05Z)` returns `2026-08-25`, a session that has not opened.
**Date-only per its own docstring. Defect-or-contract is UNDETERMINED and deliberately NOT ruled.**

## ⭐⭐ THE THREE FINDINGS OF THE NIGHT ARE ONE CLASS

```
is_cash            ONE FIELD, TWO INTENTS       skip-the-pull  vs render-as-asset-class  0.4.0_DS_ClientPlatform~Z
silver partition   ONE NAME,  TWO CLOCKS        operation date vs data as-of             0.7.0_AE_CloudOps~Z
`expected`         ONE WORD,  TWO DEFINITIONS   calendar T     vs pull T-1               this seat
```
**Two intents sharing one carrier -- a boolean, a filename, a variable. Rule 24(iii) was written for
value enums, and every defect tonight is it, one layer down.**

## ▶ DELIVERY -- UNCHANGED, NOW MEASURED RATHER THAN INFERRED

```
11:00Z  L1 writes bbg/2026-08-24/   (NO CODE)
13:00Z  gold: expected=08-25 -> picks 08-24 -> reads silver/holdings/2026-08-24.parquet
        (187 rows, 21073 B, ON DISK NOW)   -> DIVZ 29 · IDVZ 44 · PFDE 90 · PFOE 24
```
**`:1375` (the run_date-keyed partition = Andrew's 23:0xZ provenance ruling violated at the filename
layer) is REAL, is the root, and is NOT TONIGHT** -- it changes the contract every consumer reads and
is not between Andrew and four filled books.
**`0.4.0_DS_ClientPlatform~Z`'s sequencing point now has a DEADLINE rather than a window: SALXX
renders the instant the books fill, ~13:15Z.** Theirs was also the correction that their own 01:50Z
`alloc_cash=0.0000` was measured on the POST-FIX frame and reported in the present tense -- **a shell
book misclassifies nothing today.**

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| python + lib/trading_calendar | `expected_last_trading_day` at 3 instants | **08-24 at gold's run vs 08-21 served -- killed my framing** |
| sed over lib/trading_calendar.py | the function's contract | date-only, no close-awareness |
| aws s3 ls | bbg/ and silver/holdings/ partitions | bbg trading-day T-1 · silver calendar-day T (weekend partitions present) |
| directives-check | scope + completion | NOT DONE 0 of 2 |

## Blockers

None at this seat. **Zero cards at Andrew.** `@0c03c359f2` deploy-or-hold is `2.0.0_SA_COO~Z`'s
sequencing call (my block lifted on `0.4.0_DE_ClientPlatform~Z`'s measurement that all three portal
render sites SUM `cash + fixed_income`). Act 2 held · L1 not before 04:00Z · artifact intact.
