# PROPOSED — CLAUDE.md NEVER#1 amendment (trading-calendar rule), measured by exercise

**Status: PROPOSAL. NOT LANDED. Andrew's word required** — this edits the first NEVER rule.
**Author:** `1.0.0_SA_CTO~Z`. **Evidence:** `runs/freshness-deploy-verdict-tools/20260811T2020Z/`
CERTIFIED @1dea476ca5 (0.8.0_AE_CloudComp~Z author, 3.0.0_SA_CVO~Z certifier) — the first time the
rule's mechanism has been exercised rather than cited.

## What the rule says today, and what is measured

> *"a `comp-freshness` entry without `freshness_basis: trading-day-frontier` silently falls back to
> flat-hours and WILL false-alarm every Monday — so the instrument's own verdict is not a second
> opinion, it is the same error."*

**THREE-WAY SPLIT, exercised:**

| limb | verdict | measured |
|---|---|---|
| the SILENT flat-hours fallback | **STALE — repaired** | a trading-keyed entry without basis now routes frontier (calendar present) or issues a LOUD `UNVERIFIABLE-BASIS` refusal (absent). **Never silent flat.** Friday-fresh on a Monday frame scores PASS, `tdb=1`, on the real calendar. |
| the repair's INFERENCE guard | **STRUCTURALLY DEAD** | its haystack keys (`s3_prefix/s3_key/prefix/key/id/label`) match **0 of 60** live config entries (real schema: `artifact_id`/`s3_key_prefix`); **its own self-test uses fixture keys, so it can never see this.** Today's Monday-safety is carried by **22/60 explicit declarations — discipline, not the guard.** |
| the EXPOSURE | **CURRENT, one channel over** | **12 of 60** entries are trading-content-by-name, undeclared, and **all on mtime mode — pure flat-hours**, with "business-daily" existing only as a display label. A weekend-skipping daily producer reads **~66h on a Monday against fail=48h**: the 77h incident's exact shape, live. |

**Net: the rule is WRONG ABOUT THE MECHANISM and RIGHT ABOUT THE EXPOSURE, for a reason it does not
name.** Only the battery could have found that; no reading of the clause reaches the mtime channel.

## Proposed replacement for the mechanism sentence (the rest of NEVER#1 unchanged)

> **Mechanism, measured 2026-08-11 (`runs/freshness-deploy-verdict-tools/20260811T2020Z`, certified):
> the silent flat-hours fallback is REPAIRED — an undeclared trading-keyed entry now routes
> trading-day-frontier or refuses LOUDLY (`UNVERIFIABLE-BASIS`), never silently flat. THE EXPOSURE
> SURVIVES ON A DIFFERENT CHANNEL: 12 of 60 entries are trading-content-by-name, undeclared, and sit
> on `mtime` mode, which is FLAT-HOURS with "business-daily" as a display label only — a
> weekend-skipping daily producer reads ~66h on a Monday against a 48h fail threshold. AND THE
> REPAIR'S OWN INFERENCE GUARD IS DEAD ON THE LIVE SCHEMA (haystack keys match 0 of 60 real entries;
> its self-test uses fixture keys and structurally cannot see this), so today's safety rests on 22
> of 60 EXPLICIT DECLARATIONS — discipline, not mechanism. THEREFORE THE REASONING DEFAULT IS
> UNCHANGED AND LOAD-BEARING: resolve the calendar first, count in trading days, and never read a
> freshness verdict as a second opinion.**

## The residual needs a RULING, three options (Andrew's; no rec is free of cost)

1. **DECLARE THE 12** — add `freshness_basis` to the undeclared trading entries. Cheapest, closes
   the exposure now, leaves the dead guard dead (discipline forever).
2. **WEEKEND-AWARE mtime THRESHOLDS** — make mtime mode calendar-aware. Closes the class, not just
   the instances; more engineering, and it changes a verdict path in use.
3. **RULE THE SEMANTICS EXPLICITLY** — "mtime freshness is WRITE-RECENCY; weekend FAILs on mtime
   entries are accepted noise." Zero engineering, and it makes the false-alarm a KNOWN property
   instead of a defect — but it accepts recurring Monday noise on 12 entries, and noise is what
   trains readers to ignore instruments.

**⚠ The guard is a separate item either way:** a self-test that exercises a guard against the world
it was written for rather than the world it runs in is a control that could not have said otherwise.
Fixing the haystack is small; leaving it dead while believing it live is the hazard.

**Timing: no Monday for six days.** Nothing here is urgent; it is proposed now because the
measurement exists now.
