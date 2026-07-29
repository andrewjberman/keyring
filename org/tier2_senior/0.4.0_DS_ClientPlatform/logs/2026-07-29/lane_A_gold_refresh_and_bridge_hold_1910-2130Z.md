# Session log — 0.4.0_DS_ClientPlatform~A — 2026-07-29 1910Z-2130Z (gold refresh landed; bridge held)
**archetype:** MIXED
**secondary_archetypes:** DEPLOY (the refresh), DIAGNOSE, COORDINATE

**Window:** continues `lane_A_acctdist_deployed_vs_repo_AB_1645-1910Z.md`. Andrew-direct manual
gold->platinum refresh, relayed by CTO 194038Z.

## THE RESULT: GOLD IS REFRESHED TO 07-28 AND VERIFIED. PLATINUM IS NOT, BY DESIGN.

`stage_mdpf_revamp_trio.py --skip-derived`, fired 21:08:36Z, done 21:09:58Z, rc=0, all gates PASS.

```
scope         as_of_last            n_dates      new md5
49financial   2026-07-28 (was 27)   433 (432)    310e20df2266ab056a881475ba8007ac   184,962B
inflection    2026-07-28 (was 27)   433 (432)    2c3644be707f40760d491652eaa17191   147,839B
global        2026-07-28 (was 27)   451 (450)    3eccda589091f8c4f4d04640d13b06ca   339,838B
cottonwood    2026-07-27  UNCHANGED 450          (not staged by the trio; declared carry)
```

**CTO's falsifier ("if it still emits 07-27, STOP") did NOT fire.** Verified on the ARTIFACTS via
`as_of_last`, not on rc. Each upload carries the script's own fresh-GET byte-verify.

**CONTROL RUN EXPLICITLY, not assumed:** `gold/mdpf_revamp/global/account_distribution.json` =
`b429d2e8e3b1d001e1723b99b67d467f` / `00:33:17Z`, **byte-identical to the pre-run baseline I captured
before firing.** `--skip-derived` held; **7,890 was NOT hand-landed, so tomorrow's deploy stays
verifiable.**

## Three findings, in order of how much they changed the plan

### 1. "The gold producer" is NOT the file everyone would name
`dim_mdpf_aggregate_aua_timeseries.py` contains **`put_object` ZERO times** -- it is a BUILD LIBRARY,
not a writer; its only output path is a local `--out-dir`. **Running it would have been a no-op that
exits 0.** The actual staging producer is `stage_mdpf_revamp_trio.py` ("SCHEDULABLE-BY-CONSTRUCTION",
uploads the three firms with fresh-GET byte-verify).

### 2. THE FORK I REFUSED: the trio's step 3 would have landed 7,890 as a data write
Source-grounded, `stage_mdpf_revamp_trio.py`:
```
:51   ("dim_mdpf_aum_metrics.py",          ["--upload"])
:52   ("dim_mdpf_account_distribution.py", ["--firm", "global", "--upload"])
:96   rc = subprocess.call(cmd)
:127  if not args.skip_derived:
```
Invoked from `_HERE` = my repo dir, so **locally it runs the cottonwood-fold copy** and would have
staged **7,890**. I stopped and returned it to CTO rather than choose.

**CTO ruled `--skip-derived`, and his reason was sharper than mine.** Mine: "do not land undeployed
output as data." His: **"it would make tomorrow's deploy UNVERIFIABLE -- we could not distinguish 'the
deploy worked' from 'a hand-run already landed the number.' Once-only evidence spent for an hour of
earliness"** -- the same shape as an early 4c apply destroying the emitter's before-half. His
formulation is the one recorded.

### 3. NEW HAZARD: the same script produces different DATA depending on where it runs
`_HERE` resolves to the repo dir locally and to the synced deploy prefix on the runner:
```
my box        -> repo account_distribution   -> 7,890
mdpf-daily-runner -> deployed copy           -> 7,598
```
**A local hand-run of the trio is NOT equivalent to the cron, and nothing in the script says so. Both
exit 0.** This is also **why the deploy gap survived**: the scheduled trio has always run the
*deployed* aggregator, so no amount of gold refreshing could ever activate the fold. **The fix was
never one run away; it was always one DEPLOY away.** Flagged, not changed.

## AE base HELD instead of publishing -- correctly -- and the missing step was mine to name

**AE's catch:** my refresh landed in `gold/mdpf_revamp/` (STAGING); the publisher reads
`portal/gold/mdpf/` (CANONICAL), still at 07-27. Two different trees.

**AE's catch is better than it claimed:** the publisher re-stamps `_provenance.written_at` on every
write, so **all four platinum ETags would have MOVED while carrying 07-27 content.** Our agreed
"ETags moved" acceptance would have PASSED on stale data, and **the cottonwood confounder-fence we
both built would not have caught it** because inflection and 49f would have moved too. **Only the
in-artifact `as_of` check exposes that.** That is our acceptance criterion being wrong, not AE being
cautious -- reported to CTO as such.

**MY GAP:** CTO's order was step 1 gold -> step 3 publisher. **The bridge is step 2 and went unnamed
by both of us -- with my own §1 diagram of that exact chain open from this afternoon, and having
deployed `--only` onto that very script at 18:44:34Z.** AE declined to name it by inference; I named
it by ownership: **`build_portal_gold_accrual.py`**, my lane under Rule 13.

**And it is unblocked with nothing to authorize:** measured, **no `2026-07-28.json` exists under any
scope**, so the bridge writes a **NEW key** and **R5's no-clobber does not apply.** R5 on its normal
path (new date daily), not the repair path that produced `written=0` at 17:44Z.

**Dry-ran it to validate the prediction before firing** (21:24:01Z, writes nothing): PLANNED 11,
ERRORS 3, and the three NEW writes plan at **184,962 / 147,839 / 339,838 B -- digit-identical to my
md5-verified gold objects**, proving the bridge reads MY artifacts. The other 8 exist and will
R5-SKIP, **including `cottonwood/aggregate-aua-timeseries/2026-07-27.json` -- so my repaired 80,429B
slice is protected BY THE GUARD, not by anyone remembering.** Expect `written=3 skipped_existing=8
errors=3`, rc=1 from the known `aum-metrics` gap. **Judge `written=`, not rc.**

**Ruled out AE's other two candidates:** re-pointing `GOLD_ROOT` at staging would have those
underscore/date-less keys logged `UNRECOGNIZED`, dropped, and **`all_present` left TRUE -- a green run
serving nothing**; hand-promotion bypasses the R4 declared-type checks and the as-of derivation on a
client-facing tree to save ninety seconds.

## AE's cross-check is the strongest evidence in the handoff
Its platinum before-state `432/432/450/450` matches my gold "was" values on all four scopes, on the
same named field. **So platinum provably carries the exact pre-refresh gold I measured, and a
post-publish 433/433/451 is attributable to my run and nothing else.** Neither of us could have made
that claim alone -- it needed one measurement from each layer.

## THE PATTERN OF THE NIGHT: four agents, same error class, zero self-caught
AE disclosed unprompted that its first `as_of` reader was a recursive newest-date-string scan that read
`2026-07-28` **before any publish** (off `source_vintage_last`/`meta`) -- **its own test would have
passed before it did anything.**

That is the **fourth** instance tonight of an agent authoring the class it had just named:
- **CTO** read `aws s3 ls` LOCAL time as UTC while quoting that exact rule at other lanes
- **DE** collapsed *the object exists* with *the page renders it*
- **me** wrote "IS Andrew's screenshot exactly" from a single artifact
- **AE** inferred a field the artifact already carried by name

**Four for four, and every one was caught by a peer or a control -- not one by its author being
careful.** AE's fix is the general remedy: **read the field the artifact NAMES; do not pattern-match
for something that looks like the field.**

## Blockers
**ONE, evidence-cited.** The accrual-bridge run is **HELD pending CTO's word** (asked 211604Z; AE base
also holding and told so). Not assumption-blocked: it is a step his 194038Z order did not name, and
after four ownership churns today I chose one message over an unauthorized write to a client-facing
tree. **~2 minutes to execute once cleared.**

## Current State
- **Gold staging at 07-28** for 49financial / inflection / global (md5s above). Cottonwood staging
  unchanged at `a95153ab` / 80,429 B / 15:52:29Z (my composed slice).
- **Canonical tree `portal/gold/mdpf/` still at 07-27** -- the bridge has not run.
- **Platinum unchanged since 16:15:32Z**, carrying 07-27. Nothing client-visible has moved from this
  window.
- `gold/mdpf_revamp/global/account_distribution.json` deliberately at 7,597 (`b429d2e8`, `00:33:17Z`).
  **Do not "repair" it** -- AE base acknowledged and will not.
- `--only` LIVE on the bridge (`md5 cfc88b0b72d4f2a89eff0f5bf35e49ca`) but **NOT needed tonight** (new
  date, no clobber).
- Pre-stated deploy acceptance committed `@79e9b0b456`.

## Next Steps
- **[1.0.0_SA_CTO]** the bridge word (unblocks everything); the aggregator deploy tomorrow against
  `@79e9b0b456`; the label fix; the 7,553 definitions question; his blackdiamond two-day-gap lead.
- **[0.4.0_DS_ClientPlatform~A]** (me): fire the bridge on his word, verify the three 07-28 keys by
  `head-object` (not the run log), ping AE base.
- **[0.7.0_AE_CloudOps base]** publishes on my ping. Its PASS condition: inflection AND 49financial at
  `as_of_last 2026-07-28` + `n_dates 433` + `source_keys -> 07-28`; **cottonwood EXCLUDED as evidence**;
  FAIL if either clean scope is still 07-27 regardless of moved ETags.
- **[0.4.0_DE_ClientPlatform]** render steps 1-2, which flip the 32 dates from (A) to (B).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript deployed` | `dim_mdpf_aggregate_aua_timeseries.py` (FULL path) | **MATCH** | pre-run deployed-vs-repo check. Confirmed by the authoritative test too: HEAD blob md5 `374c8ba7...` == deployed ETag. **No deployed/repo ambiguity for this producer**, unlike the account-distribution one -- which is why this run needed no isolation dance. |
| `comp-surface-check` | via `safe-commit` | PASS | no critical surface. |
| `comp-pulse` (risk-reflex) | the acceptance commit | CLEAN | measured, denominator printed. |

**What worked:** the full-path form of `comp-pipescript deployed` behaved correctly again and answered
the one question that mattered before firing -- am I about to run something that differs from the
runner. Cheap, and it is the check that would have caught the account-distribution gap weeks ago had
anyone asked it.
**What failed:** nothing new this window.
**Gap found (carried, unchanged):** `comp-pipescript deployed` should compare CONTENT not raw bytes
(CRLF false-STALE) and should ERROR on an unresolvable bare basename rather than silently defaulting to
the bd tree. Both filed earlier today; both still worth building.
**Process note:** per the 2026-07-29 Andrew-direct retirement, this window does NOT append to
`org/compiler-tools-log.md` -- the Compiler Tools section lives here only.
