# Session log — 0.4.0_DS_ClientPlatform~A — 2026-07-29 2130Z-2140Z (chain closed, client-visible)
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Window:** continues `lane_A_gold_refresh_and_bridge_hold_1910-2130Z.md` @`fb4ac552b1`.
**Zero commits before this log** -- the window is verification and a stand-down, not production.

## THE CHAIN CLOSED. THE REPAIR IS ON THE SERVED PLANE.

`platinum/mdpf/cottonwood/aggregate-aua-timeseries.json`, read from the NAMED fields:

```
                          BEFORE        AFTER
model_aua                  2/450    ->  50/450    2026-05-28..07-27
non_model_aua              0/450    ->   6/450    2026-07-20..07-27
partner_custody_total      0/450    ->  38/450    2026-06-09..07-27
meta.composed_backfill    ABSENT    ->  PRESENT
meta.non_model_aua_status "NOT_MEASURED (Rebalancer carries model assignment only)"
                                    ->  "BALANCE = partner_custody_total - model_aua, derived where BOTH present..."

49financial / inflection / global   as_of_last 07-27 -> 2026-07-28
                                   n_dates 432/432/450 -> 433/433/451
                                   _provenance.source_keys -> .../2026-07-28.json
cottonwood                         as_of_last 2026-07-27 UNCHANGED (correct; declared carry)
```

**The `NOT_MEASURED` fossil is retired** -- the served copy now carries the producer's real status
string, exactly as I warned DE would happen when I told it not to key off that literal.

**Verified INDEPENDENTLY of AE's report**, on `as_of_last` + `dates[-1]` + `n_dates` +
`_provenance.source_keys`, all four agreeing per scope. Not by ETag movement, not by scanning for a
date-shaped string. My read matched AE's report exactly.

## I STOOD DOWN ON THE BRIDGE AND DID NOT FIRE IT

AE base sent a stand-down at 212652Z: **CTO re-routed BOTH steps to AE base at 212550Z**
(*"YOU OWN BOTH STEPS NOW... Single owner, no handoff"*).

**THE CAUSE OF MY SILENT 10-MINUTE WAIT, CONFIRMED: the bridge dispatch went to
`0.7.0_AE_CloudOps~A` at 211403Z -- and AE~A IS DEAD.** Two independent signals per CTO: no
`inbox-watch.sh` process, and **79 messages queued at the broker "received while idle."** So I was
waiting on a word sitting in a corpse's queue while AE base and I each held a correct-on-its-own-record
view of who owned the bridge.

**I complied immediately and did not nudge-then-fire.** AE was right that nudge-plus-clearance mid-run
was the live collision window: R5 would have made it largely idempotent, but it would have left two
runs' evidence for one action with `written=` unattributable.

**Sixth session-edge death today. Third to strand owned work.** Detected by CTO reading a roster --
again, no instrument.

## MY DRY-RUN WAS THE CONTROL FOR AE's REAL RUN, AND IT HELD TO THE DIGIT

`DONE written=3 skipped_existing=8 errors=3` -- identical to my 21:24:01Z prediction. AE ran its own
dry-run purely as a control and it reproduced mine exactly, which is why it fired without re-deriving.

**Landed keys (ListObjectsV2, 21:28:28-29Z):**
```
49financial/aggregate-aua-timeseries/2026-07-28.json  184,962  310e20df2266ab056a881475ba8007ac
inflection/aggregate-aua-timeseries/2026-07-28.json   147,839  2c3644be707f40760d491652eaa17191
global/aggregate-aua-timeseries/2026-07-28.json       339,838  3eccda589091f8c4f4d04640d13b06ca
```
**Those ETags ARE the md5s of my gold staging objects, digit for digit** -- single-part uploads, so
ETag == md5. **That is BYTE-IDENTITY, a stronger claim than the size match I predicted**, and it was
free from the listing. The bridge copied my artifacts verbatim; it did not re-derive.

**Positive control, SEPARATE invocation:** `cottonwood/.../2026-07-27.json` = 80,429 B, ETag
`a95153abc2e830a9bfd51344e140b1cd` -- **my repaired slice, R5-skipped and untouched.** Protected by the
guard, not by anyone remembering.

**`global account-distribution` R5-skipped and unmoved** (`00:35:17Z` / 6,968 B), so it stays at
**7,597** and tomorrow's deploy remains verifiable against `@79e9b0b456`.

## AE CORRECTED AN INSTRUMENT OF MINE THAT WAS LOAD-BEARING

I told CTO and AE *"no 07-28 key exists, so R5 cannot block"* -- **established with `head-object`.**

> **`head-object` IS `s3:GetObject`. A permission failure returns 403/404 INDISTINGUISHABLE from a real
> absence.** Landing verification is LISTING-based (ListObjectsV2: key + ETag + Size) -- monolith
> acceptance law 13c, which the publisher's own docstring also states.

**It happened to be true** (the listing agrees, and my earlier `s3 ls --recursive` sweep was
listing-based) -- **but "happened to be true" is not "verified", and I had no way to tell the
difference on a claim AE was about to fire on.** Corrected: ListObjectsV2 for existence/landing,
positive control as a separate invocation, `aws s3 cp` only when I need CONTENT rather than presence.

## AE's SHARPENED FENCE -- OUR ACCEPTANCE CRITERION WAS WRONG TWICE TONIGHT

**Stripped-md5 moved on ALL FOUR scopes -- including cottonwood, whose `as_of_last` correctly did NOT
move** (its platinum grew 37,518 B -> 80,710 B because it now serves the repaired 07-27 content).

> **So a "bytes moved" acceptance would have read 4/4 = FULL SUCCESS. Cottonwood does not merely fail
> to confirm the refresh -- it MANUFACTURES a false confirmation.**

That is sharper than the reason we originally fenced it. **Second criterion defect tonight**, the first
being the publisher's `_provenance.written_at` re-stamp (which would have moved all four platinum ETags
while carrying 07-27 content, passing our ETags-moved test on stale data). **Both were criterion
defects, not execution defects, and both were caught by AE base.**

## I CORRECTED MY OWN DISCLOSURE SENTENCE -- WRONG BASELINE

I had given CTO a sentence premised on the non-model band getting **sparser** (47 interpolated -> 6
measured). **That compares to the LEGACY plane, which Andrew is not reading.** Against what he actually
saw -- platinum at **0** -- the band went from nothing to 6 measured points.

**Right about the mechanism, wrong about the baseline.** Flagged before anyone used it unchanged; the
honest frame is improvement-with-a-qualifier: *"...it is short because that is as far back as
cottonwood's custodial holdings exist -- the earlier dates are outside the data, not missing."*

## Blockers
None. Everything open is on CTO's word: the aggregator deploy (against `@79e9b0b456`), the label fix
(vocabulary settled with DE), WI-2, the retirement pair.

## Current State
- **SERVED (platinum):** cottonwood 50/6/38 with `composed_backfill` present; 49f/inflection/global at
  `as_of 2026-07-28`, `n_dates 433/433/451`, `source_keys -> 2026-07-28.json`.
- **Canonical gold tree:** three new `2026-07-28.json` aggregate-aua keys (ETags == my gold md5s);
  cottonwood 07-27 intact at `a95153ab` / 80,429 B.
- **`global account-distribution` deliberately at 7,597** -- the 292 accounts are STILL absent on the
  global tile. That is tomorrow's deploy, not a defect to repair overnight. AE told CTO the same.
- `--only` LIVE on the bridge (`cfc88b0b...`) but was NOT needed (new-date path, no clobber).
- Nothing of mine in flight. No repo writes this window.

## Next Steps
- **[1.0.0_SA_CTO]** aggregator deploy vs the pre-stated acceptance `@79e9b0b456` (expect 7,890 /
  $1,675,987,041.89, delta 292 / $125,894,245; **falsifier: a post-deploy 7,598 means the deploy did
  not take**); the label fix word; the 7,553 definitions question; his blackdiamond two-day-gap lead;
  and the wording Andrew gets.
- **[0.4.0_DS_ClientPlatform~A]** (me): execute the label fix on his word; read the remaining ~70 lines
  of the aggregator diff if that deploy routes to me.
- **[0.4.0_DE_ClientPlatform]** render steps 1-2 (band guard + carry `pointClass` through `:1323-1331`),
  which flip the 32 dates from (A) to (B).
- **[0.0.0_AB_MSTR / 1.0.0_SA_CTO]** `0.7.0_AE_CloudOps~A` is dead with **79 queued** -- two messages of
  mine are in it (181718Z condition-4 confirmation, 184530Z `--only` briefing). Content already relayed
  to AE base, so nothing of mine is stranded, but the queue is not mine to drain.

## Compiler Tools
**None run this window, and the reason is specific rather than an omission:** every question was
per-field artifact content (`as_of_last` / `dates[-1]` / `n_dates` / `_provenance.source_keys`) and
object landing. `comp-freshness` answers *is this stale against a threshold*, not *did `as_of` advance
to a named date with matching `source_keys`* -- a different predicate. And **AE's 13c correction points
at the estate's own named acceptance instrument, `ListObjectsV2`**, which is raw by design: landing
verification is deliberately listing-based because `head-object` cannot distinguish absence from a
permission failure.

**Carried gaps, unchanged** (both filed 2026-07-29, both still worth building): `comp-pipescript
deployed` should compare CONTENT not raw bytes (CRLF false-STALE) and should ERROR on an unresolvable
bare basename instead of silently defaulting to the bd tree.

**Process note:** per the 2026-07-29 Andrew-direct retirement, no append to
`org/compiler-tools-log.md` -- this section is the record.
