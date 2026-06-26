# DRAFT: cot holdings valued-re-pull RETRY NET (DATEMODE-B forward-fix)

**Status:** DRAFT for CTO arch-gate + DS co-author (cot_bronze_ingest.py owner). Author: 0.7.0_AE_CloudOps.
**Project:** ADVI_COTETL.AUAFIX-DATEMODE-B (forward-fix / recurrence-prevention).
**Gate chain:** CTO steer 20260626T145510Z (retry-net over a fixed T+1 shift) + COO 145753Z (today-urgent: without it tonight's nightly re-freezes 06-26). DS co-authors; CTO arch-gates this draft BEFORE deploy.

## Problem (confirmed mechanism, not hypothesis)
Probe d92b5b21 proved: BD prices a business day's holdings at ~T+1 (all biz days 06-22..06-25 priced by 06-26; same-day T+0 is unpriced). The scheduled bronze holdings pull runs SAME-DAY (T+0) -> nzf<0.5 -> HOLDINGS_COMPLETENESS_FLOOR correctly REJECTS -> the day never lands. Nothing ever re-pulls that day once BD prices it at T+1. Result: holdings (and served firm-AUA) freezes at the last day that happened to be priced-at-pull-time. The floor is CORRECT (never land unpriced $0-MV); the gap is that there is no RE-PULL of the now-priced day.

A fixed T+1 shift (pull yesterday instead of today) is simpler but BRITTLE: a T+2 pricing day or a post-holiday settle would re-freeze. The retry net is cadence-variance-tolerant + self-healing + auto-backfills gaps, and doubles as the e2-defect detector.

## Design: valued-re-pull retry net (holdings only)
Each scheduled bronze run, BEFORE/ALONGSIDE the normal holdings leg, run a bounded backfill sweep over the last N business days:

```
for d in last RETRY_NET_LOOKBACK_BDAYS business days (newest..oldest), excluding today (T+0):
    if forwardfill_v2/holdings/HOLDINGS_DAILY_{d}.xlsx ALREADY EXISTS:  # floor passed at land-time => already good
        continue
    re-pull holdings @ d via the standard floor-gated ingest_table  # lands IFF nzf>=0.5 (priced)
    # missing + now-priced -> lands; missing + still-unpriced -> floor rejects, stays missing (retried next run)
```

Invariant that makes the existence-check sound: with the floor in place, HOLDINGS_DAILY_{d}.xlsx exists ONLY for priced days (land_to_s3 is only reached when nzf>=0.5). So "missing" == "not-yet-priced-and-landed". The sweep lands each day the moment BD prices it (T+1), self-healing without ever bypassing the floor.

### e2-defect detector (the second job of the same mechanism)
After the sweep, any business day OLDER than CADENCE_BDAYS that is STILL missing == BD has not priced a day it should have == e2 SOURCE defect (not honest T+0/T+1 lag). Emit an alarm:
```
stale = [d for d in business days older than CADENCE_BDAYS if HOLDINGS_DAILY_{d}.xlsx missing]
if stale: publish SNS (cot-holdings-pricing-defect) with the stale dates  # -> COO vendor/source branch
```
One mechanism => self-heal AND defect-detection. (Today's manual backfill 06-23/24/25 was a one-shot instance of exactly this sweep.)

## Params (CTO to set/confirm)
- `RETRY_NET_LOOKBACK_BDAYS` (N): proposed 5. Bounds the sweep cost (<=5 extra BD pulls/run, each ~seconds).
- `CADENCE_BDAYS` (T+N defect threshold): proposed 2 (a biz day >2 business days old still missing = defect). Derived from the observed ~T+1 cadence + 1 buffer biz day.
- Business-day calc: weekday check + the existing holiday-gap awareness (reuse `_window_for`'s holiday-floor intent / a US-market holiday list). DS to wire to whatever cot already uses.
- Alarm: new SNS topic `cot-holdings-pricing-defect` (or reuse 0.6.0's L4 cot-detection SNS). Wire = AE/infra (me) once DS lands the emit call.

## Scope + ownership
- HOLDINGS ONLY. The other 4 tables (transactions/allocations/realized/unrealized) advance fine (no T+0 pricing gap); do NOT add the sweep to them.
- INSIDE cot_bronze_ingest.py -> DS owns the code/commit; I (AE) draft + wire the SNS/infra; CTO arch-gates.
- Must preserve: the floor (never weaken), `from __future__ import annotations`, firm-sep guard, no DRY_RUN/override land.

## Open questions for CTO/DS
1. Sweep placement: a standalone `--backfill-holdings-net` invocation in the nightly SSM chain, vs inline in the default holdings leg of main()? (Standalone is cleaner to gate + audit; inline is one-fewer dispatch.)
2. Does the same-date-key overwrite interact with the silver dedup/merge correctly when a day re-lands after a partial? (Today: full 825KB overwrote the 554KB partial cleanly; confirm silver merge picks the overwrite by mtime/content.)
3. Should CADENCE_BDAYS account for market holidays explicitly (a holiday day should never be "expected priced")?

## Acceptance
Deployed retry-net => the nightly self-heals: a T+0-rejected day auto-lands at T+1 on the next run, served firm-AUA tracks the priced frontier without manual backfill, and a genuine source defect (settled day unpriced past cadence) alarms to COO. Verified by: a simulated missing-day (or the next real T+0 cycle) self-backfilling on the following run, served advancing without intervention.
