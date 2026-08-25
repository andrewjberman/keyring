# 0.4.0_DS_ClientPlatform~Z -- ANDREW-DIRECT DEFECT B: SALXX display name (0745-0830Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Window

Relaunch 07:45Z on Andrew's 07:3xZ direct instruction ("fix this and only this, verify visually,
confirm pipelines scheduled/robust, commit, push / prod-deploy, all necessary logging").
Two defects across the fabric; **DEFECT B (the SALXX display name) is this seat's**, assigned by
`0.0.0_AB_MSTR~Z`. Defect A (sub-categories panel) is `0.4.0_DE_ClientPlatform~Z`'s and is not
touched here.

## Current State

**DEFECT B's CODE IS DONE, COMMITTED, PUSHED AND DEPLOYED. Rung 2 (the served artifact) is NOT
discharged: the live key still carries the raw strings because nothing has invoked the new code
yet.**

- **Commit `2e9737af49`** -- `data/etfs/scripts/gold/etf_positioning_publisher.py`, +68/-1.
  **ON `origin/SITEZ`** (ls-remote `refs/heads/SITEZ` = `e4b241a80f`; `git branch -r --contains
  2e9737af49` -> `origin/SITEZ`). Pushed by `0.0.0_AB_MSTR~Z` per LD-0367, not by this seat.
- **DEPLOYED**: `etf-positioning-producer` CodeSha256 `631ELit6nuAD0+...` -> `p/mc7hvScGyYxxMK9...`
  at 2026-08-25T08:19:03Z. Applied by `0.7.0_AE_CloudOps~Z`; **verified independently at this seat
  on the deployed artifact, not on the deployer's report** (see Verification).
- **NOT PUBLISHED**: `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json` still
  LastModified 2026-08-25T04:53:51Z, 126,863 B, SALXX still
  `STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS`. "Deployed" is true and misleading alone.
  **2b (ad-hoc INVOKE of the deployed Lambda) is `0.7.0_AE_CloudOps~Z`'s and is the only remaining
  step before Andrew can see the fix.** This seat deliberately did NOT invoke: two concurrent runs
  would race a client-facing key and the loser's bytes are indistinguishable afterwards.

### What was built

A serving-tier, ticker-keyed `DISPLAY_NAME_OVERRIDES` + `_display_name(ticker, raw)` in
`etf_positioning_publisher.py`, applied at the holdings serve step. Two entries: `SALXX` ->
`State Street U.S. Government MMKT` (Andrew's verbatim string, a ruling), `FXFXX` ->
`First American Treasury Obligations Fund` (**DERIVED BY THIS SEAT, NOT HIS WORD** -- the raw
carries a meaningless maturity date on a money-market fund; approved by `2.0.0_SA_COO~Z` as
derived-awaiting-confirm and labelled as such in the code, the commit message and every message).

**Home = the platinum publisher, per Rule 17b (display naming is serving-tier).** Confirmed by
`0.0.0_AB_MSTR~Z` (8599) and `1.0.0_SA_CTO~Z` as Rule 17b APPLIED rather than a new ruling.

### Why a curated map and not a transform (four prior remedies were falsified)

```
raw     STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS
target  State Street U.S. Government MMKT
```

Title-casing yields `State Street Inst U.S. Government Mmkt Admn Class` -- wrong three ways at once.
No string function maps raw to target; the edit is EDITORIAL. **The generic alternative was tested
against real data and rejected on evidence**: a trailing-date strip works on 1 of 169 names today
and would silently corrupt a bond name the day one lands, because maturity IS a bond's identity.

**The property the four dead remedies lacked:** a ticker ABSENT from the map returns the INCOMING
NAME unchanged. `seed-etf-classifications.py:62` is `.get(ticker, ticker)` -- it falls back to THE
KEY, so a miss writes the literal `"SALXX"` and presents as success. Same idiom, opposite blast
radius.

## Verification

**The acceptance oracle (Z-S48, amended by its disarm owner `2.0.0_SA_COO~Z` from 4 names to 2).**
Built the artifact TWICE from the SAME gold partition in the same minute, fix ON and fix OFF, so
upstream movement cannot confound the diff:

```
CONTROL A  fix-OFF build == the SERVED artifact field-for-field (generated_at excluded)
           -> nothing upstream moved; the delta is mine alone
ORACLE     ROWS CHANGED 4 of 187 | FIELDS TOUCHED ['name'] | book-level diffs 0 of 4
             DIVZ SALXX + IDVZ SALXX -> State Street U.S. Government MMKT
             PFDE FXFXX + PFOE FXFXX -> First American Treasury Obligations Fund
           2 distinct names of 169 tickers; 183 of 187 ROWS byte-identical.
           BOTH GRAINS STATED -- COO~Z's oracle is in tickers, my measurement in rows, and a
           later reader diffing "2" against "4" would file a false discrepancy.
MUTANT     re-point the fallback at the KEY -> damages 8 of 8 unlisted controls.
           A control that COULD have failed and did not.
NEGATIVE   BP PLC / GSK PLC / MPLX LP unchanged (acronym companies, Z-S48's open product fork).
           JPM / MRVL / VZ unchanged -- outside Andrew's instruction.
```

**Deployed-artifact verification (Rule 22a CODE layer), done at this seat:**

```
downloaded the DEPLOYED package; recomputed sha256(b64) == reported CodeSha256 p/mc7hvS...
   -> the artifact inspected IS the artifact deployed, not a same-named one
MEMBERS 2 (etf_positioning_gold.py, etf_positioning_publisher.py)
   both raw-sha256 IDENTICAL to their repo files
   no trading_calendar.py -> nothing shadows opal-trading-calendar-layer:1
CONTENT 4/4 probes PRESENT incl. the CALL SITE; negative control zzz_no_such_token_9999 ABSENT
=> CTO~Z's stated arithmetic acceptance test for the deploy PASSES.
```

## Corrections issued against my own work

1. **"the two name maps share ZERO keys" was measured over ONE key space and argued as if it were
   the only one.** There are two: holding tickers (169, intersection 0) and BOOK CODES (4,
   intersection 4 -- **and 3 of 4 ALREADY DIVERGE**). Corrected before either exec ruled on it.
2. **"deploy-first inverts D5 from a reverter into a no-op" is FALSE.** `generated_at` is inside
   the hashed body, so **D5 can never fire** -- exercised both ways (two builds, same gold, 1s
   apart: shas differ; with `generated_at` removed: equal). The ORDERING conclusion is unchanged
   and stronger (13:00Z writes unconditionally). `1.0.0_SA_CTO~Z` ratified the correction and
   bounded it to ONE file: the source pattern it was adopted from keeps its wall-clock in the
   MANIFEST, so the defect was introduced in translation, not inherited. **The error ran in the
   direction of describing the system as SAFER than it is, inside a hazard warning.**
   `2.0.0_SA_COO~Z` had amplified the original form to six seats and self-corrected in parallel.

## Findings FILED, not fixed (scope fence: two defects, not a third)

| Finding | Evidence | Routed to |
|---|---|---|
| Book-name divergence, 3 of 4 | served `Polen Dividend Income ETF` vs shared map `Opal Dividend Income ETF`, which calls ITSELF served canon. Client-facing branding. | `2.0.0_SA_COO~Z`; escalated to Andrew by `0.0.0_AB_MSTR~Z` |
| D5 is inert while its docstring asserts it is active | `generated_at` inside the hashed body; two senior seats cited it as a live guard in a decision | `2.0.0_SA_COO~Z` |
| 3 stale PRE-FIX copies of the publisher | `.runtmp_to5/{pkg,dep/pkg,mf/pkg}/etf_positioning_publisher.py`, all 22022 B vs the real 26133 B. Untracked, not gitignored. A build from them ships old code and looks normal. INERT tonight (AE~Z's zip verified correct). | `2.0.0_SA_COO~Z`, `0.7.0_AE_CloudOps~Z` |
| `build_package.py` lists 4 members; the live package is 2 | a packaged `trading_calendar.py` would shadow the layer | ratified as a DEPLOY RULING by `1.0.0_SA_CTO~Z`; the 4-vs-2 disagreement itself filed |
| "EventBridge has ZERO rules at hour 11" is FALSE | 9 rules fire in hour 11 (8 with hour field exactly `11`, +1 at `11,21`). The zero is a `cron(0 11 ` PREFIX count. **The true and stronger finding: ZERO rules match bbg/bloomberg/terminal at ANY hour** (137 rules materialised client-side; positive control `etf` = 8). | `0.7.0_AE_CloudOps~Z` (owns the deliverable), CTO~Z, COO~Z, MSTR~Z |
| `comp-pipescript` has no `etfs` pipeline | `--pipeline` choices are bd/inf/cot/mdpf/advi only; a comp-tool coverage gap is a defect per CLAUDE.md | noted, unrouted |

## Pipelines scheduled/robust -- this seat's leg only

```
etf-positioning-producer-daily   cron(0 13 * * ? *)  ENABLED   <- a REAL ScheduleExpression
etfs-netassets-daily             cron(0 22 * * ? *)  ENABLED   <- writes silver/holdings
resolve_as_of() on the deployed path, CALLED (not assumed): as_of 2026-08-24,
   frontier 2026-08-25, trading_days_behind = 1  -> HEALTHY T-1, NEVER#1 resolved
silver/holdings newest 2026-08-24 written 22:00:17Z
   (aws s3 ls renders 18:00:17 LOCAL with no marker; pinned with head-object -- 4h offset)
```

So today's silver 2026-08-25 lands ~22:00Z, AFTER the 13:00Z gold fire; on today's inputs 13:00Z
should resolve the same as_of that rung 2's evidence is about. **Stated as a PREDICTION, not a
measurement** -- the 13:00Z input state does not exist yet. The name fix is as-of independent, so a
byte difference at 13:00Z is not a regression.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | -i NAME_OVERRIDE, -i ETFS_GOLD_BUCKET, -i opal-data-etfs, --name etf-positioning | PASS | Found the estate's existing ETF_NAME_OVERRIDES (BUILD LADDER rung 2) and the producer TF. -i used per Rule 21's case-sensitivity law. |
| comp-find | --name pattern under infra | WARN | Measured zero over 7844 files; the tool NAMED the remedy (-i) itself and the -i content form found it. Guarded-zero behaviour worked as documented. |
| comp-estate | --resource etf-positioning-producer | FAIL | "no chain references" -- the ETF positioning thread is not in the coverage resolver. |
| comp-aws | comp-aws etf-positioning-producer | FAIL | Not a valid form; comp-aws takes derive/score/snapshot/..., not a resource name. |
| comp-pipescript | io ... --pipeline etfs | FAIL | **GAP: no etfs pipeline exists.** Answered the consumer question with comp-find instead. |

**What worked:** comp-find's band classification separated the real ETF_NAME_OVERRIDES definition
from doc/test noise in one call, which located the estate's existing mechanism and made the
"different universe" argument possible.
**What failed:** comp-estate --resource and comp-aws both dead-ended on this producer.
**Gap found:** comp-pipescript has no etfs pipeline, so "who consumes this gold?" -- exactly the
completeness question a gold-script edit should ask -- has no comp-tool. Answered with comp-find
plus a live s3 ls: only the two producer files reference the ETF gold bucket, so the publisher is
its sole consumer and the fix is complete.

## MCP traffic

~28 messages read and ACKed (7 at load + the rest in-window). Significant: MSTR~Z 8577 (relaunch
brief + fence), MSTR~Z 8599 (publisher home CONFIRMED), COO~Z 8609 (Z-S48 scope RATIFIED + oracle
amended 4->2), COO~Z 8669 (rung 2 ordering ADOPTED from my inversion), COO~Z 8707 (the served
artifact was never produced by the Lambda), CTO~Z 8713 (D5 correction ratified + bounded to one
file; build_package.py deploy ruling). Sent 8 dispatches, 25/25 DELIVERED.

## Blockers

**None on this seat.** Rung 2c is SEQUENCED behind `0.7.0_AE_CloudOps~Z`'s 2b invoke, which is a
named owner performing an assigned act -- not a blocker, and not a gate I manufactured. The
verifier is written and staged; it runs in seconds on the republish.

## Next Steps

1. **[0.7.0_AE_CloudOps~Z]** 2b: invoke the DEPLOYED Lambda ad-hoc (not a local run) so the served
   artifact is produced by the production code path for the first time in this product's life.
2. **[0.4.0_DS_ClientPlatform~Z -- me]** 2c on republish: report (i) the two target rows, (ii) that
   the DEPLOYED Lambda produced the bytes (version + invocation correlation), (iii) the Z-S48
   oracle re-run ON THE SERVE.
3. **[0.2.0_DT_PortfolioAnalytics~Z]** Rung 3, the production render Andrew actually opens. They
   hold a BEFORE capture showing both defects on the live page.
4. **[Andrew]** the FXFXX target string, as a DERIVED string awaiting his confirm.
5. **[Andrew]** the Polen-vs-Opal book-name branding divergence, escalated by MSTR~Z.

---

## ADDENDUM 08:3xZ -- RUNG 2 IS NOW DISCHARGED

Appended rather than rewritten: the body above was true when committed (`a03a8fc710`) and this
record should show the sequence, not a tidied end state. **What changed: `0.7.0_AE_CloudOps~Z`
invoked the deployed Lambda at 08:30:31Z, and it published at 08:31:06Z.**

```
SERVED  platinum/etfs/positioning_data.json  08:31:06Z  126,809 B  data_as_of 2026-08-24
   DIVZ SALXX / IDVZ SALXX -> State Street U.S. Government MMKT
   PFDE FXFXX / PFOE FXFXX -> First American Treasury Obligations Fund
ORACLE RE-RUN ON THE SERVE (vs the 04:53:51Z pre-fix document, not vs a local build)
   ROWS CHANGED 4 of 187 | FIELDS TOUCHED ['name'] | book-level diffs 0 of 4
   183 of 187 rows byte-identical | VERDICT exactly-4-and-only-name TRUE
```

**PRODUCER ATTRIBUTION PROVEN ON CONTENT, NOT ON A CLOCK** -- the discriminating step, because
timestamp proximity degrades exactly when two writes land close together:

```
Lambda log:  [publisher] built 126809 B, sha256 98650407cd829225...
I hashed the served object myself: sha256 = 98650407cd829225...   IDENTICAL, size IDENTICAL
run_class=adhoc  -> correctly marked a QA run, not production
as-of resolution IN THE LAMBDA: expected_frontier=2026-08-25, as_of=2026-08-24,
   trading_days_behind=1  -> independently reproduces my pre-run prediction
```

This also closes `2.0.0_SA_COO~Z`'s 8707 finding for the first time in the product's life: the
served artifact is now one its own producer made.

**NOT discharged: RUNG 3** (the rendered page), `0.2.0_DT_PortfolioAnalytics~Z`'s. Noted to them
that Defect B needs NO promote -- it is a DATA change on an already-served key -- so the two
defects reach the page through different mechanisms and should not be reported as one gate.

**Observation for `0.7.0_AE_CloudOps~Z`'s posture leg, filed not chased:** the run took 36,847 ms
of a 120,000 ms timeout and 264 MB of 512 MB. Rule-5 sizing holds, but the measured wall time is
~2.5x the TO contract's stated 15.0 s worst case (Init 2,297 ms is only part of it). Headroom is
smaller than the contract implies.

## ADDENDUM 2 -- MY OWN HOUR-11 COUNT WAS ALSO INCOMPLETE

The findings table above records "9 rules fire in hour 11". **That number is mine and it is short.**
`1.0.0_SA_CTO~Z` re-derived rather than accepting a correction they already agreed with, and found
**TEN**: `access-anomaly-scanner-schedule` is `cron(0 * * * ? *)` -- **a WILDCARD hour field is
invisible to a literal-hour matcher**, and mine tested `"11" in hour_field.split(",")`. So my
matcher handled the list form (`11,21`) that CTO~Z's exact-match missed, and missed the wildcard
that theirs caught. `0.7.0_AE_CloudOps~Z` layered it further: **9 / 10 / 19** depending on whether
you count exact + list, plus every-hour, plus `rate()` rules.

>> **THE SAME PATTERN-FRAME CLASS BIT THE ORIGINAL CLAIM AND BOTH CORRECTIONS, ONE LEVEL DOWN EACH
   TIME.** I caught the prefix-vs-field error and then made a field-vs-*expression-language* error.
   Parsing the field was the right move and it was not sufficient: a cron hour field is a small
   language (literal, list, range, step, wildcard) and I enumerated two of its five forms. <<

**The operative conclusion is unchanged and is the reason the exact count does not matter:** the
hour-count framing should be RETIRED, not repaired. The claim that goes to Andrew is hour-independent
and unfalsifiable by any of these numbers -- **ZERO rules match `bbg|bloomberg|terminal` at ANY hour
(137 materialised; positive control `etf` = 8, so the matcher discriminates).** All four seats
converged on that wording.

**Banked:** two seats agreeing on a number is not the number being right -- CTO~Z and I agreed on 9
and both were wrong. **Re-derive a MEASUREMENT, not a FINDING** (CTO~Z's formulation): the first can
surface a defect the agreeing seats share, which is exactly what happened here.

## ADDENDUM 3 -- THE 13:00Z READ: PROCEDURE AND EXPECTED VALUES (durable carrier)

`2.0.0_SA_COO~Z` asked for a NAMED owner and a DURABLE carrier for the 13:00Z read, naming
`0.7.0_AE_CloudOps~Z`. **The OWNER is theirs. This section is the CARRIER for the part that is mine:
the artifact being checked is my producer's output, and the EXPECTED VALUES are the thing that turns
a green result into a false alarm when nobody wrote them down.**

**Anyone live after 13:00Z can run this. No re-derivation needed.**

```bash
# (a) did the scheduled run happen at all?
aws logs describe-log-streams --log-group-name /aws/lambda/etf-positioning-producer \
    --order-by LastEventTime --descending --max-items 3 \
    --query "logStreams[].[logStreamName,lastEventTimestamp]" --output text
# (b),(c),(d) the artifact
aws s3api head-object --bucket opal-data-portal-v2 \
    --key platinum/etfs/positioning_data.json --query "[LastModified,ContentLength]" --output text
aws s3 cp s3://opal-data-portal-v2/platinum/etfs/positioning_data.json ./chk.json --quiet
```

**EXPECTED VALUES -- read these BEFORE looking, so the result cannot be rationalised after:**

| # | Check | PASS looks like | The trap |
|---|---|---|---|
| a | a new log stream | `run_class=scheduled`, NOT `adhoc` | today's 08:30Z stream was ad-hoc PROOF; do not mistake it for the scheduled fire |
| b | `generated_at` | advances past `2026-08-25T08:31:05Z` | if unchanged, the rule did NOT fire -- the artifact simply persists and **looks fine** |
| c | SALXX / FXFXX | `State Street U.S. Government MMKT` / `First American Treasury Obligations Fund` | the deployed code carries the map, so a REGRESSION here means the deploy was reverted, not that the fix failed |
| d | `data_as_of` | `2026-08-24` **or** `2026-08-25` -- BOTH are correct | see below; this is the one most likely to be mis-filed |

⛔ **(d) IS THE FALSE-ALARM TRAP AND IT CUTS BOTH WAYS.** `_bbg_partition_exists` SKIPS any date with
no `bbg/{as_of}/` landing, and the 11:00Z pull is a LOCAL WINDOWS TASK on this workstation.
- `data_as_of` = **2026-08-25** -> the 11:00Z pull landed; healthy.
- `data_as_of` = **2026-08-24** -> **NOT automatically a defect.** Silver `2026-08-25` is written by
  `etfs-netassets-daily` at `cron(0 22)` = 22:00Z, which is AFTER 13:00Z, so **on today's cadence
  the gold run legitimately resolves 2026-08-24.** Measured: `resolve_as_of()` returned
  `as_of=2026-08-24, frontier=2026-08-25, trading_days_behind=1` -- **HEALTHY T-1.**
- **The discriminator is not the date, it is `trading_days_behind` and whether `bbg/2026-08-25/`
  exists.** Check `aws s3 ls s3://opal-data-etfs/bbg/` before calling anything stale.
⛔ **NEVER#1 applies with full force here: do not call this pipeline stale on a wall-clock age.**

⚠ **AND THE EDGE LAGS THE TRUTH BY UP TO 5 MINUTES.** `/api/general/*` uses `opal-api-general-5min-cache`
(DefaultTTL 300; the object sends no overriding `Cache-Control`). **A page still showing the old
figures 60 seconds after the run is EXPECTED, not a failure.** Read the S3 object for truth.

⚠ **RELATED EXPECTED-VALUE, `1.0.0_SA_CTO~Z`'s, recorded here so it is not lost:** if the 11:00Z
universe extension covers ICT/MER, the IDVZ panel goes **96.82 -> 99.51, NOT -> 100.** Anyone
expecting 100 reads a completely successful fix as a remaining defect, and the natural next move --
forcing an issuer's book to total 100 -- would be manufacturing a number on a client-facing page.

**NO MONITOR, NO ALARM, NO FRESHNESS CHECKER** (2026-07-28 moratorium). This is a procedure for a
person to run once, not machinery. **I have armed nothing and this section arms nothing.**

### CARRIER PRECEDENCE -- THIS SECTION IS SUBORDINATE, NOT PRIMARY

⛔ **`1.0.0_SA_CTO~Z` (msg 8947) is right and it corrects the section above: TWO CARRIERS WITH NO
NAMED PRIMARY DIVERGE.** A session-log section **is not queried by anybody**; `to-check.py --all` at
startup is what a successor actually runs.

```
PRIMARY    the 13:00Z TASK ORDER on 0.7.0_AE_CloudOps~Z  -- the OWNER and the ASSIGNMENT live there
SECONDARY  this section -- the CRITERIA and EXPECTED VALUES only
```

**If the two ever disagree, the TO wins.** This section carries no assignment and never did; it
exists so the criteria are not re-derived, and it should be COPIED INTO the TO rather than pointed
at from it -- **a cross-reference between two carriers is the divergence surface, not the fix.**

⚠ **And I created that surface by writing this before checking whether a primary existed.** Filing
the criteria felt like discharging the risk; it actually added one. Same shape as
[[naming a falsifier is not discharging it]] -- **writing a thing down reads as handling it.**

⭐ **CONVERGENCE NOTE, stated so priority is not mis-attributed:** `1.0.0_SA_CTO~Z` reached the
`data_as_of` false-skip independently and their message (084625Z) PREDATES mine (~0850Z). Two seats,
same conclusion, neither borrowed from the other -- **but they got there first and the record should
say so.**

### CORRECTION TO ADDENDUM 3's CHECK (d) -- MY OWN BRANCH WAS WRONG ON MECHANISM

Addendum 3 said: *"`data_as_of` = 2026-08-25 -> the 11:00Z pull landed; healthy."* **THAT IS FALSE
AND IT IS THE LOOSE DIRECTION, which is the dangerous one for a reference document: it would wave
through a genuine anomaly as healthy.**

**The mechanism, read at source rather than recalled** (`etf_positioning_gold.py:337-345`
docstring): *"`as_of` comes from the DATA (the newest silver/holdings partition that exists)."*

```
The 11:00Z local task writes  bbg/{date}/     -- a GATE on as_of, via _bbg_partition_exists
etfs-netassets-daily cron(0 22) writes  silver/holdings/{date}.parquet  -- the SOURCE of as_of
MEASURED, UTC-pinned via s3api (NOT `aws s3 ls`, which renders local with no marker):
   silver/holdings/2026-08-22.parquet   2026-08-22T22:00:14Z
   silver/holdings/2026-08-23.parquet   2026-08-23T22:00:15Z
   silver/holdings/2026-08-24.parquet   2026-08-24T22:00:17Z
```

>> **I CONFLATED THE TWO FEEDS.** The 11:00Z pull cannot advance `as_of`; it only gates it. Silver
`2026-08-25` does not exist until ~22:00Z, **nine hours after the 13:00Z fire** -- so at 13:00Z the
newest silver partition IS 2026-08-24 and `as_of` = 2026-08-24 **necessarily**, not merely
acceptably. <<

**CORRECTED (d) -- adopt `2.0.0_SA_COO~Z`'s form, which is tighter than mine and correct:**
```
data_as_of == 2026-08-24   PASS. UNCHANGED IS THE EXPECTED VALUE.
data_as_of == 2026-08-25   ANOMALY -- it means a silver partition landed ~9h early.
                           Not necessarily bad, but it is NOT self-evidently healthy and
                           must be explained, not waved through.
```
⚠ **BOTH the original framing and my correction of it were wrong, in OPPOSITE directions.** COO~Z's
first wording would have manufactured a false SKIP; mine would have licensed a false PASS. **A
too-loose expected-value is not the safe error -- it is the one that cannot fail, and a criterion
that cannot fail is not a criterion.** The mechanism, read at source, settles it and neither of our
recollections did.

### CHECK (d), FINAL FORM -- RELATIVE, NOT DATED. THIS SUPERSEDES EVERY EARLIER (d) ABOVE.

⛔ **`1.0.0_SA_CTO~Z` (msg 9000): every (d) above is written as A DATE, and this carrier exists
BECAUSE the obligation may outlive today's seats.** `data_as_of == 2026-08-24` is true today and
**silently wrong on any later fire** -- the frozen-constant class, right when written and nothing
announcing the transition.

**THE INVARIANT, which the source-read makes structural rather than coincidental:**
```
silver/holdings/{D}.parquet lands ~22:00Z ON DAY D    (measured 22:00:14 / :15 / :17, three days)
the producer fires           13:00Z ON DAY D+1         -- NINE HOURS BEFORE that day's silver
=> at ANY 13:00Z fire the newest silver partition is ALWAYS the previous trading day
```

**FINAL (d) -- use this, not any dated form:**
```
PASS      data_as_of == the last TRADING day before the fire date   (trading_days_behind == 1)
ANOMALY   data_as_of == the fire date -- a silver partition landed ~9h early. Explain it;
          do not wave it through and do not file it as a defect either.
NEVER#1   trading_days_behind == 1 is HEALTHY T-1. No wall-clock staleness call, ever.
```
⭐ **Stated relatively it survives a weekend, a market holiday, and a successor reading it in
October** -- and it makes NEVER#1's T-1 default hold BY CONSTRUCTION here rather than by
coincidence, because the 9h gap is a property of the two schedules, not of today's dates.

⚠ **ATTRIBUTION, corrected -- and it matters because a reader sent to the wrong form gets the
failing one.** I wrote "adopt COO~Z's form." **Wrong pointer.** The corrected (d) is
**`1.0.0_SA_CTO~Z`'s RULING (msg 8944) on `2.0.0_SA_COO~Z`'s original (d)**. COO~Z's ORIGINAL posed
*"advance or SKIP"* as the only two outcomes and is the form that would have fired falsely.
**"Take COO~Z's wording" would have sent AE~Z to the SUPERSEDED version** -- a pointer error that
delivers exactly the defect the correction removed. Three forms now exist and only this one is live:
```
COO~Z original (superseded)  "advance, or the bbg guard SKIPPED"     -> false SKIP on a healthy fire
DS~Z addendum 3 (superseded) "08-25 is healthy"                      -> false PASS on an early land
CTO~Z ruling 8944, RELATIVE  as_of == last trading day before fire   -> LIVE. USE THIS.
```
