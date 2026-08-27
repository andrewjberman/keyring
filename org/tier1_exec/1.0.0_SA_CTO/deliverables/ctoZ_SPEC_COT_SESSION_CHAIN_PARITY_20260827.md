# SPEC -- COT SESSION-CHAIN PARITY WITH 49F

**Spec author:** `1.0.0_SA_CTO~Z`, 2026-08-27 ~14:4xZ. **Executor:** `0.7.0_AE_CloudOps~Z`.
**Verifier at completion:** `1.0.0_SA_CTO~Z` (Andrew-direct: *"then you analyze their work at completion"*).

**AUTHORITY -- Andrew-direct 2026-08-27 at the CTO~Z terminal, VERBATIM:**
> *"i think this is a prime opportunity to develop the cot pattern so it is identical in structure to
> the 49F pattern, this way we can retain consistency. I recommend spawning 0.7.0_AE_CloudOps~Z to do
> it, pending receipt of your spec, then you analyze their work at completion."*

Earlier the same session, VERBATIM (the design intent this implements):
> *"all of this seems contingent on the refresh of the cookie/auth being managed at a proper interval
> that does not interfere with the rest of the jobs... identify simply where to place that on timing
> so that it is inobtrusive and does not interfere with the rest of the pipeline."*

**SEAT CHOICE IS CODE-GROUNDED, not just assigned:** `bd-49f-session-trigger/lambda_function.py:37`
declares *"Owner: 0.7.0_AE_CloudOps (chain wiring); box/wrapper = 0.6.2_AE_PartnerETL."* This work is
chain wiring. Same owner, same layer.

---

## s.1 -- WHAT HAPPENED, IN ONE PARAGRAPH

On 2026-08-27 the Cottonwood BD session cookie (captured `2026-08-19T11:32:39Z`) reached 8.0 days and
tripped the `MAX_SESSION_AGE_DAYS=7` bound. `cot-bd-session-trigger` correctly diverted to
`mode=session-refresh` and dispatched SSM doc `opal-cot-bd-session-fetch`. **The mint SUCCEEDED**
(`rc=0`, `state=LOGGED_IN`, fresh `.bd.identity` written to Secrets Manager). The bronze run then
never fired, because the rule that is supposed to carry `session-fetch Success -> bronze` **does not
exist**. Cottonwood lost a data day. Every downstream instrument read green, because they are all
downstream of the stage that never ran.

---

## ⛔ s.2-PRE -- AMENDMENT 1, 2026-08-27 ~15:1xZ: **THE CENSUS BELOW IS MEASURED ON ONE OF TWO PLANES**

**R2 IS ALREADY BUILT. DO NOT BUILD IT.** Found by `0.7.0_AE_CloudOps~Z` on its grounding pass
(BLOCKING surprise, msg 9173), independently confirmed by me and by `0.0.0_AB_MSTR~Z`.

**EventBridge has TWO planes with TWO APIs and they do not overlap.** `aws events list-rules`
enumerates **Rules**. `aws scheduler list-schedules` enumerates **Schedules**. My census called only
the first. Verified live on the second:

```
aws scheduler get-schedule --name cot-bd-session-daily-et
  State                       ENABLED
  ScheduleExpression          cron(30 7 * * ? *)
  ScheduleExpressionTimezone  America/New_York        <-- 07:30 ET == the observed 11:30Z
  Target.Arn                  ...function:cot-bd-session-trigger
  Target.Input                {"mode":"session-refresh"}
```
DENOMINATOR: 18 schedules on the Scheduler plane, 7 matching cot/49f/bd. The 137-rule census was
**correct and complete on its own plane** (I re-ran it; `bd-cot-session-daily` is genuinely absent
there) **and structurally blind to these 18.** A clean, confident, well-formed zero about the plane
the answer does not live on.

⛔ **BUILDING R2 WOULD BE ACTIVELY HARMFUL, on the exact axis caution (2) exists to protect:**
- **DUAL TRIGGER.** Two heads would both fire `session-refresh`. `cot-pipeline/eventbridge.tf`
  records that the old `cron(0 2)`Z Rule was deleted **in the same change** as the Scheduler
  precisely so there is *"no dual-trigger window."*
- **DST DRIFT -- the thing the Scheduler exists to prevent.** Andrew-direct 2026-07-29 chose
  Scheduler over a Rule because *"a Rule is UTC-only and a hardcoded UTC cron drifts an hour at DST,
  firing BEFORE market close come November."* **A UTC `cron(30 11)` satisfies caution (2) today and
  violates it on 2026-11-01.** My own spec would have re-introduced the defect it was written to avoid.
- The live tz-pinned Scheduler already preserves the ET-boundary landing, which is **strictly better
  than any UTC cron I could have specified.**

**R2 IS AMENDED TO: RATIFY WHAT EXISTS. Build nothing.** A4 discharges on the `get-schedule` output
plus the ET-boundary write-up. **This also answers a question I had left open as unresolved --
what fires the chain at ~11:30 daily. It is this Scheduler entry** (and
`opal-assets-ingest-mirror-cot-daily-et` is the 11:45 mirror). The COT chain was never
scheduleless; it was scheduled where I did not look.

---

## s.2 -- MEASURED PARITY CENSUS (2026-08-27 ~14:3xZ, `aws events describe-rule` / `list-targets-by-rule`)

> ⚠ **READ s.2-PRE FIRST. This table is TRUE WITHIN THE RULES PLANE AND INCOMPLETE OVERALL.**
> Its `bd-49f-session-daily` / COT-ABSENT row is superseded: COT's scheduled head exists on the
> Scheduler plane. The `bd-49f-session-complete` / COT-ABSENT row **stands and is confirmed.**

| 49F (working) | schedule / pattern | target | COT equivalent |
|---|---|---|---|
| `bd-49f-session-daily` | `cron(0 0 * * ? *)` | `bd-49f-session-trigger` | ⛔ **ABSENT** |
| `bd-49f-session-complete` | SSM `Success` event | `bd-49f-session-trigger` | ⛔ **ABSENT** |
| `bd-49f-fees-session-daily` | `cron(20 22 ? * MON-FRI *)` | `bd-49f-session-trigger` | n/a (no fees leg) |
| `bd-49f-keepalive-sched` | `rate(15 minutes)` | `bd-49f-keepalive` | ✓ `bd-cot-keepalive-sched` |
| -- | S3 sentinel | -- | ✓ `cot-bronze-complete`, `cot-silver-complete` |

**THE DELTA IS EXACTLY TWO RULES.** Everything else -- the trigger Lambda, its modes, the EC2, the
SSM documents, the keepalive, the S3 sentinel chain -- already exists on the COT side.

---

## ⛔ s.3-PRE -- AMENDMENT 2: **R1 WAS KILLED, NOT NEVER-BUILT -- AND THE KILL'S OWN REASONING IS INVERTED**

The spec said the rule *"does not exist"* / *"was never built."* **It existed and was deliberately
deleted.** Found by `0.7.0_AE_CloudOps~Z`, confirmed by me on `aws ssm list-commands`.

```
5b989deb27  kill(OPAL_MDPFCLEANUP.TO-3 apply-2): remove cot-session-complete set
            (K2 dead event leg, Andrew-ratified @874b52729c)
```
Its surviving comment in `cot-pipeline/eventbridge.tf` states the reasoning verbatim:
> *"fired 1x/7d while the chain completed DAILY without it -- the session-refresh mode dispatches
> bronze directly ... so the chain's daily completion IS the consumer-exercise proving no live
> dependency."*

⛔ **THAT REASONING IS INVERTED, AND THE INVERSION IS THE ENTIRE INCIDENT.** The rule fired 1x/7d
**because that is the mint day -- the one day it carries anything.** The *"chain completed daily
without it"* observation is the **6-of-7 SKIP days**, which never needed it and structurally could
not have exercised it. **The kill measured the days the rule is silent BY DESIGN and concluded it
had no consumer.** An instrument that could not have said otherwise (Rule 22a).

**FALSIFIED 4-FOR-4** (`aws ssm list-commands`, materialised, verified independently by me):

| mint day | bronze-run that day | `cot-session-complete` alive |
|---|---|---|
| 2026-08-03 | Success | YES (pre-kill) |
| 2026-08-11 | Success | YES (pre-kill) |
| **2026-08-19** | **NONE** | NO (post-kill) |
| **2026-08-27** | **NONE** | NO (post-kill, today) |

Over 08-06..08-26 bronze-run is missing on **exactly one day, 08-19** -- a mint day -- plus today.
Both pre-kill mint days kept their bronze run. The mint timestamps corroborate the migration:
08-03 at 22:00 ET and 08-11 at 16:31 ET (pre-Scheduler), then 08-19 and 08-27 both at **07:30 ET**.

**SEVERITY -- MEASURED, and it is narrower than "data loss":** the next successful run recovers the
gap through BD's rolling ~14-day export window. Natural experiment, 08-19:
`bronze/holdings/_complete/2026-08-18.json` **and** `2026-08-19.json` were **both written
2026-08-20T11:45:54Z**. So the true impact is **served data one day staler than it should be for
~24h on each mint day (~1 in 7), then self-healing** -- not permanent loss. **Real defect, not an
emergency.** State it this way; do not inflate it.

⚠ **08-19 IS NEW INFORMATION.** The spec was written believing today was a first occurrence. It is
the **second**, and 08-19 went unnoticed for 8 days. **REPORT, DO NOT CHASE:** no backfill of 08-19
or 08-26 is authorized here.

---

## s.3 -- WHY `cot-session-complete` IS THE LOAD-BEARING HALF

`cot-bd-session-trigger/lambda_function.py` (Lever-A docstring, ~`:222`) describes the intended path
in its own words:

> *"probe-positive but OLDER than the bound -> ... the UNCHANGED full OIDC mint leg runs
> (**session-fetch Success -> cot-session-complete -> bronze, the normal mint-then-bronze path**)"*

and again at `:262`:

> *"the skip dispatches opal-cot-bronze-run (NOT session-fetch) so **cot-session-complete (keyed on
> session-fetch Success) never fires** -> only this bronze-run runs"*

**The code was written against a rule that was never built.** The skip leg works (it dispatches
bronze directly). The mint leg dead-ends. So the failure is invisible for 6 days out of 7 and
guaranteed on the 7th.

⛔ **A SCHEDULED CRON ALONE DOES NOT FIX THIS.** With a daily cron and no `cot-session-complete`,
Lever-A still skips the mint on young cookies and still dead-ends on the mint day. **Build R1 even if
R2 is deferred.**

⚠ **NOTE THE ORIGIN, because it shapes the fix:** the `MAX_SESSION_AGE_DAYS` bound was itself the
WS-1 remedy (CTO amendment 2026-07-23T104223Z) for a 17-day window where a healthy durable cookie
suppressed the mint indefinitely -- *"refresh-only-at-death = the mint next runs exactly when
everything is already down."* That amendment was correct. **It converted refresh-at-death into
refresh-on-schedule, and routed the refresh into a link nobody had built.** The remedy for the first
gap is what arms the second. Do not read this as a reason to relax the bound.

---

## s.4 -- WHAT TO BUILD

### R1 -- `cot-session-complete` (REQUIRED, load-bearing)

Mirror `bd-49f-session-complete` exactly, substituting the COT SSM document name.

```json
{
  "source": ["aws.ssm"],
  "detail-type": ["EC2 Command Status-change Notification"],
  "detail": {
    "document-name": ["opal-cot-bd-session-fetch"],
    "status": ["Success"]
  }
}
```
- **Target:** `cot-bd-session-trigger` (the same Lambda, as 49F does -- one Lambda, mode-routed).
- **Input:** whatever mode payload drives the bronze-run leg. `_handle_bronze_run()` is already the
  single shared dispatch path (`:193-198`); **do not add a second bronze dispatch path.**
- `opal-cot-bd-session-fetch` is confirmed live in `aws ssm list-documents` (alongside
  `opal-cot-bronze-run`, `opal-cot-silver-run`, `opal-cot-gold-run`).

### R2 -- `bd-cot-session-daily` (REQUIRED for structural parity)

A **scheduled** rule targeting `cot-bd-session-trigger` in `session-refresh` mode, mirroring
`bd-49f-session-daily`.

⛔ **MIRROR THE STRUCTURE, NOT THE LITERAL CRON VALUE. DO NOT COPY `cron(0 0 * * ? *)`.**
49F's midnight works for 49F. Cottonwood's export is bound to **BD's business timezone (US Eastern)**:
`cot_bronze_ingest.py:80` records that a day *"not yet COMPLETED in BD's business timezone (US
Eastern)"* returns a **header-only ~4.6KB export**. The current ~11:30Z start (07:30 ET) is
load-bearing and proven. **Set the cron to preserve today's landing time (~11:30Z), not 49F's.**

**Also verified from BD's own native report criteria** (`sheet2.xml`, `Created (Eastern)` /
`Start Date` / `End Date`): each export is a rolling ~14-day window whose **End Date is D-1 for
holdings/allocations and D-0 for transactions/realized**. Moving the fire time across the ET
boundary changes which window BD returns. **Timing is a data-correctness parameter here, not a
scheduling convenience.**

**WHY R2 MATTERS INDEPENDENTLY:** the COT chain currently has **no schedule of its own** --
`cot-bd-session-trigger` is targeted only by `cot-bronze-complete` and `cot-silver-complete`, both
`ScheduleExpression: None`. That is CLAUDE.md's named defect (*"a pipeline whose only trigger is
another pipeline's success has no schedule and is a defect"*). R2 gives the chain a declared head.

---

## s.5 -- ON "REFRESH SAFELY PRIOR" -- THE ANALYSIS, SO THE SEAT DOES NOT RE-OPEN IT

Andrew's instinct was that the refresh should sit *before* the run so it cannot interfere. **R1
satisfies that intent without a separate earlier clock, and here is why:** with `cot-session-complete`
in place the mint **hands off** to bronze rather than terminating. A mint costs ~3-5 min inside the
same cycle (49F's own comment: *"each refresh->mint->complete cycle is ~3min"*), not a data day. The
interference was never the *timing* of the refresh -- it was that the refresh had **nowhere to go**.

A genuinely decoupled mint-only clock would need a **new mode that mints WITHOUT chaining to the
run**. 49F has no such mode. **Building one would be a divergence from the 49F pattern, which is the
opposite of what was asked.** If Andrew later wants the mint fully off the data path, that is a
separate spec and it changes both partners, not just COT.

---

## s.6 -- ACCEPTANCE CRITERIA -- EXERCISED, NOT READ

A config read is not evidence (Rule 22a). Each criterion names the test that fails if the claim is false.

| # | Criterion | Discharging evidence |
|---|---|---|
| A1 | `cot-session-complete` exists, ENABLED, correct pattern + target | `aws events describe-rule` + `list-targets-by-rule` output pasted |
| A2 | **The rule actually FIRES on a real session-fetch Success** | Force a mint (e.g. `MAX_SESSION_AGE_DAYS=0` on a scratch invoke, or an explicit `session-refresh` invoke) and show `cot-bd-session-trigger` re-invoked with a bronze-run dispatch in its CloudWatch log. **A2 IS THE ACCEPTANCE EVENT.** |
| A3 | **NEGATIVE CONTROL: the rule does NOT fire on a non-Success SSM status** or on a different document | Show a `opal-cot-bronze-run` Success does NOT re-trigger the mint path. A rule that fires on everything is not a fix. |
| A4 | `bd-cot-session-daily` exists, ENABLED, cron preserves ~11:30Z landing | rule output + a statement of the ET-boundary reasoning |
| A5 | End-to-end: bronze lands after a mint day | `opal-data-cot/forwardfill_v2/holdings/` gains a partition on a day the mint ran |
| A6 | No regression to the skip leg | On a young-cookie day, `Lever A: cot cookie POSITIVE-live -> SKIP OIDC-login mint, direct bronze-run` still logs and bronze still lands |

⛔ **A3 IS NOT OPTIONAL.** The instrument being built is an event filter; an event filter that cannot
be shown to *exclude* has not been tested.

---

## s.7 -- CONSTRAINTS (all pre-existing law; none created by this spec)

- **Terraform ONLY.** `.tools/safe-apply.sh`, never bare `terraform apply` (NEVER#4). Mirror file:
  `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf` -- the COT equivalent belongs in the
  cot-pipeline TF tree, not appended to the 49F file (bd/cot firm separation is gate + IAM enforced).
- **NO ALARMS, SNS, SES, MONITORS OR FRESHNESS CHECKERS.** Standing Andrew moratorium. 49F's
  `ALERT_TOPIC_ARN` is pre-existing; **do not mint a COT equivalent.** If the absence of one feels
  like a gap, that is a finding to surface, not a thing to build.
- **Deploy-completion ledger** opened at start, closed at completion, in
  `org/critical_paths/change_management/` (NEVER#6). A begun deploy finishes in-session or rolls back loud.
- **Rule 26:** the seat that builds it applies it, on its own box. No ferried applies.
- **Rule 27:** one project per tier-2 instance. This is `0.7.0_AE_CloudOps~Z`'s single project.
- **Surprise channel:** anything found outside this scope goes one line to `3.0.0_SA_CVO~Z` (cc me).
  Do not chase it, do not suppress it.

---

## s.8 -- EXPLICITLY OUT OF SCOPE

- **Do NOT change `MAX_SESSION_AGE_DAYS`.** Whether a daily cron makes the 7d bound redundant is a
  live design question (cadence-vs-tolerance) and it is Andrew's, not this build's.
- **`partner_roster.json` -- READ THIS, IT IS NOT "ALREADY HANDLED".** The cottonwood cadence was
  corrected today (`D+2` -> `T-1`) under its own Andrew-direct authorization, **but the correction
  reached ONE OF THREE HOMES and NOT the one production reads.** Measured 2026-08-27 ~14:5xZ:

  | home | bytes | cottonwood value feeds | sha256 |
  |---|---|---|---|
  | `data/mdpf/config/partner_roster.json` | 27,433 | **T-1** (corrected) | `e86e4631…` (pre-edit) |
  | `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/partner_roster.json` | 22,725 | **D+2** | `af44aaad…` |
  | `s3://opal-data-mdpf/code/scripts/gold/partner_roster.json` (runner) | 22,725 | **D+2** | `af44aaad…` |

  **The S3 runner copy is BYTE-IDENTICAL to the LAMBDA copy, not the config copy** -- so the emitter
  directory is the de facto publish source and `data/mdpf/config/` is a diverged sibling.
  `_load_partner_roster`'s docstring asserts *"ONE committed authority in two locations of the same
  file -- NEVER an S3-read fallback and NEVER a vendored copy (the duplicate-authority defect the
  accrual F-3 note names)."* **That is the defect it names, present in the file that denies it.**
  ⛔ **NOT AUTHORIZED BY THIS SPEC AND NOT THIS PROJECT** -- it is D8/MDPF-side, it is a separate
  Andrew call, and propagating a cadence value across diverged homes without first ruling WHICH home
  is authoritative would cement the duplication rather than fix it. **Recorded here so nobody reads
  "corrected today" as "correct in production."** Routed to Andrew.
- **Do NOT backfill 2026-08-26.** BD's rolling ~14-day export window is expected to re-cover it on
  the next successful run; two prior instances self-healed this way (08-18+08-19 landed together on
  08-20; 08-04+08-05 on 08-06). Observe, do not intervene.
- **Do NOT modify the rebalancer stream.** `cot-rebalancer-runner-daily cron(0 6 * * ? *)` is
  scheduled, healthy, and current through 08-27. It is a different stream on a different clock.
- **Do NOT re-time or re-wire `cot-bronze-complete` / `cot-silver-complete`.** They are legitimate
  accelerators; the defect was that they were the ONLY trigger, which R2 fixes.

---

## s.9 -- WHAT I WILL VERIFY AT COMPLETION

Against A1-A6, on the **live primitives**, not on the seat's report (Rule 22a; NEVER#5: never trust a
producer's self-report or `rc=0`). Specifically: `describe-rule`/`list-targets-by-rule` for DESIRED,
the CloudWatch invocation record for EXERCISED, and an S3 partition read for the end-to-end claim.
**A2 and A3 are the two I will not accept on a config read.**
