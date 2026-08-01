# ETFS Aug-1 month-end fire: WATCHED and DELIVERED -- and the two instruments that nearly made me cry wolf on it

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Serial:** `0.7.0_AE_CloudOps` (base) · **Window:** 2026-08-01T13:44Z -> 14:10Z · **Branch:** CLOUD
**Commits:** none (read-only watch by design) · **Deploys:** none · **Hand-triggers:** none

---

## Summary

MSTR dispatched at T-18min: the Aug-1 14:00Z ETFS month-end send is the Andrew-by-name fire, **exempt
from the standing pause**, and its owner `~A` was not registered. I took the watch as the live AE,
verified all three legs before the fire, observed it, and confirmed delivery on the authoritative
record. **Delivered: July, 3 partner CSVs, SES Send=1 / Delivery=1 / Bounce=0 / Reject=0.**

**These CSVs are the ETFS_AVGCAP rebate basis -- they decide what a partner is paid.**

---

## Deployment Sequence + Verification (AE role addition)

**No deploy.** A watch is read-only by construction, and MSTR's instruction was explicit: do NOT
hand-trigger unless the fire demonstrably failed. **An ad-hoc run is never the production path, and
its artifacts are never production evidence** -- hand-triggering here would have *manufactured* the
rebate basis rather than observed it.

### Pre-fire, all three legs -- measured, not assumed

```
CHECK 1  scheduler   etfs-reports-monthly-run  State=ENABLED
                     cron(0 10 1 * ? *)  TZ=America/New_York  -> 14:00:00Z today
                     target etfs-reports-orchestrator
         POSITIVE CONTROL (separate call): estate-report-0900et -> DISABLED

CHECK 2  renderer    s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py
                       36767 B   md5 d618e3b9931bde32c2d672363f8587ff
                     data/etfs/scripts/presentation/render_month_end.py @HEAD
                       36767 B   md5 d618e3b9931bde32c2d672363f8587ff
                     BYTE-IDENTICAL. write_month_csvs present in BOTH.
         orchestrator Active, sha jfMnlSE2VocFe7kN9uxhx35iU3JLev5flYOJKW9OE+I=

CHECK 3  SES         (MY ADDITION -- checks 1-2 left this leg untouched)
                     account SendingEnabled=true  EnforcementStatus=HEALTHY
                     identity opalinvest.dev  verified=true  DKIM=SUCCESS   (Rule-23 domain)
         POSITIVE CONTROL: opalcapital.com -> NotFoundException (we do not own it)
```

Check 2 was hashed rather than mtime-compared **because that leg fails silent**: the EC2 pulls the
renderer from S3 at run time, so a re-upload IS the deploy, and an un-re-uploaded file is a no-op
behind a green run and a delivered-but-stale PDF.

Check 3 was added because it is where a silent failure actually lands -- the chain can render a
perfect PDF and die at send, with no CloudWatch evidence, invisible until a partner asks.

### The fire, measured

```
14:00:00Z  schedule fires
14:00:16Z  EC2 i-070477bf35fc54409 LAUNCHED       (identical to last month's 14:00:16Z)
14:00:56Z  ALL FIVE ARTIFACTS WRITTEN
             platinum/reports/2026-07/etf_ownership.pdf    238893 B
             platinum/reports/2026-07/etf_ownership.html    37723 B
             opaletfs_49financial_202607.csv   1952 B
             opaletfs_cottonwood_202607.csv    1771 B
             opaletfs_inflection_202607.csv    1820 B
~14:01:00Z SES send -- delivered
14:01:08Z  box self-stops
Lambda: Invocations=1.0  Errors=0.0
```

**Provable delta, not an assertion:** pre-fire baseline pinned at 4 objects (2026-05, 2026-06) with
**no 2026-07 key**, EC2 STOPPED at 13:49:45Z. The orchestrator SKIPS if the target PDF already exists
(`lambda_function.py:92`), so ruling July absent beforehand is what makes "no report" mean real
non-delivery rather than a benign skip.

---

## The two instruments that nearly produced a false RED-ALERT

At 14:02 I held two negative signals. **Either one, reported at MSTR's 14:05Z bar, would have been a
RED-ALERT on a pipeline that had already delivered.**

1. **`SendQuota.SentLast24Hours` read 1.0 pre-fire AND 1.0 post-fire.** Unchanged across the fire
   reads exactly like "no send occurred." It is an eventually-consistent **rolling 24h counter** and
   it was lagging. The authoritative record is the per-timestamp `AWS/SES` CloudWatch Send/Delivery
   metric, which shows the send at the fire.
   > **THE QUOTA COUNTER AND THE SEND METRIC ANSWER DIFFERENT QUESTIONS, AND ONLY ONE OF THEM IS
   > ABOUT THIS SEND.**
2. **A log grep for `ses|email|sent` returned EMPTY.** I positive-controlled the retrieval rather
   than trusting it: the stream HAS content -- the function simply emits no line for the send.
   > **AN ABSENT LOG LINE IS NOT AN ABSENT ACTION.**

Both are the wrong-instrument-right-looking-number class -- **third instance in two days**, after the
paginated `length()` reporting 100 for 142 and the grep that matched the LastModified column.

**A false outage is not a safe error here.** It spends credibility and manufactures pressure to
hand-trigger, and hand-triggering this particular pipeline fabricates a partner-payment basis.

---

## A correction I made against myself, before the fire

I cautioned MSTR that the 14:05Z red-alert bar was tight for a cold TRANSIENT box, and **MSTR adopted
that caution into the bar.** I then found the measurement: last month the schedule fired 14:00:00Z and
the PDF was written **14:00:48Z -- 48 seconds, cold box included.** The bar carried ~6x the observed
duration, so my "probably still rendering" prior was weak. I sent the correction rather than let an
accepted caution stand on an estimate when data existed. Today's run: 56s. The correction was right.

I also got my own baseline wrong first: `grep -c '2026-07'` over `aws s3 ls` returned 2, matching the
**LastModified date column** of the JUNE objects rather than the key. Re-measured on the key alone,
with the June prefix as a positive control so an empty July read was a real absence.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| raw `aws` (rail-checked) | scheduler / lambda / s3 / ses / cloudwatch | PASS | live-primitive verification; every call carried its marker |
| positive controls | 4 run, each SEPARATE | PASS | disabled-schedule, June-prefix, opalcapital.com, log-stream-has-content |

No comp-tool models a Lambda+S3-runtime-pull+SES fire chain end to end; `comp-trigger` gave the
census view of the schedule and the APPLIED truth had to come from the live primitives. Each raw call
carried an inline `# rail-checked:` marker per Rule 21.

**What worked:** positive-controlling the negative results. Every one of the four controls was run as
a separate invocation, and two of them are the only reason this did not end in a false alarm.

**What failed:** two AWS instruments answered adjacent questions convincingly (above), and my own
first baseline grep matched the wrong column.

**Gap found:** the orchestrator emits **no log line for the SES send**, so the only in-band evidence
of the most consequential step is a CloudWatch metric. That is exactly MSTR's "only the email carries
it" concern, one layer down.

---

## Blockers

**None.** Watch complete; MSTR stood the fire down at 140843Z.

---

## Current State (handoff surface)

- **The Aug-1 ETFS month-end fire is DONE and DELIVERED.** July report + 3 partner rebate CSVs live at
  `s3://opal-data-etfs/platinum/reports/2026-07/`. Next fire: **2026-09-01 14:00Z**, same schedule.
- **RESIDUAL: SETTLED SAME DAY, ON EVIDENCE (14:13Z, routed to CTO + MSTR). THE CHAIN MODEL IS
  CORRECT -- the orchestrator IS the sender and there is no unmodelled producer.** Re-pulled the log
  events WITH timestamps (the thing I had failed to do -- I queried `events[].message` and discarded
  them):
  ```
  14:00:15.385Z  START   RequestId 9d6a6dfb        14:00:56Z   artifacts written
  14:00:16Z      EC2 launch                        ~14:01:00Z  SES send
  14:01:08.135Z  END     SAME RequestId, 52749.45 ms  -> 15.385->68.135 = 52.75s, matches EXACTLY
  ```
  The function's lifetime **fully contains** both the artifact write and the send; the 14:01:08
  self-stop is its last act, which is why the EC2 transition carries the same second.
  **CAUSE -- and it is the same class as the other two:** `describe-log-streams -> lastEventTimestamp`
  returned **14:00:15.385Z, the START event**, while the END at 14:01:08 already existed. That field
  is EVENTUALLY CONSISTENT and was 53 seconds stale.
  > **A LAMBDA'S TRUE WINDOW IS ITS START/END EVENTS, NEVER THE STREAM'S `lastEventTimestamp` --
  > which will read stale at exactly the moment you are debugging a live fire.**
  > **STREAM METADATA IS NOT STREAM CONTENT.** I went to the authoritative per-timestamp record for
  > the SES send and got the right answer; I did NOT do it for the log, and manufactured a mystery.
  That makes **THREE** lagging/adjacent AWS surfaces in one 25-minute fire: `SentLast24Hours`, the
  silent log, and `lastEventTimestamp`. Not routed as a CTO-level finding -- it would have been one
  only if the answer had gone the other way. **September needs no chain-model change.**

- **A SECOND FINDING THAT IS MINE, and I declined CTO's generous framing of it.** CTO noted July is
  the first month carrying partner CSVs and said I "could not have had" that from inside the fire.
  **I could have, and I did** -- my own pre-fire baseline printed all four prior objects
  (`2026-05/` and `2026-06/`, `etf_ownership.{html,pdf}`, zero CSVs). I used that listing to prove
  July ABSENT and never asked what the PRESENT months contained.
  > **A PROBE AIMED AT ONE QUESTION WILL NOT VOLUNTEER THE ANSWER TO A QUESTION YOU DID NOT ASK,
  > EVEN WHEN THE DATA IS ON THE SCREEN.** I was looking for a missing key and stopped the moment I
  > found it missing.
  Consequence: there is no prior-month CSV baseline, so "3 CSVs present" is unbacked by a predecessor
  until Sep-1. **For September the count must be derived from the partner roster, not from the
  literal 3** -- which I have now written down twice, and which is exactly how a magic constant is
  born.
- **Regime unchanged:** Andrew hard pause on new ESTATE starts; an idle seat at this gate is correct.
  Zero crons. Lane tree clean. Nothing applied to AWS.

---

## Next Steps

1. **[CLOSED]** ~~Log-timeline residual~~ -- SETTLED same day on evidence (14:13Z): the orchestrator IS the sender, chain model correct, no September change needed.
2. **[0.7.0_AE_CloudOps]** Remaining comp-blast dial fixes when the pause lifts: the
   UnicodeEncodeError itself, `--direction up`, the substring `matches[0]` ambiguity, the FETCHES gap.
3. **[Andrew]** The act-3 threshold question still stands: 174 of 1891 gold pairs clear at 0.70/3.0.
4. **[0.7.0_AE_CloudOps~A or successor]** Resumes ownership of this fire when it returns.

---

## MCP traffic

6 messages. Significant: MSTR 134400Z (URGENT T-18 watch dispatch), my 134910Z (checks 1+2 pass +
the 14:05Z caution), my 135320Z (correction against my own caution, 48s measurement), my 140730Z
(DELIVERED report to MSTR), my 140759Z (copy to CTO), MSTR 140843Z (confirmed, residual captured as
owned, stand down).
