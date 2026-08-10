# MDPF trigger/upload sequence — why the served scopes are split across three vintages

**Author:** `1.0.0_SA_CTO` · **2026-08-10 ~13:0xZ** · **Measured at this seat, live**
**Origin:** Andrew-direct at the base CTO terminal, 2026-08-10, VERBATIM:

> *"The 'Global' view is on August 5th, Inflection is August 5th, and 49 and Cottonwood are both on
> August 6th. All of them should be on August 7th at this point, so we need to trace the routes and
> identify the basis for the delay."*
>
> He named two suspected causes: **(1)** *"how we've defined the timing/metronicity of these ingestion
> paths, which by the way these custom definitions are irrelevant now as api paths are always T+1 in
> that you get the prior days data sometime in the morning eastern time (we know its ~1:02am for Black
> Diamond)"*; **(2)** *"the timing of eventbridge rules, if the given scope's intake is after the mdpf
> floor schedule."*

> ⛔ **THIS DOCUMENT EXISTS BECAUSE IT SHOULD HAVE EXISTED BEFORE THE SPAWN NOTE.** I dispatched
> `2.0.0_SA_COO` and `0.7.0_AE_CloudOps` telling them *"the diagnosis is DONE, execute don't
> re-derive"* — for a diagnosis that lived only in my session context and in no committed artifact.
> COO correctly refused to execute a summary of a finding they could not read, and said so.
> **A DIAGNOSIS THAT IS NOT IN GIT IS NOT DONE; IT IS A CLAIM.** Same class as everything else this
> program keeps banking.

---

## 1 · BOTH HYPOTHESES CONFIRMED — and (2) is a consequence of (1)

**MEASURED** (`aws scheduler list-schedules` materialised client-side, 16 schedules, denominator
printed; each `get-schedule` read individually and normalised to UTC at EDT = UTC−4):

```
03:05Z  opal-assets-bd49f-dim-convert-daily        49f dim convert
03:30Z  wsb-49f-model-aua-pull-daily               49f model AUA        [TUE-SAT]
03:30Z  wsd-49f-partner-held-etf-pull-daily        49f partner ETF      [TUE-SAT]
═══════════ 13:00Z  mdpf-scheduled-floor  ◄── THE FLOOR BUILDS HERE ═══════════
13:15Z  smartx-rest-pull-daily                     49f / 0824    +15 min TOO LATE
13:30Z  smartx-assets-daily-pull-daily             49f / 0824    +30 min TOO LATE
13:40Z  mdpf-accrual-bridge-daily                                +40 min
13:50Z  opal-assets-mdpf-portal-publisher-daily    publishes what 13:00Z built
20:30Z  cot-bd-session-daily-et                    Cottonwood    +7.5 HOURS TOO LATE
22:30Z  opal-assets-ingest-mirror-cot-daily-et     ~~Cottonwood~~ ⛔ SEE CORRECTION — IT IS INFLECTION
```

> ## ⛔ CORRECTION 2026-08-10 ~1419Z — THE 22:30Z ROW IS **NOT** A COTTONWOOD INTAKE.
> **Source-confirmed by `2.0.0_SA_COO` (measured by `0.7.0_AE_CloudOps` on live CloudWatch + bucket
> notification config), against this very file. The row name is misleading and my table repeated it.**
>
> ```
> lambda_function.py:353   for row in MAP + PROVENANCE_RIDERS:      <- UNCONDITIONAL
>                          the handler NEVER consults the event payload for row selection
> mirror.tf:155            input = "{}"                             <- the Scheduler target
> MAP rows: :94 orion/inflection · :115 eclipse/inflection
>           :122 blackdiamond/cottonwood · :153 cottonwood meta-templates
> ```
>
> **⇒ BOTH mirror schedules run ALL FOUR ROWS.** `-inf-daily` and `-cot-daily-et` are **two CLOCKS on
> ONE ALL-ROWS FUNCTION** — neither is firm-scoped. The 22:30Z fire drives **eclipse/inflection**
> bronze, and the silver lands from an S3 ObjectCreated event on that bronze write
> (`opal-assets-silver-eclipse`, Prefix `eclipse/inflection/bronze/`, Suffix `.json`) — not from
> either 16:00 sweep.
>
> **⇒ SO "MOVE THE COT MIRROR EARLIER" IS AN *INFLECTION* CHANGE, NOT A COTTONWOOD ONE** — and by
> §3's own inversion it makes inflection **fresher** at the floor, which surfaces the cross-axis
> refusal **MORE** often. **§4 as written moves three things and one of them is not what its name
> says.**
>
> **WHY I DID NOT CATCH IT, and the general form:** §5 bounds this table honestly as a *schedule
> read* — and **a schedule read structurally cannot see a handler's row loop.** The instrument was
> correct within its domain and silent outside it. This is the same class already banked at R-20
> (classify by mechanism, not filename), R-32 (a gate naming the wrong branch) and the R-18 control
> misattribution: **the label and the referent drift apart, and the label is what a PLAN acts on.**
> Third instance at this seat in four days.
>
> **DISPOSITION:** COO has split Track A to contain **only** `cot-bd-session-daily-et` (20:30Z), and
> moved the 22:30Z mirror to its own **HELD** track — correctly, because moving it touches the
> inflection thread, not just the schedule one.

> ## ⇒ FOUR INTAKES FIRE **AFTER** THE FLOOR THEY FEED.
> The floor cannot see them **by construction** — not intermittently, not under load. Cottonwood is
> therefore **permanently ≥1 day behind**; 49financial misses **by minutes**.

**And hypothesis (1) is why the schedules look like that.** The late intakes are named for
business-hours rhythms — a *"session"* pull at 16:30 ET, a *"mirror"* at 18:30 ET — but the paths are
T+1: the data lands in the small hours and then sits.

~~**CARRIED (NOT measured):** the ingestion draw `…MDPF_INGESTION_DRAW_VENDOR_TO_PLATINUM_20260804.md:112`
records "BD xlsx lands (02:00Z nightly …)". `cot-bd-session-daily-et` fires at 20:30Z → an 18.5-hour wait.~~

> ## ⛔⛔ CORRECTED 2026-08-10 ~1430Z — **BD LANDS 06:00:44Z, NOT 02:00Z.** THE ERROR RAN IN THE DANGEROUS DIRECTION.
> **MEASURED by `0.7.0_AE_CloudOps`** — `list-objects-v2` LastModified, true UTC, **denominator 1,229
> objects** under `blackdiamond/cottonwood/bronze/`, first landing per (data-date, feed):
>
> ```
> date         rebalancer_accounts   rebalancer_model_detail   rebalancer_models
> 2026-08-05        06:00:44               06:00:45                 06:00:43
> 2026-08-06        06:00:45               06:00:45                 06:00:44
> 2026-08-07        06:00:44               06:00:45                 06:00:43
> 2026-08-08        06:00:45               06:00:45                 06:00:44
> 2026-08-09        06:00:44               06:00:45                 06:00:43
> 2026-08-10        06:00:44               06:00:45                 06:00:43
> ```
> **All three feeds, SIX CONSECUTIVE DAYS, sub-second stable.** The real gap is **14.5 hours, not
> 18.5** — the wait is real and the direction of §4 is unchanged.
>
> ### ⛔ WHY THIS IS WORSE THAN A FOUR-HOUR CORRECTION — MY FIX WOULD HAVE INSTALLED THIS WORKSTREAM'S OWN DEFECT
> A retime anchored on *"02:00Z + margin"* lands the session trigger near **02:30Z — roughly 3.5
> HOURS BEFORE THE DATA EXISTS.** That converts a schedule which is merely **LATE** into one which is
> **STRUCTURALLY EARLY**: it would read the prior day **forever** and **look perfectly healthy doing
> it.** I diagnosed exactly that failure mode in §1 and then wrote an anchor that would recreate it.
> **The safe anchor is 06:00:45Z + margin — and only after the producer is identified.**
>
> **PROVENANCE OF MY ERROR, undiscriminated and stated as such:** the 02:00Z figure was *carried*
> from the ingestion draw, not measured on the cottonwood prefix. Two readings I cannot separate —
> **(a)** it describes the **49F BD pipeline** (`opal-data-bd`), not cottonwood's, i.e. the bd/cot
> separation; or **(b)** it moved. **Either way the number that drives a cottonwood cron must be
> measured on the cottonwood prefix**, and that is 06:00:44Z. *§5 already labelled this figure as
> carried-not-re-derived — the bound was honest and I then used the number as if it were not.*

## 2 · SERVED STATE — his figures confirmed, and they split into TWO causes

**MEASURED** (`s3://opal-data-portal-v2/platinum/mdpf/<scope>/aggregate-aua-timeseries.json`):

| scope | `as_of_last` | `generated_at` | cause |
|---|---|---|---|
| global | 2026-08-05 | 2026-08-07T03:52:12Z | **inherits inflection** — needs all three legs |
| inflection | 2026-08-05 | 2026-08-07T03:52:12Z | **cross-axis gate REFUSED it** (not scheduling) |
| 49financial | 2026-08-06 | 2026-08-07T22:47:09Z | ~~schedule ordering (SmartX +15/+30 min)~~ **⚠ UNVERIFIED — see below** |
| cottonwood | 2026-08-06 | *(absent)* | ~~schedule ordering (+7.5 / +9.5 h)~~ **⛔ REFUTED — see below** |

> ## ⛔⛔ THE CAUSE COLUMN IS NOT ESTABLISHED. CORRECTED 2026-08-10 ~1500Z.
> **`0.7.0_AE_CloudOps` read the source and REFUTED the cottonwood attribution outright.**
>
> **`cot-bd-session-trigger` IS AN OIDC SESSION-REFRESH JOB. IT PRODUCES A CREDENTIAL, NOT DATA.**
> Its docstring (`infra/aws/lambda/cot-pipeline/cot-bd-session-trigger/lambda_function.py:1-23`):
> *"starts cot-exporter EC2 … headless Playwright OIDC login … writes the SESSION BUNDLE to
> `blackdiamond/cot/session` via put-secret-value."* A grep of all 330 lines for
> `forwardfill|export|xlsx|DAILY_` returns **no reference to any data artifact**.
>
> **IT IS NOT A LATE INTAKE. IT IS THE PRODUCTION TRIGGER**, and production completes ~90s after it:
> ```
> 20:30:00Z  cot-bd-session-daily-et -> cot-bd-session-trigger  (AUTH ONLY)
> 20:30:17Z  cot-exporter EC2 starts   (measured LaunchTime, 08-09)
>            SSM opal-cot-bronze-run -> cot_bronze_ingest.py
>            (:64  FORWARDFILL_PREFIX = "forwardfill_v2")     <- THE REAL PRODUCER
> 20:31:05Z  forwardfill_v2 xlsx land
> ```
>
> ### ⇒ SO "COTTONWOOD IS A TRADING DAY BEHIND" IS **NOT** EXPLAINED BY THIS SCHEDULE'S PLACEMENT.
> The ordering FACT in §1 stands — those clocks really do sit after the floor. **What does not stand
> is my CAUSAL ATTRIBUTION from that ordering to the observed staleness.** A clock sitting after the
> floor is not evidence that it is *why* a scope is stale, and I wrote the table as though it were.
> **The real cause of the cottonwood lag is UNKNOWN and is a DIAGNOSIS job, not a cron edit.**
>
> ⚠ **AND I AM DOWNGRADING 49FINANCIAL BY THE SAME STANDARD, unprompted.** SmartX firing at
> 13:15/13:30Z against a 13:00Z floor is a measured ordering fact — but **I never verified that the
> floor consumes SmartX output directly**, and that is precisely the inferential step that just failed
> on cottonwood. It is UNVERIFIED until someone reads the floor's inputs.
>
> **THE GENERAL FORM, and it is mine:** *an ordering fact and a causal explanation are different
> claims, and I published the second while having measured only the first.* Schedule times are cheap
> to measure and causally silent; what a job actually READS AND WRITES requires opening it. Fifth
> instance this week of reasoning from a description to a mechanism.

⚠ **THE SPLIT IS THE LOAD-BEARING PART.** Two of the four are a scheduling defect and two are not.
`global` and `inflection` share a `generated_at` because they were written by the same run, and
49financial's `22:47:09Z` is **ten seconds before** inflection's refusal at `22:47:19Z` in that same
fire — the run advanced 49f and was refused on inflection.

> ⛔ **A SCHEDULE FIX MOVES COTTONWOOD AND 49FINANCIAL. IT DOES NOT MOVE INFLECTION OR GLOBAL.**
> Inflection is the cross-axis coherence gate (Andrew's separately-named next-highest priority,
> handoff `@3aac2c3e32`); global inherits it. **Any report that a retime made "MDPF current" would be
> wrong on two of four scopes.**

## 3 · THE INVERSION — carry it into any remedy

From the 08-07 evidence: inflection **REFUSED 16-minute-old data** at 22:47:19Z, having **PASSED on
two-day-stale data** at the 13:00Z fire. **It passes on stale and fails on fresh.** So moving the floor
later surfaces the refusal *more* often, not less — **a successful retime should be expected to make
the 6/12 count look WORSE**, and that is not a regression to repair toward.

## 4 · PROPOSED TARGET SHAPE — floor time unchanged

```
06:00:44Z  BD lands  (MEASURED, n=1229, 6/6 days sub-second stable)   [was wrongly 02:00Z]
~06:15Z+   cot-bd-session          <- anchor = LANDING + margin, NEVER an assumed hour
~03:30Z    smartx pulls            <- pending SmartX's own measured delivery
           ⛔ NOT the 22:30Z mirror — that is an inflection intake, HELD
13:00Z     floor — strictly downstream of every intake
13:50Z     publisher
```

> ⛔ **NO NUMBER IN THIS SHAPE MAY BE SET FROM AN ASSUMED HOUR.** Every intake time is
> `measured_landing + margin` **on that feed's own prefix**, or it does not get set. The 02:00Z error
> above is the proof of why: an anchor carried from an adjacent pipeline's documentation would have
> fired 3.5h before the data and read the prior day forever, healthily.
>
> ⛔ **AND `cot-bd-session-daily-et` DOES NOT MOVE UNTIL ITS PRODUCER IS NAMED.** `0.7.0_AE_CloudOps`
> is holding on W1-5 criterion 1 — *"an unattributed re-time is a guess with a cron expression on
> it"* — and that is correct. **RULED OUT BY MEASUREMENT, not by name:** not
> `opal-assets-ingest-mirror` (its cottonwood row raises before completing on **every** invocation in
> a 14-day 100%-failure window, yet the data lands daily and sub-second stable); not a Lambda
> `opal-cot-bronze-run` (ResourceNotFound, no log group); **not any EventBridge Rule or Scheduler
> entry — nothing fires at 06:00Z across 139 rules (121 scheduled) + 16 Scheduler entries, all
> materialised and counted client-side.** Remaining candidates: the cot EC2, ECS, or **a schedule
> outside AWS entirely** — the banked precedent, and the 2026-08-06 false-finding says to ask that
> before calling anything missing.

> ⛔ **AMENDED 2026-08-10 — the 22:30Z mirror is REMOVED from this shape** (see the §1 correction: it
> is an inflection intake, so moving it is an inflection change and it is HELD on that thread).
>
> ⛔ **AND THE FLOOR TIME IN THIS SHAPE IS NOW A LIVE QUESTION AT ANDREW, NOT A SETTLED DEFAULT.**
> His 08-07 instruction sets intakes in a **12:00–13:30Z** window with the **floor at 13:30Z**; this
> §4 keeps the floor at **13:00Z**. *Both satisfy his stated goal that every intake precede the
> floor* — they differ on whether the floor still reads **T-1**.
> **The premise under the 08-07 ruling has since moved, measured by COO/AE:** it rested on
> orion+eclipse landing T+1 at 03:30Z, but **ORION WAS NEVER ON THAT PATTERN** (same-day 14:16Z,
> unbroken 07-20→08-09) and **ECLIPSE LEFT IT THREE DAYS AGO** (same-day 22:31Z since 08-07; cause
> `ce99054e44` committed 07-29, **APPLIED 08-06T00:04:48Z** — and the `date=2026-08-06` gap missing
> from both feeds **is that cutover's seam**). Routed to Andrew with the measurement attached; COO
> correctly declined to choose between a sovereign instruction and an architectural preference, and
> so do I.
>
> ⛔ **NOTHING IN THIS SHAPE EXECUTES UNTIL ONE QUESTION IS ANSWERED** (AE resolving now):
> **does `date=D` CONTAIN day-D data, or is it a RUN-DATE LABEL on D-1 content?** If it is a label,
> his window is safe and the conflict dissolves. **No schedule moves before that answer** — the whole
> T-1-vs-same-day disagreement turns on it.

⚠ **STEP 1 IS MEASUREMENT, NOT EDITING.** BD's 02:00Z is measured. **SmartX / Orion / Eclipse are
NOT** — setting those from inference would repeat the exact error that produced this defect. The
per-vendor `updated` / `as of` tags are the source. **`0.7.0_AE_CloudOps~Z`'s MDPF_CANPLAT P0-2R
(arrived in the 913e84c3b8 site-Z merge) carries a measured SmartX/Orion/Eclipse clock read** — read
it before re-measuring; if an independent second derivation is wanted, measure BEFORE opening it, or
it is an anchor rather than a derivation.
**The COTTONWOOD move needs no further measurement** — 02:00Z delivery vs a 20:30Z pull is grounded now.

## 5 · Bounds

Schedules, served artifacts and the invocation policy are **measured live at this seat 2026-08-10
~13:0xZ**. The BD 02:00Z landing is **carried from the ingestion draw**, not re-derived. The
inflection refusal timeline is **carried from `2.0.0_SA_COO`'s brief `@efe8812873`**. I have **not**
exercised any schedule change, **not** read the failing per-date rows, and **not** resolved the open
A4-write fork from the handoff — so nothing here authorises a fix to inflection.
