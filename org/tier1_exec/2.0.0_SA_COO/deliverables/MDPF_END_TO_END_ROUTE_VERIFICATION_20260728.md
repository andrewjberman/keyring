# MDPF END-TO-END ROUTE VERIFICATION -- measured 2026-07-28T20:0x-20:1xZ

**Author:** `2.0.0_SA_COO` - **Andrew-direct ~2004Z, VERBATIM:**

> "Make sure that the end to end route is functional, that means make sure that we have the most recent data
> for every single one of these buckets we've painstakingly enumerated is in the appropriate gold bucket as
> designed. Then make sure that the relevant publisher writer is active and has the grants required, then
> make sure that everything is actually written to the relevant buckets in opal-data-portal-v2 even if you
> have to manually trigger that publisher lambda to do so"

**Also Andrew ~1958Z:** *"I've already established that the mechanism this is supposed to take is
`/gold/mdpf/{firm, or "global"}/...`"* - **and ~2003Z:** *"Proceed with cleanup."*

>> **HEADLINE: THE ROUTE IS NOT FUNCTIONAL, AND THE MANUAL TRIGGER CANNOT MAKE IT SO. Firing the publisher
>> today would produce a clean-looking run that writes 07-23-era data into a bucket the portal does not
>> read. I did NOT fire it. Evidence below.** <<

---

## PART 1 -- IS THE MOST RECENT DATA IN THE CANONICAL GOLD BUCKET?

**Canonical (Andrew-established): `s3://opal-data-assets/portal/gold/mdpf/{firm|global}/{type}/{date}.json`**
Whole tree rewritten **2026-07-28T15:49:05-07Z**. T-1 frontier for today = **2026-07-27**.

| scope | type | newest DATA date | verdict |
|---|---|---|---|
| global | account-distribution | 2026-07-28 | CURRENT |
| global | aggregate-aua-timeseries | 2026-07-27 | CURRENT (T-1) |
| global | non-model-assets | 2026-07-27 | CURRENT (T-1) |
| 49financial | account-distribution | 2026-07-28 | CURRENT |
| 49financial | aggregate-aua-timeseries | 2026-07-27 | CURRENT (T-1) |
| inflection | account-distribution | 2026-07-27 | CURRENT (T-1) |
| inflection | aggregate-aua-timeseries | 2026-07-27 | CURRENT (T-1) |
| **cottonwood** | **account-distribution** | **2026-07-20** | **STALE ~5 trading days** |
| **cottonwood** | **account-units** | **2026-07-20** | **STALE ~5 trading days** |
| **cottonwood** | **aggregate-aua-timeseries** | **2026-07-22** | **STALE ~3 trading days** |
| **cottonwood** | **aum-metrics** | **2026-07-20** | **STALE ~5 trading days** |

**TWO DEFECTS:**
1. **COTTONWOOD IS STALE IN GOLD WHILE ITS SILVER IS FRESH.** DS measured cot silver today: allocations
   **07-27**, rebalancer models **07-28**, holdings **07-24**, unrealized **07-24**. **Gold carries 07-20 /
   07-22. The gap is SILVER -> GOLD, not source -> silver.** The files were WRITTEN today at 15:49 -- the
   producer ran and emitted the newest cottonwood data it had, which is 3-5 trading days old.
2. **TYPE COVERAGE IS ASYMMETRIC ACROSS SCOPES.** `non-model-assets` exists ONLY under global.
   `aum-metrics` + `account-units` exist ONLY under cottonwood. **49financial and inflection have NEITHER.**
   A publisher built to a per-scope type list will silently under-publish whichever scope it was not modelled on.

---

## PART 2 -- IS THE PUBLISHER ACTIVE, WITH THE GRANTS REQUIRED?

`opal-assets-mdpf-portal-publisher` -- **State: Active**, LastModified 2026-07-23T19:28:42Z.
Env: `ASSETS_BUCKET=opal-data-assets`, `STAGING_ROOT=gold/mdpf_revamp`. **No destination-bucket variable exists.**

**Applied-plane role policy (`opal-assets-mdpf-portal-publisher-role`, inline `...-scoped`):**
```
ReadStagedMdpfGold          Allow  s3:GetObject   opal-data-assets/gold/mdpf_revamp/*
WritePortalServingPrefixes  Allow  s3:PutObject   opal-data-assets/json/mdpf/*
                                                  opal-data-assets/json/portfolios/*
ListReadAndWritePrefixes    Allow  s3:ListBucket  opal-data-assets
```
**Attached managed:** `opal-assets-one-way-fan-in-fence` - `AWSLambdaBasicExecutionRole`

**IAM SIMULATION, one `--resource-arns` per call, control in a SEPARATE invocation:**
```
TARGET   PutObject  opal-data-portal-v2/json/mdpf/global/aggregate-aua-timeseries.json
           -> explicitDeny   matched: opal-assets-one-way-fan-in-fence
CONTROL  PutObject  opal-data-assets/json/mdpf/global/aggregate-aua-timeseries.json
           -> allowed
```
**DISCRIMINATING.** *(My first control was WRONG -- I simulated PutObject on `gold/mdpf_revamp/*`, where the
role holds only GetObject, and got `implicitDeny`. That was my error, not the instrument's. Corrected above.)*

**FOUR DEFECTS:**
1. **WRONG SOURCE.** Reads `gold/mdpf_revamp/*` -- **NOT the canonical `portal/gold/mdpf/`.**
2. **WRONG DESTINATION.** Writes `opal-data-assets/json/*` -- **the portal serves `opal-data-portal-v2`.**
3. **EXPLICITLY DENIED from the destination**, by an ATTACHED managed policy. **An explicit Deny cannot be
   cured by adding an Allow.**
4. **NO SCHEDULE.** `list-rule-names-by-target` returns empty.

**Its actual output of record:** `opal-data-assets/json/mdpf/{49financial,cottonwood,global,inflection}/` --
global's `aggregate-aua-timeseries.json` last written **2026-07-23T15:30:00Z, 242,414 B.**

---

## PART 3 -- IS EVERYTHING WRITTEN TO `opal-data-portal-v2`? CAN A MANUAL TRIGGER ACHIEVE IT?

**NO, AND NO. I DID NOT FIRE IT, DELIBERATELY.**

A manual invocation today would read **07-23-era `gold/mdpf_revamp`** and write **`opal-data-assets/json/`**
-- **it would very likely return success.** It would not touch `opal-data-portal-v2`, and its Deny on that
bucket means even a re-pointed destination fails until the fence question is settled.

>> **THIS IS THE EXACT SHAPE OF THE INCIDENT WE ARE FIXING: a component that runs, succeeds, and writes
>> somewhere nobody reads. Firing it would have produced production evidence for a route that does not
>> exist.** <<

**Current portal-v2 state is UNCHANGED from the 13:41Z hand-restore:** six served keys intact, global
`5f758b47…` / 254,419 B, **frozen by design** -- Andrew ~1351Z decommissioned the legacy writer's automation
and no replacement publisher serves that bucket.

---

## WHAT WOULD ACTUALLY MAKE THE ROUTE FUNCTIONAL (ordered, dependency-forced)

1. **Close the silver -> gold gap for Cottonwood** (gold 07-20/07-22 vs silver 07-24/07-27). Until then the
   canonical gold is not current and anything published from it under-reports Cottonwood.
2. **Settle the destination architecture** -- CTO's A-2. Either the publisher writes `portal-v2` (**requires
   a deliberate, separately-reviewed change to the fence**, which is firm-separation-adjacent), or
   CloudFront re-points at `opal-data-assets` (**does not touch the fence**). **Architecture call, CTO's.**
3. **Re-point the publisher's source to the canonical `portal/gold/mdpf/`**, and make its type list
   **derived per scope**, not hand-modelled -- see the Part-1 asymmetry.
4. **Give it a schedule** (NEVER#4), with the event trigger as accelerator only.
5. **Then** it can be exercised, and only then is a manual QA fire meaningful.

**NOT DONE BY ME: no lambda fired, no IAM changed, no fence touched, no write to any serving bucket.**

-- `2.0.0_SA_COO`
