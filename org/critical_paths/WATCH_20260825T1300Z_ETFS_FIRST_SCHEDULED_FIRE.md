# ⛔ TIME-TRIGGER — 2026-08-25T13:00Z — THE FIRST SCHEDULED FIRE OF `etf-positioning-producer`

**Opened:** 2026-08-25 ~08:5xZ by `0.0.0_AB_MSTR~Z` · **Raised by:** `2.0.0_SA_COO~Z`
**Named owner:** `0.7.0_AE_CloudOps~Z` (COO recommendation, MSTR endorsed)
**Andrew: TOLD DIRECTLY, same turn.** He is the only actor in this system guaranteed to persist to
13:00Z, which is the whole reason this file exists.

## ⛔ THIS FILE IS **NOT** THE PRIMARY CARRIER. READ THIS BEFORE USING IT.

```
PRIMARY (DISCOVERABLE)  0.7.0_AE_CloudOps~Z session log, Next Steps
                        .../0.7.0_AE_CloudOps/logs/2026-08-25/...defectb_deploy_and_pipeline_
                        posture_0745-0835Z.md   @1c576431b8
                        *** XXX.md Step 2 MAKES a successor read it. That is the only property
                            that matters, and this file does not have it. ***
THIS FILE (DURABLE)     the criteria and the three checks, in full. Nothing queries it.
SOVEREIGN               Andrew, told directly ~08:5xZ -- the only carrier that survives every
                        session boundary in this fabric.
```
⛔ **`1.0.0_SA_CTO~Z` CAUGHT THE DEFECT IN MY REASONING AND IT IS WORTH STATING PLAINLY: I CONFLATED
DURABLE WITH DISCOVERABLE.** I committed and pushed this file and treated that as discharging the
obligation. **Measured: `deploy_ledger.py check --red` reports `SCAN DENOMINATOR: 1 of 1 sentinel(s)`
— it sweeps `change_management/`, and this file sits at the PARENT level and is in no sweep, no
startup step, and no tool's path.** An artifact nobody is pointed at is not a carrier.
⚠ **DO NOT SUMMARISE THIS FILE INTO THE LOG.** The criteria live HERE, once. A restatement is a
second place for them to drift — **and that already happened tonight: item 3 below was WRONG in this
file while the other carrier was silent on it.**

⛔ **THIS IS A DURABLE RECORD, NOT A MONITOR.** No alarm, no SNS, no checker — the 2026-07-28
moratorium stands and this deliberately does not touch it. It is a WRITTEN OBLIGATION a future seat
can find. **ZERO crons remains in force; nothing here schedules anything.**

---

## WHY THIS ONE FIRE MATTERS AND THE OTHERS DO NOT

```
13:00Z  cron(0 13 * * ? *) fires on etf-positioning-producer for the FIRST TIME EVER
        (log group created 2026-08-24T22:52:48Z -- ZERO 13:00Z instants have elapsed)
```
**THREE THINGS COINCIDE ON ONE FIRE, and no session is scheduled to see any of them:**
1. **The schedule's first-ever acceptance** — an untested trigger, not a proven one.
2. **The first PRODUCTION publication of Andrew's fix.** Everything on the page today was
   hand-invoked. **An ad-hoc run is never the production path** (CLAUDE.md, ad-hoc/scheduled rule).
3. **An UNCONDITIONAL overwrite of a client-facing artifact** we hand-published twice tonight.
   `generated_at` sits inside the hashed body, so no no-op guard can fire.

## WHAT IT SHOULD DO, AND WHY BOTH FAILURE MODES ARE SILENT

**It carries the CORRECT code** — `etf-positioning-producer` moved to the fixed package at
**08:19:03Z** (sha `p/mc7hvScGyYxxMK...`), so it *should* reproduce SALXX =
`State Street U.S. Government MMKT` and FXFXX = `First American Treasury Obligations Fund`.

⛔ **BUT:**
- **If the rule does not fire at all**, the artifact simply stays as-is. **No error, no alarm, and
  the page keeps working** — indistinguishable from success without checking the timestamp.
- **If it fires and regresses**, it overwrites a correct client-facing artifact with a wrong one.
  **Also silent.** The page renders; the names revert.
- ⚠ **AND ITS INPUT DEPENDS ON A LOCAL WINDOWS TASK.** The Bloomberg L1 pull (`OPAL_BBGTML_daily_pull`)
  runs on THIS WORKSTATION, not in AWS — **zero EventBridge rules match `bbg|bloomberg|terminal` at
  ANY hour** (positive control `etf` = 8). If this box sleeps, `bbg/{date}/` never lands, the
  producer's own guard SKIPS the day, and it serves stale on a green run.

## THE CHECK — three reads, no tooling required

```
1  aws s3api head-object --bucket opal-data-portal-v2 --key platinum/etfs/positioning_data.json
   EXPECT LastModified ~13:00-13:05Z today.  Still 08:31:06Z => THE RULE DID NOT FIRE.
2  read SALXX + FXFXX names out of the body.
   EXPECT "State Street U.S. Government MMKT" / "First American Treasury Obligations Fund".
   Reverted => the scheduled path does NOT carry the fix and PROD is serving a regression.
3  read data_as_of.  ⛔ EXPECT **THE LAST TRADING DAY BEFORE THE FIRE DATE** (`trading_days_behind
   == 1`) -- AND THAT IS THE PASS. For today's 2026-08-25 fire that resolves to **2026-08-24**.
   STRUCTURAL INVARIANT, not a coincidence: `silver/holdings/{D}.parquet` lands ~22:00Z on day D,
   NINE HOURS AFTER that day's 13:00Z fire -- so the newest partition available to ANY 13:00Z run
   is ALWAYS the prior trading day.
```
⛔ **RELATIVE, NOT DATED — CORRECTED 09:0xZ, and this is the criterion's FOURTH move tonight.**
`2.0.0_SA_COO~Z` measured that this file had stopped at move three (`EXPECT 2026-08-24`, a DATE)
while the primary carrier had advanced to the relative form. **No effect today — 08-25 is a Tuesday
and both resolve to 08-24 — but a DATED criterion in a file meant to be read by a stranger is
correct exactly once and silently wrong every day after.**
>> **THIS IS THE DIVERGENCE I DEMANDED BOTH CARRIERS GUARD AGAINST, LANDING IN MY OWN FILE, ON THE
ONE LINE THAT HAD ALREADY BEEN CORRECTED ONCE, WITHIN TWENTY MINUTES OF MY WRITING THE WARNING.**
Two durable records of one obligation drift from minute one — not as a principle, as a measurement
taken on this file. <<
⛔ **CORRECTED 08:5xZ BY `1.0.0_SA_CTO~Z` BEFORE ANYONE CARRIED IT.** This item first read *"EXPECT
2026-08-25 if the 11:00Z local pull landed; 2026-08-24 means the workstation leg did not run."*
**THAT WOULD HAVE MANUFACTURED A FALSE SKIP TODAY.** Silver for 08-25 does not land until **22:00Z**,
so at 13:00Z the producer has no 08-25 input by design. **An UNCHANGED `data_as_of` of 2026-08-24 is
the CORRECT outcome, not evidence of a missed pull.**
>> **I POSED TWO OUTCOMES AS IF THEY WERE THE ONLY TWO, AND TODAY THE TRUE OUTCOME IS NEITHER.** A
criterion that offers a false dichotomy does not fail loudly — **it hands a successor a confident
wrong verdict about a healthy run**, at 13:00Z, with none of tonight's context to check it against.
**That is the whole hazard this file exists to prevent, reproduced inside the file itself.** <<
✅ **Items 1 and 2 stand unchanged. Item 2 failing is the FIX regressing; item 1 failing is the RULE
not firing. Do not report them as one, and do not read item 3 as either.**

## IF IT REGRESSES

The remedy is already proven: re-invoke the producer (the ad-hoc path used at 08:31:06Z). **PROD's
frontend at `a7a7ff16` is unaffected either way** — the render fix lives in the bundle, not the
artifact. **Only the NAMES ride the artifact.**

## RECORD

Fix chain: `2e9737af49` (publisher map) → apply 08:19:03Z → invoke 08:31:05Z → served verified at
four seats. Frontend: `f67b3a48` → promote `a7a7ff16` → PROD deploy SUCCESS, site build 08:42:19Z.
Directive: `laneZ_ANDREW_DIRECT_20260825_0730Z_FIX_SUBCATEGORIES_AND_SALXX_NAME_THIS_AND_ONLY_THIS.md`
