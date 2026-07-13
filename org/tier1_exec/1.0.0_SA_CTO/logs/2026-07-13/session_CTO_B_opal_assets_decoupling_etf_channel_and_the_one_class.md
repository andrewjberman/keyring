# CTO~B -- OPAL_ASSETS: the decoupling, the laptop channel, and THE ONE CLASS

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, TRACE, COORDINATE, SCRIBE

**Agent:** `1.0.0_SA_CTO~B` (lane ~B; base-serial folder)
**Window:** 2026-07-13 ~21:36Z -> ~22:45Z (session start -> this log)
**Scope:** OPAL_ASSETS macro-project ONLY (Andrew `8.) A` via CTO). INF chain HELD throughout.

---

## Summary

Back under Andrew's `8.) A`, scoped to OPAL_ASSETS. Took the macro-project owner seat, grounded
the two leads MSTR handed me, and drove PRD v0.2 -> v0.9 (seven versions, all pushed). **Nothing
was built. Door 6 was never opened -- I did not write `s3://opal-data-inf/gold/meta/pipeline-complete.json`.**

**The session's real finding, which every other finding turned out to be an instance of:**

> **EVERY DISCLOSURE IN THIS ESTATE IS WRITTEN BY SOMEONE WHO COULD SEE THE DEFECT, AND READ BY NOBODY.**

Seven instances, all source- or live-confirmed:
1. `etf_probe.py` stamps `staleness_days` on every row -> **dropped at the parquet boundary** (`:113`).
2. The mdpf ETF feeder writes `as_of_date`, calls it *"audit-visible"* -> **nothing audits it**.
3. `sentinel_1_cohort0_dod` fires at **559.7%** (an 11x breach) -> **"audit-only, non-blocking"**.
4. `identity_2_etf_residual` is **DIRECTIONAL** -- catches over-attribution; the failure went the
   one way it cannot see.
5. `etf_probe.py:948-953` swallows an S3 upload failure -> WARN -> **exit 0**. The producer can
   succeed at producing and **fail at delivering, and report success**.
6. `partner_held_etf` is EXCLUDED from `vintage_bearing_feeders` for a GOOD reason -- so it cannot
   distinguish *"rolled forward 3 days by design"* from **"GONE ENTIRELY"**.
7. **TERMINAL FORM:** `coverage_state: incomplete` has correctly disclosed the estate's largest gap
   on every row for **427 partitions** -- and it is a **BOOLEAN**, so it is structurally incapable of
   conveying that it is worth **~$1.7 BILLION**.

---

## What I did

### 1. Falsified the two claims I was handed (both reached Andrew as fact)
- **"Andrew's laptop was off tonight -- 27% of the AUM stopped updating."** FALSE. Live
  `Get-ScheduledTask`: `State: Ready`, `LastTaskResult: 0`, `NumberOfMissedRuns: 0`,
  `NextRunTime 18:00 ET` -- read at **17:44 ET**. A healthy producer, 16 minutes from its next run,
  read as dead off a wall clock. **NEVER#1.** MSTR retracted to Andrew.
- **"A value reads fresh while stale with nothing saying so."** FALSE **at the probe**.
  `etf_probe.py` is the best-behaved component in the chain. **Aiming the fix there would have
  hardened the one thing that works.**

### 2. Found the real defect -- in the CONSUMER
`data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py:126-131` @ `d971650a3` is an
**UNBOUNDED roll-forward**; its only errors are zero-rows (`:217`) and missing-ticker (`:220`), so a
**6-day-stale valuation prints `OK: all 4 Opal ETFs present`** (`:231`). Its rationale (*"NAV does not
move on a non-publishing day"*) is **correct for a market holiday and catastrophic for a dead
producer -- and the code cannot tell them apart.**

### 3. Measured it (canonical, denominator printed, then RECONCILED under MSTR's STOP)
```
S3: opal-data-etfs/silver/netassets/  CAL: lib/trading_calendar.py (NYSE)
WINDOW 2026-06-01 -> 2026-07-10 inclusive   DENOMINATOR 28 trading days
MISSING 10 = 35.7%   BLACKOUT = 5 CONTIGUOUS TRADING DAYS (07-01,02,06,07,08)
```
Two agents published different counts of the same scan and **both reached Andrew**. The other
figure (11/29 = 38%) **counted 2026-07-03 -- Independence Day observed -- as a trading day**; one
mis-classified holiday inflates numerator and denominator together. **A failure to resolve the
trading calendar, inside our own measurement of a failure to resolve the trading calendar.**

### 4. G7 SELF-CORRECTION -- I almost shipped a fake fix on my own lead item
I specced G7 as *"give OPAL_ASSETS its own cron."* Source (`mdpf-daily-trigger/lambda_function.py:506,
509, 538-541`): `run_date = inf.get("as_of")`, and *"ONLY THE DRIVER HALTS. A stale spine defers."*
**INF is not merely the trigger -- INF is the CLOCK.** A cron would fire daily and **DEFER daily**.
> **A FAKE FIX THAT BURNS THE LEGITIMATE PATH LEAVES DOOR 6 AS THE ONLY REMAINING EXPLANATION --
> AND HANDS IT TO SOMEONE WHO HAS JUST ELIMINATED THE ALTERNATIVE.**
G7 split: **G7a (cron)** safe/insufficient; **G7b (remove INF-as-driver)** = the real decoupling,
**HARD-GATED ON AC11** because it un-freezes the $528mm and re-emits it daily.

### 5. Closed DS's last INFERRED link -- on the Opal side, no held surface touched
`mdpf-daily-trigger:508-521`: **a stale partner's feeders are SKIPPED, BY DESIGN.** Full chain:
`G1 stale -> bd.fresh=False -> stale_partners=[49financial] -> SKIP feeders -> partner_held_etf
absent -> 49F drops out -> residual absorbs $528mm.` And `:517-519` documents the skip as *"what
makes the roll-forward safe ... it cannot fabricate a residual."*
> **"IT CANNOT FABRICATE A RESIDUAL." IT FABRICATED A $528 MILLION RESIDUAL.**
The skip protects the partner's AUA **block**; `etf_decomposition` is **not in that block** -- it is
re-derived from the feeder the skip just removed.

### 6. Rulings issued
- **Cohort 8/9 (C), STRUCTURAL not a rename** -- row 8 was doing TWO JOBS (the additive partner-total
  AND an account cohort named for a master it does not read). **SOVEREIGN-VALIDATED**: Andrew
  independently described the exact taxonomy (*"there are two 49F Buckets ... we need to track both
  figures"*), unprompted. Rejected rebinding cohort 9 (it would destroy `model_aua`, a correct
  quantity, to satisfy a label).
- **AC11 firm-generic** (declared partner set, never a hard-coded firm id); **AC12** directional gates
  + a fired sentinel must BLOCK; **AC14 MIGRATION INVARIANT**; **AC15** conservation identity;
  **AC16** provenance survives the component grain; **AC17** re-cut (below).

### 7. Folded two sovereign rulings + corrected my own contradiction
- **Andrew #1:** *"record all the components granularly ... how we sum them is dependent on the
  presentation case."* **`additive` is not a property of an asset -- it is a property of the QUESTION.**
  I had frozen a presentation decision into storage. **R-A (my stored `additive` boolean) RETIRED.**
- **Andrew #2:** *"do not focus on how to sum ... canonical storage location and robust ingestion."*
  **This invalidated AC17, which I had landed ten minutes earlier.** AC17 v1 said the store must
  assert a MAGNITUDE -- a magnitude is a TOTAL, and Andrew's own ruling two screens above says **a
  total is not a primitive**. **I wrote an AC that contradicted the sovereign ruling I was citing.**
  **Re-cut: RECORD THE IDENTITY. DO NOT RESOLVE THE SUM.** It then collapses cleanly into AC4 --
  *the $1.7B was unpriceable because the IDENTITY CHANNEL IS DEAD, not because the number was hidden.*

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-which | `comp-which "where is the ETF net assets probe..."` | **WARN** | all-zero-ish score vector, near-tie, top score 0.33 -- correctly REFUSED to guess and routed to `comp-grep`. The argmax-as-confidence defect ~Z is redesigning, observed live. |
| comp-which | `comp-which "what does mdpf-daily-trigger dispatch"` | **WARN** | same near-tie; fell through to direct source read. |
| comp-grep | `comp-grep "opal-data-etfs"` | **PASS** | found the consumer (`build_mdpf_wsd2_etf_netassets_feeder.py:15`) that raw grep would have surfaced without the dependency context. Also printed its own denominator: *"972 sovereign-held path(s) EXCLUDED"* -- correct, and correctly disclosed. |
| comp-surface-check | auto via `safe-commit` (x7) | **PASS** | `OK: no critical surface` on every PRD commit. |
| lib/trading_calendar.py | `trading_days_between` / `is_trading_day` | **PASS** | THE instrument of the session. Produced the canonical 10/28, killed the phantom 07-03 "outage day", and reframed a "3-day" gap as a **5-trading-day** blackout. |
| live AWS primitives | `aws events list-rules`, `lambda get-function-configuration`, `s3 ls`, `Get-ScheduledTask` | **PASS** | Rule 22a APPLIED-truth grounding. `Sched: null` on `mdpf-daily-refresh-trigger` is the whole G7 finding. |

**What worked:** the trading calendar as an *offensive* instrument -- I used it to FIND the outage,
not to excuse one. The `safe-commit` `-m`-with-`$(` gate **fired on me and was right** (LD-0276);
`-F` was the correct path and my earlier grep had misread the flag.
**What failed:** `comp-which` returned an all-low-score near-tie on both natural-language questions.
It did NOT dead-end (it routed to `comp-grep`), so the rail held -- but the routing signal was noise.
**Gap found:** **`comp-pipescript deployed` is structurally blind to `etf_netassets_watch/`** -- the
channel is not under `data/*/scripts/`, so it has NEVER been scanned, and it reports CLEAN.
*An oracle that never scans a path prints a clean bill of health for it.* Landed as G8 step 5.

---

## Files Modified

See commit messages: `9d30e2613` (v0.3), `fb7e7aa3a` (v0.4), `1db3c37eb` (v0.5), `7eb44c01c` (v0.6),
`348536722` (v0.7), `31ca56df8` (v0.8), `1ca7ef1a3` (v0.9).

| File | Change |
|---|---|
| `docs/architecture/OPAL_ASSETS_PRD.md` | v0.2 -> v0.9. New: SS3h (G7 decoupling + the two couplings), SS3i (staleness ceiling), SS3j (the laptop channel), SS3k (one row, one job), SS3l (vintage + ENTITY alignment), SS3m (a fired guard must block), SS3n (the migration arms the mine), SS3o (conservation identity), SS3g-0 (Andrew's component-grain ruling). AC8-AC17. Guardrails 9-12. |
| `org/projects/OPAL_ASSETS.json` | phase/blocking/prds tracking v0.9. |

## MCP traffic
**16 messages** (9 sent / 7 received). Significant: ETF-channel grounding + falsification -> MSTR
(retracted to Andrew); cohort-8/9 **RULING (C)** -> DS (sovereign-validated an hour later);
**co-sign** of `0.5.0_AE_OpalETL`'s ETF cloud-lift landing shape; **G2 fences** -> `0.6.2_AE_PartnerETL`
(Andrew-tasked with the 0833 ETL) + same-turn scope correction; **AC14 x Cottonwood interlock** -> CTO
(who then ORDERED the guard precedes Cottonwood); canonical-count reconciliation -> MSTR + COO.

---

## Blockers

**None owned by me.** P0 (G7a + G8-bronze) is fully Opal-side and waits on nothing; two lanes are
building with my co-sign. **Awaiting Andrew:** GO on PRD v0.9's G7/G8, and the cohort row-count
(the taxonomy disentangling is his call, not mine -- surfaced, not adjudicated).

---

## Current State (zero-prior-context handoff)

- **PRD:** `docs/architecture/OPAL_ASSETS_PRD.md` **v0.9** @ `1ca7ef1a3`, pushed to CLOUD.
  Companion schema: `docs/architecture/OPAL_ASSETS_COMPONENT_GRAIN_SCHEMA.md` @ `0cafd3f6f` (CTO).
- **INF CHAIN: HELD.** I never wrote `s3://opal-data-inf/gold/meta/pipeline-complete.json`.
  `mdpf-daily-refresh-trigger` is **ENABLED with `Sched: null`** -- its ONLY trigger is
  `s3:ObjectCreated` on that key. **Writing it dispatches the held INF gold chain.**
  CTO's bucket-policy **Deny** on that key is Andrew-GO'd and **NOT YET LANDED** -- until it is, the
  door is held shut by people knowing not to touch it, **which is an agreement, not a control.**
- **DOOR 6 IS NOW AT ITS MOST TEMPTING.** The frozen mdpf artifact **froze in a BROKEN state** (a real
  ~$528mm 49F misattribution on the 07-10 partition), so the repair now looks **RESPONSIBLE** rather
  than reckless. It says "mdpf" and "ETF" and **never says "INF."**
  **A VERIFIED DEFECT IS NOT A LICENCE. A KNOWN-WRONG FROZEN NUMBER IS STRICTLY SAFER THAN AN
  UNHELD PIPELINE.** Bounded + safe to leave: headline ties at $0.00; G4 reads `ETFS_CANON`, not
  `etf_decomposition`; the artifact is frozen, so the error is **static and not spreading.**
- **Lanes in flight:** `0.5.0_AE_OpalETL` = ETF laptop->cloud lift (**bronze in the SAME change**,
  co-signed; raw bytes written BEFORE the parse and the parse reads THOSE bytes).
  `0.4.0_DS_ClientPlatform` = the emitter + AC11/12/14 guard specs.
  `0.6.2_AE_PartnerETL` = the 0833 (Black Diamond) ETL, **Andrew-tasked**.
- **CTO ORDER:** the firm-generic feeder guard **LANDS AND IS EXERCISED BEFORE COTTONWOOD.**
- **Magnitudes are UNQUOTABLE (guardrail 11):** every available partition mixes vintages.
  **Andrew gets the QUESTION, not a FIGURE.**

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** Pick: (i) the AC11 firm-generic guard against **cot's actual feeder
   shape**, dry, ahead of Cottonwood (CTO's critical path), or (ii) the **master-manifest** producer
   requirement -- **one field that closes AC4 + AC17 and un-blinds a $1.7B disclosure.** I lean (ii).
2. **[0.5.0_AE_OpalETL]** Land bronze + the parquet-boundary `staleness_days`; **exercise AC10
   (re-derive a past day from bronze ALONE)**; parity >=3 trading days before the Windows task is
   touched. Report with evidence.
3. **[0.6.2_AE_PartnerETL]** 0833 ETL design -> me before deploy. **CBUGL != RPS (new converter).**
   The headline will roughly DOUBLE -- **that is a never-widen event, not a bug fix.**
4. **[1.0.0_SA_CTO]** **LAND THE BUCKET-POLICY DENY** on the sentinel key. I am the person it is
   aimed at.
5. **[Andrew]** GO on PRD v0.9 (G7a + G8-bronze are Opal-side and unblocked); the cohort row-count.
