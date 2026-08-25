# DEPLOY-COMPLETION LEDGER -- MDPF global, clause (vi) domain precondition

**Status:** **CLOSED 2026-08-25T19:5xZ** -- the stated close condition is MET on the SERVED payload.
⛔ **READ THE "WHAT THIS CLOSE DOES NOT COVER" SECTION AT THE BOTTOM BEFORE TREATING THIS AS FINISHED.**
**Opened:** 2026-08-25T18:48:54Z by `0.4.0_DS_ClientPlatform~N`
**Closes when:** served `platinum/mdpf/global/aggregate-aua-timeseries.json` reads
`as_of_last = 2026-08-24` **and** `_provenance.source_keys` names the `2026-08-24` gold partition.
⛔ **NOT on object mtime, NOT on byte size, NOT on `_provenance.written_at`** -- that field advances
daily at fixed width over frozen content and produces a clean green on a dark product (measured;
`2.0.0_SA_COO` 70998). Key on `source_keys` / `as_of_last`.

## Why this entry exists
NEVER#6: a begun deploy FINISHES in-session or rolls back + escalates loud to COO. `2.0.0_SA_COO`
(71149) stated the obligation explicitly: *"NEVER#6 stays open until global reads
`as_of_last=2026-08-24` with `source_keys` advanced."*

## What is being deployed
`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` -- a DOMAIN PRECONDITION on the
cross-axis coherence gate's clause (vi): the triple `tot[i-1], tot[i], tot[i+1]` is compared only
where the SAME LEGS contribute a roster at all three dates.

- Commit: **`1234c8779e`** (author `0.4.0_DS_ClientPlatform~N`) -- **ON `origin/CLOUD`**, verified
  2026-08-25T19:4xZ. (Recorded as LOCAL when this entry was opened; an integrator pushed since. The
  check was `git rev-parse origin/CLOUD` == `git ls-remote origin CLOUD` FIRST -- a tracking ref can
  be stale, and an ancestry test against a stale ref is not a push claim -- then `merge-base
  --is-ancestor` per commit. All four of this repair's commits are on origin.)
- Also committed: `data/mdpf/scripts/gold/tests/test_cross_axis_membership_domain.py` (5 arms)
- Authorization: `2.0.0_SA_COO` 71118 (remedy (C) over (B)); `1.0.0_SA_CTO` 71117 raised no
  architectural objection; 71149 confirms owner + status.

## The defect being repaired
global has not emitted since **2026-08-20T13:31:05Z** -- 5 client-facing days dark. The gate
refused on `(vi) FOREIGN-DAY ROSTER: 1`, `2026-08-19: 7791 -> 8260 -> 7791`. **There was no
foreign-day roster.** Cottonwood contributes a roster on 18 of 461 dates and 2026-08-19 is the ONE
date whose neighbours BOTH lack it; its own measured +469 entered and left beside its own measured
values. Arithmetic: 49F core 7144 + inflection 562 + 49F SMA carry 85 = 7791; +469 = 8260.

⛔ **The standing prohibition was never crossed:** the gate is not weakened, bypassed or `--force`d,
and no 2026-08-19 data was touched. Fixing a clause's DOMAIN is not relaxing it -- verified by a
four-arm control set in which the proposed clause still refuses a planted foreign-day roster
(`+66` on 2026-07-06, the exact case clause (vi) was built from).

## ⛔ CORRECTION 2026-08-25T19:0xZ -- THE DEPLOY PATH BELOW WAS WRONG. TWO EXECUTORS, NOT ONE.

The section that follows named the S3 code-prefix sync as the deploy path. That is **correct for the
EC2 leg and WRONG for the scheduled acceptance path**, and the ledger is corrected here rather than
rewritten so the error stays legible.

**MEASURED (Rule 22a, CODE layer, deployed bytes read):**
1. `mdpf-scheduled-floor cron(30 13)` targets **`mdpf-gold-lambda`** -- and
   `/aws/lambda/mdpf-gold-lambda` carries this script's own stdout, including
   `2026-08-24T13:31:04Z` and `2026-08-25T13:31:03Z` `CROSS-AXIS COHERENCE GATE FAILED (global)`,
   with `2026-08-18T13:31:04Z OK: cross-axis gate PASS (global)` as the control that the group
   carries PASS lines too. **The scheduled refusals are the Lambda's.**
2. That Lambda **VENDORS** the module: handler `mdpf_gold_consolidator.lambda_handler`,
   `:70 sys.path.insert(0, _HERE)`, `:78 import dim_mdpf_aggregate_aua_timeseries as spine`;
   `download_file`/`CODE_PREFIX`/`s3.*scripts` -> **0 hits each**, positive control `import ` -> 21.
   It fetches no code from S3.
3. The vendored copy is **PRE-PATCH**: `BUILD_MANIFEST.json` bytes=171111,
   sha256 `a7db07bb68f465d5197bed499bf6ee052506fb92a64b803ae0ed04f66cda5dee`;
   `count_membership` occurrences **DEPLOYED 0 / patched local 14 / pre-patch snapshot 0**;
   LF-normalised md5 `2b59630a...` == the pre-patch snapshot.
4. The **EC2 `mdpf-daily-runner` leg does use the module -- as a LIBRARY, not an entry**
   (`mdpf-daily-dispatch.sh:157`, `:500` "library-not-entry since this swap", `:605` existence
   check). It syncs `code/scripts/` at run start, so **that leg DOES pick up the S3 copy.**

**CONSEQUENCE: the S3 sync is real and useful for the EC2 leg and DOES NOT REACH the scheduled
acceptance path.** A census of "1 S3 copy across code/ prefixes" is TRUE about S3 and blind to a copy
vendored inside a function package -- the executing population is 2, not 1.

**THE REAL DEPLOY PATH for the Lambda** (`lambda-source-map.json` -> `functions["mdpf-gold-lambda"]`):
```
tf_file      infra/aws/terraform/mdpf-pipeline/gold-lambda.tf
tf_resource  aws_lambda_function.mdpf_gold
source_dir   infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda   (the BUILDER, not the runtime source)
_build_note  package is ASSEMBLED FROM A PINNED COMMIT by build_package.py (git show <pin>:<path>)
```
Bump the pin to a commit containing `1234c8779e`, rebuild, **Terraform apply** (Deployment Rule 1:
Terraform is the only Lambda deploy mechanism; never `aws lambda update-function-code`).
**NOT STARTED** -- awaiting `2.0.0_SA_COO`, and the pin should reference a PUSHED commit.

**Also unresolved, recorded not assumed:** the `2026-08-25T18:48:07Z` upload to
`s3://opal-data-mdpf/code/scripts/gold/` was **not performed by this seat**. It is byte-correct; it
should be attributed rather than assumed.

## Deploy path AS FIRST RECORDED (superseded by the correction above -- kept, not deleted)
Deployed target: `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`
Measured 2026-08-25T18:4xZ (`comp-pipescript deployed --pipeline mdpf`):
```
STALE   local 952bbc16ea07ed14cf51a497f1b4cde5   s3 2b59630a8419193b02851dcaea207cdc
```
The s3 md5 equals the file's PRE-patch md5, so the deployed copy is a clean unmodified baseline.

⚠ **Rule 13's order is commit -> push -> S3 cp -> verify, and PUSH IS INTEGRATOR-ONLY**
(`.tools/hooks/never-rules-gate.sh:511`). `safe-deploy.sh` is the pre-push hook, so the sanctioned
deploy rides the integrator's push. Deploying before the push would put running code AHEAD OF
ORIGIN -- a provenance gap. **There is runway to avoid that:** see the clock below.

## The clock -- deploying tonight does NOT un-dark the client tonight
Measured on both trigger planes (`aws scheduler get-schedule`, UTC):
```
12:52Z  mdpf-feeder-backstop-daily        -> mdpf-feeder-trigger
13:30Z  mdpf-scheduled-floor              -> mdpf-gold-lambda        <- runs the patched script
13:40Z  mdpf-accrual-bridge-daily         -> mdpf-accrual-trigger
13:50Z  opal-assets-mdpf-portal-publisher -> platinum publish
```
Next gold execution: **2026-08-26T13:30Z**, ~18.7h after this entry was opened. Global republishes
on that run's artifact, platinum at 13:50Z. **No ad-hoc run is proposed:** an ad-hoc run is a QA
instrument and never production evidence (CLAUDE.md NEVER), and this repair's acceptance is the
scheduled run's own artifact.

⚠ Also noted, NOT acted on: `mdpf-feeder-accelerator` carries `ScheduleExpression: None` (EventBridge
rules plane) -- the known event-only-trigger condition. It is not on this repair's path and is not
this entry's subject.

## Steps
| # | Step | State |
|---|---|---|
| 1 | Fix committed + control set committed | **DONE** `1234c8779e` (local) |
| 2 | `commit-gate` / ruff / py_compile clean | **DONE** |
| 3 | 4 arms re-run against the REAL patched implementation | **DONE** A/B/C/D as predicted |
| 4 | Integrator pushes `1234c8779e` to `origin/CLOUD` | **DONE** -- verified ON ORIGIN 2026-08-25T19:4xZ |
| 5 | S3 code sync -- covers the **EC2 library leg only** | **LANDED 18:48:07Z**, not by this seat |
| 6 | `comp-pipescript deployed --pipeline mdpf` reads MATCH | **DONE** for the S3 leg |
| 6a | **Rebuild `mdpf-gold-lambda` + Terraform apply** -- HOTFIX PIN `530ba66971` | **BUILT** by `0.5.0_AE_OpalETL~B`; apply pending |
| 6b | Deployed package `BUILD_MANIFEST.json` shows the patched bytes (not 171111 B) | **PENDING** -- verify on the DEPLOYED zip, not the build report |
| 6c | **EXERCISE GATE** -- the shipping pairing run through the PRODUCTION entry point | **PASS** (my 71267) |

### The hotfix pin, and why it is not option (b)
`530ba66971` = `1234c8779e` cherry-picked onto the DEPLOYED pin `1daf1913dd`. It **OMITS**
D1_CATVIEWS rather than reverting it -- `0.4.0_DS_ClientPlatform~F`'s six commits stay exactly where
they are, untouched and undeployed. Mainline untouched; the commit exists only as an immutable build
pin. Scope at the pin: **21 members, 1 changed** (the spine), 20 unchanged including the consolidator
at its deployed sha256 `8da6c0a19480fd98`.
⛔ **Why D1_CATVIEWS could not ride:** it restructures the emission axis OF THE ARTIFACT UNDER REPAIR
(flat `ARTIFACT_TYPES` tuple -> `ARTIFACT_TYPE_SCOPE_SET` map, a `scopes_for` resolver that RAISES,
`a4_expected` re-derived), and `category-views` is `ALL_SCOPE` so global is in its scope set.
**Mechanism:** `_shape_category_views` raises `SystemExit` at `:580`; `shaped_cv` is built at `:1190`
**BEFORE** the emit loop at `:1228` -- so a refusal on ANY scope aborts the build before the restored
timeseries is ever written. Ruled by `2.0.0_SA_COO` 71224 on blast radius.

### Exercise gate -- what was actually run (my 71267)
Tree identity established FIRST, independently: I materialised all 21 members myself and only then
compared to the pin -- **21 compared, 21 IDENTICAL, 0 different**. So this exercises the artifact that
ships, not an equivalent of it.
Run through the **PRODUCTION ENTRY POINT**: `mdpf_gold_consolidator.lambda_handler({"qa_local": true})`
-- the handler's own zero-write mode (CTO 015625Z). Every write site enumerated and confirmed
`dry_run`-guarded before running: `:820 :839 :875 :995 :1024`, plus `:545`/`:555` reached only
through the guarded calls.
```
{"status": "green", "errors": [], "a4_objects_built": 12}
global 2026-08-24.json  as_of_last=2026-08-24  n_dates=461     <- the bar, MET at GOLD tier
49financial / inflection / cottonwood  all as_of_last=2026-08-24
artifact types emitted: 3 (account-distribution, aggregate-aua-timeseries, aum-metrics)
   -- D1_CATVIEWS ABSENT, observed not inferred
clause (vi) MEMBERSHIP-SKIPPED 1 excursion(s): 2026-08-19 7791 -> 8260 -> 7791
OK: cross-axis gate PASS (global) | OK: global composition gate PASS
```
⛔ **WHAT THE EXERCISE DOES NOT COVER** -- do not let it be read as more:
1. **Not production evidence.** A QA run never is. It did not touch the served payload.
2. **Not the Lambda runtime.** Local python **3.12**; the function runs **3.11 with layers and an IAM
   role**. Import-time dependency resolution, layer contents and IAM are UNEXERCISED. A green local
   run and a working deployed function are different claims.
3. **The gold body is not the served body** -- platinum is published by a separate Lambda at 13:50Z.

### ⛔ THE DEADLINE IS DATED, NOT GENERAL (`1.0.0_SA_CTO` 71273)
`1.0.0_SA_CTO` retracted the estate-wide "there is no scheduled MDPF gold run" claim: it came from a
census of EventBridge **Rules** only, and the MDPF chain lives on EventBridge **Scheduler** -- a
separate API. The chain is complete and ENABLED (matches what this entry recorded at open):
`12:52 -> 13:30 -> 13:40 -> 13:50` UTC.
**So `mdpf-scheduled-floor` fires `mdpf-gold-lambda` at 13:30Z EVERY DAY, and until the apply lands
that Lambda runs PRE-PATCH bytes.** The flip-flop risk has a clock: **2026-08-26T13:30Z, deployed or
not.**
| 7 | 2026-08-26T13:30Z scheduled run passes the gate | **PENDING** |
| 8 | Served global `as_of_last=2026-08-24` + `source_keys` advanced | **PENDING** -- closes this |
| 9 | `49financial` + `inflection` unmoved on data-bearing fields (`written_at` may differ) | **PENDING** |

## Rollback
Revert `1234c8779e` and re-sync. The prior deployed object is a clean baseline at md5
`2b59630a8419193b02851dcaea207cdc`; `opal-data-assets` / `opal-data-mdpf` are versioned, so the
prior code object is recoverable by version rather than by rebuild. Rolling back restores the
refusal -- it does NOT restore global's publishing, because the island is permanent (value dates
2026-08-18, 08-20 and 08-21 were never delivered by the vendor and never will be).

## Escalation
If step 7 or 8 fails, this does NOT get quietly retried: loud to `2.0.0_SA_COO` per NEVER#6, with
the run's own gate output.

-- `0.4.0_DS_ClientPlatform~N`


---

# CLOSE-OUT 2026-08-25T19:5xZ

## THE BAR, MEASURED ON THE SERVED PAYLOAD
```
global   as_of_last = 2026-08-24                                                    MET
         _provenance.source_keys =
           s3://opal-data-assets/portal/gold/mdpf/global/aggregate-aua-timeseries/2026-08-24.json
           -- names the 2026-08-24 gold partition                                   MET
         n_dates = 461
```
Not mtime, not size, not `written_at`.

**49financial + inflection UNMOVED**, full leaf-field diff, 18:52Z pre-state vs 19:46Z post-state:
```
49financial  12,310 leaf fields compared | DIFFERING 1 -> ._provenance.written_at
inflection   12,375 leaf fields compared | DIFFERING 1 -> ._provenance.written_at
```
Exactly the one permitted difference on both, nothing else.

## ⛔ ATTRIBUTION -- THE GOLD WRITE WAS NOT THIS SEAT'S RUN
`portal/gold/mdpf/global/aggregate-aua-timeseries/2026-08-24.json` LastModified **19:44:22Z**.
This seat fired at **19:45:21Z**. The object predates the invocation. The log group shows TWO:
```
19:44:22Z  RequestId 5aa64b78-bc00-43a0-9fa2-19cb0ae3cd58  32.5s  12/12 errors=none  <- NOT this seat
19:45:54Z  RequestId 51e5f8dc-0e3d-4e7d-880d-2c70d1c4903f  30.4s  12/12 errors=none  <- this seat
```
This seat's run completed green but `conditional_put` found byte-identical content and correctly did
not rewrite. **CLAIMED 19:51Z by `1.0.0_SA_CTO` (71318): Andrew-direct at their terminal ~19:42Z, verbatim *"Run
gold for global now and let's see if we get the fresh file displaying"*.** They invoked
`mdpf-gold-lambda` and then `opal-assets-mdpf-portal-publisher`, deliberately passing the scheduled
floor's EXACT production payload read from `aws scheduler get-schedule --query Target.Input` rather
than composing one. **THE RESTORE IS THEIRS.**
⛔ **AND THE "DOUBLY-OWNED EDGE" I RECORDED ABOVE IS WITHDRAWN.** It was not an unowned edge taken
twice by accident -- it was TWO AUTHORIZATION CHAINS ISSUED ~40 SECONDS APART, neither aware of the
other: `2.0.0_SA_COO` 71292 assigned the fire to this seat at 19:41:22Z, and Andrew independently
instructed `1.0.0_SA_CTO` at ~19:42Z while `2.0.0_SA_COO` was going non-live. Both acts authorized,
by different sovereigns. That is a materially less alarming thing than what this entry first said.
Recorded because a false attribution of a GOOD act is still a false attribution, and it is the one
nobody contests.
⚠ **Two ad-hoc PRODUCTION gold runs fired 90 seconds apart.** The invocation went from an unassigned
edge (`2.0.0_SA_COO` 71292) to doubly-owned within four minutes. No harm -- the second write was a
no-op by design -- **but it would not have been a no-op had the two runs carried different code.**

## WHAT THIS SEAT'S RUN DID ESTABLISH, since it was not the writer
It discharged residual (b) from the exercise gate: the prior exercise was LOCAL python **3.12**. The
19:45:54Z invocation ran the **deployed** artifact in Lambda **python3.11 with its real layers and
IAM role** -> `{"status":"green","errors":[],"a4_objects_built":12}`, StatusCode 200, no
FunctionError. Import-time dependency resolution, layers and IAM are now **EXERCISED, not inferred.**

## ⛔ WHAT THIS CLOSE DOES NOT COVER -- THE ACCEPTANCE IS STILL OPEN AND NEEDS AN OWNER
**The restore came from an AD-HOC run. Its artifacts are not production evidence.**
**AC6 acceptance is the SCHEDULED `cron(30 13)` gold + `cron(50 13)` publish on 2026-08-26** -- the
run that proves the thing which overwrites the client surface *every day* actually works. Nothing
tonight substitutes for it.
⛔ **AS OF THIS CLOSE THAT ACCEPTANCE HAS NO NAMED OWNER.** `2.0.0_SA_COO` and `3.0.0_SA_CVO` both
went non-live before it could be assigned (broker returned QUEUED for both). **Recording it here
rather than letting it be rediscovered** -- a correctly-filed item lost across a handoff is a defect
this estate measured twice today (`1.0.0_SA_CTO`, `ec532a0158`).
**What the acceptance read is:** after 13:50Z on 2026-08-26, the SERVED global payload still reads
`as_of_last=2026-08-25` (or later) with `source_keys` advanced, having been written by the SCHEDULED
chain -- and `49financial`/`inflection` still move only `written_at`.

## WHY THIS ENTRY CLOSES ANYWAY
NEVER#6's subject is a **half-landed deploy**. That is fully discharged: code built from an immutable
pin, applied, **verified on the deployed package's own member bytes** (spine 175,795 B,
`count_membership` = 14; consolidator `scopes_for` = 0), exercised in the real runtime, and the served
product restored. Holding this entry open against a FUTURE scheduled run would make an unclosed
deploy-ledger mean two different things, and an alarm that fires for a landed deploy trains people to
ignore it.

## RESIDUAL, ROUTED NOT CHASED
`meta.count_axis_note` -- `account_count` fans out per underlying model and must never be totalled
across models, and both the gate (`:1745`) and the composition (`:2487`) total it. Filed to
`3.0.0_SA_CVO` (71095), escalated **ARMED** (71106), **disarm owner `2.0.0_SA_COO`**, sharpened by
`1.0.0_SA_CTO` (71117) to *one served field name, three derivations, all labelled `count_basis:
measured`*. **Does not ride this repair and is not discharged by this close.**

-- `0.4.0_DS_ClientPlatform~N`


---

## ⛔ ADDENDUM -- `trigger.kind` IS A SELF-REPORT OF THE PAYLOAD AND CANNOT ATTRIBUTE A RUN
**Whoever performs the 2026-08-26 acceptance read: DO NOT USE THIS FIELD.**

Both of tonight's runs wrote a manifest under `portal/gold/mdpf/_manifests/2026-08-24/`:
```
20260825T194421Z.json  trigger {"kind":"scheduled","detail":{"source":"aws.events"}}  <- a MANUAL invoke
20260825T194554Z.json  trigger {"kind":"manual",   "detail":{"source":""}}
```
The first reads `scheduled` because `1.0.0_SA_CTO` passed the scheduled floor's production payload --
the right call for fidelity, with this side effect. **Mechanism, from the deployed handler:**
```python
src  = (event or {}).get("source") or ""
kind = "scheduled" if src == "aws.events" else ("s3-marker" if "Records" in event else "manual")
```
**The classification is derived ENTIRELY from caller-supplied payload. Any invoker can claim any kind.**

⛔ **CONSEQUENCE FOR THE ACCEPTANCE:** the durable record now holds a manifest stamped `scheduled`,
dated 2026-08-25, produced by a person. The acceptance question is *"did the SCHEDULED path restore
global by itself"* -- and the field that appears to answer it **cannot**. A reader checking it would
conclude the scheduled path ran successfully tonight. It did not.
`0.5.0_AE_OpalETL~B` measured that CloudTrail cannot supply it either: Lambda `Invoke` is a DATA
event -- 0 events in the window, with a **firing positive control** of 1 on `UpdateFunctionCode`.
⛔ **SUPERSEDED SAME NIGHT -- THE INSTRUMENT EXISTS. `0.5.0_AE_OpalETL~B` 71327 found it and I am
recording THEIR measurement rather than re-running it (a same-command re-run adds a vote, not
evidence).**

**`AWS/Scheduler` / `InvocationAttemptCount`.** AWS emits it, not the caller, so **no invoker can
forge it** -- which is exactly the property `trigger.kind` lacks. `0.5.0_AE_OpalETL~B` exercised BOTH
arms on tonight's own data:
```
POSITIVE  Scheduler deliveries today, 5-min bins UTC, ScheduleGroup=default:
            12:50 -> 12:52 backstop | 13:30 -> mdpf-scheduled-floor | 13:40 -> accrual | 13:50 -> publisher
          -- landing exactly where the cron census says they should
NEGATIVE  19:00-20:00Z window: EMPTY, while TWO invocations are KNOWN to have occurred in it
          (1.0.0_SA_CTO's gold invoke 19:42:5xZ and publisher invoke 19:46:0xZ)
```
**That empty window is a REAL negative control, not an absence of evidence:** the invocations are
known to have happened and the instrument stayed silent. It fires on scheduler delivery and is blind
to manual invokes -- the exact discrimination that was missing.

**LIMITS, as `0.5.0_AE_OpalETL~B` stated them:** (a) the dimension is `ScheduleGroup=default`, NOT
per-schedule -- attribution to a named schedule is by TIME against the cron map, sufficient for MDPF
because its four sit at distinct known minutes, and it is NOT per-schedule identity; (b) it is
`InvocationAttemptCount` -- it proves the SCHEDULER ATTEMPTED DELIVERY, never that the target ran
green.

### ⛔ THEREFORE, THE 2026-08-26 ACCEPTANCE READ IS THREE PARTS, AND `trigger.kind` ANSWERS NONE OF THEM
1. **An `AWS/Scheduler` `InvocationAttemptCount` datapoint in the 13:30 bin, `ScheduleGroup=default`,
   AT 5-MINUTE GRANULARITY** -- the delivery actually happened (payload-independent).
   ⛔ **THE BIN SIZE IS LOAD-BEARING, NOT A DETAIL.** `1.0.0_SA_CTO` (71335) re-derived this
   independently and measured that **18 schedules share `default`** and there is **no `ScheduleName`
   dimension to query at all** (`list-metrics --namespace AWS/Scheduler` returns 2 entries, neither
   carrying one). At their **1-hour** buckets the 13:00-14:00 sum was **7** -- the floor, the accrual
   bridge and the publisher collapsed together and are NOT separable. At `0.5.0_AE_OpalETL~B`'s
   **5-minute** bins the MDPF four land on distinct known minutes (12:50 / 13:30 / 13:40 / 13:50) and
   ARE separable. **Same metric, same group, two granularities, and only one of them answers the
   question.** Separation is by TIME against the cron map -- it is never per-schedule identity.
   *`1.0.0_SA_CTO`'s first attempt queried a `ScheduleName` dimension, got EMPTY including for the
   known 13:30Z fire, and correctly concluded NOTHING because their positive control did not fire --
   the empty was their own wrong-dimension call, not a missing metric.*
2. **The gold object's own result** -- it actually worked (`InvocationAttemptCount` cannot say this).
3. **The SERVED payload** -- it reached the client: `as_of_last` advanced with `source_keys` advanced,
   `49financial`/`inflection` moving only `written_at`.

⚠ **NOTHING WAS BUILT FOR THIS.** It is an ad-hoc read of a metric AWS already emits -- no alarm, no
subscription, no checker, no scheduled anything. The standing moratorium is untouched, and that is
stated here so "an instrument exists" is not later read as licence to wire detection to it.

-- `0.4.0_DS_ClientPlatform~N`
