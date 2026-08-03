# INFLECTION_SILVER_RETRO_DEDUP -- built, then correctly HALTED -- 0.7.0_AE_CloudOps~E

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE

**Date:** 2026-08-02
**Task Order:** INFLECTION_SILVER_RETRO_DEDUP (CTO GO @3c7c759386, Andrew-direct)
**Status:** HALTED by CTO ruling (correct call) -- nothing deployed, nothing written, nothing lost.
**Retroactive note:** this entry was not written at close-of-thread; filling the gap now via `/log`
before it aged further. No new work in this entry -- it is the durable record of a session that
otherwise only existed in MCP messages.

---

## Objective

Andrew-direct: retroactively dedup `orion/inflection/silver/fact_positions` on a real primary key,
then repoint `inf-etf-ownership-daily` at the deduped silver + a per-date determination, so a
duplicate/stale partition can never again reach the rebate basis undetected.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "list the partitions and schema of opal-data-assets orion inflection silver fact_positions" | NO-MATCH (correctly reported) | no comp-tool covers monolith table schema/partition inspection; routed to rail-checked raw `aws s3api` |
| n/a | `pip install pandas_market_calendars` (local dev env) | N/A -- not a comp-tool, a dependency fix | see Postmortem below; not an estate search, exempt from the rail |

**What worked:** comp-which correctly declined rather than mis-routing when no tool fit.
**What failed:** nothing in comp-tooling; the failure was in my own environment (see Postmortem).
**Gap found:** no comp-tool for cross-partition, row-level, value-axis data comparison (freeze-rate
style). Recurred across two tasks this week (this one and ETFS_PRODUCERS_REPOINT) -- worth a future
comp-tool if the pattern recurs a third time.

---

## Work Completed

### 1. Built the dual-axis dedup instrument

`data/etfs/scripts/dedup/inflection_silver_retro_dedup.py` -- fingerprint (hash of `id` + value-bearing
columns, explicit by-name exclusion of date-echoing columns), `freeze_rate()` (id-matched fraction with
identical `currentValue`), `classify()` (DUPLICATE / SUSPECT / CLEAN). `run_full_sweep.py` (streaming
driver, rolling in-memory window, freeze_rate distribution report). `test_inflection_dedup_fingerprint.py`
(AC1 mutant reproducing CTO's own exclusion-list bug on purpose; AC2/AC3/AC4 against real local
fixtures). `finalize_and_write_sweep.py` (re-classify already-computed results against a corrected
threshold without re-downloading).

### 2. Found and corrected a real metric flaw before trusting it

~65% of the book is dormant/closed $0-value positions that trivially "match" every day regardless of
freshness -- this flooded the raw freeze_rate signal (healthy pair 66.7% vs named-defect pair 81.8%,
barely distinguishable). Excluding both-zero rows: healthy pair drops to 2.35%, defect pair rises in
relative terms to 46.68% -- ~20x separation instead of 1.2x. Verified across 4 pairs before shipping the
correction. CTO independently ratified this and specifically praised applying the correction PER-AXIS
(fingerprint/DUPLICATE axis left untouched -- zeros matter there for true-duplicate detection) rather
than globally.

### 3. Ran the full 2,287-partition history sweep, set SUSPECT_FLOOR from the real distribution

First full sweep (dry-run) completed; distribution was genuinely bimodal (0-40% smooth normal curve,
94.6% of trading days; a 14x density cliff 43->3 between [30-40%) and [40-50%); only 5/1605 days in
[40%,90%) at all). Set `SUSPECT_FLOOR = 0.40` from the cliff itself, not fitted to the named 07-16
case -- it happened to land just past the cliff. Local AC1-AC4 all passed with the justified floor.

### 4. Found and fixed a SECOND real bug before trusting the sweep's output

`pandas_market_calendars` was not installed locally; `lib/trading_calendar.py`'s hardcoded fallback
holiday table only covers 2024-2027 by design (its own header says "refresh before 2028"). Every
weekday in 2020-2023 -- real NYSE holidays included -- was silently treated as a trading day. ~26 of
the first sweep's 40 "DUPLICATE" dates were actually just market holidays (MLK Day, Presidents Day,
July 4th, Thanksgiving, Christmas...), not defects. Caught by eyeballing the raw DUPLICATE date list
before writing anything, not by trusting the aggregate counts. Installed `pandas_market_calendars`
locally, verified the fix directly (`is_trading_day()` flips correctly on the same dates), added a
local disk cache (`INFLECTION_DEDUP_CACHE_DIR`) to the driver so a second full re-run would not need
to re-download all 2,287 partitions, and re-launched the corrected sweep.

### 5. Found and closed a third, unrelated hazard while vendoring `trading_calendar.py`

The Lambda needed its own copy of `lib/trading_calendar.py` (a Lambda can only import files inside its
own deploy zip). CTO flagged the vendored copy as a last-surviving-copy hazard. Checking whether the
class already existed found it estate-wide: FOUR vendored copies total, THREE of them inside freshness/
staleness-checking Lambdas (`bd-served-vintage-alarm`, `opal-assets-absence-check`,
`schwab-bronze-freshness`), zero with any drift protection before that point -- all four byte-identical
to canonical at the time coverage was added (caught before drift, not after). Built
`.github/workflows/lib-vendored-copies-parity.yml`, a repo-internal (no AWS creds) diff check covering
all four. Hit an owned-paths gate committing it myself (`.github/workflows/*` is BASE_EXEC-only); routed
to CTO rather than bypassing. CTO (or another BASE_EXEC agent) landed it as `14ff9164c0`.

### 6. Built the lambda repoint (never deployed)

`inf-etf-ownership-daily`'s `lambda_function.py` + `inf-etf-ownership-daily.tf` rewritten to compute a
LIVE dual-axis determination per date (vendored `dedup_core.py` + `trading_calendar.py`), skip writing
a slice for DUPLICATE dates, and -- a gap found while building it -- explicitly refuse to write ANY
slice for a non-trading day at all (this source uniquely carries weekend partitions and the existing
schedule fires daily). CTO confirmed this closed a previously-unexplained "phantom weekend write"
anomaly from an earlier audit. New IAM statements drafted (never applied) scoped to
`orion/inflection/silver/fact_positions/*` and `orion/inflection/meta/dedup/*`.

---

## HALT -- what stopped it, and why it was correct

Mid-second-sweep, CTO found the mechanism: `data/inf/scripts/silver/_orion_vendor_asof.py` (sealed
2026-07-02) documents that the Orion pull targets the prior settled close by design, and the vendor
stamps it with the RUN date, not the settled date. The "duplicate" partitions are real settled T-1
market data, correctly pulled, WRONGLY LABELED -- not duplicated content. Deduping on the raw label
(what this task specced) would have discarded genuine observations and encoded a known-wrong label as
truth. The larger finding: only Orion forward-labels; 49financial and cottonwood are already on the
true settled date -- so the rebate-basis file has one partner on T-1 and two on T, a cross-partner
inconsistency independent of the dedup question.

Halted immediately on receipt (same session):
- Killed the running second sweep process (confirmed dead via `ps`).
- Confirmed `s3://opal-data-assets/orion/inflection/meta/dedup/` was EMPTY -- only dry-runs had ever
  been executed, `--write` was never passed. Nothing to un-write.
- Confirmed the deployed `inf-etf-ownership-daily` Lambda still showed the OLD env vars and OLD
  CodeSha256 (from the earlier, unrelated, already-closed scheduled-floor deploy) -- the repoint code
  was committed to nothing, built nothing, applied nothing. Zero production impact.
- Caught and corrected my own error in the same exchange: told CTO the parity workflow was "already
  committed" when it was actually sitting untracked -- corrected before it stood, rather than let a
  false claim about commit state ride into a message about what's safe vs. not-yet-landed.

CTO instruction: keep the parity workflow, the non-trading-day guard, the zero-exclusion freeze_rate
fix, and the freeze_rate instrument itself (all independently valuable; the instrument becomes the
VERIFICATION tool once the real fix -- normalize the label, then dedup on the true settled date -- is
specced). Do not start the re-spec; CTO is taking it to Andrew directly since it is now a rebate-basis
correctness question, not a producer bug.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Verified the spec's premise (S1 layer table) against live data before writing code, on this task and its predecessor | Two tasks running had already shown CTO's own detector could produce a false-clean verdict; re-verifying rather than implementing-on-trust caught the metric flaw (Item 2) and, together with CTO's own parallel check, the mechanism (the HALT) before anything shipped |
| Added a local disk cache to the sweep driver after the first full run, before running it again | A second ~25min full-history download was avoidable; cheap to add, and it turned out to matter (a third full run was never needed only because the halt landed first, but the cache would have paid for itself either way) |
| Did not bypass the `.github/workflows/*` owned-paths gate | A real ownership boundary, not a bug -- routed to CTO instead of finding a workaround |
| Did not silently let the "already committed" misstatement stand | Corrected it in the same exchange, before CTO acted on the (wrong) belief that it was safely landed |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/etfs/scripts/dedup/inflection_silver_retro_dedup.py` | Fingerprint/freeze_rate/classify/sweep driver | No -- local only, per HALT |
| `data/etfs/scripts/dedup/test_inflection_dedup_fingerprint.py` | AC1-AC4 local fixture tests | No -- local only |
| `data/etfs/scripts/dedup/run_full_sweep.py` | Full-history sweep driver + disk cache | No -- local only |
| `data/etfs/scripts/dedup/finalize_and_write_sweep.py` | Re-classify without re-download | No -- local only |
| `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py` | Dedup-aware repoint (dual-axis determination, non-trading-day guard) | No -- working-tree modified, uncommitted, per HALT |
| `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/dedup_core.py` | Vendored dedup core | No -- untracked, per HALT |
| `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/trading_calendar.py` | Vendored calendar | No -- untracked, per HALT |
| `infra/aws/terraform/inf-pipeline/inf-etf-ownership-daily.tf` | New IAM (monolith + meta/dedup) drafted | No -- working-tree modified, uncommitted, per HALT |
| `.github/workflows/lib-vendored-copies-parity.yml` | Repo-internal 4-copy parity check | **Yes -- `14ff9164c0`** (landed by a BASE_EXEC agent after I was gated out) |

---

## Blockers

None currently. The repoint work is HELD, not blocked -- it resumes only if/when CTO's re-spec
(normalize-then-dedup) lands, and that is explicitly not mine to start.

---

## Current State

`inf-etf-ownership-daily` (deployed): unchanged, running the pre-existing (pre-repoint) code, untouched
by any of this session's work. Local working tree still carries the uncommitted repoint attempt
(`lambda_function.py`, `inf-etf-ownership-daily.tf` modified; `dedup_core.py`/`trading_calendar.py`
untracked) -- deliberately left in place per CTO's "keep the instrument, it becomes verification later"
instruction, not committed, not deployed. `s3://opal-data-assets/orion/inflection/meta/dedup/` is empty.
The parity workflow (a genuinely separate, still-valid improvement) is live on `CLOUD` at `14ff9164c0`.
`ETFS_ORION_LABEL_NORMALIZATION.md` @`8f0e32a642` is the real fix's spec, owned by CTO/Andrew, not this
seat, until further instruction.

---

## Next Steps

1. **[1.0.0_SA_CTO]** Re-spec with Andrew: normalize the Orion label first, then dedup on the true
   settled date -- a legitimate dedup on a real key, unlike deduping on the raw echo.
2. **[0.7.0_AE_CloudOps~E, on a future GO only]** If/when the re-spec lands: the freeze_rate instrument
   built here becomes the VERIFICATION that normalization worked, not the fix itself -- re-read this
   log's Item 2/4 corrections before reusing it, they are load-bearing.
