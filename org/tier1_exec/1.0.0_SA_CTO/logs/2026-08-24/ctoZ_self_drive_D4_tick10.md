# /self-drive D4 -- ticks 9-10 log (2026-08-24 22:47Z-23:16Z) -- state: ARMED

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier: `org/XXX.md` CTO row · continues `ctoZ_self_drive_D4_tick8.md`.
**Log cadence:** every 2 ticks; next at tick 12 or DONE.

## SCOPE + COMPLETION

```
SELF-DRIVE D4 -> 1 directive -> 2 project(s) [ETFS_INGEST, ETFS_POSITIONING]   device: sitez
  claim scan: 324 project JSONs -> 2 PRD-path claims (dedup: 1 already a member)
  ETFS_CANON: DEFERRED out of the completion set (Andrew ~22:12Z)
  open TOs in scope: 6      denominator: 1 of 9 live directives
  COMPLETION TEST: NOT DONE -- 0 of 2 complete.  REACHABLE 2 / UNREACHABLE 0.
```
Register lag unchanged (row still `{ETFS_CANON: scoping, ETFS_POSITIONING: active}`, `open_tos: 5`) --
MSTR~Z's edit, and now a DEFERRAL to record rather than a member to add.

## THE ROUND'S RESULT THIS WINDOW: THE PIPELINE RUNS END TO END

`bronze -> silver -> gold -> platinum`, **first time ever**, all four tiers exercised in one evening.

```
22:00:11Z  bronze   trueshares/{DIVZ,IDVZ}/bronze/holdings/20260824/*.csv   29 + 44 rows, raw issuer CSV
22:00:17Z  silver   silver/holdings/2026-08-24.parquet   187 rows, FOUR funds (was 114, two)
22:52:58Z  DEPLOY   etf-positioning-producer + opal-trading-calendar-layer:1   (197->198, 14->15)
22:56:44Z  gold     opal-data-etfs/gold/{book,holding}/date=2026-08-21/   <- ANDREW'S C2 HOME
23:00:45Z  platinum platinum/etfs/positioning_data.json   status published, shape_check CLEAN
```

**`run_class: adhoc` is stamped in BOTH stage manifests** -- my binding condition, satisfied on the
first real artifacts, on a field that existed nowhere in the producer before tonight.

**And the schedule gap the PRD names as its own load-bearing defect is CLOSED:** my own census
re-run, same instrument, sound before -> **136 -> 137 rules, 7 -> 8 ETF-named**,
`etf-positioning-producer-daily cron(0 13 * * ? *) ENABLED`. Verified THREE rungs deep, because
`list-rules` answers only the first and a rule with no target or no permission reads identically in
it: the rule exists · it TARGETS the function · the function's resource policy PERMITS that rule to
invoke it, SourceArn pinned to the specific rule.

## AND THE OUTPUT THAT WOULD HAVE BEEN MISREAD AS A FAILURE

Gold read `silver/holdings/2026-08-21.parquet`, not tonight's, and reports `holding_rows 114 ·
books_shell 2` -- **DIVZ/IDVZ still shells after the capture succeeded.**

**THAT IS THE CORRECT ANSWER.** `2026-08-24` is a **MONDAY**; the producer resolved the trading
calendar and selected T-1 = **Friday 08-21** (`trading_days_behind: 1`). CLAUDE.md's NEVER#1 worked
example running live. Tonight's partition is consumed tomorrow, when T-1 = Monday 08-24.

**The layer I ruled for is visibly earning itself in its first run:** `silver/holdings/` carries
CALENDAR-day partitions -- `2026-08-22` (Sat) and `2026-08-23` (Sun) both exist -- and the producer
**skipped both to reach Friday.** A naive `sorted(keys)[-1]` would have silently consumed Sunday.
Broadcast to six seats BEFORE anyone could file a false outage off it.

## RULINGS THIS WINDOW

- **TO-5 packaging: MINT THE LAYER, not a 5th `trading_calendar.py` copy.** Rung 5 ran first and
  **nearly answered wrong**: `mdpf-gold-calendar-deps` LOOKS like the answer and carries
  `exchange_calendars` + `dateutil` -- **ZERO `trading_calendar` entries across 1,507**. A name match
  would have closed the question falsely. Grounds: Rule 3 (inline vendoring needs approval, the
  layer is the default) · rung 4 (native primitive) · NEVER#1's ONE-frontier mechanism against four
  independently-editable homes. **Migration of the existing four NOT authorized -- separate cell.**
- **TO-5 AC3: ad-hoc discharges it, and I ADDED `AC7`** (first SCHEDULED fire observed at its
  invocation record) rather than read AC3's silence. Plus the condition neither seat had stated:
  **`platinum/etfs/positioning_data.json` is a LIVE SERVED KEY** carrying DE~Z's whole evidence base.
- **`run_class` derivation: from the INVOCATION EVENT, and the DIRECTION is load-bearing --**
  discriminate POSITIVELY for `scheduled` so an unrecognised shape falls to `adhoc`. Written the
  other way it is equivalent on enumerated shapes and OPPOSITE on every shape nobody enumerated.
- **CONV-1** on DS~Z's correct mid-build STOP: **the encoding is a property of the FEED, DECLARED
  per source and ASSERTED by the parser, never inferred from a census** -- "no `N` seen today" makes
  every row's meaning a function of its cohort.
- **The 13:00Z interaction, with a CORRECTION to the ordering argument it arrived with:** the retry
  defect does NOT triple the served harm -- **platinum is ONE KEY OVERWRITTEN**, so three publishes
  are the same wrong value three times. What it multiplies is INVOCATIONS and MANIFESTS (**a reader
  counting manifests stops counting fires**). **RULED: provenance fix FIRST** (client-facing wrong
  value outranks a noisy invocation record). **And AC7 amended by me: discharged on the invocation
  record AND the artifact, disagreement = PASS-WITH-FINDING** -- because the marshal defect would
  make MY OWN criterion's single oracle report RED on work that succeeded.

## ANDREW-DIRECT ~23:0xZ -- THE PROVENANCE RULING

VERBATIM: *"all downloaded information from the providers platforms (trueshares and pathfinder)
should have some kind of 'as of' field... that needs to be what is used for any date stamping on
provenance. it is fine to track metadata of when we've updated data or performed operations on it,
but that is a very different figure... maintained from bronze ingestion onward."*

**Ratifies Z-S16 sovereignly and WIDER than my spec reading** -- the provider's as-of IS the
provenance stamp, and the obligation is a chain property from bronze, not the silver cell I scoped.
**The serving end ALREADY implements it** (`generated_at` vs `data_as_of` / `data_date` /
`prior_date`, distinct and correctly named); the gap is purely the VALUE, at the source.
**AND IT HAS A CLOCK: invisible today because DIVZ/IDVZ are shells; TOMORROW'S 13:00Z FIRE MAKES IT
LIVE ON THE SERVED SURFACE** for two of four funds, silently -- no error, no byte-count change, a
plausible-looking date.

## CORRECTIONS AGAINST MYSELF THIS WINDOW

- **My surprise item led with the UNREMARKABLE half.** CVO~Z measured **50 leaves in that bucket
  collide 3+ times**; "three keys share a name" would have generated fifty false siblings. Facts
  right, emphasis wrong -- **the error with nothing to recompute.** Re-framed @ff58c2ce86.
- **I self-assigned channel id `-Z-S24`; CVO~Z had minted it the same minute.** Pulled pre-commit;
  allocated id is `Z-S25`. Ids belong to the channel owner.
- **DE~Z's diff replaces my own evidence and I adopted it over mine:** I showed the as-of separation
  EXISTS by censusing field NAMES; **they showed it HOLDS UNDER AN ACTUAL REPUBLISH -- 2,384 leaf
  fields, exactly 1 differs (`/generated_at`).** Mine could not have failed; theirs could.
- **A python text-mode JSON write CRLF-ified two project files** (41/41 and 62/62 whole-file diffs on
  a 3-line and a 2-line change). Caught by checking numstat before commit -- the banked lesson
  working rather than being re-learned.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| directives-check / to-check | scope + open TOs | 2 projects, 6 TOs |
| comp-find (-i, --name) | GICS site · run_class census · env reads · as-of surface | run_class 0 of 5 files pre-tonight; the as-of surface **0 hits / 11 files** on Positioning |
| comp-pipescript io | yang-generate-positioning | writes `json/positioning/positioning_data.json` -- the twin |
| raw aws (rail-checked) | token-walked rules/lambdas/layers/keys; both-tool plane pin; head-object | every census in this log |
| safe-commit | 6 commits ticks 9-10 | all PASS |

## Blockers

None at this seat. **Zero cards at Andrew.** He is visual-smoking on `localhost:5175` (DE~Z's server,
DEV @d43b88c5, hands-off broadcast sent) -- and **he cannot tell from the page which publish he is
seeing**, because no as-of is rendered on Positioning. That limitation is DE~Z's open finding,
arriving as a live cost in front of him tonight.
