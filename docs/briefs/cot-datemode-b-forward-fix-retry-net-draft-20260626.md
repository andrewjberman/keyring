# DRAFT: cot holdings valued-re-pull RETRY NET (DATEMODE-B forward-fix)

**Status:** REVISED v2 per CTO CONDITIONAL-GREEN 20260626T150804Z (3 hard conditions folded in). For DS co-author (cot_bronze_ingest.py owner, owns Conditions 1+2) -> revised-draft RAVC back to CTO + DS's silver proof BEFORE deploy. Author: 0.7.0_AE_CloudOps.
**Project:** ADVI_COTETL.AUAFIX-DATEMODE-B (forward-fix / recurrence-prevention).
**Gate chain:** CTO steer 145510Z -> draft 9ad287d0f -> CTO conditional-GREEN 150804Z (Cond 1 content-grounded skip / Cond 2 silver-replace-DS-proof / Cond 3 holiday-aware; params + placement confirmed). DS co-authors; CTO arch-gates the revised draft + DS silver proof BEFORE deploy. NOT tonight-rushed (served holds at 06-25 tonight).

## Problem (confirmed mechanism, not hypothesis)
Probe d92b5b21 proved: BD prices a business day's holdings at ~T+1 (all biz days 06-22..06-25 priced by 06-26; same-day T+0 is unpriced). The scheduled bronze holdings pull runs SAME-DAY (T+0) -> nzf<0.5 -> HOLDINGS_COMPLETENESS_FLOOR correctly REJECTS -> the day never lands. Nothing ever re-pulls that day once BD prices it at T+1. Result: holdings (and served firm-AUA) freezes at the last day that happened to be priced-at-pull-time. The floor is CORRECT (never land unpriced $0-MV); the gap is that there is no RE-PULL of the now-priced day.

A fixed T+1 shift (pull yesterday instead of today) is simpler but BRITTLE: a T+2 pricing day or a post-holiday settle would re-freeze. The retry net is cadence-variance-tolerant + self-healing + auto-backfills gaps, and doubles as the e2-defect detector.

## Design: valued-re-pull retry net (holdings only)
Each scheduled run (standalone `--backfill-holdings-net` step, Q1/CTO), run a bounded backfill sweep over the last N business days:

```
for d in last RETRY_NET_LOOKBACK_BDAYS BUSINESS days (newest..oldest), excluding today (T+0) and holidays:
    if holdings @ d has a COMPLETE (priced) landed snapshot per its completeness sidecar:  # CONTENT-grounded
        continue
    re-pull holdings @ d via the standard floor-gated ingest_table  # lands IFF nzf>=0.5 (priced)
    # missing/incomplete + now-priced -> lands; + still-unpriced -> floor rejects, stays incomplete (retried next run)
```

### CONDITION 1 (CTO headline) -- the skip MUST be content-grounded, NOT bare existence
**My first draft's `if EXISTS: continue` was UNSOUND -- the same mtime-not-content trap we just hit.** Falsifying evidence (my own): a 554KB sub-floor PARTIAL 06-23 file EXISTED and the 825KB full overwrote it. So a file CAN exist while being a stale partial/carry-forward -> bare existence-skip would skip that day FOREVER and never re-pull the now-priced full = a silent permanent freeze on that day. FIX (CTO-mandated PROPERTY): skip only on a COMPLETE landed snapshot, content-grounded. Primitive (pick with DS):
- **Proposed: a land-time COMPLETENESS SIDECAR.** When `land_to_s3` fires (post-floor, so nzf>=0.5), also write `forwardfill_v2/holdings/_complete/{date}.json` = `{date, nzf, landed_at, bytes}`. The sweep skips a day IFF its sidecar exists AND sidecar.nzf>=floor; else re-pull. (Alternatives DS may prefer: re-read the landed xlsx nzf each sweep [costlier], or an existing silver/bronze manifest if one already records per-date completeness.) CTO mandates the property (content-grounded skip); DS + I pick the primitive.
  - **ORDERING INVARIANT (CTO 151529Z, load-bearing):** write the sidecar ONLY AFTER `land_to_s3` returns success -- NEVER before/independently. The asymmetry: land-ok + sidecar-write-fails -> day looks incomplete -> re-pulled next run = SAFE (re-pull idempotent); but sidecar-before-land -> a failed land leaves a FALSE-complete sidecar -> day skipped forever = the silent-freeze we're killing. Invariant: `sidecar-exists IMPLIES land-succeeded`. And derive nzf from the SAME computation the floor used (`_holdings_nonzero_mv_fraction` result, passed through) -- one source of truth, no recompute drift.
- **Bonus:** this auto-heals any legacy sub-floor partials already on disk (no sidecar / sidecar-incomplete -> re-pulled).

The sweep then lands each day the moment BD prices it (T+1), self-healing, never bypassing the floor, never fooled by a stale partial.

### e2-defect detector (the second job of the same mechanism)
After the sweep, any business day OLDER than CADENCE_BDAYS that is STILL incomplete (no complete sidecar) == BD has not priced a day it should have == e2 SOURCE defect (not honest T+0/T+1 lag). Emit an alarm:
```
stale = [d for d in business days older than CADENCE_BDAYS (holiday-excluded) if NOT complete-per-sidecar]
if stale: publish to 0.6.0's L4 cot-detection SNS, subject "cot-holdings-pricing-defect", with the stale dates  # -> COO
```
One mechanism => self-heal AND defect-detection. (Today's manual backfill 06-23/24/25 was a one-shot instance of exactly this sweep.) ALARM uses 0.6.0's EXISTING L4 cot-detection SNS with a DISTINCT subject (CTO: no new-topic sprawl; COO keeps one cot-detection channel) -- coordinate the subject wiring with 0.6.0.

### CONDITION 2 (CTO hard gate -- DS owns) -- silver dedup must REPLACE, not union/keep-first
The net makes re-lands ROUTINE (today was one-shot). The silver holdings dedup MUST deterministically REPLACE a same-date partial with the re-landed FULL snapshot -- NOT union (double-counts AUA) and NOT keep-first (keeps the partial). DS must: READ the silver holdings dedup (Rule 17 = dedup+dtype only), PROVE the pick is by (date,security)->latest-complete, and TEST it (land partial, then full re-land -> silver has full rows only, count correct). HARD GATE: a re-land that double-counts AUA is worse than a 1-day-later durable fix. Content-not-self-report -- do NOT assume "overwrote cleanly"; prove the merge.

## Params (CTO-CONFIRMED 150804Z)
- `RETRY_NET_LOOKBACK_BDAYS` = **5** (sweep bound; <=5 extra BD pulls/run, each ~seconds).
- `CADENCE_BDAYS` = **2** (defect threshold; observed ~T+1 + 1 buffer biz day). CADENCE(2) < LOOKBACK(5) so the net is still actively retrying a day at the point it would alarm (CTO Condition 3).
- Business-day + holiday calc (CONDITION 3): holiday-aware for BOTH params; reuse cot's EXISTING holiday source (`_window_for`'s intent), do NOT roll a new one. A holiday is never "expected priced" -> excluded from both the sweep (don't chase a no-data day) and the defect threshold (no false e2 alarm).
- ALARM: reuse 0.6.0's L4 cot-detection SNS, DISTINCT subject `cot-holdings-pricing-defect` (no new-topic sprawl). Wire with 0.6.0.

## Scope + ownership
- HOLDINGS ONLY. The other 4 tables advance fine (no T+0 pricing gap); do NOT add the sweep to them.
- INSIDE cot_bronze_ingest.py -> DS owns code/commit (incl. the sidecar write at land_to_s3 + the silver-dedup proof, Condition 2); I (AE) draft + wire the SNS/infra + the standalone SSM step; CTO arch-gates.
- Must preserve: the floor (never weaken), `from __future__ import annotations`, firm-sep guard, no DRY_RUN/override land.

## Open questions -- RESOLVED (CTO 150804Z)
1. Placement -> **STANDALONE `--backfill-holdings-net` SSM step** (separable failure domain: a sweep failure doesn't fail the primary nightly holdings leg; own log/rc; ad-hoc runnable like today; cleaner to gate+audit).
2. Silver merge correctness -> **CONDITION 2** (DS proves the dedup REPLACEs a same-date partial; hard gate, don't deploy until proven).
3. Holidays -> **YES, explicit (CONDITION 3)**.

## Sequencing (CTO-corrected -- NOT a tonight-emergency)
The FAST-PATH (06-23/24/25 backfill) lands FIRST + closes #1 today (served=06-25). The retry-net is NOT rushed: CTO corrected the urgency -- tonight's nightly floor-rejects 06-26 but LEAVES 06-25 landed, so served HOLDS at 06-25 (alarm-tuned T+1-aware), it does NOT re-freeze. So land the retry-net PROPERLY-GATED (Conditions 1+2 resolved with DS), not tonight-rushed.

## Acceptance
Deployed retry-net => the nightly self-heals: a T+0-rejected day auto-lands at T+1 on the next run (content-grounded skip, never fooled by a stale partial), served firm-AUA tracks the priced frontier without manual backfill, silver REPLACEs partials (no AUA double-count, Condition 2 proven), and a genuine source defect alarms to COO. Verified by: land a partial then full re-land -> silver has full rows only / count correct (Condition 2 test); and the next real T+0 cycle self-backfilling on the following run.
