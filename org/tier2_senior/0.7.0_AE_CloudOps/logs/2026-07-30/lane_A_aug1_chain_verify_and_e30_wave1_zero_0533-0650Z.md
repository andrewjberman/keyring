# ~A lane: Aug-1 ETFS chain verified END-TO-END + E3.0 Wave-1 closed at ZERO (premise refuted) -- 0533-0650Z

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Serial:** `0.7.0_AE_CloudOps~A` (fresh session, PID 2556, Monitor `beeett55q`, session ba9867b2)

## Arc

1. **Startup.** `/watcher` armed (prefix resolved `/cygdrive/c`, NOT `/c`; ZERO orphans for my
   serial so no kill needed; `TaskOutput(beeett55q)` = `running`, the only probe that observes a
   consumer). LD-0290 serial file written. XXX.md 1b: A.2 audit-archive rc=0/0 findings
   (baseline 2026-07-29T185938Z, snapshot not-due); **A.3 96/96 bare-resolve AND the mandatory
   EXERCISE half** (a forwarder produced its own banner -- the half that MSTR~Z's false 93/93
   motivated); D hook wired; E context set; F = zero crons (my row: Tier-2/3 + ~lanes).
   `/cloud-ops` loaded (noting its snapshot is 2026-05-27 and carries RETIRED doctrine -- the
   `/work` 20m cron per LD-0072, the AUTO-RESPAWN watcher verdict; CLAUDE.md is canonical).
2. **HELD a stale directive rather than executing it.** Inbox surfaced base-CTO's
   `20260729T211403Z` *"RUN THE BRIDGE NOW"* as unread-while-idle. ~8h stale, three ~A sessions
   logged past it. Grounded instead: the three `2026-07-28.json` keys EXIST, written 21:28:2xZ
   (~14 min after that dispatch) at byte sizes matching his quoted staging figures exactly.
   **Already discharged; re-running would have manufactured a duplicate production run.**
3. **Item Zero (Aug-1 clock) -- the record was wrong.** COO/MSTR carried it as "patch READY,
   post-freeze apply." It was applied+deployed 07-29 03:09:32Z, ledger CLOSED, tagged v1.1.0,
   freeze overridden Andrew-direct. Verified on the APPLIED plane myself (not the predecessor's
   self-report). COO's read of `17bcbff520` was correct about that commit, ~26h stale as state.
4. **Raised a blocker, then WITHDREW it on my own exercise.** Flagged `write_month_csvs` as
   unguarded upstream of ALL S3 uploads under `set -e` -> a throw costs the PDF too (total, not
   degraded, non-delivery). Then exercised the real function against real S3 data, local-only:
   **3 CSVs for 2026-07, no exception; June positive control 3/3.** Trigger refuted -> withdrew.
   COO had already escalated it to ~C as *the* live blocker and retracted that on my evidence.
5. **Nearly reported two non-findings; killed both by grounding the mechanism.**
   (a) July CSVs are ragged 28/29/27-of-31 -- source-confirmed `_month_cap:164-175`: an
   in-progress month MTD-caps, a complete month returns `m_end` unconditionally. June's uniform
   30/30/30 is the exercised proof. **Artifact of the day I ran it; vanishes Aug-1.**
   (b) `aws events list-rules` showed NO month-end rule -> I was one step from reporting a
   missing production schedule 28h before a fire Andrew asked for BY NAME. It is an
   `aws_scheduler_schedule` (EventBridge **Scheduler**) which that API structurally cannot see.
   `comp-trigger` printed its own denominator (143 rules + 11 schedules) and resolved it ENABLED.
6. **Found and corrected a torn-down control documented as LIVE** (@`ee1c5b5c74`). README listed
   `etfs-reports-monthly-absence-check` as live component #6; it was deliberately torn down
   @`f3a78be7d8` as a PAGER under CTO GO 030135Z, and `etfs-reports-alerts` has ZERO live
   subscriptions. **Not rebuilt** (moratorium + it would reverse a CTO teardown). The mechanism
   check is what turned a "missing guard" defect report into a doc fix.
7. **THE HIGHEST-VALUE LEG, and nobody had checked it.** The renderer is NOT Terraform-deployed
   -- the EC2 `s3 cp`s it at RUN TIME, so a re-upload IS the whole deploy: no plan, no 0-diff,
   no source map, no tag. Had it gone un-re-uploaded after the 07-07 CSV commit, Aug-1 pulls a
   renderer with no CSV code **behind a green run and a delivered PDF**. Verified in sync.
8. **E3.0 Wave-1: ZERO retirements** (@`2da40ba711`). Three findings (F1-F3 below). COO ruled it
   **GATES EXERCISED / ZERO RETIRED / PREMISE REFUTED** and routed re-specification to ~C.
9. **Measured the Aug-1 carried-tail population on ~C's challenge.** ~C caught that 07-31 is a
   FRIDAY and the fire is SATURDAY, hypothesising all three partners carry. **Measured: it is
   neither framing** -- and the calendar is not the mechanism (below).

## Deployment Sequence + Verification (AE addition)

**NO DEPLOY THIS SESSION.** No Terraform, no safe-apply, no HALTGT, no code deploy. Verification
only. Actual output:

```
ORCHESTRATOR (applied plane)
  aws lambda get-function-configuration --function-name etfs-reports-orchestrator
    CodeSha256   jfMnlSE2VocFe7kN9uxhx35iU3JLev5flYOJKW9OE+I=
    LastModified 2026-07-29T03:09:32.000+0000
  == plan hash in ledger 20260729T0300Z (opened at start, CLOSED 0316Z), tag etfs-reports-v1.1.0

RENDERER ARTIFACT (run-time-fetched -- downloaded AND symbol-checked, not listed)
  s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py
    36,767 B   uploaded 2026-07-07 11:22:31   (27s after commit 5b9c6d46eb)
  md5 DEPLOYED d618e3b9931bde32c2d672363f8587ff
  md5 REPO     d618e3b9931bde32c2d672363f8587ff   IDENTICAL, 710 lines both
  deployed copy DEFINES write_month_csvs @:564 and CALLS it @:644
  -> my local exercise was of the EXACT DEPLOYED BYTES, not a proxy.
  HONEST BOUND: same bytes, different runtime (native py3.12 vs AL2023 python3 under the
  instance role). Code path exercised; environment-specific failure is NOT.

SCHEDULE (correct instrument -- aws scheduler, NOT aws events)
  etfs-reports-monthly-run  ENABLED  cron(0 10 1 * ? *)  America/New_York (DST-native)
  target etfs-reports-orchestrator  input {"mode":"run"}
  comp-trigger denominator: 143 events-rules + 11 schedules scanned, ONE match

SENDER (Rule 23)  SES_SENDER=noreply@opalinvest.dev   COMPLIANT
```

## Compiler Tools

| Tool | Why | Result | Note |
|---|---|---|---|
| `comp-which` x3 | route absence-guard / legacywriter / contract questions | PASS/PARTIAL | routed to `comp-trigger` (correct); honestly reported NO CURATED RULE on the contract-lifecycle question rather than guessing |
| `comp-trigger etfs-reports` | is the Aug-1 schedule armed | **PASS** | printed its own denominator; resolved the `aws events` blind spot |
| `comp-legacywriter --self-test` | gate before trusting the census | **PASS 10/10** | scored on OUTPUT; incl. negative controls proving it can say SOLE / UNDETERMINABLE |
| `comp-legacywriter --census` x3 | E3.0 population | PASS | first run had 3 axes UNSUPPLIED; re-ran with all four |
| `comp-heat` / `comp-dups` / `comp-debris` | supply the missing axes | PASS | `comp-dups` surfaced F3 (stale sovereign hold) |
| `comp-grep` x8 | on-rails search (raw `.tf` grep GATED, correctly) | PASS | one **FAILED RETRIEVAL** correctly reported as such, not as a zero (wrong lambda dirname) |
| `comp-surface-check` | in safe-commit, both commits | PASS | 6 surfaces / 19 carve tokens, none touched |
| `comp-pulse` risk-reflex | in safe-commit | CLEAN | denominator printed: 3 files vs 1484 danger nodes |
| `lib/trading_calendar.py` | frontier, never wall-clock | PASS | `expected_last_trading_day` needs a `now` arg -- read the signature after the TypeError |

**What worked:** `comp-trigger`'s self-printed denominator is what stopped a false outage.
`comp-legacywriter`'s self-test negative controls made its census trustworthy. `comp-grep`
distinguishing FAILED RETRIEVAL from a real zero prevented a wrong conclusion.
**What failed:** the raw `.tf` grep was gated by the rail -- correct behaviour, I re-routed.
**Gap found:** F1 -- `retire_risk` is an affordance defect on a retirement-authorizing tool.

## Findings

- **F1 (routed ~C, COO pushing hardest).** 29 of 35 E3.0 name-matched survivors **HOLD LIVE
  OBJECTS** while reading `contest=SOLE`, `deadness_score=5`, `retire_risk=LOW`, no-reader,
  code-cold -- largest 436,489 B of realized-lot crossref forensics. The tool does not lie (its
  docstring says the invocation axis is BUCKET-grain); the field is *named* `retire_risk` and
  *reads* `LOW` on a surface whose existence it never checked. Recommend forcing
  `UNKNOWN-KEY-EXISTENCE-UNCHECKED` absent a supplied key-grain listing.
- **F2 (routed ~C, real input to ~Z's WS-C1).** The TRANSIENT stopgap is a 9-entry substring
  denylist (`comp_legacywriter.py:704`). All 6 candidates cleared it **by not matching a name,
  not by being examined.** I then refuted my own transient hypothesis at source (`put_object`
  only, no `delete_object`) -- which sharpens it: the guard could not have told me that.
- **F3 (routed ~C).** `debtscan/dup_scan.py:358` `_HELD_PREFIXES` still excludes 354 bd/schwab
  paths, comment *"for when Andrew lifts"* -- **lifted completely 2026-07-14.** Used
  `--allow-held`; did NOT flip the constant (arch-gated; grantee does not remove its own guard).
- **F4 (base owns, routed by base to COO).** A deploy path where a re-upload IS the whole deploy
  has no plan/0-diff/source-map/tag. In sync today; ungated tomorrow.

## Aug-1 carried-tail: MEASURED population

`load_all_daily` reads `s3://opal-data-etfs/daily/{partner}/{YYYY-MM-DD}.json`. Enumerated via
`s3api list-objects-v2` (ISO-UTC), **never `aws s3 ls`** (LastModified renders LOCAL).
Denominators: 49financial 60 date-keys, inflection 71, cottonwood 31.
**POSITIVE CONTROL (built in):** inflection HAS 9 Sat + 8 Sun date-keys, so the scan demonstrably
CAN see weekend keys -> the zero Sat/Sun for the other two is a REAL zero.

**TAIL CADENCE (landing lag on dates that EXIST):**
```
inflection    T+0, lands 14:53-15:07Z on the data-date. 12/12 of present keys.
cottonwood    T+2 weekdays / T+4-5 across a weekend, fixed 10:30:30Z. Thu->Sat +2d is 3/3.
49financial   BACKFILLED 07-29 01:22Z (ten date-keys in 11 seconds), then ONE post-backfill
              daily landing (07-28 @ 07-29 10:45:12Z, T+1). n=1 is not a cadence.
```

**>> SELF-CORRECTION, 070251Z -- I DOWNGRADED MY OWN CONFIDENCE BEFORE ANDREW WAS ASKED. <<**
I first reported *"inflection holds 07-31, ZERO carried, HIGH CONFIDENCE (12/12 same-day)"*.
**`12/12` is a rate over date-keys that EXIST -- it says nothing about whether a given date WILL
exist.** I printed a denominator, but it was the denominator of my RETRIEVAL, not of my CLAIM.
The gaps were in my own printed output (the series jumps 07-10 -> 07-16 and 07-18 -> 07-24) and I
read the `lag=0d` column straight past them. Surfaced by `0.4.0_DE_ClientPlatform` (070039Z)
censusing interior coverage; I re-derived it independently rather than accepting their numbers.

INTERIOR COVERAGE, trading-day predicate (`is_trading_day`), 07-01..07-29, **denominator 20
trading days** of 29 calendar days (9 excluded = weekends + 07-03 July-4-observed):
```
49financial   19/20 (95%)   missing 07-29                                    <- BEST
cottonwood    17/20 (85%)   missing 07-20, 07-28, 07-29
inflection    12/20 (60%)   missing 07-01, 07-13,14,15, 07-20,21,22,23      <- WORST
              *** CONTIGUOUS RUNS: 3 days (07-13..15) and 4 days (07-20..23)
```
**THE RANKING INVERTS. I handed COO inflection as the clean partner and 49financial as the problem
child; on interior coverage it is the reverse.** Both measurements are true -- inflection lands T+0
*when it produces*, and fails to produce on ~40% of trading days. **Tail-cleanliness does not imply
interior cleanliness** (DE's phrase). Corrected carried-day ranges, with the error bar I omitted:
```
inflection    RANGE 0-2   (0 only IF it produces 07-31; P is ~60%, not "high")
cottonwood    RANGE 1-4   (1 is best-estimate but needs 3 further landings on an 85% feed)
49financial   RANGE 0-3   (range unchanged, but its 95% interior makes it the STRONGEST)
```
**Nobody should carry "inflection is clean" out of my earlier message.** UNCHANGED by this: the
`_month_cap`/`_carried_daily` mechanism, and the refutation of ~C's T-1 premise (which never needed
the presence rate). **It STRENGTHENS the remedy: a computed line needs no forecast at all -- it
prints what actually happened.**
**~C's premise is refuted as the MECHANISM:** *"under a T-1 pipeline Friday's data does not exist
on Friday"* -- inflection lands T+0, so it does. **None of the three is T-1.** The spread is three
different feed cadences, not the Friday/Saturday calendar. **~C's other half STANDS:** June
genuinely does not generalize (06-30 was a Tuesday).
**Remedy consequence:** a STATIC disclosure sentence would be FALSE (cannot say "all carry" --
inflection does not; cannot say "cottonwood" -- 49F unknown). The honest form is **per-partner,
computed at run time** from `cap`/`in_month[-1]` which the renderer ALREADY has -- unconditional,
no new pipeline, nothing notification-shaped. **Not mine to build** (DS/DE lane, payment basis).

## Blockers

**None of mine are self-inflicted.** Two items held on others' word, both authorization gates
working as designed:
1. **DELETE-AUTH -- at ANDREW, and it has nowhere else to land.** S3 deletion is human-reserved
   under Agent Autonomy. COO correctly refused ("I am an agent"); ~C **also** refused and
   declined to reason around it (outranking COO does not convert a human-reserved authorization
   into an agent one). Both recommend GRANT. Rehearsal stays STAGED.
2. **49financial cadence -- bounded unknown, resolvable today.** Watch armed (Monitor
   `bbfrc8wl9`) for `daily/49financial/2026-07-29.json`; **emits on BOTH outcomes** so silence
   is not a possible result. Converts n=1 -> n=2 without manufacturing a run.

## Current State

- **Aug-1 ETFS month-end (Andrew-named, HARD, Sat 2026-08-01 10:00 ET = 14:00Z).** Chain VERIFIED
  end-to-end: schedule ENABLED, orchestrator CodeSha256 applied-plane-verified, renderer artifact
  md5-identical AND symbol-checked, render file list = 3 CSVs exercised on deployed bytes, sender
  Rule-23 compliant. **No absence guard by design** (torn down as a pager under CTO GO) -- **I am
  the detection.** Remaining: real-content attach rehearsal, STAGED at
  `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/etfs_9999_07_attach_rehearsal_STAGED_20260730.sh`,
  one motion on Andrew's word; else the residual is recorded with ~C's name on it.
- **E3.0 Wave-1: CLOSED, 0 retirements.** Report:
  `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/E30_WAVE1_SAFE_SLICE_20260730.md` @`2da40ba711`.
  Counts: census-only 56 / derived-from-contracts 0 / COVERAGE DEBT 56 of 56. COO: do NOT reopen
  it looking for retirements.
- **Commits:** `ee1c5b5c74` (README parity), `2da40ba711` (E3.0 report + staged rehearsal). Pushed
  to CLOUD. No Terraform, no tags, no infra mutation.
- **Base<->~A boundary confirmed symmetrically** (base PID 33636): zero shared files, zero shared
  S3 keys, no TF either side, no HALTGT contention. Base RAVC-closed my renderer evidence.
- **Stood down as instructed:** AVGCAP carried-tail *remedy* (ruling is ~C's/Andrew's -- I supply
  measurement only), E3.0 re-specification (~C), the renderer guard (DS/DE lane).

## !! ADDED 0748Z -- AUG-1 STEP 2 IS MINE, STAGED AND HELD. A SUCCESSOR MUST FIND THIS. !!

**THE RENDERER IS NOT TERRAFORM-DEPLOYED. A RE-UPLOAD *IS* THE WHOLE DEPLOY.** `lambda_function.py:114`
has the transient EC2 box `aws s3 cp` `render_month_end.py` from `ARTIFACT_PREFIX` **at run time** -- no
plan, no 0-diff, no source map, no tag. Found by `0.4.0_DE_ClientPlatform` (073506Z); COO assigned me
step 2 at 073541Z; accepted as staged 074810Z.

```
step 1  0.4.0_DE   git apply patch @75c66b8733 + safe-commit          <- NOT mine
step 2  ME (~A)    re-upload + round-trip md5 vs LANDED blob + symbol grep on the DOWNLOADED copy
PROCEDURE  org/tier2_senior/0.7.0_AE_CloudOps/deliverables/etfs_renderer_reupload_STEP2_STAGED_20260730.sh
STATE      STAGED, bash -n parse-clean, NEVER EXECUTED. Runs ONLY on COO's word, ONLY after step 1 lands.
DO NOT     pre-upload "to be ready" -- that deploys a change to a PAYMENT BASIS without authorization.
ORDER      strictly after step 1 (the verify reads the LANDED blob). Not parallelisable. <1 min total.
ROLLBACK   versioning ENABLED. VersionId chTZ82VfoorkM2F7oUOTcTNFyos6JUDu, md5
           d618e3b9931bde32c2d672363f8587ff, 36767 B, 2026-07-07 15:22:31 GMT. Fires ONLY on COO's word.
MISMATCH   STOP. No retry (a blind retry overwrites the only evidence). Both hashes to COO.
IF ANDREW DECLINES the disclosure: there is NO step 2. The deployed artifact stays as-is, in sync with
           HEAD, which is the CORRECT state. Doing nothing is the right outcome in that branch.
```
**PRE-RESOLVED so a successor does not hit it mid-deploy: the CRLF trap.** Direct md5-vs-`git show HEAD:`
is valid for this file **ONLY because `.gitattributes:5` pins `*.py text eol=lf`** (0 CR bytes measured;
working tree == git blob == live S3 object, all `d618e3b993...`). **On a file WITHOUT `eol=lf` that
comparison mismatches spuriously** -- and at hour 24 on a payment path you cannot distinguish a
line-ending artifact from real corruption, so the honest response is to stop, which means missing the fire.

**ROOT CAUSE OF THE WHOLE GAP, recorded because the fix is a doc edit nobody would prioritise:** the
README read *"Re-upload after any renderer change (DE's lane)"* -- and **DE's charter EXCLUDES AWS
deploys. The doc named an owner structurally incapable of performing the step.** So the two-step deploy
carried one assigned step for a month and every reader correctly concluded it was covered.
>> **A MIS-ASSIGNED OWNER IS INDISTINGUISHABLE FROM A COVERED STEP UNTIL THE DAY IT MATTERS.** An
*unassigned* step at least looks like a hole; an assigned-but-impossible one looks DONE, so nobody
audits it. << Fixed @`085851e23b` with both steps and both lanes named.

## Next Steps

0. **[0.7.0_AE_CloudOps~A -- HIGHEST TIME-CRITICALITY]** On COO's word AFTER DE's step-1 commit lands:
   run the STAGED step-2 re-upload (see the 0748Z block above). **Nothing before COO's word; no
   pre-upload.** If Andrew declines the disclosure, there is no step 2 -- and that is a correct outcome.
1. **[0.7.0_AE_CloudOps~A]** On Monitor `bbfrc8wl9` firing: report the 49financial n=2 verdict to
   COO + DE in one line -- it closes the last unmeasured limb of a dollar-bearing ruling. Emits on
   BOTH outcomes, so silence is not a possible result.
2. **[Andrew]** TWO decisions, both human-reserved, neither delegable to an agent:
   (a) DELETE-AUTH for `s3://opal-data-etfs/platinum/reports/9999-07/*` -> I run the staged attach
       rehearsal as one motion. **COO and ~C BOTH refused to grant it** (S3 deletion is human-reserved;
       outranking COO does not convert a human-reserved authorization into an agent one). Both
       recommend GRANT. Declined is legitimate -> residual recorded with ~C's name on it.
   (b) GO/NO-GO on shipping the per-partner carried-forward disclosure -> triggers DE step 1, then my
       step 2, strictly in that order.
3. **[1.0.0_SA_CTO~C]** F1 (`retire_risk` affordance), F2 (denylist-not-lifecycle-check -> ~Z
   WS-C1), F3 (`dup_scan.py:358` stale constant), E3.0 re-specification, AVGCAP remedy ruling.
4. **[0.4.0_DS_ClientPlatform / 0.4.0_DE]** IF ~C pulls the per-partner disclosure forward: it
   must be EXERCISED (a zero-S3-write local harness exists and I will hand it over), and
   **`_month_cap` must not be touched** -- Andrew-ruled full-calendar-month billing with a CVO
   verification behind it (+$790,884 on May 49F).
5. **[2.0.0_SA_COO]** Nothing owed; both dispatched items reported and ruled.
