# DEPLOY LEDGER -- harvest TABLE migration + superseded-module retirement

**Status: CLOSED -- COMPLETE AND VERIFIED** (opened and closed 2026-09-11 ~20:1xZ by `4.0.0_SA_CRO~Z`)
**Module:** `infra/aws/terraform/harvest/` | **State:** `harvest/tfstate`
**Authority:** Andrew ~19:5xZ, VERBATIM: *"pause, CRO is going to remediate with full authority"*, on
the harvest / rename / migration surface. Preceded by *"buckets would be opal-data-harvest, and so
on"* and *"live refs only"*.

## WHAT WAS REMEDIATED, AND WHY IT WAS NOT JUST A RENAME

| resource | before | after | how |
|---|---|---|---|
| S3 store | `opal-data-research`, 53 objects | `opal-data-harvest`, 53 objects | migrated, verified, source deleted (earlier entry `20260911T1915Z`) |
| article table | `opal-amgt-articles`, 0 rows | `opal-harvest-articles`, 0 rows | create-only apply, source dropped |
| metrics table | `opal-amgt-security-metrics`, **42 rows** | `opal-harvest-security-metrics`, **42 rows** | create, copy, **verify on full item equality**, cut over, drop |
| 4 code sites | hardcoded table names | env-overridable, defaults on harvest names | `HARVEST_ARTICLES_TABLE` / `HARVEST_METRICS_TABLE` |
| `terraform/research/` | declared bucket + queue + enqueue path | **RETIRED** | all five resources live in `harvest/` |
| `terraform/amgt-resapp/` | declared both tables | **table declarations removed** | `rd-5`'s live chatter schedule deliberately kept |

## ⛔ THE FINDING THAT CHANGED THE ACT -- ItemCount IS A ~6-HOURLY CACHE

The approved plan said *"rename the tables while they are empty, it is cheap today"* -- **this seat's
own line, on `describe-table -> ItemCount 0`, repeated for hours by three seats.**

```
describe-table  opal-amgt-security-metrics  ItemCount -> 0
scan --select COUNT                         -> 42
```

Those 42 are `AMGT-rd-6`'s 32 PRICE rows beside `AMGT-rd-5`'s 10 CHATTER. **A DynamoDB rename is a
DESTROY/RECREATE, so the approved act would have silently dropped the first real output of two
round-5 cells.** Both reads come from the live AWS API; only one of them is live. Caught by
re-checking the seat's own standing advice before acting on it.
⚠ **`opal-harvest-articles` was genuinely empty on both reads** -- the cached number was not wrong
everywhere, which is what makes it dangerous.

## ⛔ THE HAZARD IN THE RETIRED MODULES, AND ITS DIRECTION

A resource in CONFIG **and** in STATE whose real table is gone plans a **CREATE**. Leaving
`amgt-resapp/dynamodb.tf` in place after its tables moved would have **RECREATED the old-named tables
as duplicates** on the next apply in that directory -- silently re-introducing the exact ambiguity
this remediation removed. Deleting the declarations flips it to the safe direction: state-without-
config plans a DESTROY of something already gone, a harmless no-op.

**KEPT DELIBERATELY:** `amgt-resapp/chatter-axis-schedule.tf` + `lambda_src/` + `main.tf` --
`AMGT-rd-5`'s LIVE scheduled producer, landed *after* this consolidation began. It is a separate
consolidation, not dead code; removing it would have taken out a live scheduled producer.

## FINAL VERIFICATION -- negative AND positive, because a 404 alone proves little

```
opal-amgt-articles          -> ResourceNotFoundException   GONE
opal-amgt-security-metrics  -> ResourceNotFoundException   GONE
opal-harvest-articles       -> ACTIVE, 0 rows              (positive control)
opal-harvest-security-metrics -> ACTIVE, 42 rows           (positive control)
opal-data-harvest           -> 53 objects
terraform validate (harvest) -> Success
terraform plan -detailed-exitcode -> rc=0, NO DRIFT
comp-find --band DEF over all three old names -> 5 hits, ALL of them
  deliverables/<serial>/ worker PROOF ARTIFACTS. ZERO live references.
```

The 42-row copy was verified on **FULL ITEM EQUALITY**, not key sets -- 42/42 keys AND every
attribute, plus a negative control. A key-only check passes with a wrong payload.

## THE ORDERING RULE THIS WHOLE REMEDIATION RAN ON

**At no point may a live consumer's resolved target fail to exist.** Knob first (env-overridable,
defaults unchanged) -> create destination -> copy -> verify -> flip defaults -> commit -> drop source.
Every destructive act was last and was gated on a check taken immediately before it.

⭐ **That ordering absorbed two real mistakes tonight** -- a stale-fallback straggler in
`pull_enqueue` that both this seat and `1.0.0_SA_CTO~Z` talked past, and the ItemCount cache. Neither
reached production because the destructive half was always last and always gated.

## STILL OPEN, NAMED

- `RESEARCH_BUCKET` stays as a transition env key on the enqueue Lambda until it is next rebuilt from
  current source; `HARVEST_BUCKET` is set alongside it so neither the running bytes nor the next
  build can lose the value.
- Three stale terraform state objects (`research/tfstate`, `amgt-resapp/tfstate`,
  `amgt-resapp/rd-2-security-metrics/tfstate`) remain in the state bucket. Inert -- their module
  directories no longer declare those resources -- but they should be cleaned up.
- `AMGT-rd-5`'s chatter schedule consolidating into `harvest/` is a separate act.
- `.tools/surprise-row-gate.py` precondition-limb fix is `1.0.0_SA_CTO~Z`'s, confirmed by this seat
  and awaiting a self-test arm that fails on current code.
