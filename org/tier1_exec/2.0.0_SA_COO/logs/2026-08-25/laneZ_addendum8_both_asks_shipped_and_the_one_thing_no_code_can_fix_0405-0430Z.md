# 2.0.0_SA_COO~Z — ADDENDUM 8: both asks shipped, and the one thing no code can fix (0405–0430Z)

**archetype:** COORDINATE · **secondary:** VALIDATE, DIAGNOSE, SCRIBE
Continues `laneZ_addendum7_...md` @6797e7985b. **~53 commits this session.** **Zero crons, whole session.**

---

## 1. ✅ DELIVERED — BOTH OF ANDREW'S ~03:2xZ ASKS ARE IN THE RUNNING BYTES

```
@e37c75ad44  ask 1  per-security performance -- reads the bbg-testpull archive. ZERO vendor calls.
@7ba77cba29  ask 2  sub-asset map SUMS TO THE BOOK on all four (DIVZ was publishing 99.22 vs 99.80)
DEPLOY #8    04:19:59Z   sha 631ELit6nuAD0+J3w9n9J12OqVWDMQxRGj1X+fCzg00=
```
✅ **VERIFIED AT MY SEAT ON THE PACKAGE, NOT ON THE REPORT** — downloaded, member read:
`60,899 B · sha256 35d3a35f04d1db90 · _load_backfill_history 2 · drop_duplicates 1 · bookSet 2 ·
SETTLES 1 · POSITIVE CONTROL "def load_history" 1 · NEGATIVE CONTROL 0`. **Both asks present, both
controls firing, so the counts are real presence and real absence.**
⚠ **AND THE DEPLOY BEAT MY OWN CORRECTION BY ONE SECOND: I routed deploy #8 at 04:18Z naming ONLY
ask 1, amended it to TWO commits at 04:20Z, and AE~Z had applied at 04:19:59Z. It carried both
because THEY BUILT FROM HEAD, not from the commit my message named. That was their discipline, not my
routing** — and it is the same lesson as `@4c234af208`: **a message is a snapshot of what the sender
knew, and this fabric commits faster than it messages.**

---

## 2. ⛔ THE THING NO CODE CAN FIX — AND EVERY SEAT AGREES ON IT

`3.0.0_SA_CVO~Z` measured what a deploy would actually see, instead of assuming the backfill closes
the windows:
```
bbg-testpull archive   109 objects token-walked  LATEST = 2026-08-20, UNIFORM across ALL 109
daily partitions       3 of 3                    08-20 · 08-21 · 08-24-carrying-08-21-rows
lib/trading_calendar                             2026-08-24 IS A TRADING DAY
=> 2026-08-24 EXISTS IN NO SOURCE.  set(need).issubset(have) FAILS ON EVERY WINDOW.
```
>> **ONE MISSING DAY AT THE FRONT GATES EVERY WINDOW REGARDLESS OF HOW MUCH HISTORY SITS BEHIND IT.
>> 5.6 YEARS OF DEPTH DOES NOT FILL `1D`.** <<
```
deploy #8 alone   -> 0/8   NECESSARY, NOT SUFFICIENT
11:00Z pull alone -> 0/8   the code that reads the archive would not be running
BOTH              -> 8/8   and only then
```
⛔ **SO ANDREW'S PERFORMANCE VIEWS AT 13:00Z HANG ENTIRELY ON `OPAL_BBGTML_daily_pull` — A LOCAL
SCHEDULED TASK ON THIS WORKSTATION WHOSE FAILURE PRODUCES NO ERROR.** Every line of code this fabric
wrote tonight is necessary and none of it is sufficient.
⭐ **CVO~Z stated it as a FALSIFIABLE PREDICTION with *"if 8/8 renders, my read is wrong and I want to
know."* That can be settled at 13:00Z by anyone in one measurement, without re-deriving the argument.
Most of tonight's open questions should have been shaped that way.**

---

## 3. ⭐ WHY `as_of` SITS ON A DATE WITH NO HISTORY — THE MECHANISM, AND IT IS A ONE-OFF

```
resolve_as_of()    steps back ONLY when the bbg PARTITION IS ABSENT   -> "does bbg/{D}/ exist?"
compute_returns()  needs EVERY TRADING DAY IN THE WINDOW              -> "does HISTORY cover D?"
```
**Two predicates, nothing syncing them. `bbg/2026-08-24/` did not exist for most of the night —
MSTR~Z's re-key created it at ~02:5xZ, advancing the as_of frontier onto a date nobody had pulled
history for.** ⛔ **The act six of us celebrated as the delivery is the act that emptied the return
windows.**
✅ **IT IS A ONE-OFF AND `resolve_as_of` MUST NOT BE "FIXED".** `0.4.0_DS_ClientPlatform~Z` tested my
call rather than adopting it, and their census proves the invariant is real:
```
bbg/2026-08-20/   history dated 08-20 .. 08-20   SELF-CONSISTENT
bbg/2026-08-21/   history dated 08-21 .. 08-21   SELF-CONSISTENT
bbg/2026-08-24/   history dated 08-21 .. 08-21   <- the RE-KEY, the only one that lies about itself
```
**The normal pull writes the partition AND its history in one run, so the two predicates advance
together BY CONSTRUCTION. A COPY carries the partition without carrying fresh history.**
▶ **RULE EARNED: a manual re-key of a `bbg/{date}/` partition either CARRIES HISTORY COVERING THAT
DATE, or is ANNOUNCED as advancing the as_of frontier onto an uncovered day.** *CTO~Z's re-key was
correct and self-documenting; this consequence is two inference steps away from it.*

---

## 4. ⛔⛔ THE SECOND TAUTOLOGICAL SELF-COMPARISON IN ONE FILE, IN ONE NIGHT

`3.0.0_SA_CVO~Z` found the resolver LISTS `bbg/{date}/` and NEVER OPENS the manifest inside it — real,
and nobody else had noticed. **Their proposed remedy — check `as_of` vs `history_window_end` — is
void, at source:**
```
etf_daily_pull.py:243   "history_window_end": asof_key       <- THE AS-OF, WRITTEN TWICE
   08-20 True · 08-21 True · 08-24 FALSE  <- FALSE only because a hand edit touched ONE copy
```
```
:66-70   asof vs expected            SAME EXPRESSION   <- the tripwire, found ~00:5xZ
:243     history_window_end = as_of  SAME VALUE        <- found 04:26Z
```
>> **`etf_daily_pull.py` HAS A HABIT: IT WRITES DERIVED COPIES INTO THE MANIFEST AND THEY READ
>> DOWNSTREAM AS INDEPENDENT SIGNALS.** `expected` reads as an oracle; `history_window_end` reads as
>> coverage. **Both are copies and both are invisible from the output.** <<
⛔ **AND THIS ONE IS NASTIER THAN THE TRIPWIRE: THE DIVERGENCE MADE IT LOOK *MORE* CREDIBLE.** A
tautology nobody has seen differ is at least suspicious; this one had a live counter-example in front
of everyone — **manufactured by a two-carriers edit, masquerading as proof the comparison works.**
✅ **A real coverage check reads the `history_topup` DATE COLUMN. An observation of the payload cannot
be a copy of the key.** **Recorded, NOT built** — the moratorium, and DS~Z declined to propose it too.

---

## 5. ⭐ THE PATTERN OF THE NIGHT, THIRD INSTANCE — AND IT IS NOT ANY ONE SEAT'S

```
DE~Z   finding: SECTOR_INDICES != ECONOMY_ORDER    TRUE   remedy: emit ECONOMY_ORDER   UNBUILDABLE
me     finding: the alarm never fired              TRUE   remedy: (would be) a checker BANNED
CVO~Z  finding: the resolver never opens the file  TRUE   remedy: check hw_end         TAUTOLOGY
```
>> **EVERY FINDING REAL; EVERY REMEDY FAILED A TEST ITS FINDING NEVER HAD TO PASS. And all three were
>> caught by THE OWNER OF THE SURFACE THE REMEDY TOUCHED. That is the routing working: the finder
>> cannot price the remedy, and the owner can.** <<

---

## 6. ⛔ MY DEFECTS THIS STRETCH

| # | defect | caught by |
|---|---|---|
| 33 | **Routed deploy #8 naming ONE commit** when ask 2 had landed 90 seconds earlier — a build from my message ships half of Andrew's request | reading DS~Z's next message |
| 34 | **My 04:16Z diagnosis order put "is the code deployed?" SECOND**, behind the 11:00Z pull — **I named landed≠running as a standing fact two hours earlier and then ordered a diagnosis that skipped it.** Anyone following it hunts a Windows task with an undeployed commit in front of them | measuring the live sha myself |

⭐ **AND THE PART THAT IS NOT A DEFECT BUT IS THE ROLE: at 04:11Z I measured that
`0.4.0_DS_ClientPlatform~Z` had received 78 MESSAGES SINCE 03:00Z, 18 IN 30 MINUTES — one every ~100
seconds to the single executor of both asks, and I had sent 5 of the last 18.** **CTO~Z asked why
there were zero commits; that was why.** A blocking-only comms freeze went on at 04:11Z; **both asks
were built by 04:17Z.**

---

## 7. STATE FOR 11:00Z / 13:00Z

```
CODE       both asks DEPLOYED and verified on the package. Nothing further to ship.
11:00Z     OPAL_BBGTML_daily_pull, LOCAL WINDOWS TASK, SILENT ON FAILURE. The ONLY thing that can
           create 2026-08-24 history. THE WHOLE DELIVERY HANGS HERE.
           CHECK: bbg/2026-08-24/history_topup.parquet contains rows DATED 2026-08-24.
           *** NOT "the file exists" -- IT EXISTS NOW AND CARRIES 167 ROWS DATED 08-21. ***
13:00Z     settles CVO~Z's prediction either way. Discriminate on run_class: scheduled.
DIAGNOSIS ORDER IF EMPTY:  1 live CodeSha256  ->  2 history dated 08-24  ->  3 only then the code.
```
**Phase 2 (deep backfill) HELD on Andrew's 04:09Z qualification pending a measured sizing.**
**Phase 1's real gap is 58 of 167 securities (~15,950 rows), not "all" — 65% smaller than scoped.**
