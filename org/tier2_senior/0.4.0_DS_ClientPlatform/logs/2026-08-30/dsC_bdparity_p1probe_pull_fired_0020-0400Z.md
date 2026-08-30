# Session 00:20-04:0xZ -- `0.4.0_DS_ClientPlatform~C` -- ADVI_BDPARITY P1-PROBE: the authorized pull FIRED, BP1-1 through BP1-4 delivered

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~C` | **Session:** post-reboot relaunch by MSTR, 00:20Z | **Project:** ADVI_BDPARITY, ONE project per Rule 27 | **Window:** whole session

---

## What this session was

Relaunched after a device reboot. Resumed from this lane's own 2026-08-29 close log and drove
`ADVI_BDPARITY.P1-PROBE` from "gated at Andrew" to **the pull fired and BP1-1 through BP1-4
delivered**. Andrew's per-use vendor word was discharged **exactly once**.

## Commits (8)

| hash | what |
|---|---|
| `076414c9f0` | BP1-1 pull extension preserved as a patch (lane-refused on `infra/aws`) |
| `28115a20b2` | BP1-1 re-pointed to CVO 84169 (SI always requested) + position-join helper |
| `fa82a129d8` | BP1-4 measurable half: the full-history load DOES NOT RUN |
| `b29b9f849b` | candidates-table annotations (superseded s.6 ask; the 535-partition sweep) |
| `5da9e7fffc` | linker: CVO ANNOTATION 2 (first-linkable coverage; BMV-0 rule), 26/26 arms |
| `6ae366e8c0` | BP1-4 correction: 10 columns not 14 (CRO caught it) |
| `5a0e1df70b` | BP1-2 harness, committed UNRUN with the reason |
| `cd7966658a` | **BP1-2 + BP1-3 delivered**: 20 cells, residual zero |

**PUSH STATE:** the first four are **on origin** (`branch -r --contains`, own read). `5da9e7fffc`
onward were LOCAL at last measure and ride MSTR's windows. Publication is the integrator's.

## The pull

**Fired ONCE, 03:05:19-03:05:40Z. StatusCode 200, no FunctionError.** 15 objects
(5 accounts x 3 endpoints) under `blackdiamond/49f/bronze/reporting_*/2026-08-30/`, **verified in S3
rather than from the function's own line**; the 07-17 snapshot untouched (negative control).
**All four ruled periods obtained**; BD honoured the mid-quarter `asOf`.

⛔ **THE FIRST INVOKE FAILED CLIENT-SIDE AND MADE NO CALL** -- `--cli-binary-format` is CLI-v2 and
this box runs v1.44.44. **Confirmed against the world (bronze unchanged) before retrying**, so the
one authorization was not spent twice. A tool rc is not a statement about the vendor.

## What I got right, and it mattered once

**I held a GO to fire.** COO's 84427 gate chain read "builder LANDED" and moved to the pull; the
DEPLOYED function predated the commit by 31 h, and `DRY_RUN` read **0** on it, so nothing mechanical
would have refused a wrong call. Firing then returns **2 of 4** ruled periods. COO corrected its own
GO within minutes and staffed the deploy. **The premise was checkable and nobody had checked it.**
I proved the staleness by **digest identity** (deployed member == the pre-BP1-1 blob), not by
timestamps, and **captured the prior package's digest before the deploy erased it** -- the negative
control the re-arm condition needed only existed in that window.

## Three corrections of my own, on the record

1. **"BD substitutes its own inception" (84141) -- REFUTED by the pull.** BD **echoes** the
   `startDate` we send, 5 of 5. The discriminator is 21089351's BMV **2,847.93** at the returned
   "SI" range -- an inception window opens at zero. **Face A3 FIRED on 4 of 5**: labelled SI,
   arithmetically QTD, nothing raised. I had called A3 "weakened". It was not.
2. **"The anchor source does not exist" (84932) -- FALSE, corrected within the hour.** It is
   `combinedLevels[].startDate`, positive control 22596361. **I looked in ONE field and concluded
   about the response.** CVO's two-pass design was right; annotation 1 named the wrong field.
3. **BP1-4's "10 columns not 14" -- PARTIAL, caught by `4.0.0_SA_CRO`.** My census reported columns
   with MORE THAN ONE TYPE; **an absent column contributes nothing to that map**, so an omission was
   invisible to it. **And the miss was in my own output** -- I printed "DISTINCT SCHEMA SIGNATURES: 2"
   and never opened what the second one was.

## The findings

- **The full-history load DOES NOT RUN** -- three partitions carry a reduced schema; the failure
  exists only in the UNION, so no slice can see it. A cast is insufficient: it cannot conjure an
  absent column. **Survived the re-emission** -> data property, not an emission-time gap.
- **twr_daily was RE-EMITTED under the probe** -- 529 of 535 rewritten inside one hour. **BP1-2 was
  HELD** rather than computed on a moving baseline, and rebuilt on the settled vintage
  @`03:22:17Z`.
- **The day-count gap closes to RESIDUAL ZERO**: QTD/YTD gap 6 = the 08-11..08-17 hole + all-null
  08-18; 1Y gap 7 = 6 + one boundary day.
- ⭐ **A one-day boundary mismatch WE authored** -- the puller asks BD for 1Y from 2025-08-28, the
  linker opened 2025-08-29. **Named, not tuned.** `1.0.0_SA_CTO` 85237 ruled ONE period convention
  for all four; the linker's 1Y open moves to it. **A definition delta, ours, not BD's.**
- **The BMV-0 rule reached n=3 from a DIFFERENT instrument** -- three accounts' first linkable day in
  OUR gold is exactly one trading day after their BD inception.

## Compiler Tools

`comp-find` for the `returnMethod` / `83426` / `trading_calendar` censuses (denominators printed
each time; the `--query length()` page-count trap caught and replaced with a client-side count).
`commit-gate.sh` on every `.py`. `safe-commit.sh -F` with non-shell-written message files.

## Blockers

**None on this seat.** The §7 classification thresholds need `4.0.0_SA_CRO`'s N-bp word (the issuer
is re-spawning that seat for the one act); the 1Y-open correction rides a cell the issuer cuts.
**Both are named, owned elsewhere, and correctly gated -- not a stall.**

## Next Steps

1. **[`0.4.0_DS_ClientPlatform~C`]** BP1-5 proof instance (this session), then the 1Y-open
   correction + BP1-2 re-run with the signed before/after when the issuer's cell lands.
2. **[`4.0.0_SA_CRO`, on re-spawn]** the N-bp thresholds for the 20-cell table.
3. **[Andrew]** card D2-T69-R2 -- non-blocking in fact; it decides who owns selection going forward.
