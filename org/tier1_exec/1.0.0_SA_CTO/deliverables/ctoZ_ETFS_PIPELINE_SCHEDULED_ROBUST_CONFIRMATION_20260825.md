# CTO~Z -- "CONFIRM PIPELINES ARE SCHEDULED/ROBUST", 2026-08-25 ~08:1xZ

**Seat:** `1.0.0_SA_CTO~Z` | **Ask:** Andrew-direct 07:3xZ, third verb: *"(and confirm pipelines are
scheduled/robust)"*. **Primary reporter:** `0.7.0_AE_CloudOps~Z`. **This is the CTO architectural
read, offered alongside theirs, not instead of it.**
⛔ **REPORT THE POSTURE. DO NOT BUILD A MONITOR** (2026-07-28 moratorium, standing). Nothing below
proposes an alarm, an SNS topic, a freshness checker, or a gate.

---

## 0. THE ANSWER IN TWO LINES

> **SCHEDULED: YES -- and the one defect CLAUDE.md names is specifically ABSENT by construction.**
> **ROBUST: ONE STRUCTURAL EXPOSURE, and it is NOT IN AWS. The chain's first leg is a LOCAL WINDOWS
> TASK ON THIS WORKSTATION, and its failure mode is a GREEN RUN THAT SERVES STALE.**

---

## 1. THE CHAIN, MEASURED -- every leg, its trigger, its plane

| # | leg | trigger | plane | state |
|---|---|---|---|---|
| 1 | L1 Bloomberg pull | `OPAL_BBGTML_daily_pull` **07:00 local = 11:00Z** | ⚠ **LOCAL WINDOWS TASK, THIS BOX** | Ready · LastRun 08-24 07:00:01 rc=**0** · NextRun 08-25 07:00 |
| 2 | bronze+silver holdings/netassets | `etfs-netassets-daily` `cron(0 22 * * ? *)` | AWS EventBridge | **ENABLED** |
| 3 | gold parquet **+ platinum JSON** | `etf-positioning-producer-daily` `cron(0 13 * * ? *)` | AWS EventBridge | **ENABLED** |

**EventBridge census: 137 rules materialised** (auto-paginated, filtered CLIENT-SIDE -- never a
`--query` over a paginated list). 9 ETF-named. **ZERO rules at hour 11** -- which is not a gap, it is
the positive confirmation that leg 1 is not in AWS at all.

---

## 2. ✅ SCHEDULED -- AND THE NAMED DEFECT IS ABSENT BY CONSTRUCTION, NOT BY LUCK

CLAUDE.md's ad-hoc/scheduled rule: *"a pipeline whose only trigger is another pipeline's success has
no schedule and is a defect."*

**Every leg above carries its own `cron(...)` or its own clock. Not one is triggered solely by an
upstream success.** And the place where that defect would most naturally have appeared -- the
gold -> platinum hand-off -- was **designed out**, in the handler's own words
(`etf_positioning_gold.py:lambda_handler`, verbatim):

> *"ONE invocation, BOTH stages, in order. Two Lambdas with an ordering edge would make stage 2 a
> pipeline whose ONLY trigger is another pipeline's success -- which is the defect CLAUDE.md's
> ad-hoc/scheduled rule names. One invocation, sequential."*

**Verified on the APPLIED plane, not the tree** (Rule 22a):
```
Handler   etf_positioning_gold.lambda_handler   -> calls publisher.run(publish=True) in-process
Runtime   python3.11   Timeout 120s   Memory 512MB   (NOT the 256/30 yang default -- Rule 5 satisfied)
ENV       OPAL_ETFS_PUBLISH_GRANT = 1     <- the publisher's live-write gate is APPLIED
          ETFS_BUCKET             = opal-data-etfs
Layers    pandas-pyarrow-requests-layer:1 · opal-trading-calendar-layer:1
Package   2 members, both raw-sha identical to their repo files (0.4.0_DS_ClientPlatform~Z measured)
```
⭐ **`OPAL_ETFS_PUBLISH_GRANT=1` is the one I most expected to find missing and it is present.** The
publisher defaults to a FULL DRY RUN without it -- so had it been unset, the scheduled fire would
have run, logged, returned success, and **published nothing**, indefinitely. It is set. **Stated
because a green run that publishes nothing is exactly this pipeline's silent-failure shape.**

---

## 3. ⚠ ROBUST -- ONE EXPOSURE, AND IT IS THE ONE ANDREW SHOULD BE TOLD ABOUT

### 3.1 The exposure

**Leg 1 is a local Windows scheduled task on this workstation.** Legs 2 and 3 fire in AWS regardless
of this box. **Leg 3's INPUT does not.**

`etf_positioning_gold.py:_bbg_partition_exists` requires a `bbg/{as_of}/` landing and **SKIPS any
date lacking one.** So:

```
this box asleep / logged out / terminal dead at 07:00 local
   -> no bbg/{today}/          -> leg 3's own guard SKIPS the day
   -> platinum is NOT rewritten -> the portal serves YESTERDAY's book
   -> the 13:00Z run reports SUCCESS. No error. No exception. A green run.
```
>> **THE FAILURE IS INVISIBLE FROM THE AWS PLANE ENTIRELY.** Every AWS instrument -- the rule fired,
the Lambda returned 200, the manifest wrote -- reads healthy. **The only tell is an artifact whose
`data_as_of` did not advance, and nothing in AWS is looking at that.** <<

⛔ **THIS IS NOT A REQUEST TO BUILD A DETECTOR.** The moratorium stands and I am not proposing one.
**It is a posture statement: the daily continuity of a client-facing product currently depends on
one workstation staying awake, and that dependency should be a KNOWN one rather than a discovered
one.** The remedy class -- if Andrew ever wants it -- is *moving leg 1 into AWS*, which is a route
decision (his ordering: canonical routes first, monitoring only once the route is settled), **not a
monitor.**

### 3.2 Two facts that bound how much today's evidence proves

**(a) THE 13:00Z SCHEDULE HAS NEVER FIRED. Today's is the FIRST.**
```
CloudWatch log streams for etf-positioning-producer: 4 total
   2026-08-24 22:56 · 23:00 · 23:12      2026-08-25 04:45
   -> NO stream at any 13:00Z. All gold/platinum objects to date are AD-HOC.
gold/ = 11 objects, newest written 2026-08-25T04:44-04:53Z (the Andrew-authorised overnight re-run)
platinum/etfs/positioning_data.json  generated_at 2026-08-25T04:53:48Z, data_as_of 2026-08-24
```
**So "the producer works" is currently grounded on AD-HOC runs only.** Per CLAUDE.md an ad-hoc run is a
legitimate QA instrument and an illegitimate production claim. **The 13:00Z fire today (~4h50m from
this writing) is the acceptance event for leg 3, and until it passes, leg 3 is SCHEDULED-BUT-UNPROVEN.**

⛔ **AMENDED 2026-08-25 ~08:3xZ -- THE SENTENCE ABOVE IS TRUE AND TOO COARSE, and the coarseness hides
the load-bearing half. `2.0.0_SA_COO~Z` measured the provenance directly and it is sharper than
"ad-hoc":**
```
served platinum @04:53:51Z (126,863 B)  -> NO Lambda invocation, in ANY of 11 etf-named log groups
                                           in the 04:45-05:00Z window
three OTHER object versions             -> correlate to a producer stream TO THE SECOND (pos control)
=> THE ARTIFACT ON THE CLIENT-FACING PAGE WAS PRODUCED LOCALLY, FROM THIS WORKSTATION.
   Not merely "not the schedule" -- NOT THE LAMBDA AT ALL.
```
**WHY I MISSED IT AND IT IS A GRAIN ERROR, NOT A WRONG FACT:** I read CloudWatch LOG STREAMS, an
instrument that answers *"did the schedule fire"* -- the question I asked. COO correlated OBJECT
VERSIONS against INVOCATIONS, which answers *"what made these bytes."* **Both reads are sound; only
one is on the provenance plane. A true statement at the wrong grain still terminates the inquiry.**
▶ **CONSEQUENCE, RULED: rung 2 is produced by INVOKING THE DEPLOYED LAMBDA, never by a local run.** A
local run proves the CODE and cannot prove the DEPLOYMENT -- and the deployment is what runs at 13:00Z
on a client-facing page.
▶ **AND WITH `0.4.0_DS_ClientPlatform~Z`'s D5 finding (the publisher hashes a body containing its own
`generated_at`, so D5 CAN NEVER SKIP), the acceptance criterion is on the `name` FIELD, NEVER on
byte-identity.** The 13:00Z run ALWAYS writes; the only question is whether what it writes is correct.
**A differing sha at 13:00Z is the EXPECTED state, and an engineer expecting a no-op will read a
perfectly correct write as a failure.**

**(b) THE FEEDER IS THE HEALTHY HALF, and it is worth saying because it is the contrast.**
```
silver/holdings/  73 objects, materialised.  SIX consecutive days present:
   08-19 · 08-20 · 08-21 · 08-22 · 08-23 · 08-24   -- every one written at 22:00:1xZ
   -> cron(0 22) is firing reliably, to the second, including weekends.
bbg/  THREE partitions only: 08-20 (7 obj... see below) · 08-21 (16 obj) · 08-24 (7 obj)
   bbg/2026-08-25/  ABSENT -- CORRECT at 08:08Z; the 11:00Z pull has not run yet.
   positive control bbg/2026-08-24/ = 7 objects   negative control zzz-no-such-prefix-9999 = 0
```
⚠ **FILED FOR `0.7.0_AE_CloudOps~Z`, NOT ADJUDICATED HERE: `bbg/2026-08-24/` carries 7 objects
against `bbg/2026-08-21/`'s 16.** 08-21 was a scheduled landing; 08-24 was written by the overnight
ad-hoc re-run. **Whether 7 is the complete set or a partial one is AE's leg, and it bears directly
on whether today's 11:00Z landing should look like 7 or like 16.** I am not calling it a defect --
**a count difference between an ad-hoc and a scheduled landing is expected until someone says what
the scheduled shape is.**

---

## 4. ⛔ AN INSTRUMENT OF MINE FAILED DURING THIS MEASUREMENT, GREEN, AND I CAUGHT IT ONLY ON THE CONTROL

My first partition probe used `d.get('KeyCount', 0)` on `list-objects-v2` output. It returned:
```
bbg/2026-08-25/   objects: 0      <- TRUE
bbg/2026-08-24/   objects: 0      <- FALSE. It holds 7.
```
**`KeyCount` is ABSENT from every response** (the CLI strips it when it auto-paginates and merges),
so `.get('KeyCount', 0)` returned a well-formed, confident **0 for every prefix in the bucket,
including live ones.** Re-measured on `len(Contents)`; both controls then discriminated.

>> **I caught this ONLY because I ran a positive control on a prefix I already knew was populated.**
Had I probed only `bbg/2026-08-25/` -- the prefix I actually cared about -- the answer would have
been RIGHT, for a REASON THAT WAS BROKEN, and I would have reported a true fact on a dead
instrument. **This is CLAUDE.md's own named class (`objects=0` on unwritable filenames; a retrieval
failure that returns a VALUE) and I reproduced it inside the very report where I quote the rule.**
**A missing dict key and a real zero are byte-identical through `.get(k, 0)`.** <<

---

## 5. WHAT I AM **NOT** CLAIMING

- **I am not claiming leg 1 will fire today.** It is `Ready` with `NextRun 08-25 07:00` and rc=0
  yesterday. That is a scheduler state, not a future.
- **I am not claiming the 13:00Z fire will pass.** It has never run. See 3.2(a).
- **I am not claiming `bbg/` completeness.** See 3.2(b) -- AE's leg.
- **I have not exercised leg 3.** No ad-hoc fire from this seat; the overnight one is not mine to
  cite as production evidence.

---

## 6. GROUNDING

| claim | instrument | denominator / control |
|---|---|---|
| 137 rules, 9 ETF, zero at hour 11 | `aws events list-rules`, auto-paginated, **client-side filter** | 137 materialised, `NextToken` absent; 17 rules carry no schedule at all |
| producer schedule + target | `list-targets-by-rule` | `cron(0 13)` -> `arn:...:function:etf-positioning-producer` |
| applied Lambda config | `get-function-configuration` | APPLIED plane, not the tree |
| both stages, one invocation | `etf_positioning_gold.py:lambda_handler` @ `10750a9a7c` | source-confirmed, quoted verbatim |
| schedule never fired | `logs describe-log-streams --order-by LastEventTime` | 4 streams, none at 13:00Z |
| silver continuity | `s3api list-objects-v2`, materialised | 73 objects, 6 consecutive days |
| bbg partitions | `s3api list-objects-v2`, **`len(Contents)` after the KeyCount failure** | pos control 08-24 = 7, neg control `zzz-no-such-prefix-9999` = 0 |
| local task state | `Get-ScheduledTask` + `Get-ScheduledTaskInfo` | 7 OPAL tasks enumerated |

**Times UTC.** Local-vs-UTC pinned explicitly: `2026-08-25T08:08:20Z` = `04:08:20-0400`, so
**07:00 local = 11:00Z** -- derived from a measured offset, never assumed, and never read off
`aws s3 ls` (which renders LOCAL with no marker).

-- `1.0.0_SA_CTO~Z`
